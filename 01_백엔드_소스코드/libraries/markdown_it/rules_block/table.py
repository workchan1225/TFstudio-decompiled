# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: table.pyc (Python 3.11)

from __future__ import annotations
import re
from common.utils import charStrAt, isStrSpace
from state_block import StateBlock
headerLineRe = re.compile('^:?-+:?$')
enclosingPipesRe = re.compile('^\\||\\|$')
MAX_AUTOCOMPLETED_CELLS = 65536

def getLine(state = None, line = None):
    pos = state.bMarks[line] + state.tShift[line]
    maximum = state.eMarks[line]
    return state.src[pos:maximum]


def escapedSplit(string = None):
    result = []
    pos = 0
    max = len(string)
    isEscaped = False
    lastPos = 0
    current = ''
    ch = charStrAt(string, pos)
# WARNING: Decompyle incomplete


def table(state = None, startLine = None, endLine = None, silent = ('state', 'StateBlock', 'startLine', 'int', 'endLine', 'int', 'silent', 'bool', 'return', 'bool')):
    tbodyLines = None
    if startLine + 2 > endLine:
        return False
    nextLine = None + 1
    if state.sCount[nextLine] < state.blkIndent:
        return False
    if None.is_code_block(nextLine):
        return False
    pos = None.bMarks[nextLine] + state.tShift[nextLine]
    if pos >= state.eMarks[nextLine]:
        return False
    first_ch = None.src[pos]
    pos += 1
    if first_ch not in ('|', '-', ':'):
        return False
    if None >= state.eMarks[nextLine]:
        return False
    second_ch = None.src[pos]
    pos += 1
    if not second_ch not in ('|', '-', ':') and isStrSpace(second_ch):
        return False
    if None == '-' and isStrSpace(second_ch):
        return False
# WARNING: Decompyle incomplete
