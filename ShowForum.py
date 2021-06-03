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

        # reads all ISIS-Bot Ankündigungen Forum
        # list all topics and their messages in discord embed
        # reacts to !show_forum
        # Author: Lennart
        @client.command()
        async def show_forum(ctx):
            if ctx.channel.name == "bot-test":

                # The personal key of the moodle User has (for now) be added to the RSS-URL
                # (insert yours for the URL to work)
                personal_key = config.key
                feed = feedparser.parse(
                    f'https://isis.tu-berlin.de/rss/file.php/1970720/{personal_key}/mod_forum/64807/rss.xml')

                entries = feed['entries']

                # forum_output is list of key/value pairs that contain title and message
                forum_output = []
                for i in entries:
                    temp = {'title': i['title'], 'message': strip_tags(i.summary).replace(u'\xa0', u'').split(".")[1]}
                    forum_output.append(temp)

                forum_embed = discord.Embed(title="Alles aus diesem Forum", color=0x990000)
                forum_embed.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                for j in forum_output:
                    forum_embed.add_field(name=j.get('title'), value="```" + j.get('message') + "```", inline=False)
                forum_embed.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=forum_embed)


def setup(client):
    client.add_cog(ShowForum(client))