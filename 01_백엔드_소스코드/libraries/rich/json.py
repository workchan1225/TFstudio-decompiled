# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: json.pyc (Python 3.11)

from pathlib import Path
from json import loads, dumps
from typing import Any, Callable, Optional, Union
from text import Text
from highlighter import JSONHighlighter, NullHighlighter

class JSON:
    '''A renderable which pretty prints JSON.

    Args:
        json (str): JSON encoded data.
        indent (Union[None, int, str], optional): Number of characters to indent by. Defaults to 2.
        highlight (bool, optional): Enable highlighting. Defaults to True.
        skip_keys (bool, optional): Skip keys not of a basic type. Defaults to False.
        ensure_ascii (bool, optional): Escape all non-ascii characters. Defaults to False.
        check_circular (bool, optional): Check for circular references. Defaults to True.
        allow_nan (bool, optional): Allow NaN and Infinity values. Defaults to True.
        default (Callable, optional): A callable that converts values that can not be encoded
            in to something that can be JSON encoded. Defaults to None.
        sort_keys (bool, optional): Sort dictionary keys. Defaults to False.
    '''
    
    def __init__(self, json, indent, highlight, skip_keys, ensure_ascii = None, check_circular = None, allow_nan = None, default = (2, True, False, False, True, True, None, False), sort_keys = ('json', str, 'indent', Union[(None, int, str)], 'highlight', bool, 'skip_keys', bool, 'ensure_ascii', bool, 'check_circular', bool, 'allow_nan', bool, 'default', Optional[Callable[([
        Any], Any)]], 'sort_keys', bool, 'return', None)):
        data = loads(json)
        json = dumps(data, indent = indent, skipkeys = skip_keys, ensure_ascii = ensure_ascii, check_circular = check_circular, allow_nan = allow_nan, default = default, sort_keys = sort_keys)
        highlighter = JSONHighlighter() if highlight else NullHighlighter()
        self.text = highlighter(json)
        self.text.no_wrap = True
        self.text.overflow = None

    from_data = (lambda cls, data, indent, highlight, skip_keys, ensure_ascii = None, check_circular = None, allow_nan = classmethod, default = (2, True, False, False, True, True, None, False), sort_keys = ('data', Any, 'indent', Union[(None, int, str)], 'highlight', bool, 'skip_keys', bool, 'ensure_ascii', bool, 'check_circular', bool, 'allow_nan', bool, 'default', Optional[Callable[([
        Any], Any)]], 'sort_keys', bool, 'return', 'JSON'): json_instance = cls.__new__(cls)json = dumps(data, indent = indent, skipkeys = skip_keys, ensure_ascii = ensure_ascii, check_circular = check_circular, allow_nan = allow_nan, default = default, sort_keys = sort_keys)highlighter = JSONHighlighter() if highlight else NullHighlighter()json_instance.text = highlighter(json)json_instance.text.no_wrap = Truejson_instance.text.overflow = Nonejson_instance)()
    
    def __rich__(self = None):
        return self.text


if __name__ == '__main__':
    import argparse
    import sys
    parser = argparse.ArgumentParser(description = 'Pretty print json')
    parser.add_argument('path', metavar = 'PATH', help = 'path to file, or - for stdin')
    parser.add_argument('-i', '--indent', metavar = 'SPACES', type = int, help = 'Number of spaces in an indent', default = 2)
    args = parser.parse_args()
    from rich.console import Console
    console = Console()
    error_console = Console(stderr = True)
    
    try:
        if args.path == '-':
            json_data = sys.stdin.read()
        else:
            json_data = Path(args.path).read_text()
    except Exception:
        error = None
        error_console.print(f'''Unable to read {args.path!r}; {error}''')
        sys.exit(-1)
        error = None
        del error
    except:
        error = None
        del error

    console.print(JSON(json_data, indent = args.indent), soft_wrap = True)
    return None
