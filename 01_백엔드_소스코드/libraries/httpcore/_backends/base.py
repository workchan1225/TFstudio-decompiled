# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

from __future__ import annotations
import ssl
import time
import typing
SOCKET_OPTION = typing.Union[(typing.Tuple[(int, int, int)], typing.Tuple[(int, int, typing.Union[(bytes, bytearray)])], typing.Tuple[(int, int, None, int)])]

class NetworkStream:
    
    def read(self = None, max_bytes = None, timeout = None):
        raise NotImplementedError()

    
    def write(self = None, buffer = None, timeout = None):
        raise NotImplementedError()

    
    def close(self = None):
        raise NotImplementedError()

    
    def start_tls(self = None, ssl_context = None, server_hostname = None, timeout = (None, None)):
        raise NotImplementedError()

    
    def get_extra_info(self = None, info = None):
        pass



class NetworkBackend:
    
    def connect_tcp(self, host = None, port = None, timeout = None, local_address = (None, None, None), socket_options = ('host', 'str', 'port', 'int', 'timeout', 'float | None', 'local_address', 'str | None', 'socket_options', 'typing.Iterable[SOCKET_OPTION] | None', 'return', 'NetworkStream')):
        raise NotImplementedError()

    
    def connect_unix_socket(self = None, path = None, timeout = None, socket_options = (None, None)):
        raise NotImplementedError()

    
    def sleep(self = None, seconds = None):
        time.sleep(seconds)



class AsyncNetworkStream:
    
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
        pass



class AsyncNetworkBackend:
    
    async def connect_tcp(self, host = None, port = None, timeout = None, local_address = (None, None, None), socket_options = ('host', 'str', 'port', 'int', 'timeout', 'float | None', 'local_address', 'str | None', 'socket_options', 'typing.Iterable[SOCKET_OPTION] | None', 'return', 'AsyncNetworkStream')):
        pass
    # WARNING: Decompyle incomplete

    
    async def connect_unix_socket(self = None, path = None, timeout = None, socket_options = (None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    async def sleep(self = None, seconds = None):
        pass
    # WARNING: Decompyle incomplete
