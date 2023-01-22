from importlib import import_module
from types import ModuleType
from typing import List, Union, Type
from discord.ext import commands
from pathlib import Path
from .const import pathlike, SCRAPATH, DEFAULT_COGS_PATH
from .fun import unpack, filter_by_type


# Some cool lambda functions
is_cog = lambda x: isinstance(x, type) and issubclass(x, commands.Cog)
is_mod = lambda x: isinstance(x, ModuleType)


# This function will extract contents from a module.
def extract_mod_content (mod : ModuleType) -> List[any]:
    """This function will extract contents from a module."""

    # First we filter out stuff like "__name__"
    names = [key for key in mod.__dict__.keys() if key[0:2] + key[-2:] != '____']

    # Extracting the Content
    return [mod.__dict__[key] for key in names]


def seek_cogs (mod : ModuleType, depth : int = 5):
    """This function will seek cogs in a module."""

    # Avoiding the inclussion of discord.py classes
    if ('discord' == mod.__name__.split('.')[0]):
        return []

    # Extracing content and classes
    children = extract_mod_content(mod)
    classes = filter(is_cog, children)

    # Check if we exeded the recursion depth limit
    if 0 >= depth:
        return list(classes)

    # Filtering and returning cogs
    submodules = filter(is_mod, children) 
    return [seek_cogs(sm, depth - 1) for sm in list(submodules)] + list(classes)
     

# This function will get a list of cogs from a module.
def get_cogs(mod : list | ModuleType) -> List[any]:
    """This function will get a list of cogs from a module."""

    if isinstance(mod, list):
        return unpack([get_cogs(m) for m in mod])
    
    return unpack(seek_cogs(mod))
    
