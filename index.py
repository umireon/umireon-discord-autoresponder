import discord
import os

client = discord.Client()

TOKEN = os.environ['TOKEN']

async def reply(message):
    reply = """Click the Create Thread in the context menu of the post (e.g. The image of egg) to create a new thread.
Please ask participants for your raid to join WantsXxx tags. The instructions are in #rules."""
    await message.channel.send(reply) # 返信メッセージを送信

@client.event
async def on_message(message):
    if client.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行

client.run(TOKEN)
