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
from _backends.base import NetworkStream
from _exceptions import ConnectionNotAvailable, LocalProtocolError, RemoteProtocolError
from _models import Origin, Request, Response
from _synchronization import Lock, Semaphore, ShieldCancellation
from _trace import Trace
from interfaces import ConnectionInterface
logger = logging.getLogger('httpcore.http2')

def has_body_headers(request = None):
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(request.headers())


class HTTPConnectionState(enum.IntEnum):
    ACTIVE = 1
    IDLE = 2
    CLOSED = 3


class HTTP2Connection(ConnectionInterface):
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
        self._init_lock = Lock()
        self._state_lock = Lock()
        self._read_lock = Lock()
        self._write_lock = Lock()
        self._sent_connection_init = False
        self._used_all_stream_ids = False
        self._connection_error = False
        self._events = { }
        self._connection_terminated = None
        self._read_exception = None
        self._write_exception = None

    
    def handle_request(self = None, request = None):
        if not self.can_handle_request(request.url.origin):
            raise RuntimeError(f'''Attempted to send request to {request.url.origin} on connection to {self._origin}''')
        self._state_lock
        if self._state in (HTTPConnectionState.ACTIVE, HTTPConnectionState.IDLE):
            None = self, self._request_count += 1, ._request_count
            self._state = HTTPConnectionState.ACTIVE
        else:
            raise ConnectionNotAvailable()
        None(None, None)
    # WARNING: Decompyle incomplete

    
    def _send_connection_init(self = None, request = None):
        '''
        The HTTP/2 connection requires some initial setup before we can start
        using individual request/response streams on it.
        '''
        self._h2_state.local_settings = h2.settings.Settings(client = True, initial_values = {
            h2.settings.SettingCodes.MAX_HEADER_LIST_SIZE: 65536,
            h2.settings.SettingCodes.MAX_CONCURRENT_STREAMS: 100,
            h2.settings.SettingCodes.ENABLE_PUSH: 0 })
        del self._h2_state.local_settings[h2.settings.SettingCodes.ENABLE_CONNECT_PROTOCOL]
        self._h2_state.initiate_connection()
        self._h2_state.increment_flow_control_window(16777216)
        self._write_outgoing_data(request)

    
    def _send_request_headers(self = None, request = None, stream_id = None):
        '''
        Send the request headers to a given stream ID.
        '''
        end_stream = not has_body_headers(request)
        authority = request.headers()[0]
        headers = (lambda .0: pass# WARNING: Decompyle incomplete
) + request.headers()
        self._h2_state.send_headers(stream_id, headers, end_stream = end_stream)
        self._h2_state.increment_flow_control_window(16777216, stream_id = stream_id)
        self._write_outgoing_data(request)

    
    def _send_request_body(self = None, request = None, stream_id = None):
        '''
        Iterate over the request body sending it to a given stream ID.
        '''
        if not has_body_headers(request):
            return None
    # WARNING: Decompyle incomplete

    
    def _send_stream_data(self = None, request = None, stream_id = None, data = ('request', 'Request', 'stream_id', 'int', 'data', 'bytes', 'return', 'None')):
        '''
        Send a single chunk of data in one or more data frames.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _send_end_stream(self = None, request = None, stream_id = None):
        '''
        Send an empty data frame on on a given stream ID with the END_STREAM flag set.
        '''
        self._h2_state.end_stream(stream_id)
        self._write_outgoing_data(request)

    
    def _receive_response(self = None, request = None, stream_id = None):
        '''
        Return the response status code and headers for a given stream ID.
        '''
        event = self._receive_stream_event(request, stream_id)
        if isinstance(event, h2.events.ResponseReceived):
            pass
        
        status_code = 200
        headers = []
    # WARNING: Decompyle incomplete

    
    def _receive_response_body(self = None, request = None, stream_id = None):
        '''
        Iterator that returns the bytes of the response body for a given stream ID.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _receive_stream_event(self = None, request = None, stream_id = None):
        '''
        Return the next available event for a given stream ID.

        Will read more data from the network if required.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _receive_events(self = None, request = None, stream_id = None):
        '''
        Read some data from the network until we see one or more events
        for a given stream ID.
        '''
        self._read_lock
    # WARNING: Decompyle incomplete

    
    def _receive_remote_settings_change(self = None, event = None):
        max_concurrent_streams = event.changed_settings.get(h2.settings.SettingCodes.MAX_CONCURRENT_STREAMS)
    # WARNING: Decompyle incomplete

    
    def _response_closed(self = None, stream_id = None):
        self._max_streams_semaphore.release()
        del self._events[stream_id]
        self._state_lock
        if not self._connection_terminated and self._events:
            self.close()
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        self._h2_state.close_connection()
        self._state = HTTPConnectionState.CLOSED
        self._network_stream.close()

    
    def _read_incoming_data(self = None, request = None):
        timeouts = request.extensions.get('timeout', { })
        timeout = timeouts.get('read', None)
    # WARNING: Decompyle incomplete

    
    def _write_outgoing_data(self = None, request = None):
        timeouts = request.extensions.get('timeout', { })
        timeout = timeouts.get('write', None)
        self._write_lock
        data_to_send = self._h2_state.data_to_send()
    # WARNING: Decompyle incomplete

    
    def _wait_for_outgoing_flow(self = None, request = None, stream_id = None):
        '''
        Returns the maximum allowable outgoing flow for a given stream.

        If the allowable flow is zero, then waits on the network until
        WindowUpdated frames have increased the flow rate.
        https://tools.ietf.org/html/rfc7540#section-6.9
        '''
        local_flow = self._h2_state.local_flow_control_window(stream_id)
        max_frame_size = self._h2_state.max_outbound_frame_size
        flow = min(local_flow, max_frame_size)
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
