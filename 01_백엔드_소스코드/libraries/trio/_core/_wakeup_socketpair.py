# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _wakeup_socketpair.pyc (Python 3.11)

from __future__ import annotations
import contextlib
import signal
import socket
import warnings
from  import _core
from _util import is_main_thread

class WakeupSocketpair:
    
    def __init__(self = None):
        self
        self
        (self.wakeup_sock, self.write_sock) = socket.socketpair()
        self.wakeup_sock.setblocking(False)
        self.write_sock.setblocking(False)
        self.wakeup_sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1)
        self.write_sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1)
        contextlib.suppress(OSError)
        self.write_sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        None(None, None)

    
    def wakeup_thread_and_signal_safe(self = None):
        contextlib.suppress(BlockingIOError)
        self.write_sock.send(b'\x00')
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    async def wait_woken(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def drain(self = None):
        
        try:
            self.wakeup_sock.recv(65536)
            continue
        except BlockingIOError:
            return None


    
    def wakeup_on_signals(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        self.wakeup_sock.close()
        self.write_sock.close()
    # WARNING: Decompyle incomplete
