# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: c_cpp.pyc (Python 3.11)

'''
    pygments.lexers.c_cpp
    ~~~~~~~~~~~~~~~~~~~~~

    Lexers for C/C++ languages.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import RegexLexer, include, bygroups, using, this, inherit, default, words
from pygments.util import get_bool_opt
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Whitespace
__all__ = [
    'CLexer',
    'CppLexer']

class CFamilyLexer(RegexLexer):
    '''
    For C family source code.  This is used as a base class to avoid repetitious
    definitions.
    '''
    _ws1 = '\\s*(?:/[*].*?[*]/\\s*)?'
    _hexpart = "[0-9a-fA-F](\\'?[0-9a-fA-F])*"
    _decpart = "\\d(\\'?\\d)*"
    _intsuffix = '(([uU][lL]{0,2})|[lL]{1,2}[uU]?)?'
    _ident = '(?!\\d)(?:[\\w$]|\\\\u[0-9a-fA-F]{4}|\\\\U[0-9a-fA-F]{8})+'
    _namespaced_ident = '(?!\\d)(?:[\\w$]|\\\\u[0-9a-fA-F]{4}|\\\\U[0-9a-fA-F]{8}|::)+'
    _comment_single = '//(?:.|(?<=\\\\)\\n)*\\n'
    _comment_multiline = '/(?:\\\\\\n)?[*](?:[^*]|[*](?!(?:\\\\\\n)?/))*[*](?:\\\\\\n)?/'
    _possible_comments = f'''\\s*(?:(?:(?:{_comment_single})|(?:{_comment_multiline}))\\s*)*'''
    tokens = {
        'whitespace': [
            ('^#if\\s+0', Comment.Preproc, 'if0'),
            ('^#', Comment.Preproc, 'macro'),
            ('^(' + _ws1 + ')(#if\\s+0)', bygroups(using(this), Comment.Preproc), 'if0'),
            ('^(' + _ws1 + ')(#)', bygroups(using(this), Comment.Preproc), 'macro'),
            ('(^[ \\t]*)(?!(?:public|private|protected|default)\\b)(' + _ident + ')(\\s*)(:)(?!:)', bygroups(Whitespace, Name.Label, Whitespace, Punctuation)),
            ('\\n', Whitespace),
            ('[^\\S\\n]+', Whitespace),
            ('\\\\\\n', Text),
            (_comment_single, Comment.Single),
            (_comment_multiline, Comment.Multiline),
            ('/(\\\\\\n)?[*][\\w\\W]*', Comment.Multiline)],
        'statements': [
            include('keywords'),
            include('types'),
            ('([LuU]|u8)?(")', bygroups(String.Affix, String), 'string'),
            ("([LuU]|u8)?(')(\\\\.|\\\\[0-7]{1,3}|\\\\x[a-fA-F0-9]{1,2}|[^\\\\\\'\\n])(')", bygroups(String.Affix, String.Char, String.Char, String.Char)),
            ('0[xX](' + _hexpart + '\\.' + _hexpart + '|\\.' + _hexpart + '|' + _hexpart + ')[pP][+-]?' + _hexpart + '[lL]?', Number.Float),
            ('(-)?(' + _decpart + '\\.' + _decpart + '|\\.' + _decpart + '|' + _decpart + ')[eE][+-]?' + _decpart + '[fFlL]?', Number.Float),
            ('(-)?((' + _decpart + '\\.(' + _decpart + ')?|\\.' + _decpart + ')[fFlL]?)|(' + _decpart + '[fFlL])', Number.Float),
            ('(-)?0[xX]' + _hexpart + _intsuffix, Number.Hex),
            ("(-)?0[bB][01](\\'?[01])*" + _intsuffix, Number.Bin),
            ("(-)?0(\\'?[0-7])+" + _intsuffix, Number.Oct),
            ('(-)?' + _decpart + _intsuffix, Number.Integer),
            ('[~!%^&*+=|?:<>/-]', Operator),
            ('[()\\[\\],.]', Punctuation),
            ('(true|false|NULL)\\b', Name.Builtin),
            (_ident, Name)],
        'types': [
            (words(('int8', 'int16', 'int32', 'int64', 'wchar_t'), prefix = '__', suffix = '\\b'), Keyword.Reserved),
            (words(('bool', 'int', 'long', 'float', 'short', 'double', 'char', 'unsigned', 'signed', 'void', '_BitInt', '__int128'), suffix = '\\b'), Keyword.Type)],
        'keywords': [
            ('(struct|union)(\\s+)', bygroups(Keyword, Whitespace), 'classname'),
            ('case\\b', Keyword, 'case-value'),
            (words(('asm', 'auto', 'break', 'const', 'continue', 'default', 'do', 'else', 'enum', 'extern', 'for', 'goto', 'if', 'register', 'restricted', 'return', 'sizeof', 'struct', 'static', 'switch', 'typedef', 'volatile', 'while', 'union', 'thread_local', 'alignas', 'alignof', 'static_assert', '_Pragma'), suffix = '\\b'), Keyword),
            (words(('inline', '_inline', '__inline', 'naked', 'restrict', 'thread'), suffix = '\\b'), Keyword.Reserved),
            ('(__m(128i|128d|128|64))\\b', Keyword.Reserved),
            (words(('asm', 'based', 'except', 'stdcall', 'cdecl', 'fastcall', 'declspec', 'finally', 'try', 'leave', 'w64', 'unaligned', 'raise', 'noop', 'identifier', 'forceinline', 'assume'), prefix = '__', suffix = '\\b'), Keyword.Reserved)],
        'root': [
            include('whitespace'),
            include('keywords'),
            ('(' + _namespaced_ident + '(?:[&*\\s])+)(' + _possible_comments + ')(' + _namespaced_ident + ')(' + _possible_comments + ')(\\([^;"\\\')]*?\\))(' + _possible_comments + ')([^;{/"\\\']*)(\\{)', bygroups(using(this), using(this, state = 'whitespace'), Name.Function, using(this, state = 'whitespace'), using(this), using(this, state = 'whitespace'), using(this), Punctuation), 'function'),
            ('(' + _namespaced_ident + '(?:[&*\\s])+)(' + _possible_comments + ')(' + _namespaced_ident + ')(' + _possible_comments + ')(\\([^;"\\\')]*?\\))(' + _possible_comments + ')([^;/"\\\']*)(;)', bygroups(using(this), using(this, state = 'whitespace'), Name.Function, using(this, state = 'whitespace'), using(this), using(this, state = 'whitespace'), using(this), Punctuation)),
            include('types'),
            default('statement')],
        'statement': [
            include('whitespace'),
            include('statements'),
            ('\\}', Punctuation),
            ('[{;]', Punctuation, '#pop')],
        'function': [
            include('whitespace'),
            include('statements'),
            (';', Punctuation),
            ('\\{', Punctuation, '#push'),
            ('\\}', Punctuation, '#pop')],
        'string': [
            ('"', String, '#pop'),
            ('\\\\([\\\\abfnrtv"\\\']|x[a-fA-F0-9]{2,4}|u[a-fA-F0-9]{4}|U[a-fA-F0-9]{8}|[0-7]{1,3})', String.Escape),
            ('[^\\\\"\\n]+', String),
            ('\\\\\\n', String),
            ('\\\\', String)],
        'macro': [
            ('(' + _ws1 + ')(include)(' + _ws1 + ')("[^"]+")([^\\n]*)', bygroups(using(this), Comment.Preproc, using(this), Comment.PreprocFile, Comment.Single)),
            ('(' + _ws1 + ')(include)(' + _ws1 + ')(<[^>]+>)([^\\n]*)', bygroups(using(this), Comment.Preproc, using(this), Comment.PreprocFile, Comment.Single)),
            ('[^/\\n]+', Comment.Preproc),
            ('/[*](.|\\n)*?[*]/', Comment.Multiline),
            ('//.*?\\n', Comment.Single, '#pop'),
            ('/', Comment.Preproc),
            ('(?<=\\\\)\\n', Comment.Preproc),
            ('\\n', Comment.Preproc, '#pop')],
        'if0': [
            ('^\\s*#if.*?(?<!\\\\)\\n', Comment.Preproc, '#push'),
            ('^\\s*#el(?:se|if).*\\n', Comment.Preproc, '#pop'),
            ('^\\s*#endif.*?(?<!\\\\)\\n', Comment.Preproc, '#pop'),
            ('.*?\\n', Comment)],
        'classname': [
            (_ident, Name.Class, '#pop'),
            ('\\s*(?=>)', Text, '#pop'),
            default('#pop')],
        'case-value': [
            ('(?<!:)(:)(?!:)', Punctuation, '#pop'),
            (_ident, Name.Constant),
            include('whitespace'),
            include('statements')] }
    stdlib_types = {
        'DIR',
        'FILE',
        'div_t',
        'off_t',
        'fpos_t',
        'ldiv_t',
        'size_t',
        'time_t',
        'wint_t',
        'clock_t',
        'jmp_buf',
        'ssize_t',
        'va_list',
        'wchar_t',
        'wctype_t',
        'mbstate_t',
        'ptrdiff_t',
        'wctrans_t',
        'sig_atomic_t'}
    c99_types = {
        'int8_t',
        'int16_t',
        'int32_t',
        'int64_t',
        'uint8_t',
        'intmax_t',
        'intptr_t',
        'uint16_t',
        'uint32_t',
        'uint64_t',
        'uintmax_t',
        'uintptr_t',
        'int_fast8_t',
        'int_fast16_t',
        'int_fast32_t',
        'int_fast64_t',
        'int_least8_t',
        'uint_fast8_t',
        'int_least16_t',
        'int_least32_t',
        'int_least64_t',
        'uint_fast16_t',
        'uint_fast32_t',
        'uint_fast64_t',
        'uint_least8_t',
        'uint_least16_t',
        'uint_least32_t',
        'uint_least64_t'}
    linux_types = {
        'id_t',
        'dev_t',
        'gid_t',
        'ino_t',
        'key_t',
        'pid_t',
        'sig_t',
        'uid_t',
        'mode_t',
        'nfds_t',
        'rlim_t',
        'timer_t',
        'sigset_t',
        'sigval_t',
        'clockid_t',
        'cpu_set_t',
        'cpumask_t',
        'siginfo_t',
        'socklen_t',
        'sighandler_t'}
    c11_atomic_types = {
        'atomic_int',
        'atomic_bool',
        'atomic_char',
        'atomic_long',
        'atomic_uint',
        'atomic_llong',
        'atomic_schar',
        'atomic_short',
        'atomic_uchar',
        'atomic_ulong',
        'atomic_size_t',
        'atomic_ullong',
        'atomic_ushort',
        'atomic_wchar_t',
        'atomic_char16_t',
        'atomic_char32_t',
        'atomic_intmax_t',
        'atomic_intptr_t',
        'atomic_ptrdiff_t',
        'atomic_uintmax_t',
        'atomic_uintptr_t',
        'atomic_int_fast8_t',
        'atomic_int_fast16_t',
        'atomic_int_fast32_t',
        'atomic_int_fast64_t',
        'atomic_int_least8_t',
        'atomic_uint_fast8_t',
        'atomic_int_least16_t',
        'atomic_int_least32_t',
        'atomic_int_least64_t',
        'atomic_uint_fast16_t',
        'atomic_uint_fast32_t',
        'atomic_uint_fast64_t',
        'atomic_uint_least8_t',
        'atomic_uint_least16_t',
        'atomic_uint_least32_t',
        'atomic_uint_least64_t'}
    
    def __init__(self, **options):
        self.stdlibhighlighting = get_bool_opt(options, 'stdlibhighlighting', True)
        self.c99highlighting = get_bool_opt(options, 'c99highlighting', True)
        self.c11highlighting = get_bool_opt(options, 'c11highlighting', True)
        self.platformhighlighting = get_bool_opt(options, 'platformhighlighting', True)
    # WARNING: Decompyle incomplete

    
    def get_tokens_unprocessed(self, text, stack = (('root',),)):
        pass
    # WARNING: Decompyle incomplete



class CLexer(CFamilyLexer):
    '''
    For C source code with preprocessor directives.

    Additional options accepted:

    `stdlibhighlighting`
        Highlight common types found in the C/C++ standard library (e.g. `size_t`).
        (default: ``True``).

    `c99highlighting`
        Highlight common types found in the C99 standard library (e.g. `int8_t`).
        Actually, this includes all fixed-width integer types.
        (default: ``True``).

    `c11highlighting`
        Highlight atomic types found in the C11 standard library (e.g. `atomic_bool`).
        (default: ``True``).

    `platformhighlighting`
        Highlight common types found in the platform SDK headers (e.g. `clockid_t` on Linux).
        (default: ``True``).
    '''
    name = 'C'
    aliases = [
        'c']
    filenames = [
        '*.c',
        '*.h',
        '*.idc',
        '*.x[bp]m']
    mimetypes = [
        'text/x-chdr',
        'text/x-csrc',
        'image/x-xbitmap',
        'image/x-xpixmap']
    url = 'https://en.wikipedia.org/wiki/C_(programming_language)'
    version_added = ''
    priority = 0.1
    tokens = {
        'keywords': [
            (words(('_Alignas', '_Alignof', '_Noreturn', '_Generic', '_Thread_local', '_Static_assert', '_Imaginary', 'noreturn', 'imaginary', 'complex'), suffix = '\\b'), Keyword),
            inherit],
        'types': [
            (words(('_Bool', '_Complex', '_Atomic'), suffix = '\\b'), Keyword.Type),
            inherit] }
    
    def analyse_text(text):
        if re.search('^\\s*#include [<"]', text, re.MULTILINE):
            return 0.1
        if None.search('^\\s*#ifn?def ', text, re.MULTILINE):
            return 0.1



class CppLexer(CFamilyLexer):
    '''
    For C++ source code with preprocessor directives.

    Additional options accepted:

    `stdlibhighlighting`
        Highlight common types found in the C/C++ standard library (e.g. `size_t`).
        (default: ``True``).

    `c99highlighting`
        Highlight common types found in the C99 standard library (e.g. `int8_t`).
        Actually, this includes all fixed-width integer types.
        (default: ``True``).

    `c11highlighting`
        Highlight atomic types found in the C11 standard library (e.g. `atomic_bool`).
        (default: ``True``).

    `platformhighlighting`
        Highlight common types found in the platform SDK headers (e.g. `clockid_t` on Linux).
        (default: ``True``).
    '''
    name = 'C++'
    url = 'https://isocpp.org/'
    aliases = [
        'cpp',
        'c++']
    filenames = [
        '*.cpp',
        '*.hpp',
        '*.c++',
        '*.h++',
        '*.cc',
        '*.hh',
        '*.cxx',
        '*.hxx',
        '*.C',
        '*.H',
        '*.cp',
        '*.CPP',
        '*.tpp']
    mimetypes = [
        'text/x-c++hdr',
        'text/x-c++src']
    version_added = ''
    priority = 0.1
    tokens = {
        'statements': [
            ('((?:[LuU]|u8)?R)(")([^\\\\()\\s]{,16})(\\()((?:.|\\n)*?)(\\)\\3)(")', bygroups(String.Affix, String, String.Delimiter, String.Delimiter, String, String.Delimiter, String)),
            inherit],
        'root': [
            inherit,
            (words(('virtual_inheritance', 'uuidof', 'super', 'single_inheritance', 'multiple_inheritance', 'interface', 'event'), prefix = '__', suffix = '\\b'), Keyword.Reserved),
            ('__(offload|blockingoffload|outer)\\b', Keyword.Pseudo)],
        'enumname': [
            include('whitespace'),
            (words(('class', 'struct'), suffix = '\\b'), Keyword),
            (CFamilyLexer._ident, Name.Class, '#pop'),
            ('\\s*(?=>)', Text, '#pop'),
            default('#pop')],
        'keywords': [
            ('(class|concept|typename)(\\s+)', bygroups(Keyword, Whitespace), 'classname'),
            (words(('catch', 'const_cast', 'delete', 'dynamic_cast', 'explicit', 'export', 'friend', 'mutable', 'new', 'operator', 'private', 'protected', 'public', 'reinterpret_cast', 'class', '__restrict', 'static_cast', 'template', 'this', 'throw', 'throws', 'try', 'typeid', 'using', 'virtual', 'constexpr', 'nullptr', 'concept', 'decltype', 'noexcept', 'override', 'final', 'constinit', 'consteval', 'co_await', 'co_return', 'co_yield', 'requires', 'import', 'module', 'typename', 'and', 'and_eq', 'bitand', 'bitor', 'compl', 'not', 'not_eq', 'or', 'or_eq', 'xor', 'xor_eq'), suffix = '\\b'), Keyword),
            ('namespace\\b', Keyword, 'namespace'),
            ('(enum)(\\s+)', bygroups(Keyword, Whitespace), 'enumname'),
            inherit],
        'types': [
            ('char(16_t|32_t|8_t)\\b', Keyword.Type),
            inherit],
        'namespace': [
            ('[;{]', Punctuation, ('#pop', 'root')),
            ('inline\\b', Keyword.Reserved),
            (CFamilyLexer._ident, Name.Namespace),
            include('statement')] }
    
    def analyse_text(text):
        if re.search('#include <[a-z_]+>', text):
            return 0.2
        if None.search('using namespace ', text):
            return 0.4
