# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: protocol.pyc (Python 3.11)

from __future__ import annotations
import enum
import logging
import uuid
from collections.abc import Generator
from typing import Union
from exceptions import ConnectionClosed, ConnectionClosedError, ConnectionClosedOK, InvalidState, PayloadTooBig, ProtocolError
from extensions import Extension
from frames import OK_CLOSE_CODES, OP_BINARY, OP_CLOSE, OP_CONT, OP_PING, OP_PONG, OP_TEXT, Close, CloseCode, Frame
from http11 import Request, Response
from streams import StreamReader
from typing import LoggerLike, Origin, Subprotocol
__all__ = [
    'Protocol',
    'Side',
    'State',
    'SEND_EOF']
Event = Union[(Request, Response, Frame)]

class Side(enum.IntEnum):
    '''A WebSocket connection is either a server or a client.'''
    (SERVER, CLIENT) = range(2)

SERVER = Side.SERVER
CLIENT = Side.CLIENT

class State(enum.IntEnum):
    '''A WebSocket connection is in one of these four states.'''
    (CONNECTING, OPEN, CLOSING, CLOSED) = range(4)

CONNECTING = State.CONNECTING
OPEN = State.OPEN
CLOSING = State.CLOSING
CLOSED = State.CLOSED
SEND_EOF = b''

class Protocol:
    '''
    Sans-I/O implementation of a WebSocket connection.

    Args:
        side: :attr:`~Side.CLIENT` or :attr:`~Side.SERVER`.
        state: Initial state of the WebSocket connection.
        max_size: Maximum size of incoming messages in bytes;
            :obj:`None` disables the limit.
        logger: Logger for this connection; depending on ``side``,
            defaults to ``logging.getLogger("websockets.client")``
            or ``logging.getLogger("websockets.server")``;
            see the :doc:`logging guide <../../topics/logging>` for details.

    '''
    
    def __init__(self = None, side = None, *, state, max_size, logger):
        self.id = uuid.uuid4()
    # WARNING: Decompyle incomplete

    state = (lambda self = None: self._state)()
    state = (lambda self = None, state = None: if self.debug:
self.logger.debug('= connection is %s', state.name)self._state = state)()
    close_code = (lambda self = None: if self.state is not CLOSED:
None# WARNING: Decompyle incomplete
)()
    close_reason = (lambda self = None: if self.state is not CLOSED:
None# WARNING: Decompyle incomplete
)()
    close_exc = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def receive_data(self = None, data = None):
        '''
        Receive data from the network.

        After calling this method:

        - You must call :meth:`data_to_send` and send this data to the network.
        - You should call :meth:`events_received` and process resulting events.

        Raises:
            EOFError: If :meth:`receive_eof` was called earlier.

        '''
        self.reader.feed_data(data)
        next(self.parser)

    
    def receive_eof(self = None):
        '''
        Receive the end of the data stream from the network.

        After calling this method:

        - You must call :meth:`data_to_send` and send this data to the network;
          it will return ``[b""]``, signaling the end of the stream, or ``[]``.
        - You aren\'t expected to call :meth:`events_received`; it won\'t return
          any new events.

        :meth:`receive_eof` is idempotent.

        '''
        if self.reader.eof:
            return None
        None.reader.feed_eof()
        next(self.parser)

    
    def send_continuation(self = None, data = None, fin = None):
        """
        Send a `Continuation frame`_.

        .. _Continuation frame:
            https://datatracker.ietf.org/doc/html/rfc6455#section-5.6

        Parameters:
            data: payload containing the same kind of data
                as the initial frame.
            fin: FIN bit; set it to :obj:`True` if this is the last frame
                of a fragmented message and to :obj:`False` otherwise.

        Raises:
            ProtocolError: If a fragmented message isn't in progress.

        """
        if not self.expect_continuation_frame:
            raise ProtocolError('unexpected continuation frame')
        if self._state is not OPEN:
            raise InvalidState(f'''connection is {self.state.name.lower()}''')
        self.expect_continuation_frame = not fin
        self.send_frame(Frame(OP_CONT, data, fin))

    
    def send_text(self = None, data = None, fin = None):
        '''
        Send a `Text frame`_.

        .. _Text frame:
            https://datatracker.ietf.org/doc/html/rfc6455#section-5.6

        Parameters:
            data: payload containing text encoded with UTF-8.
            fin: FIN bit; set it to :obj:`False` if this is the first frame of
                a fragmented message.

        Raises:
            ProtocolError: If a fragmented message is in progress.

        '''
        if self.expect_continuation_frame:
            raise ProtocolError('expected a continuation frame')
        if self._state is not OPEN:
            raise InvalidState(f'''connection is {self.state.name.lower()}''')
        self.expect_continuation_frame = not fin
        self.send_frame(Frame(OP_TEXT, data, fin))

    
    def send_binary(self = None, data = None, fin = None):
        '''
        Send a `Binary frame`_.

        .. _Binary frame:
            https://datatracker.ietf.org/doc/html/rfc6455#section-5.6

        Parameters:
            data: payload containing arbitrary binary data.
            fin: FIN bit; set it to :obj:`False` if this is the first frame of
                a fragmented message.

        Raises:
            ProtocolError: If a fragmented message is in progress.

        '''
        if self.expect_continuation_frame:
            raise ProtocolError('expected a continuation frame')
        if self._state is not OPEN:
            raise InvalidState(f'''connection is {self.state.name.lower()}''')
        self.expect_continuation_frame = not fin
        self.send_frame(Frame(OP_BINARY, data, fin))

    
    def send_close(self = None, code = None, reason = None):
        """
        Send a `Close frame`_.

        .. _Close frame:
            https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.1

        Parameters:
            code: close code.
            reason: close reason.

        Raises:
            ProtocolError: If the code isn't valid or if a reason is provided
                without a code.

        """
        if self._state is not OPEN:
            raise InvalidState(f'''connection is {self.state.name.lower()}''')
    # WARNING: Decompyle incomplete

    
    def send_ping(self = None, data = None):
        '''
        Send a `Ping frame`_.

        .. _Ping frame:
            https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.2

        Parameters:
            data: payload containing arbitrary binary data.

        '''
        if self._state is not OPEN and self._state is not CLOSING:
            raise InvalidState(f'''connection is {self.state.name.lower()}''')
        self.send_frame(Frame(OP_PING, data))

    
    def send_pong(self = None, data = None):
        '''
        Send a `Pong frame`_.

        .. _Pong frame:
            https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.3

        Parameters:
            data: payload containing arbitrary binary data.

        '''
        if self._state is not OPEN and self._state is not CLOSING:
            raise InvalidState(f'''connection is {self.state.name.lower()}''')
        self.send_frame(Frame(OP_PONG, data))

    
    def fail(self = None, code = None, reason = None):
        """
        `Fail the WebSocket connection`_.

        .. _Fail the WebSocket connection:
            https://datatracker.ietf.org/doc/html/rfc6455#section-7.1.7

        Parameters:
            code: close code
            reason: close reason

        Raises:
            ProtocolError: If the code isn't valid.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def events_received(self = None):
        '''
        Fetch events generated from data received from the network.

        Call this method immediately after any of the ``receive_*()`` methods.

        Process resulting events, likely by passing them to the application.

        Returns:
            Events read from the connection.
        '''
        events, self.events = self.events, []
        return events

    
    def data_to_send(self = None):
        '''
        Obtain data to send to the network.

        Call this method immediately after any of the ``receive_*()``,
        ``send_*()``, or :meth:`fail` methods.

        Write resulting data to the connection.

        The empty bytestring :data:`~websockets.protocol.SEND_EOF` signals
        the end of the data stream. When you receive it, half-close the TCP
        connection.

        Returns:
            Data to write to the connection.

        '''
        writes, self.writes = self.writes, []
        return writes

    
    def close_expected(self = None):
        """
        Tell if the TCP connection is expected to close soon.

        Call this method immediately after any of the ``receive_*()``,
        ``send_close()``, or :meth:`fail` methods.

        If it returns :obj:`True`, schedule closing the TCP connection after a
        short timeout if the other side hasn't already closed it.

        Returns:
            Whether the TCP connection is expected to close soon.

        """
        if self.state is OPEN:
            return False
        if None.state is CLOSING:
            return True
        if None.state is CLOSED:
            return False
    # WARNING: Decompyle incomplete

    
    def parse(self = None):
        '''
        Parse incoming data into frames.

        :meth:`receive_data` and :meth:`receive_eof` run this generator
        coroutine until it needs more data or reaches EOF.

        :meth:`parse` never raises an exception. Instead, it sets the
        :attr:`parser_exc` and yields control.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def discard(self = None):
        '''
        Discard incoming data.

        This coroutine replaces :meth:`parse`:

        - after receiving a close frame, during a normal closure (1.4);
        - after sending a close frame, during an abnormal closure (7.1.7).

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def recv_frame(self = None, frame = None):
        '''
        Process an incoming frame.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def send_frame(self = None, frame = None):
        if self.debug:
            self.logger.debug('> %s', frame)
        self.writes.append(frame.serialize(mask = self.side is CLIENT, extensions = self.extensions))

    
    def send_eof(self = None):
        pass
    # WARNING: Decompyle incomplete
