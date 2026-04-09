# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: devicetree.pyc (Python 3.11)

'''
    pygments.lexers.devicetree
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for Devicetree language.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.lexer import RegexLexer, bygroups, include, default, words
from pygments.token import Comment, Keyword, Name, Number, Operator, Punctuation, String, Text, Whitespace
__all__ = [
    'DevicetreeLexer']

class DevicetreeLexer(RegexLexer):
    '''
    Lexer for Devicetree files.
    '''
    name = 'Devicetree'
    url = 'https://www.devicetree.org/'
    aliases = [
        'devicetree',
        'dts']
    filenames = [
        '*.dts',
        '*.dtsi']
    mimetypes = [
        'text/x-c']
    version_added = '2.7'
    _ws = '\\s*(?:/[*][^*/]*?[*]/\\s*)*'
    tokens = {
        'macro': [
            ('(#include)(' + _ws + ')([^\\n]+)', bygroups(Comment.Preproc, Comment.Multiline, Comment.PreprocFile)),
            ('(#define)(' + _ws + ')([^\\n]+)', bygroups(Comment.Preproc, Comment.Multiline, Comment.Preproc)),
            ('(/[^*/{]+/)(' + _ws + ')("[^\\n{]+")', bygroups(Comment.Preproc, Comment.Multiline, Comment.PreprocFile)),
            ('(/[^*/{]+/)(' + _ws + ')([^\\n;{]*)([;]?)', bygroups(Comment.Preproc, Comment.Multiline, Comment.Preproc, Punctuation))],
        'whitespace': [
            ('\\n', Whitespace),
            ('\\s+', Whitespace),
            ('\\\\\\n', Text),
            ('//(\\n|[\\w\\W]*?[^\\\\]\\n)', Comment.Single),
            ('/(\\\\\\n)?[*][\\w\\W]*?[*](\\\\\\n)?/', Comment.Multiline),
            ('/(\\\\\\n)?[*][\\w\\W]*', Comment.Multiline)],
        'statements': [
            ('(L?)(")', bygroups(String.Affix, String), 'string'),
            ('0x[0-9a-fA-F]+', Number.Hex),
            ('\\d+', Number.Integer),
            ('([^\\s{}/*]*)(\\s*)(:)', bygroups(Name.Label, Text, Punctuation), '#pop'),
            (words(('compatible', 'model', 'phandle', 'status', '#address-cells', '#size-cells', 'reg', 'virtual-reg', 'ranges', 'dma-ranges', 'device_type', 'name'), suffix = '\\b'), Keyword.Reserved),
            ('([~!%^&*+=|?:<>/#-])', Operator),
            ('[()\\[\\]{},.]', Punctuation),
            ('[a-zA-Z_][\\w-]*(?=(?:\\s*,\\s*[a-zA-Z_][\\w-]*|(?:' + _ws + '))*\\s*[=;])', Name),
            ('[a-zA-Z_]\\w*', Name.Attribute)],
        'root': [
            include('whitespace'),
            include('macro'),
            ('([^/*@\\s&]+|/)(@?)((?:0x)?[0-9a-fA-F,]*)(' + _ws + ')(\\{)', bygroups(Name.Function, Operator, Number.Integer, Comment.Multiline, Punctuation), 'node'),
            default('statement')],
        'statement': [
            include('whitespace'),
            include('statements'),
            (';', Punctuation, '#pop')],
        'node': [
            include('whitespace'),
            include('macro'),
            ('([^/*@\\s&]+|/)(@?)((?:0x)?[0-9a-fA-F,]*)(' + _ws + ')(\\{)', bygroups(Name.Function, Operator, Number.Integer, Comment.Multiline, Punctuation), '#push'),
            include('statements'),
            ('\\};', Punctuation, '#pop'),
            (';', Punctuation)],
        'string': [
            ('"', String, '#pop'),
            ('\\\\([\\\\abfnrtv"\\\']|x[a-fA-F0-9]{2,4}|u[a-fA-F0-9]{4}|U[a-fA-F0-9]{8}|[0-7]{1,3})', String.Escape),
            ('[^\\\\"\\n]+', String),
            ('\\\\\\n', String),
            ('\\\\', String)] }
