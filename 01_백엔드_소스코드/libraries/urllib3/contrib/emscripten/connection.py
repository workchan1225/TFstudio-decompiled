# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: connection.pyc (Python 3.11)

from __future__ import annotations
import os
import typing
from http.client import HTTPException
from http.client import ResponseNotReady
from _base_connection import _TYPE_BODY
from connection import HTTPConnection, ProxyConfig, port_by_scheme
from exceptions import TimeoutError
from response import BaseHTTPResponse
from util.connection import _TYPE_SOCKET_OPTIONS
from util.timeout import _DEFAULT_TIMEOUT, _TYPE_TIMEOUT
from util.url import Url
from fetch import _RequestError, _TimeoutError, send_request, send_streaming_request
from request import EmscriptenRequest
from response import EmscriptenHttpResponseWrapper, EmscriptenResponse
if typing.TYPE_CHECKING:
    from _base_connection import BaseHTTPConnection, BaseHTTPSConnection

class EmscriptenHTTPConnection:
    proxy_config: 'ProxyConfig | None' = port_by_scheme['http']
    is_verified: 'bool' = False
    proxy_is_verified: 'bool | None' = None
    _response: 'EmscriptenResponse | None' = EmscriptenHttpResponseWrapper
    
    def __init__(self = None, host = None, port = None, *, timeout, source_address, blocksize, socket_options, proxy, proxy_config):
        self.host = host
        self.port = port
        self.timeout = timeout if isinstance(timeout, float) else 0
        self.scheme = 'http'
        self._closed = True
        self._response = None
        self.proxy = None
        self.proxy_config = None
        self.blocksize = blocksize
        self.source_address = None
        self.socket_options = None
        self.is_verified = False

    
    def set_tunnel(self = None, host = None, port = None, headers = (0, None, 'http'), scheme = ('host', 'str', 'port', 'int | None', 'headers', 'typing.Mapping[str, str] | None', 'scheme', 'str', 'return', 'None')):
        pass

    
    def connect(self = None):
        pass

    
    def request(self = None, method = None, url = None, body = None, headers = (None, None), *, chunked, preload_content, decode_content, enforce_content_length):
        self._closed = False
    # WARNING: Decompyle incomplete

    
    def getresponse(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        self._closed = True
        self._response = None

    is_closed = (lambda self = None: self._closed)()
    is_connected = (lambda self = None: True)()
    has_connected_to_proxy = (lambda self = None: False)()


class EmscriptenHTTPSConnection(EmscriptenHTTPConnection):
    pass
# WARNING: Decompyle incomplete

if typing.TYPE_CHECKING:
    _supports_http_protocol: 'BaseHTTPConnection' = EmscriptenHTTPConnection('', 0)
    _supports_https_protocol: 'BaseHTTPSConnection' = EmscriptenHTTPSConnection('', 0)
    return None
