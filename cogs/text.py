import discord
import logging
from discord.ext import commands
from discord.utils import get


class text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_message')
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.channel.id == 816398589173432380:
            await message.add_reaction("🟩")
            await message.add_reaction("🟥")

    @commands.command(case_insensitive=True)
    async def ping(self, ctx):
        logging.info('Recieved: ping')
        Pong = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! ``{Pong}ms``")
        logging.info(f'Response: {Pong}ms\n----------')

    @commands.command(case_insensitive=True)
    async def links(self, ctx):
        logging.info('Recieved: links')
        embed = discord.Embed(
            title="Important Challenge Links",
            description="[Website](http://www.challengepoints.ml/) | [Discord](https://discord.gg/SaEgfnepn7) | [Challenge Points GitHub](https://github.com/Challenge-Points)",
            color=0xff0000)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/813876085724020787/813883027960365066/ChallengePointsLogo.png")
        await ctx.send(embed=embed)
        logging.info(f'Response: embed\n----------')


def setup(bot):
    bot.add_cog(text(bot))
