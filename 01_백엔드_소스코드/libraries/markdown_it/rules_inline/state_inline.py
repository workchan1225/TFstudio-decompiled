# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: state_inline.pyc (Python 3.11)

from __future__ import annotations
from collections import namedtuple
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Literal
from common.utils import isMdAsciiPunct, isPunctChar, isWhiteSpace
from ruler import StateBase
from token import Token
from utils import EnvType
if TYPE_CHECKING:
    from markdown_it import MarkdownIt
Delimiter = <NODE:12>()
Scanned = namedtuple('Scanned', [
    'can_open',
    'can_close',
    'length'])

class StateInline(StateBase):
    
    def __init__(self, src = None, md = None, env = None, outTokens = ('src', 'str', 'md', 'MarkdownIt', 'env', 'EnvType', 'outTokens', 'list[Token]', 'return', 'None')):
        self.src = src
        self.env = env
        self.md = md
        self.tokens = outTokens
        self.tokens_meta = [
            None] * len(outTokens)
        self.pos = 0
        self.posMax = len(self.src)
        self.level = 0
        self.pending = ''
        self.pendingLevel = 0
        self.cache = { }
        self.delimiters = []
        self._prev_delimiters = []
        self.backticks = { }
        self.backticksScanned = False
        self.linkLevel = 0

    
    def __repr__(self = None):
        return f'''{self.__class__.__name__}(pos=[{self.pos} of {self.posMax}], token={len(self.tokens)})'''

    
    def pushPending(self = None):
        token = Token('text', '', 0)
        token.content = self.pending
        token.level = self.pendingLevel
        self.tokens.append(token)
        self.pending = ''
        return token

    
    def push(self = None, ttype = None, tag = None, nesting = ('ttype', 'str', 'tag', 'str', 'nesting', 'Literal[-1, 0, 1]', 'return', 'Token')):
        '''Push new token to "stream".
        If pending text exists - flush it as text token
        '''
        if self.pending:
            self.pushPending()
        token = Token(ttype, tag, nesting)
        token_meta = None
        if nesting < 0:
            self._prev_delimiters.pop() = self, self.level -= 1, .level
        token.level = self.level
        if nesting > 0:
            self._prev_delimiters.append(self.delimiters)
            [] = self, self.level += 1, .level
            token_meta = {
                'delimiters': self.delimiters }
        self.pendingLevel = self.level
        self.tokens.append(token)
        self.tokens_meta.append(token_meta)
        return token

    
    def scanDelims(self = None, start = None, canSplitWord = None):
        '''
        Scan a sequence of emphasis-like markers, and determine whether
        it can start an emphasis sequence or end an emphasis sequence.

         - start - position to scan from (it should point at a valid marker);
         - canSplitWord - determine if these markers can be found inside a word

        '''
        pos = start
        maximum = self.posMax
        marker = self.src[start]
        lastChar = self.src[start - 1] if start > 0 else ' '
    # WARNING: Decompyle incomplete
