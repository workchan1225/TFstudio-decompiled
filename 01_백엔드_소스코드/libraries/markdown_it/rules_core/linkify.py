# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: linkify.pyc (Python 3.11)

from __future__ import annotations
import re
from typing import Protocol
from common.utils import arrayReplaceAt, isLinkClose, isLinkOpen
from token import Token
from state_core import StateCore
HTTP_RE = re.compile('^http://')
MAILTO_RE = re.compile('^mailto:')
TEST_MAILTO_RE = re.compile('^mailto:', flags = re.IGNORECASE)

def linkify(state = None):
    '''Rule for identifying plain-text links.'''
    if not state.md.options.linkify:
        return None
    if not None.md.linkify:
        raise ModuleNotFoundError('Linkify enabled but not installed.')
# WARNING: Decompyle incomplete


class _LinkType(Protocol):
    schema: 'str | None' = '_LinkType'
