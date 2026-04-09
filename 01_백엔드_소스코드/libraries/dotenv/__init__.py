# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from typing import Any, Optional
from main import dotenv_values, find_dotenv, get_key, load_dotenv, set_key, unset_key

def load_ipython_extension(ipython = None):
    load_ipython_extension = load_ipython_extension
    import ipython
    load_ipython_extension(ipython)


def get_cli_string(path = None, action = None, key = None, value = (None, None, None, None, None), quote = ('path', Optional[str], 'action', Optional[str], 'key', Optional[str], 'value', Optional[str], 'quote', Optional[str])):
    '''Returns a string suitable for running as a shell script.

    Useful for converting a arguments passed to a fabric task
    to be passed to a `local` or `run` command.
    '''
    command = [
        'dotenv']
    if quote:
        command.append(f'''-q {quote}''')
    if path:
        command.append(f'''-f {path}''')
    if action:
        command.append(action)
        if key:
            command.append(key)
            if value:
                if ' ' in value:
                    command.append(f'''"{value}"''')
                else:
                    command.append(value)
    return ' '.join(command).strip()

__all__ = [
    'get_cli_string',
    'load_dotenv',
    'dotenv_values',
    'get_key',
    'set_key',
    'unset_key',
    'find_dotenv',
    'load_ipython_extension']
