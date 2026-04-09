# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: smartquotes.pyc (Python 3.11)

'''Convert straight quotation marks to typographic ones'''
from __future__ import annotations
import re
from typing import Any
from common.utils import charCodeAt, isMdAsciiPunct, isPunctChar, isWhiteSpace
from token import Token
from state_core import StateCore
QUOTE_TEST_RE = re.compile('[\'\\"]')
QUOTE_RE = re.compile('[\'\\"]')
APOSTROPHE = '’'

def replaceAt(string = None, index = None, ch = None):
    pass
# WARNING: Decompyle incomplete


def process_inlines(tokens = None, state = None):
    stack = []
# WARNING: Decompyle incomplete


def smartquotes(state = None):
    if not state.md.options.typographer:
        return None
# WARNING: Decompyle incomplete
