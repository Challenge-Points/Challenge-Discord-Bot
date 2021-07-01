import logging
from json import loads

from discord import Embed, Member

from discord.ext import commands


class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.group(invoke_without_command=True, aliases=["u"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def user(self, ctx, argument: Member = None):
        if argument is None:
            argument = ctx.author
        async with ctx.channel.typing():
            async with self.bot.session.get(f"https://challengepointsapi.herokuapp.com/api/users/{argument.id}/data") as resp:
                if await resp.text() == "Not Found":
                    logging.info(f"User not found")
                    return await ctx.send("""Something something about not having an challenge account
I'll update this when I actually understand how a user can signup lmao""") 
                json_data = loads(await resp.text())
        embed = Embed(colour=argument.colour)
        embed.set_author(name=argument.name, url=f"https://new-challenge-points.herokuapp.com/users/user?id={argument.id}", icon_url=argument.avatar_url)
        embed.add_field(
            name="Global Rank",
            value=f"#{json_data['global']}",
            inline=True
        )
        embed.add_field(
            name="CP", 
            value=json_data["cp"], 
            inline=True
        )
        embed.add_field(
            name="Average Acc",
            value=f"{json_data['avgacc']}%",
            inline=True
        )
        if json_data["badges"]:
            message = str()
            for badge in json_data["badges"]:
                message = f"{message} {badge},"
            embed.add_field(
                name="Badges",
                value=message[:-1],
                inline=False
            )
        embed.add_field(
            name="Quote",
            value=json_data["config"]["quote"],
            inline=False
        )
        await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(User(bot))
