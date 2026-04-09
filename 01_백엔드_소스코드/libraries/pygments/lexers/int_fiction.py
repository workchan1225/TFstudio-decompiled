# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: int_fiction.pyc (Python 3.11)

'''
    pygments.lexers.int_fiction
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for interactive fiction languages.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import RegexLexer, include, bygroups, using, this, default, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Error, Generic
__all__ = [
    'Inform6Lexer',
    'Inform6TemplateLexer',
    'Inform7Lexer',
    'Tads3Lexer']

class Inform6Lexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'Inform6Lexer'
    __doc__ = '\n    For Inform 6 source code.\n    '
    name = 'Inform 6'
    url = 'http://inform-fiction.org/'
    aliases = [
        'inform6',
        'i6']
    filenames = [
        '*.inf']
    version_added = '2.0'
    flags = re.MULTILINE | re.DOTALL
    _name = '[a-zA-Z_]\\w*'
    _dash = '\\-‐-—'
    _dquote = '"“”'
    _squote = "'‘’"
    _newline = '\\n  '
# WARNING: Decompyle incomplete


class Inform7Lexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'Inform7Lexer'
    __doc__ = '\n    For Inform 7 source code.\n    '
    name = 'Inform 7'
    url = 'http://inform7.com/'
    aliases = [
        'inform7',
        'i7']
    filenames = [
        '*.ni',
        '*.i7x']
    version_added = '2.0'
    flags = re.MULTILINE | re.DOTALL
    _dash = Inform6Lexer._dash
    _dquote = Inform6Lexer._dquote
    _newline = Inform6Lexer._newline
    _start = f'''\\A|(?<=[{_newline}])'''
    tokens = { }
    token_variants = [
        '+i6t-not-inline',
        '+i6t-inline',
        '+i6t-use-option']
# WARNING: Decompyle incomplete


class Inform6TemplateLexer(Inform7Lexer):
    '''
    For Inform 6 template code.
    '''
    name = 'Inform 6 template'
    aliases = [
        'i6t']
    filenames = [
        '*.i6t']
    version_added = '2.0'
    
    def get_tokens_unprocessed(self, text, stack = (('+i6t-root',),)):
        return Inform7Lexer.get_tokens_unprocessed(self, text, stack)



class Tads3Lexer(RegexLexer):
    __module__ = __name__
    __qualname__ = 'Tads3Lexer'
    __doc__ = '\n    For TADS 3 source code.\n    '
    name = 'TADS 3'
    aliases = [
        'tads3']
    filenames = [
        '*.t']
    url = 'https://www.tads.org'
    version_added = ''
    flags = re.DOTALL | re.MULTILINE
    _comment_single = '(?://(?:[^\\\\\\n]|\\\\+[\\w\\W])*$)'
    _comment_multiline = '(?:/\\*(?:[^*]|\\*(?!/))*\\*/)'
    _escape = '(?:\\\\(?:[\\n\\\\<>"\\\'^v bnrt]|u[\\da-fA-F]{,4}|x[\\da-fA-F]{,2}|[0-3]?[0-7]{1,2}))'
    _name = '(?:[_a-zA-Z]\\w*)'
    _no_quote = '(?=\\s|\\\\?>)'
    _operator = '(?:&&|\\|\\||\\+\\+|--|\\?\\?|::|[.,@\\[\\]~]|(?:[=+\\-*/%!&|^]|<<?|>>?>?)=?)'
    _ws = f'''(?:\\\\|\\s|{_comment_single}|{_comment_multiline})'''
    _ws_pp = f'''(?:\\\\\\n|[^\\S\\n]|{_comment_single}|{_comment_multiline})'''
    
    def _make_string_state(triple, double, verbatim, _escape = (None, _escape)):
        if verbatim:
            verbatim = (lambda .0: [ f'''(?:{re.escape(c.lower())}|{re.escape(c.upper())})''' for c in .0 ])(verbatim())
        char = '"' if double else "'"
        token = String.Double if double else String.Single
        escaped_quotes = f'''+|{char}(?!{char}{{2}})''' if triple else ''
        prefix = '{}{}'.format('t' if triple else '', 'd' if double else 's')
        tag_state_name = f'''{prefix}qt'''
        state = []
        state += [
            include('s/verbatim'),
            (f'''[^\\\\<&{{}}{char}]+''', token)]
        state += [
            include('s/escape'),
            (f'''\\{{([^}}<\\\\{char}]|<(?!<)|\\\\{char}{escaped_quotes}|{_escape}|\\\\.)*\\}}''', String.Interpol),
            ('[\\\\&{}<]', token)]
        return state

    
    def _make_tag_state(triple, double, _escape = (_escape,)):
        char = '"' if double else "'"
        quantifier = '{3,}' if triple else ''
        state_name = '{}{}qt'.format('t' if triple else '', 'd' if double else 's')
        token = String.Double if double else String.Single
        escaped_quotes = f'''+|{char}(?!{char}{{2}})''' if triple else ''
        return [
            (f'''{char}{quantifier}''', token, '#pop:2'),
            ('(\\s|\\\\\\n)+', Text),
            ('(=)(\\\\?")', bygroups(Punctuation, String.Double), f'''dqs/{state_name}'''),
            ("(=)(\\\\?')", bygroups(Punctuation, String.Single), f'''sqs/{state_name}'''),
            ('=', Punctuation, f'''uqs/{state_name}'''),
            ('\\\\?>', Name.Tag, '#pop'),
            (f'''\\{{([^}}<\\\\{char}]|<(?!<)|\\\\{char}{escaped_quotes}|{_escape}|\\\\.)*\\}}''', String.Interpol),
            (f'''([^\\s=><\\\\{char}]|<(?!<)|\\\\{char}{escaped_quotes}|{_escape}|\\\\.)+''', Name.Attribute),
            include('s/escape'),
            include('s/verbatim'),
            include('s/entity'),
            ('[\\\\{}&]', Name.Attribute)]

    
    def _make_attribute_value_state(terminator, host_triple, host_double, _escape = (_escape,)):
        if terminator == '"':
            pass
        elif terminator == "'":
            pass
        
        token = String.Other
        host_char = '"' if host_double else "'"
        host_quantifier = '{3,}' if host_triple else ''
        host_token = String.Double if host_double else String.Single
        escaped_quotes = f'''+|{host_char}(?!{host_char}{{2}})''' if host_triple else ''
        return [
            (f'''{host_char}{host_quantifier}''', host_token, '#pop:3'),
            ('{}{}'.format('' if token is String.Other else '\\\\?', terminator), token, '#pop'),
            include('s/verbatim'),
            include('s/entity'),
            (f'''\\{{([^}}<\\\\{host_char}]|<(?!<)|\\\\{host_char}{escaped_quotes}|{_escape}|\\\\.)*\\}}''', String.Interpol),
            ('([^\\s"\\\'<%s{}\\\\&])+' % '>' if token is String.Other else '', token),
            include('s/escape'),
            ('["\\\'\\s&{<}\\\\]', token)]

# WARNING: Decompyle incomplete
