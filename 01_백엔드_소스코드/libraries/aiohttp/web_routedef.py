# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_routedef.pyc (Python 3.11)

import abc
import os
from typing import TYPE_CHECKING, Any, Callable, Dict, Iterator, List, Optional, Sequence, Type, Union, overload
import attr
from  import hdrs
from abc import AbstractView
from typedefs import Handler, PathLike
if TYPE_CHECKING:
    from web_request import Request
    from web_response import StreamResponse
    from web_urldispatcher import AbstractRoute, UrlDispatcher
else:
    Request = None
    StreamResponse = None
    UrlDispatcher = None
    AbstractRoute = None
__all__ = ('AbstractRouteDef', 'RouteDef', 'StaticDef', 'RouteTableDef', 'head', 'options', 'get', 'post', 'patch', 'put', 'delete', 'route', 'view', 'static')

class AbstractRouteDef(abc.ABC):
    register = (lambda self = None, router = None: pass)()

_HandlerType = Union[(Type[AbstractView], Handler)]
RouteDef = <NODE:12>()
StaticDef = <NODE:12>()

def route(method = None, path = attr.s(auto_attribs = True, frozen = True, repr = False, slots = True), handler = attr.s(auto_attribs = True, frozen = True, repr = False, slots = True), **kwargs):
    return RouteDef(method, path, handler, kwargs)


def head(path = None, handler = None, **kwargs):
    pass
# WARNING: Decompyle incomplete


def options(path = None, handler = None, **kwargs):
    pass
# WARNING: Decompyle incomplete


def get(path = None, handler = None, *, name, allow_head, **kwargs):
    pass
# WARNING: Decompyle incomplete


def post(path = None, handler = None, **kwargs):
    pass
# WARNING: Decompyle incomplete


def put(path = None, handler = None, **kwargs):
    pass
# WARNING: Decompyle incomplete


def patch(path = None, handler = None, **kwargs):
    pass
# WARNING: Decompyle incomplete


def delete(path = None, handler = None, **kwargs):
    pass
# WARNING: Decompyle incomplete


def view(path = None, handler = None, **kwargs):
    pass
# WARNING: Decompyle incomplete


def static(prefix = None, path = None, **kwargs):
    return StaticDef(prefix, path, kwargs)

_Deco = Callable[([
    _HandlerType], _HandlerType)]

def RouteTableDef():
    '''RouteTableDef'''
    __doc__ = 'Route definition table'
    
    def __init__(self = None):
        self._items = []

    
    def __repr__(self = None):
        return f'''<RouteTableDef count={len(self._items)}>'''

    __getitem__ = (lambda self = None, index = None: pass)()
    __getitem__ = (lambda self = None, index = None: pass)()
    
    def __getitem__(self, index):
        return self._items[index]

    
    def __iter__(self = None):
        return iter(self._items)

    
    def __len__(self = None):
        return len(self._items)

    
    def __contains__(self = None, item = None):
        return item in self._items

    
    def route(self = None, method = None, path = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def head(self = None, path = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def get(self = None, path = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def post(self = None, path = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def put(self = None, path = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def patch(self = None, path = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def delete(self = None, path = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def options(self = None, path = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def view(self = None, path = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def static(self = None, prefix = None, path = None, **kwargs):
        self._items.append(StaticDef(prefix, path, kwargs))


RouteTableDef = <NODE:27>(RouteTableDef, 'RouteTableDef', Sequence[AbstractRouteDef])
