# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tls.pyc (Python 3.11)

'''
    pygments.lexers.tls
    ~~~~~~~~~~~~~~~~~~~

    Lexers for the TLS presentation language.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import RegexLexer, words
from pygments.token import Comment, Operator, Keyword, Name, String, Number, Punctuation, Whitespace
__all__ = [
    'TlsLexer']

class TlsLexer(RegexLexer):
    '''
    The TLS presentation language, described in RFC 8446.
    '''
    name = 'TLS Presentation Language'
    url = 'https://www.rfc-editor.org/rfc/rfc8446#section-3'
    filenames = []
    aliases = [
        'tls']
    mimetypes = []
    version_added = '2.16'
    flags = re.MULTILINE | re.DOTALL
    tokens = {
        'root': [
            ('\\s+', Whitespace),
            ('/[*].*?[*]/', Comment.Multiline),
            (words(('struct', 'enum', 'select', 'case'), suffix = '\\b'), Keyword),
            (words(('uint8', 'uint16', 'uint24', 'uint32', 'uint64', 'opaque'), suffix = '\\b'), Keyword.Type),
            ('0x[0-9a-fA-F]+', Number.Hex),
            ('[0-9]+', Number.Integer),
            ('"(\\\\.|[^"\\\\])*"', String),
            ('[.]{2}', Operator),
            ('[+\\-*/&^]', Operator),
            ('[|<>=!()\\[\\]{}.,;:\\?]', Punctuation),
            ('[^\\W\\d]\\w*', Name.Other)] }
