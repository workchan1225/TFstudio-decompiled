# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: auto.pyc (Python 3.11)

from __future__ import annotations
import typing
from _synchronization import current_async_library
from base import SOCKET_OPTION, AsyncNetworkBackend, AsyncNetworkStream

class AutoBackend(AsyncNetworkBackend):
    
    async def _init_backend(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def connect_tcp(self, host = None, port = None, timeout = None, local_address = (None, None, None), socket_options = ('host', 'str', 'port', 'int', 'timeout', 'float | None', 'local_address', 'str | None', 'socket_options', 'typing.Iterable[SOCKET_OPTION] | None', 'return', 'AsyncNetworkStream')):
        pass
    # WARNING: Decompyle incomplete

    
    async def connect_unix_socket(self = None, path = None, timeout = None, socket_options = (None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    async def sleep(self = None, seconds = None):
        pass
    # WARNING: Decompyle incomplete
