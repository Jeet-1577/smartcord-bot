# main.py

import os
from dotenv import load_dotenv
import discord
from openai import OpenAI

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Create OpenAI client
client_ai = OpenAI(api_key=OPENAI_API_KEY)

# Discord Bot
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.author == self.user:
            return
        
        if self.user in message.mentions or message.content.lower().startswith("hii"):
            channel = message.channel
            
            # OpenAI ChatCompletion using new API
            response = client_ai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": message.content}]
            )
            
            reply = response.choices[0].message.content
            await channel.send(reply)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(DISCORD_TOKEN)
