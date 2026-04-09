# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: clean.pyc (Python 3.11)

'''
    pygments.lexers.clean
    ~~~~~~~~~~~~~~~~~~~~~

    Lexer for the Clean language.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.lexer import ExtendedRegexLexer, words, default, include, bygroups
from pygments.token import Comment, Error, Keyword, Literal, Name, Number, Operator, Punctuation, String, Whitespace
__all__ = [
    'CleanLexer']

class CleanLexer(ExtendedRegexLexer):
    __module__ = __name__
    __qualname__ = 'CleanLexer'
    __doc__ = '\n    Lexer for the general purpose, state-of-the-art, pure and lazy functional\n    programming language Clean.\n\n    .. versionadded: 2.2\n    '
    name = 'Clean'
    url = 'http://clean.cs.ru.nl/Clean'
    aliases = [
        'clean']
    filenames = [
        '*.icl',
        '*.dcl']
    version_added = ''
    keywords = ('case', 'ccall', 'class', 'code', 'code inline', 'derive', 'export', 'foreign', 'generic', 'if', 'in', 'infix', 'infixl', 'infixr', 'instance', 'let', 'of', 'otherwise', 'special', 'stdcall', 'where', 'with')
    modulewords = ('implementation', 'definition', 'system')
    lowerId = '[a-z`][\\w`]*'
    upperId = '[A-Z`][\\w`]*'
    funnyId = '[~@#$%\\^?!+\\-*<>\\\\/|&=:]+'
    scoreUpperId = '_' + upperId
    scoreLowerId = '_' + lowerId
    moduleId = '[a-zA-Z_][a-zA-Z0-9_.`]+'
    classId = '|'.join([
        lowerId,
        upperId,
        funnyId])
# WARNING: Decompyle incomplete
