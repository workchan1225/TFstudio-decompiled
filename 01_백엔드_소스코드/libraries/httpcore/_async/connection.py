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
from _backends.auto import AutoBackend
from _backends.base import SOCKET_OPTION, AsyncNetworkBackend, AsyncNetworkStream
from _exceptions import ConnectError, ConnectTimeout
from _models import Origin, Request, Response
from _ssl import default_ssl_context
from _synchronization import AsyncLock
from _trace import Trace
from http11 import AsyncHTTP11Connection
from interfaces import AsyncConnectionInterface
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


class AsyncHTTPConnection(AsyncConnectionInterface):
    
    def __init__(self, origin, ssl_context, keepalive_expiry, http1, http2, retries = None, local_address = None, uds = None, network_backend = (None, None, True, False, 0, None, None, None, None), socket_options = ('origin', 'Origin', 'ssl_context', 'ssl.SSLContext | None', 'keepalive_expiry', 'float | None', 'http1', 'bool', 'http2', 'bool', 'retries', 'int', 'local_address', 'str | None', 'uds', 'str | None', 'network_backend', 'AsyncNetworkBackend | None', 'socket_options', 'typing.Iterable[SOCKET_OPTION] | None', 'return', 'None')):
        self._origin = origin
        self._ssl_context = ssl_context
        self._keepalive_expiry = keepalive_expiry
        self._http1 = http1
        self._http2 = http2
        self._retries = retries
        self._local_address = local_address
        self._uds = uds
    # WARNING: Decompyle incomplete

    
    async def handle_async_request(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _connect(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    def can_handle_request(self = None, origin = None):
        return origin == self._origin

    
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

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_value = None, traceback = (None, None, None)):
        pass
    # WARNING: Decompyle incomplete
