# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: heading.pyc (Python 3.11)

'''Atex heading (#, ##, ...)'''
from __future__ import annotations
import logging
from common.utils import isStrSpace
from state_block import StateBlock
LOGGER = logging.getLogger(__name__)

def heading(state = None, startLine = None, endLine = None, silent = ('state', 'StateBlock', 'startLine', 'int', 'endLine', 'int', 'silent', 'bool', 'return', 'bool')):
    LOGGER.debug('entering heading: %s, %s, %s, %s', state, startLine, endLine, silent)
    pos = state.bMarks[startLine] + state.tShift[startLine]
    maximum = state.eMarks[startLine]
    if state.is_code_block(startLine):
        return False
    ch = None.src[pos]
    if ch != '#' or pos >= maximum:
        return False
    level = None
    pos += 1
    
    try:
        ch = state.src[pos]
    except IndexError:
        ch = None

# WARNING: Decompyle incomplete
