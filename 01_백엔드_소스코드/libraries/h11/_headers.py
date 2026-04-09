# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _headers.pyc (Python 3.11)

import re
from typing import AnyStr, cast, List, overload, Sequence, Tuple, TYPE_CHECKING, Union
from _abnf import field_name, field_value
from _util import bytesify, LocalProtocolError, validate
if TYPE_CHECKING:
    from _events import Request

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

CONTENT_LENGTH_MAX_DIGITS = 20
_content_length_re = re.compile(b'[0-9]+')
_field_name_re = re.compile(field_name.encode('ascii'))
_field_value_re = re.compile(field_value.encode('ascii'))

def Headers():
    '''Headers'''
    __doc__ = '\n    A list-like interface that allows iterating over headers as byte-pairs\n    of (lowercased-name, value).\n\n    Internally we actually store the representation as three-tuples,\n    including both the raw original casing, in order to preserve casing\n    over-the-wire, and the lowercased name, for case-insensitive comparisions.\n\n    r = Request(\n        method="GET",\n        target="/",\n        headers=[("Host", "example.org"), ("Connection", "keep-alive")],\n        http_version="1.1",\n    )\n    assert r.headers == [\n        (b"host", b"example.org"),\n        (b"connection", b"keep-alive")\n    ]\n    assert r.headers.raw_items() == [\n        (b"Host", b"example.org"),\n        (b"Connection", b"keep-alive")\n    ]\n    '
    __slots__ = '_full_items'
    
    def __init__(self = None, full_items = None):
        self._full_items = full_items

    
    def __bool__(self = None):
        return bool(self._full_items)

    
    def __eq__(self = None, other = None):
        return list(self) == list(other)

    
    def __len__(self = None):
        return len(self._full_items)

    
    def __repr__(self = None):
        return '<Headers(%s)>' % repr(list(self))

    
    def __getitem__(self = None, idx = None):
        (_, name, value) = self._full_items[idx]
        return (name, value)

    
    def raw_items(self = None):
        return self._full_items()


Headers = <NODE:27>(Headers, 'Headers', Sequence[Tuple[(bytes, bytes)]])
HeaderTypes = Union[(List[Tuple[(bytes, bytes)]], List[Tuple[(bytes, str)]], List[Tuple[(str, bytes)]], List[Tuple[(str, str)]])]
normalize_and_validate = (lambda headers = None, _parsed = None: pass)()
normalize_and_validate = (lambda headers = None, _parsed = None: pass)()
normalize_and_validate = (lambda headers = None, _parsed = None: pass)()

def normalize_and_validate(headers = None, _parsed = None):
    new_headers = []
    seen_content_length = None
    saw_transfer_encoding = False
# WARNING: Decompyle incomplete


def get_comma_header(headers = None, name = None):
    out = []
    for _, found_name, found_raw_value in headers._full_items:
        if found_name == name:
            found_raw_value = found_raw_value.lower()
            for found_split_value in found_raw_value.split(b','):
                found_split_value = found_split_value.strip()
                if found_split_value:
                    out.append(found_split_value)
                return out


def set_comma_header(headers = None, name = None, new_values = None):
    new_headers = []
    for found_raw_name, found_name, found_raw_value in headers._full_items:
        if found_name != name:
            new_headers.append((found_raw_name, found_raw_value))
        for new_value in new_values:
            new_headers.append((name.title(), new_value))
            return normalize_and_validate(new_headers)


def has_expect_100_continue(request = None):
    if request.http_version < b'1.1':
        return False
    expect = None(request.headers, b'expect')
    return b'100-continue' in expect
