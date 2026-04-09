# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lheading.pyc (Python 3.11)

import logging
from state_block import StateBlock
LOGGER = logging.getLogger(__name__)

def lheading(state = None, startLine = None, endLine = None, silent = ('state', StateBlock, 'startLine', int, 'endLine', int, 'silent', bool, 'return', bool)):
    LOGGER.debug('entering lheading: %s, %s, %s, %s', state, startLine, endLine, silent)
    level = None
    nextLine = startLine + 1
    ruler = state.md.block.ruler
    terminatorRules = ruler.getRules('paragraph')
    if state.is_code_block(startLine):
        return False
    oldParentType = None.parentType
    state.parentType = 'paragraph'
# WARNING: Decompyle incomplete
