# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response.pyc (Python 3.11)

from __future__ import annotations
import collections
import io
import json as _json
import logging
import socket
import sys
import typing
import warnings
import zlib
from contextlib import contextmanager
from http.client import HTTPMessage as _HttplibHTTPMessage
from http.client import HTTPResponse as _HttplibHTTPResponse
from socket import timeout as SocketTimeout
if typing.TYPE_CHECKING:
    from _base_connection import BaseHTTPConnection

try:
    import brotlicffi as brotli
    
    try:
        pass
    except ImportError:
        import brotli
        
        try:
            pass
        try:
            pass
        except ImportError:
            brotli = None

        from  import util
        from _base_connection import _TYPE_BODY
        from _collections import HTTPHeaderDict
        from connection import BaseSSLError, HTTPConnection, HTTPException
        from exceptions import BodyNotHttplibCompatible, DecodeError, DependencyWarning, HTTPError, IncompleteRead, InvalidChunkLength, InvalidHeader, ProtocolError, ReadTimeoutError, ResponseNotChunked, SSLError
        from util.response import is_fp_closed, is_response_to_head
        from util.retry import Retry
        if typing.TYPE_CHECKING:
            from connectionpool import HTTPConnectionPool


log = logging.getLogger(__name__)

class ContentDecoder:
    
    def decompress(self = None, data = None, max_length = None):
        raise NotImplementedError()

    has_unconsumed_tail = (lambda self = None: raise NotImplementedError())()
    
    def flush(self = None):
        raise NotImplementedError()



class DeflateDecoder(ContentDecoder):
    
    def __init__(self = None):
        self._first_try = True
        self._first_try_data = b''
        self._unfed_data = b''
        self._obj = zlib.decompressobj()

    
    def decompress(self = None, data = None, max_length = None):
        data = self._unfed_data + data
        self._unfed_data = b''
        if not data and self._obj.unconsumed_tail:
            return data
        original_max_length = None
        if original_max_length < 0:
            max_length = 0
        elif original_max_length == 0:
            self._unfed_data = data
            return b''
        if not self._first_try:
            return self._obj.decompress(self._obj.unconsumed_tail + data, max_length = max_length)
        
        try:
            self._obj.decompress(data, max_length = max_length) = None, None._first_try_data += data, ._first_try_data
            if decompressed:
                self._first_try = False
                self._first_try_data = b''
            return decompressed
        except zlib.error:
            self._first_try = False
            self._obj = zlib.decompressobj(-(zlib.MAX_WBITS))
            self._first_try_data = b''
            return 


    has_unconsumed_tail = (lambda self = None:
