from json import loads

from discord import Embed

from discord.ext import commands


class ChallengePoints(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(case_insensitive=True)
    async def stats(self, ctx):
        async with ctx.channel.typing():
            async with self.bot.session.get("https://challengepointsapi.herokuapp.com/api/stats/all") as resp:
                json_data = loads(await resp.text())
            embed = Embed(
                title="Challenge Points Stats",
                description="Scores set: "+str(json_data["scores_set"])+"\nMaps ranked: "+str(json_data["maps_ranked"])+"\nUsers registered: "+str(json_data["users_registerd"])+"\nIn queue: "+str(json_data["in_queue"])+"\nAPI calls today: "+str(json_data["apicalls"]),
                colour=0xff0c10
            )
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(ChallengePoints(bot))