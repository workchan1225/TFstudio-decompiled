# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _exceptions.pyc (Python 3.11)

'''
Our exception hierarchy:

* HTTPError
  x RequestError
    + TransportError
      - TimeoutException
        · ConnectTimeout
        · ReadTimeout
        · WriteTimeout
        · PoolTimeout
      - NetworkError
        · ConnectError
        · ReadError
        · WriteError
        · CloseError
      - ProtocolError
        · LocalProtocolError
        · RemoteProtocolError
      - ProxyError
      - UnsupportedProtocol
    + DecodingError
    + TooManyRedirects
  x HTTPStatusError
* InvalidURL
* CookieConflict
* StreamError
  x StreamConsumed
  x StreamClosed
  x ResponseNotRead
  x RequestNotRead
'''
from __future__ import annotations
import contextlib
import typing
if typing.TYPE_CHECKING:
    from _models import Request, Response
__all__ = [
    'CloseError',
    'ConnectError',
    'ConnectTimeout',
    'CookieConflict',
    'DecodingError',
    'HTTPError',
    'HTTPStatusError',
    'InvalidURL',
    'LocalProtocolError',
    'NetworkError',
    'PoolTimeout',
    'ProtocolError',
    'ProxyError',
    'ReadError',
    'ReadTimeout',
    'RemoteProtocolError',
    'RequestError',
    'RequestNotRead',
    'ResponseNotRead',
    'StreamClosed',
    'StreamConsumed',
    'StreamError',
    'TimeoutException',
    'TooManyRedirects',
    'TransportError',
    'UnsupportedProtocol',
    'WriteError',
    'WriteTimeout']

class HTTPError(Exception):
    pass
# WARNING: Decompyle incomplete


class RequestError(HTTPError):
    pass
# WARNING: Decompyle incomplete


class TransportError(RequestError):
    '''
    Base class for all exceptions that occur at the level of the Transport API.
    '''
    pass


class TimeoutException(TransportError):
    '''
    The base class for timeout errors.

    An operation has timed out.
    '''
    pass


class ConnectTimeout(TimeoutException):
    '''
    Timed out while connecting to the host.
    '''
    pass


class ReadTimeout(TimeoutException):
    '''
    Timed out while receiving data from the host.
    '''
    pass


class WriteTimeout(TimeoutException):
    '''
    Timed out while sending data to the host.
    '''
    pass


class PoolTimeout(TimeoutException):
    '''
    Timed out waiting to acquire a connection from the pool.
    '''
    pass


class NetworkError(TransportError):
    '''
    The base class for network-related errors.

    An error occurred while interacting with the network.
    '''
    pass


class ReadError(NetworkError):
    '''
    Failed to receive data from the network.
    '''
    pass


class WriteError(NetworkError):
    '''
    Failed to send data through the network.
    '''
    pass


class ConnectError(NetworkError):
    '''
    Failed to establish a connection.
    '''
    pass


class CloseError(NetworkError):
    '''
    Failed to close a connection.
    '''
    pass


class ProxyError(TransportError):
    '''
    An error occurred while establishing a proxy connection.
    '''
    pass


class UnsupportedProtocol(TransportError):
    '''
    Attempted to make a request to an unsupported protocol.

    For example issuing a request to `ftp://www.example.com`.
    '''
    pass


class ProtocolError(TransportError):
    '''
    The protocol was violated.
    '''
    pass


class LocalProtocolError(ProtocolError):
    '''
    A protocol was violated by the client.

    For example if the user instantiated a `Request` instance explicitly,
    failed to include the mandatory `Host:` header, and then issued it directly
    using `client.send()`.
    '''
    pass


class RemoteProtocolError(ProtocolError):
    '''
    The protocol was violated by the server.

    For example, returning malformed HTTP.
    '''
    pass


class DecodingError(RequestError):
    '''
    Decoding of the response failed, due to a malformed encoding.
    '''
    pass


class TooManyRedirects(RequestError):
    '''
    Too many redirects.
    '''
    pass


class HTTPStatusError(HTTPError):
    pass
# WARNING: Decompyle incomplete


class InvalidURL(Exception):
    pass
# WARNING: Decompyle incomplete


class CookieConflict(Exception):
    pass
# WARNING: Decompyle incomplete


class StreamError(RuntimeError):
    pass
# WARNING: Decompyle incomplete


class StreamConsumed(StreamError):
    pass
# WARNING: Decompyle incomplete


class StreamClosed(StreamError):
    pass
# WARNING: Decompyle incomplete


class ResponseNotRead(StreamError):
    pass
# WARNING: Decompyle incomplete


class RequestNotRead(StreamError):
    pass
# WARNING: Decompyle incomplete

request_context = (lambda request = None: pass# WARNING: Decompyle incomplete
)()
