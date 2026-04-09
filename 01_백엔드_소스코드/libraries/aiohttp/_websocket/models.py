# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: models.pyc (Python 3.11)

'''Models for WebSocket protocol versions 13 and 8.'''
import json
from enum import IntEnum
from typing import Any, Callable, Final, NamedTuple, Optional, cast
WS_DEFLATE_TRAILING: Final[bytes] = bytes([
    0,
    0,
    255,
    255])

class WSCloseCode(IntEnum):
    OK = 1000
    GOING_AWAY = 1001
    PROTOCOL_ERROR = 1002
    UNSUPPORTED_DATA = 1003
    ABNORMAL_CLOSURE = 1006
    INVALID_TEXT = 1007
    POLICY_VIOLATION = 1008
    MESSAGE_TOO_BIG = 1009
    MANDATORY_EXTENSION = 1010
    INTERNAL_ERROR = 1011
    SERVICE_RESTART = 1012
    TRY_AGAIN_LATER = 1013
    BAD_GATEWAY = 1014


class WSMsgType(IntEnum):
    CONTINUATION = 0
    TEXT = 1
    BINARY = 2
    PING = 9
    PONG = 10
    CLOSE = 8
    CLOSING = 256
    CLOSED = 257
    ERROR = 258
    text = TEXT
    binary = BINARY
    ping = PING
    pong = PONG
    close = CLOSE
    closing = CLOSING
    closed = CLOSED
    error = ERROR


class WSMessage(NamedTuple):
    extra: Optional[str] = 'WSMessage'
    
    def json(self = None, *, loads):
        '''Return parsed JSON data.

        .. versionadded:: 0.22
        '''
        return loads(self.data)


WS_CLOSED_MESSAGE = tuple.__new__(WSMessage, (WSMsgType.CLOSED, None, None))
WS_CLOSING_MESSAGE = tuple.__new__(WSMessage, (WSMsgType.CLOSING, None, None))

class WebSocketError(Exception):
    pass
# WARNING: Decompyle incomplete


class WSHandshakeError(Exception):
    '''WebSocket protocol handshake error.'''
    pass
