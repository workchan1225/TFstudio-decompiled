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
from _backends.base import NetworkStream
from _exceptions import ConnectionNotAvailable, LocalProtocolError, RemoteProtocolError, WriteError, map_exceptions
from _models import Origin, Request, Response
from _synchronization import Lock, ShieldCancellation
from _trace import Trace
from interfaces import ConnectionInterface
logger = logging.getLogger('httpcore.http11')
H11SendEvent = typing.Union[(h11.Request, h11.Data, h11.EndOfMessage)]

class HTTPConnectionState(enum.IntEnum):
    NEW = 0
    ACTIVE = 1
    IDLE = 2
    CLOSED = 3


class HTTP11Connection(ConnectionInterface):
    READ_NUM_BYTES = 65536
    MAX_INCOMPLETE_EVENT_SIZE = 102400
    
    def __init__(self = None, origin = None, stream = None, keepalive_expiry = (None,)):
        self._origin = origin
        self._network_stream = stream
        self._keepalive_expiry = keepalive_expiry
        self._expire_at = None
        self._state = HTTPConnectionState.NEW
        self._state_lock = Lock()
        self._request_count = 0
        self._h11_state = h11.Connection(our_role = h11.CLIENT, max_incomplete_event_size = self.MAX_INCOMPLETE_EVENT_SIZE)

    
    def handle_request(self = None, request = None):
        if not self.can_handle_request(request.url.origin):
            raise RuntimeError(f'''Attempted to send request to {request.url.origin} on connection to {self._origin}''')
        self._state_lock
        if self._state in (HTTPConnectionState.NEW, HTTPConnectionState.IDLE):
            HTTPConnectionState.ACTIVE = self, self._request_count += 1, ._request_count
            self._expire_at = None
        else:
            raise ConnectionNotAvailable()
        None(None, None)
    # WARNING: Decompyle incomplete

    
    def _send_request_headers(self = None, request = None):
        timeouts = request.extensions.get('timeout', { })
        timeout = timeouts.get('write', None)
        map_exceptions({
            h11.LocalProtocolError: LocalProtocolError })
        event = h11.Request(method = request.method, target = request.url.target, headers = request.headers)
        None(None, None)

    
    def _send_request_body(self = None, request = None):
        timeouts = request.extensions.get('timeout', { })
        timeout = timeouts.get('write', None)
    # WARNING: Decompyle incomplete

    
    def _send_event(self = None, event = None, timeout = None):
        bytes_to_send = self._h11_state.send(event)
    # WARNING: Decompyle incomplete

    
    def _receive_response_headers(self = None, request = None):
        timeouts = request.extensions.get('timeout', { })
        timeout = timeouts.get('read', None)
        event = self._receive_event(timeout = timeout)
        if isinstance(event, h11.Response):
            pass
        elif isinstance(event, h11.InformationalResponse) and event.status_code == 101:
            pass
        
        http_version = b'HTTP/' + event.http_version
        headers = event.headers.raw_items()
        (trailing_data, _) = self._h11_state.trailing_data
        return (http_version, event.status_code, event.reason, headers, trailing_data)

    
    def _receive_response_body(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _receive_event(self = None, timeout = None):
