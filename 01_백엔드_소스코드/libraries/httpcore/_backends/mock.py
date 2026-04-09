# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mock.pyc (Python 3.11)

from __future__ import annotations
import ssl
import typing
from _exceptions import ReadError
from base import SOCKET_OPTION, AsyncNetworkBackend, AsyncNetworkStream, NetworkBackend, NetworkStream

class MockSSLObject:
    
    def __init__(self = None, http2 = None):
        self._http2 = http2

    
    def selected_alpn_protocol(self = None):
        return 'h2' if self._http2 else 'http/1.1'



class MockStream(NetworkStream):
    
    def __init__(self = None, buffer = None, http2 = None):
        self._buffer = buffer
        self._http2 = http2
        self._closed = False

    
    def read(self = None, max_bytes = None, timeout = None):
        if self._closed:
            raise ReadError('Connection closed')
        if not self._buffer:
            return b''
        return None._buffer.pop(0)

    
    def write(self = None, buffer = None, timeout = None):
        pass

    
    def close(self = None):
        self._closed = True

    
    def start_tls(self = None, ssl_context = None, server_hostname = None, timeout = (None, None)):
        return self

    
    def get_extra_info(self = None, info = None):
        return MockSSLObject(http2 = self._http2) if info == 'ssl_object' else None

    
    def __repr__(self = None):
        return '<httpcore.MockStream>'



class MockBackend(NetworkBackend):
    
    def __init__(self = None, buffer = None, http2 = None):
        self._buffer = buffer
        self._http2 = http2

    
    def connect_tcp(self, host = None, port = None, timeout = None, local_address = (None, None, None), socket_options = ('host', 'str', 'port', 'int', 'timeout', 'float | None', 'local_address', 'str | None', 'socket_options', 'typing.Iterable[SOCKET_OPTION] | None', 'return', 'NetworkStream')):
        return MockStream(list(self._buffer), http2 = self._http2)

    
    def connect_unix_socket(self = None, path = None, timeout = None, socket_options = (None, None)):
        return MockStream(list(self._buffer), http2 = self._http2)

    
    def sleep(self = None, seconds = None):
        pass



class AsyncMockStream(AsyncNetworkStream):
    
    def __init__(self = None, buffer = None, http2 = None):
        self._buffer = buffer
        self._http2 = http2
        self._closed = False

    
    async def read(self = None, max_bytes = None, timeout = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def write(self = None, buffer = None, timeout = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def aclose(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def start_tls(self = None, ssl_context = None, server_hostname = None, timeout = (None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def get_extra_info(self = None, info = None):
        return MockSSLObject(http2 = self._http2) if info == 'ssl_object' else None

    
    def __repr__(self = None):
        return '<httpcore.AsyncMockStream>'



class AsyncMockBackend(AsyncNetworkBackend):
    
    def __init__(self = None, buffer = None, http2 = None):
        self._buffer = buffer
        self._http2 = http2

    
    async def connect_tcp(self, host = None, port = None, timeout = None, local_address = (None, None, None), socket_options = ('host', 'str', 'port', 'int', 'timeout', 'float | None', 'local_address', 'str | None', 'socket_options', 'typing.Iterable[SOCKET_OPTION] | None', 'return', 'AsyncNetworkStream')):
        pass
    # WARNING: Decompyle incomplete

    
    async def connect_unix_socket(self = None, path = None, timeout = None, socket_options = (None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    async def sleep(self = None, seconds = None):
        pass
    # WARNING: Decompyle incomplete
