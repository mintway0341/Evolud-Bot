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

    if message.content.startswith("!형량추가"):
        plus = random.randrange(1,1500)


        print_first = "[MINT 감옥] JR님의 형량을 " + str(plus) + "년 추가했습니다! ("
        for i in range (0, plus) :
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

    if message.content.startswith("!탈퇴"):
        embed = discord.Embed(title="불가능합니다.", description="테마 만드세요.", color=0x63A2FF)
        await message.channel.send(embed=embed)
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
