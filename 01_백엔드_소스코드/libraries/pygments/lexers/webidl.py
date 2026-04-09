# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: webidl.pyc (Python 3.11)

'''
    pygments.lexers.webidl
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexers for Web IDL, including some extensions.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.lexer import RegexLexer, default, include, words
from pygments.token import Comment, Keyword, Name, Number, Punctuation, String, Text
__all__ = [
    'WebIDLLexer']
_builtin_types = ('byte', 'octet', 'boolean', '(?:unsigned\\s+)?(?:short|long(?:\\s+long)?)', '(?:unrestricted\\s+)?(?:float|double)', 'DOMString', 'ByteString', 'USVString', 'Error', 'DOMException', 'Uint8Array', 'Uint16Array', 'Uint32Array', 'Uint8ClampedArray', 'Float32Array', 'Float64Array', 'ArrayBuffer', 'DataView', 'Int8Array', 'Int16Array', 'Int32Array', 'any', 'void', 'object', 'RegExp')
_identifier = '_?[A-Za-z][a-zA-Z0-9_-]*'
_keyword_suffix = '(?![\\w-])'
_string = '"[^"]*"'

class WebIDLLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'WebIDLLexer'
    __doc__ = '\n    For Web IDL.\n    '
    name = 'Web IDL'
    url = 'https://www.w3.org/wiki/Web_IDL'
    aliases = [
        'webidl']
    filenames = [
        '*.webidl']
    version_added = '2.6'
# WARNING: Decompyle incomplete
