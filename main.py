import asyncio
import discord
import os
from discord.ext import commands

from help_cog import help_cog
from music_cog import music_cog

intents = discord.Intents.all()

# make commands start with a '/'
bot = commands.Bot(command_prefix="/", intents=intents)

# remove the default help command so that we can use our own
bot.remove_command("help")

async def main():
    async with bot:
        await bot.add_cog(help_cog(bot))
        await bot.add_cog(music_cog(bot))
        await bot.start('MTI1NzgyNjk4ODM2MjY5NDc4OQ.Gw56ly.eDdkhBD3_-CTdP1y78TKGvRh09HEGRzEs-p6xI')

asyncio.run(main())