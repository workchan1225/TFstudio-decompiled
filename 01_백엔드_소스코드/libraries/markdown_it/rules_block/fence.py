# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fence.pyc (Python 3.11)

import logging
from state_block import StateBlock
LOGGER = logging.getLogger(__name__)

def fence(state = None, startLine = None, endLine = None, silent = ('state', StateBlock, 'startLine', int, 'endLine', int, 'silent', bool, 'return', bool)):
    LOGGER.debug('entering fence: %s, %s, %s, %s', state, startLine, endLine, silent)
    haveEndMarker = False
    pos = state.bMarks[startLine] + state.tShift[startLine]
    maximum = state.eMarks[startLine]
    if state.is_code_block(startLine):
        return False
    if None + 3 > maximum:
        return False
    marker = None.src[pos]
    if marker not in ('~', '`'):
        return False
    mem = None
    pos = state.skipCharsStr(pos, marker)
    length = pos - mem
    if length < 3:
        return False
    markup = None.src[mem:pos]
    params = state.src[pos:maximum]
    if marker == '`' and marker in params:
        return False
    if None:
        return True
    nextLine = None
    nextLine += 1
    state.line = None + None if nextLine >= endLine else None if pos < maximum and state.sCount[nextLine] < state.blkIndent else nextLine if state.src[pos] != marker else 1 if haveEndMarker else 0
    token = state.push('fence', 'code', 0)
    token.info = params
    token.content = state.getLines(startLine + 1, nextLine, length, True)
    token.markup = markup
    token.map = [
        startLine,
        state.line]
    return True
