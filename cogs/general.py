import logging

from discord import Embed

from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_message')
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.channel.id == 816398589173432380 and "https://beatsaver.com/beatmap/" in message.content:
            await message.add_reaction("🟩")
            await message.add_reaction("🟥")

    @commands.command(case_insensitive=True, aliases=["link","website"])
    async def links(self, ctx):
        logging.info('Recieved: links')
        embed = Embed(
            title="Important Challenge Links",
            description="[Website](https://challengepoints.ml/) | [Discord](https://discord.gg/SaEgfnepn7) | [Challenge Points GitHub](https://github.com/Challenge-Points)",
            color=0xff0000)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/813876085724020787/813883027960365066/ChallengePointsLogo.png")
        await ctx.send(embed=embed)
        logging.info(f'Response: embed\n----------')


def setup(bot):
    bot.add_cog(General(bot))
