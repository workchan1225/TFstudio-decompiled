# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: segment.pyc (Python 3.11)

from enum import IntEnum
from functools import lru_cache
from itertools import filterfalse
from logging import getLogger
from operator import attrgetter
from typing import TYPE_CHECKING, Dict, Iterable, List, NamedTuple, Optional, Sequence, Tuple, Type, Union
from cells import _is_single_cell_widths, cached_cell_len, cell_len, get_character_cell_size, set_cell_size
from repr import Result, rich_repr
from style import Style
if TYPE_CHECKING:
    from console import Console, ConsoleOptions, RenderResult
log = getLogger('rich')

class ControlType(IntEnum):
    '''Non-printable control codes which typically translate to ANSI codes.'''
    BELL = 1
    CARRIAGE_RETURN = 2
    HOME = 3
    CLEAR = 4
    SHOW_CURSOR = 5
    HIDE_CURSOR = 6
    ENABLE_ALT_SCREEN = 7
    DISABLE_ALT_SCREEN = 8
    CURSOR_UP = 9
    CURSOR_DOWN = 10
    CURSOR_FORWARD = 11
    CURSOR_BACKWARD = 12
    CURSOR_MOVE_TO_COLUMN = 13
    CURSOR_MOVE_TO = 14
    ERASE_IN_LINE = 15
    SET_WINDOW_TITLE = 16

ControlCode = Union[(Tuple[ControlType], Tuple[(ControlType, Union[(int, str)])], Tuple[(ControlType, int, int)])]
Segment = <NODE:12>()

class Segments:
    '''A simple renderable to render an iterable of segments. This class may be useful if
    you want to print segments outside of a __rich_console__ method.

    Args:
        segments (Iterable[Segment]): An iterable of segments.
        new_lines (bool, optional): Add new lines between segments. Defaults to False.
    '''
    
    def __init__(self = None, segments = None, new_lines = None):
        self.segments = list(segments)
        self.new_lines = new_lines

    
    def __rich_console__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete



class SegmentLines:
    
    def __init__(self = None, lines = None, new_lines = None):
        '''A simple renderable containing a number of lines of segments. May be used as an intermediate
        in rendering process.

        Args:
            lines (Iterable[List[Segment]]): Lists of segments forming lines.
            new_lines (bool, optional): Insert new lines after each line. Defaults to False.
        '''
        self.lines = list(lines)
        self.new_lines = new_lines

    
    def __rich_console__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete


if __name__ == '__main__':
    from rich.console import Console
    from rich.syntax import Syntax
    from rich.text import Text
    code = 'from rich.console import Console\nconsole = Console()\ntext = Text.from_markup("Hello, [bold magenta]World[/]!")\nconsole.print(text)'
    text = Text.from_markup('Hello, [bold magenta]World[/]!')
    console = Console()
    console.rule('rich.Segment')
    console.print('A Segment is the last step in the Rich render process before generating text with ANSI codes.')
    console.print('\nConsider the following code:\n')
    console.print(Syntax(code, 'python', line_numbers = True))
    console.print()
    console.print('When you call [b]print()[/b], Rich [i]renders[/i] the object in to the following:\n')
    fragments = list(console.render(text))
    console.print(fragments)
    console.print()
    console.print('The Segments are then processed to produce the following output:\n')
    console.print(text)
    console.print('\nYou will only need to know this if you are implementing your own Rich renderables.')
    return None
