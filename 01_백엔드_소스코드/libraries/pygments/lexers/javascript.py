# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: javascript.pyc (Python 3.11)

'''
    pygments.lexers.javascript
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for JavaScript and related languages.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import bygroups, combined, default, do_insertions, include, inherit, Lexer, RegexLexer, this, using, words, line_re
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Other, Generic, Whitespace
from pygments.util import get_bool_opt
from pygments.unistring import unistring as uni
__all__ = [
    'JavascriptLexer',
    'KalLexer',
    'LiveScriptLexer',
    'DartLexer',
    'TypeScriptLexer',
    'LassoLexer',
    'ObjectiveJLexer',
    'CoffeeScriptLexer',
    'MaskLexer',
    'EarlGreyLexer',
    'JuttleLexer',
    'NodeConsoleLexer']
JS_IDENT_START = '(?:[$_' + uni.combine('Lu', 'Ll', 'Lt', 'Lm', 'Lo', 'Nl') + ']|\\\\u[a-fA-F0-9]{4})'
JS_IDENT_PART = '(?:[$' + uni.combine('Lu', 'Ll', 'Lt', 'Lm', 'Lo', 'Nl', 'Mn', 'Mc', 'Nd', 'Pc') + '‌‍]|\\\\u[a-fA-F0-9]{4})'
JS_IDENT = JS_IDENT_START + '(?:' + JS_IDENT_PART + ')*'

class JavascriptLexer(RegexLexer):
    '''
    For JavaScript source code.
    '''
    name = 'JavaScript'
    url = 'https://www.ecma-international.org/publications-and-standards/standards/ecma-262/'
    aliases = [
        'javascript',
        'js']
    filenames = [
        '*.js',
        '*.jsm',
        '*.mjs',
        '*.cjs']
    mimetypes = [
        'application/javascript',
        'application/x-javascript',
        'text/x-javascript',
        'text/javascript']
    version_added = ''
    flags = re.DOTALL | re.MULTILINE
    tokens = {
        'commentsandwhitespace': [
            ('\\s+', Whitespace),
            ('<!--', Comment),
            ('//.*?$', Comment.Single),
            ('/\\*.*?\\*/', Comment.Multiline)],
        'slashstartsregex': [
            include('commentsandwhitespace'),
            ('/(\\\\.|[^[/\\\\\\n]|\\[(\\\\.|[^\\]\\\\\\n])*])+/([gimuysd]+\\b|\\B)', String.Regex, '#pop'),
            ('(?=/)', Text, ('#pop', 'badregex')),
            default('#pop')],
        'badregex': [
            ('\\n', Whitespace, '#pop')],
        'root': [
            ('\\A#! ?/.*?$', Comment.Hashbang),
            ('^(?=\\s|/|<!--)', Text, 'slashstartsregex'),
            include('commentsandwhitespace'),
            ('0[bB][01]+n?', Number.Bin),
            ('0[oO]?[0-7]+n?', Number.Oct),
            ('0[xX][0-9a-fA-F]+n?', Number.Hex),
            ('[0-9]+n', Number.Integer),
            ('(\\.[0-9]+|[0-9]+\\.[0-9]*|[0-9]+)([eE][-+]?[0-9]+)?', Number.Float),
            ('\\.\\.\\.|=>', Punctuation),
            ('\\+\\+|--|~|\\?\\?=?|\\?|:|\\\\(?=\\n)|(<<|>>>?|==?|!=?|(?:\\*\\*|\\|\\||&&|[-<>+*%&|^/]))=?', Operator, 'slashstartsregex'),
            ('[{(\\[;,]', Punctuation, 'slashstartsregex'),
            ('[})\\].]', Punctuation),
            ('(typeof|instanceof|in|void|delete|new)\\b', Operator.Word, 'slashstartsregex'),
            ('\\b(constructor|from|as)\\b', Keyword.Reserved),
            ('(for|in|while|do|break|return|continue|switch|case|default|if|else|throw|try|catch|finally|yield|await|async|this|of|static|export|import|debugger|extends|super)\\b', Keyword, 'slashstartsregex'),
            ('(var|let|const|with|function|class)\\b', Keyword.Declaration, 'slashstartsregex'),
            ('(abstract|boolean|byte|char|double|enum|final|float|goto|implements|int|interface|long|native|package|private|protected|public|short|synchronized|throws|transient|volatile)\\b', Keyword.Reserved),
            ('(true|false|null|NaN|Infinity|undefined)\\b', Keyword.Constant),
            ('(Array|Boolean|Date|BigInt|Function|Math|ArrayBuffer|Number|Object|RegExp|String|Promise|Proxy|decodeURI|decodeURIComponent|encodeURI|encodeURIComponent|eval|isFinite|isNaN|parseFloat|parseInt|DataView|document|window|globalThis|global|Symbol|Intl|WeakSet|WeakMap|Set|Map|Reflect|JSON|Atomics|Int(?:8|16|32)Array|BigInt64Array|Float32Array|Float64Array|Uint8ClampedArray|Uint(?:8|16|32)Array|BigUint64Array)\\b', Name.Builtin),
            ('((?:Eval|Internal|Range|Reference|Syntax|Type|URI)?Error)\\b', Name.Exception),
            ('(super)(\\s*)(\\([\\w,?.$\\s]+\\s*\\))', bygroups(Keyword, Whitespace), 'slashstartsregex'),
            ('([a-zA-Z_?.$][\\w?.$]*)(?=\\(\\) \\{)', Name.Other, 'slashstartsregex'),
            (JS_IDENT, Name.Other),
            ('"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Double),
            ("'(\\\\\\\\|\\\\[^\\\\]|[^'\\\\])*'", String.Single),
            ('`', String.Backtick, 'interp'),
            ('#[a-zA-Z_]\\w*', Name)],
        'interp': [
            ('`', String.Backtick, '#pop'),
            ('\\\\.', String.Backtick),
            ('\\$\\{', String.Interpol, 'interp-inside'),
            ('\\$', String.Backtick),
            ('[^`\\\\$]+', String.Backtick)],
        'interp-inside': [
            ('\\}', String.Interpol, '#pop'),
            include('root')] }


class TypeScriptLexer(JavascriptLexer):
    '''
    For TypeScript source code.
    '''
    name = 'TypeScript'
    url = 'https://www.typescriptlang.org/'
    aliases = [
        'typescript',
        'ts']
    filenames = [
        '*.ts']
    mimetypes = [
        'application/x-typescript',
        'text/x-typescript']
    version_added = '1.6'
    priority = 0.5
    tokens = {
        'root': [
            ('(abstract|implements|private|protected|public|readonly)\\b', Keyword, 'slashstartsregex'),
            ('(enum|interface|override)\\b', Keyword.Declaration, 'slashstartsregex'),
            ('\\b(declare|type)\\b', Keyword.Reserved),
            ('\\b(string|boolean|number)\\b', Keyword.Type),
            ('\\b(module)(\\s*)([\\w?.$]+)(\\s*)', bygroups(Keyword.Reserved, Whitespace, Name.Other, Whitespace), 'slashstartsregex'),
            ('([\\w?.$]+)(\\s*)(:)(\\s*)([\\w?.$]+)', bygroups(Name.Other, Whitespace, Operator, Whitespace, Keyword.Type)),
            ('@' + JS_IDENT, Keyword.Declaration),
            inherit,
            ('#[a-zA-Z_]\\w*', Name)] }


class KalLexer(RegexLexer):
    '''
    For Kal source code.
    '''
    name = 'Kal'
    url = 'http://rzimmerman.github.io/kal'
    aliases = [
        'kal']
    filenames = [
        '*.kal']
    mimetypes = [
        'text/kal',
        'application/kal']
    version_added = '2.0'
    flags = re.DOTALL
    tokens = {
        'commentsandwhitespace': [
            ('\\s+', Whitespace),
            ('###[^#].*?###', Comment.Multiline),
            ('(#(?!##[^#]).*?)(\\n)', bygroups(Comment.Single, Whitespace))],
        'functiondef': [
            ('([$a-zA-Z_][\\w$]*)(\\s*)', bygroups(Name.Function, Whitespace), '#pop'),
            include('commentsandwhitespace')],
        'classdef': [
            ('\\b(inherits)(\\s+)(from)\\b', bygroups(Keyword, Whitespace, Keyword)),
            ('([$a-zA-Z_][\\w$]*)(?=\\s*\\n)', Name.Class, '#pop'),
            ('[$a-zA-Z_][\\w$]*\\b', Name.Class),
            include('commentsandwhitespace')],
        'listcomprehension': [
            ('\\]', Punctuation, '#pop'),
            ('\\b(property|value)\\b', Keyword),
            include('root')],
        'waitfor': [
            ('\\n', Whitespace, '#pop'),
            ('\\bfrom\\b', Keyword),
            include('root')],
        'root': [
            include('commentsandwhitespace'),
            ('/(?! )(\\\\.|[^[/\\\\\\n]|\\[(\\\\.|[^\\]\\\\\\n])*])+/([gimuysd]+\\b|\\B)', String.Regex),
            ('\\?|:|_(?=\\n)|==?|!=|-(?!>)|[<>+*/-]=?', Operator),
            ('\\b(and|or|isnt|is|not|but|bitwise|mod|\\^|xor|exists|doesnt\\s+exist)\\b', Operator.Word),
            ('(\\([^()]+\\))?(\\s*)(>)', bygroups(Name.Function, Whitespace, Punctuation)),
            ('[{(]', Punctuation),
            ('\\[', Punctuation, 'listcomprehension'),
            ('[})\\].,]', Punctuation),
            ('\\b(function|method|task)\\b', Keyword.Declaration, 'functiondef'),
            ('\\bclass\\b', Keyword.Declaration, 'classdef'),
            ('\\b(safe(?=\\s))?(\\s*)(wait(?=\\s))(\\s+)(for)\\b', bygroups(Keyword, Whitespace, Keyword, Whitespace, Keyword), 'waitfor'),
            ('\\b(me|this)(\\.[$a-zA-Z_][\\w.$]*)?\\b', Name.Variable.Instance),
            ('(?<![.$])(run)(\\s+)(in)(\\s+)(parallel)\\b', bygroups(Keyword, Whitespace, Keyword, Whitespace, Keyword)),
            ('(?<![.$])(for)(\\s+)(parallel|series)?\\b', bygroups(Keyword, Whitespace, Keyword)),
            ('(?<![.$])(except)(\\s+)(when)?\\b', bygroups(Keyword, Whitespace, Keyword)),
            ('(?<![.$])(fail)(\\s+)(with)?\\b', bygroups(Keyword, Whitespace, Keyword)),
            ('(?<![.$])(inherits)(\\s+)(from)?\\b', bygroups(Keyword, Whitespace, Keyword)),
            ('(?<![.$])(for)(\\s+)(parallel|series)?\\b', bygroups(Keyword, Whitespace, Keyword)),
            (words(('in', 'of', 'while', 'until', 'break', 'return', 'continue', 'when', 'if', 'unless', 'else', 'otherwise', 'throw', 'raise', 'try', 'catch', 'finally', 'new', 'delete', 'typeof', 'instanceof', 'super'), prefix = '(?<![.$])', suffix = '\\b'), Keyword),
            (words(('true', 'false', 'yes', 'no', 'on', 'off', 'null', 'nothing', 'none', 'NaN', 'Infinity', 'undefined'), prefix = '(?<![.$])', suffix = '\\b'), Keyword.Constant),
            (words(('Array', 'Boolean', 'Date', 'Error', 'Function', 'Math', 'Number', 'Object', 'RegExp', 'String', 'decodeURI', 'decodeURIComponent', 'encodeURI', 'encodeURIComponent', 'eval', 'isFinite', 'isNaN', 'isSafeInteger', 'parseFloat', 'parseInt', 'document', 'window', 'globalThis', 'Symbol', 'print'), suffix = '\\b'), Name.Builtin),
            ('([$a-zA-Z_][\\w.$]*)(\\s*)(:|[+\\-*/]?\\=)?\\b', bygroups(Name.Variable, Whitespace, Operator)),
            ('[0-9][0-9]*\\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            ('0x[0-9a-fA-F]+', Number.Hex),
            ('[0-9]+', Number.Integer),
            ('"""', String, 'tdqs'),
            ("'''", String, 'tsqs'),
            ('"', String, 'dqs'),
            ("'", String, 'sqs')],
        'strings': [
            ('[^#\\\\\\\'"]+', String)],
        'interpoling_string': [
            ('\\}', String.Interpol, '#pop'),
            include('root')],
        'dqs': [
            ('"', String, '#pop'),
            ("\\\\.|\\'", String),
            ('#\\{', String.Interpol, 'interpoling_string'),
            include('strings')],
        'sqs': [
            ("'", String, '#pop'),
            ('#|\\\\.|"', String),
            include('strings')],
        'tdqs': [
            ('"""', String, '#pop'),
            ('\\\\.|\\\'|"', String),
            ('#\\{', String.Interpol, 'interpoling_string'),
            include('strings')],
        'tsqs': [
            ("'''", String, '#pop'),
            ('#|\\\\.|\\\'|"', String),
            include('strings')] }


class LiveScriptLexer(RegexLexer):
    '''
    For LiveScript source code.
    '''
    name = 'LiveScript'
    url = 'https://livescript.net/'
    aliases = [
        'livescript',
        'live-script']
    filenames = [
        '*.ls']
    mimetypes = [
        'text/livescript']
    version_added = '1.6'
    flags = re.DOTALL
    tokens = {
        'commentsandwhitespace': [
            ('\\s+', Whitespace),
            ('/\\*.*?\\*/', Comment.Multiline),
            ('(#.*?)(\\n)', bygroups(Comment.Single, Whitespace))],
        'multilineregex': [
            include('commentsandwhitespace'),
            ('//([gimuysd]+\\b|\\B)', String.Regex, '#pop'),
            ('/', String.Regex),
            ('[^/#]+', String.Regex)],
        'slashstartsregex': [
            include('commentsandwhitespace'),
            ('//', String.Regex, ('#pop', 'multilineregex')),
            ('/(?! )(\\\\.|[^[/\\\\\\n]|\\[(\\\\.|[^\\]\\\\\\n])*])+/([gimuysd]+\\b|\\B)', String.Regex, '#pop'),
            ('/', Operator, '#pop'),
            default('#pop')],
        'root': [
            ('\\A(?=\\s|/)', Text, 'slashstartsregex'),
            include('commentsandwhitespace'),
            ('(?:\\([^()]+\\))?[ ]*[~-]{1,2}>|(?:\\(?[^()\\n]+\\)?)?[ ]*<[~-]{1,2}', Name.Function),
            ('\\+\\+|&&|(?<![.$])\\b(?:and|x?or|is|isnt|not)\\b|\\?|:|=|\\|\\||\\\\(?=\\n)|(<<|>>>?|==?|!=?|~(?!\\~?>)|-(?!\\-?>)|<(?!\\[)|(?<!\\])>|[+*`%&|^/])=?', Operator, 'slashstartsregex'),
            ('[{(\\[;,]', Punctuation, 'slashstartsregex'),
            ('[})\\].]', Punctuation),
            ('(?<![.$])(for|own|in|of|while|until|loop|break|return|continue|switch|when|then|if|unless|else|throw|try|catch|finally|new|delete|typeof|instanceof|super|extends|this|class|by|const|var|to|til)\\b', Keyword, 'slashstartsregex'),
            ('(?<![.$])(true|false|yes|no|on|off|null|NaN|Infinity|undefined|void)\\b', Keyword.Constant),
            ('(Array|Boolean|Date|Error|Function|Math|Number|Object|RegExp|String|decodeURI|decodeURIComponent|encodeURI|encodeURIComponent|eval|isFinite|isNaN|parseFloat|parseInt|document|window|globalThis|Symbol|Symbol|BigInt)\\b', Name.Builtin),
            ('([$a-zA-Z_][\\w.\\-:$]*)(\\s*)([:=])(\\s+)', bygroups(Name.Variable, Whitespace, Operator, Whitespace), 'slashstartsregex'),
            ('(@[$a-zA-Z_][\\w.\\-:$]*)(\\s*)([:=])(\\s+)', bygroups(Name.Variable.Instance, Whitespace, Operator, Whitespace), 'slashstartsregex'),
            ('@', Name.Other, 'slashstartsregex'),
            ('@?[$a-zA-Z_][\\w-]*', Name.Other, 'slashstartsregex'),
            ('[0-9]+\\.[0-9]+([eE][0-9]+)?[fd]?(?:[a-zA-Z_]+)?', Number.Float),
            ('[0-9]+(~[0-9a-z]+)?(?:[a-zA-Z_]+)?', Number.Integer),
            ('"""', String, 'tdqs'),
            ("'''", String, 'tsqs'),
            ('"', String, 'dqs'),
            ("'", String, 'sqs'),
            ('\\\\\\S+', String),
            ('<\\[.*?\\]>', String)],
        'strings': [
            ('[^#\\\\\\\'"]+', String)],
        'interpoling_string': [
            ('\\}', String.Interpol, '#pop'),
            include('root')],
        'dqs': [
            ('"', String, '#pop'),
            ("\\\\.|\\'", String),
            ('#\\{', String.Interpol, 'interpoling_string'),
            ('#', String),
            include('strings')],
        'sqs': [
            ("'", String, '#pop'),
            ('#|\\\\.|"', String),
            include('strings')],
        'tdqs': [
            ('"""', String, '#pop'),
            ('\\\\.|\\\'|"', String),
            ('#\\{', String.Interpol, 'interpoling_string'),
            ('#', String),
            include('strings')],
        'tsqs': [
            ("'''", String, '#pop'),
            ('#|\\\\.|\\\'|"', String),
            include('strings')] }


class DartLexer(RegexLexer):
    '''
    For Dart source code.
    '''
    name = 'Dart'
    url = 'http://dart.dev/'
    aliases = [
        'dart']
    filenames = [
        '*.dart']
    mimetypes = [
        'text/x-dart']
    version_added = '1.5'
    flags = re.MULTILINE | re.DOTALL
    tokens = {
        'root': [
            include('string_literal'),
            ('#!(.*?)$', Comment.Preproc),
            ('\\b(import|export)\\b', Keyword, 'import_decl'),
            ('\\b(library|source|part of|part)\\b', Keyword),
            ('[^\\S\\n]+', Whitespace),
            ('(//.*?)(\\n)', bygroups(Comment.Single, Whitespace)),
            ('/\\*.*?\\*/', Comment.Multiline),
            ('\\b(class|extension|mixin)\\b(\\s+)', bygroups(Keyword.Declaration, Whitespace), 'class'),
            ('\\b(as|assert|break|case|catch|const|continue|default|do|else|finally|for|if|in|is|new|rethrow|return|super|switch|this|throw|try|while)\\b', Keyword),
            ('\\b(abstract|async|await|const|covariant|extends|external|factory|final|get|implements|late|native|on|operator|required|set|static|sync|typedef|var|with|yield)\\b', Keyword.Declaration),
            ('\\b(bool|double|dynamic|int|num|Function|Never|Null|Object|String|void)\\b', Keyword.Type),
            ('\\b(false|null|true)\\b', Keyword.Constant),
            ('[~!%^&*+=|?:<>/-]|as\\b', Operator),
            ('@[a-zA-Z_$]\\w*', Name.Decorator),
            ('[a-zA-Z_$]\\w*:', Name.Label),
            ('[a-zA-Z_$]\\w*', Name),
            ('[(){}\\[\\],.;]', Punctuation),
            ('0[xX][0-9a-fA-F]+', Number.Hex),
            ('\\d+(\\.\\d*)?([eE][+-]?\\d+)?', Number),
            ('\\.\\d+([eE][+-]?\\d+)?', Number),
            ('\\n', Whitespace)],
        'class': [
            ('[a-zA-Z_$]\\w*', Name.Class, '#pop')],
        'import_decl': [
            include('string_literal'),
            ('\\s+', Whitespace),
            ('\\b(as|deferred|show|hide)\\b', Keyword),
            ('[a-zA-Z_$]\\w*', Name),
            ('\\,', Punctuation),
            ('\\;', Punctuation, '#pop')],
        'string_literal': [
            ('r"""([\\w\\W]*?)"""', String.Double),
            ("r'''([\\w\\W]*?)'''", String.Single),
            ('r"(.*?)"', String.Double),
            ("r'(.*?)'", String.Single),
            ('"""', String.Double, 'string_double_multiline'),
            ("'''", String.Single, 'string_single_multiline'),
            ('"', String.Double, 'string_double'),
            ("'", String.Single, 'string_single')],
        'string_common': [
            ('\\\\(x[0-9A-Fa-f]{2}|u[0-9A-Fa-f]{4}|u\\{[0-9A-Fa-f]*\\}|[a-z\'\\"$\\\\])', String.Escape),
            ('(\\$)([a-zA-Z_]\\w*)', bygroups(String.Interpol, Name)),
            ('(\\$\\{)(.*?)(\\})', bygroups(String.Interpol, using(this), String.Interpol))],
        'string_double': [
            ('"', String.Double, '#pop'),
            ('[^"$\\\\\\n]+', String.Double),
            include('string_common'),
            ('\\$+', String.Double)],
        'string_double_multiline': [
            ('"""', String.Double, '#pop'),
            ('[^"$\\\\]+', String.Double),
            include('string_common'),
            ('(\\$|\\")+', String.Double)],
        'string_single': [
            ("'", String.Single, '#pop'),
            ("[^'$\\\\\\n]+", String.Single),
            include('string_common'),
            ('\\$+', String.Single)],
        'string_single_multiline': [
            ("'''", String.Single, '#pop'),
            ("[^\\'$\\\\]+", String.Single),
            include('string_common'),
            ("(\\$|\\')+", String.Single)] }


class LassoLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'LassoLexer'
    __doc__ = '\n    For Lasso source code, covering both Lasso 9\n    syntax and LassoScript for Lasso 8.6 and earlier. For Lasso embedded in\n    HTML, use the `LassoHtmlLexer`.\n\n    Additional options accepted:\n\n    `builtinshighlighting`\n        If given and ``True``, highlight builtin types, traits, methods, and\n        members (default: ``True``).\n    `requiredelimiters`\n        If given and ``True``, only highlight code between delimiters as Lasso\n        (default: ``False``).\n    '
    name = 'Lasso'
    aliases = [
        'lasso',
        'lassoscript']
    filenames = [
        '*.lasso',
        '*.lasso[89]']
    version_added = '1.6'
    alias_filenames = [
        '*.incl',
        '*.inc',
        '*.las']
    mimetypes = [
        'text/x-lasso']
    url = 'https://www.lassosoft.com'
    flags = re.IGNORECASE | re.DOTALL | re.MULTILINE
# WARNING: Decompyle incomplete


class ObjectiveJLexer(RegexLexer):
    '''
    For Objective-J source code with preprocessor directives.
    '''
    name = 'Objective-J'
    aliases = [
        'objective-j',
        'objectivej',
        'obj-j',
        'objj']
    filenames = [
        '*.j']
    mimetypes = [
        'text/x-objective-j']
    url = 'https://www.cappuccino.dev/learn/objective-j.html'
    version_added = '1.3'
    _ws = '(?:\\s|//[^\\n]*\\n|/[*](?:[^*]|[*][^/])*[*]/)*'
    flags = re.DOTALL | re.MULTILINE
    tokens = {
        'root': [
            include('whitespace'),
            ('^(' + _ws + '[+-]' + _ws + ')([(a-zA-Z_].*?[^(])(' + _ws + '\\{)', bygroups(using(this), using(this, state = 'function_signature'), using(this))),
            ('(@interface|@implementation)(\\s+)', bygroups(Keyword, Whitespace), 'classname'),
            ('(@class|@protocol)(\\s*)', bygroups(Keyword, Whitespace), 'forward_classname'),
            ('(\\s*)(@end)(\\s*)', bygroups(Whitespace, Keyword, Whitespace)),
            include('statements'),
            ('[{()}]', Punctuation),
            (';', Punctuation)],
        'whitespace': [
            ('(@import)(\\s+)("(?:\\\\\\\\|\\\\"|[^"])*")', bygroups(Comment.Preproc, Whitespace, String.Double)),
            ('(@import)(\\s+)(<(?:\\\\\\\\|\\\\>|[^>])*>)', bygroups(Comment.Preproc, Whitespace, String.Double)),
            ('(#(?:include|import))(\\s+)("(?:\\\\\\\\|\\\\"|[^"])*")', bygroups(Comment.Preproc, Whitespace, String.Double)),
            ('(#(?:include|import))(\\s+)(<(?:\\\\\\\\|\\\\>|[^>])*>)', bygroups(Comment.Preproc, Whitespace, String.Double)),
            ('#if\\s+0', Comment.Preproc, 'if0'),
            ('#', Comment.Preproc, 'macro'),
            ('\\s+', Whitespace),
            ('(\\\\)(\\n)', bygroups(String.Escape, Whitespace)),
            ('//(\\n|(.|\\n)*?[^\\\\]\\n)', Comment.Single),
            ('/(\\\\\\n)?[*](.|\\n)*?[*](\\\\\\n)?/', Comment.Multiline),
            ('<!--', Comment)],
        'slashstartsregex': [
            include('whitespace'),
            ('/(\\\\.|[^[/\\\\\\n]|\\[(\\\\.|[^\\]\\\\\\n])*])+/([gim]+\\b|\\B)', String.Regex, '#pop'),
            ('(?=/)', Text, ('#pop', 'badregex')),
            default('#pop')],
        'badregex': [
            ('\\n', Whitespace, '#pop')],
        'statements': [
            ('(L|@)?"', String, 'string'),
            ("(L|@)?'(\\\\.|\\\\[0-7]{1,3}|\\\\x[a-fA-F0-9]{1,2}|[^\\\\\\'\\n])'", String.Char),
            ('"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Double),
            ("'(\\\\\\\\|\\\\[^\\\\]|[^'\\\\])*'", String.Single),
            ('(\\d+\\.\\d*|\\.\\d+|\\d+)[eE][+-]?\\d+[lL]?', Number.Float),
            ('(\\d+\\.\\d*|\\.\\d+|\\d+[fF])[fF]?', Number.Float),
            ('0x[0-9a-fA-F]+[Ll]?', Number.Hex),
            ('0[0-7]+[Ll]?', Number.Oct),
            ('\\d+[Ll]?', Number.Integer),
            ('^(?=\\s|/|<!--)', Text, 'slashstartsregex'),
            ('\\+\\+|--|~|&&|\\?|:|\\|\\||\\\\(?=\\n)|(<<|>>>?|==?|!=?|[-<>+*%&|^/])=?', Operator, 'slashstartsregex'),
            ('[{(\\[;,]', Punctuation, 'slashstartsregex'),
            ('[})\\].]', Punctuation),
            ('(for|in|while|do|break|return|continue|switch|case|default|if|else|throw|try|catch|finally|new|delete|typeof|instanceof|void|prototype|__proto__)\\b', Keyword, 'slashstartsregex'),
            ('(var|with|function)\\b', Keyword.Declaration, 'slashstartsregex'),
            ('(@selector|@private|@protected|@public|@encode|@synchronized|@try|@throw|@catch|@finally|@end|@property|@synthesize|@dynamic|@for|@accessors|new)\\b', Keyword),
            ('(int|long|float|short|double|char|unsigned|signed|void|id|BOOL|bool|boolean|IBOutlet|IBAction|SEL|@outlet|@action)\\b', Keyword.Type),
            ('(self|super)\\b', Name.Builtin),
            ('(TRUE|YES|FALSE|NO|Nil|nil|NULL)\\b', Keyword.Constant),
            ('(true|false|null|NaN|Infinity|undefined)\\b', Keyword.Constant),
            ('(ABS|ASIN|ACOS|ATAN|ATAN2|SIN|COS|TAN|EXP|POW|CEIL|FLOOR|ROUND|MIN|MAX|RAND|SQRT|E|LN2|LN10|LOG2E|LOG10E|PI|PI2|PI_2|SQRT1_2|SQRT2)\\b', Keyword.Constant),
            ('(Array|Boolean|Date|Error|Function|Math|Number|Object|RegExp|String|decodeURI|decodeURIComponent|encodeURI|encodeURIComponent|Error|eval|isFinite|isNaN|parseFloat|parseInt|document|this|window|globalThis|Symbol)\\b', Name.Builtin),
            ('([$a-zA-Z_]\\w*)(' + _ws + ')(?=\\()', bygroups(Name.Function, using(this))),
            ('[$a-zA-Z_]\\w*', Name)],
        'classname': [
            ('([a-zA-Z_]\\w*)(' + _ws + ':' + _ws + ')([a-zA-Z_]\\w*)?', bygroups(Name.Class, using(this), Name.Class), '#pop'),
            ('([a-zA-Z_]\\w*)(' + _ws + '\\()([a-zA-Z_]\\w*)(\\))', bygroups(Name.Class, using(this), Name.Label, Text), '#pop'),
            ('([a-zA-Z_]\\w*)', Name.Class, '#pop')],
        'forward_classname': [
            ('([a-zA-Z_]\\w*)(\\s*)(,)(\\s*)', bygroups(Name.Class, Whitespace, Text, Whitespace), '#push'),
            ('([a-zA-Z_]\\w*)(\\s*)(;?)', bygroups(Name.Class, Whitespace, Text), '#pop')],
        'function_signature': [
            include('whitespace'),
            ('(\\(' + _ws + ')([a-zA-Z_]\\w+)(' + _ws + '\\)' + _ws + ')([$a-zA-Z_]\\w+' + _ws + ':)', bygroups(using(this), Keyword.Type, using(this), Name.Function), 'function_parameters'),
            ('(\\(' + _ws + ')([a-zA-Z_]\\w+)(' + _ws + '\\)' + _ws + ')([$a-zA-Z_]\\w+)', bygroups(using(this), Keyword.Type, using(this), Name.Function), '#pop'),
            ('([$a-zA-Z_]\\w+' + _ws + ':)', bygroups(Name.Function), 'function_parameters'),
            ('([$a-zA-Z_]\\w+)', bygroups(Name.Function), '#pop'),
            default('#pop')],
        'function_parameters': [
            include('whitespace'),
            ('(\\(' + _ws + ')([^)]+)(' + _ws + '\\)' + _ws + ')([$a-zA-Z_]\\w+)', bygroups(using(this), Keyword.Type, using(this), Text)),
            ('([$a-zA-Z_]\\w+' + _ws + ':)', Name.Function),
            ('(:)', Name.Function),
            ('(,' + _ws + '\\.\\.\\.)', using(this)),
            ('([$a-zA-Z_]\\w+)', Text)],
        'expression': [
            ('([$a-zA-Z_]\\w*)(\\()', bygroups(Name.Function, Punctuation)),
            ('(\\))', Punctuation, '#pop')],
        'string': [
            ('"', String, '#pop'),
            ('\\\\([\\\\abfnrtv"\\\']|x[a-fA-F0-9]{2,4}|[0-7]{1,3})', String.Escape),
            ('[^\\\\"\\n]+', String),
            ('(\\\\)(\\n)', bygroups(String.Escape, Whitespace)),
            ('\\\\', String)],
        'macro': [
            ('[^/\\n]+', Comment.Preproc),
            ('/[*](.|\\n)*?[*]/', Comment.Multiline),
            ('(//.*?)(\\n)', bygroups(Comment.Single, Whitespace), '#pop'),
            ('/', Comment.Preproc),
            ('(?<=\\\\)\\n', Whitespace),
            ('\\n', Whitespace, '#pop')],
        'if0': [
            ('^\\s*#if.*?(?<!\\\\)\\n', Comment.Preproc, '#push'),
            ('^\\s*#endif.*?(?<!\\\\)\\n', Comment.Preproc, '#pop'),
            ('(.*?)(\\n)', bygroups(Comment, Whitespace))] }
    
    def analyse_text(text):
        if re.search('^\\s*@import\\s+[<"]', text, re.MULTILINE):
            return True



class CoffeeScriptLexer(RegexLexer):
    '''
    For CoffeeScript source code.
    '''
    name = 'CoffeeScript'
    url = 'http://coffeescript.org'
    aliases = [
        'coffeescript',
        'coffee-script',
        'coffee']
    filenames = [
        '*.coffee']
    mimetypes = [
        'text/coffeescript']
    version_added = '1.3'
    _operator_re = '\\+\\+|~|&&|\\band\\b|\\bor\\b|\\bis\\b|\\bisnt\\b|\\bnot\\b|\\?|:|\\|\\||\\\\(?=\\n)|(<<|>>>?|==?(?!>)|!=?|=(?!>)|-(?!>)|[<>+*`%&|\\^/])=?'
    flags = re.DOTALL
    tokens = {
        'commentsandwhitespace': [
            ('\\s+', Whitespace),
            ('###[^#].*?###', Comment.Multiline),
            ('(#(?!##[^#]).*?)(\\n)', bygroups(Comment.Single, Whitespace))],
        'multilineregex': [
            ('[^/#]+', String.Regex),
            ('///([gimuysd]+\\b|\\B)', String.Regex, '#pop'),
            ('#\\{', String.Interpol, 'interpoling_string'),
            ('[/#]', String.Regex)],
        'slashstartsregex': [
            include('commentsandwhitespace'),
            ('///', String.Regex, ('#pop', 'multilineregex')),
            ('/(?! )(\\\\.|[^[/\\\\\\n]|\\[(\\\\.|[^\\]\\\\\\n])*])+/([gimuysd]+\\b|\\B)', String.Regex, '#pop'),
            ('/', Operator, '#pop'),
            default('#pop')],
        'root': [
            include('commentsandwhitespace'),
            ('\\A(?=\\s|/)', Text, 'slashstartsregex'),
            (_operator_re, Operator, 'slashstartsregex'),
            ('(?:\\([^()]*\\))?\\s*[=-]>', Name.Function, 'slashstartsregex'),
            ('[{(\\[;,]', Punctuation, 'slashstartsregex'),
            ('[})\\].]', Punctuation),
            ('(?<![.$])(for|own|in|of|while|until|loop|break|return|continue|switch|when|then|if|unless|else|throw|try|catch|finally|new|delete|typeof|instanceof|super|extends|this|class|by)\\b', Keyword, 'slashstartsregex'),
            ('(?<![.$])(true|false|yes|no|on|off|null|NaN|Infinity|undefined)\\b', Keyword.Constant),
            ('(Array|Boolean|Date|Error|Function|Math|Number|Object|RegExp|String|decodeURI|decodeURIComponent|encodeURI|encodeURIComponent|eval|isFinite|isNaN|parseFloat|parseInt|document|window|globalThis|Symbol)\\b', Name.Builtin),
            ('([$a-zA-Z_][\\w.:$]*)(\\s*)([:=])(\\s+)', bygroups(Name.Variable, Whitespace, Operator, Whitespace), 'slashstartsregex'),
            ('(@[$a-zA-Z_][\\w.:$]*)(\\s*)([:=])(\\s+)', bygroups(Name.Variable.Instance, Whitespace, Operator, Whitespace), 'slashstartsregex'),
            ('@', Name.Other, 'slashstartsregex'),
            ('@?[$a-zA-Z_][\\w$]*', Name.Other),
            ('[0-9][0-9]*\\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            ('0x[0-9a-fA-F]+', Number.Hex),
            ('[0-9]+', Number.Integer),
            ('"""', String, 'tdqs'),
            ("'''", String, 'tsqs'),
            ('"', String, 'dqs'),
            ("'", String, 'sqs')],
        'strings': [
            ('[^#\\\\\\\'"]+', String)],
        'interpoling_string': [
            ('\\}', String.Interpol, '#pop'),
            include('root')],
        'dqs': [
            ('"', String, '#pop'),
            ("\\\\.|\\'", String),
            ('#\\{', String.Interpol, 'interpoling_string'),
            ('#', String),
            include('strings')],
        'sqs': [
            ("'", String, '#pop'),
            ('#|\\\\.|"', String),
            include('strings')],
        'tdqs': [
            ('"""', String, '#pop'),
            ('\\\\.|\\\'|"', String),
            ('#\\{', String.Interpol, 'interpoling_string'),
            ('#', String),
            include('strings')],
        'tsqs': [
            ("'''", String, '#pop'),
            ('#|\\\\.|\\\'|"', String),
            include('strings')] }


class MaskLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'MaskLexer'
    __doc__ = '\n    For Mask markup.\n    '
    name = 'Mask'
    url = 'https://github.com/atmajs/MaskJS'
    aliases = [
        'mask']
    filenames = [
        '*.mask']
    mimetypes = [
        'text/x-mask']
    version_added = '2.0'
    flags = re.MULTILINE | re.IGNORECASE | re.DOTALL
# WARNING: Decompyle incomplete


class EarlGreyLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'EarlGreyLexer'
    __doc__ = '\n    For Earl-Grey source code.\n\n    .. versionadded: 2.1\n    '
    name = 'Earl Grey'
    aliases = [
        'earl-grey',
        'earlgrey',
        'eg']
    filenames = [
        '*.eg']
    mimetypes = [
        'text/x-earl-grey']
    url = 'https://github.com/breuleux/earl-grey'
    version_added = ''
# WARNING: Decompyle incomplete


class JuttleLexer(RegexLexer):
    '''
    For Juttle source code.
    '''
    name = 'Juttle'
    url = 'http://juttle.github.io/'
    aliases = [
        'juttle']
    filenames = [
        '*.juttle']
    mimetypes = [
        'application/juttle',
        'application/x-juttle',
        'text/x-juttle',
        'text/juttle']
    version_added = '2.2'
    flags = re.DOTALL | re.MULTILINE
    tokens = {
        'commentsandwhitespace': [
            ('\\s+', Whitespace),
            ('(//.*?)(\\n)', bygroups(Comment.Single, Whitespace)),
            ('/\\*.*?\\*/', Comment.Multiline)],
        'slashstartsregex': [
            include('commentsandwhitespace'),
            ('/(\\\\.|[^[/\\\\\\n]|\\[(\\\\.|[^\\]\\\\\\n])*])+/([gimuysd]+\\b|\\B)', String.Regex, '#pop'),
            ('(?=/)', Text, ('#pop', 'badregex')),
            default('#pop')],
        'badregex': [
            ('\\n', Text, '#pop')],
        'root': [
            ('^(?=\\s|/)', Text, 'slashstartsregex'),
            include('commentsandwhitespace'),
            (':\\d{2}:\\d{2}:\\d{2}(\\.\\d*)?:', String.Moment),
            (':(now|beginning|end|forever|yesterday|today|tomorrow|(\\d+(\\.\\d*)?|\\.\\d+)(ms|[smhdwMy])?):', String.Moment),
            (':\\d{4}-\\d{2}-\\d{2}(T\\d{2}:\\d{2}:\\d{2}(\\.\\d*)?)?(Z|[+-]\\d{2}:\\d{2}|[+-]\\d{4})?:', String.Moment),
            (':((\\d+(\\.\\d*)?|\\.\\d+)[ ]+)?(millisecond|second|minute|hour|day|week|month|year)[s]?(([ ]+and[ ]+(\\d+[ ]+)?(millisecond|second|minute|hour|day|week|month|year)[s]?)|[ ]+(ago|from[ ]+now))*:', String.Moment),
            ('\\+\\+|--|~|&&|\\?|:|\\|\\||\\\\(?=\\n)|(==?|!=?|[-<>+*%&|^/])=?', Operator, 'slashstartsregex'),
            ('[{(\\[;,]', Punctuation, 'slashstartsregex'),
            ('[})\\].]', Punctuation),
            ('(import|return|continue|if|else)\\b', Keyword, 'slashstartsregex'),
            ('(var|const|function|reducer|sub|input)\\b', Keyword.Declaration, 'slashstartsregex'),
            ('(batch|emit|filter|head|join|keep|pace|pass|put|read|reduce|remove|sequence|skip|sort|split|tail|unbatch|uniq|view|write)\\b', Keyword.Reserved),
            ('(true|false|null|Infinity)\\b', Keyword.Constant),
            ('(Array|Date|Juttle|Math|Number|Object|RegExp|String)\\b', Name.Builtin),
            (JS_IDENT, Name.Other),
            ('[0-9][0-9]*\\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            ('[0-9]+', Number.Integer),
            ('"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Double),
            ("'(\\\\\\\\|\\\\[^\\\\]|[^'\\\\])*'", String.Single)] }


class NodeConsoleLexer(Lexer):
    """
    For parsing within an interactive Node.js REPL, such as:

    .. sourcecode:: nodejsrepl

        > let a = 3
        undefined
        > a
        3
        > let b = '4'
        undefined
        > b
        '4'
        > b == a
        false

    .. versionadded: 2.10
    """
    name = 'Node.js REPL console session'
    aliases = [
        'nodejsrepl']
    mimetypes = [
        'text/x-nodejsrepl']
    url = 'https://nodejs.org'
    version_added = ''
    
    def get_tokens_unprocessed(self, text):
        pass
    # WARNING: Decompyle incomplete
