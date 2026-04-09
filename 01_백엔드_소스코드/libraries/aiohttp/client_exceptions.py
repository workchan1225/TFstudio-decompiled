# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client_exceptions.pyc (Python 3.11)

__doc__ = 'HTTP related errors.'
import asyncio
import warnings
from typing import TYPE_CHECKING, Optional, Tuple, Union
from multidict import MultiMapping
from typedefs import StrOrURL
if TYPE_CHECKING:
    import ssl
    SSLContext = ssl.SSLContext
else:
    
    try:
        import ssl
        SSLContext = ssl.SSLContext
    except ImportError:
        ssl = None
        SSLContext = None

    if TYPE_CHECKING:
        from client_reqrep import ClientResponse, ConnectionKey, Fingerprint, RequestInfo
        from http_parser import RawResponseMessage
    else:
        RequestInfo = None
        ClientResponse = None
        ConnectionKey = None
        RawResponseMessage = None
__all__ = ('ClientError', 'ClientConnectionError', 'ClientConnectionResetError', 'ClientOSError', 'ClientConnectorError', 'ClientProxyConnectionError', 'ClientSSLError', 'ClientConnectorDNSError', 'ClientConnectorSSLError', 'ClientConnectorCertificateError', 'ConnectionTimeoutError', 'SocketTimeoutError', 'ServerConnectionError', 'ServerTimeoutError', 'ServerDisconnectedError', 'ServerFingerprintMismatch', 'ClientResponseError', 'ClientHttpProxyError', 'WSServerHandshakeError', 'ContentTypeError', 'ClientPayloadError', 'InvalidURL', 'InvalidUrlClientError', 'RedirectClientError', 'NonHttpUrlClientError', 'InvalidUrlRedirectClientError', 'NonHttpUrlRedirectClientError', 'WSMessageTypeError')

class ClientError(Exception):
    '''Base class for client connection errors.'''
    pass


class ClientResponseError(ClientError):
    '''Base class for exceptions that occur after getting a response.

    request_info: An instance of RequestInfo.
    history: A sequence of responses, if redirects occurred.
    status: HTTP status code.
    message: Error message.
    headers: Response headers.
    '''
    
    def __init__(self = None, request_info = None, history = None, *, code, status, message, headers):
        self.request_info = request_info
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        return '{}, message={!r}, url={!r}'.format(self.status, self.message, str(self.request_info.real_url))

    
    def __repr__(self = None):
        args = f'''{self.request_info!r}, {self.history!r}'''
        if self.status != 0:
            args += f''', status={self.status!r}'''
        if self.message != '':
            args += f''', message={self.message!r}'''
    # WARNING: Decompyle incomplete

    code = (lambda self = None: warnings.warn('code property is deprecated, use status instead', DeprecationWarning, stacklevel = 2)self.status)()
    code = (lambda self = None, value = None: warnings.warn('code property is deprecated, use status instead', DeprecationWarning, stacklevel = 2)self.status = value)()


class ContentTypeError(ClientResponseError):
    '''ContentType found is not valid.'''
    pass


class WSServerHandshakeError(ClientResponseError):
    '''websocket server handshake error.'''
    pass


class ClientHttpProxyError(ClientResponseError):
    '''HTTP proxy error.

    Raised in :class:`aiohttp.connector.TCPConnector` if
    proxy responds with status other than ``200 OK``
    on ``CONNECT`` request.
    '''
    pass


class TooManyRedirects(ClientResponseError):
    '''Client was redirected too many times.'''
    pass


class ClientConnectionError(ClientError):
    '''Base class for client socket errors.'''
    pass


class ClientConnectionResetError(ConnectionResetError, ClientConnectionError):
    '''ConnectionResetError'''
    pass


class ClientOSError(OSError, ClientConnectionError):
    '''OSError error.'''
    pass


class ClientConnectorError(ClientOSError):
    pass
# WARNING: Decompyle incomplete


class ClientConnectorDNSError(ClientConnectorError):
    '''DNS resolution failed during client connection.

    Raised in :class:`aiohttp.connector.TCPConnector` if
        DNS resolution fails.
    '''
    pass


class ClientProxyConnectionError(ClientConnectorError):
    '''Proxy connection error.

    Raised in :class:`aiohttp.connector.TCPConnector` if
        connection to proxy can not be established.
    '''
    pass


class UnixClientConnectorError(ClientConnectorError):
    pass
# WARNING: Decompyle incomplete


class ServerConnectionError(ClientConnectionError):
    '''Server connection errors.'''
    pass


class ServerDisconnectedError(ServerConnectionError):
    '''Server disconnected.'''
    
    def __init__(self = None, message = None):
        pass
    # WARNING: Decompyle incomplete



class ServerTimeoutError(asyncio.TimeoutError, ServerConnectionError):
    '''Server timeout error.'''
    pass


class ConnectionTimeoutError(ServerTimeoutError):
    '''Connection timeout error.'''
    pass


class SocketTimeoutError(ServerTimeoutError):
    '''Socket timeout error.'''
    pass


class ServerFingerprintMismatch(ServerConnectionError):
    '''SSL certificate does not match expected fingerprint.'''
    
    def __init__(self, expected = None, got = None, host = None, port = ('expected', bytes, 'got', bytes, 'host', str, 'port', int, 'return', None)):
        self.expected = expected
        self.got = got
        self.host = host
        self.port = port
        self.args = (expected, got, host, port)

    
    def __repr__(self = None):
        return '<{} expected={!r} got={!r} host={!r} port={!r}>'.format(self.__class__.__name__, self.expected, self.got, self.host, self.port)



class ClientPayloadError(ClientError):
    '''Response payload error.'''
    pass


class InvalidURL(ValueError, ClientError):
    pass
# WARNING: Decompyle incomplete


class InvalidUrlClientError(InvalidURL):
    '''Invalid URL client error.'''
    pass


class RedirectClientError(ClientError):
    '''Client redirect error.'''
    pass


class NonHttpUrlClientError(ClientError):
    '''Non http URL client error.'''
    pass


class InvalidUrlRedirectClientError(RedirectClientError, InvalidUrlClientError):
    '''Invalid URL redirect client error.'''
    pass


class NonHttpUrlRedirectClientError(RedirectClientError, NonHttpUrlClientError):
    '''Non http URL redirect client error.'''
    pass


class ClientSSLError(ClientConnectorError):
    '''Base error for ssl.*Errors.'''
    pass

# WARNING: Decompyle incomplete
