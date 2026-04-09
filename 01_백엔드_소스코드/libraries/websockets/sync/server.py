# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: server.pyc (Python 3.11)

from __future__ import annotations
import hmac
import http
import logging
import os
import re
import selectors
import socket
import ssl as ssl_module
import sys
import threading
import warnings
from collections.abc import Iterable, Sequence
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
from connection import Connection
from utils import Deadline
__all__ = [
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

    This class mirrors the API of :class:`~socketserver.BaseServer`, notably the
    :meth:`~socketserver.BaseServer.serve_forever` and
    :meth:`~socketserver.BaseServer.shutdown` methods, as well as the context
    manager protocol.

    Args:
        socket: Server socket listening for new connections.
        handler: Handler for one connection. Receives the socket and address
            returned by :meth:`~socket.socket.accept`.
        logger: Logger for this server.
            It defaults to ``logging.getLogger("websockets.server")``.
            See the :doc:`logging guide <../../topics/logging>` for details.

    '''
    
    def __init__(self = None, socket = None, handler = None, logger = (None,)):
        self.socket = socket
        self.handler = handler
    # WARNING: Decompyle incomplete

    
    def serve_forever(self = None):
        """
        See :meth:`socketserver.BaseServer.serve_forever`.

        This method doesn't return. Calling :meth:`shutdown` from another thread
        stops the server.

        Typical use::

            with serve(...) as server:
                server.serve_forever()

        """
        poller = selectors.DefaultSelector()
        
        try:
            poller.register(self.socket, selectors.EVENT_READ)
        except ValueError:
            return None

        if sys.platform != 'win32':
            poller.register(self.shutdown_watcher, selectors.EVENT_READ)
        poller.select()
        
        try:
            (sock, addr) = self.socket.accept()
        except OSError:
            return None

        thread = threading.Thread(target = self.handler, args = (sock, addr))
        thread.start()
        continue

    
    def shutdown(self = None):
        '''
        See :meth:`socketserver.BaseServer.shutdown`.

        '''
        self.socket.close()
        if sys.platform != 'win32':
            os.write(self.shutdown_notifier, b'x')
            return None

    
    def fileno(self = None):
        '''
        See :meth:`socketserver.BaseServer.fileno`.

        '''
        return self.socket.fileno()

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
        self.shutdown()



def __getattr__(name = None):
    if name == 'WebSocketServer':
        warnings.warn('WebSocketServer was renamed to Server', DeprecationWarning)
        return Server
    raise None(f'''module {__name__!r} has no attribute {name!r}''')


def serve(handler = None, host = None, port = None, *, sock, ssl, origins, extensions, subprotocols, select_subprotocol, compression, process_request, process_response, server_header, open_timeout, ping_interval, ping_timeout, close_timeout, max_size, max_queue, logger, create_connection, **kwargs):
    '''
    Create a WebSocket server listening on ``host`` and ``port``.

    Whenever a client connects, the server creates a :class:`ServerConnection`,
    performs the opening handshake, and delegates to the ``handler``.

    The handler receives the :class:`ServerConnection` instance, which you can
    use to send and receive messages.

    Once the handler completes, either normally or with an exception, the server
    performs the closing handshake and closes the connection.

    This function returns a :class:`Server` whose API mirrors
    :class:`~socketserver.BaseServer`. Treat it as a context manager to ensure
    that it will be closed and call :meth:`~Server.serve_forever` to serve
    requests::

        from websockets.sync.server import serve

        def handler(websocket):
            ...

        with serve(handler, ...) as server:
            server.serve_forever()

    Args:
        handler: Connection handler. It receives the WebSocket connection,
            which is a :class:`ServerConnection`, in argument.
        host: Network interfaces the server binds to.
            See :func:`~socket.create_server` for details.
        port: TCP port the server listens on.
            See :func:`~socket.create_server` for details.
        sock: Preexisting TCP socket. ``sock`` replaces ``host`` and ``port``.
            You may call :func:`socket.create_server` to create a suitable TCP
            socket.
        ssl: Configuration for enabling TLS on the connection.
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
            Return an HTTP response to force the response. Return :obj:`None` to
            continue normally. When you force an HTTP 101 Continue response, the
            handshake is successful. Else, the connection is aborted.
        process_response: Intercept the response during the opening handshake.
            Modify the response or return a new HTTP response to force the
            response. Return :obj:`None` to continue normally. When you force an
            HTTP 101 Continue response, the handshake is successful. Else, the
            connection is aborted.
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
        logger: Logger for this server.
            It defaults to ``logging.getLogger("websockets.server")``. See the
            :doc:`logging guide <../../topics/logging>` for details.
        create_connection: Factory for the :class:`ServerConnection` managing
            the connection. Set it to a wrapper or a subclass to customize
            connection handling.

    Any other keyword arguments are passed to :func:`~socket.create_server`.

    '''
    pass
# WARNING: Decompyle incomplete


def unix_serve(handler = None, path = None, **kwargs):
    """
    Create a WebSocket server listening on a Unix socket.

    This function accepts the same keyword arguments as :func:`serve`.

    It's only available on Unix.

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

        from websockets.sync.server import basic_auth, serve

        with serve(
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
        check_credentials: Function that verifies credentials.
            It receives ``username`` and ``password`` arguments and returns
            whether they\'re valid.
    Raises:
        TypeError: If ``credentials`` or ``check_credentials`` is wrong.
        ValueError: If ``credentials`` and ``check_credentials`` are both
            provided or both not provided.

    '''
    pass
# WARNING: Decompyle incomplete
