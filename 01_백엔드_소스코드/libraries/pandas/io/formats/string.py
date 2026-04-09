# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: string.pyc (Python 3.11)

'''
Module for formatting output data in console (to string).
'''
from __future__ import annotations
from shutil import get_terminal_size
from typing import TYPE_CHECKING
import numpy as np
from pandas.io.formats.printing import pprint_thing
if TYPE_CHECKING:
    from collections.abc import Iterable
    from pandas.io.formats.format import DataFrameFormatter

class StringFormatter:
    '''Formatter for string representation of a dataframe.'''
    
    def __init__(self = None, fmt = None, line_width = None):
        self.fmt = fmt
        self.adj = fmt.adj
        self.frame = fmt.frame
        self.line_width = line_width

    
    def to_string(self = None):
        text = self._get_string_representation()
        if self.fmt.should_show_dimensions:
            text = f'''{text}{self.fmt.dimensions_info}'''
        return text

    
    def _get_strcols(self = None):
        strcols = self.fmt.get_strcols()
        if self.fmt.is_truncated:
            strcols = self._insert_dot_separators(strcols)
        return strcols

    
    def _get_string_representation(self = None):
        if self.fmt.frame.empty:
            return self._empty_info_line
        strcols = None._get_strcols()
    # WARNING: Decompyle incomplete

    _empty_info_line = (lambda self = None: f'''Empty {type(self.frame).__name__}\nColumns: {pprint_thing(self.frame.columns)}\nIndex: {pprint_thing(self.frame.index)}''')()
    _need_to_wrap_around = (lambda self = None:
