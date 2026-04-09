# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: html_block.pyc (Python 3.11)

from __future__ import annotations
import logging
import re
from common.html_blocks import block_names
from common.html_re import HTML_OPEN_CLOSE_TAG_STR
from state_block import StateBlock
LOGGER = logging.getLogger(__name__)
HTML_SEQUENCES: 'list[tuple[re.Pattern[str], re.Pattern[str], bool]]' = [
    (re.compile('^<(script|pre|style|textarea)(?=(\\s|>|$))', re.IGNORECASE), re.compile('<\\/(script|pre|style|textarea)>', re.IGNORECASE), True),
    (re.compile('^<!--'), re.compile('-->'), True),
    (re.compile('^<\\?'), re.compile('\\?>'), True),
    (re.compile('^<![A-Z]'), re.compile('>'), True),
    (re.compile('^<!\\[CDATA\\['), re.compile('\\]\\]>'), True),
    (re.compile('^</?(' + '|'.join(block_names) + ')(?=(\\s|/?>|$))', re.IGNORECASE), re.compile('^$'), True),
    (re.compile(HTML_OPEN_CLOSE_TAG_STR + '\\s*$'), re.compile('^$'), False)]

def html_block(state = None, startLine = None, endLine = None, silent = ('state', 'StateBlock', 'startLine', 'int', 'endLine', 'int', 'silent', 'bool', 'return', 'bool')):
    LOGGER.debug('entering html_block: %s, %s, %s, %s', state, startLine, endLine, silent)
    pos = state.bMarks[startLine] + state.tShift[startLine]
    maximum = state.eMarks[startLine]
    if state.is_code_block(startLine):
        return False
    if not None.md.options.get('html', None):
        return False
    if None.src[pos] != '<':
        return False
    lineText = None.src[pos:maximum]
    html_seq = None
# WARNING: Decompyle incomplete
