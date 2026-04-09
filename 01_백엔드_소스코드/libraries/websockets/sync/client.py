# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client.pyc (Python 3.11)

from __future__ import annotations
import socket
import ssl as ssl_module
import threading
import warnings
from collections.abc import Sequence
from typing import Any, Callable, Literal, TypeVar, cast
from client import ClientProtocol
from datastructures import Headers, HeadersLike
from exceptions import InvalidProxyMessage, InvalidProxyStatus, ProxyError
from extensions.base import ClientExtensionFactory
from extensions.permessage_deflate import enable_client_permessage_deflate
from headers import build_authorization_basic, build_host, validate_subprotocols
from http11 import USER_AGENT, Response
from protocol import CONNECTING, Event
from streams import StreamReader
from typing import LoggerLike, Origin, Subprotocol
from uri import Proxy, WebSocketURI, get_proxy, parse_proxy, parse_uri
from connection import Connection
from utils import Deadline
__all__ = [
    'connect',
    'unix_connect',
    'ClientConnection']

class ClientConnection(Connection):
    pass
# WARNING: Decompyle incomplete


def connect(uri = None, *, sock, ssl, server_hostname, origin, extensions, subprotocols, compression, additional_headers, user_agent_header, proxy, proxy_ssl, proxy_server_hostname, open_timeout, ping_interval, ping_timeout, close_timeout, max_size, max_queue, logger, create_connection, **kwargs):
    '''
    Connect to the WebSocket server at ``uri``.

    This function returns a :class:`ClientConnection` instance, which you can
    use to send and receive messages.

    :func:`connect` may be used as a context manager::

        from websockets.sync.client import connect

        with connect(...) as websocket:
            ...

    The connection is closed automatically when exiting the context.

    Args:
        uri: URI of the WebSocket server.
        sock: Preexisting TCP socket. ``sock`` overrides the host and port
            from ``uri``. You may call :func:`socket.create_connection` to
            create a suitable TCP socket.
        ssl: Configuration for enabling TLS on the connection.
        server_hostname: Host name for the TLS handshake. ``server_hostname``
            overrides the host name from ``uri``.
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
        proxy_ssl: Configuration for enabling TLS on the proxy connection.
        proxy_server_hostname: Host name for the TLS handshake with the proxy.
            ``proxy_server_hostname`` overrides the host name from ``proxy``.
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
        logger: Logger for this client.
            It defaults to ``logging.getLogger("websockets.client")``.
            See the :doc:`logging guide <../../topics/logging>` for details.
        create_connection: Factory for the :class:`ClientConnection` managing
            the connection. Set it to a wrapper or a subclass to customize
            connection handling.

    Any other keyword arguments are passed to :func:`~socket.create_connection`.

    Raises:
        InvalidURI: If ``uri`` isn\'t a valid WebSocket URI.
        OSError: If the TCP connection fails.
        InvalidHandshake: If the opening handshake fails.
        TimeoutError: If the opening handshake times out.

    '''
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
            ``ws://localhost/`` or, when a ``ssl`` is provided, to
            ``wss://localhost/``.

    """
    pass
# WARNING: Decompyle incomplete


try:
    from python_socks import ProxyType
    from python_socks.sync import Proxy as SocksProxy
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
    
    def connect_socks_proxy(proxy = None, ws_uri = None, deadline = None, **kwargs):
        '''Connect via a SOCKS proxy and return the socket.'''
        socks_proxy = SocksProxy(SOCKS_PROXY_TYPES[proxy.scheme], proxy.host, proxy.port, proxy.username, proxy.password, SOCKS_PROXY_RDNS[proxy.scheme])
        kwargs.setdefault('timeout', deadline.timeout())
    # WARNING: Decompyle incomplete

except ImportError:
    
    def connect_socks_proxy(proxy = None, ws_uri = None, deadline = None, **kwargs):
        raise ImportError('python-socks is required to use a SOCKS proxy')



def prepare_connect_request(proxy = None, ws_uri = None, user_agent_header = None):
    host = build_host(ws_uri.host, ws_uri.port, ws_uri.secure, always_include_port = True)
    headers = Headers()
    headers['Host'] = build_host(ws_uri.host, ws_uri.port, ws_uri.secure)
# WARNING: Decompyle incomplete


def read_connect_response(sock = None, deadline = None):
    reader = StreamReader()
    parser = Response.parse(reader.read_line, reader.read_exact, reader.read_to_eof, include_body = False)
# WARNING: Decompyle incomplete


def connect_http_proxy(proxy = None, ws_uri = None, deadline = None, *, user_agent_header, ssl, server_hostname, **kwargs):
    kwargs.setdefault('timeout', deadline.timeout())
# WARNING: Decompyle incomplete

T = TypeVar('T')
F = TypeVar('F', bound = Callable[(..., T)])

class SSLSSLSocket:
    '''
    Socket-like object providing TLS-in-TLS.

    Only methods that are used by websockets are implemented.

    '''
    recv_bufsize = 65536
    
    def __init__(self = None, sock = None, ssl_context = None, server_hostname = (None,)):
        self.incoming = ssl_module.MemoryBIO()
        self.outgoing = ssl_module.MemoryBIO()
        self.ssl_socket = sock
        self.ssl_object = ssl_context.wrap_bio(self.incoming, self.outgoing, server_hostname = server_hostname)
        self.run_io(self.ssl_object.do_handshake)

    
    def run_io(self = None, func = None, *args):
        want_read = False
        want_write = False
    # WARNING: Decompyle incomplete

    
    def recv(self = None, buflen = None):
        
        try:
            return self.run_io(self.ssl_object.read, buflen)
        except ssl_module.SSLEOFError:
            return b''


    
    def send(self = None, data = None):
        return self.run_io(self.ssl_object.write, data)

    
    def sendall(self = None, data = None):
        count = 0
        view = memoryview(data)
        byte_view = view.cast('B')
        amount = len(byte_view)
    # WARNING: Decompyle incomplete

    
    def __getattr__(self = None, name = None):
        return getattr(self.ssl_socket, name)
