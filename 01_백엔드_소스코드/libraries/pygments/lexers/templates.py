# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: templates.pyc (Python 3.11)

"""
    pygments.lexers.templates
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for various template engines' markup.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
import re
from pygments.lexers.html import HtmlLexer, XmlLexer
from pygments.lexers.javascript import JavascriptLexer, LassoLexer
from pygments.lexers.css import CssLexer
from pygments.lexers.php import PhpLexer
from pygments.lexers.python import PythonLexer
from pygments.lexers.perl import PerlLexer
from pygments.lexers.jvm import JavaLexer, TeaLangLexer
from pygments.lexers.data import YamlLexer
from pygments.lexers.sql import SqlLexer
from pygments.lexer import Lexer, DelegatingLexer, RegexLexer, bygroups, include, using, this, default, combined
from pygments.token import Error, Punctuation, Whitespace, Text, Comment, Operator, Keyword, Name, String, Number, Other, Token
from pygments.util import html_doctype_matches, looks_like_xml
__all__ = [
    'HtmlPhpLexer',
    'XmlPhpLexer',
    'CssPhpLexer',
    'JavascriptPhpLexer',
    'ErbLexer',
    'RhtmlLexer',
    'XmlErbLexer',
    'CssErbLexer',
    'JavascriptErbLexer',
    'SmartyLexer',
    'HtmlSmartyLexer',
    'XmlSmartyLexer',
    'CssSmartyLexer',
    'JavascriptSmartyLexer',
    'DjangoLexer',
    'HtmlDjangoLexer',
    'CssDjangoLexer',
    'XmlDjangoLexer',
    'JavascriptDjangoLexer',
    'GenshiLexer',
    'HtmlGenshiLexer',
    'GenshiTextLexer',
    'CssGenshiLexer',
    'JavascriptGenshiLexer',
    'MyghtyLexer',
    'MyghtyHtmlLexer',
    'MyghtyXmlLexer',
    'MyghtyCssLexer',
    'MyghtyJavascriptLexer',
    'MasonLexer',
    'MakoLexer',
    'MakoHtmlLexer',
    'MakoXmlLexer',
    'MakoJavascriptLexer',
    'MakoCssLexer',
    'JspLexer',
    'CheetahLexer',
    'CheetahHtmlLexer',
    'CheetahXmlLexer',
    'CheetahJavascriptLexer',
    'EvoqueLexer',
    'EvoqueHtmlLexer',
    'EvoqueXmlLexer',
    'ColdfusionLexer',
    'ColdfusionHtmlLexer',
    'ColdfusionCFCLexer',
    'VelocityLexer',
    'VelocityHtmlLexer',
    'VelocityXmlLexer',
    'SspLexer',
    'TeaTemplateLexer',
    'LassoHtmlLexer',
    'LassoXmlLexer',
    'LassoCssLexer',
    'LassoJavascriptLexer',
    'HandlebarsLexer',
    'HandlebarsHtmlLexer',
    'YamlJinjaLexer',
    'LiquidLexer',
    'TwigLexer',
    'TwigHtmlLexer',
    'Angular2Lexer',
    'Angular2HtmlLexer',
    'SqlJinjaLexer']

class ErbLexer(Lexer):
    '''
    Generic ERB (Ruby Templating) lexer.

    Just highlights ruby code between the preprocessor directives, other data
    is left untouched by the lexer.

    All options are also forwarded to the `RubyLexer`.
    '''
    name = 'ERB'
    url = 'https://github.com/ruby/erb'
    aliases = [
        'erb']
    mimetypes = [
        'application/x-ruby-templating']
    version_added = ''
    _block_re = re.compile('(<%%|%%>|<%=|<%#|<%-|<%|-%>|%>|^%[^%].*?$)', re.M)
    
    def __init__(self, **options):
        RubyLexer = RubyLexer
        import pygments.lexers.ruby
    # WARNING: Decompyle incomplete

    
    def get_tokens_unprocessed(self, text):
        '''
        Since ERB doesn\'t allow "<%" and other tags inside of ruby
        blocks we have to use a split approach here that fails for
        that too.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def analyse_text(text):
        if '<%' in text or '%>' in text:
            return 0.4
        return None



class SmartyLexer(RegexLexer):
    '''
    Generic Smarty template lexer.

    Just highlights smarty code between the preprocessor directives, other
    data is left untouched by the lexer.
    '''
    name = 'Smarty'
    url = 'https://www.smarty.net/'
    aliases = [
        'smarty']
    filenames = [
        '*.tpl']
    mimetypes = [
        'application/x-smarty']
    version_added = ''
    flags = re.MULTILINE | re.DOTALL
    tokens = {
        'root': [
            ('[^{]+', Other),
            ('(\\{)(\\*.*?\\*)(\\})', bygroups(Comment.Preproc, Comment, Comment.Preproc)),
            ('(\\{php\\})(.*?)(\\{/php\\})', bygroups(Comment.Preproc, using(PhpLexer, startinline = True), Comment.Preproc)),
            ('(\\{)(/?[a-zA-Z_]\\w*)(\\s*)', bygroups(Comment.Preproc, Name.Function, Text), 'smarty'),
            ('\\{', Comment.Preproc, 'smarty')],
        'smarty': [
            ('\\s+', Text),
            ('\\{', Comment.Preproc, '#push'),
            ('\\}', Comment.Preproc, '#pop'),
            ('#[a-zA-Z_]\\w*#', Name.Variable),
            ('\\$[a-zA-Z_]\\w*(\\.\\w+)*', Name.Variable),
            ('[~!%^&*()+=|\\[\\]:;,.<>/?@-]', Operator),
            ('(true|false|null)\\b', Keyword.Constant),
            ('[0-9](\\.[0-9]*)?(eE[+-][0-9])?[flFLdD]?|0[xX][0-9a-fA-F]+[Ll]?', Number),
            ('"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Double),
            ("'(\\\\\\\\|\\\\[^\\\\]|[^'\\\\])*'", String.Single),
            ('[a-zA-Z_]\\w*', Name.Attribute)] }
    
    def analyse_text(text):
        rv = 0
        if re.search('\\{if\\s+.*?\\}.*?\\{/if\\}', text):
            rv += 0.15
        if re.search('\\{include\\s+file=.*?\\}', text):
            rv += 0.15
        if re.search('\\{foreach\\s+.*?\\}.*?\\{/foreach\\}', text):
            rv += 0.15
        if re.search('\\{\\$.*?\\}', text):
            rv += 0.01
        return rv



class VelocityLexer(RegexLexer):
    '''
    Generic Velocity template lexer.

    Just highlights velocity directives and variable references, other
    data is left untouched by the lexer.
    '''
    name = 'Velocity'
    url = 'https://velocity.apache.org/'
    aliases = [
        'velocity']
    filenames = [
        '*.vm',
        '*.fhtml']
    version_added = ''
    flags = re.MULTILINE | re.DOTALL
    identifier = '[a-zA-Z_]\\w*'
    tokens = {
        'root': [
            ('[^{#$]+', Other),
            ('(#)(\\*.*?\\*)(#)', bygroups(Comment.Preproc, Comment, Comment.Preproc)),
            ('(##)(.*?$)', bygroups(Comment.Preproc, Comment)),
            ('(#\\{?)(' + identifier + ')(\\}?)(\\s?\\()', bygroups(Comment.Preproc, Name.Function, Comment.Preproc, Punctuation), 'directiveparams'),
            ('(#\\{?)(' + identifier + ')(\\}|\\b)', bygroups(Comment.Preproc, Name.Function, Comment.Preproc)),
            ('\\$!?\\{?', Punctuation, 'variable')],
        'variable': [
            (identifier, Name.Variable),
            ('\\(', Punctuation, 'funcparams'),
            ('(\\.)(' + identifier + ')', bygroups(Punctuation, Name.Variable), '#push'),
            ('\\}', Punctuation, '#pop'),
            default('#pop')],
        'directiveparams': [
            ('(&&|\\|\\||==?|!=?|[-<>+*%&|^/])|\\b(eq|ne|gt|lt|ge|le|not|in)\\b', Operator),
            ('\\[', Operator, 'rangeoperator'),
            ('\\b' + identifier + '\\b', Name.Function),
            include('funcparams')],
        'rangeoperator': [
            ('\\.\\.', Operator),
            include('funcparams'),
            ('\\]', Operator, '#pop')],
        'funcparams': [
            ('\\$!?\\{?', Punctuation, 'variable'),
            ('\\s+', Text),
            ('[,:]', Punctuation),
            ('"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Double),
            ("'(\\\\\\\\|\\\\[^\\\\]|[^'\\\\])*'", String.Single),
            ('0[xX][0-9a-fA-F]+[Ll]?', Number),
            ('\\b[0-9]+\\b', Number),
            ('(true|false|null)\\b', Keyword.Constant),
            ('\\(', Punctuation, '#push'),
            ('\\)', Punctuation, '#pop'),
            ('\\{', Punctuation, '#push'),
            ('\\}', Punctuation, '#pop'),
            ('\\[', Punctuation, '#push'),
            ('\\]', Punctuation, '#pop')] }
    
    def analyse_text(text):
        rv = 0
        if re.search('#\\{?macro\\}?\\(.*?\\).*?#\\{?end\\}?', text, re.DOTALL):
            rv += 0.25
        if re.search('#\\{?if\\}?\\(.+?\\).*?#\\{?end\\}?', text, re.DOTALL):
            rv += 0.15
        if re.search('#\\{?foreach\\}?\\(.+?\\).*?#\\{?end\\}?', text, re.DOTALL):
            rv += 0.15
        if re.search('\\$!?\\{?[a-zA-Z_]\\w*(\\([^)]*\\))?(\\.\\w+(\\([^)]*\\))?)*\\}?', text):
            rv += 0.01
        return rv



class VelocityHtmlLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class VelocityXmlLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class DjangoLexer(RegexLexer):
    '''
    Generic `Django <https://www.djangoproject.com/documentation/templates/>`_
    and `Jinja <https://jinja.palletsprojects.com>`_ template lexer.

    It just highlights django/jinja code between the preprocessor directives,
    other data is left untouched by the lexer.
    '''
    name = 'Django/Jinja'
    aliases = [
        'django',
        'jinja']
    mimetypes = [
        'application/x-django-templating',
        'application/x-jinja']
    url = 'https://www.djangoproject.com/documentation/templates'
    version_added = ''
    flags = re.M | re.S
    tokens = {
        'root': [
            ('[^{]+', Other),
            ('\\{\\{', Comment.Preproc, 'var'),
            ('\\{#.*?#\\}', Comment),
            ('(\\{%)(-?\\s*)(comment)(\\s*-?)(%\\})(.*?)(\\{%)(-?\\s*)(endcomment)(\\s*-?)(%\\})', bygroups(Comment.Preproc, Text, Keyword, Text, Comment.Preproc, Comment, Comment.Preproc, Text, Keyword, Text, Comment.Preproc)),
            ('(\\{%)(-?\\s*)(raw)(\\s*-?)(%\\})(.*?)(\\{%)(-?\\s*)(endraw)(\\s*-?)(%\\})', bygroups(Comment.Preproc, Text, Keyword, Text, Comment.Preproc, Text, Comment.Preproc, Text, Keyword, Text, Comment.Preproc)),
            ('(\\{%)(-?\\s*)(filter)(\\s+)([a-zA-Z_]\\w*)', bygroups(Comment.Preproc, Text, Keyword, Text, Name.Function), 'block'),
            ('(\\{%)(-?\\s*)([a-zA-Z_]\\w*)', bygroups(Comment.Preproc, Text, Keyword), 'block'),
            ('\\{', Other)],
        'varnames': [
            ('(\\|)(\\s*)([a-zA-Z_]\\w*)', bygroups(Operator, Text, Name.Function)),
            ('(is)(\\s+)(not)?(\\s+)?([a-zA-Z_]\\w*)', bygroups(Keyword, Text, Keyword, Text, Name.Function)),
            ('(_|true|false|none|True|False|None)\\b', Keyword.Pseudo),
            ('(in|as|reversed|recursive|not|and|or|is|if|else|import|with(?:(?:out)?\\s*context)?|scoped|ignore\\s+missing)\\b', Keyword),
            ('(loop|block|super|forloop)\\b', Name.Builtin),
            ('[a-zA-Z_][\\w-]*', Name.Variable),
            ('\\.\\w+', Name.Variable),
            (':?"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Double),
            (":?'(\\\\\\\\|\\\\[^\\\\]|[^'\\\\])*'", String.Single),
            ('([{}()\\[\\]+\\-*/%,:~]|[><=]=?|!=)', Operator),
            ('[0-9](\\.[0-9]*)?(eE[+-][0-9])?[flFLdD]?|0[xX][0-9a-fA-F]+[Ll]?', Number)],
        'var': [
            ('\\s+', Text),
            ('(-?)(\\}\\})', bygroups(Text, Comment.Preproc), '#pop'),
            include('varnames')],
        'block': [
            ('\\s+', Text),
            ('(-?)(%\\})', bygroups(Text, Comment.Preproc), '#pop'),
            include('varnames'),
            ('.', Punctuation)] }
    
    def analyse_text(text):
        rv = 0
    # WARNING: Decompyle incomplete



class MyghtyLexer(RegexLexer):
    """
    Generic myghty templates lexer. Code that isn't Myghty
    markup is yielded as `Token.Other`.
    """
    name = 'Myghty'
    url = 'http://www.myghty.org/'
    aliases = [
        'myghty']
    filenames = [
        '*.myt',
        'autodelegate']
    mimetypes = [
        'application/x-myghty']
    version_added = '0.6'
    tokens = {
        'root': [
            ('\\s+', Text),
            ('(?s)(<%(?:def|method))(\\s*)(.*?)(>)(.*?)(</%\\2\\s*>)', bygroups(Name.Tag, Text, Name.Function, Name.Tag, using(this), Name.Tag)),
            ('(?s)(<%\\w+)(.*?)(>)(.*?)(</%\\2\\s*>)', bygroups(Name.Tag, Name.Function, Name.Tag, using(PythonLexer), Name.Tag)),
            ('(<&[^|])(.*?)(,.*?)?(&>)', bygroups(Name.Tag, Name.Function, using(PythonLexer), Name.Tag)),
            ('(?s)(<&\\|)(.*?)(,.*?)?(&>)', bygroups(Name.Tag, Name.Function, using(PythonLexer), Name.Tag)),
            ('</&>', Name.Tag),
            ('(?s)(<%!?)(.*?)(%>)', bygroups(Name.Tag, using(PythonLexer), Name.Tag)),
            ('(?<=^)#[^\\n]*(\\n|\\Z)', Comment),
            ('(?<=^)(%)([^\\n]*)(\\n|\\Z)', bygroups(Name.Tag, using(PythonLexer), Other)),
            ("(?sx)\n                 (.+?)               # anything, followed by:\n                 (?:\n                  (?<=\\n)(?=[%#]) |  # an eval or comment line\n                  (?=</?[%&]) |      # a substitution or block or\n                                     # call start or end\n                                     # - don't consume\n                  (\\\\\\n) |           # an escaped newline\n                  \\Z                 # end of string\n                 )", bygroups(Other, Operator))] }


class MyghtyHtmlLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class MyghtyXmlLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class MyghtyJavascriptLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class MyghtyCssLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class MasonLexer(RegexLexer):
    """
    Generic mason templates lexer. Stolen from Myghty lexer. Code that isn't
    Mason markup is HTML.
    """
    name = 'Mason'
    url = 'http://www.masonhq.com/'
    aliases = [
        'mason']
    filenames = [
        '*.m',
        '*.mhtml',
        '*.mc',
        '*.mi',
        'autohandler',
        'dhandler']
    mimetypes = [
        'application/x-mason']
    version_added = '1.4'
    tokens = {
        'root': [
            ('\\s+', Whitespace),
            ('(?s)(<%doc>)(.*?)(</%doc>)', bygroups(Name.Tag, Comment.Multiline, Name.Tag)),
            ('(?s)(<%(?:def|method))(\\s*)(.*?)(>)(.*?)(</%\\2\\s*>)', bygroups(Name.Tag, Whitespace, Name.Function, Name.Tag, using(this), Name.Tag)),
            ('(?s)(<%(\\w+)(.*?)(>))(.*?)(</%\\2\\s*>)', bygroups(Name.Tag, None, None, None, using(PerlLexer), Name.Tag)),
            ('(?s)(<&[^|])(.*?)(,.*?)?(&>)', bygroups(Name.Tag, Name.Function, using(PerlLexer), Name.Tag)),
            ('(?s)(<&\\|)(.*?)(,.*?)?(&>)', bygroups(Name.Tag, Name.Function, using(PerlLexer), Name.Tag)),
            ('</&>', Name.Tag),
            ('(?s)(<%!?)(.*?)(%>)', bygroups(Name.Tag, using(PerlLexer), Name.Tag)),
            ('(?<=^)#[^\\n]*(\\n|\\Z)', Comment),
            ('(?<=^)(%)([^\\n]*)(\\n|\\Z)', bygroups(Name.Tag, using(PerlLexer), Other)),
            ("(?sx)\n                 (.+?)               # anything, followed by:\n                 (?:\n                  (?<=\\n)(?=[%#]) |  # an eval or comment line\n                  (?=</?[%&]) |      # a substitution or block or\n                                     # call start or end\n                                     # - don't consume\n                  (\\\\\\n) |           # an escaped newline\n                  \\Z                 # end of string\n                 )", bygroups(using(HtmlLexer), Operator))] }
    
    def analyse_text(text):
        result = 0
    # WARNING: Decompyle incomplete



class MakoLexer(RegexLexer):
    """
    Generic mako templates lexer. Code that isn't Mako
    markup is yielded as `Token.Other`.
    """
    name = 'Mako'
    url = 'http://www.makotemplates.org/'
    aliases = [
        'mako']
    filenames = [
        '*.mao']
    mimetypes = [
        'application/x-mako']
    version_added = '0.7'
    tokens = {
        'root': [
            ('(\\s*)(%)(\\s*end(?:\\w+))(\\n|\\Z)', bygroups(Text.Whitespace, Comment.Preproc, Keyword, Other)),
            ('(\\s*)(%)([^\\n]*)(\\n|\\Z)', bygroups(Text.Whitespace, Comment.Preproc, using(PythonLexer), Other)),
            ('(\\s*)(##[^\\n]*)(\\n|\\Z)', bygroups(Text.Whitespace, Comment.Single, Text.Whitespace)),
            ('(?s)<%doc>.*?</%doc>', Comment.Multiline),
            ('(<%)([\\w.:]+)', bygroups(Comment.Preproc, Name.Builtin), 'tag'),
            ('(</%)([\\w.:]+)(>)', bygroups(Comment.Preproc, Name.Builtin, Comment.Preproc)),
            ('<%(?=([\\w.:]+))', Comment.Preproc, 'ondeftags'),
            ('(?s)(<%(?:!?))(.*?)(%>)', bygroups(Comment.Preproc, using(PythonLexer), Comment.Preproc)),
            ('(\\$\\{)(.*?)(\\})', bygroups(Comment.Preproc, using(PythonLexer), Comment.Preproc)),
            ("(?sx)\n                (.+?)                # anything, followed by:\n                (?:\n                 (?<=\\n)(?=%|\\#\\#) | # an eval or comment line\n                 (?=\\#\\*) |          # multiline comment\n                 (?=</?%) |          # a python block\n                                     # call start or end\n                 (?=\\$\\{) |          # a substitution\n                 (?<=\\n)(?=\\s*%) |\n                                     # - don't consume\n                 (\\\\\\n) |            # an escaped newline\n                 \\Z                  # end of string\n                )\n            ", bygroups(Other, Operator)),
            ('\\s+', Text)],
        'ondeftags': [
            ('<%', Comment.Preproc),
            ('(?<=<%)(include|inherit|namespace|page)', Name.Builtin),
            include('tag')],
        'tag': [
            ('((?:\\w+)\\s*=)(\\s*)(".*?")', bygroups(Name.Attribute, Text, String)),
            ('/?\\s*>', Comment.Preproc, '#pop'),
            ('\\s+', Text)],
        'attr': [
            ('".*?"', String, '#pop'),
            ("'.*?'", String, '#pop'),
            ('[^\\s>]+', String, '#pop')] }


class MakoHtmlLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class MakoXmlLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class MakoJavascriptLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class MakoCssLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class CheetahPythonLexer(Lexer):
    """
    Lexer for handling Cheetah's special $ tokens in Python syntax.
    """
    
    def get_tokens_unprocessed(self, text):
        pass
    # WARNING: Decompyle incomplete



class CheetahLexer(RegexLexer):
    """
    Generic cheetah templates lexer. Code that isn't Cheetah
    markup is yielded as `Token.Other`.  This also works for
    `spitfire templates`_ which use the same syntax.

    .. _spitfire templates: http://code.google.com/p/spitfire/
    """
    name = 'Cheetah'
    url = 'http://www.cheetahtemplate.org/'
    aliases = [
        'cheetah',
        'spitfire']
    filenames = [
        '*.tmpl',
        '*.spt']
    mimetypes = [
        'application/x-cheetah',
        'application/x-spitfire']
    version_added = ''
    tokens = {
        'root': [
            ('(##[^\\n]*)$', bygroups(Comment)),
            ('#[*](.|\\n)*?[*]#', Comment),
            ('#end[^#\\n]*(?:#|$)', Comment.Preproc),
            ('#slurp$', Comment.Preproc),
            ('(#[a-zA-Z]+)([^#\\n]*)(#|$)', bygroups(Comment.Preproc, using(CheetahPythonLexer), Comment.Preproc)),
            ('(\\$)([a-zA-Z_][\\w.]*\\w)', bygroups(Comment.Preproc, using(CheetahPythonLexer))),
            ('(?s)(\\$\\{!?)(.*?)(\\})', bygroups(Comment.Preproc, using(CheetahPythonLexer), Comment.Preproc)),
            ('(?sx)\n                (.+?)               # anything, followed by:\n                (?:\n                 (?=\\#[#a-zA-Z]*) | # an eval comment\n                 (?=\\$[a-zA-Z_{]) | # a substitution\n                 \\Z                 # end of string\n                )\n            ', Other),
            ('\\s+', Text)] }


class CheetahHtmlLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class CheetahXmlLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class CheetahJavascriptLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class GenshiTextLexer(RegexLexer):
    '''
    A lexer that highlights genshi text templates.
    '''
    name = 'Genshi Text'
    url = 'https://genshi.edgewall.org/'
    aliases = [
        'genshitext']
    mimetypes = [
        'application/x-genshi-text',
        'text/x-genshi']
    version_added = ''
    tokens = {
        'root': [
            ('[^#$\\s]+', Other),
            ('^(\\s*)(##.*)$', bygroups(Text, Comment)),
            ('^(\\s*)(#)', bygroups(Text, Comment.Preproc), 'directive'),
            include('variable'),
            ('[#$\\s]', Other)],
        'directive': [
            ('\\n', Text, '#pop'),
            ('(?:def|for|if)\\s+.*', using(PythonLexer), '#pop'),
            ('(choose|when|with)([^\\S\\n]+)(.*)', bygroups(Keyword, Text, using(PythonLexer)), '#pop'),
            ('(choose|otherwise)\\b', Keyword, '#pop'),
            ('(end\\w*)([^\\S\\n]*)(.*)', bygroups(Keyword, Text, Comment), '#pop')],
        'variable': [
            ('(?<!\\$)(\\$\\{)(.+?)(\\})', bygroups(Comment.Preproc, using(PythonLexer), Comment.Preproc)),
            ('(?<!\\$)(\\$)([a-zA-Z_][\\w.]*)', Name.Variable)] }


class GenshiMarkupLexer(RegexLexer):
    '''
    Base lexer for Genshi markup, used by `HtmlGenshiLexer` and
    `GenshiLexer`.
    '''
    flags = re.DOTALL
    tokens = {
        'root': [
            ('[^<$]+', Other),
            ('(<\\?python)(.*?)(\\?>)', bygroups(Comment.Preproc, using(PythonLexer), Comment.Preproc)),
            ('<\\s*(script|style)\\s*.*?>.*?<\\s*/\\1\\s*>', Other),
            ('<\\s*py:[a-zA-Z0-9]+', Name.Tag, 'pytag'),
            ('<\\s*[a-zA-Z0-9:.]+', Name.Tag, 'tag'),
            include('variable'),
            ('[<$]', Other)],
        'pytag': [
            ('\\s+', Text),
            ('[\\w:-]+\\s*=', Name.Attribute, 'pyattr'),
            ('/?\\s*>', Name.Tag, '#pop')],
        'pyattr': [
            ('(")(.*?)(")', bygroups(String, using(PythonLexer), String), '#pop'),
            ("(')(.*?)(')", bygroups(String, using(PythonLexer), String), '#pop'),
            ('[^\\s>]+', String, '#pop')],
        'tag': [
            ('\\s+', Text),
            ('py:[\\w-]+\\s*=', Name.Attribute, 'pyattr'),
            ('[\\w:-]+\\s*=', Name.Attribute, 'attr'),
            ('/?\\s*>', Name.Tag, '#pop')],
        'attr': [
            ('"', String, 'attr-dstring'),
            ("'", String, 'attr-sstring'),
            ('[^\\s>]*', String, '#pop')],
        'attr-dstring': [
            ('"', String, '#pop'),
            include('strings'),
            ("'", String)],
        'attr-sstring': [
            ("'", String, '#pop'),
            include('strings'),
            ("'", String)],
        'strings': [
            ('[^"\'$]+', String),
            include('variable')],
        'variable': [
            ('(?<!\\$)(\\$\\{)(.+?)(\\})', bygroups(Comment.Preproc, using(PythonLexer), Comment.Preproc)),
            ('(?<!\\$)(\\$)([a-zA-Z_][\\w\\.]*)', Name.Variable)] }


class HtmlGenshiLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class GenshiLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class JavascriptGenshiLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class CssGenshiLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class RhtmlLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class XmlErbLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class CssErbLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class JavascriptErbLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class HtmlPhpLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class XmlPhpLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class CssPhpLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class JavascriptPhpLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class HtmlSmartyLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class XmlSmartyLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class CssSmartyLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class JavascriptSmartyLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class HtmlDjangoLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class XmlDjangoLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class CssDjangoLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class JavascriptDjangoLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class JspRootLexer(RegexLexer):
    '''
    Base for the `JspLexer`. Yields `Token.Other` for area outside of
    JSP tags.

    .. versionadded:: 0.7
    '''
    tokens = {
        'root': [
            ('<%\\S?', Keyword, 'sec'),
            ('</?jsp:(forward|getProperty|include|plugin|setProperty|useBean).*?>', Keyword),
            ('[^<]+', Other),
            ('<', Other)],
        'sec': [
            ('%>', Keyword, '#pop'),
            ('[\\w\\W]+?(?=%>|\\Z)', using(JavaLexer))] }


class JspLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class EvoqueLexer(RegexLexer):
    '''
    For files using the Evoque templating system.
    '''
    name = 'Evoque'
    aliases = [
        'evoque']
    filenames = [
        '*.evoque']
    mimetypes = [
        'application/x-evoque']
    url = 'https://gizmojo.org/templating'
    version_added = '1.1'
    flags = re.DOTALL
    tokens = {
        'root': [
            ('[^#$]+', Other),
            ('#\\[', Comment.Multiline, 'comment'),
            ('\\$\\$', Other),
            ('\\$\\w+:[^$\\n]*\\$', Comment.Multiline),
            ('(\\$)(begin|end)(\\{(%)?)(.*?)((?(4)%)\\})', bygroups(Punctuation, Name.Builtin, Punctuation, None, String, Punctuation)),
            ('(\\$)(evoque|overlay)(\\{(%)?)(\\s*[#\\w\\-"\\\'.]+)?(.*?)((?(4)%)\\})', bygroups(Punctuation, Name.Builtin, Punctuation, None, String, using(PythonLexer), Punctuation)),
            ('(\\$)(\\w+)(\\{(%)?)(.*?)((?(4)%)\\})', bygroups(Punctuation, Name.Builtin, Punctuation, None, using(PythonLexer), Punctuation)),
            ('(\\$)(else|rof|fi)', bygroups(Punctuation, Name.Builtin)),
            ('(\\$\\{(%)?)(.*?)((!)(.*?))?((?(2)%)\\})', bygroups(Punctuation, None, using(PythonLexer), Name.Builtin, None, None, Punctuation)),
            ('#', Other)],
        'comment': [
            ('[^\\]#]', Comment.Multiline),
            ('#\\[', Comment.Multiline, '#push'),
            ('\\]#', Comment.Multiline, '#pop'),
            ('[\\]#]', Comment.Multiline)] }
    
    def analyse_text(text):
        '''Evoque templates use $evoque, which is unique.'''
        if '$evoque' in text:
            return 1



class EvoqueHtmlLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class EvoqueXmlLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class ColdfusionLexer(RegexLexer):
    '''
    Coldfusion statements
    '''
    name = 'cfstatement'
    aliases = [
        'cfs']
    filenames = []
    mimetypes = []
    url = 'https://www.adobe.com/products/coldfusion-family.html'
    version_added = ''
    flags = re.IGNORECASE
    tokens = {
        'root': [
            ('//.*?\\n', Comment.Single),
            ('/\\*(?:.|\\n)*?\\*/', Comment.Multiline),
            ('\\+\\+|--', Operator),
            ('[-+*/^&=!]', Operator),
            ('<=|>=|<|>|==', Operator),
            ('mod\\b', Operator),
            ('(eq|lt|gt|lte|gte|not|is|and|or)\\b', Operator),
            ('\\|\\||&&', Operator),
            ('\\?', Operator),
            ('"', String.Double, 'string'),
            ("'.*?'", String.Single),
            ('\\d+', Number),
            ('(if|else|len|var|xml|default|break|switch|component|property|function|do|try|catch|in|continue|for|return|while|required|any|array|binary|boolean|component|date|guid|numeric|query|string|struct|uuid|case)\\b', Keyword),
            ('(true|false|null)\\b', Keyword.Constant),
            ('(application|session|client|cookie|super|this|variables|arguments)\\b', Name.Constant),
            ('([a-z_$][\\w.]*)(\\s*)(\\()', bygroups(Name.Function, Text, Punctuation)),
            ('[a-z_$][\\w.]*', Name.Variable),
            ('[()\\[\\]{};:,.\\\\]', Punctuation),
            ('\\s+', Text)],
        'string': [
            ('""', String.Double),
            ('#.+?#', String.Interp),
            ('[^"#]+', String.Double),
            ('#', String.Double),
            ('"', String.Double, '#pop')] }


class ColdfusionMarkupLexer(RegexLexer):
    '''
    Coldfusion markup only
    '''
    name = 'Coldfusion'
    aliases = [
        'cf']
    filenames = []
    mimetypes = []
    url = 'https://www.adobe.com/products/coldfusion-family.html'
    tokens = {
        'root': [
            ('[^<]+', Other),
            include('tags'),
            ('<[^<>]*', Other)],
        'tags': [
            ('<!---', Comment.Multiline, 'cfcomment'),
            ('(?s)<!--.*?-->', Comment),
            ('<cfoutput.*?>', Name.Builtin, 'cfoutput'),
            ('(?s)(<cfscript.*?>)(.+?)(</cfscript.*?>)', bygroups(Name.Builtin, using(ColdfusionLexer), Name.Builtin)),
            ('(?s)(</?cf(?:component|include|if|else|elseif|loop|return|dbinfo|dump|abort|location|invoke|throw|file|savecontent|mailpart|mail|header|content|zip|image|lock|argument|try|catch|break|directory|http|set|function|param)\\b)(.*?)((?<!\\\\)>)', bygroups(Name.Builtin, using(ColdfusionLexer), Name.Builtin))],
        'cfoutput': [
            ('[^#<]+', Other),
            ('(#)(.*?)(#)', bygroups(Punctuation, using(ColdfusionLexer), Punctuation)),
            ('</cfoutput.*?>', Name.Builtin, '#pop'),
            include('tags'),
            ('(?s)<[^<>]*', Other),
            ('#', Other)],
        'cfcomment': [
            ('<!---', Comment.Multiline, '#push'),
            ('--->', Comment.Multiline, '#pop'),
            ('([^<-]|<(?!!---)|-(?!-->))+', Comment.Multiline)] }


class ColdfusionHtmlLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class ColdfusionCFCLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class SspLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class TeaTemplateRootLexer(RegexLexer):
    '''
    Base for the `TeaTemplateLexer`. Yields `Token.Other` for area outside of
    code blocks.

    .. versionadded:: 1.5
    '''
    tokens = {
        'root': [
            ('<%\\S?', Keyword, 'sec'),
            ('[^<]+', Other),
            ('<', Other)],
        'sec': [
            ('%>', Keyword, '#pop'),
            ('[\\w\\W]+?(?=%>|\\Z)', using(TeaLangLexer))] }


class TeaTemplateLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class LassoHtmlLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class LassoXmlLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class LassoCssLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class LassoJavascriptLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class HandlebarsLexer(RegexLexer):
    '''
    Generic handlebars template lexer.

    Highlights only the Handlebars template tags (stuff between `{{` and `}}`).
    Everything else is left for a delegating lexer.
    '''
    name = 'Handlebars'
    url = 'https://handlebarsjs.com/'
    aliases = [
        'handlebars']
    version_added = '2.0'
    tokens = {
        'root': [
            ('[^{]+', Other),
            ('\\{\\{!.*\\}\\}', Comment),
            ('(\\{\\{\\{)(\\s*)', bygroups(Comment.Special, Text), 'tag'),
            ('(\\{\\{)([#~/]+)([^\\s}]*)', bygroups(Comment.Preproc, Number.Attribute, Number.Attribute), 'tag'),
            ('(\\{\\{)(\\s*)', bygroups(Comment.Preproc, Text), 'tag')],
        'tag': [
            ('\\s+', Text),
            ('\\}\\}\\}', Comment.Special, '#pop'),
            ('(~?)(\\}\\})', bygroups(Number, Comment.Preproc), '#pop'),
            ('([^\\s}]+)(=)', bygroups(Name.Attribute, Operator)),
            ('(>)(\\s*)(@partial-block)', bygroups(Keyword, Text, Keyword)),
            ('(#?>)(\\s*)([\\w-]+)', bygroups(Keyword, Text, Name.Variable)),
            ('(>)(\\s*)(\\()', bygroups(Keyword, Text, Punctuation), 'dynamic-partial'),
            include('generic')],
        'dynamic-partial': [
            ('\\s+', Text),
            ('\\)', Punctuation, '#pop'),
            ('(lookup)(\\s+)(\\.|this)(\\s+)', bygroups(Keyword, Text, Name.Variable, Text)),
            ('(lookup)(\\s+)(\\S+)', bygroups(Keyword, Text, using(this, state = 'variable'))),
            ('[\\w-]+', Name.Function),
            include('generic')],
        'variable': [
            ('[()/@a-zA-Z][\\w-]*', Name.Variable),
            ('\\.[\\w-]+', Name.Variable),
            ('(this\\/|\\.\\/|(\\.\\.\\/)+)[\\w-]+', Name.Variable)],
        'generic': [
            include('variable'),
            (':?"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Double),
            (":?'(\\\\\\\\|\\\\[^\\\\]|[^'\\\\])*'", String.Single),
            ('[0-9](\\.[0-9]*)?(eE[+-][0-9])?[flFLdD]?|0[xX][0-9a-fA-F]+[Ll]?', Number)] }


class HandlebarsHtmlLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class YamlJinjaLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class LiquidLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'LiquidLexer'
    __doc__ = '\n    Lexer for Liquid templates.\n    '
    name = 'liquid'
    url = 'https://www.rubydoc.info/github/Shopify/liquid'
    aliases = [
        'liquid']
    filenames = [
        '*.liquid']
    version_added = '2.0'
# WARNING: Decompyle incomplete


class TwigLexer(RegexLexer):
    '''
    Twig template lexer.

    It just highlights Twig code between the preprocessor directives,
    other data is left untouched by the lexer.
    '''
    name = 'Twig'
    aliases = [
        'twig']
    mimetypes = [
        'application/x-twig']
    url = 'https://twig.symfony.com'
    version_added = '2.0'
    flags = re.M | re.S
    _ident_char = '[\\\\\\w-]|[^\\x00-\\x7f]'
    _ident_begin = '(?:[\\\\_a-z]|[^\\x00-\\x7f])'
    _ident_end = '(?:' + _ident_char + ')*'
    _ident_inner = _ident_begin + _ident_end
    tokens = {
        'root': [
            ('[^{]+', Other),
            ('\\{\\{', Comment.Preproc, 'var'),
            ('\\{\\#.*?\\#\\}', Comment),
            ('(\\{%)(-?\\s*)(raw)(\\s*-?)(%\\})(.*?)(\\{%)(-?\\s*)(endraw)(\\s*-?)(%\\})', bygroups(Comment.Preproc, Text, Keyword, Text, Comment.Preproc, Other, Comment.Preproc, Text, Keyword, Text, Comment.Preproc)),
            ('(\\{%)(-?\\s*)(verbatim)(\\s*-?)(%\\})(.*?)(\\{%)(-?\\s*)(endverbatim)(\\s*-?)(%\\})', bygroups(Comment.Preproc, Text, Keyword, Text, Comment.Preproc, Other, Comment.Preproc, Text, Keyword, Text, Comment.Preproc)),
            (f'''(\\{{%)(-?\\s*)(filter)(\\s+)({_ident_inner})''', bygroups(Comment.Preproc, Text, Keyword, Text, Name.Function), 'tag'),
            ('(\\{%)(-?\\s*)([a-zA-Z_]\\w*)', bygroups(Comment.Preproc, Text, Keyword), 'tag'),
            ('\\{', Other)],
        'varnames': [
            (f'''(\\|)(\\s*)({_ident_inner})''', bygroups(Operator, Text, Name.Function)),
            (f'''(is)(\\s+)(not)?(\\s*)({_ident_inner})''', bygroups(Keyword, Text, Keyword, Text, Name.Function)),
            ('(?i)(true|false|none|null)\\b', Keyword.Pseudo),
            ('(in|not|and|b-and|or|b-or|b-xor|isif|elseif|else|importconstant|defined|divisibleby|empty|even|iterable|odd|sameasmatches|starts\\s+with|ends\\s+with)\\b', Keyword),
            ('(loop|block|parent)\\b', Name.Builtin),
            (_ident_inner, Name.Variable),
            ('\\.' + _ident_inner, Name.Variable),
            ('\\.[0-9]+', Number),
            (':?"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Double),
            (":?'(\\\\\\\\|\\\\[^\\\\]|[^'\\\\])*'", String.Single),
            ('([{}()\\[\\]+\\-*/,:~%]|\\.\\.|\\?|:|\\*\\*|\\/\\/|!=|[><=]=?)', Operator),
            ('[0-9](\\.[0-9]*)?(eE[+-][0-9])?[flFLdD]?|0[xX][0-9a-fA-F]+[Ll]?', Number)],
        'var': [
            ('\\s+', Text),
            ('(-?)(\\}\\})', bygroups(Text, Comment.Preproc), '#pop'),
            include('varnames')],
        'tag': [
            ('\\s+', Text),
            ('(-?)(%\\})', bygroups(Text, Comment.Preproc), '#pop'),
            include('varnames'),
            ('.', Punctuation)] }


class TwigHtmlLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class Angular2Lexer(RegexLexer):
    """
    Generic angular2 template lexer.

    Highlights only the Angular template tags (stuff between `{{` and `}}` and
    special attributes: '(event)=', '[property]=', '[(twoWayBinding)]=').
    Everything else is left for a delegating lexer.
    """
    name = 'Angular2'
    url = 'https://angular.io/guide/template-syntax'
    aliases = [
        'ng2']
    version_added = '2.1'
    tokens = {
        'root': [
            ('[^{([*#]+', Other),
            ('(\\{\\{)(\\s*)', bygroups(Comment.Preproc, Text), 'ngExpression'),
            ('([([]+)([\\w:.-]+)([\\])]+)(\\s*)(=)(\\s*)', bygroups(Punctuation, Name.Attribute, Punctuation, Text, Operator, Text), 'attr'),
            ('([([]+)([\\w:.-]+)([\\])]+)(\\s*)', bygroups(Punctuation, Name.Attribute, Punctuation, Text)),
            ('([*#])([\\w:.-]+)(\\s*)(=)(\\s*)', bygroups(Punctuation, Name.Attribute, Text, Operator, Text), 'attr'),
            ('([*#])([\\w:.-]+)(\\s*)', bygroups(Punctuation, Name.Attribute, Text))],
        'ngExpression': [
            ('\\s+(\\|\\s+)?', Text),
            ('\\}\\}', Comment.Preproc, '#pop'),
            (':?(true|false)', String.Boolean),
            (':?"(\\\\\\\\|\\\\[^\\\\]|[^"\\\\])*"', String.Double),
            (":?'(\\\\\\\\|\\\\[^\\\\]|[^'\\\\])*'", String.Single),
            ('[0-9](\\.[0-9]*)?(eE[+-][0-9])?[flFLdD]?|0[xX][0-9a-fA-F]+[Ll]?', Number),
            ('[a-zA-Z][\\w-]*(\\(.*\\))?', Name.Variable),
            ('\\.[\\w-]+(\\(.*\\))?', Name.Variable),
            ('(\\?)(\\s*)([^}\\s]+)(\\s*)(:)(\\s*)([^}\\s]+)(\\s*)', bygroups(Operator, Text, String, Text, Operator, Text, String, Text))],
        'attr': [
            ('".*?"', String, '#pop'),
            ("'.*?'", String, '#pop'),
            ('[^\\s>]+', String, '#pop')] }


class Angular2HtmlLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete


class SqlJinjaLexer(DelegatingLexer):
    pass
# WARNING: Decompyle incomplete
