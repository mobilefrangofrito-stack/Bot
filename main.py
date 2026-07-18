import discord
import os
from discord.ext import commands

# Pega o token das variáveis de ambiente do Render
TOKEN = os.getenv('TOKEN')

# Permissões do bot
intents = discord.Intents.default()
intents.message_content = True

# Prefixo do bot
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} tá online!')
    print('Bot 24/7 no ar 🔥')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')

# Roda o bot
bot.run(TOKEN)
