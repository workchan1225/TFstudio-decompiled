# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parser.pyc (Python 3.11)

import codecs
import re
from typing import IO, Iterator, Match, NamedTuple, Optional, Pattern, Sequence, Tuple

def make_regex(string = None, extra_flags = None):
    return re.compile(string, re.UNICODE | extra_flags)

_newline = make_regex('(\\r\\n|\\n|\\r)')
_multiline_whitespace = make_regex('\\s*', extra_flags = re.MULTILINE)
_whitespace = make_regex('[^\\S\\r\\n]*')
_export = make_regex('(?:export[^\\S\\r\\n]+)?')
_single_quoted_key = make_regex("'([^']+)'")
_unquoted_key = make_regex('([^=\\#\\s]+)')
_equal_sign = make_regex('(=[^\\S\\r\\n]*)')
_single_quoted_value = make_regex("'((?:\\\\'|[^'])*)'")
_double_quoted_value = make_regex('"((?:\\\\"|[^"])*)"')
_unquoted_value = make_regex('([^\\r\\n]*)')
_comment = make_regex('(?:[^\\S\\r\\n]*#[^\\r\\n]*)?')
_end_of_line = make_regex('[^\\S\\r\\n]*(?:\\r\\n|\\n|\\r|$)')
_rest_of_line = make_regex('[^\\r\\n]*(?:\\r|\\n|\\r\\n)?')
_double_quote_escapes = make_regex('\\\\[\\\\\'\\"abfnrtv]')
_single_quote_escapes = make_regex("\\\\[\\\\']")

class Original(NamedTuple):
    line: int = 'Original'


class Binding(NamedTuple):
    error: bool = 'Binding'


class Position:
    
    def __init__(self = None, chars = None, line = None):
        self.chars = chars
        self.line = line

    start = (lambda cls = None: cls(chars = 0, line = 1))()
    
    def set(self = None, other = None):
        self.chars = other.chars
        self.line = other.line

    
    def advance(self = None, string = None):
        pass



class Error(Exception):
    pass


class Reader:
    
    def __init__(self = None, stream = None):
        self.string = stream.read()
        self.position = Position.start()
        self.mark = Position.start()

    
    def has_next(self = None):
        return self.position.chars < len(self.string)

    
    def set_mark(self = None):
        self.mark.set(self.position)

    
    def get_marked(self = None):
        return Original(string = self.string[self.mark.chars:self.position.chars], line = self.mark.line)

    
    def peek(self = None, count = None):
        return self.string[self.position.chars:self.position.chars + count]

    
    def read(self = None, count = None):
        result = self.string[self.position.chars:self.position.chars + count]
        if len(result) < count:
            raise Error('read: End of string')
        self.position.advance(result)
        return result

    
    def read_regex(self = None, regex = None):
        match = regex.match(self.string, self.position.chars)
    # WARNING: Decompyle incomplete



def decode_escapes(regex = None, string = None):
    
    def decode_match(match = None):
        return codecs.decode(match.group(0), 'unicode-escape')

    return regex.sub(decode_match, string)


def parse_key(reader = None):
    char = reader.peek(1)
    if char == '#':
        return None
    if None == "'":
        (key,) = reader.read_regex(_single_quoted_key)
    else:
        (key,) = reader.read_regex(_unquoted_key)
    return key


def parse_unquoted_value(reader = None):
    (part,) = reader.read_regex(_unquoted_value)
    return re.sub('\\s+#.*', '', part).rstrip()


def parse_value(reader = None):
    char = reader.peek(1)
    if char == "'":
        (value,) = reader.read_regex(_single_quoted_value)
        return decode_escapes(_single_quote_escapes, value)
    if None == '"':
        (value,) = reader.read_regex(_double_quoted_value)
        return decode_escapes(_double_quote_escapes, value)
    if None in ('', '\n', '\r'):
        return ''
    return None(reader)


def parse_binding(reader = None):
    reader.set_mark()
    
    try:
        reader.read_regex(_multiline_whitespace)
        if not reader.has_next():
            return None(key = Binding, value = None, original = reader.get_marked(), error = False)
        None.read_regex(_export)
        key = parse_key(reader)
        reader.read_regex(_whitespace)
        if reader.peek(1) == '=':
            reader.read_regex(_equal_sign)
            value = parse_value(reader)
        else:
            value = None
        reader.read_regex(_comment)
        reader.read_regex(_end_of_line)
        return Binding(key = key, value = value, original = reader.get_marked(), error = False)
    except Error:
        reader.read_regex(_rest_of_line)
        return 



def parse_stream(stream = None):
    pass
# WARNING: Decompyle incomplete
