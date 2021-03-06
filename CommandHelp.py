import discord
from discord.ext import commands
from datetime import date
import bot

class CommandHelp(commands.Cog):
    def __init__(self, client):
        self.client = client

        # Create a Help-Command which shows all available commands
        # reacts to !helpme, !help, !command and !commands
        # Author: Sven
        @client.command(aliases=["help", "command", "commands"])
        async def helpme(ctx):
            if ctx.channel.name == "bot-test":
                hilfe = discord.Embed(title="Commands", color=0x990000)
                hilfe.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                hilfe.add_field(name="!start", value="- starts the bot \n - asks security question \n - creates filter lists", inline=False)
                hilfe.add_field(name="!new_feed", value="adds a new feed that the bot will listen to\n(e.g. !new_feed <Course ID> <Forum ID>) \n see Documentation for infos on where to find these IDs.", inline=False)
                hilfe.add_field(name="!remove_feed", value="removes feed, called just like the !new_feed command", inline=False)
                hilfe.add_field(name="!add_b / !remove_b", value="adds or removes given entry to/from blacklist")
                hilfe.add_field(name="!add_k / !remove_k", value="adds or removes given entry to/from keyword list")
                hilfe.add_field(name="!show / !show_b / !show_k", value="sends the current state of all of your filter lists to your personal chat", inline=False)
                hilfe.add_field(name="!set_interval_to", value="followed by a number and a unit (h, min, sec), you can adjust the frequency the bot checks for new forum entries \n (e.g. !set_interval_to 30 min)", inline=False)
                hilfe.add_field(name="!shutdown", value="shuts down the bot", inline=False)
                hilfe.set_footer(text="ISIS Bot v0.1 • " + date.today().strftime("%d/%m/%y"), icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=hilfe, delete_after=30.0)


def setup(client):
    client.add_cog(CommandHelp(client))
