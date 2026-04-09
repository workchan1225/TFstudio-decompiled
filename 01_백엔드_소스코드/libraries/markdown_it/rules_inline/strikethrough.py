# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: strikethrough.pyc (Python 3.11)

from __future__ import annotations
from state_inline import Delimiter, StateInline

def tokenize(state = None, silent = None):
    '''Insert each marker as a separate text token, and add it to delimiter list'''
    start = state.pos
    ch = state.src[start]
    if silent:
        return False
    if None != '~':
        return False
    scanned = None.scanDelims(state.pos, True)
    length = scanned.length
    if length < 2:
        return False
    if None % 2:
        token = state.push('text', '', 0)
        token.content = ch
        length -= 1
    i = 0
# WARNING: Decompyle incomplete


def _postProcess(state = None, delimiters = None):
    loneMarkers = []
    maximum = len(delimiters)
    i = 0
# WARNING: Decompyle incomplete


def postProcess(state = None):
    '''Walk through delimiter list and replace text tokens with tags.'''
    tokens_meta = state.tokens_meta
    maximum = len(state.tokens_meta)
    _postProcess(state, state.delimiters)
    curr = 0
# WARNING: Decompyle incomplete
