# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: escape.pyc (Python 3.11)

'''
Process escaped chars and hardbreaks
'''
from common.utils import isStrSpace
from state_inline import StateInline

def escape(state = None, silent = None):
    '''Process escaped chars and hardbreaks.'''
    pos = state.pos
    maximum = state.posMax
    if state.src[pos] != '\\':
        return False
    None += 1
    if pos >= maximum:
        return False
    ch1 = None.src[pos]
    ch1_ord = ord(ch1)
# WARNING: Decompyle incomplete

_ESCAPED = {
    '*',
    '-',
    '<',
    '=',
    '>',
    '?',
    '_',
    '{',
    '|',
    '}',
    '~',
    '!',
    '"',
    '#',
    '$',
    '%',
    '&',
    "'",
    '(',
    ')',
    '+',
    ',',
    '.',
    '/',
    ':',
    ';',
    '@',
    '[',
    '\\',
    ']',
    '^',
    '`'}
