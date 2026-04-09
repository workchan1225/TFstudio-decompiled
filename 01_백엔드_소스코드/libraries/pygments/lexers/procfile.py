# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: procfile.pyc (Python 3.11)

'''
    pygments.lexers.procfile
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lexer for Procfile file format.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.lexer import RegexLexer, bygroups
from pygments.token import Name, Number, String, Text, Punctuation
__all__ = [
    'ProcfileLexer']

class ProcfileLexer(RegexLexer):
    '''
    Lexer for Procfile file format.

    The format is used to run processes on Heroku or is used by Foreman or
    Honcho tools.
    '''
    name = 'Procfile'
    url = 'https://devcenter.heroku.com/articles/procfile#procfile-format'
    aliases = [
        'procfile']
    filenames = [
        'Procfile']
    version_added = '2.10'
    tokens = {
        'root': [
            ('^([a-z]+)(:)', bygroups(Name.Label, Punctuation)),
            ('\\s+', Text.Whitespace),
            ('"[^"]*"', String),
            ("'[^']*'", String),
            ('[0-9]+', Number.Integer),
            ('\\$[a-zA-Z_][\\w]*', Name.Variable),
            ('(\\w+)(=)(\\w+)', bygroups(Name.Variable, Punctuation, String)),
            ('([\\w\\-\\./]+)', Text)] }
