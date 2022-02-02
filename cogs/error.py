#   Imports Start

import discord, rich, os, fade, random, colorama, time
from numpy import isin

from discord.ext import commands
from discord.ext.commands import CommandNotFound
from rich.console import Console
from colorama import init, Fore
from datetime import datetime, date
from win10toast import ToastNotifier

#import end

class error(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cooldowntest(self, ctx):
        await ctx.send("hi")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            today = date.today()
            dt = datetime.utcfromtimestamp(time.time())
            current_time = dt.strftime("%H:%M")
            print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}{today} {current_time}{Fore.LIGHTWHITE_EX}]{Fore.LIGHTWHITE_EX} [{Fore.LIGHTRED_EX}Error{Fore.LIGHTWHITE_EX}] Some retard just tried to use a non existent command')
        elif isinstance(error, commands.CommandOnCooldown):
            embcn = discord.Embed(color=0xfbb4f3)
            embcn.add_field(name=f"Command is on Cooldown", value=f"Retry after: {error.retry_after:.2f}'s")
            await ctx.send(embed=embcn)
        if isinstance(error, commands.NotOwner):
            today = date.today()
            dt = datetime.utcfromtimestamp(time.time())
            current_time = dt.strftime("%H:%M")
            print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}{today} {current_time}{Fore.LIGHTWHITE_EX}]{Fore.LIGHTWHITE_EX} [{Fore.LIGHTRED_EX}Error{Fore.LIGHTWHITE_EX}] Bro What the fuck :skull: a nigga just triet to use a owner only command LMFAOOOO ')            

def setup(bot):
    bot.add_cog(error(bot))