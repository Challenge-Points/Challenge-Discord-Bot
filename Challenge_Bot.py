import discord
import os
import logging
from dotenv import load_dotenv
from random import randint
from discord.ext import commands, tasks
from utils import jskp


cwd = os.getcwd()
load_dotenv(f"{cwd}/config.env")


intents = discord.Intents.default()
client = commands.Bot(command_prefix="!ch ",intents=intents,case_insensitive=True,allowed_mentions=discord.AllowedMentions(replied_user=False))
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

funniList = [
    "Aso kinda cute 😳",
    "Vibros",
    "Shiny Happy Days"
]

initial_cogs = [
    "jishaku",
    "cogs.error_handler",
]


for cog in initial_cogs:
    try:
        client.load_extension(cog)
        logging.info(f"Successfully loaded {cog}")
    except Exception as e:
        logging.error(f"Failed to load cog {cog}: {e}")


@tasks.loop(hours=1)
async def status():
    value = randint(0, len(funniList)) - 1
    await client.change_presence(activity=discord.Game(name=funniList[value]))
    logging.info(f"Status set to: {funniList[value]}")

@client.event
async def on_ready():
    logging.info('Bot has successfully launched as {0.user}'.format(client))
    status.start()


client.run(os.getenv("TOKEN"))
