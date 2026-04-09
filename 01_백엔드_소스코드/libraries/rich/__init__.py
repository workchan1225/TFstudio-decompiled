# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Rich text and beautiful formatting in the terminal.'''
import os
from typing import IO, TYPE_CHECKING, Any, Callable, Optional, Union
from _extension import load_ipython_extension
__all__ = [
    'get_console',
    'reconfigure',
    'print',
    'inspect',
    'print_json']
if TYPE_CHECKING:
    from console import Console
_console: Optional['Console'] = None

try:
    _IMPORT_CWD = os.path.abspath(os.getcwd())
except FileNotFoundError:
    _IMPORT_CWD = ''


def get_console():
    """Get a global :class:`~rich.console.Console` instance. This function is used when Rich requires a Console,
    and hasn't been explicitly given one.

    Returns:
        Console: A console instance.
    """
    pass
# WARNING: Decompyle incomplete


def reconfigure(*args, **kwargs):
    '''Reconfigures the global console by replacing it with another.

    Args:
        *args (Any): Positional arguments for the replacement :class:`~rich.console.Console`.
        **kwargs (Any): Keyword arguments for the replacement :class:`~rich.console.Console`.
    '''
    Console = Console
    import rich.console
# WARNING: Decompyle incomplete


def print(*, sep, end, file, flush, *objects):
    '''Print object(s) supplied via positional arguments.
    This function has an identical signature to the built-in print.
    For more advanced features, see the :class:`~rich.console.Console` class.

    Args:
        sep (str, optional): Separator between printed objects. Defaults to " ".
        end (str, optional): Character to write at end of output. Defaults to "\\\\n".
        file (IO[str], optional): File to write to, or None for stdout. Defaults to None.
        flush (bool, optional): Has no effect as Rich always flushes output. Defaults to False.

    '''
    Console = Console
    import console
# WARNING: Decompyle incomplete


def print_json(json = None, *, data, indent, highlight, skip_keys, ensure_ascii, check_circular, allow_nan, default, sort_keys):
    '''Pretty prints JSON. Output will be valid JSON.

    Args:
        json (str): A string containing JSON.
        data (Any): If json is not supplied, then encode this data.
        indent (int, optional): Number of spaces to indent. Defaults to 2.
        highlight (bool, optional): Enable highlighting of output: Defaults to True.
        skip_keys (bool, optional): Skip keys not of a basic type. Defaults to False.
        ensure_ascii (bool, optional): Escape all non-ascii characters. Defaults to False.
        check_circular (bool, optional): Check for circular references. Defaults to True.
        allow_nan (bool, optional): Allow NaN and Infinity values. Defaults to True.
        default (Callable, optional): A callable that converts values that can not be encoded
            in to something that can be JSON encoded. Defaults to None.
        sort_keys (bool, optional): Sort dictionary keys. Defaults to False.
    '''
    get_console().print_json(json, data = data, indent = indent, highlight = highlight, skip_keys = skip_keys, ensure_ascii = ensure_ascii, check_circular = check_circular, allow_nan = allow_nan, default = default, sort_keys = sort_keys)


def inspect(obj = None, *, console, title, help, methods, docs, private, dunder, sort, all, value):
