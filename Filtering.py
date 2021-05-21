import discord
from discord.ext import commands
from datetime import date

# DATE DEF
today = date.today()
d1 = today.strftime("%d/%m")
d2 = today.strftime("%d/%m/%y")


class Filtering(commands.Cog):
    def __init__(self, client):
        self.client = client

        # Create a whitelist with add and remove function
        wlist = []

        @client.command()
        async def add_w(ctx, message):
            if ctx.channel.name == "bot-test":
                wlist[ctx.author.id].extend(message)

                whitelist = discord.Embed(title="Whitelist", color=0x990000)
                whitelist.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                whitelist.add_field(name="Die Whitelist enthällt nun:",
                                    value=wlist[ctx.author.id],
                                    inline=False)
                whitelist.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=whitelist)

        @client.command()
        async def remove_w(ctx, message):
            if ctx.channel.name == "bot-test":
                wlist[ctx.author.id].remove(message)

                whitelist = discord.Embed(title="Whitelist", color=0x990000)
                whitelist.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                whitelist.add_field(name="Die Whitelist enthällt nun:",
                                    value=wlist[ctx.author.id],
                                    inline=False)
                whitelist.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=whitelist)

        # Create a blacklist with add and remove function
        blist = []

        @client.command()
        async def add_b(ctx, message):
            if ctx.channel.name == "bot-test":
                blist[ctx.author.id].extend(message)

                blacklist = discord.Embed(title="Whitelist", color=0x990000)
                blacklist.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                blacklist.add_field(name="Die Blacklist enthällt nun:",
                                    value=blist[ctx.author.id],
                                    inline=False)
                blacklist.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=blacklist)

        @client.command()
        async def remove_b(ctx, message):
            if ctx.channel.name == "bot-test":
                blist[ctx.author.id].remove(message)

                blacklist = discord.Embed(title="Whitelist", color=0x990000)
                blacklist.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                blacklist.add_field(name="Die Blacklist enthällt nun:",
                                    value=blist[ctx.author.id],
                                    inline=False)
                blacklist.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=blacklist)

        # Shows current Whitelist and Blacklist
        @client.command()
        async def show(ctx):
            if ctx.channel.name == "bot-test":
                current = discord.Embed(title="Whitelist und Blacklist", color=0x990000)
                current.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                current.add_field(name="Die Whitelist enthällt aktuell:",
                                  value=wlist[ctx.author.id],
                                  inline=False)
                current.add_field(name="Die Blacklist enthällt aktuell:",
                                  value=blist[ctx.author.id],
                                  inline=False)
                current.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=current)



def setup(client):
    client.add_cog(Filtering(client))