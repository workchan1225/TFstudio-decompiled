# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: stata.pyc (Python 3.11)

'''
    pygments.lexers.stata
    ~~~~~~~~~~~~~~~~~~~~~

    Lexer for Stata

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import RegexLexer, default, include, words
from pygments.token import Comment, Keyword, Name, Number, String, Text, Operator
from pygments.lexers._stata_builtins import builtins_base, builtins_functions
__all__ = [
    'StataLexer']

class StataLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'StataLexer'
    __doc__ = '\n    For Stata do files.\n    '
    name = 'Stata'
    url = 'http://www.stata.com/'
    version_added = '2.2'
    aliases = [
        'stata',
        'do']
    filenames = [
        '*.do',
        '*.ado']
    mimetypes = [
        'text/x-stata',
        'text/stata',
        'application/x-stata']
    flags = re.MULTILINE | re.DOTALL
# WARNING: Decompyle incomplete
