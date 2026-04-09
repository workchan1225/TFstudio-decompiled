# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: special.pyc (Python 3.11)

'''
    pygments.lexers.special
    ~~~~~~~~~~~~~~~~~~~~~~~

    Special lexers.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import ast
from pygments.lexer import Lexer, line_re
from pygments.token import Token, Error, Text, Generic
from pygments.util import get_choice_opt
__all__ = [
    'TextLexer',
    'OutputLexer',
    'RawTokenLexer']

class TextLexer(Lexer):
    '''
    "Null" lexer, doesn\'t highlight anything.
    '''
    name = 'Text only'
    aliases = [
        'text']
    filenames = [
        '*.txt']
    mimetypes = [
        'text/plain']
    url = ''
    version_added = ''
    priority = 0.01
    
    def get_tokens_unprocessed(self, text):
        pass
    # WARNING: Decompyle incomplete

    
    def analyse_text(text):
        return TextLexer.priority



class OutputLexer(Lexer):
    '''
    Simple lexer that highlights everything as ``Token.Generic.Output``.
    '''
    name = 'Text output'
    aliases = [
        'output']
    url = ''
    version_added = '2.10'
    _example = 'output/output'
    
    def get_tokens_unprocessed(self, text):
        pass
    # WARNING: Decompyle incomplete


_ttype_cache = { }

class RawTokenLexer(Lexer):
    '''
    Recreate a token stream formatted with the `RawTokenFormatter`.

    Additional options accepted:

    `compress`
        If set to ``"gz"`` or ``"bz2"``, decompress the token stream with
        the given compression algorithm before lexing (default: ``""``).
    '''
    name = 'Raw token data'
    aliases = []
    filenames = []
    mimetypes = [
        'application/x-pygments-tokens']
    url = 'https://pygments.org/docs/formatters/#RawTokenFormatter'
    version_added = ''
    
    def __init__(self, **options):
        self.compress = get_choice_opt(options, 'compress', [
            '',
            'none',
            'gz',
            'bz2'], '')
    # WARNING: Decompyle incomplete

    
    def get_tokens(self, text):
        pass
    # WARNING: Decompyle incomplete

    
    def get_tokens_unprocessed(self, text):
        pass
    # WARNING: Decompyle incomplete
