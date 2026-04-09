# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: containers.pyc (Python 3.11)

from itertools import zip_longest
from typing import TYPE_CHECKING, Iterable, Iterator, List, Optional, TypeVar, Union, overload
if TYPE_CHECKING:
    from console import Console, ConsoleOptions, JustifyMethod, OverflowMethod, RenderResult, RenderableType
    from text import Text
from cells import cell_len
from measure import Measurement
T = TypeVar('T')

class Renderables:
    '''A list subclass which renders its contents to the console.'''
    
    def __init__(self = None, renderables = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __rich_console__(self = None, console = None, options = None):
        '''Console render method to insert line-breaks.'''
        pass
    # WARNING: Decompyle incomplete

    
    def __rich_measure__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete

    
    def append(self = None, renderable = None):
        self._renderables.append(renderable)

    
    def __iter__(self = None):
        return iter(self._renderables)



class Lines:
    '''A list subclass which can render to the console.'''
    
    def __init__(self = None, lines = None):
        self._lines = list(lines)

    
    def __repr__(self = None):
        return f'''Lines({self._lines!r})'''

    
    def __iter__(self = None):
        return iter(self._lines)

    __getitem__ = (lambda self = None, index = None: pass)()
    __getitem__ = (lambda self = None, index = None: pass)()
    
    def __getitem__(self = None, index = None):
        return self._lines[index]

    
    def __setitem__(self = None, index = None, value = None):
        self._lines[index] = value
        return self

    
    def __len__(self = None):
        return self._lines.__len__()

    
    def __rich_console__(self = None, console = None, options = None):
        '''Console render method to insert line-breaks.'''
        pass
    # WARNING: Decompyle incomplete

    
    def append(self = None, line = None):
        self._lines.append(line)

    
    def extend(self = None, lines = None):
        self._lines.extend(lines)

    
    def pop(self = None, index = None):
        return self._lines.pop(index)

    
    def justify(self = None, console = None, width = None, justify = ('left', 'fold'), overflow = ('console', 'Console', 'width', int, 'justify', 'JustifyMethod', 'overflow', 'OverflowMethod', 'return', None)):
        '''Justify and overflow text to a given width.

        Args:
            console (Console): Console instance.
            width (int): Number of cells available per line.
            justify (str, optional): Default justify method for text: "left", "center", "full" or "right". Defaults to "left".
            overflow (str, optional): Default overflow for text: "crop", "fold", or "ellipsis". Defaults to "fold".

        '''
        Text = Text
        import text
    # WARNING: Decompyle incomplete
