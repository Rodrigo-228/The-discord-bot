import discord
from discord.ext import commands
import random
from settings import settings
import os

description = 'hi'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def roll(ctx,n: str):
    if len(n.split('d'))==2:
        result=''
        num=int(n.split('d')[0])
        dice=int(n.split('d')[1])
        for i in range(num):
            if i!=0:
                result+=', '
            result+=str(random.randint(1,dice))
        await ctx.send(str(result))
    else:
        await ctx.send('Invalid notation')

@bot.command()
async def spam(ctx,n: int): 
    for i in range(n):
        await ctx.send('This is spam '+str(i+1))

bot.run(settings["TOKEN"])