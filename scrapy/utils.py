import discord
import os
import pathlib
import json

def ReadSettings(path = ''):
    absolute_path = str(pathlib.Path(__file__).parent.absolute()) + '/'
    directory = absolute_path + path + 'settings'
    settings = {}

    for filename in os.scandir(directory):
        pieces = filename.name.split('.')

        if filename.is_file() and '' != pieces[0] and 'json' == pieces[1]:
            with open(filename.path) as f:
                settings[pieces[0]] = json.load(f)
    
    return settings
                

