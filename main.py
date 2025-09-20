import discord 
from os import environ

from dotenv import load_dotenv

load_dotenv()

token=environ["DISCORD_BOT_TOKEN"]

class Client(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return 
        if message.content.startswith('Dylan'):
            await message.channel.send('I hate Dylan')
        if message.content.startswith('Matt'):
            await message.channel.send('Oh man, I love Matt so much and hate Dylan')
        
intents = discord.Intents.default()
intents.message_content = True

client = Client(intents = intents)
client.run(token)