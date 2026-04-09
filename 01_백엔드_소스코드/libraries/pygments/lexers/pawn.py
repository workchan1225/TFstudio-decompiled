# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pawn.pyc (Python 3.11)

'''
    pygments.lexers.pawn
    ~~~~~~~~~~~~~~~~~~~~

    Lexers for the Pawn languages.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.lexer import RegexLexer
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation
from pygments.util import get_bool_opt
__all__ = [
    'SourcePawnLexer',
    'PawnLexer']

class SourcePawnLexer(RegexLexer):
    '''
    For SourcePawn source code with preprocessor directives.
    '''
    name = 'SourcePawn'
    aliases = [
        'sp']
    filenames = [
        '*.sp']
    mimetypes = [
        'text/x-sourcepawn']
    url = 'https://github.com/alliedmodders/sourcepawn'
    version_added = '1.6'
    _ws = '(?:\\s|//.*?\\n|/\\*.*?\\*/)+'
    _ws1 = '\\s*(?:/[*].*?[*]/\\s*)*'
    tokens = {
        'root': [
            ('^#if\\s+0', Comment.Preproc, 'if0'),
            ('^#', Comment.Preproc, 'macro'),
            ('^' + _ws1 + '#if\\s+0', Comment.Preproc, 'if0'),
            ('^' + _ws1 + '#', Comment.Preproc, 'macro'),
            ('\\n', Text),
            ('\\s+', Text),
            ('\\\\\\n', Text),
            ('/(\\\\\\n)?/(\\n|(.|\\n)*?[^\\\\]\\n)', Comment.Single),
            ('/(\\\\\\n)?\\*(.|\\n)*?\\*(\\\\\\n)?/', Comment.Multiline),
            ('[{}]', Punctuation),
            ('L?"', String, 'string'),
            ("L?'(\\\\.|\\\\[0-7]{1,3}|\\\\x[a-fA-F0-9]{1,2}|[^\\\\\\'\\n])'", String.Char),
            ('(\\d+\\.\\d*|\\.\\d+|\\d+)[eE][+-]?\\d+[LlUu]*', Number.Float),
            ('(\\d+\\.\\d*|\\.\\d+|\\d+[fF])[fF]?', Number.Float),
            ('0x[0-9a-fA-F]+[LlUu]*', Number.Hex),
            ('0[0-7]+[LlUu]*', Number.Oct),
            ('\\d+[LlUu]*', Number.Integer),
            ('[~!%^&*+=|?:<>/-]', Operator),
            ('[()\\[\\],.;]', Punctuation),
            ('(case|const|continue|native|default|else|enum|for|if|new|operator|public|return|sizeof|static|decl|struct|switch)\\b', Keyword),
            ('(bool|Float)\\b', Keyword.Type),
            ('(true|false)\\b', Keyword.Constant),
            ('[a-zA-Z_]\\w*', Name)],
        'string': [
            ('"', String, '#pop'),
            ('\\\\([\\\\abfnrtv"\\\']|x[a-fA-F0-9]{2,4}|[0-7]{1,3})', String.Escape),
            ('[^\\\\"\\n]+', String),
            ('\\\\\\n', String),
            ('\\\\', String)],
        'macro': [
            ('[^/\\n]+', Comment.Preproc),
            ('/\\*(.|\\n)*?\\*/', Comment.Multiline),
            ('//.*?\\n', Comment.Single, '#pop'),
            ('/', Comment.Preproc),
            ('(?<=\\\\)\\n', Comment.Preproc),
            ('\\n', Comment.Preproc, '#pop')],
        'if0': [
            ('^\\s*#if.*?(?<!\\\\)\\n', Comment.Preproc, '#push'),
            ('^\\s*#endif.*?(?<!\\\\)\\n', Comment.Preproc, '#pop'),
            ('.*?\\n', Comment)] }
    SM_TYPES = {
        'any',
        'bool',
        'Float',
        'Timer',
        'APLRes',
        'Action',
        'Handle',
        'Plugin',
        'String',
        'TFCond',
        'TFTeam',
        'AdminId',
        'GroupId',
        'NetFlow',
        'RayType',
        'SDKType',
        'UserMsg',
        'DBResult',
        'ExecType',
        'FileType',
        'Function',
        'Identity',
        'MoveType',
        'PathType',
        'PropType',
        'RenderFx',
        'SMCError',
        'SortType',
        'AdminFlag',
        'EventHook',
        'MapChange',
        'MenuStyle',
        'ParamType',
        'SMCResult',
        'SortOrder',
        'CookieMenu',
        'DBBindType',
        'DBPriority',
        'DialogType',
        'MenuAction',
        'MenuSource',
        'PluginInfo',
        'RegexError',
        'RenderMode',
        'SDKLibrary',
        'SortFunc2D',
        'FeatureType',
        'KvDataTypes',
        'QueryCookie',
        'ReplySource',
        'SDKCallType',
        'TFClassType',
        'ConVarBounds',
        'CookieAccess',
        'FileTimeMode',
        'ImmunityType',
        'OverrideRule',
        'OverrideType',
        'PluginStatus',
        'AdmAccessMode',
        'EventHookMode',
        'FeatureStatus',
        'PropFieldType',
        'SDKPassMethod',
        'TopMenuAction',
        'TopMenuObject',
        'AdminCachePart',
        'ListenOverride',
        'NominateResult',
        'TFResourceType',
        'TopMenuPosition',
        'CookieMenuAction',
        'ConVarQueryResult',
        'SDKFuncConfSource',
        'TopMenuObjectType',
        'TraceEntityFilter',
        'ConVarQueryFinished'}
    
    def __init__(self, **options):
        self.smhighlighting = get_bool_opt(options, 'sourcemod', True)
        self._functions = set()
        if self.smhighlighting:
            FUNCTIONS = FUNCTIONS
            import pygments.lexers._sourcemod_builtins
            self._functions.update(FUNCTIONS)
    # WARNING: Decompyle incomplete

    
    def get_tokens_unprocessed(self, text):
        pass
    # WARNING: Decompyle incomplete



class PawnLexer(RegexLexer):
    '''
    For Pawn source code.
    '''
    name = 'Pawn'
    aliases = [
        'pawn']
    filenames = [
        '*.p',
        '*.pwn',
        '*.inc']
    mimetypes = [
        'text/x-pawn']
    url = 'https://www.compuphase.com/pawn/pawn.htm'
    version_added = '2.0'
    _ws = '(?:\\s|//.*?\\n|/[*][\\w\\W]*?[*]/)+'
    _ws1 = '\\s*(?:/[*].*?[*]/\\s*)*'
    tokens = {
        'root': [
            ('^#if\\s+0', Comment.Preproc, 'if0'),
            ('^#', Comment.Preproc, 'macro'),
            ('^' + _ws1 + '#if\\s+0', Comment.Preproc, 'if0'),
            ('^' + _ws1 + '#', Comment.Preproc, 'macro'),
            ('\\n', Text),
            ('\\s+', Text),
            ('\\\\\\n', Text),
            ('/(\\\\\\n)?/(\\n|(.|\\n)*?[^\\\\]\\n)', Comment.Single),
            ('/(\\\\\\n)?\\*[\\w\\W]*?\\*(\\\\\\n)?/', Comment.Multiline),
            ('[{}]', Punctuation),
            ('L?"', String, 'string'),
            ("L?'(\\\\.|\\\\[0-7]{1,3}|\\\\x[a-fA-F0-9]{1,2}|[^\\\\\\'\\n])'", String.Char),
            ('(\\d+\\.\\d*|\\.\\d+|\\d+)[eE][+-]?\\d+[LlUu]*', Number.Float),
            ('(\\d+\\.\\d*|\\.\\d+|\\d+[fF])[fF]?', Number.Float),
            ('0x[0-9a-fA-F]+[LlUu]*', Number.Hex),
            ('0[0-7]+[LlUu]*', Number.Oct),
            ('\\d+[LlUu]*', Number.Integer),
            ('[~!%^&*+=|?:<>/-]', Operator),
            ('[()\\[\\],.;]', Punctuation),
            ('(switch|case|default|const|new|static|char|continue|break|if|else|for|while|do|operator|enum|public|return|sizeof|tagof|state|goto)\\b', Keyword),
            ('(bool|Float)\\b', Keyword.Type),
            ('(true|false)\\b', Keyword.Constant),
            ('[a-zA-Z_]\\w*', Name)],
        'string': [
            ('"', String, '#pop'),
            ('\\\\([\\\\abfnrtv"\\\']|x[a-fA-F0-9]{2,4}|[0-7]{1,3})', String.Escape),
            ('[^\\\\"\\n]+', String),
            ('\\\\\\n', String),
            ('\\\\', String)],
        'macro': [
            ('[^/\\n]+', Comment.Preproc),
            ('/\\*(.|\\n)*?\\*/', Comment.Multiline),
            ('//.*?\\n', Comment.Single, '#pop'),
            ('/', Comment.Preproc),
            ('(?<=\\\\)\\n', Comment.Preproc),
            ('\\n', Comment.Preproc, '#pop')],
        'if0': [
            ('^\\s*#if.*?(?<!\\\\)\\n', Comment.Preproc, '#push'),
            ('^\\s*#endif.*?(?<!\\\\)\\n', Comment.Preproc, '#pop'),
            ('.*?\\n', Comment)] }
    
    def analyse_text(text):
        """This is basically C. There is a keyword which doesn't exist in C
        though and is nearly unique to this language."""
        if 'tagof' in text:
            return 0.01
