import datetime
import traceback
from typing import List, Type
from .const import LOGPATH, pathlike


# Filters itens in a list by type.
def filter_by_type(l : List[any], t : Type[any]):
    """Filters itens in a list by type."""
    return filter(lambda x: isinstance(x, t), l)

# The unpack function. It will unpack a list.
def unpack (l : list) -> list:
    """
    This function will try to unpack a deeply nested list. It will return a
    unidimentional standart python3 list.
    """

    itens = [x for x in l if not isinstance(x, list)]
    sublists = [unpack(x) for x in l if isinstance(x, list)]
    unpacked_list = [y for x in sublists if isinstance(x, list) for y in x]
    return itens + unpacked_list


def log(*args, sep : str = ' ', end : str = '\n', start : str = '', log_file : pathlike = LOGPATH) -> str:
    output = f'[{datetime.datetime.now()}] {start + sep.join(map(str, args)) + end}'
    
    print(output)

    with open(log_file, 'a') as f:
        f.write(output)

    return output
