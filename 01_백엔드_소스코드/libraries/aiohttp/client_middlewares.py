# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client_middlewares.pyc (Python 3.11)

'''Client middleware support.'''
from collections.abc import Awaitable, Callable, Sequence
from client_reqrep import ClientRequest, ClientResponse
__all__ = ('ClientMiddlewareType', 'ClientHandlerType', 'build_client_middlewares')
ClientHandlerType = Callable[([
    ClientRequest], Awaitable[ClientResponse])]
ClientMiddlewareType = Callable[([
    ClientRequest,
    ClientHandlerType], Awaitable[ClientResponse])]

def build_client_middlewares(handler = None, middlewares = None):
    """
    Apply middlewares to request handler.

    The middlewares are applied in reverse order, so the first middleware
    in the list wraps all subsequent middlewares and the handler.

    This implementation avoids using partial/update_wrapper to minimize overhead
    and doesn't cache to avoid holding references to stateful middleware.
    """
    pass
# WARNING: Decompyle incomplete
