# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: abc.pyc (Python 3.11)

import asyncio
import logging
import socket
from abc import ABC, abstractmethod
from collections.abc import Sized
from http.cookies import BaseCookie, Morsel
from typing import TYPE_CHECKING, Any, Awaitable, Callable, Dict, Generator, Iterable, List, Optional, Sequence, Tuple, TypedDict, Union
from multidict import CIMultiDict
from yarl import URL
from _cookie_helpers import parse_set_cookie_headers
from typedefs import LooseCookies
if TYPE_CHECKING:
    from web_app import Application
    from web_exceptions import HTTPException
    from web_request import BaseRequest, Request
    from web_response import StreamResponse
else:
    BaseRequest = None
    Request = None
    Application = None
    StreamResponse = None
    HTTPException = None

class AbstractRouter(ABC):
    
    def __init__(self = None):
        self._frozen = False

    
    def post_init(self = None, app = None):
        '''Post init stage.

        Not an abstract method for sake of backward compatibility,
        but if the router wants to be aware of the application
        it can override this.
        '''
        pass

    frozen = (lambda self = None: self._frozen)()
    
    def freeze(self = None):
        '''Freeze router.'''
        self._frozen = True

    resolve = (lambda self = None, request = None: pass# WARNING: Decompyle incomplete
)()


class AbstractMatchInfo(ABC):
    __slots__ = ()
    handler = (lambda self = None: pass)()()
    expect_handler = (lambda self = None: pass)()()
    http_exception = (lambda self = None: pass)()()
    get_info = (lambda self = None: pass)()
    apps = (lambda self = None: pass)()()
    add_app = (lambda self = None, app = None: pass)()
    freeze = (lambda self = None: pass)()


class AbstractView(ABC):
    '''Abstract class based view.'''
    
    def __init__(self = None, request = None):
        self._request = request

    request = (lambda self = None: self._request)()
    __await__ = (lambda self = None: pass)()


class ResolveResult(TypedDict):
    flags: int = "Resolve result.\n\n    This is the result returned from an AbstractResolver's\n    resolve method.\n\n    :param hostname: The hostname that was provided.\n    :param host: The IP address that was resolved.\n    :param port: The port that was resolved.\n    :param family: The address family that was resolved.\n    :param proto: The protocol that was resolved.\n    :param flags: The flags that were resolved.\n    "


class AbstractResolver(ABC):
    '''Abstract DNS resolver.'''
    resolve = (lambda self = None, host = None, port = abstractmethod, family = (0, socket.AF_INET): pass# WARNING: Decompyle incomplete
)()
    close = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

ClearCookiePredicate = Callable[([
    'Morsel[str]'], bool)]

class AbstractCookieJar(IterableBase, Sized):
    '''Abstract Cookie Jar.'''
    
    def __init__(self = None, *, loop):
        if not loop:
            pass
        self._loop = asyncio.get_running_loop()

    quote_cookie = (lambda self = None: pass)()()
    clear = (lambda self = None, predicate = None: pass)()
    clear_domain = (lambda self = None, domain = None: pass)()
    update_cookies = (lambda self = None, cookies = None, response_url = abstractmethod: pass)()
    
    def update_cookies_from_headers(self = None, headers = None, response_url = None):
        '''Update cookies from raw Set-Cookie headers.'''
        if headers:
            cookies_to_update = parse_set_cookie_headers(headers)
            if parse_set_cookie_headers(headers):
                self.update_cookies(cookies_to_update, response_url)
                return None
            return None

    filter_cookies = (lambda self = None, request_url = None: pass)()


class AbstractStreamWriter(ABC):
    '''Abstract stream writer.'''
    buffer_size: int = 0
    output_size: int = 0
    length: Optional[int] = 0
    write = (lambda self = None, chunk = None: pass# WARNING: Decompyle incomplete
)()
    write_eof = (lambda self = None, chunk = None: pass# WARNING: Decompyle incomplete
)()
    drain = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    enable_compression = (lambda self = None, encoding = None, strategy = abstractmethod: pass)()
    enable_chunking = (lambda self = None: pass)()
    write_headers = (lambda self = None, status_line = None, headers = abstractmethod: pass# WARNING: Decompyle incomplete
)()
    
    def send_headers(self = None):
        '''Force sending buffered headers if not already sent.

        Required only if write_headers() buffers headers instead of sending immediately.
        For backwards compatibility, this method does nothing by default.
        '''
        pass



class AbstractAccessLogger(ABC):
    '''Abstract writer to access log.'''
    __slots__ = ('logger', 'log_format')
    
    def __init__(self = None, logger = None, log_format = None):
        self.logger = logger
        self.log_format = log_format

    log = (lambda self = None, request = None, response = abstractmethod, time = ('request', BaseRequest, 'response', StreamResponse, 'time', float, 'return', None): pass)()
    enabled = (lambda self = None: True)()
