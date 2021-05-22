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
                if ctx.author.id in pairs:
                    wlist[pairs.get(ctx.author.id)].append(message)

                    whitelist = discord.Embed(title="Whitelist", color=0x990000)
                    whitelist.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    whitelist.add_field(name="Die Whitelist enthällt nun:",
                                        value=wlist[pairs.get(ctx.author.id)],
                                        inline=False)
                    whitelist.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=whitelist)

                else:
                    createfirst = discord.Embed(title="Whitelist und Blacklist", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="Du besitzt noch keine Whitelist und Blacklist",
                                  value="Mit !create erstellen",
                                  inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=createfirst)

        @client.command()
        async def remove_w(ctx, message):
            if ctx.channel.name == "bot-test":
                if ctx.author.id in pairs:
                    try:
                        wlist[pairs.get(ctx.author.id)].remove(message)
                    except ValueError:
                        pass

                    whitelist = discord.Embed(title="Whitelist", color=0x990000)
                    whitelist.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    whitelist.add_field(name="Die Whitelist enthällt nun:",
                                        value=wlist[pairs.get(ctx.author.id)],
                                        inline=False)
                    whitelist.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=whitelist)

                else:
                    createfirst = discord.Embed(title="Whitelist und Blacklist", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="Du besitzt noch keine Whitelist und Blacklist",
                                  value="Mit !create erstellen",
                                  inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=createfirst)

        # Create a blacklist with add and remove function
        blist = []

        @client.command()
        async def add_b(ctx, message):
            if ctx.channel.name == "bot-test":
                if ctx.author.id in pairs:
                    blist[pairs.get(ctx.author.id)].append(message)

                    blacklist = discord.Embed(title="Whitelist", color=0x990000)
                    blacklist.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    blacklist.add_field(name="Die Blacklist enthällt nun:",
                                        value=blist[pairs.get(ctx.author.id)],
                                        inline=False)
                    blacklist.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=blacklist)

                else:
                    createfirst = discord.Embed(title="Whitelist und Blacklist", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="Du besitzt noch keine Whitelist und Blacklist",
                                  value="Mit !create erstellen",
                                  inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=createfirst)


        @client.command()
        async def remove_b(ctx, message):
            if ctx.channel.name == "bot-test":
                if ctx.author.id in pairs:
                    try:
                        blist[pairs.get(ctx.author.id)].remove(message)
                    except ValueError:
                        pass

                    blacklist = discord.Embed(title="Whitelist", color=0x990000)
                    blacklist.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    blacklist.add_field(name="Die Blacklist enthällt nun:",
                                        value=blist[pairs.get(ctx.author.id)],
                                        inline=False)
                    blacklist.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=blacklist)

                else:
                    createfirst = discord.Embed(title="Whitelist und Blacklist", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="Du besitzt noch keine Whitelist und Blacklist",
                                  value="Mit !create erstellen",
                                  inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=createfirst)

        # Shows current Whitelist and Blacklist
        @client.command()
        async def show(ctx):
            if ctx.channel.name == "bot-test":
                if ctx.author.id in pairs:
                    current = discord.Embed(title="Whitelist und Blacklist", color=0x990000)
                    current.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    current.add_field(name="Die Whitelist enthällt aktuell:",
                                      value=wlist[pairs.get(ctx.author.id)],
                                      inline=False)
                    current.add_field(name="Die Blacklist enthällt aktuell:",
                                      value=blist[pairs.get(ctx.author.id)],
                                      inline=False)
                    current.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=current)

                else:
                    createfirst = discord.Embed(title="Whitelist und Blacklist", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="Du besitzt noch keine Whitelist und Blacklist",
                                  value="Mit !create erstellen",
                                  inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=createfirst)


        # Create a List space in Whitelist and Blacklist for the user with key value pairs
        pairs = {}

        @client.command()
        async def create(ctx):
            if ctx.channel.name == "bot-test":
                if ctx.author.id not in pairs:
                    pairs[ctx.author.id] = len(wlist)

                wlist.append([])
                blist.append([])

                create = discord.Embed(title="Whitelist und Blacklist", color=0x990000)
                create.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                create.add_field(name="Es wurde eine Whitelist und Blacklist erstellt.",
                                 value="Nun kannst du mit !add_w Sachen zur Whitelist hinzufügen. Mit !add_b kannst du Sachen zur Blacklist "
                                       "hinzufügen. Außerdem kannst du mit !remove_b und remove_w Sachen entfernen. "
                                       "Beispiel: !add_b Test",
                                    inline=False)
                create.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=create)



def setup(client):
    client.add_cog(Filtering(client))