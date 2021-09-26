import discord
import os

client = discord.Client()

TOKEN = os.environ['TOKEN']

async def reply(message):
    rules = client.get_channel(889512252472959018)
    reply = f"""Click the Create Thread in the context menu of the post (e.g. The image of egg) to create a new thread.
Please ask participants for your raid to join WantsXxx tags. The instructions are in {rules.mention}."""
    await message.channel.send(reply) # 返信メッセージを送信

@client.event
async def on_message(message):
    server = client.get_guild(876131915424489472)
    mega_role = server.get_role(890106825817587723)
    uxie_role = server.get_role(890106629830361099)
    mesprit_role = server.get_role(890106668220821545)
    azelf_role = server.get_role(890106033920442368)
    threestar_role = server.get_role(890106737183572019)
    onestart_role = server.get_role(890106793689231360)
    if mega_role in message.role_mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行
    elif uxie_role in message.role_mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行
    elif mesprit_role in message.role_mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行
    elif azelf_role in message.role_mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行
    elif threestar_role in message.role_mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行
    elif onestart_role in message.role_mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行

client.run(TOKEN)
