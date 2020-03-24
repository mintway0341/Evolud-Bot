import discord
import random
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("JR님 형량 추가")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event

async def on_message(message):
    if message.author.bot:
        return None

    id = message.author.id
    channel = message.channel  # channel

    if message.content.startswith("!노동"):
        embed = discord.Embed(title="좋은 마음가짐이에요.", description="테마 만드세요.", color=0x63A2FF)
        await message.channel.send(embed=embed)
        
    if message.content.startswith("!노동반대"):
        plus = random.randrange(1, 1501)
        print_first = "[MINT 감옥] JR님의 형량을 " + str(plus) + "년 추가했습니다! ("
        print(plus // 10)
        for i in range(0, plus // 10):
            print_first += "짝"
        print_first += ")"

        embed = discord.Embed(title="노동반대하면 안됩니다.", description=print_first, color=0x63A2FF)
        await message.channel.send(embed=embed)

    if message.content.startswith("!형량추가"):
        plus = random.randrange(1,1501)

        if plus < 51 :
            print_first = "귀 찮 아 ^^"
        elif plus < 101 :
            print_first = "그 만 불 러 ^^"
        elif plus < 151:
            print_first = "시 끄 러 워 ^^"
        else :
            print_first = "[MINT 감옥] JR님의 형량을 " + str(plus) + "년 추가했습니다! ("
            print(plus // 10)
            for i in range (0, plus // 10) :
                print_first += "짝"
            print_first += ")"

        embed = discord.Embed(title="축하드립니다.", description=print_first, color=0x63A2FF)
        await message.channel.send(embed=embed)

        # await message.channel.send(print_first)

    if message.content.startswith("!형량삭감"):
        plus = random.randrange(1, 10)
        print_first = "[MINT 감옥] JR님의 형량을 " + str(plus) + "년 삭감했습니다! ("
        for i in range(0, plus):
            print_first += "짝"
        print_first += ")"

        embed = discord.Embed(title="축하드립니다.", description=print_first, color=0x63A2FF)
        await message.channel.send(embed=embed)

        # await message.channel.send(print_first)

    if message.content.startswith("!탈퇴") or message.content.startswith("!퇴사") or message.content.startswith("!탈옥") or message.content.startswith("!탈주") or message.content.startswith("!사망"):
        embed = discord.Embed(title="불가능합니다.", description="테마 만드세요.", color=0x63A2FF)
        await message.channel.send(embed=embed)

    if message.content.startswith("!인피케이"):
        rand = random.randrange(1, 101)
        if rand % 5 == 0:
            embed = discord.Embed(title="임의의 ε>0 에 대하여...", description="수학 공부 중입니다.", color=0x63A2FF)
        elif rand % 5 == 1:
            embed = discord.Embed(title="Q.E.D.", description="수학 공부 중입니다.", color=0x63A2FF)
        elif rand % 5 == 2:
            embed = discord.Embed(title="이를 적기에는 여백이 부족하다.", description="수학 공부 중입니다.", color=0x63A2FF)
        elif rand % 5 == 3:
            embed = discord.Embed(title="리만 제타 함수 ζ(0)을 만족하는...", description="수학 공부 중입니다.", color=0x63A2FF)
        else:
            embed = discord.Embed(title="S가 내적공간 V의 부분집합일때...", description="수학 공부 중입니다.", color=0x63A2FF)
        await message.channel.send(embed=embed)

    if message.content.startswith("!인피케잌"):
        rand = random.randrange(1, 101)
        if rand % 4 == 0 :
            embed = discord.Embed(title="고구마 케잌", description="🍠🍰", color=0x63A2FF)
        elif rand % 4 == 1 :
            embed = discord.Embed(title="딸기 케잌", description="🍓🍰", color=0x63A2FF)
        elif rand % 4 == 2 :
            embed = discord.Embed(title="아이스크림 케잌", description="🍦🍰", color=0x63A2FF)
        else :
            embed = discord.Embed(title="초코 케잌", description="🍫🍰", color=0x63A2FF)
        await message.channel.send(embed=embed)

    if message.content.startswith("!민트웨이"):
        rand = random.randrange(1, 101)
        if rand % 5 == 0 :
            embed = discord.Embed(title="나는야 앱등이", description="I like macOS", color=0x63A2FF)
        elif rand % 5 == 1 :
            embed = discord.Embed(title="👨‍💻", description="디스코드 봇 제작중입니다.", color=0x63A2FF)
        elif rand % 5 == 2 :
            embed = discord.Embed(title="🍎", description="Developer at Apple in California", color=0x63A2FF)
        elif rand % 5 == 3:
            embed = discord.Embed(title="✏️", description="심층면접/논술 공부 중입니다.", color=0x63A2FF)
        else :
            embed = discord.Embed(title="✏️", description="선형대수학 공부 중입니다.", color=0x63A2FF)
        await message.channel.send(embed=embed)

    if message.content.startswith("!구름"):
        rand = random.randrange(1, 101)
        if rand % 5 == 0:
            embed = discord.Embed(title="ZZZ", description="잠만", color=0x63A2FF)
        elif rand % 5 == 1:
            embed = discord.Embed(title="👨‍💻", description="디스코드 봇 제작중입니다.", color=0x63A2FF)
        elif rand % 5 == 2:
            embed = discord.Embed(title="🍎", description="Developer at Apple in California", color=0x63A2FF)
        elif rand % 5 == 3:
            embed = discord.Embed(title="✏️", description="심층면접/논술 공부 중입니다.", color=0x63A2FF)
        else:
            embed = discord.Embed(title="✏️", description="선형대수학 공부 중입니다.", color=0x63A2FF)
        await message.channel.send(embed=embed)
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
