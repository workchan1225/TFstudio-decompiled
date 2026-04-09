# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: jsonnet.pyc (Python 3.11)

'''
    pygments.lexers.jsonnet
    ~~~~~~~~~~~~~~~~~~~~~~~

    Lexer for Jsonnet data templating language.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.lexer import include, RegexLexer, words
from pygments.token import Comment, Keyword, Name, Number, Operator, Punctuation, String, Text, Whitespace
__all__ = [
    'JsonnetLexer']
jsonnet_token = '[^\\W\\d]\\w*'
jsonnet_function_token = jsonnet_token + '(?=\\()'

def string_rules(quote_mark):
    return [
        (f'''[^{quote_mark}\\\\]''', String),
        ('\\\\.', String.Escape),
        (quote_mark, String, '#pop')]


def quoted_field_name(quote_mark):
    return [
        (f'''([^{quote_mark}\\\\]|\\\\.)*{quote_mark}''', Name.Variable, 'field_separator')]


class JsonnetLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'JsonnetLexer'
    __doc__ = 'Lexer for Jsonnet source code.'
    name = 'Jsonnet'
    aliases = [
        'jsonnet']
    filenames = [
        '*.jsonnet',
        '*.libsonnet']
    url = 'https://jsonnet.org'
    version_added = ''
# WARNING: Decompyle incomplete
