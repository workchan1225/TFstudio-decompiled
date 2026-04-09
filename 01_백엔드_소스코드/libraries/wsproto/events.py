# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: events.pyc (Python 3.11)

'''
wsproto/events
~~~~~~~~~~~~~~

Events that result from processing data on a WebSocket connection.
'''
from __future__ import annotations
from abc import ABC
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Generic, TypeVar
if TYPE_CHECKING:
    from collections.abc import Sequence
    from extensions import Extension
    from typing import Headers

class Event(ABC):
    '''
    Base class for wsproto events.
    '''
    pass

Request = <NODE:12>()
AcceptConnection = <NODE:12>()
RejectConnection = <NODE:12>()
RejectData = <NODE:12>()
CloseConnection = <NODE:12>()
T = TypeVar('T', bytes | bytearray, str)

def Message():
    '''Message'''
    data: 'T' = '\n    The websocket data message.\n\n    Fields:\n\n    .. attribute:: data\n\n       (Required) The message data as byte string, can be decoded as UTF-8 for\n       TEXT messages.  This only represents a single chunk of data and\n       not a full WebSocket message.  You need to buffer and\n       reassemble these chunks to get the full message.\n\n    .. attribute:: frame_finished\n\n       This has no semantic content, but is provided just in case some\n       weird edge case user wants to be able to reconstruct the\n       fragmentation pattern of the original stream.\n\n    .. attribute:: message_finished\n\n       True if this frame is the last one of this message, False if\n       more frames are expected.\n\n    '
    frame_finished: 'bool' = True
    message_finished: 'bool' = True

Message = <NODE:27>(Message, 'Message', Event, Generic[T])()

def TextMessage():
    '''TextMessage'''
    __doc__ = '\n    Fired when a data frame with TEXT payload is received.\n\n    Fields:\n\n    .. attribute:: data\n\n       The message data as string, This only represents a single chunk\n       of data and not a full WebSocket message.  You need to buffer\n       and reassemble these chunks to get the full message.\n    '

TextMessage = <NODE:27>(TextMessage, 'TextMessage', Message[str])()

def BytesMessage():
    '''BytesMessage'''
    __doc__ = '\n    Fired when a data frame with BINARY payload is received.\n\n    Fields:\n\n    .. attribute:: data\n\n       The message data as bytes or a bytearray, can be decoded as UTF-8 for\n       TEXT messages.  This only represents a single chunk of data and\n       not a full WebSocket message.  You need to buffer and\n       reassemble these chunks to get the full message.\n    '

BytesMessage = <NODE:27>(BytesMessage, 'BytesMessage', Message[bytearray | bytes])()
Ping = <NODE:12>()
Pong = <NODE:12>()
