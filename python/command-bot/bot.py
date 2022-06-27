import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_connect():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def test(ctx, arg1, arg2):
    response = '[{2} @{0}] : {1}\n Taged @{3}'.format(ctx.guild, ctx.message.clean_content, ctx.author, ctx.message.mentions[0].name)
    await ctx.send(response)

@bot.command()
async def echo(ctx, *args):
    await ctx.send(args)

@bot.command()
async def clear(ctx):
    await ctx.channel.clone()
    await ctx.channel.purge()

@bot.command()
async def delete(ctx):
    await ctx.channel.delete()

bot.run('OTgxMjk3ODg3NTI5MDA5MTkz.GT0WT3.cre2E8AF5GlTIVvHe3PTxoGKyK77Q4_voIn3t4')