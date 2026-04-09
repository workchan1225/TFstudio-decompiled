# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: prql.pyc (Python 3.11)

'''
    pygments.lexers.prql
    ~~~~~~~~~~~~~~~~~~~~

    Lexer for the PRQL query language.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.lexer import RegexLexer, combined, words, include, bygroups
from pygments.token import Comment, Literal, Keyword, Name, Number, Operator, Punctuation, String, Text, Whitespace
__all__ = [
    'PrqlLexer']

class PrqlLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'PrqlLexer'
    __doc__ = '\n    For PRQL source code.\n\n    grammar: https://github.com/PRQL/prql/tree/main/grammars\n    '
    name = 'PRQL'
    url = 'https://prql-lang.org/'
    aliases = [
        'prql']
    filenames = [
        '*.prql']
    mimetypes = [
        'application/prql',
        'application/x-prql']
    version_added = '2.17'
    builtinTypes = words(('bool', 'int', 'int8', 'int16', 'int32', 'int64', 'int128', 'float', 'text', 'set'), suffix = '\\b')
    
    def innerstring_rules(ttype):
        return [
            ('\\{((\\w+)((\\.\\w+)|(\\[[^\\]]+\\]))*)?(\\:(.?[<>=\\^])?[-+ ]?#?0?(\\d+)?,?(\\.\\d+)?[E-GXb-gnosx%]?)?\\}', String.Interpol),
            ('[^\\\\\\\'"%{\\n]+', ttype),
            ('[\\\'"\\\\]', ttype),
            ('%|(\\{{1,2})', ttype)]

    
    def fstring_rules(ttype):
        return [
            ('\\}', String.Interpol),
            ('\\{', String.Interpol, 'expr-inside-fstring'),
            ('[^\\\\\\\'"{}\\n]+', ttype),
            ('[\\\'"\\\\]', ttype)]

# WARNING: Decompyle incomplete
