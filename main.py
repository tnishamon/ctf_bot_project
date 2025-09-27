import discord 
from discord.ext import commands
from os import environ
import os
from dotenv import load_dotenv
import sqlite3 
import requests 
import time
import datetime
import pandas as pd

load_dotenv()
# Token from .env
token=environ["DISCORD_BOT_TOKEN"]
GUILD_ID = discord.Object(id=1391665916194066483)

# Class for discord events, will need to refactor later
class Client(discord.Client):
    # Initialie bot for client and for specific Guild
    async def on_ready(self):
        print('Testing print :)')
        
        try:
            synced = await self.tree.sync(guild=GUILD_ID)
        except Exception as e:
            print('Error')
        
# Declares our discord intent, which Discord needs specified. 
intents = discord.Intents.default()
intents.message_content = True
# Intialie client with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Command on client
@bot.command(guild = GUILD_ID)
async def test(ctx):
    # This is so gross, someone please refactor this shit
    initalize = datetime.datetime.now()
    ts = pd.Timestamp(initalize)
    start = ts.round(freq='d')
    end = start + datetime.timedelta(days=14)
    ts2 = pd.Timestamp(end)
    end2 = ts2.round(freq='h')
    start = int(start.timestamp())
    end3 = int(end2.timestamp())
    
    # API request
    response = requests.get('https://ctftime.org/api/v1/events/?limit=30&start=' + str(start) + '&finish=' + str(end3))
    if response.status_code == 200:
        data = response.json()
        await ctx.channel.send('CTFs in next two weeks: \n')
        
        # Get data from json
        for i in data:
            await ctx.channel.send('Name: ' + i['title'] + '\n' +
                             'Date: ' + i['start'] + '\n' +
                             'Description: ' + i['description'] + '\n' +
                             'Link: ' + i['url'])
            
    else:
        await ctx.channel.send('Sorry, bub, no get request for you')
# Run client (our bot) 
bot.run(token)