# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_urldispatcher.pyc (Python 3.11)

import abc
import asyncio
import base64
import functools
import hashlib
import html
import inspect
import keyword
import os
import re
import sys
import warnings
from functools import wraps
from pathlib import Path
from types import MappingProxyType
from typing import TYPE_CHECKING, Any, Awaitable, Callable, Container, Dict, Final, Generator, Iterable, Iterator, List, Mapping, NoReturn, Optional, Pattern, Set, Sized, Tuple, Type, TypedDict, Union, cast
from yarl import URL, __version__ as yarl_version
from  import hdrs
from abc import AbstractMatchInfo, AbstractRouter, AbstractView
from helpers import DEBUG
from http import HttpVersion11
from typedefs import Handler, PathLike
from web_exceptions import HTTPException, HTTPExpectationFailed, HTTPForbidden, HTTPMethodNotAllowed, HTTPNotFound
from web_fileresponse import FileResponse
from web_request import Request
from web_response import Response, StreamResponse
from web_routedef import AbstractRouteDef
__all__ = ('UrlDispatcher', 'UrlMappingMatchInfo', 'AbstractResource', 'Resource', 'PlainResource', 'DynamicResource', 'AbstractRoute', 'ResourceRoute', 'StaticResource', 'View')
if TYPE_CHECKING:
    from web_app import Application
    BaseDict = Dict[(str, str)]
else:
    BaseDict = dict
if sys.version_info < (3, 10) and sys.platform.startswith('win32'):
    pass
elif sys.version_info < (3, 13):
    pass

CIRCULAR_SYMLINK_ERROR = ()
YARL_VERSION: Final[Tuple[(int, ...)]] = tuple(map(int, yarl_version.split('.')[:2]))
HTTP_METHOD_RE: Final[Pattern[str]] = re.compile("^[0-9A-Za-z!#\\$%&'\\*\\+\\-\\.\\^_`\\|~]+$")
ROUTE_RE: Final[Pattern[str]] = re.compile('(\\{[_a-zA-Z][^{}]*(?:\\{[^{}]*\\}[^{}]*)*\\})')
PATH_SEP: Final[str] = re.escape('/')
_ExpectHandler = Callable[([
    Request], Awaitable[Optional[StreamResponse]])]
_Resolve = Tuple[(Optional['UrlMappingMatchInfo'], Set[str])]
html_escape = functools.partial(html.escape, quote = True)

def _InfoDict():
    '''_InfoDict'''
    http_exception: HTTPException = '_InfoDict'

_InfoDict = <NODE:27>(_InfoDict, '_InfoDict', TypedDict, total = False)

def AbstractResource():
    '''AbstractResource'''
    
    def __init__(self = None, *, name):
        self._name = name

    name = (lambda self = None: self._name)()
    canonical = (lambda self = None: pass)()()
    url_for = (lambda self = None: pass)()
    resolve = (lambda self = None, request = None: pass# WARNING: Decompyle incomplete
)()
    add_prefix = (lambda self = None, prefix = None: pass)()
    get_info = (lambda self = None: pass)()
    
    def freeze(self = None):
        pass

    raw_match = (lambda self = None, path = None: pass)()

AbstractResource = <NODE:27>(AbstractResource, 'AbstractResource', Sized, Iterable['AbstractRoute'])

class AbstractRoute(abc.ABC):
    
    def __init__(self = None, method = None, handler = None, *, expect_handler, resource):
        pass
    # WARNING: Decompyle incomplete

    method = (lambda self = None: self._method)()
    handler = (lambda self = None: self._handler)()
    name = (lambda self = None: pass)()()
    resource = (lambda self = None: self._resource)()
    get_info = (lambda self = None: pass)()
    url_for = (lambda self = None: pass)()
    
    async def handle_expect_header(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete



class UrlMappingMatchInfo(AbstractMatchInfo, BaseDict):
    pass
# WARNING: Decompyle incomplete


class MatchInfoError(UrlMappingMatchInfo):
    pass
# WARNING: Decompyle incomplete


async def _default_expect_handler(request = None):
    '''Default handler for Expect header.

    Just send "100 Continue" to client.
    raise HTTPExpectationFailed if value of header is not "100-continue"
    '''
    pass
# WARNING: Decompyle incomplete


class Resource(AbstractResource):
    pass
# WARNING: Decompyle incomplete


class PlainResource(Resource):
    pass
# WARNING: Decompyle incomplete


class DynamicResource(Resource):
    pass
# WARNING: Decompyle incomplete


class PrefixResource(AbstractResource):
    pass
# WARNING: Decompyle incomplete


class StaticResource(PrefixResource):
    pass
# WARNING: Decompyle incomplete


class PrefixedSubAppResource(PrefixResource):
    pass
# WARNING: Decompyle incomplete


class AbstractRuleMatching(abc.ABC):
    match = (lambda self = None, request = None: pass# WARNING: Decompyle incomplete
)()
    get_info = (lambda self = None: pass)()
    canonical = (lambda self = None: pass)()()


class Domain(AbstractRuleMatching):
    pass
# WARNING: Decompyle incomplete


class MaskDomain(Domain):
    pass
# WARNING: Decompyle incomplete


class MatchedSubAppResource(PrefixedSubAppResource):
    
    def __init__(self = None, rule = None, app = None):
        AbstractResource.__init__(self)
        self._prefix = ''
        self._app = app
        self._rule = rule

    canonical = (lambda self = None: self._rule.canonical)()
    
    def get_info(self = None):
        return {
            'app': self._app,
            'rule': self._rule }

    
    async def resolve(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''<MatchedSubAppResource -> {self._app!r}>'''



class ResourceRoute(AbstractRoute):
    pass
# WARNING: Decompyle incomplete


class SystemRoute(AbstractRoute):
    pass
# WARNING: Decompyle incomplete


class View(AbstractView):
    
    async def _iter(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __await__(self = None):
        return self._iter().__await__()

    
    def _raise_allowed_methods(self = None):
        pass
    # WARNING: Decompyle incomplete



def ResourcesView():
    '''ResourcesView'''
    
    def __init__(self = None, resources = None):
        self._resources = resources

    
    def __len__(self = None):
        return len(self._resources)

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __contains__(self = None, resource = None):
        return resource in self._resources


ResourcesView = <NODE:27>(ResourcesView, 'ResourcesView', Sized, Iterable[AbstractResource], Container[AbstractResource])

def RoutesView():
    '''RoutesView'''
    
    def __init__(self = None, resources = None):
        self._routes = []
        for resource in resources:
            for route in resource:
                self._routes.append(route)
                return None

    
    def __len__(self = None):
        return len(self._routes)

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __contains__(self = None, route = None):
        return route in self._routes


RoutesView = <NODE:27>(RoutesView, 'RoutesView', Sized, Iterable[AbstractRoute], Container[AbstractRoute])

def UrlDispatcher():
    '''UrlDispatcher'''
    pass
# WARNING: Decompyle incomplete

UrlDispatcher = <NODE:27>(UrlDispatcher, 'UrlDispatcher', AbstractRouter, Mapping[(str, AbstractResource)])

def _quote_path(value = None):
    if YARL_VERSION < (1, 6):
        value = value.replace('%', '%25')
    return URL.build(path = value, encoded = False).raw_path


def _unquote_path_safe(value = None):
    if '%' not in value:
        return value
    return None.replace('%2F', '/').replace('%25', '%')


def _requote_path(value = None):
    result = _quote_path(value)
    if '%' in value:
        result = result.replace('%25', '%')
    return result
