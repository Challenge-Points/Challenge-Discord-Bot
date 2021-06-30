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
            description="""[Challenge Points Website](https://new-challenge-points.herokuapp.com/)
[Challenge Points Discord](https://discord.gg/SaEgfnepn7)
[Challenge Points GitHub](https://github.com/Challenge-Points)""",
            color=0xff0000)
        embed.set_thumbnail(url=(self.bot.get_guild(812293813518991390).icon_url))
        await ctx.send(embed=embed)
        logging.info(f'Response: embed\n----------')


def setup(bot):
    bot.add_cog(General(bot))
