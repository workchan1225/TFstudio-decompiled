# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: asgi.pyc (Python 3.11)

from __future__ import annotations
import typing
from _models import Request, Response
from _types import AsyncByteStream
from base import AsyncBaseTransport
if typing.TYPE_CHECKING:
    import asyncio
    import trio
    Event = typing.Union[(asyncio.Event, trio.Event)]
_Message = typing.MutableMapping[(str, typing.Any)]
_Receive = typing.Callable[([], typing.Awaitable[_Message])]
_Send = typing.Callable[([
    typing.MutableMapping[(str, typing.Any)]], typing.Awaitable[None])]
_ASGIApp = typing.Callable[([
    typing.MutableMapping[(str, typing.Any)],
    _Receive,
    _Send], typing.Awaitable[None])]
__all__ = [
    'ASGITransport']

def is_running_trio():
    
    try:
        import sniffio
        if sniffio.current_async_library() == 'trio':
            return True
    except ImportError:
        pass

    return False


def create_event():
    if is_running_trio():
        import trio
        return trio.Event()
    import asyncio
    return asyncio.Event()


class ASGIResponseStream(AsyncByteStream):
    
    def __init__(self = None, body = None):
        self._body = body

    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete



class ASGITransport(AsyncBaseTransport):
    '''
    A custom AsyncTransport that handles sending requests directly to an ASGI app.

    ```python
    transport = httpx.ASGITransport(
        app=app,
        root_path="/submount",
        client=("1.2.3.4", 123)
    )
    client = httpx.AsyncClient(transport=transport)
    ```

    Arguments:

    * `app` - The ASGI application.
    * `raise_app_exceptions` - Boolean indicating if exceptions in the application
       should be raised. Default to `True`. Can be set to `False` for use cases
       such as testing the content of a client 500 response.
    * `root_path` - The root path on which the ASGI application should be mounted.
    * `client` - A two-tuple indicating the client IP and port of incoming requests.
    ```
    '''
    
    def __init__(self = None, app = None, raise_app_exceptions = None, root_path = (True, '', ('127.0.0.1', 123)), client = ('app', '_ASGIApp', 'raise_app_exceptions', 'bool', 'root_path', 'str', 'client', 'tuple[str, int]', 'return', 'None')):
        self.app = app
        self.raise_app_exceptions = raise_app_exceptions
        self.root_path = root_path
        self.client = client

    
    async def handle_async_request(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete
