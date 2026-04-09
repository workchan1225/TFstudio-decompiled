# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_app.pyc (Python 3.11)

import asyncio
import logging
import warnings
from functools import lru_cache, partial, update_wrapper
from typing import TYPE_CHECKING, Any, AsyncIterator, Awaitable, Callable, Dict, Iterable, Iterator, List, Mapping, MutableMapping, Optional, Sequence, Tuple, Type, TypeVar, Union, cast, overload
from aiosignal import Signal
from frozenlist import FrozenList
from  import hdrs
from abc import AbstractAccessLogger, AbstractMatchInfo, AbstractRouter, AbstractStreamWriter
from helpers import DEBUG, AppKey
from http_parser import RawRequestMessage
from log import web_logger
from streams import StreamReader
from typedefs import Handler, Middleware
from web_exceptions import NotAppKeyWarning
from web_log import AccessLogger
from web_middlewares import _fix_request_current_app
from web_protocol import RequestHandler
from web_request import Request
from web_response import StreamResponse
from web_routedef import AbstractRouteDef
from web_server import Server
from web_urldispatcher import AbstractResource, AbstractRoute, Domain, MaskDomain, MatchedSubAppResource, PrefixedSubAppResource, SystemRoute, UrlDispatcher
__all__ = ('Application', 'CleanupError')
if TYPE_CHECKING:
    _AppSignal = Signal['Application']
    _RespPrepareSignal = Signal[(Request, StreamResponse)]
    _Middlewares = FrozenList[Middleware]
    _MiddlewaresHandlers = Optional[Sequence[Tuple[(Middleware, bool)]]]
    _Subapps = List['Application']
else:
    _AppSignal = Signal
    _RespPrepareSignal = Signal
    _Middlewares = FrozenList
    _MiddlewaresHandlers = Optional[Sequence]
    _Subapps = List
_T = TypeVar('_T')
_U = TypeVar('_U')
_Resource = TypeVar('_Resource', bound = AbstractResource)

def _build_middlewares(handler = None, apps = None):
    '''Apply middlewares to handler.'''
    for app in apps[::-1]:
        for m, _ in app._middlewares_handlers:
            handler = update_wrapper(partial(m, handler = handler), handler)
            return handler

_cached_build_middleware = lru_cache(maxsize = 1024)(_build_middlewares)

def Application():
    '''Application'''
    pass
# WARNING: Decompyle incomplete

Application = <NODE:27>(Application, 'Application', MutableMapping[(Union[(str, AppKey[Any])], Any)])

class CleanupError(RuntimeError):
    exceptions = (lambda self = None: cast(List[BaseException], self.args[1]))()


class CleanupContext(_CleanupContextBase):
    pass
# WARNING: Decompyle incomplete
