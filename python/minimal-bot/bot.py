import discord
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run('OTgxMjk3ODg3NTI5MDA5MTkz.GT0WT3.cre2E8AF5GlTIVvHe3PTxoGKyK77Q4_voIn3t4')