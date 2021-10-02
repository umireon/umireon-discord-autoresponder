import discord
import os
import re

client = discord.Client()

TOKEN = os.environ['TOKEN']

async def reply(message):
    rules = client.get_channel(889512252472959018)
    reply = f"""Click the Create Thread in the context menu of the post (e.g. The image of egg) to create a new thread.
Please ask participants for your raid to join WantsXxx tags. The instructions are in {rules.mention}."""
    await message.channel.send(reply)

@client.event
async def on_message(message):
    server = client.get_guild(876131915424489472)
    prog = re.compile("^Wants")
    roles = set(role for role in server.roles if prog.match(role.name) is not None)
    role_mentions = set(message.role_mentions)
    if len(roles & role_mentions) > 0:
        await reply(message)

client.run(TOKEN)
