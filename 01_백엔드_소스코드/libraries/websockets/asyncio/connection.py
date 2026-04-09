# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: connection.pyc (Python 3.11)

from __future__ import annotations
import asyncio
import collections
import contextlib
import logging
import random
import struct
import sys
import traceback
import uuid
from collections.abc import AsyncIterable, AsyncIterator, Awaitable, Iterable, Mapping
from types import TracebackType
from typing import Any, Literal, cast, overload
from exceptions import ConcurrencyError, ConnectionClosed, ConnectionClosedOK, ProtocolError
from frames import DATA_OPCODES, BytesLike, CloseCode, Frame, Opcode
from http11 import Request, Response
from protocol import CLOSED, OPEN, Event, Protocol, State
from typing import Data, LoggerLike, Subprotocol
from compatibility import TimeoutError, aiter, anext, asyncio_timeout, asyncio_timeout_at
from messages import Assembler
__all__ = [
    'Connection']

class Connection(asyncio.Protocol):
    """
    :mod:`asyncio` implementation of a WebSocket connection.

    :class:`Connection` provides APIs shared between WebSocket servers and
    clients.

    You shouldn't use it directly. Instead, use
    :class:`~websockets.asyncio.client.ClientConnection` or
    :class:`~websockets.asyncio.server.ServerConnection`.

    """
    
    def __init__(self = None, protocol = None, *, ping_interval, ping_timeout, close_timeout, max_queue, write_limit):
        self.protocol = protocol
        self.ping_interval = ping_interval
        self.ping_timeout = ping_timeout
        self.close_timeout = close_timeout
    # WARNING: Decompyle incomplete

    local_address = (lambda self = None: self.transport.get_extra_info('sockname'))()
    remote_address = (lambda self = None: self.transport.get_extra_info('peername'))()
    state = (lambda self = None: self.protocol.state)()
    subprotocol = (lambda self = None: self.protocol.subprotocol)()
    close_code = (lambda self = None: self.protocol.close_code)()
    close_reason = (lambda self = None: self.protocol.close_reason)()
    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self = None):
        '''
        Iterate on incoming messages.

        The iterator calls :meth:`recv` and yields messages asynchronously in an
        infinite loop.

        It exits when the connection is closed normally. It raises a
        :exc:`~websockets.exceptions.ConnectionClosedError` exception after a
        protocol error or a network failure.

        '''
        pass
    # WARNING: Decompyle incomplete

    recv = (lambda self = None, decode = None: pass# WARNING: Decompyle incomplete
)()
    recv = (lambda self = None, decode = None: pass# WARNING: Decompyle incomplete
)()
    recv = (lambda self = None, decode = None: pass# WARNING: Decompyle incomplete
)()
    
    async def recv(self = None, decode = None):
        """
        Receive the next message.

        When the connection is closed, :meth:`recv` raises
        :exc:`~websockets.exceptions.ConnectionClosed`. Specifically, it raises
        :exc:`~websockets.exceptions.ConnectionClosedOK` after a normal closure
        and :exc:`~websockets.exceptions.ConnectionClosedError` after a protocol
        error or a network failure. This is how you detect the end of the
        message stream.

        Canceling :meth:`recv` is safe. There's no risk of losing data. The next
        invocation of :meth:`recv` will return the next message.

        This makes it possible to enforce a timeout by wrapping :meth:`recv` in
        :func:`~asyncio.timeout` or :func:`~asyncio.wait_for`.

        When the message is fragmented, :meth:`recv` waits until all fragments
        are received, reassembles them, and returns the whole message.

        Args:
            decode: Set this flag to override the default behavior of returning
                :class:`str` or :class:`bytes`. See below for details.

        Returns:
            A string (:class:`str`) for a Text_ frame or a bytestring
            (:class:`bytes`) for a Binary_ frame.

            .. _Text: https://datatracker.ietf.org/doc/html/rfc6455#section-5.6
            .. _Binary: https://datatracker.ietf.org/doc/html/rfc6455#section-5.6

            You may override this behavior with the ``decode`` argument:

            * Set ``decode=False`` to disable UTF-8 decoding of Text_ frames and
              return a bytestring (:class:`bytes`). This improves performance
              when decoding isn't needed, for example if the message contains
              JSON and you're using a JSON library that expects a bytestring.
            * Set ``decode=True`` to force UTF-8 decoding of Binary_ frames
              and return a string (:class:`str`). This may be useful for
              servers that send binary frames instead of text frames.

        Raises:
            ConnectionClosed: When the connection is closed.
            ConcurrencyError: If two coroutines call :meth:`recv` or
                :meth:`recv_streaming` concurrently.

        """
        pass
    # WARNING: Decompyle incomplete

    recv_streaming = (lambda self = None, decode = None: pass)()
    recv_streaming = (lambda self = None, decode = None: pass)()
    recv_streaming = (lambda self = None, decode = None: pass)()
    
    def recv_streaming(self = None, decode = None):
        """
        Receive the next message frame by frame.

        This method is designed for receiving fragmented messages. It returns an
        asynchronous iterator that yields each fragment as it is received. This
        iterator must be fully consumed. Else, future calls to :meth:`recv` or
        :meth:`recv_streaming` will raise
        :exc:`~websockets.exceptions.ConcurrencyError`, making the connection
        unusable.

        :meth:`recv_streaming` raises the same exceptions as :meth:`recv`.

        Canceling :meth:`recv_streaming` before receiving the first frame is
        safe. Canceling it after receiving one or more frames leaves the
        iterator in a partially consumed state, making the connection unusable.
        Instead, you should close the connection with :meth:`close`.

        Args:
            decode: Set this flag to override the default behavior of returning
                :class:`str` or :class:`bytes`. See below for details.

        Returns:
            An iterator of strings (:class:`str`) for a Text_ frame or
            bytestrings (:class:`bytes`) for a Binary_ frame.

            .. _Text: https://datatracker.ietf.org/doc/html/rfc6455#section-5.6
            .. _Binary: https://datatracker.ietf.org/doc/html/rfc6455#section-5.6

            You may override this behavior with the ``decode`` argument:

            * Set ``decode=False`` to disable UTF-8 decoding of Text_ frames
              and return bytestrings (:class:`bytes`). This may be useful to
              optimize performance when decoding isn't needed.
            * Set ``decode=True`` to force UTF-8 decoding of Binary_ frames
              and return strings (:class:`str`). This is useful for servers
              that send binary frames instead of text frames.

        Raises:
            ConnectionClosed: When the connection is closed.
            ConcurrencyError: If two coroutines call :meth:`recv` or
                :meth:`recv_streaming` concurrently.

        """
        pass
    # WARNING: Decompyle incomplete

    
    async def send(self = None, message = None, text = None):
        """
        Send a message.

        A string (:class:`str`) is sent as a Text_ frame. A bytestring or
        bytes-like object (:class:`bytes`, :class:`bytearray`, or
        :class:`memoryview`) is sent as a Binary_ frame.

        .. _Text: https://datatracker.ietf.org/doc/html/rfc6455#section-5.6
        .. _Binary: https://datatracker.ietf.org/doc/html/rfc6455#section-5.6

        You may override this behavior with the ``text`` argument:

        * Set ``text=True`` to send a bytestring or bytes-like object
          (:class:`bytes`, :class:`bytearray`, or :class:`memoryview`) as a
          Text_ frame. This improves performance when the message is already
          UTF-8 encoded, for example if the message contains JSON and you're
          using a JSON library that produces a bytestring.
        * Set ``text=False`` to send a string (:class:`str`) in a Binary_
          frame. This may be useful for servers that expect binary frames
          instead of text frames.

        :meth:`send` also accepts an iterable or an asynchronous iterable of
        strings, bytestrings, or bytes-like objects to enable fragmentation_.
        Each item is treated as a message fragment and sent in its own frame.
        All items must be of the same type, or else :meth:`send` will raise a
        :exc:`TypeError` and the connection will be closed.

        .. _fragmentation: https://datatracker.ietf.org/doc/html/rfc6455#section-5.4

        :meth:`send` rejects dict-like objects because this is often an error.
        (If you really want to send the keys of a dict-like object as fragments,
        call its :meth:`~dict.keys` method and pass the result to :meth:`send`.)

        Canceling :meth:`send` is discouraged. Instead, you should close the
        connection with :meth:`close`. Indeed, there are only two situations
        where :meth:`send` may yield control to the event loop and then get
        canceled; in both cases, :meth:`close` has the same effect and is
        more clear:

        1. The write buffer is full. If you don't want to wait until enough
           data is sent, your only alternative is to close the connection.
           :meth:`close` will likely time out then abort the TCP connection.
        2. ``message`` is an asynchronous iterator that yields control.
           Stopping in the middle of a fragmented message will cause a
           protocol error and the connection will be closed.

        When the connection is closed, :meth:`send` raises
        :exc:`~websockets.exceptions.ConnectionClosed`. Specifically, it
        raises :exc:`~websockets.exceptions.ConnectionClosedOK` after a normal
        connection closure and
        :exc:`~websockets.exceptions.ConnectionClosedError` after a protocol
        error or a network failure.

        Args:
            message: Message to send.

        Raises:
            ConnectionClosed: When the connection is closed.
            TypeError: If ``message`` doesn't have a supported type.

        """
        pass
    # WARNING: Decompyle incomplete

    
    async def close(self = None, code = None, reason = None):
        """
        Perform the closing handshake.

        :meth:`close` waits for the other end to complete the handshake and
        for the TCP connection to terminate.

        :meth:`close` is idempotent: it doesn't do anything once the
        connection is closed.

        Args:
            code: WebSocket close code.
            reason: WebSocket close reason.

        """
        pass
    # WARNING: Decompyle incomplete

    
    async def wait_closed(self = None):
        '''
        Wait until the connection is closed.

        :meth:`wait_closed` waits for the closing handshake to complete and for
        the TCP connection to terminate.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def ping(self = None, data = None):
        """
        Send a Ping_.

        .. _Ping: https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.2

        A ping may serve as a keepalive or as a check that the remote endpoint
        received all messages up to this point

        Args:
            data: Payload of the ping. A :class:`str` will be encoded to UTF-8.
                If ``data`` is :obj:`None`, the payload is four random bytes.

        Returns:
            A future that will be completed when the corresponding pong is
            received. You can ignore it if you don't intend to wait. The result
            of the future is the latency of the connection in seconds.

            ::

                pong_waiter = await ws.ping()
                # only if you want to wait for the corresponding pong
                latency = await pong_waiter

        Raises:
            ConnectionClosed: When the connection is closed.
            ConcurrencyError: If another ping was sent with the same data and
                the corresponding pong wasn't received yet.

        """
        pass
    # WARNING: Decompyle incomplete

    
    async def pong(self = None, data = None):
        '''
        Send a Pong_.

        .. _Pong: https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.3

        An unsolicited pong may serve as a unidirectional heartbeat.

        Args:
            data: Payload of the pong. A :class:`str` will be encoded to UTF-8.

        Raises:
            ConnectionClosed: When the connection is closed.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def process_event(self = None, event = None):
        '''
        Process one incoming event.

        This method is overridden in subclasses to handle the handshake.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def acknowledge_pings(self = None, data = None):
        '''
        Acknowledge pings when receiving a pong.

        '''
        if data not in self.pong_waiters:
            return None
        pong_timestamp = None.loop.time()
        ping_id = None
        ping_ids = []
        for pong_waiter, ping_timestamp in self.pong_waiters.items():
            ping_ids.append(ping_id)
            latency = pong_timestamp - ping_timestamp
            if not pong_waiter.done():
                pong_waiter.set_result(latency)
            if ping_id == data:
                self.latency = latency
            
            raise AssertionError('solicited pong not found in pings')
            for ping_id in ping_ids:
                del self.pong_waiters[ping_id]
                return None

    
    def abort_pings(self = None):
        """
        Raise ConnectionClosed in pending pings.

        They'll never receive a pong once the connection is closed.

        """
        pass
    # WARNING: Decompyle incomplete

    
    async def keepalive(self = None):
        '''
        Send a Ping frame and wait for a Pong frame at regular intervals.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def start_keepalive(self = None):
        '''
        Run :meth:`keepalive` in a task, unless keepalive is disabled.

        '''
        pass
    # WARNING: Decompyle incomplete

    send_context = (lambda self = None, *, expected_state: pass# WARNING: Decompyle incomplete
)()
    
    def send_data(self = None):
        '''
        Send outgoing data.

        Raises:
            OSError: When a socket operations fails.

        '''
        for data in self.protocol.data_to_send():
            if data:
                self.transport.write(data)
                continue
            if self.transport.can_write_eof():
                if self.debug:
                    self.logger.debug('x half-closing TCP connection')
                self.transport.write_eof()
                continue
                except (OSError, RuntimeError):
                    continue
            if self.debug:
                self.logger.debug('x closing TCP connection')
            self.transport.close()
            return None

    
    def set_recv_exc(self = None, exc = None):
        '''
        Set recv_exc, if not set yet.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def connection_made(self = None, transport = None):
        transport = cast(asyncio.Transport, transport)
    # WARNING: Decompyle incomplete

    
    def connection_lost(self = None, exc = None):
        self.protocol.receive_eof()
    # WARNING: Decompyle incomplete

    
    def pause_writing(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def resume_writing(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def drain(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def data_received(self = None, data = None):
        self.protocol.receive_data(data)
        events = self.protocol.events_received()
        
        try:
            self.send_data()
        except Exception:
            exc = None
            if self.debug:
                self.logger.debug('! error while sending data', exc_info = True)
            self.set_recv_exc(exc)
            exc = None
            del exc
        except:
            exc = None
            del exc

    # WARNING: Decompyle incomplete

    
    def eof_received(self = None):
        self.protocol.receive_eof()
        events = self.protocol.events_received()
        self.send_data()
        for event in events:
            self.process_event(event)
            return None



def broadcast(connections = None, message = None, raise_exceptions = None):
    """
    Broadcast a message to several WebSocket connections.

    A string (:class:`str`) is sent as a Text_ frame. A bytestring or bytes-like
    object (:class:`bytes`, :class:`bytearray`, or :class:`memoryview`) is sent
    as a Binary_ frame.

    .. _Text: https://datatracker.ietf.org/doc/html/rfc6455#section-5.6
    .. _Binary: https://datatracker.ietf.org/doc/html/rfc6455#section-5.6

    :func:`broadcast` pushes the message synchronously to all connections even
    if their write buffers are overflowing. There's no backpressure.

    If you broadcast messages faster than a connection can handle them, messages
    will pile up in its write buffer until the connection times out. Keep
    ``ping_interval`` and ``ping_timeout`` low to prevent excessive memory usage
    from slow connections.

    Unlike :meth:`~websockets.asyncio.connection.Connection.send`,
    :func:`broadcast` doesn't support sending fragmented messages. Indeed,
    fragmentation is useful for sending large messages without buffering them in
    memory, while :func:`broadcast` buffers one copy per connection as fast as
    possible.

    :func:`broadcast` skips connections that aren't open in order to avoid
    errors on connections where the closing handshake is in progress.

    :func:`broadcast` ignores failures to write the message on some connections.
    It continues writing to other connections. On Python 3.11 and above, you may
    set ``raise_exceptions`` to :obj:`True` to record failures and raise all
    exceptions in a :pep:`654` :exc:`ExceptionGroup`.

    While :func:`broadcast` makes more sense for servers, it works identically
    with clients, if you have a use case for opening connections to many servers
    and broadcasting a message to them.

    Args:
        websockets: WebSocket connections to which the message will be sent.
        message: Message to send.
        raise_exceptions: Whether to raise an exception in case of failures.

    Raises:
        TypeError: If ``message`` doesn't have a supported type.

    """
    if isinstance(message, str):
        send_method = 'send_text'
        message = message.encode()
    elif isinstance(message, BytesLike):
        send_method = 'send_binary'
    else:
        raise TypeError('data must be str or bytes')
    if raise_exceptions:
        if sys.version_info[:2] < (3, 11):
            raise ValueError('raise_exceptions requires at least Python 3.11')
        exceptions = []
# WARNING: Decompyle incomplete

broadcast.__module__ = 'websockets.asyncio.server'
