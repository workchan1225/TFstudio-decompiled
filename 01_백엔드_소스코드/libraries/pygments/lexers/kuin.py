# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: kuin.pyc (Python 3.11)

'''
    pygments.lexers.kuin
    ~~~~~~~~~~~~~~~~~~~~

    Lexers for the Kuin language.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.lexer import RegexLexer, include, using, this, bygroups, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Whitespace
__all__ = [
    'KuinLexer']

class KuinLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'KuinLexer'
    __doc__ = '\n    For Kuin source code.\n    '
    name = 'Kuin'
    url = 'https://github.com/kuina/Kuin'
    aliases = [
        'kuin']
    filenames = [
        '*.kn']
    version_added = '2.9'
# WARNING: Decompyle incomplete
