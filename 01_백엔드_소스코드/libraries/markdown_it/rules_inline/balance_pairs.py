# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: balance_pairs.pyc (Python 3.11)

'''Balance paired characters (*, _, etc) in inline tokens.'''
from __future__ import annotations
from state_inline import Delimiter, StateInline

def processDelimiters(state = None, delimiters = None):
    '''For each opening emphasis-like marker find a matching closing one.'''
    if not delimiters:
        return None
    openersBottom = None
    maximum = len(delimiters)
    headerIdx = 0
    lastTokenIdx = -2
    jumps = []
    closerIdx = 0
# WARNING: Decompyle incomplete


def link_pairs(state = None):
    tokens_meta = state.tokens_meta
    maximum = len(state.tokens_meta)
    processDelimiters(state, state.delimiters)
    curr = 0
# WARNING: Decompyle incomplete
