# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: expression.pyc (Python 3.11)

"""Evaluate match expressions, as used by `-k` and `-m`.

The grammar is:

expression: expr? EOF
expr:       and_expr ('or' and_expr)*
and_expr:   not_expr ('and' not_expr)*
not_expr:   'not' not_expr | '(' expr ')' | ident kwargs?

ident:      (\\w|:|\\+|-|\\.|\\[|\\]|\\\\|/)+
kwargs:     ('(' name '=' value ( ', ' name '=' value )*  ')')
name:       a valid ident, but not a reserved keyword
value:      (unescaped) string literal | (-)?[0-9]+ | 'False' | 'True' | 'None'

The semantics are:

- Empty expression evaluates to False.
- ident evaluates to True or False according to a provided matcher function.
- ident with parentheses and keyword arguments evaluates to True or False according to a provided matcher function.
- or/and/not evaluate according to the usual boolean semantics.
"""
from __future__ import annotations
import ast
from collections.abc import Iterator
from collections.abc import Mapping
from collections.abc import Sequence
import dataclasses
import enum
import keyword
import re
import types
from typing import Final
from typing import final
from typing import Literal
from typing import NoReturn
from typing import overload
from typing import Protocol
__all__ = [
    'Expression',
    'ExpressionMatcher']
FILE_NAME: 'Final' = '<pytest match expression>'

class TokenType(enum.Enum):
    LPAREN = 'left parenthesis'
    RPAREN = 'right parenthesis'
    OR = 'or'
    AND = 'and'
    NOT = 'not'
    IDENT = 'identifier'
    EOF = 'end of input'
    EQUAL = '='
    STRING = 'string literal'
    COMMA = ','

Token = <NODE:12>()

class Scanner:
    __slots__ = ('current', 'input', 'tokens')
    
    def __init__(self = None, input = None):
        self.input = input
        self.tokens = self.lex(input)
        self.current = next(self.tokens)

    
    def lex(self = None, input = None):
        pass
    # WARNING: Decompyle incomplete

    accept = (lambda self = None, type = None, *, reject,
