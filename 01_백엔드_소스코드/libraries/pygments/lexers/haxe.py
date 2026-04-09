# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: haxe.pyc (Python 3.11)

'''
    pygments.lexers.haxe
    ~~~~~~~~~~~~~~~~~~~~

    Lexers for Haxe and related stuff.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import ExtendedRegexLexer, RegexLexer, include, bygroups, default
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Generic, Whitespace
__all__ = [
    'HaxeLexer',
    'HxmlLexer']

class HaxeLexer(ExtendedRegexLexer):
    __module__ = __name__
    __qualname__ = 'HaxeLexer'
    __doc__ = '\n    For Haxe source code.\n    '
    name = 'Haxe'
    url = 'http://haxe.org/'
    aliases = [
        'haxe',
        'hxsl',
        'hx']
    filenames = [
        '*.hx',
        '*.hxsl']
    mimetypes = [
        'text/haxe',
        'text/x-haxe',
        'text/x-hx']
    version_added = '1.3'
    keyword = '(?:function|class|static|var|if|else|while|do|for|break|return|continue|extends|implements|import|switch|case|default|public|private|try|untyped|catch|new|this|throw|extern|enum|in|interface|cast|override|dynamic|typedef|package|inline|using|null|true|false|abstract)\\b'
    typeid = '_*[A-Z]\\w*'
    ident = '(?:_*[a-z]\\w*|_+[0-9]\\w*|' + typeid + '|_+|\\$\\w+)'
    binop = '(?:%=|&=|\\|=|\\^=|\\+=|\\-=|\\*=|/=|<<=|>\\s*>\\s*=|>\\s*>\\s*>\\s*=|==|!=|<=|>\\s*=|&&|\\|\\||<<|>>>|>\\s*>|\\.\\.\\.|<|>|%|&|\\||\\^|\\+|\\*|/|\\-|=>|=)'
    ident_no_keyword = '(?!' + keyword + ')' + ident
    flags = re.DOTALL | re.MULTILINE
    preproc_stack = []
    
    def preproc_callback(self, match, ctx):
        pass
    # WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete


class HxmlLexer(RegexLexer):
    '''
    Lexer for haXe build files.
    '''
    name = 'Hxml'
    url = 'https://haxe.org/manual/compiler-usage-hxml.html'
    aliases = [
        'haxeml',
        'hxml']
    filenames = [
        '*.hxml']
    version_added = '1.6'
    tokens = {
        'root': [
            ('(--)(next)', bygroups(Punctuation, Generic.Heading)),
            ('(-)(prompt|debug|v)', bygroups(Punctuation, Keyword.Keyword)),
            ('(--)(neko-source|flash-strict|flash-use-stage|no-opt|no-traces|no-inline|times|no-output)', bygroups(Punctuation, Keyword)),
            ('(-)(cpp|js|neko|x|as3|swf9?|swf-lib|php|xml|main|lib|D|resource|cp|cmd)( +)(.+)', bygroups(Punctuation, Keyword, Whitespace, String)),
            ('(-)(swf-version)( +)(\\d+)', bygroups(Punctuation, Keyword, Whitespace, Number.Integer)),
            ('(-)(swf-header)( +)(\\d+)(:)(\\d+)(:)(\\d+)(:)([A-Fa-f0-9]{6})', bygroups(Punctuation, Keyword, Whitespace, Number.Integer, Punctuation, Number.Integer, Punctuation, Number.Integer, Punctuation, Number.Hex)),
            ('(--)(js-namespace|php-front|php-lib|remap|gen-hx-classes)( +)(.+)', bygroups(Punctuation, Keyword, Whitespace, String)),
            ('#.*', Comment.Single)] }
