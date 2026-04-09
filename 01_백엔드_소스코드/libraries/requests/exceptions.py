# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

"""
requests.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of Requests' exceptions.
"""
from urllib3.exceptions import HTTPError as BaseHTTPError
from compat import JSONDecodeError as CompatJSONDecodeError

class RequestException(IOError):
    pass
# WARNING: Decompyle incomplete


class InvalidJSONError(RequestException):
    '''A JSON error occurred.'''
    pass


class JSONDecodeError(CompatJSONDecodeError, InvalidJSONError):
    """Couldn't decode the text into json"""
    
    def __init__(self, *args, **kwargs):
        """
        Construct the JSONDecodeError instance first with all
        args. Then use it's args to construct the IOError so that
        the json specific args aren't used as IOError specific args
        and the error message from JSONDecodeError is preserved.
        """
        pass
    # WARNING: Decompyle incomplete



class HTTPError(RequestException):
    '''An HTTP error occurred.'''
    pass


class ConnectionError(RequestException):
    '''A Connection error occurred.'''
    pass


class ProxyError(ConnectionError):
    '''A proxy error occurred.'''
    pass


class SSLError(ConnectionError):
    '''An SSL error occurred.'''
    pass


class Timeout(RequestException):
    '''The request timed out.

    Catching this error will catch both
    :exc:`~requests.exceptions.ConnectTimeout` and
    :exc:`~requests.exceptions.ReadTimeout` errors.
    '''
    pass


class ConnectTimeout(Timeout, ConnectionError):
    '''The request timed out while trying to connect to the remote server.

    Requests that produced this error are safe to retry.
    '''
    pass


class ReadTimeout(Timeout):
    '''The server did not send any data in the allotted amount of time.'''
    pass


class URLRequired(RequestException):
    '''A valid URL is required to make a request.'''
    pass


class TooManyRedirects(RequestException):
    '''Too many redirects.'''
    pass


class MissingSchema(ValueError, RequestException):
    '''The URL scheme (e.g. http or https) is missing.'''
    pass


class InvalidSchema(ValueError, RequestException):
    '''The URL scheme provided is either invalid or unsupported.'''
    pass


class InvalidURL(ValueError, RequestException):
    '''The URL provided was somehow invalid.'''
    pass


class InvalidHeader(ValueError, RequestException):
    '''The header value provided was somehow invalid.'''
    pass


class InvalidProxyURL(InvalidURL):
    '''The proxy URL provided is invalid.'''
    pass


class ChunkedEncodingError(RequestException):
    '''The server declared chunked encoding but sent an invalid chunk.'''
    pass


class ContentDecodingError(BaseHTTPError, RequestException):
    '''Failed to decode response content.'''
    pass


class StreamConsumedError(TypeError, RequestException):
    '''The content for this response was already consumed.'''
    pass


class RetryError(RequestException):
    '''Custom retries logic failed'''
    pass


class UnrewindableBodyError(RequestException):
    '''Requests encountered an error when trying to rewind a body.'''
    pass


class RequestsWarning(Warning):
    '''Base warning for Requests.'''
    pass


class FileModeWarning(DeprecationWarning, RequestsWarning):
    '''A file was opened in text mode, but Requests determined its binary length.'''
    pass


class RequestsDependencyWarning(RequestsWarning):
    """An imported dependency doesn't match the expected version range."""
    pass
