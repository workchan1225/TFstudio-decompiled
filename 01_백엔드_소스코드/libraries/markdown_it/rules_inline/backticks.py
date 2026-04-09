# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: backticks.pyc (Python 3.11)

import re
from state_inline import StateInline
regex = re.compile('^ (.+) $')

def backtick(state = None, silent = None):
    pos = state.pos
    if state.src[pos] != '`':
        return False
    start = None
    pos += 1
    maximum = state.posMax
# WARNING: Decompyle incomplete
