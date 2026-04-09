# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: wsgi.pyc (Python 3.11)

from __future__ import annotations
import io
import itertools
import sys
import typing
from _models import Request, Response
from _types import SyncByteStream
from base import BaseTransport
if typing.TYPE_CHECKING:
    from _typeshed import OptExcInfo
    from _typeshed.wsgi import WSGIApplication
_T = typing.TypeVar('_T')
__all__ = [
    'WSGITransport']

def _skip_leading_empty_chunks(body = None):
    body = iter(body)
    for chunk in body:
        if chunk:
            
            return None, itertools.chain([
                chunk], body)
        return []


class WSGIByteStream(SyncByteStream):
    
    def __init__(self = None, result = None):
        self._close = getattr(result, 'close', None)
        self._result = _skip_leading_empty_chunks(result)

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        pass
    # WARNING: Decompyle incomplete



class WSGITransport(BaseTransport):
    '''
    A custom transport that handles sending requests directly to an WSGI app.
    The simplest way to use this functionality is to use the `app` argument.

    ```
    client = httpx.Client(app=app)
    ```

    Alternatively, you can setup the transport instance explicitly.
    This allows you to include any additional configuration arguments specific
    to the WSGITransport class:

    ```
    transport = httpx.WSGITransport(
        app=app,
        script_name="/submount",
        remote_addr="1.2.3.4"
    )
    client = httpx.Client(transport=transport)
    ```

    Arguments:

    * `app` - The WSGI application.
    * `raise_app_exceptions` - Boolean indicating if exceptions in the application
       should be raised. Default to `True`. Can be set to `False` for use cases
       such as testing the content of a client 500 response.
    * `script_name` - The root path on which the WSGI application should be mounted.
    * `remote_addr` - A string indicating the client IP of incoming requests.
    ```
    '''
    
    def __init__(self, app = None, raise_app_exceptions = None, script_name = None, remote_addr = (True, '', '127.0.0.1', None), wsgi_errors = ('app', 'WSGIApplication', 'raise_app_exceptions', 'bool', 'script_name', 'str', 'remote_addr', 'str', 'wsgi_errors', 'typing.TextIO | None', 'return', 'None')):
        self.app = app
        self.raise_app_exceptions = raise_app_exceptions
        self.script_name = script_name
        self.remote_addr = remote_addr
        self.wsgi_errors = wsgi_errors

    
    def handle_request(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete
