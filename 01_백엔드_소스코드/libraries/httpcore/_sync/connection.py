# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: connection.pyc (Python 3.11)

from __future__ import annotations
import itertools
import logging
import ssl
import types
import typing
from _backends.sync import SyncBackend
from _backends.base import SOCKET_OPTION, NetworkBackend, NetworkStream
from _exceptions import ConnectError, ConnectTimeout
from _models import Origin, Request, Response
from _ssl import default_ssl_context
from _synchronization import Lock
from _trace import Trace
from http11 import HTTP11Connection
from interfaces import ConnectionInterface
RETRIES_BACKOFF_FACTOR = 0.5
logger = logging.getLogger('httpcore.connection')

def exponential_backoff(factor = None):
    '''
    Generate a geometric sequence that has a ratio of 2 and starts with 0.

    For example:
    - `factor = 2`: `0, 2, 4, 8, 16, 32, 64, ...`
    - `factor = 3`: `0, 3, 6, 12, 24, 48, 96, ...`
    '''
    pass
# WARNING: Decompyle incomplete


class HTTPConnection(ConnectionInterface):
    
    def __init__(self, origin, ssl_context, keepalive_expiry, http1, http2, retries = None, local_address = None, uds = None, network_backend = (None, None, True, False, 0, None, None, None, None), socket_options = ('origin', 'Origin', 'ssl_context', 'ssl.SSLContext | None', 'keepalive_expiry', 'float | None', 'http1', 'bool', 'http2', 'bool', 'retries', 'int', 'local_address', 'str | None', 'uds', 'str | None', 'network_backend', 'NetworkBackend | None', 'socket_options', 'typing.Iterable[SOCKET_OPTION] | None', 'return', 'None')):
        self._origin = origin
        self._ssl_context = ssl_context
        self._keepalive_expiry = keepalive_expiry
        self._http1 = http1
        self._http2 = http2
        self._retries = retries
        self._local_address = local_address
        self._uds = uds
    # WARNING: Decompyle incomplete

    
    def handle_request(self = None, request = None):
        if not self.can_handle_request(request.url.origin):
            raise RuntimeError(f'''Attempted to send request to {request.url.origin} on connection to {self._origin}''')
    # WARNING: Decompyle incomplete

    
    def _connect(self = None, request = None):
        timeouts = request.extensions.get('timeout', { })
        sni_hostname = request.extensions.get('sni_hostname', None)
        timeout = timeouts.get('connect', None)
        retries_left = self._retries
        delays = exponential_backoff(factor = RETRIES_BACKOFF_FACTOR)
    # WARNING: Decompyle incomplete

    
    def can_handle_request(self = None, origin = None):
        return origin == self._origin

    
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

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = (None, None, None)):
        self.close()
