# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _parser.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Iterable
import string
from types import MappingProxyType
from typing import Any, BinaryIO, NamedTuple
from _re import RE_DATETIME, RE_LOCALTIME, RE_NUMBER, match_to_datetime, match_to_localtime, match_to_number
from _types import Key, ParseFloat, Pos
ASCII_CTRL = (lambda .0: pass# WARNING: Decompyle incomplete
)(range(32)()) | frozenset(chr(127))
ILLEGAL_BASIC_STR_CHARS = ASCII_CTRL - frozenset('\t')
ILLEGAL_MULTILINE_BASIC_STR_CHARS = ASCII_CTRL - frozenset('\t\n')
ILLEGAL_LITERAL_STR_CHARS = ILLEGAL_BASIC_STR_CHARS
ILLEGAL_MULTILINE_LITERAL_STR_CHARS = ILLEGAL_MULTILINE_BASIC_STR_CHARS
ILLEGAL_COMMENT_CHARS = ILLEGAL_BASIC_STR_CHARS
TOML_WS = frozenset(' \t')
TOML_WS_AND_NEWLINE = TOML_WS | frozenset('\n')
BARE_KEY_CHARS = frozenset(string.ascii_letters + string.digits + '-_')
KEY_INITIAL_CHARS = BARE_KEY_CHARS | frozenset('"\'')
HEXDIGIT_CHARS = frozenset(string.hexdigits)
BASIC_STR_ESCAPE_REPLACEMENTS = MappingProxyType({
    '\\b': '\x08',
    '\\t': '\t',
    '\\n': '\n',
    '\\f': '\x0c',
    '\\r': '\r',
    '\\"': '"',
    '\\\\': '\\' })

class TOMLDecodeError(ValueError):
    '''An error raised if a document is not valid TOML.'''
    pass


def load(__fp = None, *, parse_float):
    '''Parse TOML from a binary file object.'''
    b = __fp.read()
    
    try:
        s = b.decode()
    except AttributeError:
        raise TypeError("File must be opened in binary mode, e.g. use `open('foo.toml', 'rb')`"), None

    return loads(s, parse_float = parse_float)


def loads(__s = None, *, parse_float):
    '''Parse TOML from a string.'''
    src = __s.replace('\r\n', '\n')
    pos = 0
    out = Output(NestedDict(), Flags())
    header = ()
    parse_float = make_safe_parse_float(parse_float)
    pos = skip_chars(src, pos, TOML_WS)
    
    try:
        char = src[pos]
    except IndexError:
        pass
    except:
        if char == '\n':
            pos += 1
            continue
        if char in KEY_INITIAL_CHARS:
            pos = key_value_rule(src, pos, out, header, parse_float)
            pos = skip_chars(src, pos, TOML_WS)
        elif char == '[':
            
            try:
                second_char = src[pos + 1]
            except IndexError:
                second_char = None

            out.flags.finalize_pending()
            if second_char == '[':
                (pos, header) = create_list_rule(src, pos, out)
            else:
                (pos, header) = create_dict_rule(src, pos, out)
            pos = skip_chars(src, pos, TOML_WS)
        elif char != '#':
            raise suffixed_err(src, pos, 'Invalid statement')
        pos = skip_comment(src, pos)
        
        try:
            char = src[pos]
        except IndexError:
            pass
        except:
            if char != '\n':
                raise suffixed_err(src, pos, 'Expected newline or end of document after a statement')
            pos += 1
            continue

        return out.data.dict



class Flags:
    '''Flags that map to parsed keys/namespaces.'''
    FROZEN = 0
    EXPLICIT_NEST = 1
    
    def __init__(self = None):
        self._flags = { }
        self._pending_flags = set()

    
    def add_pending(self = None, key = None, flag = None):
        self._pending_flags.add((key, flag))

    
    def finalize_pending(self = None):
        for key, flag in self._pending_flags:
            self.set(key, flag, recursive = False)
            self._pending_flags.clear()
            return None

    
    def unset_all(self = None, key = None):
        cont = self._flags
        for k in key[:-1]:
            if k not in cont:
                return None
            cont = None[k]['nested']
            cont.pop(key[-1], None)
            return None

    
    def set(self = None, key = None, flag = None, *, recursive):
        cont = self._flags
        key_stem = key[-1]
        key_parent = key[:-1]
        for k in key_parent:
            if k not in cont:
                cont[k] = {
                    'flags': set(),
                    'recursive_flags': set(),
                    'nested': { } }
            cont = cont[k]['nested']
            if key_stem not in cont:
                cont[key_stem] = {
                    'flags': set(),
                    'recursive_flags': set(),
                    'nested': { } }
        cont[key_stem]['recursive_flags' if recursive else 'flags'].add(flag)

    
    def is_(self = None, key = None, flag = None):
