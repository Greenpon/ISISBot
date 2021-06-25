import discord
from discord.ext import commands
import bot
import ShowForum

#Import from bot
import config

today = bot.today
d1 = bot.d1
d2 = bot.d2

# Storing the channel id
channel_id = []
post_id = []

# Each user id gets added into this list in the create section
user = []
# Simple function to return all user ids in a list
def getUsers():
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
            if ctx.channel.id in channel_id:
                if ctx.author.id in pairs:
                    wlist[pairs.get(ctx.author.id)].append(message)

                    whitelist = discord.Embed(title="Whitelist", color=0x990000)
                    whitelist.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    whitelist.add_field(name="Your Whitelist now contains:",
                                        value=wlist[pairs.get(ctx.author.id)],
                                        inline=False)
                    whitelist.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.author.send(embed=whitelist)

                else:
                    createfirst = discord.Embed(title="Filter Lists", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="No filter lists yet!",
                                  value="Filter lists will be created automatically after you have read the data security notice and agreed by reacting with the green checkmark emoji.",
                                  inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.author.send(embed=createfirst)

        # Remove Function for whitelists
        # reacts to !remove_w 'Test' and removes Test from the whitelist
        # Ignors the ValueError if 'Test' is not in whitelist (=nothing happens)
        # checks if the user already has a whitelist
        # Author: Sven
        @client.command()
        async def remove_w(ctx, message):
            if ctx.channel.id in channel_id:
                if ctx.author.id in pairs:
                    try:
                        wlist[pairs.get(ctx.author.id)].remove(message)
                    except ValueError:
                        pass

                    whitelist = discord.Embed(title="Whitelist", color=0x990000)
                    whitelist.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    whitelist.add_field(name="Your Whitelist now contains:",
                                        value=wlist[pairs.get(ctx.author.id)],
                                        inline=False)
                    whitelist.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.author.send(embed=whitelist)

                else:
                    createfirst = discord.Embed(title="Filter Lists", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="No filter lists yet!",
                                          value="Filter lists will be created automatically after you have read the data security notice and agreed by reacting with the green checkmark emoji.",
                                          inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.author.send(embed=createfirst)

        # Add Function for blacklists
        # reacts to !add_b 'Test' and adds Test to the blacklist
        # checks if the user already has a blacklist
        # Author: Sven
        @client.command()
        async def add_b(ctx, message):
            if ctx.channel.id in channel_id:
                if ctx.author.id in pairs:
                    blist[pairs.get(ctx.author.id)].append(message)

                    blacklist = discord.Embed(title="Blacklist", color=0x990000)
                    blacklist.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    blacklist.add_field(name="Your Blacklist now contains:",
                                        value=blist[pairs.get(ctx.author.id)],
                                        inline=False)
                    blacklist.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.author.send(embed=blacklist)

                else:
                    createfirst = discord.Embed(title="Filter Lists", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="No filter lists yet!",
                                          value="Filter lists will be created automatically after you have read the data security notice and agreed by reacting with the green checkmark emoji.",
                                          inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.author.send(embed=createfirst)

        # Remove Function for blacklists
        # reacts to !remove_b 'Test' and removes Test from the blacklist
        # Ignors the ValueError if 'Test' is not in blacklist (=nothing happens)
        # checks if the user already has a blacklist
        # Author: Sven
        @client.command()
        async def remove_b(ctx, message):
            if ctx.channel.id in channel_id:
                if ctx.author.id in pairs:
                    try:
                        blist[pairs.get(ctx.author.id)].remove(message)
                    except ValueError:
                        pass

                    blacklist = discord.Embed(title="Blacklist", color=0x990000)
                    blacklist.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    blacklist.add_field(name="Your Blacklist now contains:",
                                        value=blist[pairs.get(ctx.author.id)],
                                        inline=False)
                    blacklist.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.author.send(embed=blacklist)

                else:
                    createfirst = discord.Embed(title="Filter Lists", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="No filter lists yet!",
                                          value="Filter lists will be created automatically after you have read the data security notice and agreed by reacting with the green checkmark emoji.",
                                          inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.author.send(embed=createfirst)

        # Add Function for Keywords
        # reacts to !add_k 'Test' and adds Test to Keywords
        # checks if the user already has a Keywordlist
        # Author: Sven
        @client.command()
        async def add_k(ctx, message):
            if ctx.channel.id in channel_id:
                if ctx.author.id in pairs:
                    klist[pairs.get(ctx.author.id)].append(message)

                    keyword = discord.Embed(title="Keyword List", color=0x990000)
                    keyword.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    keyword.add_field(name="Your Keyword list now contains:",
                                        value=klist[pairs.get(ctx.author.id)],
                                        inline=False)
                    keyword.set_footer(text="ISIS Bot v0.1 • " + d2,
                                         icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.author.send(embed=keyword)

                else:
                    createfirst = discord.Embed(title="Filter Lists", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="No filter lists yet!",
                                          value="Filter lists will be created automatically after you have read the data security notice and agreed by reacting with the green checkmark emoji.",
                                          inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2,
                                           icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.author.send(embed=createfirst)

        # Remove Function for Keywords
        # reacts to !remove_k 'Test' and removes Test from the Keywords
        # Ignors the ValueError if 'Test' is not in Keywords (=nothing happens)
        # checks if the user already has a Keywordlist
        # Author: Sven
        @client.command()
        async def remove_k(ctx, message):
            if ctx.channel.id in channel_id:
                if ctx.author.id in pairs:
                    try:
                        klist[pairs.get(ctx.author.id)].remove(message)
                    except ValueError:
                        pass

                    keyword = discord.Embed(title="Keyword List", color=0x990000)
                    keyword.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    keyword.add_field(name="Your Keyword list now contains:",
                                        value=klist[pairs.get(ctx.author.id)],
                                        inline=False)
                    keyword.set_footer(text="ISIS Bot v0.1 • " + d2,
                                        icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.author.send(embed=keyword)

                else:
                    createfirst = discord.Embed(title="Filter Lists", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="No filter lists yet!",
                                          value="Filter lists will be created automatically after you have read the data security notice and agreed by reacting with the green checkmark emoji.",
                                          inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2,
                                           icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.author.send(embed=createfirst)

        # Shows current Filterlisten
        # reacts to !show to show all lists but also reacts to !show_w , !show_b and !show_k
        # these will only show one of the three lists. (if only !show is used it will show all)
        # Checks which command is used
        # Checks if the user already has Filterlisten
        # Author: Sven
        @client.command(aliases=["show_w", "show_b", "show_k"])
        async def show(ctx):
            if ctx.channel.id in channel_id:
                if ctx.author.id in pairs:
                    current = discord.Embed(title="Filter Lists", color=0x990000)
                    current.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")

                    if ctx.invoked_with.lower() == "show_w":
                        current.add_field(name="Your Whitelist currently contains:",
                                          value=wlist[pairs.get(ctx.author.id)],
                                          inline=False)
                    elif ctx.invoked_with.lower() == "show_b":
                        current.add_field(name="Your Blacklist currently contains:",
                                          value=blist[pairs.get(ctx.author.id)],
                                          inline=False)
                    elif ctx.invoked_with.lower() == "show_k":
                        current.add_field(name="Your Keyword list currently contains:",
                                          value=klist[pairs.get(ctx.author.id)],
                                          inline=False)
                    else:
                        current.add_field(name="Your Whitelist currently contains:",
                                          value=wlist[pairs.get(ctx.author.id)],
                                          inline=False)
                        current.add_field(name="Your Blacklist currently contains:",
                                          value=blist[pairs.get(ctx.author.id)],
                                          inline=False)
                        current.add_field(name="Your Keyword list currently contains::",
                                          value=klist[pairs.get(ctx.author.id)],
                                          inline=False)

                    current.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.author.send(embed=current)

                else:
                    createfirst = discord.Embed(title="Filter lists", color=0x990000)
                    createfirst.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                    createfirst.add_field(name="No filter lists yet!",
                                          value="Filter lists will be created automatically after you have read the data security notice and agreed by reacting with the green checkmark emoji.",
                                          inline=False)
                    createfirst.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                    await ctx.author.send(embed=createfirst)

        # waits for Reacts to the Datenschutz message
        # Checks if the user reacted to the right message in the right channel
        # CREATE USER LISTS AFTER REACTING
        # If its the initial post it will also set the channel id
        # It also removes the reaction after creating or removing the user
        # Author Sven
        @client.event
        async def on_raw_reaction_add(payload):
            if not channel_id:
                channel_id.append(payload.channel_id)
            if not post_id:
                post_id.append(payload.message_id)
            if payload.user_id not in config.Bot_Id:
                if payload.channel_id in channel_id and payload.message_id in post_id:
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
            author = await client.fetch_user(id)
            if id not in pairs:
                pairs[id] = len(wlist)
                user.append(id)

                wlist.append([])
                blist.append([])
                klist.append([])

                create = discord.Embed(title="Filter lists", color=0x990000)
                create.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                create.add_field(name="You have agreed to the data security statement and Filter lists were created:",
                                value="Add entries to your Blacklist with !add_b \n"
                                      "Add entries to your Keyowrd list with !add_k \n"
                                      "Get information about you Filter lists with !show \n"
                                      "e.g. \"!add_b Klausur\" will add Klausur to your blacklist \n",
                                        inline=False)
                create.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await author.send(embed=create)


            elif id not in user:
                user.append(id)

                create = discord.Embed(title="Filter lists", color=0x990000)
                create.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                create.add_field(name="You agree to the Datenschutz again!",
                                 value="Add entries to your Blacklist with !add_b \n"
                                      "Add entries to your Keyowrd list with !add_k \n"
                                      "Get information about you Filter lists with !show \n"
                                      "e.g. \"!add_b Klausur\" will add Klausur to your blacklist \n",
                                 inline=False)
                create.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await author.send(embed=create)

            else:
                create = discord.Embed(title="Date security", color=0x990000)
                create.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                create.add_field(name="You already agreed to the data security statement!",
                                value="Add entries to your Blacklist with !add_b \n"
                                      "Add entries to your Keyowrd list with !add_k \n"
                                      "Get information about you Filter lists with !show \n"
                                      "e.g. \"!add_b Klausur\" will add Klausur to your blacklist \n",
                                inline=False)
                create.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await author.send(embed=create)

        # Same as create but remove
        # Author: Sven
        async def remove(id):
            author = await client.fetch_user(id)
            if id in user:

                user.remove(id)

                remove = discord.Embed(title="Data security", color=0x990000)
                remove.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                remove.add_field(name="You don't agree to the data security statement anymore!",
                                 value="Your filter lists will be saved for if you ever change your mind.",
                                 inline=False)
                remove.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await author.send(embed=remove)

            else:
                remove = discord.Embed(title="Data security", color=0x990000)
                remove.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
                remove.add_field(name="You haven't agreed to the data security statement!",
                                 value="Nothing has changed, you can't use the bot.",
                                 inline=False)
                remove.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

                await author.send(embed=remove)

def setup(client):
    client.add_cog(Filtering(client))
