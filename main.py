#Author: porphyri0n - Github link: https://github.com/Porphyri0n
import discord
import os
import json
from discord.ext import commands

bot_token = ""

def get_prefix(client, message):
    with open("./cogs/prefixes.json","r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix= get_prefix, intents = discord.Intents.all())

@client.event
async def on_ready():
    print("bot is ready")
    print("--------------------------------")
    channel = client.get_channel(1004682956918489111)
    await channel.send('Good morning everyone!')

@client.command()
async def load(ctx, extension):
     client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
     client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')




client.run(bot_token)
