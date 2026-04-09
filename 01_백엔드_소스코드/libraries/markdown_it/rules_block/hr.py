# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hr.pyc (Python 3.11)

'''Horizontal rule

At least 3 of these characters on a line * - _
'''
import logging
from common.utils import isStrSpace
from state_block import StateBlock
LOGGER = logging.getLogger(__name__)

def hr(state = None, startLine = None, endLine = None, silent = ('state', StateBlock, 'startLine', int, 'endLine', int, 'silent', bool, 'return', bool)):
    LOGGER.debug('entering hr: %s, %s, %s, %s', state, startLine, endLine, silent)
    pos = state.bMarks[startLine] + state.tShift[startLine]
    maximum = state.eMarks[startLine]
    if state.is_code_block(startLine):
        return False
    
    try:
        marker = state.src[pos]
    except IndexError:
        return False

    pos += 1
    if marker not in ('*', '-', '_'):
        return False
    cnt = None
# WARNING: Decompyle incomplete
