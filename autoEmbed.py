import discord
from discord.ext import commands
from dotenv import load_dotenv

import time

from pytube import YouTube
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if "www.youtube.com/" in message.content:
        for file in os.listdir('C:\\Users\\rhero\\Documents\\DiscordYoutube\\'):
            if file.endswith(".mp4"):
                os.remove(file)
        yt = YouTube(message.content)
        await message.delete()
        try:
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        except:
             await message.channel.send("Bad link.")
        success = False
        for x in range(10):
            for file in os.listdir('C:\\Users\\rhero\\Documents\\DiscordYoutube\\'):
                if file.endswith(".mp4"):
                    await message.channel.send(file=discord.File(file))
                    os.remove(file)
                    success = True
                    break
            time.sleep(3)
        if success != True:
            await message.channel.send("Download Failed.")
client.run(TOKEN)
