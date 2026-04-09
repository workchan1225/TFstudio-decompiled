# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client.pyc (Python 3.11)

from __future__ import annotations
import asyncio
import functools
import logging
import os
import random
import traceback
import urllib.parse as urllib
import warnings
from collections.abc import AsyncIterator, Generator, Sequence
from types import TracebackType
from typing import Any, Callable, cast
from asyncio.compatibility import asyncio_timeout
from datastructures import Headers, HeadersLike
from exceptions import InvalidHeader, InvalidHeaderValue, InvalidMessage, NegotiationError, SecurityError
from extensions import ClientExtensionFactory, Extension
from extensions.permessage_deflate import enable_client_permessage_deflate
from headers import build_authorization_basic, build_extension, build_host, build_subprotocol, parse_extension, parse_subprotocol, validate_subprotocols
from http11 import USER_AGENT
from typing import ExtensionHeader, LoggerLike, Origin, Subprotocol
from uri import WebSocketURI, parse_uri
from exceptions import InvalidStatusCode, RedirectHandshake
from handshake import build_request, check_response
from http import read_response
from protocol import WebSocketCommonProtocol
__all__ = [
    'connect',
    'unix_connect',
    'WebSocketClientProtocol']

class WebSocketClientProtocol(WebSocketCommonProtocol):
    pass
# WARNING: Decompyle incomplete


class Connect:
    '''
    Connect to the WebSocket server at ``uri``.

    Awaiting :func:`connect` yields a :class:`WebSocketClientProtocol` which
    can then be used to send and receive messages.

    :func:`connect` can be used as a asynchronous context manager::

        async with connect(...) as websocket:
            ...

    The connection is closed automatically when exiting the context.

    :func:`connect` can be used as an infinite asynchronous iterator to
    reconnect automatically on errors::

        async for websocket in connect(...):
            try:
                ...
            except websockets.exceptions.ConnectionClosed:
                continue

    The connection is closed automatically after each iteration of the loop.

    If an error occurs while establishing the connection, :func:`connect`
    retries with exponential backoff. The backoff delay starts at three
    seconds and increases up to one minute.

    If an error occurs in the body of the loop, you can handle the exception
    and :func:`connect` will reconnect with the next iteration; or you can
    let the exception bubble up and break out of the loop. This lets you
    decide which errors trigger a reconnection and which errors are fatal.

    Args:
        uri: URI of the WebSocket server.
        create_protocol: Factory for the :class:`asyncio.Protocol` managing
            the connection. It defaults to :class:`WebSocketClientProtocol`.
            Set it to a wrapper or a subclass to customize connection handling.
        logger: Logger for this client.
            It defaults to ``logging.getLogger("websockets.client")``.
            See the :doc:`logging guide <../../topics/logging>` for details.
        compression: The "permessage-deflate" extension is enabled by default.
            Set ``compression`` to :obj:`None` to disable it. See the
            :doc:`compression guide <../../topics/compression>` for details.
        origin: Value of the ``Origin`` header, for servers that require it.
        extensions: List of supported extensions, in order in which they
            should be negotiated and run.
        subprotocols: List of supported subprotocols, in order of decreasing
            preference.
        extra_headers: Arbitrary HTTP headers to add to the handshake request.
        user_agent_header: Value of  the ``User-Agent`` request header.
            It defaults to ``"Python/x.y.z websockets/X.Y"``.
            Setting it to :obj:`None` removes the header.
        open_timeout: Timeout for opening the connection in seconds.
            :obj:`None` disables the timeout.

    See :class:`~websockets.legacy.protocol.WebSocketCommonProtocol` for the
    documentation of ``ping_interval``, ``ping_timeout``, ``close_timeout``,
    ``max_size``, ``max_queue``, ``read_limit``, and ``write_limit``.

    Any other keyword arguments are passed the event loop\'s
    :meth:`~asyncio.loop.create_connection` method.

    For example:

    * You can set ``ssl`` to a :class:`~ssl.SSLContext` to enforce TLS
      settings. When connecting to a ``wss://`` URI, if ``ssl`` isn\'t
      provided, a TLS context is created
      with :func:`~ssl.create_default_context`.

    * You can set ``host`` and ``port`` to connect to a different host and
      port from those found in ``uri``. This only changes the destination of
      the TCP connection. The host name from ``uri`` is still used in the TLS
      handshake for secure connections and in the ``Host`` header.

    Raises:
        InvalidURI: If ``uri`` isn\'t a valid WebSocket URI.
        OSError: If the TCP connection fails.
        InvalidHandshake: If the opening handshake fails.
        ~asyncio.TimeoutError: If the opening handshake times out.

    '''
    MAX_REDIRECTS_ALLOWED = int(os.environ.get('WEBSOCKETS_MAX_REDIRECTS', '10'))
    
    def __init__(self = None, uri = None, *, create_protocol, logger, compression, origin, extensions, subprotocols, extra_headers, user_agent_header, open_timeout, ping_interval, ping_timeout, close_timeout, max_size, max_queue, read_limit, write_limit, **kwargs):
        timeout = kwargs.pop('timeout', None)
    # WARNING: Decompyle incomplete

    
    def handle_redirect(self = None, uri = None):
        old_uri = self._uri
        old_wsuri = self._wsuri
        new_uri = urllib.parse.urljoin(old_uri, uri)
        new_wsuri = parse_uri(new_uri)
        if not old_wsuri.secure and new_wsuri.secure:
            raise SecurityError('redirect from WSS to WS')
    # WARNING: Decompyle incomplete

    BACKOFF_INITIAL = float(os.environ.get('WEBSOCKETS_BACKOFF_INITIAL_DELAY', '5'))
    BACKOFF_MIN = float(os.environ.get('WEBSOCKETS_BACKOFF_MIN_DELAY', '3.1'))
    BACKOFF_MAX = float(os.environ.get('WEBSOCKETS_BACKOFF_MAX_DELAY', '90.0'))
    BACKOFF_FACTOR = float(os.environ.get('WEBSOCKETS_BACKOFF_FACTOR', '1.618'))
    
    def __aiter__(self = None):
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

connect = Connect

def unix_connect(path = None, uri = None, **kwargs):
    """
    Similar to :func:`connect`, but for connecting to a Unix socket.

    This function builds upon the event loop's
    :meth:`~asyncio.loop.create_unix_connection` method.

    It is only available on Unix.

    It's mainly useful for debugging servers listening on Unix sockets.

    Args:
        path: File system path to the Unix socket.
        uri: URI of the WebSocket server; the host is used in the TLS
            handshake for secure connections and in the ``Host`` header.

    """
    pass
# WARNING: Decompyle incomplete
