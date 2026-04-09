# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: entity.pyc (Python 3.11)

import re
from common.entities import entities
from common.utils import fromCodePoint, isValidEntityCode
from state_inline import StateInline
DIGITAL_RE = re.compile('^&#((?:x[a-f0-9]{1,6}|[0-9]{1,7}));', re.IGNORECASE)
NAMED_RE = re.compile('^&([a-z][a-z0-9]{1,31});', re.IGNORECASE)

def entity(state = None, silent = None):
    pos = state.pos
    maximum = state.posMax
    if state.src[pos] != '&':
        return False
    if None + 1 >= maximum:
        return False
    if None.src[pos + 1] == '#':
        match = DIGITAL_RE.search(state.src[pos:])
        if DIGITAL_RE.search(state.src[pos:]):
            if not silent:
                match1 = match.group(1)
                code = int(match1[1:], 16) if match1[0].lower() == 'x' else int(match1, 10)
                token = state.push('text_special', '', 0)
                token.content = fromCodePoint(code) if isValidEntityCode(code) else fromCodePoint(65533)
                token.markup = match.group(0)
                token.info = 'entity'
            return True
    NAMED_RE.search(state.src[pos:]) = NAMED_RE.search(state.src[pos:])
    if None and match.group(1) in entities:
        if not silent:
            token = state.push('text_special', '', 0)
            token.content = entities[match.group(1)]
            token.markup = match.group(0)
            token.info = 'entity'
        return True
