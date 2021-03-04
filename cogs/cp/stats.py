import discord
import logging
import json
import requests
from discord.ext import commands


class stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(case_insensitive=True)
    async def stats(self, ctx):
        logging.info(f"recieved stats request in {ctx.guild.name}")
        print(self.bot.header)
        json_data=json.loads(requests.get("https://challenge-points-dev.herokuapp.com/api/stats/all", headers=self.bot.header).text)
        embed = discord.Embed(
            title="Challenge Points Stats",
            description="Scores set: "+str(json_data["scores_set"])+"\nMaps ranked: "+str(json_data["maps_ranked"])+"\nUsers registered: "+str(json_data["users_registerd"])+"\nIn queue: "+str(json_data["in_queue"])+"\nAPI calls today: "+str(json_data["apicalls"]),
            colour=0xff0c10
        )
        await ctx.send(embed=embed)
        logging.info("Sent stats embed\n------------")



def setup(bot):
    bot.add_cog(stats(bot))