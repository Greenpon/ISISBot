# https://discordpy.readthedocs.io/en/latest/api.html
import asyncio
import discord
from discord.ext import commands
from datetime import date
import random
import ShowForum
import logging

#LOGGING CONFIG (for debugging)
logging.basicConfig(filename='debug.log')

# DATE DEF
today = date.today()
d1 = today.strftime("%d/%m")
d2 = today.strftime("%d/%m/%y")

# EXTENSIONS
extensions = ["Befehle", "Filtering", "ShowForum"]

# INIT BOT
client = commands.Bot(command_prefix='!', help_command=None)

# PRESENCE & BOOT CONF.
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='ISIS'))
    print(f"{client.user} is running :)")

# ERROR HANDLING (COMMAND DOES NOT EXIST)
@client.event
async def on_command_error(ctx, error):
    if ctx.channel.id in channel_id:
        if isinstance(error, commands.CommandNotFound):

            errormsg = discord.Embed(title="", color=0x990000)
            errormsg.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
            errormsg.add_field(name="Achtung!", value="Diesen Befehl kenne ich nicht. \nSchau dir meine Befehle mit !help an.", inline=False)
            errormsg.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

            await ctx.send(embed=errormsg)

# NOTIF TEST COMMAND (random content)
@client.command()
async def notif(ctx):

    if ctx.channel.name == "bot-test":
        module = [
            "IntroProg",
            "AlgoDat",
            "Ana2",
            "Ana1-LinAlg",
            "ProMedi",
            "Einf. MedInfo",
            "DigiSys",
            "WebTech",
        ]
        random.shuffle(module)
        modul_1 = module[1]
        modul_2 = module[2]
        modul_3 = module[3]

        foren = [
            "Ankündigungen",
            "Studierendenforum",
            "FAQ",
            "Diskussionsforum",
            "Fragen zur Vorlesung Q&A",
            "Organisatorische Fragen",
            "Fragen zur Vorlesung Q&A",
        ]
        random.shuffle(foren)
        forum_1 = foren[1]
        forum_2 = foren[2]
        forum_3 = foren[3]

        nachrichten = [
            "Suche eine HA-Gruppe",
            "Drittes HA-Blatt bis heute 18h abzugeben!",
            "Vergessen sie nicht, sich bis zum " + d1 + " in QUISPOS einzuschreiben!",
            "Probleme bei der Abgabe B05"
        ]
        random.shuffle(nachrichten)
        nachricht_1 = nachrichten[1]
        nachricht_2 = nachrichten[2]
        nachricht_3 = nachrichten[3]

        unsubscribe = "[*Forum abbestellen*](https://isis.tu-berlin.de/login/index.php)"

        test_notif = discord.Embed(color=0x990000)
        test_notif.set_author(name=f"Benachrichtigungen für {ctx.author.display_name}" + " vom " + d1,
                              icon_url=ctx.author.avatar_url)
        test_notif.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
        test_notif.add_field(name=modul_1 + " ➔ " + forum_1, value=nachricht_1 + "\n" + unsubscribe, inline=False)
        test_notif.add_field(name=modul_2 + " ➔ " + forum_2, value=nachricht_2 + "\n" + unsubscribe, inline=False)
        test_notif.add_field(name=modul_3 + " ➔ " + forum_3, value=nachricht_3 + "\n" + unsubscribe, inline=False)
        test_notif.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

        test_notif.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

        await ctx.send(embed=test_notif)

#SETUP TO GET THE CHANNEL WHICH WILL BE USED & START THE BOT
channel_id =[]
@client.command(aliases=["startup", "Start", "init"])
async def start(ctx):

    channel_id.append(ctx.channel.id)
    await datenschutz()

#REMOVES ALL COMMANDS FROM THE CHANNEL TO KEEP IT CLEAN
@client.event
async def on_message(message):
    if message.content.startswith("!"):
        await client.process_commands(message)
        await message.delete()



#DATENSCHUTZ DISCLAIMER
#Also adds reactions and pins the message
#Author: Sven
async def datenschutz():

    datenschutzmsg = discord.Embed(title="", color=0x990000)
    datenschutzmsg.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
    datenschutzmsg.add_field(name="Achtung!", value="This application was created for research purpose and is not  officially utilized by the TU Berlin. Personal data, such as full names that are published in ISIS forums will be obtained and processed from ISIS in Discord. Users are obliged to use the bot only on Discord servers subscribed by fellow students that are related to the ISIS module you configure it for. Please do not use this bot on Discord servers where you can not guarantee that the personal data of your fellow students is safe from misuse. For more information about TU Berlin data security have a look at https://www.tu-berlin.de/allgemeine-seiten/datenschutz/.", inline=False)
    datenschutzmsg.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

    channel = client.get_channel(channel_id[0])

    embed_datenschutz = await channel.send(embed=datenschutzmsg)
    await embed_datenschutz.add_reaction("\U00002705")
    await embed_datenschutz.add_reaction("\U0000274C")
    await embed_datenschutz.pin()

#SHUTDOWN FOR THE BOT (ONLY OWNER CAN DO SO)
@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await client.close()
    print("Bot Closed")



# RUN BOT AND LOAD EXTENSIONS
if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            logging.debug(e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    import config

    try:
        client.run(config.Token)
    except Exception as e:
        logging.debug(e)
