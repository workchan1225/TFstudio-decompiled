# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base_protocol.pyc (Python 3.11)

import asyncio
from typing import Optional, cast
from client_exceptions import ClientConnectionResetError
from helpers import set_exception
from tcp_helpers import tcp_nodelay

class BaseProtocol(asyncio.Protocol):
    __slots__ = ('_loop', '_paused', '_drain_waiter', '_connection_lost', '_reading_paused', 'transport')
    
    def __init__(self = None, loop = None):
        self._loop = loop
        self._paused = False
        self._drain_waiter = None
        self._reading_paused = False
        self.transport = None

    connected = (lambda self = None: self.transport is not None)()
    writing_paused = (lambda self = None: self._paused)()
    
    def pause_writing(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def resume_writing(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def pause_reading(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def resume_reading(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def connection_made(self = None, transport = None):
        tr = cast(asyncio.Transport, transport)
        tcp_nodelay(tr, True)
        self.transport = tr

    
    def connection_lost(self = None, exc = None):
        self.transport = None
        if not self._paused:
            return None
        waiter = None._drain_waiter
    # WARNING: Decompyle incomplete

    
    async def _drain_helper(self = None):
        pass
    # WARNING: Decompyle incomplete
