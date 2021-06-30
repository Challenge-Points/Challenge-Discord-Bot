from jishaku import Jishaku, Feature
from discord.ext.commands import Context

async def cog_check_patch(self: Feature, ctx: Context):
    if "797422816584007720" in str(ctx.author.roles): 
        return True
    if ctx.author.id == ctx.bot.owner_id:
        return True
    return False

Jishaku.cog_check = cog_check_patch