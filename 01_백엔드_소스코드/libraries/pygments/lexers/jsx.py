# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: jsx.pyc (Python 3.11)

'''
    pygments.lexers.jsx
    ~~~~~~~~~~~~~~~~~~~

    Lexers for JSX (React) and TSX (TypeScript flavor).

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import bygroups, default, include, inherit
from pygments.lexers.javascript import JavascriptLexer, TypeScriptLexer
from pygments.token import Name, Operator, Punctuation, String, Text, Whitespace
__all__ = [
    'JsxLexer',
    'TsxLexer']
_JSX_RULES = {
    'jsx': [
        ('</?>', Punctuation),
        ('(<)(\\w+)(\\.?)', bygroups(Punctuation, Name.Tag, Punctuation), 'tag'),
        ('(</)(\\w+)(>)', bygroups(Punctuation, Name.Tag, Punctuation)),
        ('(</)(\\w+)', bygroups(Punctuation, Name.Tag), 'fragment')],
    'tag': [
        ('\\s+', Whitespace),
        ('([\\w-]+)(\\s*)(=)(\\s*)', bygroups(Name.Attribute, Whitespace, Operator, Whitespace), 'attr'),
        ('[{}]+', Punctuation),
        ('[\\w\\.]+', Name.Attribute),
        ('(/?)(\\s*)(>)', bygroups(Punctuation, Text, Punctuation), '#pop')],
    'fragment': [
        ('(.)(\\w+)', bygroups(Punctuation, Name.Attribute)),
        ('(>)', bygroups(Punctuation), '#pop')],
    'attr': [
        ('\\{', Punctuation, 'expression'),
        ('".*?"', String, '#pop'),
        ("'.*?'", String, '#pop'),
        default('#pop')],
    'expression': [
        ('\\{', Punctuation, '#push'),
        ('\\}', Punctuation, '#pop'),
        include('root')] }

class JsxLexer(JavascriptLexer):
    __module__ = __name__
    __qualname__ = 'JsxLexer'
    __doc__ = 'For JavaScript Syntax Extension (JSX).\n    '
    name = 'JSX'
    aliases = [
        'jsx',
        'react']
    filenames = [
        '*.jsx',
        '*.react']
    mimetypes = [
        'text/jsx',
        'text/typescript-jsx']
    url = 'https://facebook.github.io/jsx/'
    version_added = '2.17'
    flags = re.MULTILINE | re.DOTALL
# WARNING: Decompyle incomplete


class TsxLexer(TypeScriptLexer):
    __module__ = __name__
    __qualname__ = 'TsxLexer'
    __doc__ = 'For TypeScript with embedded JSX\n    '
    name = 'TSX'
    aliases = [
        'tsx']
    filenames = [
        '*.tsx']
    mimetypes = [
        'text/typescript-tsx']
    url = 'https://www.typescriptlang.org/docs/handbook/jsx.html'
    version_added = '2.19'
    flags = re.MULTILINE | re.DOTALL
# WARNING: Decompyle incomplete
