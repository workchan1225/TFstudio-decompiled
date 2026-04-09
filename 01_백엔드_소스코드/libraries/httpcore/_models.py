# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _models.pyc (Python 3.11)

from __future__ import annotations
import base64
import ssl
import typing
import urllib.parse as urllib
ByteOrStr = typing.Union[(bytes, str)]
HeadersAsSequence = typing.Sequence[typing.Tuple[(ByteOrStr, ByteOrStr)]]
HeadersAsMapping = typing.Mapping[(ByteOrStr, ByteOrStr)]
HeaderTypes = typing.Union[(HeadersAsSequence, HeadersAsMapping, None)]
Extensions = typing.MutableMapping[(str, typing.Any)]

def enforce_bytes(value = None, *, name):
    '''
    Any arguments that are ultimately represented as bytes can be specified
    either as bytes or as strings.

    However we enforce that any string arguments must only contain characters in
    the plain ASCII range. chr(0)...chr(127). If you need to use characters
    outside that range then be precise, and use a byte-wise argument.
    '''
    if isinstance(value, str):
        
        try:
            return value.encode('ascii')
        except UnicodeEncodeError:
            raise TypeError(f'''{name} strings may not include unicode characters.''')
            if isinstance(value, bytes):
                return value
            seen_type = None(value).__name__
            raise TypeError(f'''{name} must be bytes or str, but got {seen_type}.''')



def enforce_url(value = None, *, name):
    '''
    Type check for URL parameters.
    '''
    if isinstance(value, (bytes, str)):
        return URL(value)
    if None(value, URL):
        return value
    seen_type = None(value).__name__
    raise TypeError(f'''{name} must be a URL, bytes, or str, but got {seen_type}.''')


def enforce_headers(value = None, *, name):
    '''
    Convienence function that ensure all items in request or response headers
    are either bytes or strings in the plain ASCII range.
    '''
    pass
# WARNING: Decompyle incomplete


def enforce_stream(value = None, *, name):
    pass
# WARNING: Decompyle incomplete

DEFAULT_PORTS = {
    b'ftp': 21,
    b'http': 80,
    b'https': 443,
    b'ws': 80,
    b'wss': 443 }

def include_request_headers(headers = None, *, url, content):
    headers_set = (lambda .0: pass# WARNING: Decompyle incomplete
)(headers())
# WARNING: Decompyle incomplete


class ByteStream:
    '''
    A container for non-streaming content, and that supports both sync and async
    stream iteration.
    '''
    
    def __init__(self = None, content = None):
        self._content = content

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''<{self.__class__.__name__} [{len(self._content)} bytes]>'''



class Origin:
    
    def __init__(self = None, scheme = None, host = None, port = ('scheme', 'bytes', 'host', 'bytes', 'port', 'int', 'return', 'None')):
        self.scheme = scheme
        self.host = host
        self.port = port

    
    def __eq__(self = None, other = None):
