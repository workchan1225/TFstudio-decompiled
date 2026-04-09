# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: google_auth_httplib2.pyc (Python 3.11)

'''Transport adapter for httplib2.'''
from __future__ import absolute_import
import http.client as http
import logging
from google.auth import exceptions
from google.auth import transport
import httplib2
_LOGGER = logging.getLogger(__name__)
_STREAM_PROPERTIES = ('read', 'seek', 'tell')

class _Response(transport.Response):
    '''httplib2 transport response adapter.

    Args:
        response (httplib2.Response): The raw httplib2 response.
        data (bytes): The response body.
    '''
    
    def __init__(self, response, data):
        self._response = response
        self._data = data

    status = (lambda self: self._response.status)()
    headers = (lambda self: dict(self._response))()
    data = (lambda self: self._data)()


class Request(transport.Request):
    '''httplib2 request adapter.

    This class is used internally for making requests using various transports
    in a consistent way. If you use :class:`AuthorizedHttp` you do not need
    to construct or use this class directly.

    This class can be useful if you want to manually refresh a
    :class:`~google.auth.credentials.Credentials` instance::

        import google_auth_httplib2
        import httplib2

        http = httplib2.Http()
        request = google_auth_httplib2.Request(http)

        credentials.refresh(request)

    Args:
        http (httplib2.Http): The underlying http object to use to make
            requests.
    '''
    
    def __init__(self, http):
        self.http = http

    
    def __call__(self, url, method, body, headers, timeout = ('GET', None, None, None), **kwargs):
        """Make an HTTP request using httplib2.

        Args:
            url (str): The URI to be requested.
            method (str): The HTTP method to use for the request. Defaults
                to 'GET'.
            body (bytes): The payload / body in HTTP request.
            headers (Mapping[str, str]): Request headers.
            timeout (Optional[int]): The number of seconds to wait for a
                response from the server. This is ignored by httplib2 and will
                issue a warning.
            kwargs: Additional arguments passed throught to the underlying
                :meth:`httplib2.Http.request` method.

        Returns:
            google.auth.transport.Response: The HTTP response.

        Raises:
            google.auth.exceptions.TransportError: If any exception occurred.
        """
        pass
    # WARNING: Decompyle incomplete



def _make_default_http():
    '''Returns a default httplib2.Http instance.'''
    return httplib2.Http()


class AuthorizedHttp(object):
    """A httplib2 HTTP class with credentials.

    This class is used to perform requests to API endpoints that require
    authorization::

        from google.auth.transport._httplib2 import AuthorizedHttp

        authed_http = AuthorizedHttp(credentials)

        response = authed_http.request(
            'https://www.googleapis.com/storage/v1/b')

    This class implements :meth:`request` in the same way as
    :class:`httplib2.Http` and can usually be used just like any other
    instance of :class:`httplib2.Http`.

    The underlying :meth:`request` implementation handles adding the
    credentials' headers to the request and refreshing credentials as needed.
    """
    
    def __init__(self, credentials, http, refresh_status_codes, max_refresh_attempts = (None, transport.DEFAULT_REFRESH_STATUS_CODES, transport.DEFAULT_MAX_REFRESH_ATTEMPTS)):
        '''
        Args:
            credentials (google.auth.credentials.Credentials): The credentials
                to add to the request.
            http (httplib2.Http): The underlying HTTP object to
                use to make requests. If not specified, a
                :class:`httplib2.Http` instance will be constructed.
            refresh_status_codes (Sequence[int]): Which HTTP status codes
                indicate that credentials should be refreshed and the request
                should be retried.
            max_refresh_attempts (int): The maximum number of times to attempt
                to refresh the credentials and retry the request.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def close(self):
        """Calls httplib2's Http.close"""
        self.http.close()

    
    def request(self, uri, method, body, headers, redirections, connection_type = ('GET', None, None, httplib2.DEFAULT_MAX_REDIRECTS, None), **kwargs):
        """Implementation of httplib2's Http.request."""
        pass
    # WARNING: Decompyle incomplete

    
    def add_certificate(self, key, cert, domain, password = (None,)):
        '''Proxy to httplib2.Http.add_certificate.'''
        self.http.add_certificate(key, cert, domain, password = password)

    connections = (lambda self: self.http.connections)()
    connections = (lambda self, value: self.http.connections = value)()
    follow_redirects = (lambda self: self.http.follow_redirects)()
    follow_redirects = (lambda self, value: self.http.follow_redirects = value)()
    timeout = (lambda self: self.http.timeout)()
    timeout = (lambda self, value: self.http.timeout = value)()
    redirect_codes = (lambda self: self.http.redirect_codes)()
    redirect_codes = (lambda self, value: self.http.redirect_codes = value)()
