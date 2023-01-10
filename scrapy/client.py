from . import settings
import discord

class Client(discord.Client):
    # PRINT WHEN WE ARE READY
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    # WHEN WE SEE A MESSAGE
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        print(message)
        if message.content.startswith('!hello'):
            await message.channel.send(f'Hello, {message.author.name}')