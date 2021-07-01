import logging
from logging.handlers import RotatingFileHandler
from asyncio import get_event_loop
from os import getcwd, getenv

from discord import Intents, AllowedMentions
from aiohttp import ClientSession
from dotenv import load_dotenv
from firebase_admin import credentials, initialize_app

from discord.ext.commands import Bot
from utils import jskp


logging.basicConfig(format= '%(asctime)s:%(levelname)s:%(name)s: %(message)s',level=logging.INFO,handlers=[RotatingFileHandler(filename="log.log", maxBytes=5000000, backupCount=2)])

load_dotenv(getcwd()+"/.env")

intents = Intents.default()
intents.members = True
bot = Bot(command_prefix="!cb ", intents=intents, case_insensitive=True, allowed_mentions=AllowedMentions(replied_user=False))


cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "challengepoints-475e8",
    "private_key_id": "846a1fedbb168eec61e2493cf7a354f9df1d6a5d",
    "private_key": getenv("PRIVATE_KEY").replace('\\n', '\n'),  
    "client_email": "firebase-adminsdk-vhibp@challengepoints-475e8.iam.gserviceaccount.com",
    "client_id": "117926289697887103422",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-vhibp%40challengepoints-475e8.iam.gserviceaccount.com"
})

default_app = initialize_app(cred)


initial_cogs = [
    "jishaku",
    "cogs.beatsaver",
    "cogs.challenge_points",
    "cogs.error_handler",
    "cogs.general",
    "cogs.user",
    "cogs.waifu"
]

for cog in initial_cogs:
    try:
        bot.load_extension(cog)
        logging.info(f"Successfully loaded {cog}")
    except Exception as e:
        logging.error(f"Failed to load cog {cog}: {e}")


@bot.event
async def on_ready():
    bot.session = ClientSession(loop=get_event_loop(), headers={"User-Agent": "Challenge Bot (https://github.com/Challenge-Points/Challenge-Discord-Bot)"})
    logging.info('Bot has successfully launched as {0.user}'.format(bot))

@bot.before_invoke
async def before_invoke(ctx):
    logging.info(f"Invoked {ctx.command} in {ctx.guild.name} by {ctx.author.name}\nArgs: {ctx.args}" )

@bot.after_invoke
async def after_invoke(ctx):
    logging.info(f"Concluded {ctx.command}")


bot.run(getenv("TOKEN"))
