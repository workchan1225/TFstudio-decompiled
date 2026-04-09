# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: robotframework.pyc (Python 3.11)

'''
    pygments.lexers.robotframework
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Lexer for Robot Framework.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
import re
from pygments.lexer import Lexer
from pygments.token import Token
__all__ = [
    'RobotFrameworkLexer']
HEADING = Token.Generic.Heading
SETTING = Token.Keyword.Namespace
IMPORT = Token.Name.Namespace
TC_KW_NAME = Token.Generic.Subheading
KEYWORD = Token.Name.Function
ARGUMENT = Token.String
VARIABLE = Token.Name.Variable
COMMENT = Token.Comment
SEPARATOR = Token.Punctuation
SYNTAX = Token.Punctuation
GHERKIN = Token.Generic.Emph
ERROR = Token.Error

def normalize(string, remove = ('',)):
    string = string.lower()
    for char in remove + ' ':
        if char in string:
            string = string.replace(char, '')
        return string


class RobotFrameworkLexer(Lexer):
    '''
    For Robot Framework test data.

    Supports both space and pipe separated plain text formats.
    '''
    name = 'RobotFramework'
    url = 'http://robotframework.org'
    aliases = [
        'robotframework']
    filenames = [
        '*.robot',
        '*.resource']
    mimetypes = [
        'text/x-robotframework']
    version_added = '1.6'
    
    def __init__(self, **options):
        options['tabsize'] = 2
        options['encoding'] = 'UTF-8'
    # WARNING: Decompyle incomplete

    
    def get_tokens_unprocessed(self, text):
        pass
    # WARNING: Decompyle incomplete



class VariableTokenizer:
    
    def tokenize(self, string, token):
        pass
    # WARNING: Decompyle incomplete

    
    def _tokenize(self, var, string, orig_token):
        pass
    # WARNING: Decompyle incomplete



class RowTokenizer:
    
    def __init__(self):
        self._table = UnknownTable()
        self._splitter = RowSplitter()
        testcases = TestCaseTable()
        settings = SettingTable(testcases.set_default_template)
        variables = VariableTable()
        keywords = KeywordTable()
        self._tables = {
            'settings': settings,
            'setting': settings,
            'metadata': settings,
            'variables': variables,
            'variable': variables,
            'testcases': testcases,
            'testcase': testcases,
            'tasks': testcases,
            'task': testcases,
            'keywords': keywords,
            'keyword': keywords,
            'userkeywords': keywords,
            'userkeyword': keywords }

    
    def tokenize(self, row):
        pass
    # WARNING: Decompyle incomplete

    
    def _start_table(self, header):
        name = normalize(header, remove = '*')
        return self._tables.get(name, UnknownTable())

    
    def _tokenize(self, value, index, commented, separator, heading):
        pass
    # WARNING: Decompyle incomplete



class RowSplitter:
    _space_splitter = re.compile('( {2,})')
    _pipe_splitter = re.compile('((?:^| +)\\|(?: +|$))')
    
    def split(self, row):
        pass
    # WARNING: Decompyle incomplete

    
    def _split_from_spaces(self, row):
        pass
    # WARNING: Decompyle incomplete

    
    def _split_from_pipes(self, row):
        pass
    # WARNING: Decompyle incomplete



class Tokenizer:
    _tokens = None
    
    def __init__(self):
        self._index = 0

    
    def tokenize(self, value):
        values_and_tokens = self._tokenize(value, self._index)
        if isinstance(values_and_tokens, type(Token)):
            [
                (value, values_and_tokens)] = self, self._index += 1, ._index
        return values_and_tokens

    
    def _tokenize(self, value, index):
        index = min(index, len(self._tokens) - 1)
        return self._tokens[index]

    
    def _is_assign(self, value):
