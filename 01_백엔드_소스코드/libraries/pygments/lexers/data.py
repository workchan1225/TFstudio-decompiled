# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: data.pyc (Python 3.11)

'''
    pygments.lexers.data
    ~~~~~~~~~~~~~~~~~~~~

    Lexers for data file format.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.lexer import Lexer, ExtendedRegexLexer, LexerContext, include, bygroups
from pygments.token import Comment, Error, Keyword, Literal, Name, Number, Punctuation, String, Whitespace
__all__ = [
    'YamlLexer',
    'JsonLexer',
    'JsonBareObjectLexer',
    'JsonLdLexer']

class YamlLexerContext(LexerContext):
    pass
# WARNING: Decompyle incomplete


class YamlLexer(ExtendedRegexLexer):
    pass
# WARNING: Decompyle incomplete


class JsonLexer(Lexer):
    '''
    For JSON data structures.

    Javascript-style comments are supported (like ``/* */`` and ``//``),
    though comments are not part of the JSON specification.
    This allows users to highlight JSON as it is used in the wild.

    No validation is performed on the input JSON document.
    '''
    name = 'JSON'
    url = 'https://www.json.org'
    aliases = [
        'json',
        'json-object']
    filenames = [
        '*.json',
        '*.jsonl',
        '*.ndjson',
        'Pipfile.lock']
    mimetypes = [
        'application/json',
        'application/json-object',
        'application/x-ndjson',
        'application/jsonl',
        'application/json-seq']
    version_added = '1.5'
    integers = set('-0123456789')
    floats = set('.eE+')
    constants = set('truefalsenull')
    hexadecimals = set('0123456789abcdefABCDEF')
    punctuations = set('{}[],')
    whitespaces = {
        '\n',
        ' ',
        '\t',
        '\r'}
    
    def get_tokens_unprocessed(self, text):
        '''Parse JSON data.'''
        pass
    # WARNING: Decompyle incomplete



class JsonBareObjectLexer(JsonLexer):
    '''
    For JSON data structures (with missing object curly braces).

    .. deprecated:: 2.8.0

       Behaves the same as `JsonLexer` now.
    '''
    name = 'JSONBareObject'
    aliases = []
    filenames = []
    mimetypes = []
    version_added = '2.2'


class JsonLdLexer(JsonLexer):
    pass
# WARNING: Decompyle incomplete
