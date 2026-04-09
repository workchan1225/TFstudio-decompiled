# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: text.pyc (Python 3.11)

import functools
import re
from state_inline import StateInline
_TerminatorChars = {
    '\n',
    '*',
    '-',
    '<',
    '=',
    '>',
    '_',
    '{',
    '}',
    '~',
    '!',
    '#',
    '$',
    '%',
    '&',
    '+',
    ':',
    '@',
    '[',
    '\\',
    ']',
    '^',
    '`'}
_terminator_char_regex = (lambda : re.compile('[' + re.escape(''.join(_TerminatorChars)) + ']'))()

def text(state = None, silent = None):
    pos = state.pos
    posMax = state.posMax
    terminator_char = _terminator_char_regex().search(state.src, pos)
    pos = terminator_char.start() if terminator_char else posMax
    if pos == state.pos:
        return False
    if not None:
        pass
    pos = state, state.pending += state.src[state.pos:pos], .pending
    return True
