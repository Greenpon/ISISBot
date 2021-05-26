# https://discordpy.readthedocs.io/en/latest/api.html

import discord
from discord.ext import commands
from datetime import date
import feedparser
import random

# DATE DEF
today = date.today()
d1 = today.strftime("%d/%m")
d2 = today.strftime("%d/%m/%y")

# EXTENSIONS
extensions = ["Befehle", "Filtering"]

# INIT BOT
client = commands.Bot(command_prefix='!', help_command=None)

# PRESENCE & BOOT CONF.
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='ISIS'))
    print(f"{client.user} is running :)")


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

#DATENSCHUTZ DISCLAIMER
@client.command()
async def datenschutz(ctx):

    if ctx.channel.name == "bot-test":

        datenschutz = discord.Embed(title="", color=0x990000)
        datenschutz.set_thumbnail(url="https://i.imgur.com/TBr8R7L.png")
        datenschutz.add_field(name="Achtung!", value="Mit der Benutzung dieses Bots willigst du ein, dass deine personenbezogenen Daten von ISIS bezogen und verarbeitet werden! Bitte benutze diesen Bot nicht, wenn du damit nicht einverstanden bist.", inline=False)
        datenschutz.set_footer(text="ISIS Bot v0.1 • " + d2, icon_url="https://i.imgur.com/s8Ni2X1.png")

        await ctx.send(embed=datenschutz)

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
            print('Failed to load extension {}\n{}'.format(extension, exc))
    import config
    client.run(config.Token)
