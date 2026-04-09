# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: aiohttp.pyc (Python 3.11)

'''Transport adapter for Asynchronous HTTP Requests based on aiohttp.
'''
import asyncio
import logging
from typing import AsyncGenerator, Mapping, Optional

try:
    import aiohttp
except ImportError:
    caught_exc = None
    raise ImportError('The aiohttp library is not installed from please install the aiohttp package to use the aiohttp transport.'), caught_exc
    caught_exc = None
    del caught_exc

from google.auth import _helpers
from google.auth import exceptions
from google.auth.aio import _helpers as _helpers_async
from google.auth.aio import transport
_LOGGER = logging.getLogger(__name__)

class Response(transport.Response):
    '''
    Represents an HTTP response and its data. It is returned by ``google.auth.aio.transport.sessions.AsyncAuthorizedSession``.

    Args:
        response (aiohttp.ClientResponse): An instance of aiohttp.ClientResponse.

    Attributes:
        status_code (int): The HTTP status code of the response.
        headers (Mapping[str, str]): The HTTP headers of the response.
    '''
    
    def __init__(self = None, response = None):
        self._response = response

    status_code = (lambda self = None: self._response.status)()()
    headers = (lambda self = None: self._response.headers.items()())()()
    content = (lambda self = None, chunk_size = None: pass# WARNING: Decompyle incomplete
)()
    read = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    close = (lambda self: pass# WARNING: Decompyle incomplete
)()


class Request(transport.Request):
    '''Asynchronous Requests request adapter.

    This class is used internally for making requests using aiohttp
    in a consistent way. If you use :class:`google.auth.aio.transport.sessions.AsyncAuthorizedSession`
    you do not need to construct or use this class directly.

    This class can be useful if you want to configure a Request callable
    with a custom ``aiohttp.ClientSession`` in :class:`AuthorizedSession` or if
    you want to manually refresh a :class:`~google.auth.aio.credentials.Credentials` instance::

        import aiohttp
        import google.auth.aio.transport.aiohttp

        # Default example:
        request = google.auth.aio.transport.aiohttp.Request()
        await credentials.refresh(request)

        # Custom aiohttp Session Example:
        session = session=aiohttp.ClientSession(auto_decompress=False)
        request = google.auth.aio.transport.aiohttp.Request(session=session)
        auth_sesion = google.auth.aio.transport.sessions.AsyncAuthorizedSession(auth_request=request)

    Args:
        session (aiohttp.ClientSession): An instance :class:`aiohttp.ClientSession` used
            to make HTTP requests. If not specified, a session will be created.

    .. automethod:: __call__
    '''
    
    def __init__(self = None, session = None):
        self._session = session
        self._closed = False

    
    async def __call__(self, url = None, method = None, body = None, headers = ('GET', None, None, transport._DEFAULT_TIMEOUT_SECONDS), timeout = ('url', str, 'method', str, 'body', Optional[bytes], 'headers', Optional[Mapping[(str, str)]], 'timeout', float, 'return', transport.Response), **kwargs):
        """
        Make an HTTP request using aiohttp.

        Args:
            url (str): The URL to be requested.
            method (Optional[str]):
                The HTTP method to use for the request. Defaults to 'GET'.
            body (Optional[bytes]):
                The payload or body in HTTP request.
            headers (Optional[Mapping[str, str]]):
                Request headers.
            timeout (float): The number of seconds to wait for a
                response from the server. If not specified or if None, the
                requests default timeout will be used.
            kwargs: Additional arguments passed through to the underlying
                aiohttp :meth:`aiohttp.Session.request` method.

        Returns:
            google.auth.aio.transport.Response: The HTTP response.

        Raises:
            - google.auth.exceptions.TransportError: If the request fails or if the session is closed.
            - google.auth.exceptions.TimeoutError: If the request times out.
        """
        pass
    # WARNING: Decompyle incomplete

    
    async def close(self = None):
        '''
        Close the underlying aiohttp session to release the acquired resources.
        '''
        pass
    # WARNING: Decompyle incomplete
