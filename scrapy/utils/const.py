from typing import Union
from pathlib import Path

SCRAPATH : Path = Path(__file__).parent.parent.absolute()
PARENT : Path = SCRAPATH.parent
LOGPATH : Path = SCRAPATH / 'logs.txt'

DEFAULT_SETTINGS_PATH : Path = SCRAPATH / 'default_settings.json'
DEFAULT_COGS_PATH : Path = SCRAPATH / 'cogs'

pathlike = Union[str, Path]
