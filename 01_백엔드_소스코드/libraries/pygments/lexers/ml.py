# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ml.pyc (Python 3.11)

'''
    pygments.lexers.ml
    ~~~~~~~~~~~~~~~~~~

    Lexers for ML family languages.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import RegexLexer, include, bygroups, default, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Error
__all__ = [
    'SMLLexer',
    'OcamlLexer',
    'OpaLexer',
    'ReasonLexer',
    'FStarLexer']

class SMLLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'SMLLexer'
    __doc__ = '\n    For the Standard ML language.\n    '
    name = 'Standard ML'
    aliases = [
        'sml']
    filenames = [
        '*.sml',
        '*.sig',
        '*.fun']
    mimetypes = [
        'text/x-standardml',
        'application/x-standardml']
    url = 'https://en.wikipedia.org/wiki/Standard_ML'
    version_added = '1.5'
    alphanumid_reserved = {
        'as',
        'do',
        'fn',
        'if',
        'in',
        'of',
        'op',
        'and',
        'end',
        'fun',
        'let',
        'rec',
        'sig',
        'val',
        'case',
        'else',
        'open',
        'then',
        'type',
        'with',
        'infix',
        'local',
        'raise',
        'where',
        'while',
        'eqtype',
        'handle',
        'infixr',
        'nonfix',
        'orelse',
        'struct',
        'abstype',
        'andalso',
        'functor',
        'include',
        'sharing',
        'datatype',
        'withtype',
        'exception',
        'signature',
        'structure'}
    symbolicid_reserved = {
        '=',
        '#',
        ':',
        '->',
        ':>',
        '=>',
        '\\|'}
    nonid_reserved = {
        '...',
        '_',
        '{',
        '}',
        '(',
        ')',
        ',',
        ';',
        '[',
        ']'}
    alphanumid_re = "[a-zA-Z][\\w']*"
    symbolicid_re = '[!%&$#+\\-/:<=>?@\\\\~`^|*]+'
    
    def stringy(whatkind):
        return [
            ('[^"\\\\]', whatkind),
            ('\\\\[\\\\"abtnvfr]', String.Escape),
            ('\\\\\\^[\\x40-\\x5e]', String.Escape),
            ('\\\\[0-9]{3}', String.Escape),
            ('\\\\u[0-9a-fA-F]{4}', String.Escape),
            ('\\\\\\s+\\\\', String.Interpol),
            ('"', whatkind, '#pop')]

    
    def long_id_callback(self, match):
        pass
    # WARNING: Decompyle incomplete

    
    def end_id_callback(self, match):
        pass
    # WARNING: Decompyle incomplete

    
    def id_callback(self, match):
        pass
    # WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete


class OcamlLexer(RegexLexer):
    '''
    For the OCaml language.
    '''
    name = 'OCaml'
    url = 'https://ocaml.org/'
    aliases = [
        'ocaml']
    filenames = [
        '*.ml',
        '*.mli',
        '*.mll',
        '*.mly']
    mimetypes = [
        'text/x-ocaml']
    version_added = '0.7'
    keywords = ('and', 'as', 'assert', 'begin', 'class', 'constraint', 'do', 'done', 'downto', 'else', 'end', 'exception', 'external', 'false', 'for', 'fun', 'function', 'functor', 'if', 'in', 'include', 'inherit', 'initializer', 'lazy', 'let', 'match', 'method', 'module', 'mutable', 'new', 'object', 'of', 'open', 'private', 'raise', 'rec', 'sig', 'struct', 'then', 'to', 'true', 'try', 'type', 'val', 'virtual', 'when', 'while', 'with')
    keyopts = ('!=', '#', '&', '&&', '\\(', '\\)', '\\*', '\\+', ',', '-', '-\\.', '->', '\\.', '\\.\\.', ':', '::', ':=', ':>', ';', ';;', '<', '<-', '=', '>', '>]', '>\\}', '\\?', '\\?\\?', '\\[', '\\[<', '\\[>', '\\[\\|', ']', '_', '`', '\\{', '\\{<', '\\|', '\\|]', '\\}', '~')
    operators = '[!$%&*+\\./:<=>?@^|~-]'
    word_operators = ('asr', 'land', 'lor', 'lsl', 'lxor', 'mod', 'or')
    prefix_syms = '[!?~]'
    infix_syms = '[=<>@^|&+\\*/$%-]'
    primitives = ('unit', 'int', 'float', 'bool', 'string', 'char', 'list', 'array')
    tokens = {
        'escape-sequence': [
            ('\\\\[\\\\"\\\'ntbr]', String.Escape),
            ('\\\\[0-9]{3}', String.Escape),
            ('\\\\x[0-9a-fA-F]{2}', String.Escape)],
        'root': [
            ('\\s+', Text),
            ('false|true|\\(\\)|\\[\\]', Name.Builtin.Pseudo),
            ("\\b([A-Z][\\w\\']*)(?=\\s*\\.)", Name.Namespace, 'dotted'),
            ("\\b([A-Z][\\w\\']*)", Name.Class),
            ('\\(\\*(?![)])', Comment, 'comment'),
            ('\\b({})\\b'.format('|'.join(keywords)), Keyword),
            ('({})'.format('|'.join(keyopts[::-1])), Operator),
            (f'''({infix_syms}|{prefix_syms})?{operators}''', Operator),
            ('\\b({})\\b'.format('|'.join(word_operators)), Operator.Word),
            ('\\b({})\\b'.format('|'.join(primitives)), Keyword.Type),
            ("[^\\W\\d][\\w']*", Name),
            ('-?\\d[\\d_]*(.[\\d_]*)?([eE][+\\-]?\\d[\\d_]*)', Number.Float),
            ('0[xX][\\da-fA-F][\\da-fA-F_]*', Number.Hex),
            ('0[oO][0-7][0-7_]*', Number.Oct),
            ('0[bB][01][01_]*', Number.Bin),
            ('\\d[\\d_]*', Number.Integer),
            ('\'(?:(\\\\[\\\\\\"\'ntbr ])|(\\\\[0-9]{3})|(\\\\x[0-9a-fA-F]{2}))\'', String.Char),
            ("'.'", String.Char),
            ("'", Keyword),
            ('"', String.Double, 'string'),
            ("[~?][a-z][\\w\\']*:", Name.Variable)],
        'comment': [
            ('[^(*)]+', Comment),
            ('\\(\\*', Comment, '#push'),
            ('\\*\\)', Comment, '#pop'),
            ('[(*)]', Comment)],
        'string': [
            ('[^\\\\"]+', String.Double),
            include('escape-sequence'),
            ('\\\\\\n', String.Double),
            ('"', String.Double, '#pop')],
        'dotted': [
            ('\\s+', Text),
            ('\\.', Punctuation),
            ("[A-Z][\\w\\']*(?=\\s*\\.)", Name.Namespace),
            ("[A-Z][\\w\\']*", Name.Class, '#pop'),
            ("[a-z_][\\w\\']*", Name, '#pop'),
            default('#pop')] }


class OpaLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'OpaLexer'
    __doc__ = '\n    Lexer for the Opa language.\n    '
    name = 'Opa'
    aliases = [
        'opa']
    filenames = [
        '*.opa']
    mimetypes = [
        'text/x-opa']
    url = 'http://opalang.org'
    version_added = '1.5'
    keywords = ('and', 'as', 'begin', 'case', 'client', 'css', 'database', 'db', 'do', 'else', 'end', 'external', 'forall', 'function', 'if', 'import', 'match', 'module', 'or', 'package', 'parser', 'rec', 'server', 'then', 'type', 'val', 'with', 'xml_parser')
    ident_re = '(([a-zA-Z_]\\w*)|(`[^`]*`))'
    op_re = '[.=\\-<>,@~%/+?*&^!]'
    punc_re = '[()\\[\\],;|]'
# WARNING: Decompyle incomplete


class ReasonLexer(RegexLexer):
    '''
    For the ReasonML language.
    '''
    name = 'ReasonML'
    url = 'https://reasonml.github.io/'
    aliases = [
        'reasonml',
        'reason']
    filenames = [
        '*.re',
        '*.rei']
    mimetypes = [
        'text/x-reasonml']
    version_added = '2.6'
    keywords = ('as', 'assert', 'begin', 'class', 'constraint', 'do', 'done', 'downto', 'else', 'end', 'exception', 'external', 'false', 'for', 'fun', 'esfun', 'function', 'functor', 'if', 'in', 'include', 'inherit', 'initializer', 'lazy', 'let', 'switch', 'module', 'pub', 'mutable', 'new', 'nonrec', 'object', 'of', 'open', 'pri', 'rec', 'sig', 'struct', 'then', 'to', 'true', 'try', 'type', 'val', 'virtual', 'when', 'while', 'with')
    keyopts = ('!=', '#', '&', '&&', '\\(', '\\)', '\\*', '\\+', ',', '-', '-\\.', '=>', '\\.', '\\.\\.', '\\.\\.\\.', ':', '::', ':=', ':>', ';', ';;', '<', '<-', '=', '>', '>]', '>\\}', '\\?', '\\?\\?', '\\[', '\\[<', '\\[>', '\\[\\|', ']', '_', '`', '\\{', '\\{<', '\\|', '\\|\\|', '\\|]', '\\}', '~')
    operators = '[!$%&*+\\./:<=>?@^|~-]'
    word_operators = ('and', 'asr', 'land', 'lor', 'lsl', 'lsr', 'lxor', 'mod', 'or')
    prefix_syms = '[!?~]'
    infix_syms = '[=<>@^|&+\\*/$%-]'
    primitives = ('unit', 'int', 'float', 'bool', 'string', 'char', 'list', 'array')
    tokens = {
        'escape-sequence': [
            ('\\\\[\\\\"\\\'ntbr]', String.Escape),
            ('\\\\[0-9]{3}', String.Escape),
            ('\\\\x[0-9a-fA-F]{2}', String.Escape)],
        'root': [
            ('\\s+', Text),
            ('false|true|\\(\\)|\\[\\]', Name.Builtin.Pseudo),
            ("\\b([A-Z][\\w\\']*)(?=\\s*\\.)", Name.Namespace, 'dotted'),
            ("\\b([A-Z][\\w\\']*)", Name.Class),
            ('//.*?\\n', Comment.Single),
            ('\\/\\*(?!/)', Comment.Multiline, 'comment'),
            ('\\b({})\\b'.format('|'.join(keywords)), Keyword),
            ('({})'.format('|'.join(keyopts[::-1])), Operator.Word),
            (f'''({infix_syms}|{prefix_syms})?{operators}''', Operator),
            ('\\b({})\\b'.format('|'.join(word_operators)), Operator.Word),
            ('\\b({})\\b'.format('|'.join(primitives)), Keyword.Type),
            ("[^\\W\\d][\\w']*", Name),
            ('-?\\d[\\d_]*(.[\\d_]*)?([eE][+\\-]?\\d[\\d_]*)', Number.Float),
            ('0[xX][\\da-fA-F][\\da-fA-F_]*', Number.Hex),
            ('0[oO][0-7][0-7_]*', Number.Oct),
            ('0[bB][01][01_]*', Number.Bin),
            ('\\d[\\d_]*', Number.Integer),
            ('\'(?:(\\\\[\\\\\\"\'ntbr ])|(\\\\[0-9]{3})|(\\\\x[0-9a-fA-F]{2}))\'', String.Char),
            ("'.'", String.Char),
            ("'", Keyword),
            ('"', String.Double, 'string'),
            ("[~?][a-z][\\w\\']*:", Name.Variable)],
        'comment': [
            ('[^/*]+', Comment.Multiline),
            ('\\/\\*', Comment.Multiline, '#push'),
            ('\\*\\/', Comment.Multiline, '#pop'),
            ('\\*', Comment.Multiline)],
        'string': [
            ('[^\\\\"]+', String.Double),
            include('escape-sequence'),
            ('\\\\\\n', String.Double),
            ('"', String.Double, '#pop')],
        'dotted': [
            ('\\s+', Text),
            ('\\.', Punctuation),
            ("[A-Z][\\w\\']*(?=\\s*\\.)", Name.Namespace),
            ("[A-Z][\\w\\']*", Name.Class, '#pop'),
            ("[a-z_][\\w\\']*", Name, '#pop'),
            default('#pop')] }


class FStarLexer(RegexLexer):
    '''
    For the F* language.
    '''
    name = 'FStar'
    url = 'https://www.fstar-lang.org/'
    aliases = [
        'fstar']
    filenames = [
        '*.fst',
        '*.fsti']
    mimetypes = [
        'text/x-fstar']
    version_added = '2.7'
    keywords = ('abstract', 'attributes', 'noeq', 'unopteq', 'andbegin', 'by', 'default', 'effect', 'else', 'end', 'ensures', 'exception', 'exists', 'false', 'forall', 'fun', 'function', 'if', 'in', 'include', 'inline', 'inline_for_extraction', 'irreducible', 'logic', 'match', 'module', 'mutable', 'new', 'new_effect', 'noextract', 'of', 'open', 'opaque', 'private', 'range_of', 'reifiable', 'reify', 'reflectable', 'requires', 'set_range_of', 'sub_effect', 'synth', 'then', 'total', 'true', 'try', 'type', 'unfold', 'unfoldable', 'val', 'when', 'with', 'not')
    decl_keywords = ('let', 'rec')
    assume_keywords = ('assume', 'admit', 'assert', 'calc')
    keyopts = ('~', '-', '/\\\\', '\\\\/', '<:', '<@', '\\(\\|', '\\|\\)', '#', 'u#', '&', '\\(', '\\)', '\\(\\)', ',', '~>', '->', '<-', '<--', '<==>', '==>', '\\.', '\\?', '\\?\\.', '\\.\\[', '\\.\\(', '\\.\\(\\|', '\\.\\[\\|', '\\{:pattern', ':', '::', ':=', ';', ';;', '=', '%\\[', '!\\{', '\\[', '\\[@', '\\[\\|', '\\|>', '\\]', '\\|\\]', '\\{', '\\|', '\\}', '\\$')
    operators = '[!$%&*+\\./:<=>?@^|~-]'
    prefix_syms = '[!?~]'
    infix_syms = '[=<>@^|&+\\*/$%-]'
    primitives = ('unit', 'int', 'float', 'bool', 'string', 'char', 'list', 'array')
    tokens = {
        'escape-sequence': [
            ('\\\\[\\\\"\\\'ntbr]', String.Escape),
            ('\\\\[0-9]{3}', String.Escape),
            ('\\\\x[0-9a-fA-F]{2}', String.Escape)],
        'root': [
            ('\\s+', Text),
            ('false|true|False|True|\\(\\)|\\[\\]', Name.Builtin.Pseudo),
            ("\\b([A-Z][\\w\\']*)(?=\\s*\\.)", Name.Namespace, 'dotted'),
            ("\\b([A-Z][\\w\\']*)", Name.Class),
            ('\\(\\*(?![)])', Comment, 'comment'),
            ('\\/\\/.+$', Comment),
            ('\\b({})\\b'.format('|'.join(keywords)), Keyword),
            ('\\b({})\\b'.format('|'.join(assume_keywords)), Name.Exception),
            ('\\b({})\\b'.format('|'.join(decl_keywords)), Keyword.Declaration),
            ('({})'.format('|'.join(keyopts[::-1])), Operator),
            (f'''({infix_syms}|{prefix_syms})?{operators}''', Operator),
            ('\\b({})\\b'.format('|'.join(primitives)), Keyword.Type),
            ("[^\\W\\d][\\w']*", Name),
            ('-?\\d[\\d_]*(.[\\d_]*)?([eE][+\\-]?\\d[\\d_]*)', Number.Float),
            ('0[xX][\\da-fA-F][\\da-fA-F_]*', Number.Hex),
            ('0[oO][0-7][0-7_]*', Number.Oct),
            ('0[bB][01][01_]*', Number.Bin),
            ('\\d[\\d_]*', Number.Integer),
            ('\'(?:(\\\\[\\\\\\"\'ntbr ])|(\\\\[0-9]{3})|(\\\\x[0-9a-fA-F]{2}))\'', String.Char),
            ("'.'", String.Char),
            ("'", Keyword),
            ("\\`([\\w\\'.]+)\\`", Operator.Word),
            ('\\`', Keyword),
            ('"', String.Double, 'string'),
            ("[~?][a-z][\\w\\']*:", Name.Variable)],
        'comment': [
            ('[^(*)]+', Comment),
            ('\\(\\*', Comment, '#push'),
            ('\\*\\)', Comment, '#pop'),
            ('[(*)]', Comment)],
        'string': [
            ('[^\\\\"]+', String.Double),
            include('escape-sequence'),
            ('\\\\\\n', String.Double),
            ('"', String.Double, '#pop')],
        'dotted': [
            ('\\s+', Text),
            ('\\.', Punctuation),
            ("[A-Z][\\w\\']*(?=\\s*\\.)", Name.Namespace),
            ("[A-Z][\\w\\']*", Name.Class, '#pop'),
            ("[a-z_][\\w\\']*", Name, '#pop'),
            default('#pop')] }
