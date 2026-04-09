# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: normalize.pyc (Python 3.11)

'''Normalize input string.'''
import re
from state_core import StateCore
NEWLINES_RE = re.compile('\\r\\n?|\\n')
NULL_RE = re.compile('\\0')

def normalize(state = None):
    string = NEWLINES_RE.sub('\n', state.src)
    string = NULL_RE.sub('�', string)
    state.src = string
