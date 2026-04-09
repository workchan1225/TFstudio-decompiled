# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: handshake.pyc (Python 3.11)

'''
wsproto/handshake
~~~~~~~~~~~~~~~~~~

An implementation of WebSocket handshakes.
'''
from __future__ import annotations
from collections import deque
from typing import TYPE_CHECKING, cast
import h11
from connection import Connection, ConnectionState, ConnectionType
from events import AcceptConnection, Event, RejectConnection, RejectData, Request
from extensions import Extension
from utilities import LocalProtocolError, RemoteProtocolError, generate_accept_token, generate_nonce, normed_header_dict, split_comma_header
if TYPE_CHECKING:
    from collections.abc import Generator, Iterable, Sequence
    from typing import Headers
WEBSOCKET_VERSION = b'13'
WEBSOCKET_UPGRADE = b'websocket'

class H11Handshake:
    '''A Handshake implementation for HTTP/1.1 connections.'''
    
    def __init__(self = None, connection_type = None):
        self.client = connection_type is ConnectionType.CLIENT
        self._state = ConnectionState.CONNECTING
        if self.client:
            self._h11_connection = h11.Connection(h11.CLIENT)
        else:
            self._h11_connection = h11.Connection(h11.SERVER)
        self._connection = None
        self._events = deque()
        self._initiating_request = None
        self._nonce = None

    state = (lambda self = None: self._state)()
    connection = (lambda self = None: self._connection)()
    
    def initiate_upgrade_connection(self = None, headers = None, path = None):
        '''
        Initiate an upgrade connection.

        This should be used if the request has already be received and
        parsed.

        :param list headers: HTTP headers represented as a list of 2-tuples.
        :param str path: A URL path.
        '''
        if self.client:
            msg = 'Cannot initiate an upgrade connection when acting as the client'
            raise LocalProtocolError(msg)
        upgrade_request = h11.Request(method = b'GET', target = path, headers = headers)
        h11_client = h11.Connection(h11.CLIENT)
        self.receive_data(h11_client.send(upgrade_request))

    
    def send(self = None, event = None):
        '''
        Send an event to the remote.

        This will return the bytes to send based on the event or raise
        a LocalProtocolError if the event is not valid given the
        state.

        :returns: Data to send to the WebSocket peer.
        :rtype: bytes
        '''
        data = b''
        if isinstance(event, Request):
            data += self._initiate_connection(event)
        elif isinstance(event, AcceptConnection):
            data += self._accept(event)
        elif isinstance(event, RejectConnection):
            data += self._reject(event)
        elif isinstance(event, RejectData):
            data += self._send_reject_data(event)
        else:
            msg = f'''Event {event} cannot be sent during the handshake'''
            raise LocalProtocolError(msg)
        return data

    
    def receive_data(self = None, data = None):
        '''
        Receive data from the remote.

        A list of events that the remote peer triggered by sending
        this data can be retrieved with :meth:`events`.

        :param bytes data: Data received from the WebSocket peer.
        '''
        if not data:
            self._h11_connection.receive_data(b'')
            
            try:
                event = self._h11_connection.next_event()
            except h11.RemoteProtocolError:
                self._h11_connection.receive_data
                msg = 'Bad HTTP message'
                raise RemoteProtocolError(msg, event_hint = RejectConnection())

            if isinstance(event, h11.ConnectionClosed) and event is h11.NEED_DATA or event is h11.PAUSED:
                return None
            if data.client:
                if isinstance(event, h11.InformationalResponse):
                    if event.status_code == 101:
                        self._events.append(self._establish_client_connection(event))
                    else:
                        self._events.append(RejectConnection(headers = list(event.headers), status_code = event.status_code, has_body = False))
                        self._state = ConnectionState.CLOSED
                elif isinstance(event, h11.Response):
                    self._state = ConnectionState.REJECTING
                    self._events.append(RejectConnection(headers = list(event.headers), status_code = event.status_code, has_body = True))
                elif isinstance(event, h11.Data):
                    self._events.append(RejectData(data = event.data, body_finished = False))
                elif isinstance(event, h11.EndOfMessage):
                    self._events.append(RejectData(data = b'', body_finished = True))
                    self._state = ConnectionState.CLOSED
                elif isinstance(event, h11.Request):
                    self._events.append(self._process_connection_request(event))
        continue

    
    def events(self = None):
        '''
        Return a generator that provides any events that have been generated
        by protocol activity.

        :returns: a generator that yields H11 events.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _process_connection_request(self = None, event = None):
        if event.method != b'GET':
            msg = 'Request method must be GET'
            raise RemoteProtocolError(msg, event_hint = RejectConnection())
        connection_tokens = None
        extensions = []
        host = None
        key = None
        subprotocols = []
        upgrade = b''
        version = None
        headers = []
    # WARNING: Decompyle incomplete

    
    def _accept(self = None, event = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _reject(self = None, event = None):
