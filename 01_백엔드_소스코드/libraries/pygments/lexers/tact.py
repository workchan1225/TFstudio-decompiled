# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tact.pyc (Python 3.11)

'''
    pygments.lexers.tact
    ~~~~~~~~~~~~~~~~~~~~

    Lexers for Tact.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.lexer import RegexLexer, include, bygroups, words
from pygments.token import Comment, Operator, Keyword, Name, String, Number, Whitespace, Punctuation
__all__ = [
    'TactLexer']

class TactLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'TactLexer'
    __doc__ = 'For Tact source code.'
    name = 'Tact'
    aliases = [
        'tact']
    filenames = [
        '*.tact']
    url = 'https://tact-lang.org'
    version_added = '2.18'
# WARNING: Decompyle incomplete
