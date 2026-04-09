# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: requests.pyc (Python 3.11)

'''Transport adapter for Requests.'''
from __future__ import absolute_import
import functools
import logging
import numbers
import os
import time

try:
    import requests
except ImportError:
    caught_exc = None
    raise ImportError('The requests library is not installed from please install the requests package to use the requests transport.'), caught_exc
    caught_exc = None
    del caught_exc

import requests.adapters as requests
import requests.exceptions as requests
from requests.packages.urllib3.util.ssl_ import create_urllib3_context
from google.auth import _helpers
from google.auth import environment_vars
from google.auth import exceptions
from google.auth import transport
import google.auth.transport._mtls_helper as google
from google.oauth2 import service_account
_LOGGER = logging.getLogger(__name__)
_DEFAULT_TIMEOUT = 120

class _Response(transport.Response):
    '''Requests transport response adapter.

    Args:
        response (requests.Response): The raw Requests response.
    '''
    
    def __init__(self, response):
        self._response = response

    status = (lambda self: self._response.status_code)()
    headers = (lambda self: self._response.headers)()
    data = (lambda self: self._response.content)()


class TimeoutGuard(object):
    '''A context manager raising an error if the suite execution took too long.

    Args:
        timeout (Union[None, Union[float, Tuple[float, float]]]):
            The maximum number of seconds a suite can run without the context
            manager raising a timeout exception on exit. If passed as a tuple,
            the smaller of the values is taken as a timeout. If ``None``, a
            timeout error is never raised.
        timeout_error_type (Optional[Exception]):
            The type of the error to raise on timeout. Defaults to
            :class:`requests.exceptions.Timeout`.
    '''
    
    def __init__(self, timeout, timeout_error_type = (requests.exceptions.Timeout,)):
        self._timeout = timeout
        self.remaining_timeout = timeout
        self._timeout_error_type = timeout_error_type

    
    def __enter__(self):
        self._start = time.time()
        return self

    
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    # WARNING: Decompyle incomplete



class Request(transport.Request):
    '''Requests request adapter.

    This class is used internally for making requests using various transports
    in a consistent way. If you use :class:`AuthorizedSession` you do not need
    to construct or use this class directly.

    This class can be useful if you want to manually refresh a
    :class:`~google.auth.credentials.Credentials` instance::

        import google.auth.transport.requests
        import requests

        request = google.auth.transport.requests.Request()

        credentials.refresh(request)

    Args:
        session (requests.Session): An instance :class:`requests.Session` used
            to make HTTP requests. If not specified, a session will be created.

    .. automethod:: __call__
    '''
    
    def __init__(self, session = (None,)):
        if not session:
            session = requests.Session()
        self.session = session

    
    def __del__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self, url, method, body, headers, timeout = ('GET', None, None, _DEFAULT_TIMEOUT), **kwargs):
        """Make an HTTP request using requests.

        Args:
            url (str): The URI to be requested.
            method (str): The HTTP method to use for the request. Defaults
                to 'GET'.
            body (bytes): The payload or body in HTTP request.
            headers (Mapping[str, str]): Request headers.
            timeout (Optional[int]): The number of seconds to wait for a
                response from the server. If not specified or if None, the
                requests default timeout will be used.
            kwargs: Additional arguments passed through to the underlying
                requests :meth:`~requests.Session.request` method.

        Returns:
            google.auth.transport.Response: The HTTP response.

        Raises:
            google.auth.exceptions.TransportError: If any exception occurred.
        """
        pass
    # WARNING: Decompyle incomplete



class _MutualTlsAdapter(requests.adapters.HTTPAdapter):
    pass
# WARNING: Decompyle incomplete


class _MutualTlsOffloadAdapter(requests.adapters.HTTPAdapter):
    pass
# WARNING: Decompyle incomplete


class AuthorizedSession(requests.Session):
    pass
# WARNING: Decompyle incomplete
