# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: blockquote.pyc (Python 3.11)

from __future__ import annotations
import logging
from common.utils import isStrSpace
from state_block import StateBlock
LOGGER = logging.getLogger(__name__)

def blockquote(state = None, startLine = None, endLine = None, silent = ('state', 'StateBlock', 'startLine', 'int', 'endLine', 'int', 'silent', 'bool', 'return', 'bool')):
    LOGGER.debug('entering blockquote: %s, %s, %s, %s', state, startLine, endLine, silent)
    oldLineMax = state.lineMax
    pos = state.bMarks[startLine] + state.tShift[startLine]
    max = state.eMarks[startLine]
    if state.is_code_block(startLine):
        return False
# WARNING: Decompyle incomplete
