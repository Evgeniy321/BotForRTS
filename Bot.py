import discord
from discord.ext import commands
import requests
import asyncio
import time





DISCORD_BOT_TOKEN = '' #токен

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_voice_state_update(message, before, after,):
    if before.channel is None and after.channel is not None:
        channel = client.get_channel(975044149189435472)
        await channel.send(embed = discord.Embed(description = f'Посмотрите консоль!', colour = discord.Color.green()))
        print('Введите айди канала')
        channelid = input()
        chid = int(channelid)
    elif before.channel is not None and after.channel is None:
        channel1 = client.get_channel(975044149189435472)
        await channel1.send(embed = discord.Embed(description = f'1. Как тебе сегодняшний урок?', colour = discord.Color.green()))
        await channel1.send(embed = discord.Embed(description = f'**Подсказка**', colour = discord.Color.green()))
        await channel1.send(embed = discord.Embed(description = f'Что-бы ответить пиши 1.(Ответ)', colour = discord.Color.green()))

@client.event
async def on_message(message):
    if message.content.startswith('1.'):
        seconds = time.time()
        date = time.ctime(seconds)
        member = message.author
        mcontent = message.content
        channel = client.get_channel(975044149189435472)
        logchannel = client.get_channel(975118850947444816)
        await message.send(embed = discord.Embed(description = f'Спасибо за оценку!', colour = discord.Color.green()))
        await logchannel.send(embed = discord.Embed(description = f'+1 Log', colour = discord.Color.green()))
        await logchannel.send(embed = discord.Embed(description = f'Человек: {member.mention}', colour = discord.Color.green()))
        await logchannel.send(embed = discord.Embed(description = f'``Сообщение: {mcontent}``', colour = discord.Color.green()))
        await logchannel.send(embed = discord.Embed(description = f'``Дата: {date}``', colour = discord.Color.green()))









client.run(DISCORD_BOT_TOKEN)


