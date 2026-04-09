# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: protocol.pyc (Python 3.11)

from __future__ import annotations
import asyncio
import codecs
import collections
import logging
import random
import ssl
import struct
import sys
import time
import traceback
import uuid
import warnings
from collections.abc import AsyncIterable, AsyncIterator, Awaitable, Iterable, Mapping
from typing import Any, Callable, Deque, cast
from asyncio.compatibility import asyncio_timeout
from datastructures import Headers
from exceptions import ConnectionClosed, ConnectionClosedError, ConnectionClosedOK, InvalidState, PayloadTooBig, ProtocolError
from extensions import Extension
from frames import OK_CLOSE_CODES, OP_BINARY, OP_CLOSE, OP_CONT, OP_PING, OP_PONG, OP_TEXT, Close, CloseCode, Opcode
from protocol import State
from typing import Data, LoggerLike, Subprotocol
from framing import Frame, prepare_ctrl, prepare_data
__all__ = [
    'WebSocketCommonProtocol']

class WebSocketCommonProtocol(asyncio.Protocol):
    is_client: 'bool' = '\n    WebSocket connection.\n\n    :class:`WebSocketCommonProtocol` provides APIs shared between WebSocket\n    servers and clients. You shouldn\'t use it directly. Instead, use\n    :class:`~websockets.legacy.client.WebSocketClientProtocol` or\n    :class:`~websockets.legacy.server.WebSocketServerProtocol`.\n\n    This documentation focuses on low-level details that aren\'t covered in the\n    documentation of :class:`~websockets.legacy.client.WebSocketClientProtocol`\n    and :class:`~websockets.legacy.server.WebSocketServerProtocol` for the sake\n    of simplicity.\n\n    Once the connection is open, a Ping_ frame is sent every ``ping_interval``\n    seconds. This serves as a keepalive. It helps keeping the connection open,\n    especially in the presence of proxies with short timeouts on inactive\n    connections. Set ``ping_interval`` to :obj:`None` to disable this behavior.\n\n    .. _Ping: https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.2\n\n    If the corresponding Pong_ frame isn\'t received within ``ping_timeout``\n    seconds, the connection is considered unusable and is closed with code 1011.\n    This ensures that the remote endpoint remains responsive. Set\n    ``ping_timeout`` to :obj:`None` to disable this behavior.\n\n    .. _Pong: https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.3\n\n    See the discussion of :doc:`keepalive <../../topics/keepalive>` for details.\n\n    The ``close_timeout`` parameter defines a maximum wait time for completing\n    the closing handshake and terminating the TCP connection. For legacy\n    reasons, :meth:`close` completes in at most ``5 * close_timeout`` seconds\n    for clients and ``4 * close_timeout`` for servers.\n\n    ``close_timeout`` is a parameter of the protocol because websockets usually\n    calls :meth:`close` implicitly upon exit:\n\n    * on the client side, when using :func:`~websockets.legacy.client.connect`\n      as a context manager;\n    * on the server side, when the connection handler terminates.\n\n    To apply a timeout to any other API, wrap it in :func:`~asyncio.timeout` or\n    :func:`~asyncio.wait_for`.\n\n    The ``max_size`` parameter enforces the maximum size for incoming messages\n    in bytes. The default value is 1 MiB. If a larger message is received,\n    :meth:`recv` will raise :exc:`~websockets.exceptions.ConnectionClosedError`\n    and the connection will be closed with code 1009.\n\n    The ``max_queue`` parameter sets the maximum length of the queue that\n    holds incoming messages. The default value is ``32``. Messages are added\n    to an in-memory queue when they\'re received; then :meth:`recv` pops from\n    that queue. In order to prevent excessive memory consumption when\n    messages are received faster than they can be processed, the queue must\n    be bounded. If the queue fills up, the protocol stops processing incoming\n    data until :meth:`recv` is called. In this situation, various receive\n    buffers (at least in :mod:`asyncio` and in the OS) will fill up, then the\n    TCP receive window will shrink, slowing down transmission to avoid packet\n    loss.\n\n    Since Python can use up to 4 bytes of memory to represent a single\n    character, each connection may use up to ``4 * max_size * max_queue``\n    bytes of memory to store incoming messages. By default, this is 128 MiB.\n    You may want to lower the limits, depending on your application\'s\n    requirements.\n\n    The ``read_limit`` argument sets the high-water limit of the buffer for\n    incoming bytes. The low-water limit is half the high-water limit. The\n    default value is 64 KiB, half of asyncio\'s default (based on the current\n    implementation of :class:`~asyncio.StreamReader`).\n\n    The ``write_limit`` argument sets the high-water limit of the buffer for\n    outgoing bytes. The low-water limit is a quarter of the high-water limit.\n    The default value is 64 KiB, equal to asyncio\'s default (based on the\n    current implementation of ``FlowControlMixin``).\n\n    See the discussion of :doc:`memory usage <../../topics/memory>` for details.\n\n    Args:\n        logger: Logger for this server.\n            It defaults to ``logging.getLogger("websockets.protocol")``.\n            See the :doc:`logging guide <../../topics/logging>` for details.\n        ping_interval: Interval between keepalive pings in seconds.\n            :obj:`None` disables keepalive.\n        ping_timeout: Timeout for keepalive pings in seconds.\n            :obj:`None` disables timeouts.\n        close_timeout: Timeout for closing the connection in seconds.\n            For legacy reasons, the actual timeout is 4 or 5 times larger.\n        max_size: Maximum size of incoming messages in bytes.\n            :obj:`None` disables the limit.\n        max_queue: Maximum number of incoming messages in receive buffer.\n            :obj:`None` disables the limit.\n        read_limit: High-water mark of read buffer in bytes.\n        write_limit: High-water mark of write buffer in bytes.\n\n    '
    side: 'str' = 'undefined'
    
    def __init__(self = None, *, logger, ping_interval, ping_timeout, close_timeout, max_size, max_queue, read_limit, write_limit, host, port, secure, legacy_recv, loop, timeout):
        if legacy_recv:
            warnings.warn('legacy_recv is deprecated', DeprecationWarning)
    # WARNING: Decompyle incomplete

    
    async def _drain_helper(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _drain(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def connection_open(self = None):
        '''
        Callback when the WebSocket opening handshake completes.

        Enter the OPEN state and start the data transfer phase.

        '''
        pass
    # WARNING: Decompyle incomplete

    host = (lambda self = None: alternative = 'remote_address' if self.is_client else 'local_address'warnings.warn(f'''use {alternative}[0] instead of host''', DeprecationWarning)self._host)()
    port = (lambda self = None: alternative = 'remote_address' if self.is_client else 'local_address'warnings.warn(f'''use {alternative}[1] instead of port''', DeprecationWarning)self._port)()
    secure = (lambda self = None: warnings.warn("don't use secure", DeprecationWarning)self._secure)()
    local_address = (lambda self = None: try:
transport = self.transporttransport.get_extra_info('sockname')except AttributeError:
None)()
    remote_address = (lambda self = None: try:
transport = self.transporttransport.get_extra_info('peername')except AttributeError:
None)()
    open = (lambda self = None: if self.state is State.OPEN:
passnot self.transfer_data_task.done())()
    closed = (lambda self = None: self.state is State.CLOSED)()
    close_code = (lambda self = None: if self.state is not State.CLOSED:
None# WARNING: Decompyle incomplete
)()
    close_reason = (lambda self = None: if self.state is not State.CLOSED:
None# WARNING: Decompyle incomplete
)()
    
    def __aiter__(self = None):
        '''
        Iterate on incoming messages.

        The iterator exits normally when the connection is closed with the close
        code 1000 (OK) or 1001 (going away) or without a close code.

        It raises a :exc:`~websockets.exceptions.ConnectionClosedError`
        exception when the connection is closed with any other code.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def recv(self = None):
        """
        Receive the next message.

        When the connection is closed, :meth:`recv` raises
        :exc:`~websockets.exceptions.ConnectionClosed`. Specifically, it raises
        :exc:`~websockets.exceptions.ConnectionClosedOK` after a normal
        connection closure and
        :exc:`~websockets.exceptions.ConnectionClosedError` after a protocol
        error or a network failure. This is how you detect the end of the
        message stream.

        Canceling :meth:`recv` is safe. There's no risk of losing the next
        message. The next invocation of :meth:`recv` will return it.

        This makes it possible to enforce a timeout by wrapping :meth:`recv` in
        :func:`~asyncio.timeout` or :func:`~asyncio.wait_for`.

        Returns:
            A string (:class:`str`) for a Text_ frame. A bytestring
            (:class:`bytes`) for a Binary_ frame.

            .. _Text: https://datatracker.ietf.org/doc/html/rfc6455#section-5.6
            .. _Binary: https://datatracker.ietf.org/doc/html/rfc6455#section-5.6

        Raises:
            ConnectionClosed: When the connection is closed.
            RuntimeError: If two coroutines call :meth:`recv` concurrently.

        """
        pass
    # WARNING: Decompyle incomplete

    
    async def send(self = None, message = None):
        """
        Send a message.

        A string (:class:`str`) is sent as a Text_ frame. A bytestring or
        bytes-like object (:class:`bytes`, :class:`bytearray`, or
        :class:`memoryview`) is sent as a Binary_ frame.

        .. _Text: https://datatracker.ietf.org/doc/html/rfc6455#section-5.6
        .. _Binary: https://datatracker.ietf.org/doc/html/rfc6455#section-5.6

        :meth:`send` also accepts an iterable or an asynchronous iterable of
        strings, bytestrings, or bytes-like objects to enable fragmentation_.
        Each item is treated as a message fragment and sent in its own frame.
        All items must be of the same type, or else :meth:`send` will raise a
        :exc:`TypeError` and the connection will be closed.

        .. _fragmentation: https://datatracker.ietf.org/doc/html/rfc6455#section-5.4

        :meth:`send` rejects dict-like objects because this is often an error.
        (If you want to send the keys of a dict-like object as fragments, call
        its :meth:`~dict.keys` method and pass the result to :meth:`send`.)

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
        for the TCP connection to terminate. As a consequence, there's no need
        to await :meth:`wait_closed` after :meth:`close`.

        :meth:`close` is idempotent: it doesn't do anything once the
        connection is closed.

        Wrapping :func:`close` in :func:`~asyncio.create_task` is safe, given
        that errors during connection termination aren't particularly useful.

        Canceling :meth:`close` is discouraged. If it takes too long, you can
        set a shorter ``close_timeout``. If you don't want to wait, let the
        Python process exit, then the OS will take care of closing the TCP
        connection.

        Args:
            code: WebSocket close code.
            reason: WebSocket close reason.

        """
        pass
    # WARNING: Decompyle incomplete

    
    async def wait_closed(self = None):
        '''
        Wait until the connection is closed.

        This coroutine is identical to the :attr:`closed` attribute, except it
        can be awaited.

        This can make it easier to detect connection termination, regardless
        of its cause, in tasks that interact with the WebSocket connection.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def ping(self = None, data = None):
        """
        Send a Ping_.

        .. _Ping: https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.2

        A ping may serve as a keepalive, as a check that the remote endpoint
        received all messages up to this point, or to measure :attr:`latency`.

        Canceling :meth:`ping` is discouraged. If :meth:`ping` doesn't return
        immediately, it means the write buffer is full. If you don't want to
        wait, you should close the connection.

        Canceling the :class:`~asyncio.Future` returned by :meth:`ping` has no
        effect.

        Args:
            data: Payload of the ping. A string will be encoded to UTF-8.
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
            RuntimeError: If another ping was sent with the same data and
                the corresponding pong wasn't received yet.

        """
        pass
    # WARNING: Decompyle incomplete

    
    async def pong(self = None, data = None):
        """
        Send a Pong_.

        .. _Pong: https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.3

        An unsolicited pong may serve as a unidirectional heartbeat.

        Canceling :meth:`pong` is discouraged. If :meth:`pong` doesn't return
        immediately, it means the write buffer is full. If you don't want to
        wait, you should close the connection.

        Args:
            data: Payload of the pong. A string will be encoded to UTF-8.

        Raises:
            ConnectionClosed: When the connection is closed.

        """
        pass
    # WARNING: Decompyle incomplete

    
    def connection_closed_exc(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def ensure_open(self = None):
        """
        Check that the WebSocket connection is open.

        Raise :exc:`~websockets.exceptions.ConnectionClosed` if it isn't.

        """
        pass
    # WARNING: Decompyle incomplete

    
    async def transfer_data(self = None):
        '''
        Read incoming messages and put them in a queue.

        This coroutine runs in a task until the closing handshake is started.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def read_message(self = None):
        '''
        Read a single message from the connection.

        Re-assemble data frames if the message is fragmented.

        Return :obj:`None` when the closing handshake is started.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def read_data_frame(self = None, max_size = None):
        '''
        Read a single data frame from the connection.

        Process control frames received before the next data frame.

        Return :obj:`None` if a close frame is encountered before any data frame.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def read_frame(self = None, max_size = None):
        '''
        Read a single frame from the connection.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def write_frame_sync(self = None, fin = None, opcode = None, data = ('fin', 'bool', 'opcode', 'int', 'data', 'bytes', 'return', 'None')):
        frame = Frame(fin, Opcode(opcode), data)
        if self.debug:
            self.logger.debug('> %s', frame)
        frame.write(self.transport.write, mask = self.is_client, extensions = self.extensions)

    
    async def drain(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def write_frame(self = None, fin = None, opcode = None, data = None, *, _state):
        pass
    # WARNING: Decompyle incomplete

    
    async def write_close_frame(self = None, close = None, data = None):
        '''
        Write a close frame if and only if the connection state is OPEN.

        This dedicated coroutine must be used for writing close frames to
        ensure that at most one close frame is sent on a given connection.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def keepalive_ping(self = None):
        '''
        Send a Ping frame and wait for a Pong frame at regular intervals.

        This coroutine exits when the connection terminates and one of the
        following happens:

        - :meth:`ping` raises :exc:`ConnectionClosed`, or
        - :meth:`close_connection` cancels :attr:`keepalive_ping_task`.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def close_connection(self = None):
        """
        7.1.1. Close the WebSocket Connection

        When the opening handshake succeeds, :meth:`connection_open` starts
        this coroutine in a task. It waits for the data transfer phase to
        complete then it closes the TCP connection cleanly.

        When the opening handshake fails, :meth:`fail_connection` does the
        same. There's no data transfer phase in that case.

        """
        pass
    # WARNING: Decompyle incomplete

    
    async def close_transport(self = None):
        '''
        Close the TCP connection.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def wait_for_connection_lost(self = None):
        '''
        Wait until the TCP connection is closed or ``self.close_timeout`` elapses.

        Return :obj:`True` if the connection is closed and :obj:`False`
        otherwise.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def fail_connection(self = None, code = None, reason = None):
        '''
        7.1.7. Fail the WebSocket Connection

        This requires:

        1. Stopping all processing of incoming data, which means cancelling
           :attr:`transfer_data_task`. The close code will be 1006 unless a
           close frame was received earlier.

        2. Sending a close frame with an appropriate code if the opening
           handshake succeeded and the other side is likely to process it.

        3. Closing the connection. :meth:`close_connection` takes care of
           this once :attr:`transfer_data_task` exits after being canceled.

        (The specification describes these steps in the opposite order.)

        '''
        if self.debug:
            self.logger.debug('! failing connection with code %d', code)
        if hasattr(self, 'transfer_data_task'):
            self.transfer_data_task.cancel()
    # WARNING: Decompyle incomplete

    
    def abort_pings(self = None):
        """
        Raise ConnectionClosed in pending keepalive pings.

        They'll never receive a pong once the connection is closed.

        """
        pass
    # WARNING: Decompyle incomplete

    
    def connection_made(self = None, transport = None):
        """
        Configure write buffer limits.

        The high-water limit is defined by ``self.write_limit``.

        The low-water limit currently defaults to ``self.write_limit // 4`` in
        :meth:`~asyncio.WriteTransport.set_write_buffer_limits`, which should
        be all right for reasonable use cases of this library.

        This is the earliest point where we can get hold of the transport,
        which means it's the best point for configuring it.

        """
        transport = cast(asyncio.Transport, transport)
        transport.set_write_buffer_limits(self.write_limit)
        self.transport = transport
        self.reader.set_transport(transport)

    
    def connection_lost(self = None, exc = None):
        '''
        7.1.4. The WebSocket Connection is Closed.

        '''
        self.state = State.CLOSED
        self.logger.debug('= connection is CLOSED')
        self.abort_pings()
        self.connection_lost_waiter.set_result(None)
    # WARNING: Decompyle incomplete

    
    def pause_writing(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def resume_writing(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def data_received(self = None, data = None):
        self.reader.feed_data(data)

    
    def eof_received(self = None):
        """
        Close the transport after receiving EOF.

        The WebSocket protocol has its own closing handshake: endpoints close
        the TCP or TLS connection after sending and receiving a close frame.

        As a consequence, they never need to write after receiving EOF, so
        there's no reason to keep the transport open by returning :obj:`True`.

        Besides, that doesn't work on TLS connections.

        """
        self.reader.feed_eof()



def broadcast(websockets = None, message = None, raise_exceptions = None):
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

    Unlike :meth:`~websockets.legacy.protocol.WebSocketCommonProtocol.send`,
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
    if not isinstance(message, (str, bytes, bytearray, memoryview)):
        raise TypeError('data must be str or bytes-like')
    if raise_exceptions:
        if sys.version_info[:2] < (3, 11):
            raise ValueError('raise_exceptions requires at least Python 3.11')
        exceptions = []
    (opcode, data) = prepare_data(message)
# WARNING: Decompyle incomplete

broadcast.__module__ = 'websockets.legacy.server'
