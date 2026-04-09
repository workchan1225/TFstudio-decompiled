# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
wsproto
~~~~~~~

A WebSocket implementation.
'''
from __future__ import annotations
from typing import TYPE_CHECKING
from connection import Connection, ConnectionState, ConnectionType
from handshake import H11Handshake
if TYPE_CHECKING:
    from collections.abc import Generator
    from events import Event
    from typing import Headers
__version__ = '1.3.2'

class WSConnection:
    '''
    Represents the local end of a WebSocket connection to a remote peer.
    '''
    
    def __init__(self = None, connection_type = None):
        '''
        Constructor

        :param wsproto.connection.ConnectionType connection_type: Controls
            whether the library behaves as a client or as a server.
        '''
        self.client = connection_type is ConnectionType.CLIENT
        self.handshake = H11Handshake(connection_type)
        self.connection = None

    state = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def initiate_upgrade_connection(self = None, headers = None, path = None):
        self.handshake.initiate_upgrade_connection(headers, path)

    
    def send(self = None, event = None):
        '''
        Generate network data for the specified event.

        When you want to communicate with a WebSocket peer, you should construct
        an event and pass it to this method. This method will return the bytes
        that you should send to the peer.

        :param wsproto.events.Event event: The event to generate data for
        :returns bytes: The data to send to the peer
        '''
        data = b''
    # WARNING: Decompyle incomplete

    
    def receive_data(self = None, data = None):
        '''
        Feed network data into the connection instance.

        After calling this method, you should call :meth:`events` to see if the
        received data triggered any new events.

        :param bytes data: Data received from remote peer
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def events(self = None):
        '''
        A generator that yields pending events.

        Each event is an instance of a subclass of
        :class:`wsproto.events.Event`.
        '''
        pass
    # WARNING: Decompyle incomplete


__all__ = ('ConnectionType', 'WSConnection')
