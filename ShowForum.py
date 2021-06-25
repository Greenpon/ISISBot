import feedparser
import config
import discord
import asyncio
from discord.ext import commands
from datetime import date
from io import StringIO
from html.parser import HTMLParser

import config
import rss
import Filtering

# DATE DEF
today = date.today()
d1 = today.strftime("%d/%m")
d2 = today.strftime("%d/%m/%y")

#Key-Value Pairs for the Feed, so the user can set multiple Feeds at once
#Structure {Course.id : Forum.id}
rssdata = {}

def get_RSSData():
    return rssdata

# strip html tags and only get the needed values inside
class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


intervalTime = 10


class ShowForum(commands.Cog):
    def __init__(self, client):
        self.client = client

        # listens to the rss-feed and refreshes it permanently
        # posts new entries from the rss-feed after receiving them
        # @initial startup wont post entries from the past
        # posts one notification for each user in the Filtering-Lists
        # checks the blacklist and keywords. If the post contains anything from the blacklist it will not be posted
        # If the post contains anything from the keyword list the text will be bold and in a different colour
        # If there a no Filterlists it will just post the Notifications without modification
        # Author: Sven & Lennart
        async def listen(ctx):
            Listening = True
            IDsUsed = []

            while (Listening):
                if not rssdata:
                    Listening = False
                else:
                    for entry in get_RSSData():
                        course_id = int(entry)
                        forum_id = int(rssdata.get(course_id))
                        feed = rss.refreshFeed(course_id, forum_id)
                        feed.reverse()

                        for entry_in_feed in feed:
                            if entry_in_feed.id in IDsUsed:
                                continue
                            else:
                                IDsUsed.append(entry_in_feed.id)
                                if entry_in_feed.published_parsed.tm_year < today.year or \
                                        (
                                                entry_in_feed.published_parsed.tm_year == today.year and entry_in_feed.published_parsed.tm_mon < today.month) or \
                                        (
                                                entry_in_feed.published_parsed.tm_mon == today.month and entry_in_feed.published_parsed.tm_mday < today.day):
                                    continue
                                else:
                                    author = strip_tags(entry_in_feed.summary).replace(u'\xa0', u'').split(".")[0]
                                    message = strip_tags(entry_in_feed.summary).replace(u'\xa0', u'').split(".")[1]

                                    users = Filtering.getUsers()
                                    if not users:
                                        noti = discord.Embed(color=0x990000)
                                        noti.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                                        noti.add_field(name=entry_in_feed.title + " " + author,
                                                       value="```" + message + "```" + "\n" + entry_in_feed.published + "\n" + "[Direktlink]({})".format(
                                                           entry_in_feed.link), inline=False)
                                        noti.set_footer(text="ISIS Bot v0.1 • " + d2,
                                                        icon_url="https://i.imgur.com/s8Ni2X1.png")

                                        await ctx.send(embed=noti)
                                    else:
                                        for user in users:
                                            pairs = Filtering.getPairs()
                                            blist = Filtering.getBlacklist()

                                            post = True

                                            for x in blist[pairs.get(user)]:
                                                if x in entry_in_feed.title or x in author or x in message:
                                                    post = False

                                            if post:
                                                klist = Filtering.getKeywordlist()

                                                mark = False

                                                for x in klist[pairs.get(user)]:
                                                    if x in entry_in_feed.title or x in author or x in message:
                                                        mark = True

                                                if mark:
                                                    await ctx.send("Neue Benachrichtigung für <@{}>".format(user))
                                                    noti = discord.Embed(color=0x990000)
                                                    noti.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                                                    noti.add_field(name=entry_in_feed.title + " " + author,
                                                                   value="```yaml\n**" + message + "**```" + "\n" + entry_in_feed.published + "\n" + "[Direktlink]({})".format(
                                                                       entry_in_feed.link), inline=False)
                                                    noti.set_footer(text="ISIS Bot v0.1 • " + d2,
                                                                    icon_url="https://i.imgur.com/s8Ni2X1.png")

                                                    await ctx.send(embed=noti)

                                                else:
                                                    await ctx.send("Neue Benachrichtigung für <@{}>".format(user))
                                                    noti = discord.Embed(color=0x990000)
                                                    noti.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                                                    noti.add_field(name=entry_in_feed.title + " " + author,
                                                                   value="```" + message + "```" + "\n" + entry_in_feed.published + "\n" + "[Direktlink]({})".format(
                                                                       entry_in_feed.link), inline=False)
                                                    noti.set_footer(text="ISIS Bot v0.1 • " + d2,
                                                                    icon_url="https://i.imgur.com/s8Ni2X1.png")

                                                    await ctx.send(embed=noti)

                await asyncio.sleep(intervalTime)

        # Command to add a new Feed to the bot it will listen to
        # This also auto starts the listen fuction
        # Author: Sven
        @client.command()
        async def new_feed(ctx, *args):
            try:
                if len(args) != 2:
                    raise ValueError(
                        "Please give me two numbers first the ID of the Course and then the ID of the Forum.\n"
                        "e.g. https://isis.tu-berlin.de/rss/file.php/<COURSE ID>/<YOUR SECURITYKEY>/mod_forum/<FORUM ID>/rss.xml")

                course = args[0]
                forum = args[1]

                if not course.isnumeric() or forum.isnumeric():
                    raise ValueError(
                        "You provided at least one wrong input. Please provide two Integer as an input.")

                rssdata[course] = forum

                success = discord.Embed(title="", color=0x990000)
                success.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                success.add_field(name="New Feed", value="You did set up a new RSS Feed!", inline=False)
                success.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=success, delete_after=10.0)

                await listen(ctx)

            except ValueError as e:
                warn = discord.Embed(title="", color=0x990000)
                warn.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                warn.add_field(name="Wrong Input", value=e, inline=False)
                warn.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=warn, delete_after=10.0)

        # Command to add a new Feed to the bot it will listen to
        # This also auto starts the listen fuction
        # Author: Sven
        @client.command()
        async def remove_feed(ctx, *args):
            try:
                if len(args) != 2:
                    raise ValueError(
                        "Please give me two numbers first the ID of the Course and then the ID of the Forum.\n"
                        "e.g. https://isis.tu-berlin.de/rss/file.php/<COURSE ID>/<YOUR SECURITYKEY>/mod_forum/<FORUM ID>/rss.xml")

                course = args[0]
                forum = args[1]

                if not course.isnumeric() or forum.isnumeric():
                    raise ValueError(
                        "You provided at least one wrong input. Please provide two Integer as an input.")

                rssdata.pop(course, forum)

                success = discord.Embed(title="", color=0x990000)
                success.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                success.add_field(name="Removed Feed", value="You did remove a RSS Feed!", inline=False)
                success.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=success, delete_after=10.0)

            except ValueError as e:
                warn = discord.Embed(title="", color=0x990000)
                warn.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                warn.add_field(name="Wrong Input", value=e, inline=False)
                warn.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=warn, delete_after=10.0)




        # gives user the opportunity to set the refresh interval of Isi.
        # reacts to !set_interval_to <Int> <[h, min, sec]>
        # checks if enough and the right arguments are given
        # if arguments are incorrect, it displays an error message which disappears after 10 seconds
        # if arguments are correct, user will get a verification message
        #
        # CURRENTLY ONLY FOR OWNER
        # Author: Lennart
        @client.command()
        @commands.is_owner()
        async def set_interval_to(ctx, *args):
            try:
                if len(args) != 2:
                    raise ValueError(
                        "Please give a number and a unit of time [h, min or sec] for your interval (e.g. **!set_interval_to 60 min**)")

                time = args[0]
                unit = args[1]
                if not time.isnumeric():
                    raise ValueError(
                        "You provided a " + str(type(time)) + " for the time value, please provide an Integer.")
                if unit != "sec" and unit != "min" and unit != "h":
                    raise ValueError("Please provide the right unit (h, min, sec)")

                global intervalTime
                if (unit == "sec"):
                    intervalTime = int(time)
                    unit = "seconds"
                elif (unit == "min"):
                    intervalTime = int(time) * 60
                    unit = "minutes"
                elif (args[1] == "h"):
                    intervalTime = int(time) * 360
                    unit = "hours"

                changeSuccess = discord.Embed(
                    title="Isi will now check for new Forum entries every " + time + " " + unit, color=0x990000)
                if (intervalTime > 2880):
                    changeSuccess = discord.Embed(
                        title="Isi will now check for new Forum entries every " + time + " " + unit, color=0xFFD300)
                    changeSuccess.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    changeSuccess.add_field(
                        name="Warning", value="You have set your bot to check for forum entries less than three times a day. Due to restrictions by moodle and the RSS feed, Isi can only recieve the latest ten entries. \n \n If the forum Isi is listening to has a lot of traffic, you might miss out on some of the entries.", inline=False)
                changeSuccess.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")
                await ctx.send(embed=changeSuccess)

            except ValueError as e:
                warn = discord.Embed(title="", color=0x990000)
                warn.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                warn.add_field(name="Wrong Input", value=e, inline=False)
                warn.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=warn, delete_after=10.0)


def setup(client):
    client.add_cog(ShowForum(client))
