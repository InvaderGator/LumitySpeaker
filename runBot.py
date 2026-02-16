#IMPORT REQUIREMENTS
import discord
import os
from dotenv import load_dotenv

#LOADS ENV FILE
load_dotenv()

#CREATES CLIENT CLASS
client = discord.Bot()

#DICTIONARY FOR LUMITY SPEAK
lumityDict = {
    "a": "🦇",
    "b": "⛰",
    "c": "🦀",
    "d": "😭",
    "e": "🎹",
    "f": "📊",
    "g": "🍤",
    "h": "🌴",
    "i": "⛔",
    "j": "🦈",
    "k": "✂",
    "l": "✔",
    "m": "🌜",
    "n": "🐍",
    "o": "🌞",
    "p": "🧢",
    "q": "🍀",
    "r": "📈",
    "s": "⚡",
    "t": "☂",
    "u": "↩",
    "v": "🥢",
    "w": "🌛",
    "x": "⚔",
    "y": "🌂",
    "z": "🧬",
    "!": "❗",
    "?": "❓",
}

#DICTIONARY FOR ENGLISH LETTERS
englishDict = {
    "🦇": "a",
    "⛰": "b",
    "🦀": "c",
    "😭": "d",
    "🎹": "e",
    "📊": "f",
    "🍤": "g",
    "🌴": "h",
    "⛔": "i",
    "🦈": "j",
    "✂": "k",
    "✔": "l",
    "🌜": "m",
    "🐍": "n",
    "🌞": "o",
    "🧢": "p",
    "🍀": "q",
    "📈": "r",
    "⚡": "s",
    "☂": "t",
    "↩": "u",
    "🥢": "v",
    "🌛": "w",
    "⚔": "x",
    "🌂": "y",
    "🧬": "z",
    "❗": "!",
    "❓": "?",
}

#TRANSLATION TABLES
trans = str.maketrans(lumityDict)
transEnglish = str.maketrans(englishDict)

#EMOJI ARRAY FOR COMPARISON
emojis = [
    "🦇", "⛰️", "🦀", "😭", "🎹", "📊", "🍤", "🌴", "⛔", "🦈",
    "✂️", "✔️", "🌜", "🐍", "🌞", "🧢", "🍀", "📈", "⚡", "☂️",
    "↩️", "🥢", "🌛", "⚔️", "🌂", "🧬", "❗", "❓",
]

#LETTER ARRAY FOR COMPARISON
letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z", "!", "?"
]

#DETERMINES FORMATING FOR DICTIONARY
#SCARY, I DON'T LIKE IT.
#NUMBERS OF LETTERS AND EMOJIS NEED TO BE EVEN FOR THIS TO WORK
dictionaryList = []
dictionaryListCounter = 0
while(len(emojis)-1 > dictionaryListCounter):
    emoji = emojis[dictionaryListCounter]
    emoji2 = emojis[dictionaryListCounter + 1]
    letter = letters[dictionaryListCounter]
    letter2 = letters[dictionaryListCounter + 1]
    dictionaryList.append(emoji + "  |  " + letter + "                        " + emoji2 + "  |  " + letter2)
    dictionaryListCounter += 2

#WHEN BOT CONNECTS AND IS READY
@client.event
async def on_ready():
    print(f"{client.user} is ready and online!")

#Thank you to toothyfernsan on the py-cord discord.
#I would've cried if i needed to reprogram this thing in another launguage to get dm channels working
#WHEN SOMEONE TRANSLATES A MESSAGE WITHOUT SPECIFICATION FOR ENGLISH OR LUMITY
@client.slash_command(name="translate", description="Translate a message!", integration_types={discord.IntegrationType.user_install})
async def translate(
        ctx: discord.ApplicationContext,
        message: discord.Option(str, description="Message to translate."),
        isprivate: discord.Option(bool, description="If message is private or not. Default is false.")
):
    #BOOLEAN FOR ENGLISH OR LUMITY TRANSLATION
    #DECIDES BASED ON IF IT STARTS WITH AN EMOJI OR NOT
    isToEnglish = False

    #ALL MESSAGES NEED TO BE LOWERCASE. TRANSLATION IS CASE SENSITIVE WITHOUT THIS CHECK
    lowerMessage = message.lower()

    for x in emojis:
        if(lowerMessage.startswith(x)):
            isToEnglish = True

    if(isToEnglish):
        newMessage=lowerMessage.translate(transEnglish)
    else:
        newMessage=lowerMessage.translate(trans)

    await ctx.respond(newMessage, ephemeral=isprivate)

#WHEN USER SPECIFICALLY TRANSLATES TO LUMITY SPEAK
@client.slash_command(name="translatetolumity", description="Translate Lumity to English!", integration_types={discord.IntegrationType.user_install})
async def translatetolumity(
        ctx: discord.ApplicationContext,
        message: discord.Option(str, description="Message to translate."),
        isprivate: discord.Option(bool, description="If the message is private. Default is no.", default=False)
):
    lowerMessage = message.lower()

    newMessage=lowerMessage.translate(trans)
    await ctx.respond(newMessage, ephemeral=isprivate)

#WHEN USER SPECIFICALLY TRANSLATES TO ENGLISH LETTERING
@client.slash_command(name="translatetoenglish", description="Translate English to Lumity!", integration_types={discord.IntegrationType.user_install})
async def translatetoenglish(
        ctx: discord.ApplicationContext,
        message: discord.Option(str, decription="Message you want translated."),
        isprivate: discord.Option(bool, description="If the translation is private or not. Default is false.", default=False)
):
    lowerMessage = message.lower()

    newMessage = lowerMessage.translate(transEnglish)
    await ctx.respond(newMessage, ephemeral=isprivate)

#WHEN USER WANTS TO SEE THE DICTIONARY
#MY FRIEND AND I DECIDED SOME LETTERING OURSELVES SINCE THERE IS NO UNIFIED VERSION OF LUMITY SPEAK
@client.slash_command(name="dictionary", description="View dictionary!", integration_types={discord.IntegrationType.user_install})
async def dictionary(
        ctx: discord.ApplicationContext,
        isprivate = discord.Option(bool, description="If the dictionary is private. Default is false.", default=False)
):

    #FORMATING FOR MESSAGING
    formattedMessage = '\n'.join(dictionaryList)
    newMessage = "*Dictionary!*\n>>> {}".format(formattedMessage)

    await ctx.respond(newMessage, ephemeral=isprivate)

#WHEN USER WANTS TO VIEW GITHUB PAGE
@client.slash_command(name="github", description="View source code and instructions.", integration_types={discord.IntegrationType.user_install})
async def github(ctx: discord.ApplicationContext):
    await ctx.respond("https://github.com/InvaderGator/LumitySpeaker", ephemeral=True)

#WHEN USER WANTS TO VIEW COMMANDS AND USES OF COMMANDS
@client.slash_command(name="help", description="Get commands and use the bot!", integration_types={discord.IntegrationType.user_install})
async def help(ctx: discord.ApplicationContext):
    commands = [
        "***/help*** | For this command menu.",
        "***/github*** | Sends github link.",
        "***/invite*** | Sends invite link.",
        "***/translate*** | Translate a generic message.",
        "***/translatetolumity*** | Translate letters into Lumity.",
        "***/translatetoenglish*** | Translate Lumity into letters.",
        "***/dictionary*** | View dictionary."
    ]
    #JOINS ARRAYS FOR FORMATTING
    formattedMessage = '\n'.join(commands)
    newMessage = '*Welcome! View github for more context!*\n>>> {}'.format(formattedMessage, ephemeral=True)

    await ctx.respond(newMessage)

#RUNS BOT

client.run(os.getenv('DISCORD_TOKEN'))
