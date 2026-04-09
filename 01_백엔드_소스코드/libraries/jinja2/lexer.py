# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lexer.pyc (Python 3.11)

__doc__ = "Implements a Jinja / Python combination lexer. The ``Lexer`` class\nis used to do some preprocessing. It filters out invalid operators like\nthe bitshift operators we don't allow in templates. It separates\ntemplate code and python code in expressions.\n"
import re
import typing as t
from ast import literal_eval
from collections import deque
from sys import intern
from _identifier import pattern as name_re
from exceptions import TemplateSyntaxError
from utils import LRUCache
if t.TYPE_CHECKING:
    import typing_extensions as te
    from environment import Environment
_lexer_cache: t.MutableMapping[(t.Tuple, 'Lexer')] = LRUCache(50)
whitespace_re = re.compile('\\s+')
newline_re = re.compile('(\\r\\n|\\r|\\n)')
string_re = re.compile('(\'([^\'\\\\]*(?:\\\\.[^\'\\\\]*)*)\'|"([^"\\\\]*(?:\\\\.[^"\\\\]*)*)")', re.S)
integer_re = re.compile('\n    (\n        0b(_?[0-1])+ # binary\n    |\n        0o(_?[0-7])+ # octal\n    |\n        0x(_?[\\da-f])+ # hex\n    |\n        [1-9](_?\\d)* # decimal\n    |\n        0(_?0)* # decimal zero\n    )\n    ', re.IGNORECASE | re.VERBOSE)
float_re = re.compile("\n    (?<!\\.)  # doesn't start with a .\n    (\\d+_)*\\d+  # digits, possibly _ separated\n    (\n        (\\.(\\d+_)*\\d+)?  # optional fractional part\n        e[+\\-]?(\\d+_)*\\d+  # exponent part\n    |\n        \\.(\\d+_)*\\d+  # required fractional part\n    )\n    ", re.IGNORECASE | re.VERBOSE)
TOKEN_ADD = intern('add')
TOKEN_ASSIGN = intern('assign')
TOKEN_COLON = intern('colon')
TOKEN_COMMA = intern('comma')
TOKEN_DIV = intern('div')
TOKEN_DOT = intern('dot')
TOKEN_EQ = intern('eq')
TOKEN_FLOORDIV = intern('floordiv')
TOKEN_GT = intern('gt')
TOKEN_GTEQ = intern('gteq')
TOKEN_LBRACE = intern('lbrace')
TOKEN_LBRACKET = intern('lbracket')
TOKEN_LPAREN = intern('lparen')
TOKEN_LT = intern('lt')
TOKEN_LTEQ = intern('lteq')
TOKEN_MOD = intern('mod')
TOKEN_MUL = intern('mul')
TOKEN_NE = intern('ne')
TOKEN_PIPE = intern('pipe')
TOKEN_POW = intern('pow')
TOKEN_RBRACE = intern('rbrace')
TOKEN_RBRACKET = intern('rbracket')
TOKEN_RPAREN = intern('rparen')
TOKEN_SEMICOLON = intern('semicolon')
TOKEN_SUB = intern('sub')
TOKEN_TILDE = intern('tilde')
TOKEN_WHITESPACE = intern('whitespace')
TOKEN_FLOAT = intern('float')
TOKEN_INTEGER = intern('integer')
TOKEN_NAME = intern('name')
TOKEN_STRING = intern('string')
TOKEN_OPERATOR = intern('operator')
TOKEN_BLOCK_BEGIN = intern('block_begin')
TOKEN_BLOCK_END = intern('block_end')
TOKEN_VARIABLE_BEGIN = intern('variable_begin')
TOKEN_VARIABLE_END = intern('variable_end')
TOKEN_RAW_BEGIN = intern('raw_begin')
TOKEN_RAW_END = intern('raw_end')
TOKEN_COMMENT_BEGIN = intern('comment_begin')
TOKEN_COMMENT_END = intern('comment_end')
TOKEN_COMMENT = intern('comment')
TOKEN_LINESTATEMENT_BEGIN = intern('linestatement_begin')
TOKEN_LINESTATEMENT_END = intern('linestatement_end')
TOKEN_LINECOMMENT_BEGIN = intern('linecomment_begin')
TOKEN_LINECOMMENT_END = intern('linecomment_end')
TOKEN_LINECOMMENT = intern('linecomment')
TOKEN_DATA = intern('data')
TOKEN_INITIAL = intern('initial')
TOKEN_EOF = intern('eof')
# WARNING: Decompyle incomplete
