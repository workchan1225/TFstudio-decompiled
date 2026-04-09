# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: router.pyc (Python 3.11)

from __future__ import annotations
import http
import ssl as ssl_module
import urllib.parse as urllib
from typing import Any, Awaitable, Callable, Literal
from werkzeug.exceptions import NotFound
from werkzeug.routing import Map, RequestRedirect
from http11 import Request, Response
from server import Server, ServerConnection, serve
__all__ = [
    'route',
    'unix_route',
    'Router']

class Router:
    '''WebSocket router supporting :func:`route`.'''
    
    def __init__(self = None, url_map = None, server_name = None, url_scheme = (None, 'ws')):
        self.url_map = url_map
        self.server_name = server_name
        self.url_scheme = url_scheme
        for rule in self.url_map.iter_rules():
            rule.websocket = True
            return None

    
    def get_server_name(self = None, connection = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    def redirect(self = None, connection = None, url = None):
        response = connection.respond(http.HTTPStatus.FOUND, f'''Found at {url}''')
        response.headers['Location'] = url
        return response

    
    def not_found(self = None, connection = None):
        return connection.respond(http.HTTPStatus.NOT_FOUND, 'Not Found')

    
    def route_request(self = None, connection = None, request = None):
        '''Route incoming request.'''
        url_map_adapter = self.url_map.bind(server_name = self.get_server_name(connection, request), url_scheme = self.url_scheme)
        
        try:
            parsed = urllib.parse.urlparse(request.path)
            (handler, kwargs) = url_map_adapter.match(path_info = parsed.path, query_args = parsed.query)
        except RequestRedirect:
            redirect = None
            del redirect
            return None
            None = 
            del redirect
            except NotFound:
                return 

        connection.handler, connection.handler_kwargs = handler, kwargs

    
    async def handler(self = None, connection = None):
        '''Handle a connection.'''
        pass
    # WARNING: Decompyle incomplete



def route(url_map = None, *, server_name, ssl, create_router, *args, **kwargs):
    '''
    Create a WebSocket server dispatching connections to different handlers.

    This feature requires the third-party library `werkzeug`_:

    .. code-block:: console

        $ pip install werkzeug

    .. _werkzeug: https://werkzeug.palletsprojects.com/

    :func:`route` accepts the same arguments as
    :func:`~websockets.sync.server.serve`, except as described below.

    The first argument is a :class:`werkzeug.routing.Map` that maps URL patterns
    to connection handlers. In addition to the connection, handlers receive
    parameters captured in the URL as keyword arguments.

    Here\'s an example::


        from websockets.asyncio.router import route
        from werkzeug.routing import Map, Rule

        async def channel_handler(websocket, channel_id):
            ...

        url_map = Map([
            Rule("/channel/<uuid:channel_id>", endpoint=channel_handler),
            ...
        ])

        # set this future to exit the server
        stop = asyncio.get_running_loop().create_future()

        async with route(url_map, ...) as server:
            await stop


    Refer to the documentation of :mod:`werkzeug.routing` for details.

    If you define redirects with ``Rule(..., redirect_to=...)`` in the URL map,
    when the server runs behind a reverse proxy that modifies the ``Host``
    header or terminates TLS, you need additional configuration:

    * Set ``server_name`` to the name of the server as seen by clients. When not
      provided, websockets uses the value of the ``Host`` header.

    * Set ``ssl=True`` to generate ``wss://`` URIs without actually enabling
      TLS. Under the hood, this bind the URL map with a ``url_scheme`` of
      ``wss://`` instead of ``ws://``.

    There is no need to specify ``websocket=True`` in each rule. It is added
    automatically.

    Args:
        url_map: Mapping of URL patterns to connection handlers.
        server_name: Name of the server as seen by clients. If :obj:`None`,
            websockets uses the value of the ``Host`` header.
        ssl: Configuration for enabling TLS on the connection. Set it to
            :obj:`True` if a reverse proxy terminates TLS connections.
        create_router: Factory for the :class:`Router` dispatching requests to
            handlers. Set it to a wrapper or a subclass to customize routing.

    '''
    pass
# WARNING: Decompyle incomplete


def unix_route(url_map = None, path = None, **kwargs):
    '''
    Create a WebSocket Unix server dispatching connections to different handlers.

    :func:`unix_route` combines the behaviors of :func:`route` and
    :func:`~websockets.asyncio.server.unix_serve`.

    Args:
        url_map: Mapping of URL patterns to connection handlers.
        path: File system path to the Unix socket.

    '''
    pass
# WARNING: Decompyle incomplete
