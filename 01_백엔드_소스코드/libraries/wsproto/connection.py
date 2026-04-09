# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: connection.pyc (Python 3.11)

'''
wsproto/connection
~~~~~~~~~~~~~~~~~~

An implementation of a WebSocket connection.
'''
from __future__ import annotations
from collections import deque
from enum import Enum
from typing import TYPE_CHECKING
from events import BytesMessage, CloseConnection, Event, Message, Ping, Pong, TextMessage
from frame_protocol import CloseReason, FrameProtocol, Opcode, ParseFailed
from utilities import LocalProtocolError
if TYPE_CHECKING:
    from collections.abc import Generator
    from extensions import Extension

class ConnectionState(Enum):
    '''
    RFC 6455, Section 4 - Opening Handshake
    '''
    CONNECTING = 0
    OPEN = 1
    REMOTE_CLOSING = 2
    LOCAL_CLOSING = 3
    CLOSED = 4
    REJECTING = 5


class ConnectionType(Enum):
    '''An enumeration of connection types.'''
    CLIENT = 1
    SERVER = 2

CLIENT = ConnectionType.CLIENT
SERVER = ConnectionType.SERVER

class Connection:
    '''
    A low-level WebSocket connection object.

    This wraps two other protocol objects, an HTTP/1.1 protocol object used
    to do the initial HTTP upgrade handshake and a WebSocket frame protocol
    object used to exchange messages and other control frames.
    '''
    
    def __init__(self = None, connection_type = None, extensions = None, trailing_data = (None, b'')):
