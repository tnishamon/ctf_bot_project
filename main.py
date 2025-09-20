import discord 
from os import environ
from dotenv import load_dotenv

load_dotenv()
# Token from .env
token=environ["DISCORD_BOT_TOKEN"]

# Class for discord events, will need to refactor later
class Client(discord.Client):
    # Track different messages input
    async def on_message(self, message):
        if message.author == self.user:
            return 
        if message.content.startswith('Dylan'):
            await message.channel.send('I hate Dylan')
        if message.content.startswith('Matt'):
            await message.channel.send('Oh man, I love Matt so much and hate Dylan')

# Declares our discord intent, which Discord needs specified. 
intents = discord.Intents.default()
intents.message_content = True

# Run client locally 
client = Client(intents = intents)
client.run(token)