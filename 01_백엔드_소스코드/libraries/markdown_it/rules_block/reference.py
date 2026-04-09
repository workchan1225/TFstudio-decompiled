# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reference.pyc (Python 3.11)

import logging
from common.utils import charCodeAt, isSpace, normalizeReference
from state_block import StateBlock
LOGGER = logging.getLogger(__name__)

def reference(state = None, startLine = None, _endLine = None, silent = ('state', StateBlock, 'startLine', int, '_endLine', int, 'silent', bool, 'return', bool)):
    LOGGER.debug('entering reference: %s, %s, %s, %s', state, startLine, _endLine, silent)
    pos = state.bMarks[startLine] + state.tShift[startLine]
    maximum = state.eMarks[startLine]
    nextLine = startLine + 1
    if state.is_code_block(startLine):
        return False
    if None.src[pos] != '[':
        return False
    string = None.src[pos:maximum + 1]
    maximum = len(string)
    labelEnd = None
    pos = 1
# WARNING: Decompyle incomplete


def getNextLine(state = None, nextLine = None):
    endLine = state.lineMax
    if nextLine >= endLine or state.isEmpty(nextLine):
        return None
    isContinuation = None
    if state.is_code_block(nextLine):
        isContinuation = True
    if state.sCount[nextLine] < 0:
        isContinuation = True
    if not isContinuation:
        terminatorRules = state.md.block.ruler.getRules('reference')
        oldParentType = state.parentType
        state.parentType = 'reference'
        terminate = False
        for terminatorRule in terminatorRules:
            if terminatorRule(state, nextLine, endLine, True):
                terminate = True
            
            state.parentType = oldParentType
            if terminate:
                return None
            pos = None.bMarks[nextLine] + state.tShift[nextLine]
            maximum = state.eMarks[nextLine]
            return state.src[pos:maximum + 1]
