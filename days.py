#   Imports Start

import discord, rich, os, fade, random, colorama, requests, time, ctypes

from discord.ext import commands
from rich.console import Console
from datetime import datetime
from datetime import date
from win10toast import ToastNotifier
from colorama import Fore

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

for filename in os.listdir('./cogs'):
  if filename.endswith(".py"):
    bot.load_extension(f'cogs.{filename[:-3]}')

def splash():
    colorama.init(strip = True, convert = True, autoreset = True)
@bot.event
async def on_ready():
    #variables = [fade.blackwhite, fade.greenblue, fade.purpleblue, fade.fire, fade.purplepink, fade.fire, fade.water, fade.pinkred]
    variables = [fade.blackwhite]
    splash = random.choice(variables)(f'''
                ██╗    ██╗██╗████████╗██╗  ██╗███████╗██████╗ 
                ██║    ██║██║╚══██╔══╝██║  ██║██╔════╝██╔══██╗
                ██║ █╗ ██║██║   ██║   ███████║█████╗  ██████╔╝
                ██║███╗██║██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
                ╚███╔███╔╝██║   ██║   ██║  ██║███████╗██║  ██║
                 ╚══╝╚══╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                            
''')
    motd = requests.get('https://raw.githubusercontent.com/probablynothate/days/master/motd')
    
    mtext = ""

    if motd.status_code == 404:
        mtext = "No MOTD found"
    else:
        mtext = motd.text
    info = f''' 
                {version}
                Connected as: {bot.user}
                Prefix: {bot.command_prefix}
                Guild Count: {len(bot.guilds)}
                Cogs Count: {len(bot.cogs)}
                ┌───────────────────────────────┐
                motd: {mtext}
                └───────────────────────────────┘
'''
    interface()
    coloredversion = fade.blackwhite(info)
    console.print(splash, justify="center", end=" ")
    console.print(coloredversion, justify="center")
    ctypes.windll.kernel32.SetConsoleTitleW("breathe v1 | Logging Terminal")
token = "OTM1OTY3NjM1OTIzOTI3MDkw.YfGVyQ.ld06qjko95CDowrFULsbWI3LoqU"


@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    embed = discord.Embed(description=f"Cogs Loaded Successfully. `{extension}`", color=0x5dff9c)
    embed.set_author(name="Loaded Cogs")
    await ctx.send(embed=embed)

@bot.command()
@commands.is_owner()
async def motd(ctx):
    today = date.today()
    dt = datetime.utcfromtimestamp(time.time())
    current_time = dt.strftime("%H:%M")
    motd = requests.get('https://raw.githubusercontent.com/probablynothate/days/master/motd')
    
    mtext = ""

    if motd.status_code == 404:
        mtext = "No MOTD found"
    else:
        mtext = motd.text
    embb = discord.Embed(description="Today's MOTD", color=0x2f3136)
    embb.add_field(name=f"{today} | {current_time}", value=f"{mtext}")
    await ctx.send(embed=embb)
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
    embed = discord.Embed(description=f"`{extension} reloaded sucessfully`", color=0x2F3136)
    embed.set_author(name="Reloaded Cogs")
    await ctx.send(embed=embed)

@bot.command(aliases=["coc"])
@commands.is_owner()
async def cogc(ctx):
    emb = discord.Embed(description="Total Cogs Loaded.", color=0xfbb4f3)
    emb.add_field(name="Total Cog Count", value=f"{len(bot.cogs)}")
    await ctx.send(embed=emb)    

bot.run(token)