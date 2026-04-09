# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mojo.pyc (Python 3.11)

'''
    pygments.lexers.mojo
    ~~~~~~~~~~~~~~~~~~~~

    Lexers for Mojo and related languages.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import keyword
from pygments import unistring as uni
from pygments.lexer import RegexLexer, bygroups, combined, default, include, this, using, words
from pygments.token import Comment, Keyword, Name, Number, Operator, Punctuation, String, Text, Whitespace
from pygments.util import shebang_matches
__all__ = [
    'MojoLexer']

class MojoLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'MojoLexer'
    __doc__ = '\n    For Mojo source code (version 24.2.1).\n    '
    name = 'Mojo'
    url = 'https://docs.modular.com/mojo/'
    aliases = [
        'mojo',
        '🔥']
    filenames = [
        '*.mojo',
        '*.🔥']
    mimetypes = [
        'text/x-mojo',
        'application/x-mojo']
    version_added = '2.18'
    uni_name = f'''[{uni.xid_start}][{uni.xid_continue}]*'''
    
    def innerstring_rules(ttype):
        return [
            ('%(\\(\\w+\\))?[-#0 +]*([0-9]+|[*])?(\\.([0-9]+|[*]))?[hlL]?[E-GXc-giorsaux%]', String.Interpol),
            ('\\{((\\w+)((\\.\\w+)|(\\[[^\\]]+\\]))*)?(\\![sra])?(\\:(.?[<>=\\^])?[-+ ]?#?0?(\\d+)?,?(\\.\\d+)?[E-GXb-gnosx%]?)?\\}', String.Interpol),
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
