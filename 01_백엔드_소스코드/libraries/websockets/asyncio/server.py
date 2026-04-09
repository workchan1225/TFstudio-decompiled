# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: server.pyc (Python 3.11)

from __future__ import annotations
import asyncio
import hmac
import http
import logging
import re
import socket
import sys
from collections.abc import Awaitable, Generator, Iterable, Sequence
from types import TracebackType
from typing import Any, Callable, Mapping, cast
from exceptions import InvalidHeader
from extensions.base import ServerExtensionFactory
from extensions.permessage_deflate import enable_server_permessage_deflate
from frames import CloseCode
from headers import build_www_authenticate_basic, parse_authorization_basic, validate_subprotocols
from http11 import SERVER, Request, Response
from protocol import CONNECTING, OPEN, Event
from server import ServerProtocol
from typing import LoggerLike, Origin, StatusLike, Subprotocol
from compatibility import asyncio_timeout
from connection import Connection, broadcast
__all__ = [
    'broadcast',
    'serve',
    'unix_serve',
    'ServerConnection',
    'Server',
    'basic_auth']

class ServerConnection(Connection):
    pass
# WARNING: Decompyle incomplete


class Server:
    '''
    WebSocket server returned by :func:`serve`.

    This class mirrors the API of :class:`asyncio.Server`.

    It keeps track of WebSocket connections in order to close them properly
    when shutting down.

    Args:
        handler: Connection handler. It receives the WebSocket connection,
            which is a :class:`ServerConnection`, in argument.
        process_request: Intercept the request during the opening handshake.
            Return an HTTP response to force the response. Return :obj:`None` to
            continue normally. When you force an HTTP 101 Continue response, the
            handshake is successful. Else, the connection is aborted.
            ``process_request`` may be a function or a coroutine.
        process_response: Intercept the response during the opening handshake.
            Modify the response or return a new HTTP response to force the
            response. Return :obj:`None` to continue normally. When you force an
            HTTP 101 Continue response, the handshake is successful. Else, the
            connection is aborted. ``process_response`` may be a function or a
            coroutine.
        server_header: Value of  the ``Server`` response header.
            It defaults to ``"Python/x.y.z websockets/X.Y"``. Setting it to
            :obj:`None` removes the header.
        open_timeout: Timeout for opening connections in seconds.
            :obj:`None` disables the timeout.
        logger: Logger for this server.
            It defaults to ``logging.getLogger("websockets.server")``.
            See the :doc:`logging guide <../../topics/logging>` for details.

    '''
    
    def __init__(self = None, handler = None, *, process_request, process_response, server_header, open_timeout, logger):
        self.loop = asyncio.get_running_loop()
        self.handler = handler
        self.process_request = process_request
        self.process_response = process_response
        self.server_header = server_header
        self.open_timeout = open_timeout
    # WARNING: Decompyle incomplete

    connections = (lambda self = None: self.handlers())()
    
    def wrap(self = None, server = None):
        """
        Attach to a given :class:`asyncio.Server`.

        Since :meth:`~asyncio.loop.create_server` doesn't support injecting a
        custom ``Server`` class, the easiest solution that doesn't rely on
        private :mod:`asyncio` APIs is to:

        - instantiate a :class:`Server`
        - give the protocol factory a reference to that instance
        - call :meth:`~asyncio.loop.create_server` with the factory
        - attach the resulting :class:`asyncio.Server` with this method

        """
        self.server = server
        for sock in server.sockets:
            if sock.family == socket.AF_INET:
                name = '%s:%d' % sock.getsockname()
            elif sock.family == socket.AF_INET6:
                name = '[%s]:%d' % sock.getsockname()[:2]
            elif sock.family == socket.AF_UNIX:
                name = sock.getsockname()
            else:
                name = str(sock.getsockname())
            self.logger.info('server listening on %s', name)
            return None

    
    async def conn_handler(self = None, connection = None):
        """
        Handle the lifecycle of a WebSocket connection.

        Since this method doesn't have a caller that can handle exceptions,
        it attempts to log relevant ones.

        It guarantees that the TCP connection is closed before exiting.

        """
        pass
    # WARNING: Decompyle incomplete

    
    def start_connection_handler(self = None, connection = None):
        '''
        Register a connection with this server.

        '''
        self.handlers[connection] = self.loop.create_task(self.conn_handler(connection))

    
    def close(self = None, close_connections = None):
        """
        Close the server.

        * Close the underlying :class:`asyncio.Server`.
        * When ``close_connections`` is :obj:`True`, which is the default,
          close existing connections. Specifically:

          * Reject opening WebSocket connections with an HTTP 503 (service
            unavailable) error. This happens when the server accepted the TCP
            connection but didn't complete the opening handshake before closing.
          * Close open WebSocket connections with close code 1001 (going away).

        * Wait until all connection handlers terminate.

        :meth:`close` is idempotent.

        """
        pass
    # WARNING: Decompyle incomplete

    
    async def _close(self = None, close_connections = None):
        '''
        Implementation of :meth:`close`.

        This calls :meth:`~asyncio.Server.close` on the underlying
        :class:`asyncio.Server` object to stop accepting new connections and
        then closes open connections with close code 1001.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def wait_closed(self = None):
        '''
        Wait until the server is closed.

        When :meth:`wait_closed` returns, all TCP connections are closed and
        all connection handlers have returned.

        To ensure a fast shutdown, a connection handler should always be
        awaiting at least one of:

        * :meth:`~ServerConnection.recv`: when the connection is closed,
          it raises :exc:`~websockets.exceptions.ConnectionClosedOK`;
        * :meth:`~ServerConnection.wait_closed`: when the connection is
          closed, it returns.

        Then the connection handler is immediately notified of the shutdown;
        it can clean up and exit.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_loop(self = None):
        '''
        See :meth:`asyncio.Server.get_loop`.

        '''
        return self.server.get_loop()

    
    def is_serving(self = None):
        '''
        See :meth:`asyncio.Server.is_serving`.

        '''
        return self.server.is_serving()

    
    async def start_serving(self = None):
        '''
        See :meth:`asyncio.Server.start_serving`.

        Typical use::

            server = await serve(..., start_serving=False)
            # perform additional setup here...
            # ... then start the server
            await server.start_serving()

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def serve_forever(self = None):
        """
        See :meth:`asyncio.Server.serve_forever`.

        Typical use::

            server = await serve(...)
            # this coroutine doesn't return
            # canceling it stops the server
            await server.serve_forever()

        This is an alternative to using :func:`serve` as an asynchronous context
        manager. Shutdown is triggered by canceling :meth:`serve_forever`
        instead of exiting a :func:`serve` context.

        """
        pass
    # WARNING: Decompyle incomplete

    sockets = (lambda self = None: self.server.sockets)()
    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete



class serve:
    '''
    Create a WebSocket server listening on ``host`` and ``port``.

    Whenever a client connects, the server creates a :class:`ServerConnection`,
    performs the opening handshake, and delegates to the ``handler`` coroutine.

    The handler receives the :class:`ServerConnection` instance, which you can
    use to send and receive messages.

    Once the handler completes, either normally or with an exception, the server
    performs the closing handshake and closes the connection.

    This coroutine returns a :class:`Server` whose API mirrors
    :class:`asyncio.Server`. Treat it as an asynchronous context manager to
    ensure that the server will be closed::

        from websockets.asyncio.server import serve

        def handler(websocket):
            ...

        # set this future to exit the server
        stop = asyncio.get_running_loop().create_future()

        async with serve(handler, host, port):
            await stop

    Alternatively, call :meth:`~Server.serve_forever` to serve requests and
    cancel it to stop the server::

        server = await serve(handler, host, port)
        await server.serve_forever()

    Args:
        handler: Connection handler. It receives the WebSocket connection,
            which is a :class:`ServerConnection`, in argument.
        host: Network interfaces the server binds to.
            See :meth:`~asyncio.loop.create_server` for details.
        port: TCP port the server listens on.
            See :meth:`~asyncio.loop.create_server` for details.
        origins: Acceptable values of the ``Origin`` header, for defending
            against Cross-Site WebSocket Hijacking attacks. Values can be
            :class:`str` to test for an exact match or regular expressions
            compiled by :func:`re.compile` to test against a pattern. Include
            :obj:`None` in the list if the lack of an origin is acceptable.
        extensions: List of supported extensions, in order in which they
            should be negotiated and run.
        subprotocols: List of supported subprotocols, in order of decreasing
            preference.
        select_subprotocol: Callback for selecting a subprotocol among
            those supported by the client and the server. It receives a
            :class:`ServerConnection` (not a
            :class:`~websockets.server.ServerProtocol`!) instance and a list of
            subprotocols offered by the client. Other than the first argument,
            it has the same behavior as the
            :meth:`ServerProtocol.select_subprotocol
            <websockets.server.ServerProtocol.select_subprotocol>` method.
        compression: The "permessage-deflate" extension is enabled by default.
            Set ``compression`` to :obj:`None` to disable it. See the
            :doc:`compression guide <../../topics/compression>` for details.
        process_request: Intercept the request during the opening handshake.
            Return an HTTP response to force the response or :obj:`None` to
            continue normally. When you force an HTTP 101 Continue response, the
            handshake is successful. Else, the connection is aborted.
            ``process_request`` may be a function or a coroutine.
        process_response: Intercept the response during the opening handshake.
            Return an HTTP response to force the response or :obj:`None` to
            continue normally. When you force an HTTP 101 Continue response, the
            handshake is successful. Else, the connection is aborted.
            ``process_response`` may be a function or a coroutine.
        server_header: Value of  the ``Server`` response header.
            It defaults to ``"Python/x.y.z websockets/X.Y"``. Setting it to
            :obj:`None` removes the header.
        open_timeout: Timeout for opening connections in seconds.
            :obj:`None` disables the timeout.
        ping_interval: Interval between keepalive pings in seconds.
            :obj:`None` disables keepalive.
        ping_timeout: Timeout for keepalive pings in seconds.
            :obj:`None` disables timeouts.
        close_timeout: Timeout for closing connections in seconds.
            :obj:`None` disables the timeout.
        max_size: Maximum size of incoming messages in bytes.
            :obj:`None` disables the limit.
        max_queue: High-water mark of the buffer where frames are received.
            It defaults to 16 frames. The low-water mark defaults to ``max_queue
            // 4``. You may pass a ``(high, low)`` tuple to set the high-water
            and low-water marks. If you want to disable flow control entirely,
            you may set it to ``None``, although that\'s a bad idea.
        write_limit: High-water mark of write buffer in bytes. It is passed to
            :meth:`~asyncio.WriteTransport.set_write_buffer_limits`. It defaults
            to 32 KiB. You may pass a ``(high, low)`` tuple to set the
            high-water and low-water marks.
        logger: Logger for this server.
            It defaults to ``logging.getLogger("websockets.server")``. See the
            :doc:`logging guide <../../topics/logging>` for details.
        create_connection: Factory for the :class:`ServerConnection` managing
            the connection. Set it to a wrapper or a subclass to customize
            connection handling.

    Any other keyword arguments are passed to the event loop\'s
    :meth:`~asyncio.loop.create_server` method.

    For example:

    * You can set ``ssl`` to a :class:`~ssl.SSLContext` to enable TLS.

    * You can set ``sock`` to provide a preexisting TCP socket. You may call
      :func:`socket.create_server` (not to be confused with the event loop\'s
      :meth:`~asyncio.loop.create_server` method) to create a suitable server
      socket and customize it.

    * You can set ``start_serving`` to ``False`` to start accepting connections
      only after you call :meth:`~Server.start_serving()` or
      :meth:`~Server.serve_forever()`.

    '''
    
    def __init__(self = None, handler = None, host = None, port = None, *, origins, extensions, subprotocols, select_subprotocol, compression, process_request, process_response, server_header, open_timeout, ping_interval, ping_timeout, close_timeout, max_size, max_queue, write_limit, logger, create_connection, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def __await__(self = None):
        return self.__await_impl__().__await__()

    
    async def __await_impl__(self = None):
        pass
    # WARNING: Decompyle incomplete

    __iter__ = __await__


def unix_serve(handler = None, path = None, **kwargs):
    """
    Create a WebSocket server listening on a Unix socket.

    This function is identical to :func:`serve`, except the ``host`` and
    ``port`` arguments are replaced by ``path``. It's only available on Unix.

    It's useful for deploying a server behind a reverse proxy such as nginx.

    Args:
        handler: Connection handler. It receives the WebSocket connection,
            which is a :class:`ServerConnection`, in argument.
        path: File system path to the Unix socket.

    """
    pass
# WARNING: Decompyle incomplete


def is_credentials(credentials = None):
    
    try:
        (username, password) = credentials
        if isinstance(username, str):
            return isinstance(password, str)
        except (TypeError, ValueError):
            return False



def basic_auth(realm = None, credentials = None, check_credentials = None):
    '''
    Factory for ``process_request`` to enforce HTTP Basic Authentication.

    :func:`basic_auth` is designed to integrate with :func:`serve` as follows::

        from websockets.asyncio.server import basic_auth, serve

        async with serve(
            ...,
            process_request=basic_auth(
                realm="my dev server",
                credentials=("hello", "iloveyou"),
            ),
        ):

    If authentication succeeds, the connection\'s ``username`` attribute is set.
    If it fails, the server responds with an HTTP 401 Unauthorized status.

    One of ``credentials`` or ``check_credentials`` must be provided; not both.

    Args:
        realm: Scope of protection. It should contain only ASCII characters
            because the encoding of non-ASCII characters is undefined. Refer to
            section 2.2 of :rfc:`7235` for details.
        credentials: Hard coded authorized credentials. It can be a
            ``(username, password)`` pair or a list of such pairs.
        check_credentials: Function or coroutine that verifies credentials.
            It receives ``username`` and ``password`` arguments and returns
            whether they\'re valid.
    Raises:
        TypeError: If ``credentials`` or ``check_credentials`` is wrong.
        ValueError: If ``credentials`` and ``check_credentials`` are both
            provided or both not provided.

    '''
    pass
# WARNING: Decompyle incomplete
