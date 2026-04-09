# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: anyio.pyc (Python 3.11)

from __future__ import annotations
import ssl
import typing
import anyio
from _exceptions import ConnectError, ConnectTimeout, ReadError, ReadTimeout, WriteError, WriteTimeout, map_exceptions
from _utils import is_socket_readable
from base import SOCKET_OPTION, AsyncNetworkBackend, AsyncNetworkStream

class AnyIOStream(AsyncNetworkStream):
    
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
        if info == 'ssl_object':
            return self._stream.extra(anyio.streams.tls.TLSAttribute.ssl_object, None)
        if None == 'client_addr':
            return self._stream.extra(anyio.abc.SocketAttribute.local_address, None)
        if None == 'server_addr':
            return self._stream.extra(anyio.abc.SocketAttribute.remote_address, None)
        if None == 'socket':
            return self._stream.extra(anyio.abc.SocketAttribute.raw_socket, None)
        if None == 'is_readable':
            sock = self._stream.extra(anyio.abc.SocketAttribute.raw_socket, None)
            return is_socket_readable(sock)



class AnyIOBackend(AsyncNetworkBackend):
    
    async def connect_tcp(self, host = None, port = None, timeout = None, local_address = (None, None, None), socket_options = ('host', 'str', 'port', 'int', 'timeout', 'float | None', 'local_address', 'str | None', 'socket_options', 'typing.Iterable[SOCKET_OPTION] | None', 'return', 'AsyncNetworkStream')):
        pass
    # WARNING: Decompyle incomplete

    
    async def connect_unix_socket(self = None, path = None, timeout = None, socket_options = (None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    async def sleep(self = None, seconds = None):
        pass
    # WARNING: Decompyle incomplete
