import discord
import json
from discord.ext import commands

class prefix(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open("./cogs/prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = "."

        with open("./cogs/prefixes.json", "w") as f:
            json.dump(prefixes, f, indent = 4)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open("./cogs/prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open("./cogs/prefixes.json", "w") as f:
            json.dump(prefixes, f, indent = 4)

    @commands.command()
    async def changeprefix(self, ctx, prefix):
        with open("./cogs/prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open("./cogs/prefixes.json", "w") as f:
            json.dump(prefixes, f, indent = 4)

        await ctx.send("prefix has changed to: "+ str(prefix))


def setup(client):
    client.add_cog(prefix(client))
