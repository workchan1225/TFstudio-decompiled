# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_middlewares.pyc (Python 3.11)

import re
from typing import TYPE_CHECKING, Tuple, Type, TypeVar
from typedefs import Handler, Middleware
from web_exceptions import HTTPMove, HTTPPermanentRedirect
from web_request import Request
from web_response import StreamResponse
from web_urldispatcher import SystemRoute
__all__ = ('middleware', 'normalize_path_middleware')
if TYPE_CHECKING:
    from web_app import Application
_Func = TypeVar('_Func')

async def _check_request_resolves(request = None, path = None):
    pass
# WARNING: Decompyle incomplete


def middleware(f = None):
    f.__middleware_version__ = 1
    return f


def normalize_path_middleware(*, append_slash, remove_slash, merge_slashes, redirect_class):
    '''Factory for producing a middleware that normalizes the path of a request.

    Normalizing means:
        - Add or remove a trailing slash to the path.
        - Double slashes are replaced by one.

    The middleware returns as soon as it finds a path that resolves
    correctly. The order if both merge and append/remove are enabled is
        1) merge slashes
        2) append/remove slash
        3) both merge slashes and append/remove slash.
    If the path resolves with at least one of those conditions, it will
    redirect to the new path.

    Only one of `append_slash` and `remove_slash` can be enabled. If both
    are `True` the factory will raise an assertion error

    If `append_slash` is `True` the middleware will append a slash when
    needed. If a resource is defined with trailing slash and the request
    comes without it, it will append it automatically.

    If `remove_slash` is `True`, `append_slash` must be `False`. When enabled
    the middleware will remove trailing slashes and redirect if the resource
    is defined

    If merge_slashes is True, merge multiple consecutive slashes in the
    path into one.
    '''
    pass
# WARNING: Decompyle incomplete


def _fix_request_current_app(app = None):
    pass
# WARNING: Decompyle incomplete
