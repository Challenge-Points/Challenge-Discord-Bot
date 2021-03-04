import discord
import os
import logging
import firebase_admin
from firebase_admin import credentials
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
from random import randint
from discord.ext import commands, tasks
from utils import jskp


cwd = os.getcwd()
load_dotenv(f"{cwd}/config.env")
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!cb ",intents=intents,case_insensitive=True,allowed_mentions=discord.AllowedMentions(replied_user=False))
bot.header = {"User-Agent": "Challenge Bot (https://github.com/Challenge-Points/Challenge-Discord-Bot)"}
logging.basicConfig(format= '%(asctime)s:%(levelname)s:%(name)s: %(message)s',level=logging.INFO,handlers=[logging.handlers.RotatingFileHandler(filename="log.log", maxBytes=5000000, backupCount=1)])

cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "challengepoints-475e8",
    "private_key_id": "846a1fedbb168eec61e2493cf7a354f9df1d6a5d",
    "private_key": os.getenv("PRIVATE_KEY").replace('\\n', '\n'),  
    "client_email": "firebase-adminsdk-vhibp@challengepoints-475e8.iam.gserviceaccount.com",
    "client_id": "117926289697887103422",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-vhibp%40challengepoints-475e8.iam.gserviceaccount.com"
})

default_app = firebase_admin.initialize_app(cred)

status_list = [
    "Aso kinda cute 😳",
    "Vibros",
    "Challenge Maps",
    "Beat Saber",
    "Yeet Saber",
    "Meat Saber",
    "Shiny Happy Days"
]

initial_cogs = [
    "jishaku",
    "cogs.cp.stats",
    "cogs.error_handler",
    "cogs.text",
    "cogs.link",
    "cogs.neko"
]


for cog in initial_cogs:
    try:
        bot.load_extension(cog)
        logging.info(f"Successfully loaded {cog}")
    except Exception as e:
        logging.error(f"Failed to load cog {cog}: {e}")


@tasks.loop(hours=1)
async def status():
    await bot.wait_until_ready()
    value = (randint(0, len(status_list))) - 1
    await bot.change_presence(activity=discord.Game(name=status_list[value]))
    logging.info(f"Status set to: {status_list[value]}")

@bot.event
async def on_ready():
    logging.info('Bot has successfully launched as {0.user}'.format(bot))
    status.start()


bot.run(os.getenv("TOKEN"))
