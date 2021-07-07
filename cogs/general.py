from discord import Embed, Permissions

from discord.ext import commands
from discord.utils import oauth_url


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

    @commands.command(case_insensitive=True, aliases=["invite","website"])
    async def links(self, ctx):
        permission_names = (
            "send_messages",
            "embed_links",
            "attach_files",
            "add_reactions",
            "use_external_emojis"
        )
        perms = Permissions()
        perms.update(**dict.fromkeys(permission_names, True))
        embed = Embed(
            description=
f"""[**Bot Invite Link**]({oauth_url(self.bot.user.id, perms)})
[**Home Server**](https://discord.gg/SaEgfnepn7)
[**Challenge Points Website**](https://new-challenge-points.herokuapp.com/)
[**Github Repo**](https://github.com/Challenge-Points)\n
I hope you're having a good day :)""",
            colour=0xff0000)
        embed.set_thumbnail(url=(self.bot.get_guild(812293813518991390).icon_url))
        await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
