import discord
import os
import re

client = discord.Client(
    allowed_mentions=discord.AllowedMentions.all()
)

TOKEN = os.environ['TOKEN']


async def reply_instructions(message):
    join_tags = client.get_channel(894244917184987226)
    reply = f"""レイド卵の投稿などのコンテキストメニューを表示し、（写真の外側をロングタップする）、スレッドを作成するからスレッドを作成してください！
Click the Create Thread in the context menu of the post (e.g. The image of egg) to create a new thread.
Please ask participants for your raid to join WantsXxx tags. The instructions are in {join_tags.mention}."""
    await message.channel.send(reply)


async def reply_five(five_role, message):
    reply = f"""{five_role.mention} no instructions"""
    await message.channel.send(reply)


async def reply_one_three(one_three_role, message):
    reply = f"""{one_three_role.mention} no instructions"""
    await message.channel.send(reply)


@client.event
async def on_message(message):
    server = client.get_guild(876131915424489472)
    role_mentions = set(message.role_mentions)

    prog_wants = re.compile("^Wants")
    wants_roles = set(role for role in server.roles if prog_wants.match(
        role.name) is not None)
    if len(wants_roles & role_mentions) > 0 and "no instructions" not in message.content:
        await reply_instructions(message)

    one_three_role = server.get_role(893286398604501032)
    prog_wants13_number = re.compile("^Wants[13]")
    numbered13_roles = set(role for role in server.roles if prog_wants13_number.match(
        role.name) is not None)
    if len(numbered13_roles & role_mentions) > 0:
        await reply_one_three(one_three_role, message)

    five_role = server.get_role(893286159558541362)
    prog_wants5_number = re.compile("^Wants[5]")
    numbered5_roles = set(role for role in server.roles if prog_wants5_number.match(
        role.name) is not None)
    if len(numbered5_roles & role_mentions) > 0:
        await reply_five(five_role, message)

client.run(TOKEN)
