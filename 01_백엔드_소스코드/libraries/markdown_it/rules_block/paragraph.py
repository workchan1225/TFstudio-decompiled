# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: paragraph.pyc (Python 3.11)

'''Paragraph.'''
import logging
from state_block import StateBlock
LOGGER = logging.getLogger(__name__)

def paragraph(state = None, startLine = None, endLine = None, silent = ('state', StateBlock, 'startLine', int, 'endLine', int, 'silent', bool, 'return', bool)):
    LOGGER.debug('entering paragraph: %s, %s, %s, %s', state, startLine, endLine, silent)
    nextLine = startLine + 1
    ruler = state.md.block.ruler
    terminatorRules = ruler.getRules('paragraph')
    endLine = state.lineMax
    oldParentType = state.parentType
    state.parentType = 'paragraph'
# WARNING: Decompyle incomplete
