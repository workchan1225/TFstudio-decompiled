# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: state_core.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING
from ruler import StateBase
from token import Token
from utils import EnvType
if TYPE_CHECKING:
    from markdown_it import MarkdownIt

class StateCore(StateBase):
    
    def __init__(self = None, src = None, md = None, env = (None,), tokens = ('src', 'str', 'md', 'MarkdownIt', 'env', 'EnvType', 'tokens', 'list[Token] | None', 'return', 'None')):
