import discord
import os
import re

client = discord.Client()

TOKEN = os.environ['TOKEN']


async def reply_instructions(message):
    join_tags = client.get_channel(894244917184987226)
    reply = f"""Click the Create Thread in the context menu of the post (e.g. The image of egg) to create a new thread.
Please ask participants for your raid to join WantsXxx tags. The instructions are in {join_tags.mention}."""
    await message.channel.send(reply)


async def reply_one_three(message):
    join_tags = client.get_channel(894244917184987226)
    reply = f"""Click the Create Thread in the context menu of the post (e.g. The image of egg) to create a new thread.
Please ask participants for your raid to join WantsXxx tags. The instructions are in {join_tags.mention}."""
    await message.channel.send(reply)


@client.event
async def on_message(message):
    server = client.get_guild(876131915424489472)
    prog = re.compile("^Wants")
    roles = set(role for role in server.roles if prog.match(
        role.name) is not None)
    role_mentions = set(message.role_mentions)
    if len(roles & role_mentions) > 0:
        await reply_instructions(message)

    rufflet_role = server.get_role(893294731436625970)
    chansey_role = server.get_role(893487840133017661)
    one_three_roles = set(rufflet_role, chansey_role)
    if len(one_three_roles & role_mentions) > 0:
        await reply_one_three(message)

client.run(TOKEN)
