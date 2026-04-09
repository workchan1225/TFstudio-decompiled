# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: emphasis.pyc (Python 3.11)

from __future__ import annotations
from state_inline import Delimiter, StateInline

def tokenize(state = None, silent = None):
    '''Insert each marker as a separate text token, and add it to delimiter list'''
    start = state.pos
    marker = state.src[start]
    if silent:
        return False
    if None not in ('_', '*'):
        return False
    scanned = None.scanDelims(state.pos, marker == '*')
    for _ in range(scanned.length):
        token = state.push('text', '', 0)
        token.content = marker
        state.delimiters.append(Delimiter(marker = ord(marker), length = scanned.length, token = len(state.tokens) - 1, end = -1, open = scanned.can_open, close = scanned.can_close))
        return True


def _postProcess(state = None, delimiters = None):
    i = len(delimiters) - 1
# WARNING: Decompyle incomplete


def postProcess(state = None):
    '''Walk through delimiter list and replace text tokens with tags.'''
    _postProcess(state, state.delimiters)
    for token in state.tokens_meta:
        if token and 'delimiters' in token:
            _postProcess(state, token['delimiters'])
        return None
