# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client.pyc (Python 3.11)

from __future__ import annotations
import asyncio
import logging
import os
import socket
import ssl as ssl_module
import traceback
import urllib.parse as urllib
from collections.abc import AsyncIterator, Generator, Sequence
from types import TracebackType
from typing import Any, Callable, Literal, cast
from client import ClientProtocol, backoff
from datastructures import Headers, HeadersLike
from exceptions import InvalidMessage, InvalidProxyMessage, InvalidProxyStatus, InvalidStatus, ProxyError, SecurityError
from extensions.base import ClientExtensionFactory
from extensions.permessage_deflate import enable_client_permessage_deflate
from headers import build_authorization_basic, build_host, validate_subprotocols
from http11 import USER_AGENT, Response
from protocol import CONNECTING, Event
from streams import StreamReader
from typing import LoggerLike, Origin, Subprotocol
from uri import Proxy, WebSocketURI, get_proxy, parse_proxy, parse_uri
from compatibility import TimeoutError, asyncio_timeout
from connection import Connection
__all__ = [
    'connect',
    'unix_connect',
    'ClientConnection']
MAX_REDIRECTS = int(os.environ.get('WEBSOCKETS_MAX_REDIRECTS', '10'))

class ClientConnection(Connection):
    pass
# WARNING: Decompyle incomplete


def process_exception(exc = None):
    '''
    Determine whether a connection error is retryable or fatal.

    When reconnecting automatically with ``async for ... in connect(...)``, if a
    connection attempt fails, :func:`process_exception` is called to determine
    whether to retry connecting or to raise the exception.

    This function defines the default behavior, which is to retry on:

    * :exc:`EOFError`, :exc:`OSError`, :exc:`asyncio.TimeoutError`: network
      errors;
    * :exc:`~websockets.exceptions.InvalidStatus` when the status code is 500,
      502, 503, or 504: server or proxy errors.

    All other exceptions are considered fatal.

    You can change this behavior with the ``process_exception`` argument of
    :func:`connect`.

    Return :obj:`None` if the exception is retryable i.e. when the error could
    be transient and trying to reconnect with the same parameters could succeed.
    The exception will be logged at the ``INFO`` level.

    Return an exception, either ``exc`` or a new exception, if the exception is
    fatal i.e. when trying to reconnect will most likely produce the same error.
    That exception will be raised, breaking out of the retry loop.

    '''
    if isinstance(exc, (OSError, TimeoutError, asyncio.TimeoutError)):
        return None
    if None(exc, InvalidMessage) and isinstance(exc.__cause__, EOFError):
        return None
    if None(exc, InvalidStatus) and exc.response.status_code in (500, 502, 503, 504):
        return None


class connect:
    '''
    Connect to the WebSocket server at ``uri``.

    This coroutine returns a :class:`ClientConnection` instance, which you can
    use to send and receive messages.

    :func:`connect` may be used as an asynchronous context manager::

        from websockets.asyncio.client import connect

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

    If the connection fails with a transient error, it is retried with
    exponential backoff. If it fails with a fatal error, the exception is
    raised, breaking out of the loop.

    The connection is closed automatically after each iteration of the loop.

    Args:
        uri: URI of the WebSocket server.
        origin: Value of the ``Origin`` header, for servers that require it.
        extensions: List of supported extensions, in order in which they
            should be negotiated and run.
        subprotocols: List of supported subprotocols, in order of decreasing
            preference.
        compression: The "permessage-deflate" extension is enabled by default.
            Set ``compression`` to :obj:`None` to disable it. See the
            :doc:`compression guide <../../topics/compression>` for details.
        additional_headers (HeadersLike | None): Arbitrary HTTP headers to add
            to the handshake request.
        user_agent_header: Value of  the ``User-Agent`` request header.
            It defaults to ``"Python/x.y.z websockets/X.Y"``.
            Setting it to :obj:`None` removes the header.
        proxy: If a proxy is configured, it is used by default. Set ``proxy``
            to :obj:`None` to disable the proxy or to the address of a proxy
            to override the system configuration. See the :doc:`proxy docs
            <../../topics/proxies>` for details.
        process_exception: When reconnecting automatically, tell whether an
            error is transient or fatal. The default behavior is defined by
            :func:`process_exception`. Refer to its documentation for details.
        open_timeout: Timeout for opening the connection in seconds.
            :obj:`None` disables the timeout.
        ping_interval: Interval between keepalive pings in seconds.
            :obj:`None` disables keepalive.
        ping_timeout: Timeout for keepalive pings in seconds.
            :obj:`None` disables timeouts.
        close_timeout: Timeout for closing the connection in seconds.
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
        logger: Logger for this client.
            It defaults to ``logging.getLogger("websockets.client")``.
            See the :doc:`logging guide <../../topics/logging>` for details.
        create_connection: Factory for the :class:`ClientConnection` managing
            the connection. Set it to a wrapper or a subclass to customize
            connection handling.

    Any other keyword arguments are passed to the event loop\'s
    :meth:`~asyncio.loop.create_connection` method.

    For example:

    * You can set ``ssl`` to a :class:`~ssl.SSLContext` to enforce TLS settings.
      When connecting to a ``wss://`` URI, if ``ssl`` isn\'t provided, a TLS
      context is created with :func:`~ssl.create_default_context`.

    * You can set ``server_hostname`` to override the host name from ``uri`` in
      the TLS handshake.

    * You can set ``host`` and ``port`` to connect to a different host and port
      from those found in ``uri``. This only changes the destination of the TCP
      connection. The host name from ``uri`` is still used in the TLS handshake
      for secure connections and in the ``Host`` header.

    * You can set ``sock`` to provide a preexisting TCP socket. You may call
      :func:`socket.create_connection` (not to be confused with the event loop\'s
      :meth:`~asyncio.loop.create_connection` method) to create a suitable
      client socket and customize it.

    When using a proxy:

    * Prefix keyword arguments with ``proxy_`` for configuring TLS between the
      client and an HTTPS proxy: ``proxy_ssl``, ``proxy_server_hostname``,
      ``proxy_ssl_handshake_timeout``, and ``proxy_ssl_shutdown_timeout``.
    * Use the standard keyword arguments for configuring TLS between the proxy
      and the WebSocket server: ``ssl``, ``server_hostname``,
      ``ssl_handshake_timeout``, and ``ssl_shutdown_timeout``.
    * Other keyword arguments are used only for connecting to the proxy.

    Raises:
        InvalidURI: If ``uri`` isn\'t a valid WebSocket URI.
        InvalidProxy: If ``proxy`` isn\'t a valid proxy.
        OSError: If the TCP connection fails.
        InvalidHandshake: If the opening handshake fails.
        TimeoutError: If the opening handshake times out.

    '''
    
    def __init__(self = None, uri = None, *, origin, extensions, subprotocols, compression, additional_headers, user_agent_header, proxy, process_exception, open_timeout, ping_interval, ping_timeout, close_timeout, max_size, max_queue, write_limit, logger, create_connection, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    async def create_connection(self = None):
        '''Create TCP or Unix connection.'''
        pass
    # WARNING: Decompyle incomplete

    
    def process_redirect(self = None, exc = None):
        """
        Determine whether a connection error is a redirect that can be followed.

        Return the new URI if it's a valid redirect. Else, return an exception.

        """
        if not isinstance(exc, InvalidStatus) and exc.response.status_code in (300, 301, 302, 303, 307, 308) or 'Location' in exc.response.headers:
            return exc
        old_ws_uri = None(self.uri)
        new_uri = urllib.parse.urljoin(self.uri, exc.response.headers['Location'])
        new_ws_uri = parse_uri(new_uri)
    # WARNING: Decompyle incomplete

    
    def __await__(self = None):
        return self.__await_impl__().__await__()

    
    async def __await_impl__(self = None):
        pass
    # WARNING: Decompyle incomplete

    __iter__ = __await__
    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete



def unix_connect(path = None, uri = None, **kwargs):
    """
    Connect to a WebSocket server listening on a Unix socket.

    This function accepts the same keyword arguments as :func:`connect`.

    It's only available on Unix.

    It's mainly useful for debugging servers listening on Unix sockets.

    Args:
        path: File system path to the Unix socket.
        uri: URI of the WebSocket server. ``uri`` defaults to
            ``ws://localhost/`` or, when a ``ssl`` argument is provided, to
            ``wss://localhost/``.

    """
    pass
# WARNING: Decompyle incomplete


try:
    from python_socks import ProxyType
    from python_socks.async_.asyncio import Proxy as SocksProxy
    SOCKS_PROXY_TYPES = {
        'socks5h': ProxyType.SOCKS5,
        'socks5': ProxyType.SOCKS5,
        'socks4a': ProxyType.SOCKS4,
        'socks4': ProxyType.SOCKS4 }
    SOCKS_PROXY_RDNS = {
        'socks5h': True,
        'socks5': False,
        'socks4a': True,
        'socks4': False }
    
    async def connect_socks_proxy(proxy = None, ws_uri = None, **kwargs):
        '''Connect via a SOCKS proxy and return the socket.'''
        pass
    # WARNING: Decompyle incomplete

except ImportError:
    
    async def connect_socks_proxy(proxy = None, ws_uri = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete



def prepare_connect_request(proxy = None, ws_uri = None, user_agent_header = None):
    host = build_host(ws_uri.host, ws_uri.port, ws_uri.secure, always_include_port = True)
    headers = Headers()
    headers['Host'] = build_host(ws_uri.host, ws_uri.port, ws_uri.secure)
# WARNING: Decompyle incomplete


class HTTPProxyConnection(asyncio.Protocol):
    
    def __init__(self = None, ws_uri = None, proxy = None, user_agent_header = (None,)):
        self.ws_uri = ws_uri
        self.proxy = proxy
        self.user_agent_header = user_agent_header
        self.reader = StreamReader()
        self.parser = Response.parse(self.reader.read_line, self.reader.read_exact, self.reader.read_to_eof, include_body = False)
        loop = asyncio.get_running_loop()
        self.response = loop.create_future()

    
    def run_parser(self = None):
        
        try:
            next(self.parser)
            return None
        except StopIteration:
            exc = None
            response = exc.value
            if  <= 200, response.status_code or 200, response.status_code < 300:
                pass
            
        except:
            self.response.set_result(response)
        except:
            self.response.set_exception(InvalidProxyStatus(response))
            del exc
            return None

        None = None
        del exc
        return None
        exc = None
        del exc
        except Exception:
            exc = None
            proxy_exc = InvalidProxyMessage('did not receive a valid HTTP response from proxy')
            proxy_exc.__cause__ = exc
            self.response.set_exception(proxy_exc)
            exc = None
            del exc
            return None
            exc = None
            del exc

    
    def connection_made(self = None, transport = None):
        transport = cast(asyncio.Transport, transport)
        self.transport = transport
        self.transport.write(prepare_connect_request(self.proxy, self.ws_uri, self.user_agent_header))

    
    def data_received(self = None, data = None):
        self.reader.feed_data(data)
        self.run_parser()

    
    def eof_received(self = None):
        self.reader.feed_eof()
        self.run_parser()

    
    def connection_lost(self = None, exc = None):
        self.reader.feed_eof()
    # WARNING: Decompyle incomplete



async def connect_http_proxy(proxy = None, ws_uri = None, user_agent_header = None, **kwargs):
    pass
# WARNING: Decompyle incomplete
