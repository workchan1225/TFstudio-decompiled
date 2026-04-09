# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dylan.pyc (Python 3.11)

'''
    pygments.lexers.dylan
    ~~~~~~~~~~~~~~~~~~~~~

    Lexers for the Dylan language.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import Lexer, RegexLexer, bygroups, do_insertions, default, line_re
from pygments.token import Comment, Operator, Keyword, Name, String, Number, Punctuation, Generic, Literal, Whitespace
__all__ = [
    'DylanLexer',
    'DylanConsoleLexer',
    'DylanLidLexer']

class DylanLexer(RegexLexer):
    '''
    For the Dylan language.
    '''
    name = 'Dylan'
    url = 'http://www.opendylan.org/'
    aliases = [
        'dylan']
    filenames = [
        '*.dylan',
        '*.dyl',
        '*.intr']
    mimetypes = [
        'text/x-dylan']
    version_added = '0.7'
    flags = re.IGNORECASE
    builtins = {
        'inline-only',
        'compiler-open',
        'each-subclass',
        'compiler-sideways',
        'open',
        'slot',
        'block',
        'class',
        'macro',
        'domain',
        'import',
        'inline',
        'method',
        'module',
        'sealed',
        'thread',
        'dynamic',
        'exclude',
        'generic',
        'handler',
        'keyword',
        'library',
        'primary',
        'virtual',
        'abstract',
        'concrete',
        'constant',
        'function',
        'instance',
        'required',
        'sideways',
        'subclass',
        'variable',
        'exception',
        'inherited',
        'interface',
        'singleton'}
    keywords = {
        'by',
        'if',
        'in',
        'to',
        'end',
        'for',
        'let',
        'use',
        'case',
        'else',
        'from',
        'then',
        'when',
        'above',
        'begin',
        'below',
        'local',
        'until',
        'while',
        'create',
        'define',
        'elseif',
        'export',
        'rename',
        'select',
        'signal',
        'unless',
        'cleanup',
        'finally',
        'otherwise',
        'afterwards'}
    operators = {
        '<=',
        '==',
        '>=',
        '~=',
        '~==',
        '*',
        '-',
        '<',
        '=',
        '>',
        '|',
        '~',
        '&',
        '+',
        '^'}
    functions = {
        'add!',
        'any?',
        'odd?',
        'even?',
        'fill!',
        'sort!',
        'zero?',
        'empty?',
        'every?',
        'floor/',
        'map-as',
        'one-of',
        'round/',
        'add-new',
        'logbit?',
        'member?',
        'remove!',
        'add-new!',
        'ceiling/',
        'false-or',
        'find-key',
        'key-test',
        'map-into',
        'pop-last',
        'reverse!',
        'subtype?',
        'choose-by',
        'instance?',
        'integral?',
        'negative?',
        'positive?',
        'push-last',
        'truncate/',
        'add-method',
        'check-type',
        'type-union',
        'aref-setter',
        'do-handlers',
        'find-method',
        'head-setter',
        'last-setter',
        'next-method',
        'object-hash',
        'remove-key!',
        'size-setter',
        'tail-setter',
        'as-lowercase',
        'as-uppercase',
        'first-setter',
        'key-sequence',
        'object-class',
        'return-query',
        'shallow-copy',
        'third-setter',
        'as-lowercase!',
        'as-uppercase!',
        'copy-sequence',
        'remove-method',
        'restart-query',
        'second-setter',
        'type-for-copy',
        'concatenate-as',
        'element-setter',
        'table-protocol',
        'default-handler',
        'return-allowed?',
        'row-major-index',
        'all-superclasses',
        'merge-hash-codes',
        'type-error-value',
        'direct-subclasses',
        'remove-duplicates',
        'replace-elements!',
        'slot-initialized?',
        'applicable-method?',
        'function-arguments',
        'remove-duplicates!',
        'return-description',
        'direct-superclasses',
        'replace-subsequence!',
        'subsequence-position',
        'function-specializers',
        'function-return-values',
        'condition-format-string',
        'generic-function-methods',
        'type-error-expected-type',
        'sorted-applicable-methods',
        'condition-format-arguments',
        'forward-iteration-protocol',
        'backward-iteration-protocol',
        'generic-function-mandatory-keywords',
        'as',
        'do',
        'abs',
        'add',
        'ash',
        'gcd',
        'lcm',
        'map',
        'max',
        'min',
        'pop',
        'aref',
        'head',
        'last',
        'list',
        'make',
        'pair',
        'push',
        'rank',
        'size',
        'sort',
        'tail',
        'abort',
        'apply',
        'break',
        'curry',
        'error',
        'first',
        'floor',
        'range',
        'round',
        'third',
        'union',
        'always',
        'cerror',
        'choose',
        'logand',
        'logior',
        'lognot',
        'logxor',
        'modulo',
        'rcurry',
        'reduce',
        'remove',
        'second',
        'signal',
        'values',
        'vector',
        'ceiling',
        'compose',
        'conjoin',
        'disjoin',
        'element',
        'limited',
        'reduce1',
        'reverse',
        'identity',
        'negative',
        'truncate',
        'dimension',
        'remainder',
        'singleton',
        'complement',
        'dimensions',
        'initialize',
        'concatenate',
        'intersection'}
    valid_name = '\\\\?[\\w!&*<>|^$%@\\-+~?/=]+'
    
    def get_tokens_unprocessed(self, text):
        pass
    # WARNING: Decompyle incomplete

    tokens = {
        'root': [
            ('\\s+', Whitespace),
            ('//.*?\\n', Comment.Single),
            ('([a-z0-9-]+)(:)([ \\t]*)(.*(?:\\n[ \\t].+)*)', bygroups(Name.Attribute, Operator, Whitespace, String)),
            default('code')],
        'code': [
            ('\\s+', Whitespace),
            ('(//.*?)(\\n)', bygroups(Comment.Single, Whitespace)),
            ('/\\*', Comment.Multiline, 'comment'),
            ('"', String, 'string'),
            ("'(\\\\.|\\\\[0-7]{1,3}|\\\\x[a-f0-9]{1,2}|[^\\\\\\'\\n])'", String.Char),
            ('#b[01]+', Number.Bin),
            ('#o[0-7]+', Number.Oct),
            ('[-+]?(\\d*\\.\\d+(e[-+]?\\d+)?|\\d+(\\.\\d*)?e[-+]?\\d+)', Number.Float),
            ('[-+]?\\d+', Number.Integer),
            ('#x[0-9a-f]+', Number.Hex),
            ('(\\?' + valid_name + ')(:)(token|name|variable|expression|body|case-body|\\*)', bygroups(Name.Tag, Operator, Name.Builtin)),
            ('(\\?)(:)(token|name|variable|expression|body|case-body|\\*)', bygroups(Name.Tag, Operator, Name.Builtin)),
            ('\\?' + valid_name, Name.Tag),
            ('(=>|::|#\\(|#\\[|##|\\?\\?|\\?=|\\?|[(){}\\[\\],.;])', Punctuation),
            (':=', Operator),
            ('#[tf]', Literal),
            ('#"', String.Symbol, 'keyword'),
            ('#[a-z0-9-]+', Keyword),
            (valid_name + ':', Keyword),
            ('<' + valid_name + '>', Name.Class),
            ('\\*' + valid_name + '\\*', Name.Variable.Global),
            ('\\$' + valid_name, Name.Constant),
            (valid_name, Name)],
        'comment': [
            ('[^*/]+', Comment.Multiline),
            ('/\\*', Comment.Multiline, '#push'),
            ('\\*/', Comment.Multiline, '#pop'),
            ('[*/]', Comment.Multiline)],
        'keyword': [
            ('"', String.Symbol, '#pop'),
            ('[^\\\\"]+', String.Symbol)],
        'string': [
            ('"', String, '#pop'),
            ('\\\\([\\\\abfnrtv"\\\']|x[a-f0-9]{2,4}|[0-7]{1,3})', String.Escape),
            ('[^\\\\"\\n]+', String),
            ('\\\\\\n', String),
            ('\\\\', String)] }


class DylanLidLexer(RegexLexer):
    '''
    For Dylan LID (Library Interchange Definition) files.
    '''
    name = 'DylanLID'
    aliases = [
        'dylan-lid',
        'lid']
    filenames = [
        '*.lid',
        '*.hdp']
    mimetypes = [
        'text/x-dylan-lid']
    url = 'http://www.opendylan.org/'
    version_added = '1.6'
    flags = re.IGNORECASE
    tokens = {
        'root': [
            ('\\s+', Whitespace),
            ('(//.*?)(\\n)', bygroups(Comment.Single, Whitespace)),
            ('(.*?)(:)([ \\t]*)(.*(?:\\n[ \\t].+)*)', bygroups(Name.Attribute, Operator, Whitespace, String))] }


class DylanConsoleLexer(Lexer):
    '''
    For Dylan interactive console output.

    This is based on a copy of the ``RubyConsoleLexer``.
    '''
    name = 'Dylan session'
    aliases = [
        'dylan-console',
        'dylan-repl']
    filenames = [
        '*.dylan-console']
    mimetypes = [
        'text/x-dylan-console']
    url = 'http://www.opendylan.org/'
    version_added = '1.6'
    _example = 'dylan-console/console.dylan-console'
    _prompt_re = re.compile('\\?| ')
    
    def get_tokens_unprocessed(self, text):
        pass
    # WARNING: Decompyle incomplete
