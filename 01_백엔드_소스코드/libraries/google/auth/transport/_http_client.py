# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _http_client.pyc (Python 3.11)

'''Transport adapter for http.client, for internal use only.'''
from http.client import client as http_client
import logging
import socket
import urllib
from google.auth import _helpers
from google.auth import exceptions
from google.auth import transport
_LOGGER = logging.getLogger(__name__)

class Response(transport.Response):
    '''http.client transport response adapter.

    Args:
        response (http.client.HTTPResponse): The raw http client response.
    '''
    
    def __init__(self, response):
        self._status = response.status
        self._headers = response.getheaders()()
        self._data = response.read()

    status = (lambda self: self._status)()
    headers = (lambda self: self._headers)()
    data = (lambda self: self._data)()


class Request(transport.Request):
    '''http.client transport request adapter.'''
    
    def __call__(self, url, method, body, headers, timeout = ('GET', None, None, None), **kwargs):
        """Make an HTTP request using http.client.

        Args:
            url (str): The URI to be requested.
            method (str): The HTTP method to use for the request. Defaults
                to 'GET'.
            body (bytes): The payload / body in HTTP request.
            headers (Mapping): Request headers.
            timeout (Optional(int)): The number of seconds to wait for a
                response from the server. If not specified or if None, the
                socket global default timeout will be used.
            kwargs: Additional arguments passed throught to the underlying
                :meth:`~http.client.HTTPConnection.request` method.

        Returns:
            Response: The HTTP response.

        Raises:
            google.auth.exceptions.TransportError: If any exception occurred.
        """
        pass
    # WARNING: Decompyle incomplete
