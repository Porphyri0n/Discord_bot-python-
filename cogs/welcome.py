import discord
from discord.ext import commands

class welcome(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined a server')
        await member.send(f'{member} Welcome to our server!')
        for channel in member.guild.channels:
            if str(channel) == "member-log":
                await channel.send(f"""Welcome to the server {member.mention}""")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server')
        for channel in member.guild.channels:
            if str(channel) == "member-log":
                await channel.send(f'{member} has left a server')


def setup(client):
    client.add_cog(welcome(client))
