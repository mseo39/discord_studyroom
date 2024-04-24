from dico_token import Token 
from discord.ext import commands
import discord
import datetime

prefix = '!'

# 봇을 생성하고 명령어 기능을 활성화
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

start_time = {} # 시작시간
total_time = {} # 총 시간

def time_calculation(total):
    total_seconds = int(total)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return hours, minutes,seconds

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
        hours,minutes,seconds = time_calculation(total_time[ctx.author.id])
        
        await ctx.send(f"{ctx.author.name}님, 공부를 종료했습니다. 공부한 시간: {hours:02d}:{minutes:02d}:{seconds:02d}")
    else:
        await ctx.send("공부를 시작하지 않았습니다.")

# !ing 명령어 : 현재까지 공부 시간 확인
@bot.command(name='ing')
async def end(ctx):
    
    # 해당 사용자가 없다면
    if ctx.author.id not in total_time:
        await ctx.send("힘차게 공부를 시작해보세요!")
    else:
        # 공부를 하는 중이라면
        if ctx.author.id in start_time:
            # 그전 총시간이랑 현재 공부시간을 합해줘서 계산
            start_t = start_time[ctx.author.id]
            end_t = datetime.datetime.now()
            
            #시분초 계산
            hours,minutes,seconds = time_calculation(total_time[ctx.author.id] + (end_t - start_t).total_seconds())
            
            await ctx.send(f"{ctx.author.name}님, 현재 공부시간: {hours:02d}:{minutes:02d}:{seconds:02d}")
        else:
            # 공부 중이 아니라면
            
            #시분초 계산
            hours,minutes,seconds = time_calculation(total_time[ctx.author.id])
            
            await ctx.send(f"{ctx.author.name}님, 현재 공부시간: {hours:02d}:{minutes:02d}:{seconds:02d}")
        
 
bot.run(Token)