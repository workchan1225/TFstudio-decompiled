# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: phystokens.pyc (Python 3.11)

'''Better tokenizing for coverage.py.'''
from __future__ import annotations
import ast
import io
import keyword
import re
import sys
import token
import tokenize
from collections.abc import Iterable
from coverage import env
from coverage.types import TLineNo, TSourceTokenLines
TokenInfos = Iterable[tokenize.TokenInfo]

def _phys_tokens(toks = None):
    """Return all physical tokens, even line continuations.

    tokenize.generate_tokens() doesn't return a token for the backslash that
    continues lines.  This wrapper provides those tokens so that we can
    re-create a faithful representation of the original source.

    Returns the same values as generate_tokens()

    """
    pass
# WARNING: Decompyle incomplete


def find_soft_key_lines(source = None):
    '''Helper for finding lines with soft keywords, like match/case lines.'''
    soft_key_lines = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Match):
            soft_key_lines.add(node.lineno)
            for case in node.cases:
                soft_key_lines.add(case.pattern.lineno)
                if sys.version_info >= (3, 12) and isinstance(node, ast.TypeAlias):
                    soft_key_lines.add(node.lineno)
        return soft_key_lines


def source_token_lines(source = None):
    """Generate a series of lines, one for each line in `source`.

    Each line is a list of pairs, each pair is a token::

        [('key', 'def'), ('ws', ' '), ('nam', 'hello'), ('op', '('), ... ]

    Each pair has a token class, and the token text.

    If you concatenate all the token texts, and then join them with newlines,
    you should have your original `source` back, with two differences:
    trailing white space is not preserved, and a final line with no newline
    is indistinguishable from a final line with a newline.

    """
    pass
# WARNING: Decompyle incomplete


def generate_tokens(text = None):
    """A helper around `tokenize.generate_tokens`.

    Originally this was used to cache the results, but it didn't seem to make
    reporting go faster, and caused issues with using too much memory.

    """
    readline = io.StringIO(text).readline
    return tokenize.generate_tokens(readline)


def source_encoding(source = None):
    '''Determine the encoding for `source`, according to PEP 263.

    `source` is a byte string: the text of the program.

    Returns a string, the name of the encoding.

    '''
    readline = iter(source.splitlines(True)).__next__
    return tokenize.detect_encoding(readline)[0]
