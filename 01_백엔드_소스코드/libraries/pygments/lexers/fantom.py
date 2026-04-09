# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fantom.pyc (Python 3.11)

'''
    pygments.lexers.fantom
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexer for the Fantom language.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from string import Template
from pygments.lexer import RegexLexer, include, bygroups, using, this, default, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Literal, Whitespace
__all__ = [
    'FantomLexer']

class FantomLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'FantomLexer'
    __doc__ = '\n    For Fantom source code.\n    '
    name = 'Fantom'
    aliases = [
        'fan']
    filenames = [
        '*.fan']
    mimetypes = [
        'application/x-fantom']
    url = 'https://www.fantom.org'
    version_added = '1.5'
    
    def s(str):
        return Template(str).substitute(dict(pod = '[\\"\\w\\.]+', eos = '\\n|;', id = '[a-zA-Z_]\\w*', type = '(?:\\[|[a-zA-Z_]|\\|)[:\\w\\[\\]|\\->?]*?'))

# WARNING: Decompyle incomplete
