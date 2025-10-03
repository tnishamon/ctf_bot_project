import discord 
from discord.ext import commands
from os import environ
import os
from dotenv import load_dotenv
import sqlite3 
import requests 
import stampTime as ts

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
    # Invoke custom class to get timestamps (I cleaned that ugly garbage up)
    x = ts.stampTime()
    # Get start time and end time in epoch time (returns as int)
    start = x.startTimeStamp(x.saveStart)
    end = x.endTimeStamp(x.saveStart, 28)
    # API request
    response = requests.get('https://ctftime.org/api/v1/events/?limit=30&start=' + str(start) + '&finish=' + str(end))
    if response.status_code == 200:
        data = response.json()
        await ctx.channel.send('CTFs in next month: \n')
        
        # Get data from json
        for i in data:
            await ctx.channel.send('Name: ' + i['title'] + '\n' +
                             'Date: ' + i['start'] + '\n' +
                             'Link: <' + i['url'] + '>' + '\n')
           
    else:
        await ctx.channel.send('Sorry, bub, no get request for you')

# Run client (our bot) 
bot.run(token)