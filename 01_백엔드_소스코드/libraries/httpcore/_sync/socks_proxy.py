# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: socks_proxy.pyc (Python 3.11)

from __future__ import annotations
import logging
import ssl
import socksio
from _backends.sync import SyncBackend
from _backends.base import NetworkBackend, NetworkStream
from _exceptions import ConnectionNotAvailable, ProxyError
from _models import URL, Origin, Request, Response, enforce_bytes, enforce_url
from _ssl import default_ssl_context
from _synchronization import Lock
from _trace import Trace
from connection_pool import ConnectionPool
from http11 import HTTP11Connection
from interfaces import ConnectionInterface
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

def _init_socks5_connection(stream = None, *, host, port, auth):
    conn = socksio.socks5.SOCKS5Connection()
# WARNING: Decompyle incomplete


class SOCKSProxy(ConnectionPool):
    pass
# WARNING: Decompyle incomplete


class Socks5Connection(ConnectionInterface):
    
    def __init__(self, proxy_origin, remote_origin, proxy_auth, ssl_context = None, keepalive_expiry = None, http1 = None, http2 = (None, None, None, True, False, None), network_backend = ('proxy_origin', 'Origin', 'remote_origin', 'Origin', 'proxy_auth', 'tuple[bytes, bytes] | None', 'ssl_context', 'ssl.SSLContext | None', 'keepalive_expiry', 'float | None', 'http1', 'bool', 'http2', 'bool', 'network_backend', 'NetworkBackend | None', 'return', 'None')):
        self._proxy_origin = proxy_origin
        self._remote_origin = remote_origin
        self._proxy_auth = proxy_auth
        self._ssl_context = ssl_context
        self._keepalive_expiry = keepalive_expiry
        self._http1 = http1
        self._http2 = http2
    # WARNING: Decompyle incomplete

    
    def handle_request(self = None, request = None):
        timeouts = request.extensions.get('timeout', { })
        sni_hostname = request.extensions.get('sni_hostname', None)
        timeout = timeouts.get('connect', None)
        self._connect_lock
    # WARNING: Decompyle incomplete

    
    def can_handle_request(self = None, origin = None):
        return origin == self._remote_origin

    
    def close(self = None):
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
