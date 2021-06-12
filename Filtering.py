import discord
from discord.ext import commands
import bot

#Import from bot
import config

today = bot.today
d1 = bot.d1
d2 = bot.d2

# Storing the channel id
channel_id = []

# Each user id gets added into this list in the create section
user = []
# Simple function to return all user ids in a list
def users():
    return user

# Create a whitelist
wlist = []
def getWhitelist():
    return wlist

# Create a blacklist
blist = []
def getBlacklist():
    return blist

# Create a Keywordlist
klist = []
def getKeywordlist():
    return klist

# Create a space for key value pairs
pairs = {}
def getPairs():
    return pairs

class Filtering(commands.Cog):
    def __init__(self, client):
        self.client = client

        # Add Function for whitelists
        # reacts to !add_w 'Test' and adds Test to the whitelist
        # checks if the user already has a whitelist
        # Author: Sven
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
                    createfirst = discord.Embed(title="Filterlisten", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="Du besitzt noch keine Filterlisten",
                                  value="Mit !create erstellen",
                                  inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=createfirst)

        # Remove Function for whitelists
        # reacts to !remove_w 'Test' and removes Test from the whitelist
        # Ignors the ValueError if 'Test' is not in whitelist (=nothing happens)
        # checks if the user already has a whitelist
        # Author: Sven
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
                    createfirst = discord.Embed(title="Filterlisten", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="Du besitzt noch keine Filterlisten",
                                          value="Mit !create erstellen",
                                          inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=createfirst)

        # Add Function for blacklists
        # reacts to !add_b 'Test' and adds Test to the blacklist
        # checks if the user already has a blacklist
        # Author: Sven
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
                    createfirst = discord.Embed(title="Filterlisten", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="Du besitzt noch keine Filterlisten",
                                          value="Mit !create erstellen",
                                          inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=createfirst)

        # Remove Function for blacklists
        # reacts to !remove_b 'Test' and removes Test from the blacklist
        # Ignors the ValueError if 'Test' is not in blacklist (=nothing happens)
        # checks if the user already has a blacklist
        # Author: Sven
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
                    createfirst = discord.Embed(title="Filterlisten", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="Du besitzt noch keine Filterlisten",
                                          value="Mit !create erstellen",
                                          inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=createfirst)

        # Add Function for Keywords
        # reacts to !add_k 'Test' and adds Test to Keywords
        # checks if the user already has a Keywordlist
        # Author: Sven
        @client.command()
        async def add_k(ctx, message):
            if ctx.channel.name == "bot-test":
                if ctx.author.id in pairs:
                    klist[pairs.get(ctx.author.id)].append(message)

                    keyword = discord.Embed(title="Keywords", color=0x990000)
                    keyword.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    keyword.add_field(name="Du hast folgende Keywords gesetzt:",
                                        value=klist[pairs.get(ctx.author.id)],
                                        inline=False)
                    keyword.set_footer(text="ISIS Bot v0.1 • " + d2,
                                         icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=keyword)

                else:
                    createfirst = discord.Embed(title="Filterlisten", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="Du besitzt noch keine Filterlisten",
                                          value="Mit !create erstellen",
                                          inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2,
                                           icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=createfirst)

        # Remove Function for Keywords
        # reacts to !remove_k 'Test' and removes Test from the Keywords
        # Ignors the ValueError if 'Test' is not in Keywords (=nothing happens)
        # checks if the user already has a Keywordlist
        # Author: Sven
        @client.command()
        async def remove_k(ctx, message):
            if ctx.channel.name == "bot-test":
                if ctx.author.id in pairs:
                    try:
                        klist[pairs.get(ctx.author.id)].remove(message)
                    except ValueError:
                        pass

                    keyword = discord.Embed(title="Keywords", color=0x990000)
                    keyword.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    keyword.add_field(name="Du hast folgende Keywords gesetzt:",
                                        value=klist[pairs.get(ctx.author.id)],
                                        inline=False)
                    keyword.set_footer(text="ISIS Bot v0.1 • " + d2,
                                        icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=keyword)

                else:
                    createfirst = discord.Embed(title="Filterlisten", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="Du besitzt noch keine Filterlisten",
                                          value="Mit !create erstellen",
                                          inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2,
                                           icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=createfirst)

        # Shows current Filterlisten
        # reacts to !show to show all lists but also reacts to !show_w , !show_b and !show_k
        # these will only show one of the three lists. (if only !show is used it will show all)
        # Checks which command is used
        # Checks if the user already has Filterlisten
        # Author: Sven
        @client.command(aliases=["show_w", "show_b", "show_k"])
        async def show(ctx):
            if ctx.channel.name == "bot-test":
                if ctx.author.id in pairs:
                    current = discord.Embed(title="Filterlisten", color=0x990000)
                    current.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")

                    if ctx.invoked_with.lower() == "show_w":
                        current.add_field(name="Die Whitelist enthällt aktuell:",
                                          value=wlist[pairs.get(ctx.author.id)],
                                          inline=False)
                    elif ctx.invoked_with.lower() == "show_b":
                        current.add_field(name="Die Blacklist enthällt aktuell:",
                                          value=blist[pairs.get(ctx.author.id)],
                                          inline=False)
                    elif ctx.invoked_with.lower() == "show_k":
                        current.add_field(name="Du hast folgende Keywords gesetzt:",
                                          value=klist[pairs.get(ctx.author.id)],
                                          inline=False)
                    else:
                        current.add_field(name="Die Whitelist enthällt aktuell:",
                                          value=wlist[pairs.get(ctx.author.id)],
                                          inline=False)
                        current.add_field(name="Die Blacklist enthällt aktuell:",
                                          value=blist[pairs.get(ctx.author.id)],
                                          inline=False)
                        current.add_field(name="Du hast folgende Keywords gesetzt:",
                                          value=klist[pairs.get(ctx.author.id)],
                                          inline=False)

                    current.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=current)

                else:
                    createfirst = discord.Embed(title="Filterlisten", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="Du besitzt noch keine Filterlisten",
                                          value="Mit !create erstellen",
                                          inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.send(embed=createfirst)

        # waits for Reacts to the Datenschutz message
        # Maybe still have to implement the id of the Datenschutz message(It only tracks the channel atm)
        # CREATE USER LISTS AFTER REACTING
        # If its the initial post it will also set the channel id
        # It also removes the reaction after creating or removing the user
        # Author Sven
        @client.event
        async def on_raw_reaction_add(payload):
            if not channel_id:
                channel_id.append(payload.channel_id)
            if payload.user_id not in config.Bot_Id:
                if payload.channel_id == channel_id[0]:
                    if payload.emoji.name == '✅':
                        await create(payload.user_id)
                        channel = client.get_channel(payload.channel_id)
                        message = await channel.fetch_message(payload.message_id)
                        await message.remove_reaction(payload.emoji, payload.member)
                    elif payload.emoji.name == '❌':
                        await remove(payload.user_id)
                        channel = client.get_channel(payload.channel_id)
                        message = await channel.fetch_message(payload.message_id)
                        await message.remove_reaction(payload.emoji, payload.member)


        # Creates the lists for Whitelist, Blacklist and Keywords
        # Gives the user a key-value pair so each user has own lists
        # checks if the user already has lists
        # Author: Sven
        async def create(id):
            ctx = client.get_channel(channel_id[0])
            if id not in pairs:
                pairs[id] = len(wlist)
                user.append(id)

                wlist.append([])
                blist.append([])
                klist.append([])

                create = discord.Embed(title="Filterlisten", color=0x990000)
                create.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                create.add_field(name="Du hast dem Datenschutz zugestimmt und s wurden Filterlisten erstellt",
                                value="Mit !add_w Sachen zur Whitelist hinzufügen. "
                                        "Mit !add_b Sachen zur Blacklist hinzufügen. "
                                        "Mit !add_k Sachen zu den Keywords hinzufügen. "
                                        "Beispiel: !add_w 'Test' fügt 'Test' zur Whitelist hinzu.",
                                        inline=False)
                create.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=create)

            elif id not in user:
                user.append(id)

                create = discord.Embed(title="Filterlisten", color=0x990000)
                create.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                create.add_field(name="Du hast dem Datenschutz zugestimmt und s wurden Filterlisten erstellt",
                                 value="Mit !add_w Sachen zur Whitelist hinzufügen. "
                                       "Mit !add_b Sachen zur Blacklist hinzufügen. "
                                       "Mit !add_k Sachen zu den Keywords hinzufügen. "
                                       "Beispiel: !add_w 'Test' fügt 'Test' zur Whitelist hinzu.",
                                 inline=False)
                create.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=create)

            else:
                create = discord.Embed(title="Datenschutz", color=0x990000)
                create.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                create.add_field(name="Du hast dem Datenschutz bereits zugestimmt!",
                                value="Nun kannst du mit !add_w Sachen zur Whitelist hinzufügen. Mit !add_b kannst du Sachen zur Blacklist "
                                        "hinzufügen. Außerdem kannst du mit !remove_w und remove_b Sachen entfernen. "
                                        "Beispiel: !add_w Test",
                                    inline=False)
                create.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=create)

        # Same as create but remove
        # Author: Sven
        async def remove(id):
            ctx = client.get_channel(channel_id[0])
            if id in user:

                user.remove(id)

                remove = discord.Embed(title="Datenschutz", color=0x990000)
                remove.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                remove.add_field(name="Du stimmst dem Datenschutz jetzt nicht mehr zu!",
                                 value=" ",
                                 inline=False)
                remove.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=remove)

            else:
                remove = discord.Embed(title="Datenschutz", color=0x990000)
                remove.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                remove.add_field(name="Du hattest dem Datenschutz nicht zugestimmt!",
                                 value=" ",
                                 inline=False)
                remove.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await ctx.send(embed=remove)

def setup(client):
    client.add_cog(Filtering(client))
