# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: style.pyc (Python 3.11)

import sys
from functools import lru_cache
from operator import attrgetter
from pickle import dumps, loads
from random import randint
from typing import Any, Dict, Iterable, List, Optional, Type, Union, cast
from  import errors
from color import Color, ColorParseError, ColorSystem, blend_rgb
from repr import Result, rich_repr
from terminal_theme import DEFAULT_TERMINAL_THEME, TerminalTheme
_hash_getter = attrgetter('_color', '_bgcolor', '_attributes', '_set_attributes', '_link', '_meta')
StyleType = Union[(str, 'Style')]

class _Bit:
    '''A descriptor to get/set a style attribute bit.'''
    __slots__ = [
        'bit']
    
    def __init__(self = None, bit_no = None):
        self.bit = 1 << bit_no

    
    def __get__(self = None, obj = None, objtype = None):
        if obj._set_attributes & self.bit:
            return obj._attributes & self.bit != 0


Style = <NODE:12>()
NULL_STYLE = Style()

class StyleStack:
    '''A stack of styles.'''
    __slots__ = [
        '_stack']
    
    def __init__(self = None, default_style = None):
        self._stack = [
            default_style]

    
    def __repr__(self = None):
        return f'''<stylestack {self._stack!r}>'''

    current = (lambda self = None: self._stack[-1])()
    
    def push(self = None, style = None):
        '''Push a new style on to the stack.

        Args:
            style (Style): New style to combine with current style.
        '''
        self._stack.append(self._stack[-1] + style)

    
    def pop(self = None):
        '''Pop last style and discard.

        Returns:
            Style: New current style (also available as stack.current)
        '''
        self._stack.pop()
        return self._stack[-1]
