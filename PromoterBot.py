# PromoterBot.py

import os
import discord
import json
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PROMO_CHANNEL = os.getenv('PROMO_CHANNEL_ID')

bot = commands.Bot(command_prefix='!')

# This runs once, when the bot is finished initializing and ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Command handler for !shook command
@bot.command(name='shook', help='Responds with a link to the next Shook event')
async def fetch_shook_event(ctx):
    response = 'placeholder message for event link'
    await ctx.send(response)

bot.run(TOKEN)