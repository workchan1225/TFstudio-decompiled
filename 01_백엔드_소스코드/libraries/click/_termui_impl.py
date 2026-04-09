# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _termui_impl.pyc (Python 3.11)

'''
This module contains implementations for the termui module. To keep the
import time of Click down, some infrequently used functionality is
placed in this module and only imported as needed.
'''
import contextlib
import math
import os
import sys
import time
import typing as t
from gettext import gettext as _
from io import StringIO
from shutil import which
from types import TracebackType
from _compat import _default_text_stdout
from _compat import CYGWIN
from _compat import get_best_encoding
from _compat import isatty
from _compat import open_stream
from _compat import strip_ansi
from _compat import term_len
from _compat import WIN
from exceptions import ClickException
from utils import echo
V = t.TypeVar('V')
if os.name == 'nt':
    BEFORE_BAR = '\r'
    AFTER_BAR = '\n'
else:
    BEFORE_BAR = '\r\x1b[?25l'
    AFTER_BAR = '\x1b[?25h\n'

def ProgressBar():
    '''ProgressBar'''
    
    def __init__(self, iterable, length, fill_char, empty_char, bar_template, info_sep, show_eta, show_percent, show_pos, item_show_func, label = None, file = None, color = None, update_min_steps = (None, '#', ' ', '%(bar)s', '  ', True, None, False, None, None, None, None, 1, 30), width = ('iterable', t.Optional[t.Iterable[V]], 'length', t.Optional[int], 'fill_char', str, 'empty_char', str, 'bar_template', str, 'info_sep', str, 'show_eta', bool, 'show_percent', t.Optional[bool], 'show_pos', bool, 'item_show_func', t.Optional[t.Callable[([
        t.Optional[V]], t.Optional[str])]], 'label', t.Optional[str], 'file', t.Optional[t.TextIO], 'color', t.Optional[bool], 'update_min_steps', int, 'width', int, 'return', None)):
        self.fill_char = fill_char
        self.empty_char = empty_char
        self.bar_template = bar_template
        self.info_sep = info_sep
        self.show_eta = show_eta
        self.show_percent = show_percent
        self.show_pos = show_pos
        self.item_show_func = item_show_func
    # WARNING: Decompyle incomplete

    
    def __enter__(self = None):
        self.entered = True
        self.render_progress()
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, tb = ('exc_type', t.Optional[t.Type[BaseException]], 'exc_value', t.Optional[BaseException], 'tb', t.Optional[TracebackType], 'return', None)):
        self.render_finish()

    
    def __iter__(self = None):
        if not self.entered:
            raise RuntimeError('You need to use progress bars in a with block.')
        self.render_progress()
        return self.generator()

    
    def __next__(self = None):
        return next(iter(self))

    
    def render_finish(self = None):
        if self.is_hidden:
            return None
        None.file.write(AFTER_BAR)
        self.file.flush()

    pct = (lambda self = None:
