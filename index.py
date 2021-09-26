import discord
import os

client = discord.Client()

TOKEN = os.environ['TOKEN']

async def reply(message):
    reply = f'Hey'
    await message.channel.send(reply) # 返信メッセージを送信

@client.event
async def on_message(message):
    if client.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行

client.run(TOKEN)
