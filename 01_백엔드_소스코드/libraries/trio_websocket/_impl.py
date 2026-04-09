# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _impl.pyc (Python 3.11)

from __future__ import annotations
import sys
from collections import OrderedDict
from contextlib import asynccontextmanager, AbstractAsyncContextManager
from functools import partial
from ipaddress import ip_address
import itertools
import logging
import random
import ssl
import struct
import urllib.parse as urllib
from typing import Any, List, NoReturn, Optional, Union, TypeVar, TYPE_CHECKING, Generic, cast
from importlib.metadata import version
import outcome
import trio
import trio.abc as trio
from wsproto import ConnectionType, WSConnection
from wsproto.connection import ConnectionState
from wsproto.frame_protocol import frame_protocol as wsframeproto
from wsproto.events import AcceptConnection, BytesMessage, CloseConnection, Ping, Pong, RejectConnection, RejectData, Request, TextMessage
import wsproto.utilities as wsproto
if sys.version_info < (3, 11):
    from exceptiongroup import BaseExceptionGroup
if TYPE_CHECKING:
    from types import TracebackType
    from typing_extensions import Final
    from collections.abc import AsyncGenerator, Awaitable, Callable, Iterable, Coroutine, Sequence
_IS_TRIO_MULTI_ERROR: 'Final' = tuple(map(int, version('trio').split('.')[:2])) < (0, 22)
if _IS_TRIO_MULTI_ERROR:
    _TRIO_EXC_GROUP_TYPE = trio.MultiError
else:
    _TRIO_EXC_GROUP_TYPE = BaseExceptionGroup
CONN_TIMEOUT: 'Final' = 60
MESSAGE_QUEUE_SIZE: 'Final' = 1
MAX_MESSAGE_SIZE: 'Final' = 1048576
RECEIVE_BYTES: 'Final' = 4096
logger: 'Final' = logging.getLogger('trio-websocket')
T = TypeVar('T')
E = TypeVar('E', bound = BaseException)

class TrioWebsocketInternalError(Exception):
    '''Raised as a fallback when open_websocket is unable to unwind an exceptiongroup
    into a single preferred exception. This should never happen, if it does then
    underlying assumptions about the internal code are incorrect.
    '''
    pass


def _ignore_cancel(exc = None):
    return None if isinstance(exc, trio.Cancelled) else exc


class _preserve_current_exception:
    '''A context manager which should surround an ``__exit__`` or
    ``__aexit__`` handler or the contents of a ``finally:``
    block. It ensures that any exception that was being handled
    upon entry is not masked by a `trio.Cancelled` raised within
    the body of the context manager.

    https://github.com/python-trio/trio/issues/1559
    https://gitter.im/python-trio/general?at=5faf2293d37a1a13d6a582cf
    '''
    __slots__ = ('_armed',)
    
    def __init__(self = None):
        self._armed = False

    
    def __enter__(self = None):
        self._armed = sys.exc_info()[1] is not None

    
    def __exit__(self = None, ty = None, value = None, tb = ('ty', 'type[BaseException] | None', 'value', 'BaseException | None', 'tb', 'TracebackType | None', 'return', 'bool')):
        pass
    # WARNING: Decompyle incomplete


open_websocket = (lambda host = None, port = None, resource = None, *, use_ssl, subprotocols, extra_headers: pass# WARNING: Decompyle incomplete
)()

async def connect_websocket(nursery = None, host = None, port = None, resource = None, *, use_ssl, subprotocols, extra_headers, message_queue_size, max_message_size, receive_buffer_size):
    """
    Return an open WebSocket client connection to a host.

    This function is used to specify a custom nursery to run connection
    background tasks in. The caller is responsible for closing the connection.

    If you don't need a custom nursery, you should probably use
    :func:`open_websocket` instead.

    :param nursery: A Trio nursery to run background tasks in.
    :param str host: The host to connect to.
    :param int port: The port to connect to.
    :param str resource: The resource, i.e. URL path.
    :param Union[bool, ssl.SSLContext] use_ssl: If this is an SSL context, then
        use that context. If this is ``True`` then use default SSL context. If
        this is ``False`` then disable SSL.
    :param subprotocols: An iterable of strings representing preferred
        subprotocols.
    :param list[tuple[bytes,bytes]] extra_headers: A list of 2-tuples containing
        HTTP header key/value pairs to send with the connection request. Note
        that headers used by the WebSocket protocol (e.g.
        ``Sec-WebSocket-Accept``) will be overwritten.
    :param int message_queue_size: The maximum number of messages that will be
        buffered in the library's internal message queue.
    :param int max_message_size: The maximum message size as measured by
        ``len()``. If a message is received that is larger than this size,
        then the connection is closed with code 1009 (Message Too Big).
    :param Optional[int] receive_buffer_size: The buffer size we use to
        receive messages internally. None to let trio choose. Defaults
        to 4 KiB.
    :rtype: WebSocketConnection
    """
    pass
# WARNING: Decompyle incomplete


def open_websocket_url(url = None, ssl_context = None, *, subprotocols, extra_headers, message_queue_size, max_message_size, connect_timeout, disconnect_timeout, receive_buffer_size):
    """
    Open a WebSocket client connection to a URL.

    This async context manager connects when entering the context manager and
    disconnects when exiting. It yields a
    :class:`WebSocketConnection` instance.

    :param str url: A WebSocket URL, i.e. `ws:` or `wss:` URL scheme.
    :param ssl_context: Optional SSL context used for ``wss:`` URLs. A default
        SSL context is used for ``wss:`` if this argument is ``None``.
    :type ssl_context: ssl.SSLContext or None
    :param subprotocols: An iterable of strings representing preferred
        subprotocols.
    :param list[tuple[bytes,bytes]] extra_headers: A list of 2-tuples containing
        HTTP header key/value pairs to send with the connection request. Note
        that headers used by the WebSocket protocol (e.g.
        ``Sec-WebSocket-Accept``) will be overwritten.
    :param int message_queue_size: The maximum number of messages that will be
        buffered in the library's internal message queue.
    :param int max_message_size: The maximum message size as measured by
        ``len()``. If a message is received that is larger than this size,
        then the connection is closed with code 1009 (Message Too Big).
    :param Optional[int] receive_buffer_size: The buffer size we use to
        receive messages internally. None to let trio choose. Defaults
        to 4 KiB.
    :param float connect_timeout: The number of seconds to wait for the
        connection before timing out.
    :param float disconnect_timeout: The number of seconds to wait when closing
        the connection before timing out.
    :raises HandshakeError: for any networking error,
        client-side timeout (:exc:`ConnectionTimeout`, :exc:`DisconnectionTimeout`),
        or server rejection (:exc:`ConnectionRejected`) during handshakes.
    """
    (host, port, resource, return_ssl_context) = _url_to_host(url, ssl_context)
    return open_websocket(host, port, resource, use_ssl = return_ssl_context, subprotocols = subprotocols, extra_headers = extra_headers, message_queue_size = message_queue_size, max_message_size = max_message_size, receive_buffer_size = receive_buffer_size, connect_timeout = connect_timeout, disconnect_timeout = disconnect_timeout)


async def connect_websocket_url(nursery = None, url = None, ssl_context = None, *, subprotocols, extra_headers, message_queue_size, max_message_size, receive_buffer_size):
    """
    Return an open WebSocket client connection to a URL.

    This function is used to specify a custom nursery to run connection
    background tasks in. The caller is responsible for closing the connection.

    If you don't need a custom nursery, you should probably use
    :func:`open_websocket_url` instead.

    :param nursery: A nursery to run background tasks in.
    :param str url: A WebSocket URL.
    :param ssl_context: Optional SSL context used for ``wss:`` URLs.
    :type ssl_context: ssl.SSLContext or None
    :param subprotocols: An iterable of strings representing preferred
        subprotocols.
    :param list[tuple[bytes,bytes]] extra_headers: A list of 2-tuples containing
        HTTP header key/value pairs to send with the connection request. Note
        that headers used by the WebSocket protocol (e.g.
        ``Sec-WebSocket-Accept``) will be overwritten.
    :param int message_queue_size: The maximum number of messages that will be
        buffered in the library's internal message queue.
    :param int max_message_size: The maximum message size as measured by
        ``len()``. If a message is received that is larger than this size,
        then the connection is closed with code 1009 (Message Too Big).
    :param Optional[int] receive_buffer_size: The buffer size we use to
        receive messages internally. None to let trio choose. Defaults
        to 4 KiB.
    :rtype: WebSocketConnection
    """
    pass
# WARNING: Decompyle incomplete


def _url_to_host(url = None, ssl_context = None):
    '''
    Convert a WebSocket URL to a (host,port,resource) tuple.

    The returned ``ssl_context`` is either the same object that was passed in,
    or if ``ssl_context`` is None, then a bool indicating if a default SSL
    context needs to be created.

    :param str url: A WebSocket URL.
    :type ssl_context: ssl.SSLContext or None
    :returns: A tuple of ``(host, port, resource, ssl_context)``.
    '''
    url = str(url)
    parts = urllib.parse.urlsplit(url)
    if parts.scheme not in ('ws', 'wss'):
        raise ValueError('WebSocket URL scheme must be "ws:" or "wss:"')
# WARNING: Decompyle incomplete


async def wrap_client_stream(nursery = None, stream = None, host = None, resource = None, *, subprotocols, extra_headers, message_queue_size, max_message_size, receive_buffer_size):
    """
    Wrap an arbitrary stream in a WebSocket connection.

    This is a low-level function only needed in rare cases. In most cases, you
    should use :func:`open_websocket` or :func:`open_websocket_url`.

    :param nursery: A Trio nursery to run background tasks in.
    :param stream: A Trio stream to be wrapped.
    :type stream: trio.abc.Stream
    :param str host: A host string that will be sent in the ``Host:`` header.
    :param str resource: A resource string, i.e. the path component to be
        accessed on the server.
    :param subprotocols: An iterable of strings representing preferred
        subprotocols.
    :param list[tuple[bytes,bytes]] extra_headers: A list of 2-tuples containing
        HTTP header key/value pairs to send with the connection request. Note
        that headers used by the WebSocket protocol (e.g.
        ``Sec-WebSocket-Accept``) will be overwritten.
    :param int message_queue_size: The maximum number of messages that will be
        buffered in the library's internal message queue.
    :param int max_message_size: The maximum message size as measured by
        ``len()``. If a message is received that is larger than this size,
        then the connection is closed with code 1009 (Message Too Big).
    :param Optional[int] receive_buffer_size: The buffer size we use to
        receive messages internally. None to let trio choose. Defaults
        to 4 KiB.
    :rtype: WebSocketConnection
    """
    pass
# WARNING: Decompyle incomplete


async def wrap_server_stream(nursery = None, stream = None, message_queue_size = None, max_message_size = (MESSAGE_QUEUE_SIZE, MAX_MESSAGE_SIZE, RECEIVE_BYTES), receive_buffer_size = ('nursery', 'trio.Nursery', 'stream', 'trio.abc.Stream', 'message_queue_size', 'int', 'max_message_size', 'int', 'receive_buffer_size', 'Union[None, int]', 'return', 'WebSocketRequest')):
    """
    Wrap an arbitrary stream in a server-side WebSocket.

    This is a low-level function only needed in rare cases. In most cases, you
    should use :func:`serve_websocket`.

    :param nursery: A nursery to run background tasks in.
    :param stream: A stream to be wrapped.
    :param int message_queue_size: The maximum number of messages that will be
        buffered in the library's internal message queue.
    :param int max_message_size: The maximum message size as measured by
        ``len()``. If a message is received that is larger than this size,
        then the connection is closed with code 1009 (Message Too Big).
    :param Optional[int] receive_buffer_size: The buffer size we use to
        receive messages internally. None to let trio choose. Defaults
        to 4 KiB.
    :type stream: trio.abc.Stream
    :rtype: WebSocketRequest
    """
    pass
# WARNING: Decompyle incomplete


async def serve_websocket(handler = None, host = None, port = None, ssl_context = None, *, handler_nursery, message_queue_size, max_message_size, receive_buffer_size, connect_timeout, disconnect_timeout, task_status):
    """
    Serve a WebSocket over TCP.

    This function supports the Trio nursery start protocol: ``server = await
    nursery.start(serve_websocket, …)``. It will block until the server
    is accepting connections and then return a :class:`WebSocketServer` object.

    Note that if ``host`` is ``None`` and ``port`` is zero, then you may get
    multiple listeners that have *different port numbers!*

    :param handler: An async function that is invoked with a request
        for each new connection.
    :param host: The host interface to bind. This can be an address of an
        interface, a name that resolves to an interface address (e.g.
        ``localhost``), or a wildcard address like ``0.0.0.0`` for IPv4 or
        ``::`` for IPv6. If ``None``, then all local interfaces are bound.
    :type host: str, bytes, or None
    :param int port: The port to bind to.
    :param ssl_context: The SSL context to use for encrypted connections, or
        ``None`` for unencrypted connection.
    :type ssl_context: ssl.SSLContext or None
    :param handler_nursery: An optional nursery to spawn handlers and background
        tasks in. If not specified, a new nursery will be created internally.
    :param int message_queue_size: The maximum number of messages that will be
        buffered in the library's internal message queue.
    :param int max_message_size: The maximum message size as measured by
        ``len()``. If a message is received that is larger than this size,
        then the connection is closed with code 1009 (Message Too Big).
    :param Optional[int] receive_buffer_size: The buffer size we use to
        receive messages internally. None to let trio choose. Defaults
        to 4 KiB.
    :param float connect_timeout: The number of seconds to wait for a client
        to finish connection handshake before timing out.
    :param float disconnect_timeout: The number of seconds to wait for a client
        to finish the closing handshake before timing out.
    :param task_status: Part of Trio nursery start protocol.
    :returns: This function runs until cancelled.
    """
    pass
# WARNING: Decompyle incomplete


class HandshakeError(Exception):
    '''
    There was an error during connection or disconnection with the websocket
    server.
    '''
    pass


class ConnectionTimeout(HandshakeError):
    '''There was a timeout when connecting to the websocket server.'''
    pass


class DisconnectionTimeout(HandshakeError):
    '''There was a timeout when disconnecting from the websocket server.'''
    pass


class ConnectionClosed(Exception):
    pass
# WARNING: Decompyle incomplete


class ConnectionRejected(HandshakeError):
    pass
# WARNING: Decompyle incomplete


class CloseReason:
    ''' Contains information about why a WebSocket was closed. '''
    
    def __init__(self = None, code = None, reason = None):
        '''
        Constructor.

        :param int code:
        :param Optional[str] reason:
        '''
        self._code = code
        
        try:
            self._name = wsframeproto.CloseReason(code).name
        except ValueError:
            if  <= 1000, code or 1000, code <= 2999:
                pass
            
        except:
            pass
        except:
            if  <= 3000, code or 3000, code <= 3999:
                pass
            else:
                'RFC_RESERVED'
        except:
            pass
        except:
            if  <= 4000, code or 4000, code <= 4999:
                pass
            else:
                'IANA_RESERVED'
        except:
            pass
        except:
            'INVALID_CODE' = 'PRIVATE_RESERVED'

        self._reason = reason

    code = (lambda self = None: self._code)()
    name = (lambda self = None: self._name)()
    reason = (lambda self = None: self._reason)()
    
    def __repr__(self = None):
        ''' Show close code, name, and reason. '''
        return f'''{self.__class__.__name__}<code={self.code}, name={self.name}, reason={self.reason}>'''


NULL: 'Final' = object()

def Future():
    '''Future'''
    __doc__ = ' Represents a value that will be available in the future. '
    
    def __init__(self = None):
        ''' Constructor. '''
        self._value = cast(T, NULL)
        self._value_event = trio.Event()

    
    def set_value(self = None, value = None):
        '''
        Set a value, which will notify any waiters.

        :param value:
        '''
        self._value = value
        self._value_event.set()

    
    async def wait_value(self = None):
        '''
        Wait for this future to have a value, then return it.

        :returns: The value set by ``set_value()``.
        '''
        pass
    # WARNING: Decompyle incomplete


Future = <NODE:27>(Future, 'Future', Generic[T])

class WebSocketRequest:
    '''
    Represents a handshake presented by a client to a server.

    The server may modify the handshake or leave it as is. The server should
    call ``accept()`` to finish the handshake and obtain a connection object.
    '''
    
    def __init__(self = None, connection = None, event = None):
        '''
        Constructor.

        :param WebSocketConnection connection:
        :type event: wsproto.events.Request
        '''
        self._connection = connection
        self._event = event

    headers = (lambda self = None: self._event.extra_headers)()
    path = (lambda self = None: self._event.target)()
    proposed_subprotocols = (lambda self = None: tuple(self._event.subprotocols))()
    local = (lambda self = None: self._connection.local)()
    remote = (lambda self = None: self._connection.remote)()
    
    async def accept(self = None, *, subprotocol, extra_headers):
        '''
        Accept the request and return a connection object.

        :param subprotocol: The selected subprotocol for this connection.
        :type subprotocol: str or None
        :param extra_headers: A list of 2-tuples containing key/value pairs to
            send as HTTP headers.
        :type extra_headers: list[tuple[bytes,bytes]] or None
        :rtype: WebSocketConnection
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def reject(self = None, status_code = None, *, extra_headers, body):
        '''
        Reject the handshake.

        :param int status_code: The 3 digit HTTP status code. In order to be
            RFC-compliant, this should NOT be 101, and would ideally be an
            appropriate code in the range 300-599.
        :param list[tuple[bytes,bytes]] extra_headers: A list of 2-tuples
            containing key/value pairs to send as HTTP headers.
        :param body: If provided, this data will be sent in the response
            body, otherwise no response body will be sent.
        :type body: bytes or None
        '''
        pass
    # WARNING: Decompyle incomplete



def _get_stream_endpoint(stream = None, *, local):
    '''
    Construct an endpoint from a stream.

    :param trio.Stream stream:
    :param bool local: If true, return local endpoint. Otherwise return remote.
    :returns: An endpoint instance or ``repr()`` for streams that cannot be
        represented as an endpoint.
    :rtype: Endpoint or str
    '''
    (socket, is_ssl) = (None, False)
    if isinstance(stream, trio.SocketStream):
        socket = stream.socket
    elif isinstance(stream, trio.SSLStream):
        socket = stream.transport_stream.socket
        is_ssl = True
# WARNING: Decompyle incomplete


class WebSocketConnection(trio.abc.AsyncResource):
    ''' A WebSocket connection. '''
    CONNECTION_ID = itertools.count()
    
    def __init__(self = None, stream = None, ws_connection = None, *, host, path, client_subprotocols, client_extra_headers, message_queue_size, max_message_size, receive_buffer_size):
        """
        Constructor.

        Generally speaking, users are discouraged from directly instantiating a
        ``WebSocketConnection`` and should instead use one of the convenience
        functions in this module, e.g. ``open_websocket()`` or
        ``serve_websocket()``. This class has some tricky internal logic and
        timing that depends on whether it is an instance of a client connection
        or a server connection. The convenience functions handle this complexity
        for you.

        :param SocketStream stream:
        :param ws_connection wsproto.WSConnection:
        :param str host: The hostname to send in the HTTP request headers. Only
            used for client connections.
        :param str path: The URL path for this connection.
        :param list client_subprotocols: A list of desired subprotocols. Only
            used for client connections.
        :param list[tuple[bytes,bytes]] client_extra_headers: Extra headers to
            send with the connection request. Only used for client connections.
        :param int message_queue_size: The maximum number of messages that will be
            buffered in the library's internal message queue.
        :param int max_message_size: The maximum message size as measured by
            ``len()``. If a message is received that is larger than this size,
            then the connection is closed with code 1009 (Message Too Big).
        :param Optional[int] receive_buffer_size: The buffer size we use to
            receive messages internally. None to let trio choose. Defaults
            to 4 KiB.
        """
        self._close_reason = None
        self._id = next(self.__class__.CONNECTION_ID)
        self._stream = stream
        self._stream_lock = trio.StrictFIFOLock()
        self._wsproto = ws_connection
        self._message_size = 0
        self._message_parts = []
        self._max_message_size = max_message_size
        self._receive_buffer_size = receive_buffer_size
        self._reader_running = True
    # WARNING: Decompyle incomplete

    closed = (lambda self = None: self._close_reason)()
    is_client = (lambda self = None: self._wsproto.client)()
    is_server = (lambda self = None: not (self._wsproto.client))()
    local = (lambda self = None: _get_stream_endpoint(self._stream, local = True))()
    remote = (lambda self = None: _get_stream_endpoint(self._stream, local = False))()
    path = (lambda self = None: self._path)()
    subprotocol = (lambda self = None: self._subprotocol)()
    handshake_headers = (lambda self = None: self._handshake_headers)()
    
    async def aclose(self = None, code = None, reason = None):
        '''
        Close the WebSocket connection.

        This sends a closing frame and suspends until the connection is closed.
        After calling this method, any further I/O on this WebSocket (such as
        ``get_message()`` or ``send_message()``) will raise
        ``ConnectionClosed``.

        This method is idempotent: it may be called multiple times on the same
        connection without any errors.

        :param int code: A 4-digit code number indicating the type of closure.
        :param str reason: An optional string describing the closure.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _aclose(self = None, code = None, reason = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def get_message(self = None):
        '''
        Receive the next WebSocket message.

        If no message is available immediately, then this function blocks until
        a message is ready.

        If the remote endpoint closes the connection, then the caller can still
        get messages sent prior to closing. Once all pending messages have been
        retrieved, additional calls to this method will raise
        ``ConnectionClosed``. If the local endpoint closes the connection, then
        pending messages are discarded and calls to this method will immediately
        raise ``ConnectionClosed``.

        :rtype: str or bytes
        :raises ConnectionClosed: if the connection is closed.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def ping(self = None, payload = None):
        '''
        Send WebSocket ping to remote endpoint and wait for a correspoding pong.

        Each in-flight ping must include a unique payload. This function sends
        the ping and then waits for a corresponding pong from the remote
        endpoint.

        *Note: If the remote endpoint recieves multiple pings, it is allowed to
        send a single pong. Therefore, the order of calls to ``ping()`` is
        tracked, and a pong will wake up its corresponding ping as well as all
        previous in-flight pings.*

        :param payload: The payload to send. If ``None`` then a random 32-bit
            payload is created.
        :type payload: bytes or None
        :raises ConnectionClosed: if connection is closed.
        :raises ValueError: if ``payload`` is identical to another in-flight
            ping.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def pong(self = None, payload = None):
        """
        Send an unsolicted pong.

        :param payload: The pong's payload. If ``None``, then no payload is
            sent.
        :type payload: bytes or None
        :raises ConnectionClosed: if connection is closed
        """
        pass
    # WARNING: Decompyle incomplete

    
    async def send_message(self = None, message = None):
        '''
        Send a WebSocket message.

        :param message: The message to send.
        :type message: str or bytes
        :raises ConnectionClosed: if connection is closed, or being closed
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        ''' Connection ID and type. '''
        type_ = 'client' if self.is_client else 'server'
        return f'''{type_}-{self._id}'''

    
    async def _accept(self = None, request = None, subprotocol = None, extra_headers = ('request', 'Request', 'subprotocol', 'str | None', 'extra_headers', 'list[tuple[bytes, bytes]]', 'return', 'None')):
        '''
        Accept the handshake.

        This method is only applicable to server-side connections.

        :param wsproto.events.Request request:
        :param subprotocol:
        :type subprotocol: str or None
        :param list[tuple[bytes,bytes]] extra_headers: A list of 2-tuples
            containing key/value pairs to send as HTTP headers.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _reject(self = None, status_code = None, headers = None, body = ('status_code', 'int', 'headers', 'list[tuple[bytes, bytes]]', 'body', 'bytes', 'return', 'None')):
        '''
        Reject the handshake.

        :param int status_code: The 3 digit HTTP status code. In order to be
            RFC-compliant, this must not be 101, and should be an appropriate
            code in the range 300-599.
        :param list[tuple[bytes,bytes]] headers: A list of 2-tuples containing
            key/value pairs to send as HTTP headers.
        :param bytes body: An optional response body.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _abort_web_socket(self = None):
        '''
        If a stream is closed outside of this class, e.g. due to network
        conditions or because some other code closed our stream object, then we
        cannot perform the close handshake. We just need to clean up internal
        state.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _close_stream(self = None):
        ''' Close the TCP connection. '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _close_web_socket(self = None, code = None, reason = None):
        '''
        Mark the WebSocket as closed. Close the message channel so that if any
        tasks are suspended in get_message(), they will wake up with a
        ConnectionClosed exception.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _get_request(self = None):
        '''
        Return a proposal for a WebSocket handshake.

        This method can only be called on server connections and it may only be
        called one time.

        :rtype: WebSocketRequest
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _handle_request_event(self = None, event = None):
        '''
        Handle a connection request.

        This method is async even though it never awaits, because the event
        dispatch requires an async function.

        :param event:
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _handle_accept_connection_event(self = None, event = None):
        '''
        Handle an AcceptConnection event.

        :param wsproto.eventsAcceptConnection event:
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _handle_reject_connection_event(self = None, event = None):
        '''
        Handle a RejectConnection event.

        :param event:
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _handle_reject_data_event(self = None, event = None):
        '''
        Handle a RejectData event.

        :param event:
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _handle_close_connection_event(self = None, event = None):
        '''
        Handle a close event.

        :param wsproto.events.CloseConnection event:
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _handle_message_event(self = None, event = None):
        '''
        Handle a message event.

        :param event:
        :type event: wsproto.events.BytesMessage or wsproto.events.TextMessage
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _handle_ping_event(self = None, event = None):
        '''
        Handle a PingReceived event.

        Wsproto queues a pong frame automatically, so this handler just needs to
        send it.

        :param wsproto.events.Ping event:
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _handle_pong_event(self = None, event = None):
        '''
        Handle a PongReceived event.

        When a pong is received, check if we have any ping requests waiting for
        this pong response. If the remote endpoint skipped any earlier pings,
        then we wake up those skipped pings, too.

        This function is async even though it never awaits, because the other
        event handlers are async, too, and event dispatch would be more
        complicated if some handlers were sync.

        :param event:
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _reader_task(self = None):
        ''' A background task that reads network data and generates events. '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _send(self = None, event = None):
        '''
        Send an event to the remote WebSocket.

        The reader task and one or more writers might try to send messages at
        the same time, so this method uses an internal lock to serialize
        requests to send data.

        :param wsproto.events.Event event:
        '''
        pass
    # WARNING: Decompyle incomplete



class Endpoint:
    ''' Represents a connection endpoint. '''
    
    def __init__(self = None, address = None, port = None, is_ssl = ('address', 'str | int', 'port', 'int', 'is_ssl', 'bool', 'return', 'None')):
        self.address = ip_address(address)
        self.port = port
        self.is_ssl = is_ssl

    url = (lambda self = None: scheme = 'wss' if self.is_ssl else 'ws'if (self.port == 80 or self.is_ssl or self.port == 443) and self.is_ssl:
port_str = ''else:
port_str = ':' + str(self.port)if self.address.version == 4:
f'''{scheme}://{self.address}{port_str}'''f'''{None}://[{self.address}]{port_str}''')()
    
    def __repr__(self = None):
        ''' Return endpoint info as string. '''
        return f'''Endpoint(address="{self.address}", port={self.port}, is_ssl={self.is_ssl})'''



class WebSocketServer:
    '''
    WebSocket server.

    The server class handles incoming connections on one or more ``Listener``
    objects. For each incoming connection, it creates a ``WebSocketConnection``
    instance and starts some background tasks,
    '''
    
    def __init__(self = None, handler = None, listeners = None, *, handler_nursery, message_queue_size, max_message_size, receive_buffer_size, connect_timeout, disconnect_timeout):
        """
        Constructor.

        Note that if ``host`` is ``None`` and ``port`` is zero, then you may get
        multiple listeners that have _different port numbers!_ See the
        ``listeners`` property.

        :param handler: the async function called with a :class:`WebSocketRequest`
            on each new connection.  The call will be made
            once the HTTP handshake completes, which notably implies that the
            connection's `path` property will be valid.
        :param listeners: The WebSocket will be served on each of the listeners.
        :param handler_nursery: An optional nursery to spawn connection tasks
            inside of. If ``None``, then a new nursery will be created
            internally.
        :param Optional[int] receive_buffer_size: The buffer size we use to
            receive messages internally. None to let trio choose. Defaults
            to 4 KiB.
        :param float connect_timeout: The number of seconds to wait for a client
            to finish connection handshake before timing out.
        :param float disconnect_timeout: The number of seconds to wait for a client
            to finish the closing handshake before timing out.
        """
        if len(listeners) == 0:
            raise ValueError('Listeners must contain at least one item.')
        self._handler = handler
        self._handler_nursery = handler_nursery
        self._listeners = listeners
        self._message_queue_size = message_queue_size
        self._max_message_size = max_message_size
        self._receive_buffer_size = receive_buffer_size
        self._connect_timeout = connect_timeout
        self._disconnect_timeout = disconnect_timeout

    port = (lambda self = None: if len(self._listeners) > 1:
raise RuntimeError('Cannot get port because this server has more than 1 listener.')listener = self.listeners[0]try:
listener.portexcept AttributeError:
raise RuntimeError(f'''This socket does not have a port: {repr(listener)}'''), None)()
    listeners = (lambda self = None: listeners = []# WARNING: Decompyle incomplete
)()
    
    async def run(self = None, *, task_status):
        '''
        Start serving incoming connections requests.

        This method supports the Trio nursery start protocol: ``server = await
        nursery.start(server.run, …)``. It will block until the server is
        accepting connections and then return a :class:`WebSocketServer` object.

        :param task_status: Part of the Trio nursery start protocol.
        :returns: This method never returns unless cancelled.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _handle_connection(self = None, stream = None):
        '''
        Handle an incoming connection by spawning a connection background task
        and a handler task inside a new nursery.

        :param stream:
        :type stream: trio.abc.Stream
        '''
        pass
    # WARNING: Decompyle incomplete
