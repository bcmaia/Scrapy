import discord
from .consts import *
from .vars import *

from .client import Client

from . import utils

intents = discord.Intents.all()
client = Client(intents=intents)

def run():
    client.run(BOT_TOKEN)