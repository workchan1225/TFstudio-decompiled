# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: connection.pyc (Python 3.11)

from __future__ import annotations
import contextlib
import logging
import random
import socket
import struct
import threading
import time
import uuid
from collections.abc import Iterable, Iterator, Mapping
from types import TracebackType
from typing import Any, Literal, overload
from exceptions import ConcurrencyError, ConnectionClosed, ConnectionClosedOK, ProtocolError
from frames import DATA_OPCODES, BytesLike, CloseCode, Frame, Opcode
from http11 import Request, Response
from protocol import CLOSED, OPEN, Event, Protocol, State
from typing import Data, LoggerLike, Subprotocol
from messages import Assembler
from utils import Deadline
__all__ = [
    'Connection']

class Connection:
    """
    :mod:`threading` implementation of a WebSocket connection.

    :class:`Connection` provides APIs shared between WebSocket servers and
    clients.

    You shouldn't use it directly. Instead, use
    :class:`~websockets.sync.client.ClientConnection` or
    :class:`~websockets.sync.server.ServerConnection`.

    """
    recv_bufsize = 65536
    
    def __init__(self = None, socket = None, protocol = None, *, ping_interval, ping_timeout, close_timeout, max_queue):
        self.socket = socket
        self.protocol = protocol
        self.ping_interval = ping_interval
        self.ping_timeout = ping_timeout
        self.close_timeout = close_timeout
    # WARNING: Decompyle incomplete

    local_address = (lambda self = None: self.socket.getsockname())()
    remote_address = (lambda self = None: self.socket.getpeername())()
    state = (lambda self = None: self.protocol.state)()
    subprotocol = (lambda self = None: self.protocol.subprotocol)()
    close_code = (lambda self = None: self.protocol.close_code)()
    close_reason = (lambda self = None: self.protocol.close_reason)()
    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def __iter__(self = None):
        '''
        Iterate on incoming messages.

        The iterator calls :meth:`recv` and yields messages in an infinite loop.

        It exits when the connection is closed normally. It raises a
        :exc:`~websockets.exceptions.ConnectionClosedError` exception after a
        protocol error or a network failure.

        '''
        pass
    # WARNING: Decompyle incomplete

    recv = (lambda self = None, timeout = None, decode = overload: pass)()
    recv = (lambda self = None, timeout = None, decode = overload: pass)()
    recv = (lambda self = None, timeout = None, *, decode,
