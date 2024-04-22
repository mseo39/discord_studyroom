from dico_token import Token 
from discord.ext import commands
import discord
import datetime

prefix = '!'

# 봇을 생성하고 명령어 기능을 활성화
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

start_time = {} # 시작시간
total_time = {} # 총 시간

# 봇이 준비되었을 때 실행되는 이벤트
@bot.event
async def on_ready():
    print(f'{bot.user.name}과 함께 공부를 시작해봐요!')

# !S 명령어
@bot.command(name='s')
async def start(ctx):
    # 공부 처음 시작일 때
    if ctx.author.id not in total_time  and ctx.author.id not in start_time:
        start_time[ctx.author.id]=datetime.datetime.now()
        total_time[ctx.author.id] = 0
        await ctx.send(f'{ctx.author.name}님 공부 시작')
    elif ctx.author.id in total_time:
        # 처음 시작이 아니라면
        
        # 중단된 상태라면
        if ctx.author.id not in start_time:
            start_time[ctx.author.id]=datetime.datetime.now()
            await ctx.send(f'{ctx.author.name}님 공부 다시 시작')
        else:
            # 하고 있는 상태라면
            await ctx.send(f'{ctx.author.name}님, 이미 하고 계신걸요!')

@bot.command(name='e')
async def end(ctx):
    global start_time
    # 해당 사용자가 있고 공부를 시작했다면
    if ctx.author.id in start_time:
        start_t = start_time.pop(ctx.author.id)
        end_t = datetime.datetime.now()
        total_time[ctx.author.id] += (end_t - start_t).total_seconds()
        
        #시분초 계산
        total_seconds = int(total_time[ctx.author.id])
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60 
        
        
        await ctx.send(f"{ctx.author.name}님, 공부를 종료했습니다. 공부한 시간: {hours:02d}:{minutes:02d}:{seconds:02d}")
    else:
        await ctx.send("공부를 시작하지 않았습니다.")
 
bot.run(Token)