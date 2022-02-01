#   Imports Start

from http.client import REQUESTED_RANGE_NOT_SATISFIABLE


import discord, rich, os, fade, random, colorama, requests

from discord.ext import commands
from rich.console import Console
from win10toast import ToastNotifier

#import end

version = "1.0"

console = Console(
    color_system="auto",
    legacy_windows=True
)

if os.name == 'ns':
    toast_noti = ToastNotifier()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

nl = "\n"

def interface():
    os.system('cls' if os.name == 'nt' else 'clear')

bot = commands.Bot(command_prefix="$")



def splash():
    colorama.init(strip = True, convert = True, autoreset = True)
@bot.event
async def on_ready():
    #variables = [fade.blackwhite, fade.greenblue, fade.purpleblue, fade.fire, fade.purplepink, fade.fire, fade.water, fade.pinkred]
    variables = [fade.greenblue]
    splash = random.choice(variables)("""
    
                   ██████╗  █████╗ ██╗   ██╗███████╗
                   ██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝
                   ██║  ██║███████║ ╚████╔╝ ███████╗
                   ██║  ██║██╔══██║  ╚██╔╝  ╚════██║
                   ██████╔╝██║  ██║   ██║   ██████╔╝
                   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═════╝
""")
    motd = requests.get('https://raw.github.com/probablynothate/days/master/motd')
    if motd.statuscode in (200, 204):
        return
    info = f''' 
                {version}
                Connected as: {bot.user}
                Prefix: {bot.command_prefix}
                Guild Count: {len(bot.guilds)}
                Cogs Count: {len(bot.cogs)}
                ┌───────────────────────────────┐
                motd: {motd.text}
                └───────────────────────────────┘
'''
    interface()
    coloredversion = fade.greenblue(info)
    console.print(splash, justify="center", end=" ")
    console.print(coloredversion, justify="center")
token = "OTM1OTY3NjM1OTIzOTI3MDkw.YfGVyQ.wHiJcHmYErJUbUJX8miVGotaO3w"

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    embed = discord.Embed(description=f"Cogs Loaded Successfully. `{extension}`", color=0x5dff9c)
    embed.set_author(name="Loaded Cogs")
    await ctx.send(embed=embed)

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    embed = discord.Embed(description=f"Unloaded Cogs `{extension}`", color=0x2F3136)
    await ctx.send(embed=embed)

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    embed = discord.Embed(description=f"Cogs Have Been Reloaded `{extension}`", color=0x2F3136)
    embed.set_author(name="Reloaded Cogs")
    await ctx.send(embed=embed)

bot.run(token)