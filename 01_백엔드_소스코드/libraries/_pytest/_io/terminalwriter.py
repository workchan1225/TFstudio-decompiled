# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: terminalwriter.pyc (Python 3.11)

'''Helper functions for writing to terminals and files.'''
from __future__ import annotations
from collections.abc import Sequence
import os
import shutil
import sys
from typing import final
from typing import Literal
from typing import TextIO
import pygments
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexer import Lexer
from pygments.lexers.diff import DiffLexer
from pygments.lexers.python import PythonLexer
from compat import assert_never
from wcwidth import wcswidth

def get_terminal_width():
    (width, _) = shutil.get_terminal_size(fallback = (80, 24))
    if width < 40:
        width = 80
    return width


def should_do_markup(file = None):
