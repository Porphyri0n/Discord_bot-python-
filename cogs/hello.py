#Author: porphyri0n - Github link: https://github.com/Porphyri0n
import discord
from discord.ext import commands

class hello(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hi")

def setup(client):
    client.add_cog(hello(client))
