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
    channel = message.channel

    if message.content.startswith("!알려주세요"):
        embed = discord.Embed(title="Evolud Bot 사용방법", description="", color=0x63A2FF)
        embed.add_field(name="노동", value="`!노동`, `!노동반대`, `!노동싫어`", inline=True)
        embed.add_field(name="형량", value="`!형량추가`, `!형량삭감`", inline=True)
        embed.add_field(name="나쁜말", value="`!탈퇴`, `!퇴사`, `!탈옥`, `!탈주`, `!사망`", inline=True)
        embed.add_field(name="노래", value="`!노래추천`", inline=True)
        embed.add_field(name="멤버", value="`!인피케이`, `!infikei`, `!Infikei`, `!INFIKEI`, "
                                         "`!인피케잌`, `!inficake`, `!Inficake`, `!INFICAKE`, "
                                         "`!민트웨이`, `!mintway`, `!Mintway`, `!MintWay`, `!MINTWAY`, "
                                         "`!구름`, `!cloud`, `!Cloud`, `!CLOUD`, "
                                         "`!jr`, `!Jr`, `!JR`, `!jwr`, `!JwR`, `!JWR`, `!제이알`, `!화련`", inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith("!노동반대") or message.content.startswith("!노동싫어"):
        plus = random.randrange(1, 1501)
        print_first = "[MINT 감옥] JR님의 형량을 " + str(plus) + "년 추가했습니다! ("
        print(plus // 10)
        for i in range(0, plus // 10):
            print_first += "짝"
        print_first += ")"

        embed = discord.Embed(title="노동반대하면 안됩니다.", description=print_first, color=0x63A2FF)
        await message.channel.send(embed=embed)

    elif message.content.startswith("!노동") and (len(message.content) == 3):
        embed = discord.Embed(title="좋은 마음가짐이에요.", description="테마 만드세요.", color=0x63A2FF)
        await message.channel.send(embed=embed)

    if message.content.startswith("!형량추가"):
        plus = random.randrange(1,1501)

        if plus < 501 :
            embed = discord.Embed(title="오류", description="귀 찮 아 ^^", color=0x63A2FF)
        elif plus < 101 :
            embed = discord.Embed(title="오류", description="그 만 불 러 ^^", color=0x63A2FF)
        elif plus < 151:
            embed = discord.Embed(title="오류", description="시 끄 러 워 ^^", color=0x63A2FF)
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

    if message.content.startswith("!인피케이") or message.content.startswith("!infikei") or message.content.startswith("!Infikei") or message.content.startswith("!INFIKEI"):
        rand = random.randrange(1, 101)
        if rand % 5 == 0:
            embed = discord.Embed(title="임의의 ε>0 에 대하여...", description="수학 공부 중입니다.", color=0x63A2FF)
        elif rand % 5 == 1:
            embed = discord.Embed(title="Q.E.D.", description="수학 공부 중입니다.", color=0x63A2FF)
        elif rand % 5 == 2:
            embed = discord.Embed(title="증명을 적기에는 여백이 부족하다.", description="수학 공부 중입니다.", color=0x63A2FF)
        elif rand % 5 == 3:
            embed = discord.Embed(title="리만 제타 함수 ζ(0)을 만족하는...", description="수학 공부 중입니다.", color=0x63A2FF)
        else:
            embed = discord.Embed(title="S가 내적공간 V의 부분집합일때...", description="수학 공부 중입니다.", color=0x63A2FF)
        await message.channel.send(embed=embed)

    if message.content.startswith("!인피케잌") or message.content.startswith("!inficake") or message.content.startswith("!Inficake") or message.content.startswith("!INFICAKE"):
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

    if message.content.startswith("!민트웨이") or message.content.startswith("!mintway") or message.content.startswith("!Mintway") or message.content.startswith("!MintWay") or message.content.startswith("!MINTWAY"):
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

    if message.content.startswith("!구름") or message.content.startswith("!cloud") or message.content.startswith("!Cloud") or message.content.startswith("!CLOUD"):
        rand = random.randrange(1, 101)
        if rand % 4 == 0:
            embed = discord.Embed(title="ZZZ", description="잠만보", color=0x63A2FF)
        elif rand % 4 == 1:
            embed = discord.Embed(title="ZZZZZZZZ", description="잠만보", color=0x63A2FF)
        elif rand % 4 == 2:
            embed = discord.Embed(title="몽실몽실", description="CLOUD UX 2020", color=0x63A2FF)
        else:
            embed = discord.Embed(title="!", description="닉네임 변경 중입니다.", color=0x63A2FF)
        await message.channel.send(embed=embed)

    if message.content.startswith("!jr") or message.content.startswith("!Jr") or message.content.startswith("!JR") or message.content.startswith("!jwr") or message.content.startswith("!JWR") or message.content.startswith("!JwR"):
        rand = random.randrange(1, 101)
        if rand % 4 == 0:
            embed = discord.Embed(title="노동 중", description="테마 제작은 재밌어요!!", color=0x63A2FF)
        elif rand % 4 == 1:
            embed = discord.Embed(title="나도 앱등이", description="에어팟 프로는 현존 최고의 코드리스 이어폰이죠.", color=0x63A2FF)
        elif rand % 4 == 2:
            embed = discord.Embed(title="고먐미", description="냥냥냥", color=0x63A2FF)
        else:
            embed = discord.Embed(title="앵그리 JwR", description="닉네임 그만 변경하세요ㅡㅡ", color=0x63A2FF)
        await message.channel.send(embed=embed)

    if message.content.startswith("!제이알"):
        embed = discord.Embed(title="KING OF KLCK", description="JR님 만세!!!!!", color=0x63A2FF)
        await message.channel.send(embed=embed)

    if message.content.startswith("!화련"):
        embed = discord.Embed(title="고객 지원팀 보스", description="안녕하세요. 상담원 화련입니다.", color=0x63A2FF)
        await message.channel.send(embed=embed)

    if message.content.startswith("!노래추천"):
        rand = random.randrange(1, 101)
        if rand % 4 == 0:
            embed = discord.Embed(title="엪취리칠", description="https://www.youtube.com/watch?v=Zyi9QUB-fyo", color=0x63A2FF)
        elif rand % 4 == 1:
            embed = discord.Embed(title="노동하세요", description="https://www.youtube.com/watch?v=TpPwI_Lo0YY", color=0x63A2FF)
        elif rand % 4 == 2:
            embed = discord.Embed(title="난난난난나", description="https://www.youtube.com/watch?v=QUXKib-jfEM", color=0x63A2FF)
        else:
            embed = discord.Embed(title="YEEEEEEEEE", description="https://www.youtube.com/watch?v=q6EoRBvdVPQ", color=0x63A2FF)
        await message.channel.send(embed=embed)
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
