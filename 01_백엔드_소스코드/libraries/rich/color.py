# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: color.pyc (Python 3.11)

import re
import sys
from colorsys import rgb_to_hls
from enum import IntEnum
from functools import lru_cache
from typing import TYPE_CHECKING, NamedTuple, Optional, Tuple
from _palettes import EIGHT_BIT_PALETTE, STANDARD_PALETTE, WINDOWS_PALETTE
from color_triplet import ColorTriplet
from repr import Result, rich_repr
from terminal_theme import DEFAULT_TERMINAL_THEME
if TYPE_CHECKING:
    from terminal_theme import TerminalTheme
    from text import Text
WINDOWS = sys.platform == 'win32'

class ColorSystem(IntEnum):
    '''One of the 3 color system supported by terminals.'''
    STANDARD = 1
    EIGHT_BIT = 2
    TRUECOLOR = 3
    WINDOWS = 4
    
    def __repr__(self = None):
        return f'''ColorSystem.{self.name}'''

    
    def __str__(self = None):
        return repr(self)



class ColorType(IntEnum):
    '''Type of color stored in Color class.'''
    DEFAULT = 0
    STANDARD = 1
    EIGHT_BIT = 2
    TRUECOLOR = 3
    WINDOWS = 4
    
    def __repr__(self = None):
        return f'''ColorType.{self.name}'''


# WARNING: Decompyle incomplete
