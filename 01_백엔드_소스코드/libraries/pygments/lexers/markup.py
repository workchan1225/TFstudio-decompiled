# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: markup.pyc (Python 3.11)

'''
    pygments.lexers.markup
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexers for non-HTML markup languages.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexers.html import XmlLexer
from pygments.lexers.javascript import JavascriptLexer
from pygments.lexers.css import CssLexer
from pygments.lexers.lilypond import LilyPondLexer
from pygments.lexers.data import JsonLexer
from pygments.lexer import RegexLexer, DelegatingLexer, include, bygroups, using, this, do_insertions, default, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Generic, Other, Whitespace, Literal
from pygments.util import get_bool_opt, ClassNotFound
__all__ = [
    'BBCodeLexer',
    'MoinWikiLexer',
    'RstLexer',
    'TexLexer',
    'GroffLexer',
    'MozPreprocHashLexer',
    'MozPreprocPercentLexer',
    'MozPreprocXulLexer',
    'MozPreprocJavascriptLexer',
    'MozPreprocCssLexer',
    'MarkdownLexer',
    'OrgLexer',
    'TiddlyWiki5Lexer',
    'WikitextLexer']

class BBCodeLexer(RegexLexer):
    '''
    A lexer that highlights BBCode(-like) syntax.
    '''
    name = 'BBCode'
    aliases = [
        'bbcode']
    mimetypes = [
        'text/x-bbcode']
    url = 'https://www.bbcode.org/'
    version_added = '0.6'
    tokens = {
        'root': [
            ('[^[]+', Text),
            ('\\[/?\\w+', Keyword, 'tag'),
            ('\\[', Text)],
        'tag': [
            ('\\s+', Text),
            ('(\\w+)(=)("?[^\\s"\\]]+"?)', bygroups(Name.Attribute, Operator, String)),
            ('(=)("?[^\\s"\\]]+"?)', bygroups(Operator, String)),
            ('\\]', Keyword, '#pop')] }


class MoinWikiLexer(RegexLexer):
    '''
    For MoinMoin (and Trac) Wiki markup.
    '''
    name = 'MoinMoin/Trac Wiki markup'
    aliases = [
        'trac-wiki',
        'moin']
    filenames = []
    mimetypes = [
        'text/x-trac-wiki']
    url = 'https://moinmo.in'
    version_added = '0.7'
    flags = re.MULTILINE | re.IGNORECASE
    tokens = {
        'root': [
            ('^#.*$', Comment),
            ('(!)(\\S+)', bygroups(Keyword, Text)),
            ('^(=+)([^=]+)(=+)(\\s*#.+)?$', bygroups(Generic.Heading, using(this), Generic.Heading, String)),
            ('(\\{\\{\\{)(\\n#!.+)?', bygroups(Name.Builtin, Name.Namespace), 'codeblock'),
            ("(\\'\\'\\'?|\\|\\||`|__|~~|\\^|,,|::)", Comment),
            ('^( +)([.*-])( )', bygroups(Text, Name.Builtin, Text)),
            ('^( +)([a-z]{1,5}\\.)( )', bygroups(Text, Name.Builtin, Text)),
            ('\\[\\[\\w+.*?\\]\\]', Keyword),
            ('(\\[[^\\s\\]]+)(\\s+[^\\]]+?)?(\\])', bygroups(Keyword, String, Keyword)),
            ('^----+$', Keyword),
            ("[^\\n\\'\\[{!_~^,|]+", Text),
            ('\\n', Text),
            ('.', Text)],
        'codeblock': [
            ('\\}\\}\\}', Name.Builtin, '#pop'),
            ('\\{\\{\\{', Text, '#push'),
            ('[^{}]+', Comment.Preproc),
            ('.', Comment.Preproc)] }


class RstLexer(RegexLexer):
    '''
    For reStructuredText markup.

    Additional options accepted:

    `handlecodeblocks`
        Highlight the contents of ``.. sourcecode:: language``,
        ``.. code:: language`` and ``.. code-block:: language``
        directives with a lexer for the given language (default:
        ``True``).

        .. versionadded:: 0.8
    '''
    name = 'reStructuredText'
    url = 'https://docutils.sourceforge.io/rst.html'
    aliases = [
        'restructuredtext',
        'rst',
        'rest']
    filenames = [
        '*.rst',
        '*.rest']
    mimetypes = [
        'text/x-rst',
        'text/prs.fallenstein.rst']
    version_added = '0.7'
    flags = re.MULTILINE
    
    def _handle_sourcecode(self, match):
        pass
    # WARNING: Decompyle incomplete

    closers = '\'")]}>’”»!?'
    unicode_delimiters = '‐‑‒–— '
    end_string_suffix = f'''((?=$)|(?=[-/:.,; \\n\\x00{re.escape(unicode_delimiters)}{re.escape(closers)}]))'''
    tokens = {
        'root': [
            ('^(=+|-+|`+|:+|\\.+|\\\'+|"+|~+|\\^+|_+|\\*+|\\++|#+)([ \\t]*\\n)(.+)(\\n)(\\1)(\\n)', bygroups(Generic.Heading, Text, Generic.Heading, Text, Generic.Heading, Text)),
            ('^(\\S.*)(\\n)(={3,}|-{3,}|`{3,}|:{3,}|\\.{3,}|\\\'{3,}|"{3,}|~{3,}|\\^{3,}|_{3,}|\\*{3,}|\\+{3,}|#{3,})(\\n)', bygroups(Generic.Heading, Text, Generic.Heading, Text)),
            ('^(\\s*)([-*+])( .+\\n(?:\\1  .+\\n)*)', bygroups(Text, Number, using(this, state = 'inline'))),
            ('^(\\s*)([0-9#ivxlcmIVXLCM]+\\.)( .+\\n(?:\\1  .+\\n)*)', bygroups(Text, Number, using(this, state = 'inline'))),
            ('^(\\s*)(\\(?[0-9#ivxlcmIVXLCM]+\\))( .+\\n(?:\\1  .+\\n)*)', bygroups(Text, Number, using(this, state = 'inline'))),
            ('^(\\s*)([A-Z]+\\.)( .+\\n(?:\\1  .+\\n)+)', bygroups(Text, Number, using(this, state = 'inline'))),
            ('^(\\s*)(\\(?[A-Za-z]+\\))( .+\\n(?:\\1  .+\\n)+)', bygroups(Text, Number, using(this, state = 'inline'))),
            ('^(\\s*)(\\|)( .+\\n(?:\\|  .+\\n)*)', bygroups(Text, Operator, using(this, state = 'inline'))),
            ('^( *\\.\\.)(\\s*)((?:source)?code(?:-block)?)(::)([ \\t]*)([^\\n]+)(\\n[ \\t]*\\n)([ \\t]+)(.*)(\\n)((?:(?:\\8.*)?\\n)+)', _handle_sourcecode),
            ('^( *\\.\\.)(\\s*)([\\w:-]+?)(::)(?:([ \\t]*)(.*))', bygroups(Punctuation, Text, Operator.Word, Punctuation, Text, using(this, state = 'inline'))),
            ('^( *\\.\\.)(\\s*)(_(?:[^:\\\\]|\\\\.)+:)(.*?)$', bygroups(Punctuation, Text, Name.Tag, using(this, state = 'inline'))),
            ('^( *\\.\\.)(\\s*)(\\[.+\\])(.*?)$', bygroups(Punctuation, Text, Name.Tag, using(this, state = 'inline'))),
            ('^( *\\.\\.)(\\s*)(\\|.+\\|)(\\s*)([\\w:-]+?)(::)(?:([ \\t]*)(.*))', bygroups(Punctuation, Text, Name.Tag, Text, Operator.Word, Punctuation, Text, using(this, state = 'inline'))),
            ('^ *\\.\\..*(\\n( +.*\\n|\\n)+)?', Comment),
            ('^( *)(:(?:\\\\\\\\|\\\\:|[^:\\n])+:(?=\\s))([ \\t]*)', bygroups(Text, Name.Class, Text)),
            ('^(\\S.*(?<!::)\\n)((?:(?: +.*)\\n)+)', bygroups(using(this, state = 'inline'), using(this, state = 'inline'))),
            ('(::)(\\n[ \\t]*\\n)([ \\t]+)(.*)(\\n)((?:(?:\\3.*)?\\n)+)', bygroups(String.Escape, Text, String, String, Text, String)),
            include('inline')],
        'inline': [
            ('\\\\.', Text),
            ('``', String, 'literal'),
            ('(`.+?)(<.+?>)(`__?)', bygroups(String, String.Interpol, String)),
            ('`.+?`__?', String),
            ('(`.+?`)(:[a-zA-Z0-9:-]+?:)?', bygroups(Name.Variable, Name.Attribute)),
            ('(:[a-zA-Z0-9:-]+?:)(`.+?`)', bygroups(Name.Attribute, Name.Variable)),
            ('\\*\\*.+?\\*\\*', Generic.Strong),
            ('\\*.+?\\*', Generic.Emph),
            ('\\[.*?\\]_', String),
            ('<.+?>', Name.Tag),
            ('[^\\\\\\n\\[*`:]+', Text),
            ('.', Text)],
        'literal': [
            ('[^`]+', String),
            ('``' + end_string_suffix, String, '#pop'),
            ('`', String)] }
    
    def __init__(self, **options):
        self.handlecodeblocks = get_bool_opt(options, 'handlecodeblocks', True)
    # WARNING: Decompyle incomplete

    
    def analyse_text(text):
        if text[:2] == '..' and text[2:3] != '.':
            return 0.3
        p1 = None.find('\n')
        p2 = text.find('\n', p1 + 1)
        if p2 > -1 or p1 * 2 + 1 == p2 or text[p1 + 1] in '-=' or text[p1 + 1] == text[p2 - 1]:
            return 0.5
        return None
        return None
        return None



class TexLexer(RegexLexer):
    '''
    Lexer for the TeX and LaTeX typesetting languages.
    '''
    name = 'TeX'
    aliases = [
        'tex',
        'latex']
    filenames = [
        '*.tex',
        '*.aux',
        '*.toc']
    mimetypes = [
        'text/x-tex',
        'text/x-latex']
    url = 'https://tug.org'
    version_added = ''
    tokens = {
        'general': [
            ('%.*?\\n', Comment),
            ('[{}]', Name.Builtin),
            ('[&_^]', Name.Builtin)],
        'root': [
            ('\\\\\\[', String.Backtick, 'displaymath'),
            ('\\\\\\(', String, 'inlinemath'),
            ('\\$\\$', String.Backtick, 'displaymath'),
            ('\\$', String, 'inlinemath'),
            ('\\\\([a-zA-Z@_:]+|\\S?)', Keyword, 'command'),
            ('\\\\$', Keyword),
            include('general'),
            ('[^\\\\$%&_^{}]+', Text)],
        'math': [
            ('\\\\([a-zA-Z]+|\\S?)', Name.Variable),
            include('general'),
            ('[0-9]+', Number),
            ('[-=!+*/()\\[\\]]', Operator),
            ('[^=!+*/()\\[\\]\\\\$%&_^{}0-9-]+', Name.Builtin)],
        'inlinemath': [
            ('\\\\\\)', String, '#pop'),
            ('\\$', String, '#pop'),
            include('math')],
        'displaymath': [
            ('\\\\\\]', String, '#pop'),
            ('\\$\\$', String, '#pop'),
            ('\\$', Name.Builtin),
            include('math')],
        'command': [
            ('\\[.*?\\]', Name.Attribute),
            ('\\*', Keyword),
            default('#pop')] }
    
    def analyse_text(text):
        for start in ('\\documentclass', '\\input', '\\documentstyle', '\\relax'):
            if text[:len(start)] == start:
                return True
            return None



class GroffLexer(RegexLexer):
    '''
    Lexer for the (g)roff typesetting language, supporting groff
    extensions. Mainly useful for highlighting manpage sources.
    '''
    name = 'Groff'
    aliases = [
        'groff',
        'nroff',
        'man']
    filenames = [
        '*.[1-9]',
        '*.man',
        '*.1p',
        '*.3pm']
    mimetypes = [
        'application/x-troff',
        'text/troff']
    url = 'https://www.gnu.org/software/groff'
    version_added = '0.6'
    tokens = {
        'root': [
            ('(\\.)(\\w+)', bygroups(Text, Keyword), 'request'),
            ('\\.', Punctuation, 'request'),
            ('[^\\\\\\n]+', Text, 'textline'),
            default('textline')],
        'textline': [
            include('escapes'),
            ('[^\\\\\\n]+', Text),
            ('\\n', Text, '#pop')],
        'escapes': [
            ('\\\\"[^\\n]*', Comment),
            ('\\\\[fn]\\w', String.Escape),
            ('\\\\\\(.{2}', String.Escape),
            ('\\\\.\\[.*\\]', String.Escape),
            ('\\\\.', String.Escape),
            ('\\\\\\n', Text, 'request')],
        'request': [
            ('\\n', Text, '#pop'),
            include('escapes'),
            ('"[^\\n"]+"', String.Double),
            ('\\d+', Number),
            ('\\S+', String),
            ('\\s+', Text)] }
    
    def analyse_text(text):
        if text[:1] != '.':
            return False
        if None[:3] == '.\\"':
            return True
        if None[:4] == '.TH ':
            return True
        if None[1:3].isalnum() or text[3].isspace():
            return 0.9
        return None



class MozPreprocHashLexer(RegexLexer):
    """
    Lexer for Mozilla Preprocessor files (with '#' as the marker).

    Other data is left untouched.
    """
    name = 'mozhashpreproc'
    aliases = [
        name]
    filenames = []
    mimetypes = []
    url = 'https://firefox-source-docs.mozilla.org/build/buildsystem/preprocessor.html'
    version_added = '2.0'
    tokens = {
        'root': [
            ('^#', Comment.Preproc, ('expr', 'exprstart')),
            ('.+', Other)],
        'exprstart': [
            ('(literal)(.*)', bygroups(Comment.Preproc, Text), '#pop:2'),
            (words(('define', 'undef', 'if', 'ifdef', 'ifndef', 'else', 'elif', 'elifdef', 'elifndef', 'endif', 'expand', 'filter', 'unfilter', 'include', 'includesubst', 'error')), Comment.Preproc, '#pop')],
        'expr': [
            (words(('!', '!=', '==', '&&', '||')), Operator),
            ('(defined)(\\()', bygroups(Keyword, Punctuation)),
            ('\\)', Punctuation),
            ('[0-9]+', Number.Decimal),
            ('__\\w+?__', Name.Variable),
            ('@\\w+?@', Name.Class),
            ('\\w+', Name),
            ('\\n', Text, '#pop'),
            ('\\s+', Text),
            ('\\S', Punctuation)] }


class MozPreprocPercentLexer(MozPreprocHashLexer):
    """
    Lexer for Mozilla Preprocessor files (with '%' as the marker).

    Other data is left untouched.
    """
    name = 'mozpercentpreproc'
    aliases = [
        name]
    filenames = []
    mimetypes = []
    url = 'https://firefox-source-docs.mozilla.org/build/buildsystem/preprocessor.html'
    version_added = '2.0'
    tokens = {
        'root': [
            ('^%', Comment.Preproc, ('expr', 'exprstart')),
            ('.+', Other)] }


class MozPreprocXulLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class MozPreprocJavascriptLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class MozPreprocCssLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class MarkdownLexer(RegexLexer):
    '''
    For Markdown markup.
    '''
    name = 'Markdown'
    url = 'https://daringfireball.net/projects/markdown/'
    aliases = [
        'markdown',
        'md']
    filenames = [
        '*.md',
        '*.markdown']
    mimetypes = [
        'text/x-markdown']
    version_added = '2.2'
    flags = re.MULTILINE
    
    def _handle_codeblock(self, match):
        pass
    # WARNING: Decompyle incomplete

    tokens = {
        'root': [
            ('(^#[^#].+)(\\n)', bygroups(Generic.Heading, Text)),
            ('(^#{2,6}[^#].+)(\\n)', bygroups(Generic.Subheading, Text)),
            ('^(.+)(\\n)(=+)(\\n)', bygroups(Generic.Heading, Text, Generic.Heading, Text)),
            ('^(.+)(\\n)(-+)(\\n)', bygroups(Generic.Subheading, Text, Generic.Subheading, Text)),
            ('^(\\s*)([*-] )(\\[[ xX]\\])( .+\\n)', bygroups(Whitespace, Keyword, Keyword, using(this, state = 'inline'))),
            ('^(\\s*)([*-])(\\s)(.+\\n)', bygroups(Whitespace, Keyword, Whitespace, using(this, state = 'inline'))),
            ('^(\\s*)([0-9]+\\.)( .+\\n)', bygroups(Whitespace, Keyword, using(this, state = 'inline'))),
            ('^(\\s*>\\s)(.+\\n)', bygroups(Keyword, Generic.Emph)),
            ('^(\\s*```\\n[\\w\\W]*?^\\s*```$\\n)', String.Backtick),
            ('(?x)\n              ^(?P<initial>\\s*```)\n              (?P<lang>[\\w\\-]+)\n              (?P<afterlang>\n                 (?P<whitespace>[^\\S\\n]+)\n                 (?P<extra>.*))?\n              (?P<newline>\\n)\n              (?P<code>(.|\\n)*?)\n              (?P<terminator>^\\s*```$\\n)\n              ', _handle_codeblock),
            include('inline')],
        'inline': [
            ('\\\\.', Text),
            ('([^`]?)(`[^`\\n]+`)', bygroups(Text, String.Backtick)),
            ('([^\\*]?)(\\*\\*[^* \\n][^*\\n]*\\*\\*)', bygroups(Text, Generic.Strong)),
            ('([^_]?)(__[^_ \\n][^_\\n]*__)', bygroups(Text, Generic.Strong)),
            ('([^\\*]?)(\\*[^* \\n][^*\\n]*\\*)', bygroups(Text, Generic.Emph)),
            ('([^_]?)(_[^_ \\n][^_\\n]*_)', bygroups(Text, Generic.Emph)),
            ('([^~]?)(~~[^~ \\n][^~\\n]*~~)', bygroups(Text, Generic.Deleted)),
            ('[@#][\\w/:]+', Name.Entity),
            ('(!?\\[)([^]]+)(\\])(\\()([^)]+)(\\))', bygroups(Text, Name.Tag, Text, Text, Name.Attribute, Text)),
            ('(\\[)([^]]+)(\\])(\\[)([^]]*)(\\])', bygroups(Text, Name.Tag, Text, Text, Name.Label, Text)),
            ('^(\\s*\\[)([^]]*)(\\]:\\s*)(.+)', bygroups(Text, Name.Label, Text, Name.Attribute)),
            ('[^\\\\\\s]+', Text),
            ('.', Text)] }
    
    def __init__(self, **options):
        self.handlecodeblocks = get_bool_opt(options, 'handlecodeblocks', True)
    # WARNING: Decompyle incomplete



class OrgLexer(RegexLexer):
    '''
    For Org Mode markup.
    '''
    name = 'Org Mode'
    url = 'https://orgmode.org'
    aliases = [
        'org',
        'orgmode',
        'org-mode']
    filenames = [
        '*.org']
    mimetypes = [
        'text/org']
    version_added = '2.18'
    
    def _inline(start, end):
        return f'''(?<!\\w){start}(.|\\n(?!\\n))+?{end}(?!\\w)'''

    tokens = {
        [][('^# .*', Comment.Single)][('^(\\* )(COMMENT)( .*)', bygroups(Generic.Heading, Comment.Preproc, Generic.Heading))][('^(\\*\\*+ )(COMMENT)( .*)', bygroups(Generic.Subheading, Comment.Preproc, Generic.Subheading))][('^(\\* )(DONE)( .*)', bygroups(Generic.Heading, Generic.Deleted, Generic.Heading))][('^(\\*\\*+ )(DONE)( .*)', bygroups(Generic.Subheading, Generic.Deleted, Generic.Subheading))][('^(\\* )(TODO)( .*)', bygroups(Generic.Heading, Generic.Error, Generic.Heading))][('^(\\*\\*+ )(TODO)( .*)', bygroups(Generic.Subheading, Generic.Error, Generic.Subheading))][('^(\\* .+?)( :[a-zA-Z0-9_@:]+:)?$', bygroups(Generic.Heading, Generic.Emph))][('^(\\*\\*+ .+?)( :[a-zA-Z0-9_@:]+:)?$', bygroups(Generic.Subheading, Generic.Emph))][('^(?:( *)([+-] )|( +)(\\* ))(\\[[ X-]\\])?(.+ ::)?', bygroups(Whitespace, Keyword, Whitespace, Keyword, Generic.Prompt, Name.Label))][('^( *)([0-9]+[.)])( \\[@[0-9]+\\])?', bygroups(Whitespace, Keyword, Generic.Emph))][('(?i)^( *#\\+begin: *)((?:.|\\n)*?)(^ *#\\+end: *$)', bygroups(Operator.Word, using(this), Operator.Word))][('(?i)^( *#\\+begin_comment *\\n)((?:.|\\n)*?)(^ *#\\+end_comment *$)', bygroups(Operator.Word, Comment.Multiline, Operator.Word))][('(?i)^( *#\\+begin_src .*)((?:.|\\n)*?)(^ *#\\+end_src *$)', bygroups(Operator.Word, Text, Operator.Word))][('(?i)^( *#\\+begin_\\w+)( *\\n)((?:.|\\n)*?)(^ *#\\+end_\\w+)( *$)', bygroups(Operator.Word, Whitespace, Text, Operator.Word, Whitespace))][('^(#\\+\\w+:)(.*)$', bygroups(Name.Namespace, Text))][('(?i)^( *:\\w+: *\\n)((?:.|\\n)*?)(^ *:end: *$)', bygroups(Name.Decorator, Comment.Special, Name.Decorator))][('\\\\\\\\$', Operator)][('(?i)^( *(?:DEADLINE|SCHEDULED): )(<.+?> *)$', bygroups(Generic.Error, Literal.Date))][('(?i)^( *CLOSED: )(\\[.+?\\] *)$', bygroups(Generic.Deleted, Literal.Date))][(_inline('\\*', '\\*+'), Generic.Strong)][(_inline('/', '/'), Generic.Emph)][(_inline('=', '='), String)][(_inline('~', '~'), String)][(_inline('\\+', '\\+'), Generic.Deleted)][(_inline('_', '_+'), Generic.EmphStrong)][('<.+?>', Literal.Date)][('\\{\\{\\{.+?\\}\\}\\}', Comment.Preproc)][('(?<!\\[)\\[fn:.+?\\]', Name.Tag)][('(?s)(\\[\\[)(.*?)(\\]\\[)(.*?)(\\]\\])', bygroups(Punctuation, Name.Attribute, Punctuation, Name.Tag, Punctuation))][('(?s)(\\[\\[)(.+?)(\\]\\])', bygroups(Punctuation, Name.Attribute, Punctuation))][('(<<)(.+?)(>>)', bygroups(Punctuation, Name.Attribute, Punctuation))][('^( *)(\\|[ -].*?[ -]\\|)$', bygroups(Whitespace, String))][('[^#*+\\-0-9:\\\\/=~_<{\\[|\\n]+', Text)]: [][('^# .*', Comment.Single)][('^(\\* )(COMMENT)( .*)', bygroups(Generic.Heading, Comment.Preproc, Generic.Heading))][('^(\\*\\*+ )(COMMENT)( .*)', bygroups(Generic.Subheading, Comment.Preproc, Generic.Subheading))][('^(\\* )(DONE)( .*)', bygroups(Generic.Heading, Generic.Deleted, Generic.Heading))][('^(\\*\\*+ )(DONE)( .*)', bygroups(Generic.Subheading, Generic.Deleted, Generic.Subheading))][('^(\\* )(TODO)( .*)', bygroups(Generic.Heading, Generic.Error, Generic.Heading))][('^(\\*\\*+ )(TODO)( .*)', bygroups(Generic.Subheading, Generic.Error, Generic.Subheading))][('^(\\* .+?)( :[a-zA-Z0-9_@:]+:)?$', bygroups(Generic.Heading, Generic.Emph))][('^(\\*\\*+ .+?)( :[a-zA-Z0-9_@:]+:)?$', bygroups(Generic.Subheading, Generic.Emph))][('^(?:( *)([+-] )|( +)(\\* ))(\\[[ X-]\\])?(.+ ::)?', bygroups(Whitespace, Keyword, Whitespace, Keyword, Generic.Prompt, Name.Label))][('^( *)([0-9]+[.)])( \\[@[0-9]+\\])?', bygroups(Whitespace, Keyword, Generic.Emph))][('(?i)^( *#\\+begin: *)((?:.|\\n)*?)(^ *#\\+end: *$)', bygroups(Operator.Word, using(this), Operator.Word))][('(?i)^( *#\\+begin_comment *\\n)((?:.|\\n)*?)(^ *#\\+end_comment *$)', bygroups(Operator.Word, Comment.Multiline, Operator.Word))][('(?i)^( *#\\+begin_src .*)((?:.|\\n)*?)(^ *#\\+end_src *$)', bygroups(Operator.Word, Text, Operator.Word))][('(?i)^( *#\\+begin_\\w+)( *\\n)((?:.|\\n)*?)(^ *#\\+end_\\w+)( *$)', bygroups(Operator.Word, Whitespace, Text, Operator.Word, Whitespace))][('^(#\\+\\w+:)(.*)$', bygroups(Name.Namespace, Text))][('(?i)^( *:\\w+: *\\n)((?:.|\\n)*?)(^ *:end: *$)', bygroups(Name.Decorator, Comment.Special, Name.Decorator))][('\\\\\\\\$', Operator)][('(?i)^( *(?:DEADLINE|SCHEDULED): )(<.+?> *)$', bygroups(Generic.Error, Literal.Date))][('(?i)^( *CLOSED: )(\\[.+?\\] *)$', bygroups(Generic.Deleted, Literal.Date))][(_inline('\\*', '\\*+'), Generic.Strong)][(_inline('/', '/'), Generic.Emph)][(_inline('=', '='), String)][(_inline('~', '~'), String)][(_inline('\\+', '\\+'), Generic.Deleted)][(_inline('_', '_+'), Generic.EmphStrong)][('<.+?>', Literal.Date)][('\\{\\{\\{.+?\\}\\}\\}', Comment.Preproc)][('(?<!\\[)\\[fn:.+?\\]', Name.Tag)][('(?s)(\\[\\[)(.*?)(\\]\\[)(.*?)(\\]\\])', bygroups(Punctuation, Name.Attribute, Punctuation, Name.Tag, Punctuation))][('(?s)(\\[\\[)(.+?)(\\]\\])', bygroups(Punctuation, Name.Attribute, Punctuation))][('(<<)(.+?)(>>)', bygroups(Punctuation, Name.Attribute, Punctuation))][('^( *)(\\|[ -].*?[ -]\\|)$', bygroups(Whitespace, String))][('[^#*+\\-0-9:\\\\/=~_<{\\[|\\n]+', Text)][('[#*+\\-0-9:\\\\/=~_<{\\[|\\n]', Text)] }


class TiddlyWiki5Lexer(RegexLexer):
    '''
    For TiddlyWiki5 markup.
    '''
    name = 'tiddler'
    url = 'https://tiddlywiki.com/#TiddlerFiles'
    aliases = [
        'tid']
    filenames = [
        '*.tid']
    mimetypes = [
        'text/vnd.tiddlywiki']
    version_added = '2.7'
    flags = re.MULTILINE
    
    def _handle_codeblock(self, match):
        '''
        match args: 1:backticks, 2:lang_name, 3:newline, 4:code, 5:backticks
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _handle_cssblock(self, match):
        '''
        match args: 1:style tag 2:newline, 3:code, 4:closing style tag
        '''
        pass
    # WARNING: Decompyle incomplete

    tokens = {
        'root': [
            ('^(title)(:\\s)(.+\\n)', bygroups(Keyword, Text, Generic.Heading)),
            ('^(!)([^!].+\\n)', bygroups(Generic.Heading, Text)),
            ('^(!{2,6})(.+\\n)', bygroups(Generic.Subheading, Text)),
            ('^(\\s*)([*#>]+)(\\s*)(.+\\n)', bygroups(Text, Keyword, Text, using(this, state = 'inline'))),
            ('^(<<<.*\\n)([\\w\\W]*?)(^<<<.*$)', bygroups(String, Text, String)),
            ('^(\\|.*?\\|h)$', bygroups(Generic.Strong)),
            ('^(\\|.*?\\|[cf])$', bygroups(Generic.Emph)),
            ('^(\\|.*?\\|k)$', bygroups(Name.Tag)),
            ('^(;.*)$', bygroups(Generic.Strong)),
            ('^(```\\n)([\\w\\W]*?)(^```$)', bygroups(String, Text, String)),
            ('^(```)(\\w+)(\\n)([\\w\\W]*?)(^```$)', _handle_codeblock),
            ('^(<style>)(\\n)([\\w\\W]*?)(^</style>$)', _handle_cssblock),
            include('keywords'),
            include('inline')],
        'keywords': [
            (words(('\\define', '\\end', 'caption', 'created', 'modified', 'tags', 'title', 'type'), prefix = '^', suffix = '\\b'), Keyword)],
        'inline': [
            ('\\\\.', Text),
            ('\\d{17}', Number.Integer),
            ('(\\s)(//[^/]+//)((?=\\W|\\n))', bygroups(Text, Generic.Emph, Text)),
            ('(\\s)(\\^\\^[^\\^]+\\^\\^)', bygroups(Text, Generic.Emph)),
            ('(\\s)(,,[^,]+,,)', bygroups(Text, Generic.Emph)),
            ('(\\s)(__[^_]+__)', bygroups(Text, Generic.Strong)),
            ("(\\s)(''[^']+'')((?=\\W|\\n))", bygroups(Text, Generic.Strong, Text)),
            ('(\\s)(~~[^~]+~~)((?=\\W|\\n))', bygroups(Text, Generic.Deleted, Text)),
            ('<<[^>]+>>', Name.Tag),
            ('\\$\\$[^$]+\\$\\$', Name.Tag),
            ('\\$\\([^)]+\\)\\$', Name.Tag),
            ('^@@.*$', Name.Tag),
            ('</?[^>]+>', Name.Tag),
            ('`[^`]+`', String.Backtick),
            ('&\\S*?;', String.Regex),
            ('(\\[{2})([^]\\|]+)(\\]{2})', bygroups(Text, Name.Tag, Text)),
            ('(\\[{2})([^]\\|]+)(\\|)([^]\\|]+)(\\]{2})', bygroups(Text, Name.Tag, Text, Name.Attribute, Text)),
            ('(\\{{2})([^}]+)(\\}{2})', bygroups(Text, Name.Tag, Text)),
            ('(\\b.?.?tps?://[^\\s"]+)', bygroups(Name.Attribute)),
            ('[\\w]+', Text),
            ('.', Text)] }
    
    def __init__(self, **options):
        self.handlecodeblocks = get_bool_opt(options, 'handlecodeblocks', True)
    # WARNING: Decompyle incomplete



class WikitextLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'WikitextLexer'
    __doc__ = '\n    For MediaWiki Wikitext.\n\n    Parsing Wikitext is tricky, and results vary between different MediaWiki\n    installations, so we only highlight common syntaxes (built-in or from\n    popular extensions), and also assume templates produce no unbalanced\n    syntaxes.\n    '
    name = 'Wikitext'
    url = 'https://www.mediawiki.org/wiki/Wikitext'
    aliases = [
        'wikitext',
        'mediawiki']
    filenames = []
    mimetypes = [
        'text/x-wiki']
    version_added = '2.15'
    flags = re.MULTILINE
    
    def nowiki_tag_rules(tag_name):
        return [
            (f'''(?i)(</)({tag_name})(\\s*)(>)''', bygroups(Punctuation, Name.Tag, Whitespace, Punctuation), '#pop'),
            include('entity'),
            include('text')]

    
    def plaintext_tag_rules(tag_name):
        return [
            (f'''(?si)(.*?)(</)({tag_name})(\\s*)(>)''', bygroups(Text, Punctuation, Name.Tag, Whitespace, Punctuation), '#pop')]

    
    def delegate_tag_rules(tag_name, lexer, **lexer_kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def text_rules(token):
        return [
            ('\\w+', token),
            ('[^\\S\\n]+', token),
            ('(?s).', token)]

    
    def handle_syntaxhighlight(self, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def handle_score(self, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    title_char = ' %!"$&\\\'()*,\\-./0-9:;=?@A-Z\\\\\\^_`~+\\u0080-\\uFFFF'
    nbsp_char = '(?:\\t|&nbsp;|&\\#0*160;|&\\#[Xx]0*[Aa]0;|[ \\xA0\\u1680\\u2000-\\u200A\\u202F\\u205F\\u3000])'
    link_address = '(?:[0-9.]+|\\[[0-9a-f:.]+\\]|[^\\x00-\\x20"<>\\[\\]\\x7F\\xA0\\u1680\\u2000-\\u200A\\u202F\\u205F\\u3000\\uFFFD])'
    link_char_class = '[^\\x00-\\x20"<>\\[\\]\\x7F\\xA0\\u1680\\u2000-\\u200A\\u202F\\u205F\\u3000\\uFFFD]'
    double_slashes_i = {
        '__TOC__',
        '__NOCC__',
        '__NOTC__',
        '__NOTOC__',
        '__FORCETOC__',
        '__NOGALLERY__',
        '__NOEDITSECTION__',
        '__NOTITLECONVERT__',
        '__NOCONTENTCONVERT__'}
    double_slashes = {
        '__INDEX__',
        '__NOINDEX__',
        '__DISAMBIG__',
        '__NOGLOBAL__',
        '__HIDDENCAT__',
        '__NEWSECTIONLINK__',
        '__STATICREDIRECT__',
        '__NONEWSECTIONLINK__',
        '__EXPECTUNUSEDCATEGORY__',
        '__EXPECTED_UNCONNECTED_PAGE__'}
    protocols = {
        'geo:',
        'sip:',
        'sms:',
        'tel:',
        'urn:',
        'news:',
        'sips:',
        'xmpp:',
        'ftp://',
        'git://',
        'irc://',
        'mms://',
        'ssh://',
        'svn://',
        'ftps://',
        'http://',
        'ircs://',
        'magnet:',
        'mailto:',
        'nntp://',
        'sftp://',
        'bitcoin:',
        'https://',
        'redis://',
        'gopher://',
        'telnet://',
        'worldwind://',
        '//'}
    non_relative_protocols = protocols - {
        '//'}
    html_tags = {
        'b',
        'i',
        'p',
        'q',
        's',
        'u',
        'br',
        'dd',
        'dl',
        'dt',
        'em',
        'h1',
        'h2',
        'h3',
        'h4',
        'h5',
        'h6',
        'hr',
        'li',
        'ol',
        'rb',
        'rp',
        'rt',
        'td',
        'th',
        'tr',
        'tt',
        'ul',
        'bdi',
        'bdo',
        'big',
        'del',
        'dfn',
        'div',
        'ins',
        'kbd',
        'rtc',
        'sub',
        'sup',
        'var',
        'wbr',
        'abbr',
        'cite',
        'code',
        'data',
        'font',
        'link',
        'mark',
        'meta',
        'ruby',
        'samp',
        'span',
        'time',
        'small',
        'table',
        'center',
        'strike',
        'strong',
        'caption',
        'blockquote'}
    parser_tags = {
        'ce',
        'pre',
        'ref',
        'rss',
        'chem',
        'math',
        'poem',
        'tvar',
        'graph',
        'hiero',
        'score',
        'nowiki',
        'gallery',
        'maplink',
        'section',
        'imagemap',
        'inputbox',
        'mapframe',
        'timeline',
        'languages',
        'noinclude',
        'translate',
        'charinsert',
        'references',
        'includeonly',
        'langconvert',
        'onlyinclude',
        'categorytree',
        'templatedata',
        'templatestyles',
        'dynamicpagelist',
        'syntaxhighlight'}
    variant_langs = {
        'sr-ec',
        'sr-el',
        'zh-cn',
        'zh-hk',
        'zh-mo',
        'zh-my',
        'zh-sg',
        'zh-tw',
        'ku-arab',
        'ku-latn',
        'sh-cyrl',
        'sh-latn',
        'tg-latn',
        'uz-cyrl',
        'uz-latn',
        'zh-hans',
        'zh-hant',
        'ban-bali',
        'crh-cyrl',
        'crh-latn',
        'gan-hans',
        'gan-hant',
        'ike-cans',
        'ike-latn',
        'shi-latn',
        'shi-tfng',
        'tly-cyrl',
        'wuu-hans',
        'wuu-hant',
        'ban-x-pku',
        'ban-x-dharma',
        'en-x-piglatin',
        'ban-x-palmleaf',
        'en',
        'iu',
        'ku',
        'sr',
        'tg',
        'uz',
        'zh',
        'ban',
        'crh',
        'gan',
        'shi',
        'tly',
        'wuu'}
    magic_vars_i = {
        'INT',
        'PAGEID',
        'SERVER',
        'STYLEPATH',
        'SCRIPTPATH',
        'SERVERNAME',
        'ARTICLEPATH'}
    magic_vars = {
        '=',
        'DIRMARK',
        'LOCALDAY',
        'LOCALDOW',
        'PAGENAME',
        'SITENAME',
        'LOCALDAY2',
        'LOCALHOUR',
        'LOCALTIME',
        'LOCALWEEK',
        'LOCALYEAR',
        'NAMESPACE',
        'PAGENAMEE',
        'TALKSPACE',
        'CURRENTDAY',
        'CURRENTDOW',
        'LOCALMONTH',
        'NAMESPACEE',
        'REVISIONID',
        'TALKSPACEE',
        'CONTENTLANG',
        'CURRENTDAY2',
        'CURRENTHOUR',
        'CURRENTTIME',
        'CURRENTWEEK',
        'CURRENTYEAR',
        'LOCALMONTH1',
        'LOCALMONTH2',
        'REVISIONDAY',
        'SUBPAGENAME',
        'ARTICLESPACE',
        'BASEPAGENAME',
        'CURRENTMONTH',
        'FULLPAGENAME',
        'LOCALDAYNAME',
        'PAGELANGUAGE',
        'REVISIONDAY2',
        'REVISIONSIZE',
        'REVISIONUSER',
        'REVISIONYEAR',
        'ROOTPAGENAME',
        'SUBJECTSPACE',
        'SUBPAGENAMEE',
        'TALKPAGENAME',
        'ARTICLESPACEE',
        'BASEPAGENAMEE',
        'CURRENTMONTH1',
        'CURRENTMONTH2',
        'DIRECTIONMARK',
        'FULLPAGENAMEE',
        'NUMBEROFEDITS',
        'NUMBEROFFILES',
        'NUMBEROFPAGES',
        'NUMBEROFUSERS',
        'REVISIONMONTH',
        'ROOTPAGENAMEE',
        'SUBJECTSPACEE',
        'TALKPAGENAMEE',
        'CURRENTDAYNAME',
        'CURRENTVERSION',
        'LOCALMONTHNAME',
        'LOCALTIMESTAMP',
        'NUMBEROFADMINS',
        'REVISIONMONTH1',
        'ARTICLEPAGENAME',
        'CONTENTLANGUAGE',
        'NAMESPACENUMBER',
        'SUBJECTPAGENAME',
        'ARTICLEPAGENAMEE',
        'CASCADINGSOURCES',
        'CURRENTMONTHNAME',
        'CURRENTTIMESTAMP',
        'LOCALMONTHABBREV',
        'NUMBEROFARTICLES',
        'SUBJECTPAGENAMEE',
        'LOCALMONTHNAMEGEN',
        'REVISIONTIMESTAMP',
        'CURRENTMONTHABBREV',
        'CURRENTMONTHNAMEGEN',
        'NUMBEROFACTIVEUSERS',
        '!'}
    parser_functions_i = {
        '\\#LANGUAGE',
        'LC',
        'NS',
        'UC',
        'INT',
        'NSE',
        'BIDI',
        'GENDER',
        'PAGEID',
        'PLURAL',
        'FULLURL',
        'GRAMMAR',
        'LCFIRST',
        'PADLEFT',
        'UCFIRST',
        'FILEPATH',
        'FULLURLE',
        'LOCALURL',
        'PADRIGHT',
        'FORMATNUM',
        'LOCALURLE',
        'URLENCODE',
        'ANCHORENCODE',
        'CANONICALURL',
        'CANONICALURLE'}
    parser_functions = {
        'INT',
        'PAGENAME',
        'PAGESIZE',
        'NAMESPACE',
        'PAGENAMEE',
        'PAGESINNS',
        'TALKSPACE',
        'NAMESPACEE',
        'NUMINGROUP',
        'PAGESINCAT',
        'REVISIONID',
        'TALKSPACEE',
        'DEFAULTSORT',
        'REVISIONDAY',
        'SUBPAGENAME',
        'ARTICLESPACE',
        'BASEPAGENAME',
        'DISPLAYTITLE',
        'FULLPAGENAME',
        'REVISIONDAY2',
        'REVISIONUSER',
        'REVISIONYEAR',
        'ROOTPAGENAME',
        'SUBJECTSPACE',
        'SUBPAGENAMEE',
        'TALKPAGENAME',
        'ARTICLESPACEE',
        'BASEPAGENAMEE',
        'FULLPAGENAMEE',
        'NUMBERINGROUP',
        'NUMBEROFEDITS',
        'NUMBEROFFILES',
        'NUMBEROFPAGES',
        'NUMBEROFUSERS',
        'REVISIONMONTH',
        'ROOTPAGENAMEE',
        'SUBJECTSPACEE',
        'TALKPAGENAMEE',
        'DEFAULTSORTKEY',
        'NUMBEROFADMINS',
        'REVISIONMONTH1',
        'ARTICLEPAGENAME',
        'NAMESPACENUMBER',
        'PAGESINCATEGORY',
        'PROTECTIONLEVEL',
        'SUBJECTPAGENAME',
        'ARTICLEPAGENAMEE',
        'CASCADINGSOURCES',
        'NUMBEROFARTICLES',
        'PAGESINNAMESPACE',
        'PROTECTIONEXPIRY',
        'SUBJECTPAGENAMEE',
        'REVISIONTIMESTAMP',
        'DEFAULTCATEGORYSORT',
        'NUMBEROFACTIVEUSERS'}
# WARNING: Decompyle incomplete
