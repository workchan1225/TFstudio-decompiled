# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: trio.pyc (Python 3.11)

from __future__ import annotations
import ssl
import typing
import trio
from _exceptions import ConnectError, ConnectTimeout, ExceptionMapping, ReadError, ReadTimeout, WriteError, WriteTimeout, map_exceptions
from base import SOCKET_OPTION, AsyncNetworkBackend, AsyncNetworkStream

class TrioStream(AsyncNetworkStream):
    
    def __init__(self = None, stream = None):
        self._stream = stream

    
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
        if info == 'ssl_object' and isinstance(self._stream, trio.SSLStream):
            return self._stream._ssl_object
        if None == 'client_addr':
            return self._get_socket_stream().socket.getsockname()
        if None == 'server_addr':
            return self._get_socket_stream().socket.getpeername()
    # WARNING: Decompyle incomplete

    
    def _get_socket_stream(self = None):
        stream = self._stream
    # WARNING: Decompyle incomplete



class TrioBackend(AsyncNetworkBackend):
    
    async def connect_tcp(self, host = None, port = None, timeout = None, local_address = (None, None, None), socket_options = ('host', 'str', 'port', 'int', 'timeout', 'float | None', 'local_address', 'str | None', 'socket_options', 'typing.Iterable[SOCKET_OPTION] | None', 'return', 'AsyncNetworkStream')):
        pass
    # WARNING: Decompyle incomplete

    
    async def connect_unix_socket(self = None, path = None, timeout = None, socket_options = (None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    async def sleep(self = None, seconds = None):
        pass
    # WARNING: Decompyle incomplete
