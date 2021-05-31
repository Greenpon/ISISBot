from typing import List
import feedparser
import config
import discord
from discord.ext import commands
from datetime import date
from io import StringIO
from html.parser import HTMLParser

# DATE DEF
today = date.today()
d1 = today.strftime("%d/%m")
d2 = today.strftime("%d/%m/%y")


# %%

# some code from stack overflow to be able to strip html tags and only get the needed values insede
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

        # reads all ISIS-Bot Ankündigungen Forum
        # list all topics and their messages in discord embed
        # reacts to !show_forum
        # Author: Lennart
        # note: The implementation of the forum_output array should be changed to a key/value pair object (oder wie man das auch nennt)
        @client.command()
        async def show_forum(ctx):
            if ctx.channel.name == "bot-test":

                # The personal key of the moodle User has (for now) be added to the RSS-URL
                # (insert yours for the URL to work)
                personal_key = config.key
                feed = feedparser.parse(
                    f'https://isis.tu-berlin.de/rss/file.php/1970720/{personal_key}/mod_forum/64807/rss.xml')

                entries = feed['entries']

                # forum_output is list of Strings, that contain title, Author and message
                forum_output = []

                # has to be changed to key/value pairs, I was to lazy to do that
                for i in entries:
                    title = i['title']
                    author = strip_tags(i.summary).replace(u'\xa0', u'').split(".")[0]
                    message = strip_tags(i.summary).replace(u'\xa0', u'').split(".")[1]
                    forum_output.append([title, author, message])

                forum_embed = discord.Embed(title="Alles aus diesem Forum", color=0x990000)
                forum_embed.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                for j in forum_output:
                    forum_embed.add_field(name=j[0], value=j[1] + "\n" + "```" + j[2] + "```", inline=False)
                forum_embed.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=forum_embed)


def setup(client):
    client.add_cog(ShowForum(client))