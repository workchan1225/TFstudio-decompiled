# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sessions.pyc (Python 3.11)

import asyncio
from contextlib import asynccontextmanager
import functools
import time
from typing import Mapping, Optional
from google.auth import _exponential_backoff, exceptions
from google.auth.aio import transport
from google.auth.aio.credentials import Credentials
from google.auth.exceptions import TimeoutError

try:
    from google.auth.aio.transport.aiohttp import Request as AiohttpRequest
    AIOHTTP_INSTALLED = True
except ImportError:
    AIOHTTP_INSTALLED = False

timeout_guard = (lambda timeout: pass# WARNING: Decompyle incomplete
)()

class AsyncAuthorizedSession:
    """This is an asynchronous implementation of :class:`google.auth.requests.AuthorizedSession` class.
    We utilize an instance of a class that implements :class:`google.auth.aio.transport.Request` configured
    by the caller or otherwise default to `google.auth.aio.transport.aiohttp.Request` if the external aiohttp
    package is installed.

    A Requests Session class with credentials.

    This class is used to perform asynchronous requests to API endpoints that require
    authorization::

        import aiohttp
        from google.auth.aio.transport import sessions

        async with sessions.AsyncAuthorizedSession(credentials) as authed_session:
            response = await authed_session.request(
                'GET', 'https://www.googleapis.com/storage/v1/b')

    The underlying :meth:`request` implementation handles adding the
    credentials' headers to the request and refreshing credentials as needed.

    Args:
        credentials (google.auth.aio.credentials.Credentials):
            The credentials to add to the request.
        auth_request (Optional[google.auth.aio.transport.Request]):
            An instance of a class that implements
            :class:`~google.auth.aio.transport.Request` used to make requests
            and refresh credentials. If not passed,
            an instance of :class:`~google.auth.aio.transport.aiohttp.Request`
            is created.

    Raises:
        - google.auth.exceptions.TransportError: If `auth_request` is `None`
            and the external package `aiohttp` is not installed.
        - google.auth.exceptions.InvalidType: If the provided credentials are
            not of type `google.auth.aio.credentials.Credentials`.
    """
    
    def __init__(self = None, credentials = None, auth_request = None):
        if not isinstance(credentials, Credentials):
            raise exceptions.InvalidType(f'''The configured credentials of type {type(credentials)} are invalid and must be of type `google.auth.aio.credentials.Credentials`''')
        self._credentials = credentials
        _auth_request = auth_request
        if _auth_request and AIOHTTP_INSTALLED:
            _auth_request = AiohttpRequest()
    # WARNING: Decompyle incomplete

    
    async def request(self, method, url = None, data = None, headers = None, max_allowed_time = (None, None, transport._DEFAULT_TIMEOUT_SECONDS, transport._DEFAULT_TIMEOUT_SECONDS), timeout = ('method', str, 'url', str, 'data', Optional[bytes], 'headers', Optional[Mapping[(str, str)]], 'max_allowed_time', float, 'timeout', float, 'return', transport.Response), **kwargs):
        '''
        Args:
                method (str): The http method used to make the request.
                url (str): The URI to be requested.
                data (Optional[bytes]): The payload or body in HTTP request.
                headers (Optional[Mapping[str, str]]): Request headers.
                timeout (float):
                The amount of time in seconds to wait for the server response
                with each individual request.
                max_allowed_time (float):
                If the method runs longer than this, a ``Timeout`` exception is
                automatically raised. Unlike the ``timeout`` parameter, this
                value applies to the total method execution time, even if
                multiple requests are made under the hood.

                Mind that it is not guaranteed that the timeout error is raised
                at ``max_allowed_time``. It might take longer, for example, if
                an underlying request takes a lot of time, but the request
                itself does not timeout, e.g. if a large file is being
                transmitted. The timout error will be raised after such
                request completes.

        Returns:
                google.auth.aio.transport.Response: The HTTP response.

        Raises:
                google.auth.exceptions.TimeoutError: If the method does not complete within
                the configured `max_allowed_time` or the request exceeds the configured
                `timeout`.
        '''
        pass
    # WARNING: Decompyle incomplete

    get = (lambda self, url = None, data = None, headers = functools.wraps(request), max_allowed_time = (None, None, transport._DEFAULT_TIMEOUT_SECONDS, transport._DEFAULT_TIMEOUT_SECONDS), timeout = ('url', str, 'data', Optional[bytes], 'headers', Optional[Mapping[(str, str)]], 'max_allowed_time', float, 'timeout', float, 'return', transport.Response): pass# WARNING: Decompyle incomplete
)()
    post = (lambda self, url = None, data = None, headers = functools.wraps(request), max_allowed_time = (None, None, transport._DEFAULT_TIMEOUT_SECONDS, transport._DEFAULT_TIMEOUT_SECONDS), timeout = ('url', str, 'data', Optional[bytes], 'headers', Optional[Mapping[(str, str)]], 'max_allowed_time', float, 'timeout', float, 'return', transport.Response): pass# WARNING: Decompyle incomplete
)()
    put = (lambda self, url = None, data = None, headers = functools.wraps(request), max_allowed_time = (None, None, transport._DEFAULT_TIMEOUT_SECONDS, transport._DEFAULT_TIMEOUT_SECONDS), timeout = ('url', str, 'data', Optional[bytes], 'headers', Optional[Mapping[(str, str)]], 'max_allowed_time', float, 'timeout', float, 'return', transport.Response): pass# WARNING: Decompyle incomplete
)()
    patch = (lambda self, url = None, data = None, headers = functools.wraps(request), max_allowed_time = (None, None, transport._DEFAULT_TIMEOUT_SECONDS, transport._DEFAULT_TIMEOUT_SECONDS), timeout = ('url', str, 'data', Optional[bytes], 'headers', Optional[Mapping[(str, str)]], 'max_allowed_time', float, 'timeout', float, 'return', transport.Response): pass# WARNING: Decompyle incomplete
)()
    delete = (lambda self, url = None, data = None, headers = functools.wraps(request), max_allowed_time = (None, None, transport._DEFAULT_TIMEOUT_SECONDS, transport._DEFAULT_TIMEOUT_SECONDS), timeout = ('url', str, 'data', Optional[bytes], 'headers', Optional[Mapping[(str, str)]], 'max_allowed_time', float, 'timeout', float, 'return', transport.Response): pass# WARNING: Decompyle incomplete
)()
    
    async def close(self = None):
        '''
        Close the underlying auth request session.
        '''
        pass
    # WARNING: Decompyle incomplete
