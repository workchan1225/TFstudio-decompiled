# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _emoji_replace.pyc (Python 3.11)

from typing import Callable, Match, Optional
import re
from _emoji_codes import EMOJI
_ReStringMatch = Match[str]
_ReSubCallable = Callable[([
    _ReStringMatch], str)]
_EmojiSubMethod = Callable[([
    _ReSubCallable,
    str], str)]

def _emoji_replace(text = None, default_variant = None, _emoji_sub = None):
    '''Replace emoji code in text.'''
    pass
# WARNING: Decompyle incomplete
