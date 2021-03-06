import logging
from math import ceil
from asyncio import sleep

from discord import Embed, Colour

from discord.ext import commands


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        logging.info(f"ErrorHandler invoked")
        

        if hasattr(ctx.command, "on_error"):
            return
        
        if isinstance(error, commands.BadArgument):
            logging.info("BadArgument handler ran")
            return await ctx.send(f"You've given a bad argument!\nCheck ``{ctx.prefix}help`` for what arguments you need to give")

        if isinstance(error, commands.CommandNotFound):
            logging.info("CommandNotFound handler ran")
            return await ctx.send("Command not found")

        if isinstance(error, commands.BotMissingPermissions):
            logging.info(f"BotMissingPermissions handler ran - {error.missing_perms}")
            return await ctx.send(f"Bot missing the following permissions: {error.missing_perms}")

        if isinstance(error, commands.NotOwner):
            logging.info("NotOwner handler ran")
            return await ctx.send("This is an owner only command.")

        if isinstance(error, commands.CommandOnCooldown):
            logging.info("CommandOnCooldown handler ran")
            message = await ctx.send(f"Command on cooldown, ``{ceil(error.retry_after)} seconds``")
            await sleep(int(ceil(error.retry_after)))
            return await message.add_reaction("✅")

        if isinstance(error, commands.MissingRequiredArgument):
            logging.info(f"MissingRequiredArgument handler ran. Missing: {error.param.name}")
            return await ctx.send("You didn't give a required argument.")

        if isinstance(error, commands.MissingPermissions):
            logging.info("MissingPermissions handler ran")
            return await ctx.send("You don't have the permissions for this command.")


        logging.error(error)
        await ctx.send(embed=Embed(
            title="Uh oh. Something bad happened <:PepeHands:820648896413171722>",
            description=f"An unhandled error occured.\nIf this keeps occuring open an [issue report](https://github.com/Challenge-Points/Challenge-Discord-Bot/issues)\n\n```{error}```",
            colour=Colour.red()
        ))
        return await self.bot.get_channel(859718487366303774).send(embed=Embed(
            title=f"{ctx.command} in {ctx.guild.name}",
            description=f"{ctx.guild.id}\n**Message Content**```{ctx.message.content}```\n**Error**```{error}```",
            colour=Colour.red()
        ))


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
