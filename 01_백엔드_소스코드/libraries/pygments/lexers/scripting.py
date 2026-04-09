# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scripting.pyc (Python 3.11)

'''
    pygments.lexers.scripting
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexer for scripting and embedded languages.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import RegexLexer, include, bygroups, default, combined, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Error, Whitespace, Other
from pygments.util import get_bool_opt, get_list_opt
__all__ = [
    'LuaLexer',
    'LuauLexer',
    'MoonScriptLexer',
    'ChaiscriptLexer',
    'LSLLexer',
    'AppleScriptLexer',
    'RexxLexer',
    'MOOCodeLexer',
    'HybrisLexer',
    'EasytrieveLexer',
    'JclLexer',
    'MiniScriptLexer']

def all_lua_builtins():
    MODULES = MODULES
    import pygments.lexers._lua_builtins
    return MODULES.values()()


class LuaLexer(RegexLexer):
    """
    For Lua source code.

    Additional options accepted:

    `func_name_highlighting`
        If given and ``True``, highlight builtin function names
        (default: ``True``).
    `disabled_modules`
        If given, must be a list of module names whose function names
        should not be highlighted. By default all modules are highlighted.

        To get a list of allowed modules have a look into the
        `_lua_builtins` module:

        .. sourcecode:: pycon

            >>> from pygments.lexers._lua_builtins import MODULES
            >>> MODULES.keys()
            ['string', 'coroutine', 'modules', 'io', 'basic', ...]
    """
    name = 'Lua'
    url = 'https://www.lua.org/'
    aliases = [
        'lua']
    filenames = [
        '*.lua',
        '*.wlua']
    mimetypes = [
        'text/x-lua',
        'application/x-lua']
    version_added = ''
    _comment_multiline = '(?:--\\[(?P<level>=*)\\[[\\w\\W]*?\\](?P=level)\\])'
    _comment_single = '(?:--.*$)'
    _space = '(?:\\s+(?!\\s))'
    _s = f'''(?:{_comment_multiline}|{_comment_single}|{_space})'''
    _name = '(?:[^\\W\\d]\\w*)'
    tokens = {
        'root': [
            ('#!.*', Comment.Preproc),
            default('base')],
        'ws': [
            (_comment_multiline, Comment.Multiline),
            (_comment_single, Comment.Single),
            (_space, Whitespace)],
        'base': [
            include('ws'),
            ('(?i)0x[\\da-f]*(\\.[\\da-f]*)?(p[+-]?\\d+)?', Number.Hex),
            ('(?i)(\\d*\\.\\d+|\\d+\\.\\d*)(e[+-]?\\d+)?', Number.Float),
            ('(?i)\\d+e[+-]?\\d+', Number.Float),
            ('\\d+', Number.Integer),
            ('(?s)\\[(=*)\\[.*?\\]\\1\\]', String),
            ('::', Punctuation, 'label'),
            ('\\.{3}', Punctuation),
            ('[=<>|~&+\\-*/%#^]+|\\.\\.', Operator),
            ('[\\[\\]{}().,:;]+', Punctuation),
            ('(and|or|not)\\b', Operator.Word),
            (words([
                'break',
                'do',
                'else',
                'elseif',
                'end',
                'for',
                'if',
                'in',
                'repeat',
                'return',
                'then',
                'until',
                'while'], suffix = '\\b'), Keyword.Reserved),
            ('goto\\b', Keyword.Reserved, 'goto'),
            ('(local)\\b', Keyword.Declaration),
            ('(true|false|nil)\\b', Keyword.Constant),
            ('(function)\\b', Keyword.Reserved, 'funcname'),
            (words(all_lua_builtins(), suffix = '\\b'), Name.Builtin),
            (f'''[A-Za-z_]\\w*(?={_s}*[.:])''', Name.Variable, 'varname'),
            (f'''[A-Za-z_]\\w*(?={_s}*\\()''', Name.Function),
            ('[A-Za-z_]\\w*', Name.Variable),
            ("'", String.Single, combined('stringescape', 'sqs')),
            ('"', String.Double, combined('stringescape', 'dqs'))],
        'varname': [
            include('ws'),
            ('\\.\\.', Operator, '#pop'),
            ('[.:]', Punctuation),
            (f'''{_name}(?={_s}*[.:])''', Name.Property),
            (f'''{_name}(?={_s}*\\()''', Name.Function, '#pop'),
            (_name, Name.Property, '#pop')],
        'funcname': [
            include('ws'),
            ('[.:]', Punctuation),
            (f'''{_name}(?={_s}*[.:])''', Name.Class),
            (_name, Name.Function, '#pop'),
            ('\\(', Punctuation, '#pop')],
        'goto': [
            include('ws'),
            (_name, Name.Label, '#pop')],
        'label': [
            include('ws'),
            ('::', Punctuation, '#pop'),
            (_name, Name.Label)],
        'stringescape': [
            ('\\\\([abfnrtv\\\\"\\\']|[\\r\\n]{1,2}|z\\s*|x[0-9a-fA-F]{2}|\\d{1,3}|u\\{[0-9a-fA-F]+\\})', String.Escape)],
        'sqs': [
            ("'", String.Single, '#pop'),
            ("[^\\\\']+", String.Single)],
        'dqs': [
            ('"', String.Double, '#pop'),
            ('[^\\\\"]+', String.Double)] }
    
    def __init__(self, **options):
        self.func_name_highlighting = get_bool_opt(options, 'func_name_highlighting', True)
        self.disabled_modules = get_list_opt(options, 'disabled_modules', [])
        self._functions = set()
    # WARNING: Decompyle incomplete

    
    def get_tokens_unprocessed(self, text):
        pass
    # WARNING: Decompyle incomplete



def _luau_make_expression(should_pop, _s):
