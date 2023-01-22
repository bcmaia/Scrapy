import json
from pathlib import Path
from typing import Union
from .const import SCRAPATH, DEFAULT_SETTINGS_PATH

def read_settings (path : Union[str, Path, dict] = DEFAULT_SETTINGS_PATH) -> dict:
    if isinstance(path, dict):
        return path
    
    settings = dict()
    with open(DEFAULT_SETTINGS_PATH) as f:
        settings = json.load(f)
    return settings

DEFAULT_SETTINGS = read_settings()
