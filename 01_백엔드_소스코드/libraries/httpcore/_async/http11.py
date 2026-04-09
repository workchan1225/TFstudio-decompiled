# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: http11.pyc (Python 3.11)

from __future__ import annotations
import enum
import logging
import ssl
import time
import types
import typing
import h11
from _backends.base import AsyncNetworkStream
from _exceptions import ConnectionNotAvailable, LocalProtocolError, RemoteProtocolError, WriteError, map_exceptions
from _models import Origin, Request, Response
from _synchronization import AsyncLock, AsyncShieldCancellation
from _trace import Trace
from interfaces import AsyncConnectionInterface
logger = logging.getLogger('httpcore.http11')
H11SendEvent = typing.Union[(h11.Request, h11.Data, h11.EndOfMessage)]

class HTTPConnectionState(enum.IntEnum):
    NEW = 0
    ACTIVE = 1
    IDLE = 2
    CLOSED = 3


class AsyncHTTP11Connection(AsyncConnectionInterface):
    READ_NUM_BYTES = 65536
    MAX_INCOMPLETE_EVENT_SIZE = 102400
    
    def __init__(self = None, origin = None, stream = None, keepalive_expiry = (None,)):
        self._origin = origin
        self._network_stream = stream
        self._keepalive_expiry = keepalive_expiry
        self._expire_at = None
        self._state = HTTPConnectionState.NEW
        self._state_lock = AsyncLock()
        self._request_count = 0
        self._h11_state = h11.Connection(our_role = h11.CLIENT, max_incomplete_event_size = self.MAX_INCOMPLETE_EVENT_SIZE)

    
    async def handle_async_request(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _send_request_headers(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _send_request_body(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _send_event(self = None, event = None, timeout = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _receive_response_headers(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _receive_response_body(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _receive_event(self = None, timeout = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _response_closed(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def aclose(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def can_handle_request(self = None, origin = None):
        return origin == self._origin

    
    def is_available(self = None):
        return self._state == HTTPConnectionState.IDLE

    
    def has_expired(self = None):
