#   Imports Start

import discord, rich, os, fade, random, colorama

from discord.ext import commands
from rich.console import Console
from win10toast import ToastNotifier

#import end

class dev(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["cc"])
    @commands.is_owner()
    async def cogcount(self, ctx):
        emb = discord.Embed(description="Total Cogs Loaded.", color=0xfbb4f3)
        emb.add_field(name="Total Cog Count", value=f"{len(self.bot.cogs)}")
        await ctx.send(embed=emb)
    
    @commands.command(aliases=["lc"])
    @commands.is_owner()
    async def listcogs(self, ctx):
        embl = discord.Embed(description="Listing the Cogs.", color=0xfbb4f3)
        embl.add_field(name="Total Cogs List", value=f"`{list(self.bot.cogs)}`")
        await ctx.send(embed=embl)

def setup(bot):
    bot.add_cog(dev(bot))