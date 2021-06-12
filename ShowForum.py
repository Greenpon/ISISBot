import feedparser
import config
import discord
from discord.ext import commands
from datetime import date
from io import StringIO
from html.parser import HTMLParser
import rss
import Filtering

# DATE DEF
today = date.today()
d1 = today.strftime("%d/%m")
d2 = today.strftime("%d/%m/%y")


# %%

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


# %%

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
        @client.command()
        async def listen(ctx):
            if ctx.channel.name == "bot-test":

                IDsUsed = []

                feed = rss.refreshFeed()
                feed.reverse()


                while (True):

                    for entry_in_feed in feed:
                        if entry_in_feed.id in IDsUsed:
                            continue
                        else:
                            IDsUsed.append(entry_in_feed.id)
                            if entry_in_feed.published_parsed.tm_year < today.year or \
                                    (entry_in_feed.published_parsed.tm_year == today.year and entry_in_feed.published_parsed.tm_mon < today.month) or \
                                     (entry_in_feed.published_parsed.tm_mon == today.month and entry_in_feed.published_parsed.tm_mday < today.day):
                                continue
                            else:
                                author = strip_tags(entry_in_feed.summary).replace(u'\xa0', u'').split(".")[0]
                                message = strip_tags(entry_in_feed.summary).replace(u'\xa0', u'').split(".")[1]

                                users = Filtering.users()
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
                                                                value="```" + message + "```" + "\n" + entry_in_feed.published + "\n" + "[Direktlink]({})".format(entry_in_feed.link), inline=False)
                                                noti.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                                                await ctx.send(embed=noti)

                    await asyncio.sleep(10)
                    feed = rss.refreshFeed()


def setup(client):
    client.add_cog(ShowForum(client))