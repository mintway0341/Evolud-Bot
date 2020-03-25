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
        embed = discord.Embed(title="Evolud Bot 사용방법", description="!노동 / !노동반대 / !노동싫어 / !형량추가 / !형량삭감 / \n!탈퇴 / !퇴사 / !탈옥 / !탈주 / !사망 / \n!인피케이 / !infikei / !Infikei / !INFIKEI / \n!인피케잌 / !inficake / !Inficake / !INFICAKE / \n!민트웨이 / !mintway / !Mintway / !MintWay / !MINTWAY / \n!구름 / !cloud / !Cloud / !CLOUD / \n!jr / !Jr / !JR / !jwr / !JwR / !JWR", color=0x63A2FF)
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

    if message.content.startswith("!노래추천"):
        rand = random.randrange(1, 101)
        if rand % 4 == 0:
            embed = discord.Embed(title="엪취리칠", description="https://www.youtube.com/watch?v=Zyi9QUB-fyo", color=0x63A2FF)
            embed.set_image(url="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAEEAdAMBIgACEQEDEQH/xAAbAAABBQEBAAAAAAAAAAAAAAAEAAIDBQYBB//EADsQAAIBAwMBBQUDCgcAAAAAAAECAwAEEQUSITEGE0FRYRQiMnGBcpGhFSMzNDZCc7HB8BY1Q1KD0eH/xAAaAQACAwEBAAAAAAAAAAAAAAACAwQFBgEA/8QAJREAAgIBAwQCAwEAAAAAAAAAAAECAxEEIUESIjEyUXEUM2ET/9oADAMBAAIRAxEAPwAmYiOVrcoRcHLYznA8vnmu6aJ01S3jO8qZl93GdvPU/dUWp6jbWt1cLcRymVn70d2CxOTwRg8eHlUnZe+N/qMcjW7wgyLhpPifAPODz/fWpb8EBLu2AtenWLXGdyQcklxyBwcVU6Vayf4YVNwd2PUE4wWyP6fjRetzN7RfuQrKJCMP5Y9fnU2mRdx2ehOC8BJK4YdSG2n6HnHpVdXLqsaXgu9anCuGeSTQImt2uIpICSVB3qeDjIIzVvo8dxDJcBXMUEQYRxNyvnuoTTbuKO59knQd3IC2STl+cEfiKvtKFr7L3do4eJGKfUdRRXLhECpZDrWRZYEeNwysoIK9CKnHzNQoixRhY1AVRgKKlXOMkYri2RIQpCdhwTQOqMy2THJ6Gjn+E0HqozZkeamuw90I1W1Mvowc3xGhW5NFXXB+tCE88VdqKRiYTl8ixXc0h603NEsBqcvkaSc12uGu0eEF1S+TdJpNtNLK0iQmMEDIkYnPj+9gUTb2djZSKIFjSRQWTagz6812JtOAkga4Q7334LdT6fdTpJbCLBR8lVKrjJxUFqRoouJiLuIy22otMoUbyAqoFUlgB4f+Ufdxyjs1FBZARvvEaMWyM4IB8adDpk11LNpTnupZpQxLt0QMCTnw4BxV9caDcDRYClzEwiR7tnKsu5Y+owec+8KqdPGUbJuXLLjV2KyqEYvOEA9m7c+w2zTKskit7zHxIxmry3gjg3LGioCScChNG0mW70a1nFwscUkckne5IMQB2n61eWum9xpsKEi4lFuC028++27AP1p9jzIjV7IGFdBJ9Rn8aKlsHiR272NzGQJFXqmfOi4bKJkgOwENFGznOOSeaHA7JVsMqaEv8tb4A/dNXM2nFpHEMiELJtK55UHpmoLvT/zbRm4hBUYPU4PlxXo+6YvUd1UkeWXr5kbHIBxQw8881p7zsrPbrPLeX9pbQxzGMtIT1wCPnkHpQF52cubH8omeaILY7NzYOJC490LVqrEzH/i2xW6KYscc0wHxpHkVwdMU6LF4wdzSptKiPF7bXVwjo50gx7RuG+ReT6EHpTvy3qM4b2XTkwG2Ek+Pl0qxsLTvI2jv7TOBhXi91Tkcg8sc/d9c0TDZxW6FI1kjiBJ96Tx+lROrPlmh6ElshlhI2lqvaO+hUyrmNreNjgZIG4E+PH40drXauO0hsBJZtNDcJNBJG0p3NG4BPPnkCgr60aexgAlkW32s7RxjPeEc4wetUHal/c0wxwPGB3m1X8sL1qC8ux5JNfbE1dhrdpPoq2r2TQaesEkLwpOS/dk53ZHIP/Zq3stbiEaWtpaSrFHAojkZsgjORz1JrH6JK9tYxTzSxdyynk4XamCMsfHpV5oslzLZRyXZjLtzmL4SPDFJm8SRIr3L+4vI5Yp1jh7tp8d627PjnjyqWLUtkaIY/hjROG/2nNVo+Zp1dyOwg86kiM0kUG1nkDPls5+VA6hqy21rOzRMe8YOO7faflnypjj3T69ap+0TAW21c9AaKveaRG1sv89PKSKntV2i/K9q8AtTGDcicktnom3FP7V6vFNo+m6ZBdR3LxIDcTxqQH2jCA568E/WqC6H5w0Ix8MVaKuO2DKrVWSTzydxXdtcXmnke7T0IbIiKVInmlXQj1d7S0VMyXiqPnQNzp+iuwkubh5uOF3Hb91U+mzzPAr95uDxBlQ+HAzRU0qxuGlmwOMDIwarvBqW0+CO6hvIbP262ktV09V224EZ3jJxkjx58Koe07OYtLNw5L7HJYqBz7vhWhhnmk7KiYyIIIWZX2jJOHGMVnO0Vyl3DYFRjMT4LeOcc/35VHe0huO0L017oafENNht2lkOzDHhgQAWPHXHh6VpNLNzsZLmCKPYcJ3ZyCPP0rFnUJ7GxhvoImD7O6DOeFGcbsVqdPWS6a2vjcNtEfKL8LE+NR556kuRlbRexrvZVyASQOaOv7AWqKyuzZYqdy7eniPSq9fvFTSSvJjeSdvTLE0fA4ik4TJ6HpVT2hXNoGHlVrIqsMsASvT0qu1pN1lhenNdr2sRH10erTyX8MRd/ET6UD1NHXZ2jHjQKnFXCaMZWmkPjGDUj8imA5604kYo0zzW5CRzSrpIzSruQ8M08H6Bf4AoTV/9L7I/lSpVWs1a8Cb/ACn/AJ/6iq/tR+v2H8J6VKlT9g14J9T/AGdf5VotM/Zu0+wP50qVKu919B1exorf4B9kVMKVKvcD0ck/Rt8qrtQ/Uo/rSpVxeyF3fqZhNQ+I/OgV6UqVWBnY+CRa63SlSo0eIT1pUqVdCP/Z")
        elif rand % 4 == 1:
            embed = discord.Embed(title="노동하세요", description="https://www.youtube.com/watch?v=TpPwI_Lo0YY", color=0x63A2FF)
            embed.set_image(url="data:image/jpeg;base64,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")
        elif rand % 4 == 2:
            embed = discord.Embed(title="난난난난나", description="https://www.youtube.com/watch?v=QUXKib-jfEM", color=0x63A2FF)
            embed.set_image(url="data:image/jpeg;base64,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")
        else:
            embed = discord.Embed(title="YEEEEEEEEE", description="https://www.youtube.com/watch?v=q6EoRBvdVPQ", color=0x63A2FF)
            embed.set_image(url="data:image/jpeg;base64,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")
        await message.channel.send(embed=embed)
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
