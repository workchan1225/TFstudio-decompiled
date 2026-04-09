# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image.pyc (Python 3.11)

from __future__ import annotations
from common.utils import isStrSpace, normalizeReference
from token import Token
from state_inline import StateInline

def image(state = None, silent = None):
    label = None
    href = ''
    oldPos = state.pos
    max = state.posMax
    if state.src[state.pos] != '!':
        return False
    if None.pos + 1 < state.posMax and state.src[state.pos + 1] != '[':
        return False
    labelStart = None.pos + 2
    labelEnd = state.md.helpers.parseLinkLabel(state, state.pos + 1, False)
    if labelEnd < 0:
        return False
    pos = None + 1
# WARNING: Decompyle incomplete
