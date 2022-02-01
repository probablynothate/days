#   Imports Start

import discord, rich, os, fade, random, colorama

from discord.ext import commands
from rich.console import Console
from win10toast import ToastNotifier
from days import initial_extensions

#import end

class dev(commands.Cog):

    def __init__(self, bot):
        self = bot

    @commands.command(aliases=["cc"])
    @commands.is_owner()
    async def cogcount(self, ctx):
        emb = discord.Embed(description="Total Cogs Loaded.", color=0xfbb4f3)
        emb.add_field(name="\u200b", value=f"{len(initial_extensions)}")
        await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(dev(bot))
