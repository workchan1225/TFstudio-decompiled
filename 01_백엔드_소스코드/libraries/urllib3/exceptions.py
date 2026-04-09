# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

from __future__ import annotations
import socket
import typing
import warnings
from email.errors import MessageDefect
from http.client import IncompleteRead as httplib_IncompleteRead
if typing.TYPE_CHECKING:
    from connection import HTTPConnection
    from connectionpool import ConnectionPool
    from response import HTTPResponse
    from util.retry import Retry

class HTTPError(Exception):
    '''Base exception used by this module.'''
    pass


class HTTPWarning(Warning):
    '''Base warning used by this module.'''
    pass

_TYPE_REDUCE_RESULT = tuple[(typing.Callable[(..., object)], tuple[(object, ...)])]

class PoolError(HTTPError):
    pass
# WARNING: Decompyle incomplete


class RequestError(PoolError):
    pass
# WARNING: Decompyle incomplete


class SSLError(HTTPError):
    '''Raised when SSL certificate fails in an HTTPS connection.'''
    pass


class ProxyError(HTTPError):
    pass
# WARNING: Decompyle incomplete


class DecodeError(HTTPError):
    '''Raised when automatic decoding based on Content-Type fails.'''
    pass


class ProtocolError(HTTPError):
    '''Raised when something unexpected happens mid-request/response.'''
    pass

ConnectionError = ProtocolError

class MaxRetryError(RequestError):
    pass
# WARNING: Decompyle incomplete


class HostChangedError(RequestError):
    pass
# WARNING: Decompyle incomplete


class TimeoutStateError(HTTPError):
    '''Raised when passing an invalid state to a timeout'''
    pass


class TimeoutError(HTTPError):
    '''Raised when a socket timeout error occurs.

    Catching this error will catch both :exc:`ReadTimeoutErrors
    <ReadTimeoutError>` and :exc:`ConnectTimeoutErrors <ConnectTimeoutError>`.
    '''
    pass


class ReadTimeoutError(RequestError, TimeoutError):
    '''Raised when a socket timeout occurs while receiving data from a server'''
    pass


class ConnectTimeoutError(TimeoutError):
    '''Raised when a socket timeout occurs while connecting to a server'''
    pass


class NewConnectionError(HTTPError, ConnectTimeoutError):
    pass
# WARNING: Decompyle incomplete


class NameResolutionError(NewConnectionError):
    pass
# WARNING: Decompyle incomplete


class EmptyPoolError(PoolError):
    '''Raised when a pool runs out of connections and no more are allowed.'''
    pass


class FullPoolError(PoolError):
    '''Raised when we try to add a connection to a full pool in blocking mode.'''
    pass


class ClosedPoolError(PoolError):
    '''Raised when a request enters a pool after the pool has been closed.'''
    pass


class LocationValueError(HTTPError, ValueError):
    '''Raised when there is something wrong with a given URL input.'''
    pass


class LocationParseError(LocationValueError):
    pass
# WARNING: Decompyle incomplete


class URLSchemeUnknown(LocationValueError):
    pass
# WARNING: Decompyle incomplete


class ResponseError(HTTPError):
    '''Used as a container for an error reason supplied in a MaxRetryError.'''
    GENERIC_ERROR = 'too many error responses'
    SPECIFIC_ERROR = 'too many {status_code} error responses'


class SecurityWarning(HTTPWarning):
    '''Warned when performing security reducing actions'''
    pass


class InsecureRequestWarning(SecurityWarning):
    '''Warned when making an unverified HTTPS request.'''
    pass


class NotOpenSSLWarning(SecurityWarning):
    '''Warned when using unsupported SSL library'''
    pass


class SystemTimeWarning(SecurityWarning):
    '''Warned when system time is suspected to be wrong'''
    pass


class InsecurePlatformWarning(SecurityWarning):
    '''Warned when certain TLS/SSL configuration is not available on a platform.'''
    pass


class DependencyWarning(HTTPWarning):
    '''
    Warned when an attempt is made to import a module with missing optional
    dependencies.
    '''
    pass


class ResponseNotChunked(ValueError, ProtocolError):
    '''Response needs to be chunked in order to read it as chunks.'''
    pass


class BodyNotHttplibCompatible(HTTPError):
    '''
    Body should be :class:`http.client.HTTPResponse` like
    (have an fp attribute which returns raw chunks) for read_chunked().
    '''
    pass


class IncompleteRead(httplib_IncompleteRead, HTTPError):
    expected: 'int' = "\n    Response length doesn't match expected Content-Length\n\n    Subclass of :class:`http.client.IncompleteRead` to allow int value\n    for ``partial`` to avoid creating large objects on streamed reads.\n    "
    
    def __init__(self = None, partial = None, expected = None):
        self.partial = partial
        self.expected = expected

    
    def __repr__(self = None):
        return 'IncompleteRead(%i bytes read, %i more expected)' % (self.partial, self.expected)



class InvalidChunkLength(httplib_IncompleteRead, HTTPError):
    '''Invalid chunk length in a chunked response.'''
    
    def __init__(self = None, response = None, length = None):
        self.partial = response.tell()
        self.expected = response.length_remaining
        self.response = response
        self.length = length

    
    def __repr__(self = None):
        return 'InvalidChunkLength(got length %r, %i bytes read)' % (self.length, self.partial)



class InvalidHeader(HTTPError):
    '''The header provided was somehow invalid.'''
    pass


class ProxySchemeUnknown(URLSchemeUnknown, AssertionError):
    pass
# WARNING: Decompyle incomplete


class ProxySchemeUnsupported(ValueError):
    '''Fetching HTTPS resources through HTTPS proxies is unsupported'''
    pass


class HeaderParsingError(HTTPError):
    pass
# WARNING: Decompyle incomplete


class UnrewindableBodyError(HTTPError):
    '''urllib3 encountered an error when trying to rewind a body'''
    pass
