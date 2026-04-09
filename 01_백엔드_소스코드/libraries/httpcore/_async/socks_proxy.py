# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: socks_proxy.pyc (Python 3.11)

from __future__ import annotations
import logging
import ssl
import socksio
from _backends.auto import AutoBackend
from _backends.base import AsyncNetworkBackend, AsyncNetworkStream
from _exceptions import ConnectionNotAvailable, ProxyError
from _models import URL, Origin, Request, Response, enforce_bytes, enforce_url
from _ssl import default_ssl_context
from _synchronization import AsyncLock
from _trace import Trace
from connection_pool import AsyncConnectionPool
from http11 import AsyncHTTP11Connection
from interfaces import AsyncConnectionInterface
logger = logging.getLogger('httpcore.socks')
AUTH_METHODS = {
    b'\x00': 'NO AUTHENTICATION REQUIRED',
    b'\x01': 'GSSAPI',
    b'\x02': 'USERNAME/PASSWORD',
    b'\xff': 'NO ACCEPTABLE METHODS' }
REPLY_CODES = {
    b'\x00': 'Succeeded',
    b'\x01': 'General SOCKS server failure',
    b'\x02': 'Connection not allowed by ruleset',
    b'\x03': 'Network unreachable',
    b'\x04': 'Host unreachable',
    b'\x05': 'Connection refused',
    b'\x06': 'TTL expired',
    b'\x07': 'Command not supported',
    b'\x08': 'Address type not supported' }

async def _init_socks5_connection(stream = None, *, host, port, auth):
    pass
# WARNING: Decompyle incomplete


class AsyncSOCKSProxy(AsyncConnectionPool):
    pass
# WARNING: Decompyle incomplete


class AsyncSocks5Connection(AsyncConnectionInterface):
    
    def __init__(self, proxy_origin, remote_origin, proxy_auth, ssl_context = None, keepalive_expiry = None, http1 = None, http2 = (None, None, None, True, False, None), network_backend = ('proxy_origin', 'Origin', 'remote_origin', 'Origin', 'proxy_auth', 'tuple[bytes, bytes] | None', 'ssl_context', 'ssl.SSLContext | None', 'keepalive_expiry', 'float | None', 'http1', 'bool', 'http2', 'bool', 'network_backend', 'AsyncNetworkBackend | None', 'return', 'None')):
        self._proxy_origin = proxy_origin
        self._remote_origin = remote_origin
        self._proxy_auth = proxy_auth
        self._ssl_context = ssl_context
        self._keepalive_expiry = keepalive_expiry
        self._http1 = http1
        self._http2 = http2
    # WARNING: Decompyle incomplete

    
    async def handle_async_request(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    def can_handle_request(self = None, origin = None):
        return origin == self._remote_origin

    
    async def aclose(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_available(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def has_expired(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_idle(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_closed(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def info(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''<{self.__class__.__name__} [{self.info()}]>'''
