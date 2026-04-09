# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: connection_pool.pyc (Python 3.11)

from __future__ import annotations
import ssl
import sys
import types
import typing
from _backends.auto import AutoBackend
from _backends.base import SOCKET_OPTION, AsyncNetworkBackend
from _exceptions import ConnectionNotAvailable, UnsupportedProtocol
from _models import Origin, Proxy, Request, Response
from _synchronization import AsyncEvent, AsyncShieldCancellation, AsyncThreadLock
from connection import AsyncHTTPConnection
from interfaces import AsyncConnectionInterface, AsyncRequestInterface

class AsyncPoolRequest:
    
    def __init__(self = None, request = None):
        self.request = request
        self.connection = None
        self._connection_acquired = AsyncEvent()

    
    def assign_to_connection(self = None, connection = None):
        self.connection = connection
        self._connection_acquired.set()

    
    def clear_connection(self = None):
        self.connection = None
        self._connection_acquired = AsyncEvent()

    
    async def wait_for_connection(self = None, timeout = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_queued(self = None):
        return self.connection is None



class AsyncConnectionPool(AsyncRequestInterface):
    '''
    A connection pool for making HTTP requests.
    '''
    
    def __init__(self, ssl_context, proxy, max_connections, max_keepalive_connections, keepalive_expiry, http1, http2, retries = None, local_address = None, uds = None, network_backend = (None, None, 10, None, None, True, False, 0, None, None, None, None), socket_options = ('ssl_context', 'ssl.SSLContext | None', 'proxy', 'Proxy | None', 'max_connections', 'int | None', 'max_keepalive_connections', 'int | None', 'keepalive_expiry', 'float | None', 'http1', 'bool', 'http2', 'bool', 'retries', 'int', 'local_address', 'str | None', 'uds', 'str | None', 'network_backend', 'AsyncNetworkBackend | None', 'socket_options', 'typing.Iterable[SOCKET_OPTION] | None', 'return', 'None')):
        '''
        A connection pool for making HTTP requests.

        Parameters:
            ssl_context: An SSL context to use for verifying connections.
                If not specified, the default `httpcore.default_ssl_context()`
                will be used.
            max_connections: The maximum number of concurrent HTTP connections that
                the pool should allow. Any attempt to send a request on a pool that
                would exceed this amount will block until a connection is available.
            max_keepalive_connections: The maximum number of idle HTTP connections
                that will be maintained in the pool.
            keepalive_expiry: The duration in seconds that an idle HTTP connection
                may be maintained for before being expired from the pool.
            http1: A boolean indicating if HTTP/1.1 requests should be supported
                by the connection pool. Defaults to True.
            http2: A boolean indicating if HTTP/2 requests should be supported by
                the connection pool. Defaults to False.
            retries: The maximum number of retries when trying to establish a
                connection.
            local_address: Local address to connect from. Can also be used to connect
                using a particular address family. Using `local_address="0.0.0.0"`
                will connect using an `AF_INET` address (IPv4), while using
                `local_address="::"` will connect using an `AF_INET6` address (IPv6).
            uds: Path to a Unix Domain Socket to use instead of TCP sockets.
            network_backend: A backend instance to use for handling network I/O.
            socket_options: Socket options that have to be included
             in the TCP socket when the connection was established.
        '''
        self._ssl_context = ssl_context
        self._proxy = proxy
    # WARNING: Decompyle incomplete

    
    def create_connection(self = None, origin = None):
        pass
    # WARNING: Decompyle incomplete

    connections = (lambda self = None: list(self._connections))()
    
    async def handle_async_request(self = None, request = None):
        '''
        Send an HTTP request, and return an HTTP response.

        This is the core implementation that is called into by `.request()` or `.stream()`.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _assign_requests_to_connections(self = None):
        '''
        Manage the state of the connection pool, assigning incoming
        requests to connections as available.

        Called whenever a new request is added or removed from the pool.

        Any closing connections are returned, allowing the I/O for closing
        those connections to be handled seperately.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _close_connections(self = None, closing = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def aclose(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_value = None, traceback = (None, None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        class_name = self.__class__.__name__
        self._optional_thread_lock
        request_is_queued = self._requests()
        connection_is_idle = self._connections()
        num_active_requests = request_is_queued.count(False)
        num_queued_requests = request_is_queued.count(True)
        num_active_connections = connection_is_idle.count(False)
        num_idle_connections = connection_is_idle.count(True)
        None(None, None)



class PoolByteStream:
    
    def __init__(self = None, stream = None, pool_request = None, pool = ('stream', 'typing.AsyncIterable[bytes]', 'pool_request', 'AsyncPoolRequest', 'pool', 'AsyncConnectionPool', 'return', 'None')):
        self._stream = stream
        self._pool_request = pool_request
        self._pool = pool
        self._closed = False

    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def aclose(self = None):
        pass
    # WARNING: Decompyle incomplete
