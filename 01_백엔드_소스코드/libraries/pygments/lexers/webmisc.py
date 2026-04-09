# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: webmisc.pyc (Python 3.11)

'''
    pygments.lexers.webmisc
    ~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for misc. web stuff.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import RegexLexer, ExtendedRegexLexer, include, bygroups, default, using
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Literal, Whitespace
from pygments.lexers.css import _indentation, _starts_block
from pygments.lexers.html import HtmlLexer
from pygments.lexers.javascript import JavascriptLexer
from pygments.lexers.ruby import RubyLexer
__all__ = [
    'DuelLexer',
    'SlimLexer',
    'XQueryLexer',
    'QmlLexer',
    'CirruLexer']

class DuelLexer(RegexLexer):
    '''
    Lexer for Duel Views Engine (formerly JBST) markup with JavaScript code blocks.
    '''
    name = 'Duel'
    url = 'http://duelengine.org/'
    aliases = [
        'duel',
        'jbst',
        'jsonml+bst']
    filenames = [
        '*.duel',
        '*.jbst']
    mimetypes = [
        'text/x-duel',
        'text/x-jbst']
    version_added = '1.4'
    flags = re.DOTALL
    tokens = {
        'root': [
            ('(<%[@=#!:]?)(.*?)(%>)', bygroups(Name.Tag, using(JavascriptLexer), Name.Tag)),
            ('(<%\\$)(.*?)(:)(.*?)(%>)', bygroups(Name.Tag, Name.Function, Punctuation, String, Name.Tag)),
            ('(<%--)(.*?)(--%>)', bygroups(Name.Tag, Comment.Multiline, Name.Tag)),
            ('(<script.*?>)(.*?)(</script>)', bygroups(using(HtmlLexer), using(JavascriptLexer), using(HtmlLexer))),
            ('(.+?)(?=<)', using(HtmlLexer)),
            ('.+', using(HtmlLexer))] }


class XQueryLexer(ExtendedRegexLexer):
    __module__ = __name__
    __qualname__ = 'XQueryLexer'
    __doc__ = '\n    An XQuery lexer, parsing a stream and outputting the tokens needed to\n    highlight xquery code.\n    '
    name = 'XQuery'
    url = 'https://www.w3.org/XML/Query/'
    aliases = [
        'xquery',
        'xqy',
        'xq',
        'xql',
        'xqm']
    filenames = [
        '*.xqy',
        '*.xquery',
        '*.xq',
        '*.xql',
        '*.xqm']
    mimetypes = [
        'text/xquery',
        'application/xquery']
    version_added = '1.4'
    xquery_parse_state = []
    ncnamestartchar = '(?:[A-Z]|_|[a-z])'
    ncnamechar = '(?:' + ncnamestartchar + '|-|\\.|[0-9])'
    ncname = f'''(?:{ncnamestartchar}+{ncnamechar}*)'''
    pitarget_namestartchar = '(?:[A-KN-WYZ]|_|:|[a-kn-wyz])'
    pitarget_namechar = '(?:' + pitarget_namestartchar + '|-|\\.|[0-9])'
    pitarget = f'''{pitarget_namestartchar}+{pitarget_namechar}*'''
    prefixedname = f'''{ncname}:{ncname}'''
    unprefixedname = ncname
    qname = f'''(?:{prefixedname}|{unprefixedname})'''
    entityref = '(?:&(?:lt|gt|amp|quot|apos|nbsp);)'
    charref = '(?:&#[0-9]+;|&#x[0-9a-fA-F]+;)'
    stringdouble = '(?:"(?:' + entityref + '|' + charref + '|""|[^&"])*")'
    stringsingle = "(?:'(?:" + entityref + '|' + charref + "|''|[^&'])*')"
    elementcontentchar = '[A-Za-z]|\\s|\\d|[!"#$%()*+,\\-./:;=?@\\[\\\\\\]^_\\\'`|~]'
    quotattrcontentchar = "[A-Za-z]|\\s|\\d|[!#$%()*+,\\-./:;=?@\\[\\\\\\]^_\\'`|~]"
    aposattrcontentchar = '[A-Za-z]|\\s|\\d|[!"#$%()*+,\\-./:;=?@\\[\\\\\\]^_`|~]'
    flags = re.DOTALL | re.MULTILINE
    
    def punctuation_root_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def operator_root_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def popstate_tag_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def popstate_xmlcomment_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def popstate_kindtest_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def popstate_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_element_content_starttag_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_cdata_section_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_starttag_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_operator_order_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_operator_map_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_operator_root_validate(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_operator_root_validate_withmode(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_operator_processing_instruction_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_element_content_processing_instruction_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_element_content_cdata_section_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_operator_cdata_section_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_element_content_xmlcomment_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_operator_xmlcomment_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_kindtest_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_operator_kindtestforpi_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_operator_kindtest_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_occurrenceindicator_kindtest_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_operator_starttag_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_operator_root_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_operator_root_construct_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_root_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

    
    def pushstate_operator_attribute_callback(lexer, match, ctx):
        pass
    # WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete


class QmlLexer(RegexLexer):
    '''
    For QML files.
    '''
    name = 'QML'
    url = 'https://doc.qt.io/qt-6/qmlapplications.html'
    aliases = [
        'qml',
        'qbs']
    filenames = [
        '*.qml',
        '*.qbs']
    mimetypes = [
        'application/x-qml',
        'application/x-qt.qbs+qml']
    version_added = '1.6'
    flags = re.DOTALL | re.MULTILINE
    tokens = {
        'commentsandwhitespace': [
            ('\\s+', Text),
            ('<!--', Comment),
            ('//.*?\\n', Comment.Single),
            ('/\\*.*?\\*/', Comment.Multiline)],
        'slashstartsregex': [
            include('commentsandwhitespace'),
            ('/(\\\\.|[^[/\\\\\\n]|\\[(\\\\.|[^\\]\\\\\\n])*])+/([gim]+\\b|\\B)', String.Regex, '#pop'),
            ('(?=/)', Text, ('#pop', 'badregex')),
            default('#pop')],
        'badregex': [
            ('\\n', Text, '#pop')],
        'root': [
            ('^(?=\\s|/|<!--)', Text, 'slashstartsregex'),
            include('commentsandwhitespace'),
            ('\\+\\+|--|~|&&|\\?|:|\\|\\||\\\\(?=\\n)|(<<|>>>?|==?|!=?|[-<>+*%&|^/])=?', Operator, 'slashstartsregex'),
            ('[{(\\[;,]', Punctuation, 'slashstartsregex'),
            ('[})\\].]', Punctuation),
            ('\\bid\\s*:\\s*[A-Za-z][\\w.]*', Keyword.Declaration, 'slashstartsregex'),
            ('\\b[A-Za-z][\\w.]*\\s*:', Keyword, 'slashstartsregex'),
            ('(for|in|while|do|break|return|continue|switch|case|default|if|else|throw|try|catch|finally|new|delete|typeof|instanceof|void|this)\\b', Keyword, 'slashstartsregex'),
            ('(var|let|with|function)\\b', Keyword.Declaration, 'slashstartsregex'),
            ('(abstract|boolean|byte|char|class|const|debugger|double|enum|export|extends|final|float|goto|implements|import|int|interface|long|native|package|private|protected|public|short|static|super|synchronized|throws|transient|volatile)\\b', Keyword.Reserved),
            ('(true|false|null|NaN|Infinity|undefined)\\b', Keyword.Constant),
            ('(Array|Boolean|Date|Error|Function|Math|netscape|Number|Object|Packages|RegExp|String|sun|decodeURI|decodeURIComponent|encodeURI|encodeURIComponent|Error|eval|isFinite|isNaN|parseFloat|parseInt|document|this|window)\\b', Name.Builtin),
            ('[$a-zA-Z_]\\w*', Name.Other),
            ('[0-9][0-9]*\\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            ('0x[0-9a-fA-F]+', Number.Hex),
            ('[0-9]+', Number.Integer),
            ('"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Double),
            ("'(\\\\\\\\|\\\\[^\\\\]|[^'\\\\])*'", String.Single)] }


class CirruLexer(RegexLexer):
    '''
    * using ``()`` for expressions, but restricted in a same line
    * using ``""`` for strings, with ``\\`` for escaping chars
    * using ``$`` as folding operator
    * using ``,`` as unfolding operator
    * using indentations for nested blocks
    '''
    name = 'Cirru'
    url = 'http://cirru.org/'
    aliases = [
        'cirru']
    filenames = [
        '*.cirru']
    mimetypes = [
        'text/x-cirru']
    version_added = '2.0'
    flags = re.MULTILINE
    tokens = {
        'string': [
            ('[^"\\\\\\n]+', String),
            ('\\\\', String.Escape, 'escape'),
            ('"', String, '#pop')],
        'escape': [
            ('.', String.Escape, '#pop')],
        'function': [
            ('\\,', Operator, '#pop'),
            ('[^\\s"()]+', Name.Function, '#pop'),
            ('\\)', Operator, '#pop'),
            ('(?=\\n)', Text, '#pop'),
            ('\\(', Operator, '#push'),
            ('"', String, ('#pop', 'string')),
            ('[ ]+', Text.Whitespace)],
        'line': [
            ('(?<!\\w)\\$(?!\\w)', Operator, 'function'),
            ('\\(', Operator, 'function'),
            ('\\)', Operator),
            ('\\n', Text, '#pop'),
            ('"', String, 'string'),
            ('[ ]+', Text.Whitespace),
            ('[+-]?[\\d.]+\\b', Number),
            ('[^\\s"()]+', Name.Variable)],
        'root': [
            ('^\\n+', Text.Whitespace),
            default(('line', 'function'))] }


class SlimLexer(ExtendedRegexLexer):
    '''
    For Slim markup.
    '''
    name = 'Slim'
    aliases = [
        'slim']
    filenames = [
        '*.slim']
    mimetypes = [
        'text/x-slim']
    url = 'https://slim-template.github.io'
    version_added = '2.0'
    flags = re.IGNORECASE
    _dot = '(?: \\|\\n(?=.* \\|)|.)'
    tokens = {
        'root': [
            ('[ \\t]*\\n', Text),
            ('[ \\t]*', _indentation)],
        'css': [
            ('\\.[\\w:-]+', Name.Class, 'tag'),
            ('\\#[\\w:-]+', Name.Function, 'tag')],
        'eval-or-plain': [
            ('([ \\t]*==?)(.*\\n)', bygroups(Punctuation, using(RubyLexer)), 'root'),
            ('[ \\t]+[\\w:-]+(?==)', Name.Attribute, 'html-attributes'),
            default('plain')],
        'content': [
            include('css'),
            ('[\\w:-]+:[ \\t]*\\n', Text, 'plain'),
            ('(-)(.*\\n)', bygroups(Punctuation, using(RubyLexer)), '#pop'),
            ('\\|' + _dot + '*\\n', _starts_block(Text, 'plain'), '#pop'),
            ('/' + _dot + '*\\n', _starts_block(Comment.Preproc, 'slim-comment-block'), '#pop'),
            ('[\\w:-]+', Name.Tag, 'tag'),
            include('eval-or-plain')],
        'tag': [
            include('css'),
            ('[<>]{1,2}(?=[ \\t=])', Punctuation),
            ('[ \\t]+\\n', Punctuation, '#pop:2'),
            include('eval-or-plain')],
        'plain': [
            ('([^#\\n]|#[^{\\n]|(\\\\\\\\)*\\\\#\\{)+', Text),
            ('(#\\{)(.*?)(\\})', bygroups(String.Interpol, using(RubyLexer), String.Interpol)),
            ('\\n', Text, 'root')],
        'html-attributes': [
            ('=', Punctuation),
            ('"[^"]+"', using(RubyLexer), 'tag'),
            ("\\'[^\\']+\\'", using(RubyLexer), 'tag'),
            ('\\w+', Text, 'tag')],
        'slim-comment-block': [
            (_dot + '+', Comment.Preproc),
            ('\\n', Text, 'root')] }
