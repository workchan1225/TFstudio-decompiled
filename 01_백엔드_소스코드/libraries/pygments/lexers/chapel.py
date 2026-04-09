# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chapel.pyc (Python 3.11)

'''
    pygments.lexers.chapel
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexer for the Chapel language.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.lexer import RegexLexer, bygroups, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Whitespace
__all__ = [
    'ChapelLexer']

class ChapelLexer(RegexLexer):
