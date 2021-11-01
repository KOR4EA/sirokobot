import discord
import asyncio
import random

client = discord.Client()

token = "OTAzODY0ODgwMzQ2NTc4OTY0.YXzLxA.Iq4EszvEBG4Iew7Ro0gR_NtC7FE"

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 시로코 봇이 가동중!')
    game = discord.Game('봇이 성공적으로 가동중!')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "시로코":
        await message.channel.send("왜 그래요 센세")

    if message.content == "심심해":
        await message.channel.send("소금 찍어 먹으셈")

    if message.content == "안녕 시로코":
        await message.channel.send("곤니치와, 센세")

    if message.content == "끝말잇기 하자":
        await message.channel.send("칼륨")

    if message.content == "놀아줘":
        await message.channel.send("총 들고 모험을 떠나 볼까요?")

    if message.content == "숨바꼭질 하자":
        await message.channel.send("여기 인터넷인데 어케함")

    if message.content == "블루아카이브 언제 나옴":
        await message.channel.send("11월 쯤에 나옴")

    if message.content == "시로코 자폭해":
        await message.channel.send("싫은데?")

    if message.content == "시로코 뭐해?":
        await message.channel.send("니가 뭔데 나한테 뭐하냐고 함?")

    if message.content == "시로코 너는 뭘 좋아해?":
        await message.channel.send("운동, 자전거 타기, 조깅을 좋아해~")
    
    if message.content == "시로코 나랑 운동할래?":
        await message.channel.send("자전거 타고 가자~")
    
    if message.content == "시로코 여기 물":
        await message.channel.send("아리가토, 센세!")

    if message.content == "시로코 멍청이":
        await message.channel.send("니가 더 멍청이야 총 맞을래?")

    if message.content == "시로코 에니메이션 노래 추천해줘":
        ran = random.randint(0,3)
        if ran == 0:
            d = "https://www.youtube.com/watch?v=2TCqIaVV2LU"
        if ran == 1:
            d = "https://www.youtube.com/watch?v=K6wVTP3LiEU"
        if ran == 2:
            d = "https://www.youtube.com/watch?v=HWoGmUhX8D0"
        if ran == 3:
            d = "https://youtu.be/DWc00UtMHQA"
        await message.channel.send(d)

    if message.content == "랜덤 뽑기":
        ran = random.randint(0,1)
        if ran == 0:
            d = "꽝입니다."
        if ran == 1:
            d = "당첨입니다!"
        await message.channel.send(d)

    if message.content == "행운의 점수":
        ran = random.randint(0,5)
        if ran == 0:
            d = "0점"
        if ran == 1:
            d = "1점"
        if ran == 2:
            d = "2점"
        if ran == 3:
            d = "3점"
        if ran == 4:
            d = "4점"
        if ran == 5:
            d = "5점"
        await message.channel.send(d)

    if message.content == "나 잘생겼니?":
        ran = random.randint(0,1)
        if ran == 0:
            d = "못생겼네요."
        if ran == 1:
            d = "잘생겼습니다."
        await message.channel.send(d)
 
 
client.run(token)