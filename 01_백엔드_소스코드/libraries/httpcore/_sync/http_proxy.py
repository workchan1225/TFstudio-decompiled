# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: http_proxy.pyc (Python 3.11)

from __future__ import annotations
import base64
import logging
import ssl
import typing
from _backends.base import SOCKET_OPTION, NetworkBackend
from _exceptions import ProxyError
from _models import URL, Origin, Request, Response, enforce_bytes, enforce_headers, enforce_url
from _ssl import default_ssl_context
from _synchronization import Lock
from _trace import Trace
from connection import HTTPConnection
from connection_pool import ConnectionPool
from http11 import HTTP11Connection
from interfaces import ConnectionInterface
ByteOrStr = typing.Union[(bytes, str)]
HeadersAsSequence = typing.Sequence[typing.Tuple[(ByteOrStr, ByteOrStr)]]
HeadersAsMapping = typing.Mapping[(ByteOrStr, ByteOrStr)]
logger = logging.getLogger('httpcore.proxy')

def merge_headers(default_headers = None, override_headers = None):
    '''
    Append default_headers and override_headers, de-duplicating if a key exists
    in both cases.
    '''
    pass
# WARNING: Decompyle incomplete


class HTTPProxy(ConnectionPool):
    pass
# WARNING: Decompyle incomplete


class ForwardHTTPConnection(ConnectionInterface):
    
    def __init__(self, proxy_origin, remote_origin, proxy_headers = None, keepalive_expiry = None, network_backend = None, socket_options = (None, None, None, None, None), proxy_ssl_context = ('proxy_origin', 'Origin', 'remote_origin', 'Origin', 'proxy_headers', 'HeadersAsMapping | HeadersAsSequence | None', 'keepalive_expiry', 'float | None', 'network_backend', 'NetworkBackend | None', 'socket_options', 'typing.Iterable[SOCKET_OPTION] | None', 'proxy_ssl_context', 'ssl.SSLContext | None', 'return', 'None')):
        self._connection = HTTPConnection(origin = proxy_origin, keepalive_expiry = keepalive_expiry, network_backend = network_backend, socket_options = socket_options, ssl_context = proxy_ssl_context)
        self._proxy_origin = proxy_origin
        self._proxy_headers = enforce_headers(proxy_headers, name = 'proxy_headers')
        self._remote_origin = remote_origin

    
    def handle_request(self = None, request = None):
        headers = merge_headers(self._proxy_headers, request.headers)
        url = URL(scheme = self._proxy_origin.scheme, host = self._proxy_origin.host, port = self._proxy_origin.port, target = bytes(request.url))
        proxy_request = Request(method = request.method, url = url, headers = headers, content = request.stream, extensions = request.extensions)
        return self._connection.handle_request(proxy_request)

    
    def can_handle_request(self = None, origin = None):
        return origin == self._remote_origin

    
    def close(self = None):
        self._connection.close()

    
    def info(self = None):
        return self._connection.info()

    
    def is_available(self = None):
        return self._connection.is_available()

    
    def has_expired(self = None):
        return self._connection.has_expired()

    
    def is_idle(self = None):
        return self._connection.is_idle()

    
    def is_closed(self = None):
        return self._connection.is_closed()

    
    def __repr__(self = None):
        return f'''<{self.__class__.__name__} [{self.info()}]>'''



class TunnelHTTPConnection(ConnectionInterface):
    
    def __init__(self, proxy_origin, remote_origin, ssl_context, proxy_ssl_context, proxy_headers, keepalive_expiry = None, http1 = None, http2 = None, network_backend = (None, None, None, None, True, False, None, None), socket_options = ('proxy_origin', 'Origin', 'remote_origin', 'Origin', 'ssl_context', 'ssl.SSLContext | None', 'proxy_ssl_context', 'ssl.SSLContext | None', 'proxy_headers', 'typing.Sequence[tuple[bytes, bytes]] | None', 'keepalive_expiry', 'float | None', 'http1', 'bool', 'http2', 'bool', 'network_backend', 'NetworkBackend | None', 'socket_options', 'typing.Iterable[SOCKET_OPTION] | None', 'return', 'None')):
        self._connection = HTTPConnection(origin = proxy_origin, keepalive_expiry = keepalive_expiry, network_backend = network_backend, socket_options = socket_options, ssl_context = proxy_ssl_context)
        self._proxy_origin = proxy_origin
        self._remote_origin = remote_origin
        self._ssl_context = ssl_context
        self._proxy_ssl_context = proxy_ssl_context
        self._proxy_headers = enforce_headers(proxy_headers, name = 'proxy_headers')
        self._keepalive_expiry = keepalive_expiry
        self._http1 = http1
        self._http2 = http2
        self._connect_lock = Lock()
        self._connected = False

    
    def handle_request(self = None, request = None):
        timeouts = request.extensions.get('timeout', { })
        timeout = timeouts.get('connect', None)
        self._connect_lock
    # WARNING: Decompyle incomplete

    
    def can_handle_request(self = None, origin = None):
        return origin == self._remote_origin

    
    def close(self = None):
        self._connection.close()

    
    def info(self = None):
        return self._connection.info()

    
    def is_available(self = None):
        return self._connection.is_available()

    
    def has_expired(self = None):
        return self._connection.has_expired()

    
    def is_idle(self = None):
        return self._connection.is_idle()

    
    def is_closed(self = None):
        return self._connection.is_closed()

    
    def __repr__(self = None):
        return f'''<{self.__class__.__name__} [{self.info()}]>'''
