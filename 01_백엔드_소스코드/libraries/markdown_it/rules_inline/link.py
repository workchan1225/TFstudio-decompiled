# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: link.pyc (Python 3.11)

from common.utils import isStrSpace, normalizeReference
from state_inline import StateInline

def link(state = None, silent = None):
    href = ''
    title = ''
    label = None
    oldPos = state.pos
    maximum = state.posMax
    start = state.pos
    parseReference = True
    if state.src[state.pos] != '[':
        return False
    labelStart = None.pos + 1
    labelEnd = state.md.helpers.parseLinkLabel(state, state.pos, True)
    if labelEnd < 0:
        return False
    pos = None + 1
# WARNING: Decompyle incomplete
