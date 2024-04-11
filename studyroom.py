from dico_token import Token 
from discord.ext import commands
import discord

# 봇의 설정
prefix = '!'  # 명령어 접두사

# 봇을 생성하고 명령어 기능을 활성화
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

# 봇이 준비되었을 때 실행되는 이벤트
@bot.event
async def on_ready():
    print(f'{bot.user.name}이(가) 준비되었습니다.')

# !hello 명령어
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('안녕하세요!')
 
bot.run(Token)