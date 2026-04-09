# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rebol.pyc (Python 3.11)

'''
    pygments.lexers.rebol
    ~~~~~~~~~~~~~~~~~~~~~

    Lexers for the REBOL and related languages.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import RegexLexer, bygroups
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Generic, Whitespace
__all__ = [
    'RebolLexer',
    'RedLexer']

class RebolLexer(RegexLexer):
    '''
    A REBOL lexer.
    '''
    name = 'REBOL'
    aliases = [
        'rebol']
    filenames = [
        '*.r',
        '*.r3',
        '*.reb']
    mimetypes = [
        'text/x-rebol']
    url = 'http://www.rebol.com'
    version_added = '1.1'
    flags = re.IGNORECASE | re.MULTILINE
    escape_re = '(?:\\^\\([0-9a-f]{1,4}\\)*)'
    
    def word_callback(lexer, match):
        pass
    # WARNING: Decompyle incomplete

    tokens = {
        'root': [][('\\s+', Text)][('#"', String.Char, 'char')][('#\\{[0-9a-f]*\\}', Number.Hex)][('2#\\{', Number.Hex, 'bin2')][('64#\\{[0-9a-z+/=\\s]*\\}', Number.Hex)][('"', String, 'string')][('\\{', String, 'string2')][(';#+.*\\n', Comment.Special)][(';\\*+.*\\n', Comment.Preproc)][(';.*\\n', Comment)][('%"', Name.Decorator, 'stringFile')][('%[^(^{")\\s\\[\\]]+', Name.Decorator)][('[+-]?([a-z]{1,3})?\\$\\d+(\\.\\d+)?', Number.Float)][('[+-]?\\d+\\:\\d+(\\:\\d+)?(\\.\\d+)?', String.Other)][('\\d+[\\-/][0-9a-z]+[\\-/]\\d+(\\/\\d+\\:\\d+((\\:\\d+)?([.\\d+]?([+-]?\\d+:\\d+)?)?)?)?', String.Other)][('\\d+(\\.\\d+)+\\.\\d+', Keyword.Constant)][('\\d+X\\d+', Keyword.Constant)][("[+-]?\\d+(\\'\\d+)?([.,]\\d*)?E[+-]?\\d+", Number.Float)][("[+-]?\\d+(\\'\\d+)?[.,]\\d*", Number.Float)][("[+-]?\\d+(\\'\\d+)?", Number)][('[\\[\\]()]', Generic.Strong)][('[a-z]+[^(^{"\\s:)]*://[^(^{"\\s)]*', Name.Decorator)][('mailto:[^(^{"@\\s)]+@[^(^{"@\\s)]+', Name.Decorator)][('[^(^{"@\\s)]+@[^(^{"@\\s)]+', Name.Decorator)][('comment\\s"', Comment, 'commentString1')][('comment\\s\\{', Comment, 'commentString2')][('comment\\s\\[', Comment, 'commentBlock')][('comment\\s[^(\\s{"\\[]+', Comment)][('/[^(^{")\\s/[\\]]*', Name.Attribute)][('([^(^{")\\s/[\\]]+)(?=[:({"\\s/\\[\\]])', word_callback)][('<[\\w:.-]*>', Name.Tag)][('<[^(<>\\s")]+', Name.Tag, 'tag')][('([^(^{")\\s]+)', Text)],
        'string': [
            ('[^(^")]+', String),
            (escape_re, String.Escape),
            ('[(|)]+', String),
            ('\\^.', String.Escape),
            ('"', String, '#pop')],
        'string2': [
            ('[^(^{})]+', String),
            (escape_re, String.Escape),
            ('[(|)]+', String),
            ('\\^.', String.Escape),
            ('\\{', String, '#push'),
            ('\\}', String, '#pop')],
        'stringFile': [
            ('[^(^")]+', Name.Decorator),
            (escape_re, Name.Decorator),
            ('\\^.', Name.Decorator),
            ('"', Name.Decorator, '#pop')],
        'char': [
            (escape_re + '"', String.Char, '#pop'),
            ('\\^."', String.Char, '#pop'),
            ('."', String.Char, '#pop')],
        'tag': [
            (escape_re, Name.Tag),
            ('"', Name.Tag, 'tagString'),
            ('[^(<>\\r\\n")]+', Name.Tag),
            ('>', Name.Tag, '#pop')],
        'tagString': [
            ('[^(^")]+', Name.Tag),
            (escape_re, Name.Tag),
            ('[(|)]+', Name.Tag),
            ('\\^.', Name.Tag),
            ('"', Name.Tag, '#pop')],
        'tuple': [
            ('(\\d+\\.)+', Keyword.Constant),
            ('\\d+', Keyword.Constant, '#pop')],
        'bin2': [
            ('\\s+', Number.Hex),
            ('([01]\\s*){8}', Number.Hex),
            ('\\}', Number.Hex, '#pop')],
        'commentString1': [
            ('[^(^")]+', Comment),
            (escape_re, Comment),
            ('[(|)]+', Comment),
            ('\\^.', Comment),
            ('"', Comment, '#pop')],
        'commentString2': [
            ('[^(^{})]+', Comment),
            (escape_re, Comment),
            ('[(|)]+', Comment),
            ('\\^.', Comment),
            ('\\{', Comment, '#push'),
            ('\\}', Comment, '#pop')],
        'commentBlock': [
            ('\\[', Comment, '#push'),
            ('\\]', Comment, '#pop'),
            ('"', Comment, 'commentString1'),
            ('\\{', Comment, 'commentString2'),
            ('[^(\\[\\]"{)]+', Comment)] }
    
    def analyse_text(text):
        '''
        Check if code contains REBOL header and so it probably not R code
        '''
        if re.match('^\\s*REBOL\\s*\\[', text, re.IGNORECASE):
            return 1
        if None.search('\\s*REBOL\\s*\\[', text, re.IGNORECASE):
            return 0.5



class RedLexer(RegexLexer):
    '''
    A Red-language lexer.
    '''
    name = 'Red'
    aliases = [
        'red',
        'red/system']
    filenames = [
        '*.red',
        '*.reds']
    mimetypes = [
        'text/x-red',
        'text/x-red-system']
    url = 'https://www.red-lang.org'
    version_added = '2.0'
    flags = re.IGNORECASE | re.MULTILINE
    escape_re = '(?:\\^\\([0-9a-f]{1,4}\\)*)'
    
    def word_callback(lexer, match):
        pass
    # WARNING: Decompyle incomplete

    tokens = {
        'root': [][('\\s+', Text)][('#"', String.Char, 'char')][('#\\{[0-9a-f\\s]*\\}', Number.Hex)][('2#\\{', Number.Hex, 'bin2')][('64#\\{[0-9a-z+/=\\s]*\\}', Number.Hex)][('([0-9a-f]+)(h)((\\s)|(?=[\\[\\]{}"()]))', bygroups(Number.Hex, Name.Variable, Whitespace))][('"', String, 'string')][('\\{', String, 'string2')][(';#+.*\\n', Comment.Special)][(';\\*+.*\\n', Comment.Preproc)][(';.*\\n', Comment)][('%"', Name.Decorator, 'stringFile')][('%[^(^{")\\s\\[\\]]+', Name.Decorator)][('[+-]?([a-z]{1,3})?\\$\\d+(\\.\\d+)?', Number.Float)][('[+-]?\\d+\\:\\d+(\\:\\d+)?(\\.\\d+)?', String.Other)][('\\d+[\\-/][0-9a-z]+[\\-/]\\d+(/\\d+:\\d+((:\\d+)?([\\.\\d+]?([+-]?\\d+:\\d+)?)?)?)?', String.Other)][('\\d+(\\.\\d+)+\\.\\d+', Keyword.Constant)][('\\d+X\\d+', Keyword.Constant)][("[+-]?\\d+(\\'\\d+)?([.,]\\d*)?E[+-]?\\d+", Number.Float)][("[+-]?\\d+(\\'\\d+)?[.,]\\d*", Number.Float)][("[+-]?\\d+(\\'\\d+)?", Number)][('[\\[\\]()]', Generic.Strong)][('[a-z]+[^(^{"\\s:)]*://[^(^{"\\s)]*', Name.Decorator)][('mailto:[^(^{"@\\s)]+@[^(^{"@\\s)]+', Name.Decorator)][('[^(^{"@\\s)]+@[^(^{"@\\s)]+', Name.Decorator)][('comment\\s"', Comment, 'commentString1')][('comment\\s\\{', Comment, 'commentString2')][('comment\\s\\[', Comment, 'commentBlock')][('comment\\s[^(\\s{"\\[]+', Comment)][('/[^(^{^")\\s/[\\]]*', Name.Attribute)][('([^(^{^")\\s/[\\]]+)(?=[:({"\\s/\\[\\]])', word_callback)][('<[\\w:.-]*>', Name.Tag)][('<[^(<>\\s")]+', Name.Tag, 'tag')][('([^(^{")\\s]+)', Text)],
        'string': [
            ('[^(^")]+', String),
            (escape_re, String.Escape),
            ('[(|)]+', String),
            ('\\^.', String.Escape),
            ('"', String, '#pop')],
        'string2': [
            ('[^(^{})]+', String),
            (escape_re, String.Escape),
            ('[(|)]+', String),
            ('\\^.', String.Escape),
            ('\\{', String, '#push'),
            ('\\}', String, '#pop')],
        'stringFile': [
            ('[^(^")]+', Name.Decorator),
            (escape_re, Name.Decorator),
            ('\\^.', Name.Decorator),
            ('"', Name.Decorator, '#pop')],
        'char': [
            (escape_re + '"', String.Char, '#pop'),
            ('\\^."', String.Char, '#pop'),
            ('."', String.Char, '#pop')],
        'tag': [
            (escape_re, Name.Tag),
            ('"', Name.Tag, 'tagString'),
            ('[^(<>\\r\\n")]+', Name.Tag),
            ('>', Name.Tag, '#pop')],
        'tagString': [
            ('[^(^")]+', Name.Tag),
            (escape_re, Name.Tag),
            ('[(|)]+', Name.Tag),
            ('\\^.', Name.Tag),
            ('"', Name.Tag, '#pop')],
        'tuple': [
            ('(\\d+\\.)+', Keyword.Constant),
            ('\\d+', Keyword.Constant, '#pop')],
        'bin2': [
            ('\\s+', Number.Hex),
            ('([01]\\s*){8}', Number.Hex),
            ('\\}', Number.Hex, '#pop')],
        'commentString1': [
            ('[^(^")]+', Comment),
            (escape_re, Comment),
            ('[(|)]+', Comment),
            ('\\^.', Comment),
            ('"', Comment, '#pop')],
        'commentString2': [
            ('[^(^{})]+', Comment),
            (escape_re, Comment),
            ('[(|)]+', Comment),
            ('\\^.', Comment),
            ('\\{', Comment, '#push'),
            ('\\}', Comment, '#pop')],
        'commentBlock': [
            ('\\[', Comment, '#push'),
            ('\\]', Comment, '#pop'),
            ('"', Comment, 'commentString1'),
            ('\\{', Comment, 'commentString2'),
            ('[^(\\[\\]"{)]+', Comment)] }
