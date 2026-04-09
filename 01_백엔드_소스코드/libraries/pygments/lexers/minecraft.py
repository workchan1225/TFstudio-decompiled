# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: minecraft.pyc (Python 3.11)

'''
    pygments.lexers.minecraft
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for Minecraft related languages.

    SNBT. A data communication format used in Minecraft.
    wiki: https://minecraft.wiki/w/NBT_format

    MCFunction. The Function file for Minecraft Data packs and Add-ons.
    official: https://learn.microsoft.com/en-us/minecraft/creator/documents/functionsintroduction
    wiki: https://minecraft.wiki/w/Function

    MCSchema. A kind of data Schema for Minecraft Add-on Development.
    official: https://learn.microsoft.com/en-us/minecraft/creator/reference/content/schemasreference/
    community example: https://www.mcbe-dev.net/addons/data-driven/manifest.html

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.lexer import RegexLexer, default, include, bygroups
from pygments.token import Comment, Keyword, Literal, Name, Number, Operator, Punctuation, String, Text, Whitespace
__all__ = [
    'SNBTLexer',
    'MCFunctionLexer',
    'MCSchemaLexer']

class SNBTLexer(RegexLexer):
    '''Lexer for stringified NBT, a data format used in Minecraft
    '''
    name = 'SNBT'
    url = 'https://minecraft.wiki/w/NBT_format'
    aliases = [
        'snbt']
    filenames = [
        '*.snbt']
    mimetypes = [
        'text/snbt']
    version_added = '2.12'
    tokens = {
        'root': [
            ('\\{', Punctuation, 'compound'),
            ('[^\\{]+', Text)],
        'whitespace': [
            ('\\s+', Whitespace)],
        'operators': [
            ('[,:;]', Punctuation)],
        'literals': [
            ('(true|false)', Keyword.Constant),
            ('-?\\d+[eE]-?\\d+', Number.Float),
            ('-?\\d*\\.\\d+[fFdD]?', Number.Float),
            ('-?\\d+[bBsSlLfFdD]?', Number.Integer),
            ('"', String.Double, 'literals.string_double'),
            ("'", String.Single, 'literals.string_single')],
        'literals.string_double': [
            ('\\\\.', String.Escape),
            ('[^\\\\"\\n]+', String.Double),
            ('"', String.Double, '#pop')],
        'literals.string_single': [
            ('\\\\.', String.Escape),
            ("[^\\\\'\\n]+", String.Single),
            ("'", String.Single, '#pop')],
        'compound': [
            ('[A-Z_a-z]+', Name.Attribute),
            include('operators'),
            include('whitespace'),
            include('literals'),
            ('\\{', Punctuation, '#push'),
            ('\\[', Punctuation, 'list'),
            ('\\}', Punctuation, '#pop')],
        'list': [
            ('[A-Z_a-z]+', Name.Attribute),
            include('literals'),
            include('operators'),
            include('whitespace'),
            ('\\[', Punctuation, '#push'),
            ('\\{', Punctuation, 'compound'),
            ('\\]', Punctuation, '#pop')] }


class MCFunctionLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'MCFunctionLexer'
    __doc__ = 'Lexer for the mcfunction scripting language used in Minecraft\n    Modelled somewhat after the `GitHub mcfunction grammar <https://github.com/Arcensoth/language-mcfunction>`_.\n    '
    name = 'MCFunction'
    url = 'https://minecraft.wiki/w/Commands'
    aliases = [
        'mcfunction',
        'mcf']
    filenames = [
        '*.mcfunction']
    mimetypes = [
        'text/mcfunction']
    version_added = '2.12'
    _block_comment_prefix = '[>!]'
# WARNING: Decompyle incomplete


class MCSchemaLexer(RegexLexer):
    '''Lexer for Minecraft Add-ons data Schemas, an interface structure standard used in Minecraft
    '''
    name = 'MCSchema'
    url = 'https://learn.microsoft.com/en-us/minecraft/creator/reference/content/schemasreference/'
    aliases = [
        'mcschema']
    filenames = [
        '*.mcschema']
    mimetypes = [
        'text/mcschema']
    version_added = '2.14'
    tokens = {
        'commentsandwhitespace': [
            ('\\s+', Whitespace),
            ('//.*?$', Comment.Single),
            ('/\\*.*?\\*/', Comment.Multiline)],
        'slashstartsregex': [
            include('commentsandwhitespace'),
            ('/(\\\\.|[^[/\\\\\\n]|\\[(\\\\.|[^\\]\\\\\\n])*])+/([gimuysd]+\\b|\\B)', String.Regex, '#pop'),
            ('(?=/)', Text, ('#pop', 'badregex')),
            default('#pop')],
        'badregex': [
            ('\\n', Whitespace, '#pop')],
        'singlestring': [
            ('\\\\.', String.Escape),
            ("'", String.Single, '#pop'),
            ("[^\\\\']+", String.Single)],
        'doublestring': [
            ('\\\\.', String.Escape),
            ('"', String.Double, '#pop'),
            ('[^\\\\"]+', String.Double)],
        'root': [
            ('^(?=\\s|/|<!--)', Text, 'slashstartsregex'),
            include('commentsandwhitespace'),
            ('(?<=: )opt', Operator.Word),
            ('(?<=\\s)[\\w-]*(?=(\\s+"|\\n))', Keyword.Declaration),
            ('0[bB][01]+', Number.Bin),
            ('0[oO]?[0-7]+', Number.Oct),
            ('0[xX][0-9a-fA-F]+', Number.Hex),
            ('\\d+', Number.Integer),
            ('(\\.\\d+|\\d+\\.\\d*|\\d+)([eE][-+]?\\d+)?', Number.Float),
            ('\\.\\.\\.|=>', Punctuation),
            ('\\+\\+|--|~|\\?\\?=?|\\?|:|\\\\(?=\\n)|(<<|>>>?|==?|!=?|(?:\\*\\*|\\|\\||&&|[-<>+*%&|^/]))=?', Operator, 'slashstartsregex'),
            ('[{(\\[;,]', Punctuation, 'slashstartsregex'),
            ('[})\\].]', Punctuation),
            ("'", String.Single, 'singlestring'),
            ('"', String.Double, 'doublestring'),
            ('[\\w-]*?(?=:\\{?\\n)', String.Symbol),
            ('([\\w-]*?)(:)(\\d+)(?:(\\.)(\\d+)(?:(\\.)(\\d+)(?:(\\-)((?:[^\\W_]|-)*(?:\\.(?:[^\\W_]|-)*)*))?(?:(\\+)((?:[^\\W_]|-)+(?:\\.(?:[^\\W_]|-)+)*))?)?)?(?=:\\{?\\n)', bygroups(String.Symbol, Operator, Number.Integer, Operator, Number.Integer, Operator, Number.Integer, Operator, String, Operator, String)),
            ('.*\\n', Text)] }
