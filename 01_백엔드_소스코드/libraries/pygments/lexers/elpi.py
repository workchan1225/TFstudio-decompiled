# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: elpi.pyc (Python 3.11)

'''
    pygments.lexers.elpi
    ~~~~~~~~~~~~~~~~~~~~

    Lexer for the `Elpi <http://github.com/LPCIC/elpi>`_ programming language.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.lexer import RegexLexer, bygroups, include, using
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation
__all__ = [
    'ElpiLexer']
from pygments.lexers.theorem import CoqLexer

class ElpiLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'ElpiLexer'
    __doc__ = '\n    Lexer for the Elpi programming language.\n    '
    name = 'Elpi'
    url = 'http://github.com/LPCIC/elpi'
    aliases = [
        'elpi']
    filenames = [
        '*.elpi']
    mimetypes = [
        'text/x-elpi']
    version_added = '2.11'
    lcase_re = '[a-z]'
    ucase_re = '[A-Z]'
    digit_re = '[0-9]'
    schar2_re = "([+*^?/<>`'@#~=&!])"
    schar_re = f'''({schar2_re}|-|\\$|_)'''
    idchar_re = f'''({lcase_re}|{ucase_re}|{digit_re}|{schar_re})'''
    idcharstarns_re = f'''({idchar_re}*(\\.({lcase_re}|{ucase_re}){idchar_re}*)*)'''
    symbchar_re = f'''({lcase_re}|{ucase_re}|{digit_re}|{schar_re}|:)'''
    constant_re = f'''({ucase_re}{idchar_re}*|{lcase_re}{idcharstarns_re}|{schar2_re}{symbchar_re}*|_{idchar_re}+)'''
    symbol_re = '(,|<=>|->|:-|;|\\?-|->|&|=>|\\bas\\b|\\buvar\\b|<|=<|=|==|>=|>|\\bi<|\\bi=<|\\bi>=|\\bi>|\\bis\\b|\\br<|\\br=<|\\br>=|\\br>|\\bs<|\\bs=<|\\bs>=|\\bs>|@|::|\\[\\]|`->|`:|`:=|\\^|-|\\+|\\bi-|\\bi\\+|r-|r\\+|/|\\*|\\bdiv\\b|\\bi\\*|\\bmod\\b|\\br\\*|~|\\bi~|\\br~)'
    escape_re = f'''\\(({constant_re}|{symbol_re})\\)'''
    const_sym_re = f'''({constant_re}|{symbol_re}|{escape_re})'''
# WARNING: Decompyle incomplete
