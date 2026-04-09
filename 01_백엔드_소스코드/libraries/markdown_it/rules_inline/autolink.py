# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: autolink.pyc (Python 3.11)

import re
from state_inline import StateInline
EMAIL_RE = re.compile("^([a-zA-Z0-9.!#$%&\\'*+\\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*)$")
AUTOLINK_RE = re.compile('^([a-zA-Z][a-zA-Z0-9+.\\-]{1,31}):([^<>\\x00-\\x20]*)$')

def autolink(state = None, silent = None):
    pos = state.pos
    if state.src[pos] != '<':
        return False
    start = None.pos
    maximum = state.posMax
    pos += 1
    if pos >= maximum:
        return False
    ch = None.src[pos]
    if ch == '<':
        return False
    if None == '>':
        pass
    
    url = state.src[start + 1:pos]
# WARNING: Decompyle incomplete
