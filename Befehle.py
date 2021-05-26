import discord
from discord.ext import commands
from datetime import date

#DATE DEF
today = date.today()
d1 = today.strftime("%d/%m")
d2 = today.strftime("%d/%m/%y")


class Befehle(commands.Cog):
    def __init__(self, client):
        self.client = client

        # Create a Help-Command which shows all available commands
        # reacts to !helpme, !help, !command and !commands
        # Author: Sven
        @client.command(aliases=["help", "command", "commands"])
        async def helpme(ctx):
            if ctx.channel.name == "bot-test":
                hilfe = discord.Embed(title="Befehle", color=0x990000)
                hilfe.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                hilfe.add_field(name="Hier sind alle Befehle die ich kenne:",
                                value="Kommt noch :)",
                                inline=False)
                hilfe.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=hilfe)


def setup(client):
    client.add_cog(Befehle(client))