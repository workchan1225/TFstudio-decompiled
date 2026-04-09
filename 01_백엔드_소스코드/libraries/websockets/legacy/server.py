# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: server.pyc (Python 3.11)

from __future__ import annotations
import asyncio
import email.utils as email
import functools
import http
import inspect
import logging
import socket
import warnings
from collections.abc import Awaitable, Generator, Iterable, Sequence
from types import TracebackType
from typing import Any, Callable, Union, cast
from asyncio.compatibility import asyncio_timeout
from datastructures import Headers, HeadersLike, MultipleValuesError
from exceptions import InvalidHandshake, InvalidHeader, InvalidMessage, InvalidOrigin, InvalidUpgrade, NegotiationError
from extensions import Extension, ServerExtensionFactory
from extensions.permessage_deflate import enable_server_permessage_deflate
from headers import build_extension, parse_extension, parse_subprotocol, validate_subprotocols
from http11 import SERVER
from protocol import State
from typing import ExtensionHeader, LoggerLike, Origin, StatusLike, Subprotocol
from exceptions import AbortHandshake
from handshake import build_response, check_request
from http import read_request
from protocol import WebSocketCommonProtocol, broadcast
__all__ = [
    'broadcast',
    'serve',
    'unix_serve',
    'WebSocketServerProtocol',
    'WebSocketServer']
HeadersLikeOrCallable = Union[(HeadersLike, Callable[([
    str,
    Headers], HeadersLike)])]
HTTPResponse = tuple[(StatusLike, HeadersLike, bytes)]

class WebSocketServerProtocol(WebSocketCommonProtocol):
    pass
# WARNING: Decompyle incomplete


class WebSocketServer:
    '''
    WebSocket server returned by :func:`serve`.

    This class mirrors the API of :class:`~asyncio.Server`.

    It keeps track of WebSocket connections in order to close them properly
    when shutting down.

    Args:
        logger: Logger for this server.
            It defaults to ``logging.getLogger("websockets.server")``.
            See the :doc:`logging guide <../../topics/logging>` for details.

    '''
    
    def __init__(self = None, logger = None):
        pass
    # WARNING: Decompyle incomplete

    
    def wrap(self = None, server = None):
        """
        Attach to a given :class:`~asyncio.Server`.

        Since :meth:`~asyncio.loop.create_server` doesn't support injecting a
        custom ``Server`` class, the easiest solution that doesn't rely on
        private :mod:`asyncio` APIs is to:

        - instantiate a :class:`WebSocketServer`
        - give the protocol factory a reference to that instance
        - call :meth:`~asyncio.loop.create_server` with the factory
        - attach the resulting :class:`~asyncio.Server` with this method

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
            self.closed_waiter = server.get_loop().create_future()
            return None

    
    def register(self = None, protocol = None):
        '''
        Register a connection with this server.

        '''
        self.websockets.add(protocol)

    
    def unregister(self = None, protocol = None):
        '''
        Unregister a connection with this server.

        '''
        self.websockets.remove(protocol)

    
    def close(self = None, close_connections = None):
        """
        Close the server.

        * Close the underlying :class:`~asyncio.Server`.
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
        :class:`~asyncio.Server` object to stop accepting new connections and
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

        * :meth:`~WebSocketServerProtocol.recv`: when the connection is closed,
          it raises :exc:`~websockets.exceptions.ConnectionClosedOK`;
        * :meth:`~WebSocketServerProtocol.wait_closed`: when the connection is
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



class Serve:
    '''
    Start a WebSocket server listening on ``host`` and ``port``.

    Whenever a client connects, the server creates a
    :class:`WebSocketServerProtocol`, performs the opening handshake, and
    delegates to the connection handler, ``ws_handler``.

    The handler receives the :class:`WebSocketServerProtocol` and uses it to
    send and receive messages.

    Once the handler completes, either normally or with an exception, the
    server performs the closing handshake and closes the connection.

    Awaiting :func:`serve` yields a :class:`WebSocketServer`. This object
    provides a :meth:`~WebSocketServer.close` method to shut down the server::

        # set this future to exit the server
        stop = asyncio.get_running_loop().create_future()

        server = await serve(...)
        await stop
        server.close()
        await server.wait_closed()

    :func:`serve` can be used as an asynchronous context manager. Then, the
    server is shut down automatically when exiting the context::

        # set this future to exit the server
        stop = asyncio.get_running_loop().create_future()

        async with serve(...):
            await stop

    Args:
        ws_handler: Connection handler. It receives the WebSocket connection,
            which is a :class:`WebSocketServerProtocol`, in argument.
        host: Network interfaces the server binds to.
            See :meth:`~asyncio.loop.create_server` for details.
        port: TCP port the server listens on.
            See :meth:`~asyncio.loop.create_server` for details.
        create_protocol: Factory for the :class:`asyncio.Protocol` managing
            the connection. It defaults to :class:`WebSocketServerProtocol`.
            Set it to a wrapper or a subclass to customize connection handling.
        logger: Logger for this server.
            It defaults to ``logging.getLogger("websockets.server")``.
            See the :doc:`logging guide <../../topics/logging>` for details.
        compression: The "permessage-deflate" extension is enabled by default.
            Set ``compression`` to :obj:`None` to disable it. See the
            :doc:`compression guide <../../topics/compression>` for details.
        origins: Acceptable values of the ``Origin`` header, for defending
            against Cross-Site WebSocket Hijacking attacks. Include :obj:`None`
            in the list if the lack of an origin is acceptable.
        extensions: List of supported extensions, in order in which they
            should be negotiated and run.
        subprotocols: List of supported subprotocols, in order of decreasing
            preference.
        extra_headers (HeadersLike | Callable[[str, Headers] | HeadersLike]):
            Arbitrary HTTP headers to add to the response. This can be
            a :data:`~websockets.datastructures.HeadersLike` or a callable
            taking the request path and headers in arguments and returning
            a :data:`~websockets.datastructures.HeadersLike`.
        server_header: Value of  the ``Server`` response header.
            It defaults to ``"Python/x.y.z websockets/X.Y"``.
            Setting it to :obj:`None` removes the header.
        process_request (Callable[[str, Headers],             Awaitable[tuple[StatusLike, HeadersLike, bytes] | None]] | None):
            Intercept HTTP request before the opening handshake.
            See :meth:`~WebSocketServerProtocol.process_request` for details.
        select_subprotocol: Select a subprotocol supported by the client.
            See :meth:`~WebSocketServerProtocol.select_subprotocol` for details.
        open_timeout: Timeout for opening connections in seconds.
            :obj:`None` disables the timeout.

    See :class:`~websockets.legacy.protocol.WebSocketCommonProtocol` for the
    documentation of ``ping_interval``, ``ping_timeout``, ``close_timeout``,
    ``max_size``, ``max_queue``, ``read_limit``, and ``write_limit``.

    Any other keyword arguments are passed the event loop\'s
    :meth:`~asyncio.loop.create_server` method.

    For example:

    * You can set ``ssl`` to a :class:`~ssl.SSLContext` to enable TLS.

    * You can set ``sock`` to a :obj:`~socket.socket` that you created
      outside of websockets.

    Returns:
        WebSocket server.

    '''
    
    def __init__(self = None, ws_handler = None, host = None, port = None, *, create_protocol, logger, compression, origins, extensions, subprotocols, extra_headers, server_header, process_request, select_subprotocol, open_timeout, ping_interval, ping_timeout, close_timeout, max_size, max_queue, read_limit, write_limit, **kwargs):
        timeout = kwargs.pop('timeout', None)
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

serve = Serve

def unix_serve(ws_handler = None, path = None, **kwargs):
    """
    Start a WebSocket server listening on a Unix socket.

    This function is identical to :func:`serve`, except the ``host`` and
    ``port`` arguments are replaced by ``path``. It is only available on Unix.

    Unrecognized keyword arguments are passed the event loop's
    :meth:`~asyncio.loop.create_unix_server` method.

    It's useful for deploying a server behind a reverse proxy such as nginx.

    Args:
        path: File system path to the Unix socket.

    """
    pass
# WARNING: Decompyle incomplete


def remove_path_argument(ws_handler = None):
    pass
# WARNING: Decompyle incomplete
