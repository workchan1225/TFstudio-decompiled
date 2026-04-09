# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: interfaces.pyc (Python 3.11)

from __future__ import annotations
import contextlib
import typing
from _models import URL, Extensions, HeaderTypes, Origin, Request, Response, enforce_bytes, enforce_headers, enforce_url, include_request_headers

class AsyncRequestInterface:
    
    async def request(self = None, method = None, url = None, *, headers, content, extensions):
        pass
    # WARNING: Decompyle incomplete

    stream = (lambda self = None, method = None, url = None, *, headers, content, extensions: pass# WARNING: Decompyle incomplete
)()
    
    async def handle_async_request(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete



class AsyncConnectionInterface(AsyncRequestInterface):
    
    async def aclose(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def info(self = None):
        raise NotImplementedError()

    
    def can_handle_request(self = None, origin = None):
        raise NotImplementedError()

    
    def is_available(self = None):
        '''
        Return `True` if the connection is currently able to accept an
        outgoing request.

        An HTTP/1.1 connection will only be available if it is currently idle.

        An HTTP/2 connection will be available so long as the stream ID space is
        not yet exhausted, and the connection is not in an error state.

        While the connection is being established we may not yet know if it is going
        to result in an HTTP/1.1 or HTTP/2 connection. The connection should be
        treated as being available, but might ultimately raise `NewConnectionRequired`
        required exceptions if multiple requests are attempted over a connection
        that ends up being established as HTTP/1.1.
        '''
        raise NotImplementedError()

    
    def has_expired(self = None):
        '''
        Return `True` if the connection is in a state where it should be closed.

        This either means that the connection is idle and it has passed the
        expiry time on its keep-alive, or that server has sent an EOF.
        '''
        raise NotImplementedError()

    
    def is_idle(self = None):
        '''
        Return `True` if the connection is currently idle.
        '''
        raise NotImplementedError()

    
    def is_closed(self = None):
        '''
        Return `True` if the connection has been closed.

        Used when a response is closed to determine if the connection may be
        returned to the connection pool or not.
        '''
        raise NotImplementedError()
