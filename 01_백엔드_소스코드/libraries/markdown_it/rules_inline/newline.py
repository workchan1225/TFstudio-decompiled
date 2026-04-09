# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: newline.pyc (Python 3.11)

"""Proceess '
'."""
from common.utils import charStrAt, isStrSpace
from state_inline import StateInline

def newline(state = None, silent = None):
    pos = state.pos
    if state.src[pos] != '\n':
        return False
    pmax = None(state.pending) - 1
    maximum = state.posMax
# WARNING: Decompyle incomplete
