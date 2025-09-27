import discord 
from discord.ext import commands
from os import environ
import os
from dotenv import load_dotenv
import sqlite3 
import requests 

load_dotenv()
# Token from .env
token=environ["DISCORD_BOT_TOKEN"]


# Class for discord events, will need to refactor later
class Client(discord.Client):
    async def on_ready(self):
        print('Testing print :)')
        
        try:
            guild = discord.Object(id=1391665916194066483)
            synced = await self.tree.sync(guild=guild)
        except Exception as e:
            print('Error')
        
# Declares our discord intent, which Discord needs specified. 
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

GUILD_ID = discord.Object(id=1391665916194066483)

@client.command(guild = GUILD_ID)
async def test(ctx):
    response = requests.get('https://ctftime.org/api/v1/top/')
    data = response.json()
    await ctx.channel.send(data)

# Run client locally 
client.run(token)