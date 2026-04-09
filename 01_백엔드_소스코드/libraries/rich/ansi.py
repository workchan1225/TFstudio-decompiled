# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ansi.pyc (Python 3.11)

import re
import sys
from contextlib import suppress
from typing import Iterable, NamedTuple, Optional
from color import Color
from style import Style
from text import Text
re_ansi = re.compile('\n(?:\\x1b[0-?])|\n(?:\\x1b\\](.*?)\\x1b\\\\)|\n(?:\\x1b([(@-Z\\\\-_]|\\[[0-?]*[ -/]*[@-~]))\n', re.VERBOSE)

class _AnsiToken(NamedTuple):
    '''Result of ansi tokenized string.'''
    plain: str = ''
    sgr: Optional[str] = ''
    osc: Optional[str] = ''


def _ansi_tokenize(ansi_text = None):
    '''Tokenize a string in to plain text and ANSI codes.

    Args:
        ansi_text (str): A String containing ANSI codes.

    Yields:
        AnsiToken: A named tuple of (plain, sgr, osc)
    '''
    pass
# WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete
