import traceback
from pathlib import Path
from types import ModuleType
from typing import Union, List
import discord
from discord.ext import commands
from . import cogs
from . import utils
from .utils.fun import log


cogs_type = commands.Cog | type | List[commands.Cog] | List[type]

THIS_PATH = Path(__file__).parent.absolute()


class Bot:
    def __init__ (self, settings : Union[dict, str, Path] = utils.config.DEFAULT_SETTINGS, extra_cogs : List[ModuleType] = []):
        self.settings = utils.config.read_settings(settings)
        self.cogs = utils.cog.get_cogs([cogs] + extra_cogs)
        self.client = commands.Bot(
            command_prefix = self.settings['prefix'],
            intents = discord.Intents.all(),
        )             

    async def _init(self):
        await self.add_cog(self.cogs)
        return self

    async def create (settings : Union[dict, str, Path] = utils.config.DEFAULT_SETTINGS, extra_cogs : List[ModuleType] = []):
        log('Starting the initialization of a new bot.', start = '\n\n')

        bot = Bot()
        await bot._init()

        log('New bot Created.', end='\n\n')

        return bot

    def run (self):
        log('Starting the client...')
        self.client.run(self.settings['token'])
        return self

    async def add_cog (self, cogs : cogs_type):
        if not isinstance(cogs, list):
            cogs = [cogs]
            log('Attempting to add a lonely cog.')
        else:
            log('Attempting to add a batch of cogs.')

        successes = 0
        failures = 0

        for cog in cogs:
            try:
                await self.client.add_cog(cog(self.client))
                log(f'Added new cog: {cog.__name__} {cog}')
                successes += 1
            except Exception as e:
                log(
                    f'Failed to add new cog: {cog.__name__} {cog}'
                    + f' due to an error:' + f'\n!->>> {e}\n'
                    + traceback.format_exc()
                )
                failures += 1
        
        log(f'All {successes + failures} cog operations finished with {failures} failures.')
        return self


        
        
