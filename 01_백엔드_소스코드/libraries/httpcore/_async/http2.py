# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: http2.pyc (Python 3.11)

from __future__ import annotations
import enum
import logging
import time
import types
import typing
import h2.config as h2
import h2.connection as h2
import h2.events as h2
import h2.exceptions as h2
import h2.settings as h2
from _backends.base import AsyncNetworkStream
from _exceptions import ConnectionNotAvailable, LocalProtocolError, RemoteProtocolError
from _models import Origin, Request, Response
from _synchronization import AsyncLock, AsyncSemaphore, AsyncShieldCancellation
from _trace import Trace
from interfaces import AsyncConnectionInterface
logger = logging.getLogger('httpcore.http2')

def has_body_headers(request = None):
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(request.headers())


class HTTPConnectionState(enum.IntEnum):
    ACTIVE = 1
    IDLE = 2
    CLOSED = 3


class AsyncHTTP2Connection(AsyncConnectionInterface):
    READ_NUM_BYTES = 65536
    CONFIG = h2.config.H2Configuration(validate_inbound_headers = False)
    
    def __init__(self = None, origin = None, stream = None, keepalive_expiry = (None,)):
        self._origin = origin
        self._network_stream = stream
        self._keepalive_expiry = keepalive_expiry
        self._h2_state = h2.connection.H2Connection(config = self.CONFIG)
        self._state = HTTPConnectionState.IDLE
        self._expire_at = None
        self._request_count = 0
        self._init_lock = AsyncLock()
        self._state_lock = AsyncLock()
        self._read_lock = AsyncLock()
        self._write_lock = AsyncLock()
        self._sent_connection_init = False
        self._used_all_stream_ids = False
        self._connection_error = False
        self._events = { }
        self._connection_terminated = None
        self._read_exception = None
        self._write_exception = None

    
    async def handle_async_request(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _send_connection_init(self = None, request = None):
        '''
        The HTTP/2 connection requires some initial setup before we can start
        using individual request/response streams on it.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _send_request_headers(self = None, request = None, stream_id = None):
        '''
        Send the request headers to a given stream ID.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _send_request_body(self = None, request = None, stream_id = None):
        '''
        Iterate over the request body sending it to a given stream ID.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _send_stream_data(self = None, request = None, stream_id = None, data = ('request', 'Request', 'stream_id', 'int', 'data', 'bytes', 'return', 'None')):
        '''
        Send a single chunk of data in one or more data frames.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _send_end_stream(self = None, request = None, stream_id = None):
        '''
        Send an empty data frame on on a given stream ID with the END_STREAM flag set.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _receive_response(self = None, request = None, stream_id = None):
        '''
        Return the response status code and headers for a given stream ID.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _receive_response_body(self = None, request = None, stream_id = None):
        '''
        Iterator that returns the bytes of the response body for a given stream ID.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _receive_stream_event(self = None, request = None, stream_id = None):
        '''
        Return the next available event for a given stream ID.

        Will read more data from the network if required.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _receive_events(self = None, request = None, stream_id = None):
        '''
        Read some data from the network until we see one or more events
        for a given stream ID.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _receive_remote_settings_change(self = None, event = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _response_closed(self = None, stream_id = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def aclose(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _read_incoming_data(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _write_outgoing_data(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _wait_for_outgoing_flow(self = None, request = None, stream_id = None):
        '''
        Returns the maximum allowable outgoing flow for a given stream.

        If the allowable flow is zero, then waits on the network until
        WindowUpdated frames have increased the flow rate.
        https://tools.ietf.org/html/rfc7540#section-6.9
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def can_handle_request(self = None, origin = None):
        return origin == self._origin

    
    def is_available(self = None):
        if self._state != HTTPConnectionState.CLOSED:
            if not (self._connection_error):
                if not (self._used_all_stream_ids):
                    pass
        return not (self._h2_state.state_machine.state == h2.connection.ConnectionState.CLOSED)

    
    def has_expired(self = None):
