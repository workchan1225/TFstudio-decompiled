# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: csound.pyc (Python 3.11)

'''
    pygments.lexers.csound
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexers for Csound languages.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import RegexLexer, bygroups, default, include, using, words
from pygments.token import Comment, Error, Keyword, Name, Number, Operator, Punctuation, String, Text, Whitespace
from pygments.lexers._csound_builtins import OPCODES, DEPRECATED_OPCODES, REMOVED_OPCODES
from pygments.lexers.html import HtmlLexer
from pygments.lexers.python import PythonLexer
from pygments.lexers.scripting import LuaLexer
__all__ = [
    'CsoundScoreLexer',
    'CsoundOrchestraLexer',
    'CsoundDocumentLexer']
newline = ('((?:(?:;|//).*)*)(\\n)', bygroups(Comment.Single, Text))

class CsoundLexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'CsoundLexer'
    url = 'https://csound.com/'
# WARNING: Decompyle incomplete


class CsoundScoreLexer(CsoundLexer):
    '''
    For `Csound <https://csound.com>`_ scores.
    '''
    name = 'Csound Score'
    aliases = [
        'csound-score',
        'csound-sco']
    filenames = [
        '*.sco']
    version_added = '2.1'
    tokens = {
        'root': [
            ('\\n', Whitespace),
            include('whitespace and macro uses'),
            include('preprocessor directives'),
            ('[aBbCdefiqstvxy]', Keyword),
            ('z', Keyword.Constant),
            ('([nNpP][pP])(\\d+)', bygroups(Keyword, Number.Integer)),
            ('[mn]', Keyword, 'mark statement'),
            include('numbers'),
            ('[!+\\-*/^%&|<>#~.]', Operator),
            ('[()\\[\\]]', Punctuation),
            ('"', String, 'quoted string'),
            ('\\{', Comment.Preproc, 'loop after left brace')],
        'mark statement': [
            include('whitespace and macro uses'),
            ('[A-Z_a-z]\\w*', Name.Label),
            ('\\n', Whitespace, '#pop')],
        'loop after left brace': [
            include('whitespace and macro uses'),
            ('\\d+', Number.Integer, ('#pop', 'loop after repeat count'))],
        'loop after repeat count': [
            include('whitespace and macro uses'),
            ('[A-Z_a-z]\\w*', Comment.Preproc, ('#pop', 'loop'))],
        'loop': [
            ('\\}', Comment.Preproc, '#pop'),
            include('root')],
        'braced string': [
            ('\\}\\}', String, '#pop'),
            ('[^}]|\\}(?!\\})', String)] }


class CsoundOrchestraLexer(CsoundLexer):
    __module__ = __name__
    __qualname__ = 'CsoundOrchestraLexer'
    __doc__ = '\n    For `Csound <https://csound.com>`_ orchestras.\n    '
    name = 'Csound Orchestra'
    aliases = [
        'csound',
        'csound-orc']
    filenames = [
        '*.orc',
        '*.udo']
    version_added = '2.1'
    user_defined_opcodes = set()
    
    def opcode_name_callback(lexer, match):
        pass
    # WARNING: Decompyle incomplete

    
    def name_callback(lexer, match):
        pass
    # WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete


class CsoundDocumentLexer(RegexLexer):
    '''
    For Csound documents.
    '''
    name = 'Csound Document'
    aliases = [
        'csound-document',
        'csound-csd']
    filenames = [
        '*.csd']
    url = 'https://csound.com'
    version_added = '2.1'
    tokens = {
        'root': [
            ('/[*](.|\\n)*?[*]/', Comment.Multiline),
            ('(?:;|//).*$', Comment.Single),
            ('[^/;<]+|/(?!/)', Text),
            ('<\\s*CsInstruments', Name.Tag, ('orchestra', 'tag')),
            ('<\\s*CsScore', Name.Tag, ('score', 'tag')),
            ('<\\s*[Hh][Tt][Mm][Ll]', Name.Tag, ('HTML', 'tag')),
            ('<\\s*[\\w:.-]+', Name.Tag, 'tag'),
            ('<\\s*/\\s*[\\w:.-]+\\s*>', Name.Tag)],
        'orchestra': [
            ('<\\s*/\\s*CsInstruments\\s*>', Name.Tag, '#pop'),
            ('(.|\\n)+?(?=<\\s*/\\s*CsInstruments\\s*>)', using(CsoundOrchestraLexer))],
        'score': [
            ('<\\s*/\\s*CsScore\\s*>', Name.Tag, '#pop'),
            ('(.|\\n)+?(?=<\\s*/\\s*CsScore\\s*>)', using(CsoundScoreLexer))],
        'HTML': [
            ('<\\s*/\\s*[Hh][Tt][Mm][Ll]\\s*>', Name.Tag, '#pop'),
            ('(.|\\n)+?(?=<\\s*/\\s*[Hh][Tt][Mm][Ll]\\s*>)', using(HtmlLexer))],
        'tag': [
            ('\\s+', Whitespace),
            ('[\\w.:-]+\\s*=', Name.Attribute, 'attr'),
            ('/?\\s*>', Name.Tag, '#pop')],
        'attr': [
            ('\\s+', Whitespace),
            ('".*?"', String, '#pop'),
            ("'.*?'", String, '#pop'),
            ('[^\\s>]+', String, '#pop')] }
