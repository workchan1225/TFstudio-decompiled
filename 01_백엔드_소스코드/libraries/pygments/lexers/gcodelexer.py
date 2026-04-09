# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: gcodelexer.pyc (Python 3.11)

'''
    pygments.lexers.gcodelexer
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for the G Code Language.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.lexer import RegexLexer, bygroups
from pygments.token import Comment, Name, Text, Keyword, Number
__all__ = [
    'GcodeLexer']

class GcodeLexer(RegexLexer):
    '''
    For gcode source code.
    '''
    name = 'g-code'
    aliases = [
        'gcode']
    filenames = [
        '*.gcode']
    url = 'https://en.wikipedia.org/wiki/G-code'
    version_added = '2.9'
    tokens = {
        'root': [
            (';.*\\n', Comment),
            ('^[gmGM]\\d{1,4}\\s', Name.Builtin),
            ('([^gGmM])([+-]?\\d*[.]?\\d+)', bygroups(Keyword, Number)),
            ('\\s', Text.Whitespace),
            ('.*\\n', Text)] }
