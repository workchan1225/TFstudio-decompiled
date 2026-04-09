# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _asyncio_selector_thread.pyc (Python 3.11)

from __future__ import annotations
import asyncio
import socket
import threading
from collections.abc import Callable
from selectors import EVENT_READ, EVENT_WRITE, DefaultSelector
from typing import TYPE_CHECKING, Any
if TYPE_CHECKING:
    from _typeshed import FileDescriptorLike
_selector_lock = threading.Lock()
_selector: 'Selector | None' = None

class Selector:
    
    def __init__(self = None):
        self._thread = threading.Thread(target = self.run, name = 'AnyIO socket selector')
        self._selector = DefaultSelector()
        (self._send, self._receive) = socket.socketpair()
        self._send.setblocking(False)
        self._receive.setblocking(False)
        self._receive.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1)
        self._send.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1)
        
        try:
            self._send.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        except OSError:
            pass

        self._selector.register(self._receive, EVENT_READ)
        self._closed = False

    
    def start(self = None):
        self._thread.start()
        threading._register_atexit(self._stop)

    
    def _stop(self = None):
        global _selector
        self._closed = True
        self._notify_self()
        self._send.close()
        self._thread.join()
        self._selector.unregister(self._receive)
        self._receive.close()
        self._selector.close()
        _selector = None
    # WARNING: Decompyle incomplete

    
    def _notify_self(self = None):
        
        try:
            self._send.send(b'\x00')
            return None
        except BlockingIOError:
            return None


    
    def add_reader(self = None, fd = None, callback = None):
        loop = asyncio.get_running_loop()
        
        try:
            key = self._selector.get_key(fd)
            if EVENT_READ in key.data:
                raise ValueError('this file descriptor is already registered for reading')
            key.data[EVENT_READ] = (loop, callback)
            self._selector.modify(fd, key.events | EVENT_READ, key.data)
        except KeyError:
            self._selector.register(fd, EVENT_READ, {
                EVENT_READ: (loop, callback) })

        self._notify_self()

    
    def add_writer(self = None, fd = None, callback = None):
        loop = asyncio.get_running_loop()
        
        try:
            key = self._selector.get_key(fd)
            if EVENT_WRITE in key.data:
                raise ValueError('this file descriptor is already registered for writing')
            key.data[EVENT_WRITE] = (loop, callback)
            self._selector.modify(fd, key.events | EVENT_WRITE, key.data)
        except KeyError:
            self._selector.register(fd, EVENT_WRITE, {
                EVENT_WRITE: (loop, callback) })

        self._notify_self()

    
    def remove_reader(self = None, fd = None):
        
        try:
            key = self._selector.get_key(fd)
        except KeyError:
            return False

        new_events = key.events ^ EVENT_READ
        if key.events ^ EVENT_READ:
            del key.data[EVENT_READ]
            self._selector.modify(fd, new_events, key.data)
        else:
            self._selector.unregister(fd)
        return True

    
    def remove_writer(self = None, fd = None):
        
        try:
            key = self._selector.get_key(fd)
        except KeyError:
            return False

        new_events = key.events ^ EVENT_WRITE
        if key.events ^ EVENT_WRITE:
            del key.data[EVENT_WRITE]
            self._selector.modify(fd, new_events, key.data)
        else:
            self._selector.unregister(fd)
        return True

    
    def run(self = None):
        pass
    # WARNING: Decompyle incomplete



def get_selector():
    _selector_lock
# WARNING: Decompyle incomplete
