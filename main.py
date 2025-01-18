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

# Load the token from the 'token.txt' file
def load_token():
    try:
        with open("token.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Error: 'token.txt' file not found.")
        exit()

async def main():
    async with bot:
        await bot.add_cog(help_cog(bot))
        await bot.add_cog(music_cog(bot))
        await bot.start(load_token())

asyncio.run(main())