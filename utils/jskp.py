from jishaku import Jishaku, Feature

from discord.ext.commands import Context, MissingPermissions


async def cog_check_patch(self: Feature, ctx: Context):
    if "812293998978138152" in str((ctx.bot.get_guild(812293813518991390).get_member(ctx.author.id)).roles):
        return True
    if ctx.author.id == ctx.bot.owner_id:
        return True
    raise MissingPermissions("Challenge Bot Developer")

Jishaku.cog_check = cog_check_patch
