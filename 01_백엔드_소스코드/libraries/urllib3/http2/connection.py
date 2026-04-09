# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: connection.pyc (Python 3.11)

from __future__ import annotations
import logging
import re
import threading
import types
import typing
import h2.config as h2
import h2.connection as h2
import h2.events as h2
from _base_connection import _TYPE_BODY
from _collections import HTTPHeaderDict
from connection import HTTPSConnection, _get_default_user_agent
from exceptions import ConnectionError
from response import BaseHTTPResponse
orig_HTTPSConnection = HTTPSConnection
T = typing.TypeVar('T')
log = logging.getLogger(__name__)
RE_IS_LEGAL_HEADER_NAME = re.compile(b"^[!#$%&'*+\\-.^_`|~0-9a-z]+$")
RE_IS_ILLEGAL_HEADER_VALUE = re.compile(b'[\\0\\x00\\x0a\\x0d\\r\\n]|^[ \\r\\n\\t]|[ \\r\\n\\t]$')

def _is_legal_header_name(name = None):
    '''
    "An implementation that validates fields according to the definitions in Sections
    5.1 and 5.5 of [HTTP] only needs an additional check that field names do not
    include uppercase characters." (https://httpwg.org/specs/rfc9113.html#n-field-validity)

    `http.client._is_legal_header_name` does not validate the field name according to the
    HTTP 1.1 spec, so we do that here, in addition to checking for uppercase characters.

    This does not allow for the `:` character in the header name, so should not
    be used to validate pseudo-headers.
    '''
    return bool(RE_IS_LEGAL_HEADER_NAME.match(name))


def _is_illegal_header_value(value = None):
    '''
    "A field value MUST NOT contain the zero value (ASCII NUL, 0x00), line feed
    (ASCII LF, 0x0a), or carriage return (ASCII CR, 0x0d) at any position. A field
    value MUST NOT start or end with an ASCII whitespace character (ASCII SP or HTAB,
    0x20 or 0x09)." (https://httpwg.org/specs/rfc9113.html#n-field-validity)
    '''
    return bool(RE_IS_ILLEGAL_HEADER_VALUE.search(value))


def _LockedObject():
    '''_LockedObject'''
    __doc__ = '\n    A wrapper class that hides a specific object behind a lock.\n    The goal here is to provide a simple way to protect access to an object\n    that cannot safely be simultaneously accessed from multiple threads. The\n    intended use of this class is simple: take hold of it with a context\n    manager, which returns the protected object.\n    '
    __slots__ = ('lock', '_obj')
    
    def __init__(self = None, obj = None):
        self.lock = threading.RLock()
        self._obj = obj

    
    def __enter__(self = None):
        self.lock.acquire()
        return self._obj

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'types.TracebackType | None', 'return', 'None')):
        self.lock.release()


_LockedObject = <NODE:27>(_LockedObject, '_LockedObject', typing.Generic[T])

class HTTP2Connection(HTTPSConnection):
    pass
# WARNING: Decompyle incomplete


class HTTP2Response(BaseHTTPResponse):
    pass
# WARNING: Decompyle incomplete
