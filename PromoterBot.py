# PromoterBot.py

import os
import discord
from discord import Embed
from dotenv import load_dotenv
from discord.ext import commands
from fb_link_parser import *
from get_event_data import get_event_data

shook_url = "https://m.facebook.com/pg/shookatkremwerk/events"
krem_url = "https://m.facebook.com/pg/kremwerk/events/"
s44_url = "https://m.facebook.com/pg/studiofourfour/events/"
q_url = "https://m.facebook.com/pg/qnightclub/events"

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


def fetch_event_data_and_format(nextEventURL, location):
    eventData = get_event_data(nextEventURL)

    embed = Embed(url=nextEventURL,
                  title=eventData['title'] + ' @ ' + location)
    embed.description = eventData['time']
    embed.set_image(url=eventData['imageURL'])
    return embed


@bot.command(name='shook', help='Responds with a link to the next Shook event')
async def fetch_shook_event(ctx):
    URLS = get_links(shook_url)
    obj = fetch_event_data_and_format(
        nextEventURL=URLS[0], location='shook')

    await ctx.send(embed=obj)


# Command handler for !s44 command


@bot.command(name='s44', help='Responds with a link to the next Studio 4/4 event')
async def fetch_s44_event(ctx):
    URLS = get_links(s44_url)
    obj = fetch_event_data_and_format(
        nextEventURL=URLS[0], location='Studio 4/4')

    await ctx.send(embed=obj)

# Command handler for !krem command


@bot.command(name='krem', help='Responds with a link to the next Kremwerk event')
async def fetch_krem_event(ctx):
    URLS = get_links(krem_url)
    response = "The next Kremwerk event is: " + URLS[0]
    await ctx.send(response)

 # Command handler for !qnightclub command


@bot.command(name='qnightclub', help='Responds with a link to the next Q Nightclub event')
async def fetch_q_event(ctx):
    URLS = get_links(q_url)
    obj = fetch_event_data_and_format(
        nextEventURL=URLS[0], location='Q Nightclub')

    await ctx.send(embed=obj)

bot.run(TOKEN)
