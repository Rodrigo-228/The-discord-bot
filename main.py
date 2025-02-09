import discord
from discord.ext import commands
import random
from settings import settings
import os

def is_num(text):
    num=True
    for i in text:
        if i.isalpha():
            num=False
    return num


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
async def bot_page(ctx):
    await ctx.send('https://rodrigo-228.github.io/The_Bot_Page/')

chars=['Bishop', 'Goblin', 'Golem', 'Hornet', 'King_Slime', 'Slime']
spells=['Explosion', 'Fuego', 'Hielo', 'Rayo']
items=['Hacha', 'Hacha de batalla', 'Bomba', 'Paquete Sorpresa', 'Pistola', 'Martillo', 'Imán', 'Baculo', 'Baculo de Invocador']

@bot.command()
async def char(ctx):
    char=random.choice(chars)
    attack=random.randint(1,25)
    hp=random.randint(1,25)
    magic=random.randint(1,25)
    speed=random.randint(1,25)
    spell=[]
    item=[]

    await ctx.send(char)
    
    with open('images/chars/'+char+'.png','rb') as f:
        await ctx.send(file=discord.File(f))
    
    await ctx.send('Estadisticas:')
    
    if attack<25:
        await ctx.send('-Ataque -> '+str(attack))
    else:
        await ctx.send('-Ataque -> max(25)')
    
    if hp<25:
      await ctx.send('-Salud -> '+str(hp))
    else:
        await ctx.send('-Salud -> max(25)')
    
    if magic<25:
       await ctx.send('-Magia -> '+str(magic))
    else:
        await ctx.send('-Magia -> max(25)')
    
    if speed<25:
        await ctx.send('-Velocidad -> '+str(speed))
    else:
        await ctx.send('-Velocidad -> max(25)')
    
    await ctx.send('------')
    await ctx.send('Hechizos:')

    if magic<6:
        await ctx.send('-Ninguno')
    elif magic<14:
        spell.append(random.randint(0,len(spells)-1))
        await ctx.send('-'+spells[spell[0]])
        with open('images/spells/'+os.listdir('images/spells')[spell[0]],'rb') as f:
            await ctx.send(file=discord.File(f))
    elif magic<22:
        for i in range(2):
            z=random.randint(0,len(spells)-1)
            dup=False
            for j in range(len(spell)):
                if z==spell[j]:
                    dup=True
            while dup:
                z=random.randint(0,len(spells)-1)
                dup=False
                for j in range(len(spell)):
                    if z==spell[j]:
                        dup=True
            spell.append(z)
            await ctx.send('-'+spells[spell[i]])
            with open('images/spells/'+os.listdir('images/spells')[spell[i]],'rb') as f:
                await ctx.send(file=discord.File(f))
    else:
        for i in range(3):
            z=random.randint(0,len(spells)-1)
            dup=False
            for j in range(len(spell)):
                if z==spell[j]:
                    dup=True
            while dup:
                z=random.randint(0,len(spells)-1)
                dup=False
                for j in range(len(spell)):
                    if z==spell[j]:
                        dup=True
            spell.append(z)
            await ctx.send('-'+spells[spell[i]])
            with open('images/spells/'+os.listdir('images/spells')[spell[i]],'rb') as f:
                await ctx.send(file=discord.File(f))
    
    await ctx.send('------')
    await ctx.send('Objetos:')

    n=random.randint(0,3)

    if n==0:
        await ctx.send('-Ninguno')
    elif n==1:
        item.append(random.randint(0,len(items)-1))
        await ctx.send('-'+items[item[0]])
        with open('images/items/'+os.listdir('images/items')[item[0]],'rb') as f:
            await ctx.send(file=discord.File(f))
    elif n==2:
        for i in range(2):
            z=random.randint(0,len(items)-1)
            dup=False
            for j in range(len(item)):
                if z==item[j]:
                    dup=True
            while dup:
                z=random.randint(0,len(items)-1)
                dup=False
                for j in range(len(item)):
                    if z==item[j]:
                        dup=True
            item.append(z)
            await ctx.send('-'+items[item[i]])
            with open('images/items/'+os.listdir('images/items')[item[i]],'rb') as f:
                await ctx.send(file=discord.File(f))
    else:
        for i in range(3):
            z=random.randint(0,len(items)-1)
            dup=False
            for j in range(len(item)):
                if z==item[j]:
                    dup=True
            while dup:
                z=random.randint(0,len(items)-1)
                dup=False
                for j in range(len(item)):
                    if z==item[j]:
                        dup=True
            item.append(z)
            await ctx.send('-'+items[item[i]])
            with open('images/items/'+os.listdir('images/items')[item[i]],'rb') as f:
                await ctx.send(file=discord.File(f))
    
    await ctx.send('------')
    await ctx.send('Hecho')


@bot.command()
async def best_game_ever(ctx):
    with open('files/Golmy\'s island.zip','rb') as f:
        await ctx.send('Este es el mejor juego jamas creado')
        await ctx.send(file=discord.File(f))

@bot.command()
async def shaw(ctx):
    await ctx.send('Silksong sale mañana')
    with open('images/chars/Hornet.png','rb') as f:
        await ctx.send(file=discord.File(f))

@bot.command()
async def roll(ctx,n:str):
    if len(n.split('d'))==2:
        result=''
        num=n.split('d')[0]
        dice=n.split('d')[1]
        if is_num(num) and is_num(dice):
            for i in range(int(num)):
                if i!=0:
                    result+=', '
                result+=str(random.randint(1,int(dice)))
            await ctx.send(str(result))
        else:
            await ctx.send('Notation invalida')
    else:
        await ctx.send('Notation invalida')

@bot.command()
async def spam(ctx,n:int): 
    for i in range(n):
        await ctx.send('Esto es spam '+str(i+1))

@bot.command()
async def clean(ctx):
    await ctx.channel.purge()

bot.run(settings['TOKEN'])