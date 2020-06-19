# bot.py
import os
import random
import typing
import discord
import youtube_dl

from dotenv import load_dotenv
from discord.ext import commands

#get environment variable containing private discord bot token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#instantiate bot with prefix "!"
bot = commands.Bot(command_prefix='!')
players = {}

#ROLL: rolls a n sided die with m sides
@bot.command(name = 'roll', help = 'dice rolling simulation: "!roll (# of sides) (# of dice)"')
async def roll(ctx, number_of_sides: typing.Optional[int] = 6, number_of_dice: typing.Optional[int] = 1):
  dice = [str(random.choice(range(1, number_of_sides + 1))) for _ in range(number_of_dice)]
  await ctx.send(', '.join(dice))

#JOIN: join a voice channel
@bot.command(pass_context = True)
async def join(ctx):
  channel = ctx.author.voice.channel
  await channel.connect()

#LEAVE: disconnect from voice channel
@bot.command(pass_context = True)
async def leave(ctx):
  await ctx.voice_client.disconnect()

#LEBI: echo 'lebi' string. (inside joke)
@bot.command(name = 'lebi', help = 'lebi')
async def lebi(ctx):
  response = 'lebi'
  await ctx.send(response)

bot.run(TOKEN)
