# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: code.pyc (Python 3.11)

'''Code block (4 spaces padded).'''
import logging
from state_block import StateBlock
LOGGER = logging.getLogger(__name__)

def code(state = None, startLine = None, endLine = None, silent = ('state', StateBlock, 'startLine', int, 'endLine', int, 'silent', bool, 'return', bool)):
    LOGGER.debug('entering code: %s, %s, %s, %s', state, startLine, endLine, silent)
    if not state.is_code_block(startLine):
        return False
    last = None + 1
    nextLine = None + 1
    if nextLine < endLine:
        if state.isEmpty(nextLine):
            nextLine += 1
            continue
        if state.is_code_block(nextLine):
            nextLine += 1
            last = nextLine
            continue
    state.line = last
    token = state.push('code_block', 'code', 0)
    token.content = state.getLines(startLine, last, 4 + state.blkIndent, False) + '\n'
    token.map = [
        startLine,
        state.line]
    return True
