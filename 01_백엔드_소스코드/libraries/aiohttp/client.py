# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client.pyc (Python 3.11)

'''HTTP Client for asyncio.'''
import asyncio
import base64
import hashlib
import json
import os
import sys
import traceback
import warnings
from contextlib import suppress
from types import TracebackType
from typing import TYPE_CHECKING, Any, Awaitable, Callable, Coroutine, Final, FrozenSet, Generator, Generic, Iterable, List, Mapping, Optional, Sequence, Set, Tuple, Type, TypedDict, TypeVar, Union
import attr
from multidict import CIMultiDict, MultiDict, MultiDictProxy, istr
from yarl import URL
from  import hdrs, http, payload
from _websocket.reader import WebSocketDataQueue
from abc import AbstractCookieJar
from client_exceptions import ClientConnectionError, ClientConnectionResetError, ClientConnectorCertificateError, ClientConnectorDNSError, ClientConnectorError, ClientConnectorSSLError, ClientError, ClientHttpProxyError, ClientOSError, ClientPayloadError, ClientProxyConnectionError, ClientResponseError, ClientSSLError, ConnectionTimeoutError, ContentTypeError, InvalidURL, InvalidUrlClientError, InvalidUrlRedirectClientError, NonHttpUrlClientError, NonHttpUrlRedirectClientError, RedirectClientError, ServerConnectionError, ServerDisconnectedError, ServerFingerprintMismatch, ServerTimeoutError, SocketTimeoutError, TooManyRedirects, WSMessageTypeError, WSServerHandshakeError
from client_middlewares import ClientMiddlewareType, build_client_middlewares
from client_reqrep import ClientRequest, ClientResponse, Fingerprint, RequestInfo, _merge_ssl_params
from client_ws import DEFAULT_WS_CLIENT_TIMEOUT, ClientWebSocketResponse, ClientWSTimeout
from connector import HTTP_AND_EMPTY_SCHEMA_SET, BaseConnector, NamedPipeConnector, TCPConnector, UnixConnector
from cookiejar import CookieJar
from helpers import _SENTINEL, DEBUG, EMPTY_BODY_METHODS, BasicAuth, TimeoutHandle, basicauth_from_netrc, get_env_proxy_for_url, netrc_from_env, sentinel, strip_auth_from_url
from http import WS_KEY, HttpVersion, WebSocketReader, WebSocketWriter
from http_websocket import WSHandshakeError, ws_ext_gen, ws_ext_parse
from tracing import Trace, TraceConfig
from typedefs import JSONEncoder, LooseCookies, LooseHeaders, Query, StrOrURL
__all__ = ('ClientConnectionError', 'ClientConnectionResetError', 'ClientConnectorCertificateError', 'ClientConnectorDNSError', 'ClientConnectorError', 'ClientConnectorSSLError', 'ClientError', 'ClientHttpProxyError', 'ClientOSError', 'ClientPayloadError', 'ClientProxyConnectionError', 'ClientResponseError', 'ClientSSLError', 'ConnectionTimeoutError', 'ContentTypeError', 'InvalidURL', 'InvalidUrlClientError', 'RedirectClientError', 'NonHttpUrlClientError', 'InvalidUrlRedirectClientError', 'NonHttpUrlRedirectClientError', 'ServerConnectionError', 'ServerDisconnectedError', 'ServerFingerprintMismatch', 'ServerTimeoutError', 'SocketTimeoutError', 'TooManyRedirects', 'WSServerHandshakeError', 'ClientRequest', 'ClientResponse', 'Fingerprint', 'RequestInfo', 'BaseConnector', 'TCPConnector', 'UnixConnector', 'NamedPipeConnector', 'ClientWebSocketResponse', 'ClientSession', 'ClientTimeout', 'ClientWSTimeout', 'request', 'WSMessageTypeError')
if TYPE_CHECKING:
    from ssl import SSLContext
else:
    SSLContext = None
if sys.version_info >= (3, 11) and TYPE_CHECKING:
    from typing import Unpack

def _RequestOptions():
    '''_RequestOptions'''
    middlewares: Optional[Sequence[ClientMiddlewareType]] = '_RequestOptions'

_RequestOptions = <NODE:27>(_RequestOptions, '_RequestOptions', TypedDict, total = False)
ClientTimeout = <NODE:12>()
DEFAULT_TIMEOUT: Final[ClientTimeout] = ClientTimeout(total = 300, sock_connect = 30)
IDEMPOTENT_METHODS = frozenset({
    'GET',
    'PUT',
    'HEAD',
    'TRACE',
    'DELETE',
    'OPTIONS'})
_RetType = TypeVar('_RetType', ClientResponse, ClientWebSocketResponse)
_CharsetResolver = Callable[([
    ClientResponse,
    bytes], str)]

class ClientSession:
    pass
# WARNING: Decompyle incomplete


def _BaseRequestContextManager():
    '''_BaseRequestContextManager'''
    __slots__ = ('_coro', '_resp')
    
    def __init__(self = None, coro = None):
        self._coro = coro

    
    def send(self = None, arg = None):
        return self._coro.send(arg)

    
    def throw(self = None, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        return self._coro.close()

    
    def __await__(self = None):
        ret = self._coro.__await__()
        return ret

    
    def __iter__(self = None):
        return self.__await__()

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc = None, tb = ('exc_type', Optional[Type[BaseException]], 'exc', Optional[BaseException], 'tb', Optional[TracebackType], 'return', None)):
        pass
    # WARNING: Decompyle incomplete


_BaseRequestContextManager = <NODE:27>(_BaseRequestContextManager, '_BaseRequestContextManager', Coroutine[(Any, Any, _RetType)], Generic[_RetType])
_RequestContextManager = _BaseRequestContextManager[ClientResponse]
_WSRequestContextManager = _BaseRequestContextManager[ClientWebSocketResponse]

class _SessionRequestContextManager:
    __slots__ = ('_coro', '_resp', '_session')
    
    def __init__(self = None, coro = None, session = None):
        self._coro = coro
        self._resp = None
        self._session = session

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc = None, tb = ('exc_type', Optional[Type[BaseException]], 'exc', Optional[BaseException], 'tb', Optional[TracebackType], 'return', None)):
        pass
    # WARNING: Decompyle incomplete


if sys.version_info >= (3, 11) and TYPE_CHECKING:
    
    def request(method = None, url = attr.s(auto_attribs = True, frozen = True, slots = True), *, version, connector, loop, **kwargs):
        pass

    return None

def request(method = None, url = None, *, version, connector, loop, **kwargs):
    """Constructs and sends a request.

        Returns response object.
        method - HTTP method
        url - request url
        params - (optional) Dictionary or bytes to be sent in the query
        string of the new request
        data - (optional) Dictionary, bytes, or file-like object to
        send in the body of the request
        json - (optional) Any json compatible python object
        headers - (optional) Dictionary of HTTP Headers to send with
        the request
        cookies - (optional) Dict object to send with the request
        auth - (optional) BasicAuth named tuple represent HTTP Basic Auth
        auth - aiohttp.helpers.BasicAuth
        allow_redirects - (optional) If set to False, do not follow
        redirects
        version - Request HTTP version.
        compress - Set to True if request has to be compressed
        with deflate encoding.
        chunked - Set to chunk size for chunked transfer encoding.
        expect100 - Expect 100-continue response from server.
        connector - BaseConnector sub-class instance to support
        connection pooling.
        read_until_eof - Read response until eof if response
        does not have Content-Length header.
        loop - Optional event loop.
        timeout - Optional ClientTimeout settings structure, 5min
        total timeout by default.
        Usage::
        >>> import aiohttp
        >>> async with aiohttp.request('GET', 'http://python.org/') as resp:
        ...    print(resp)
        ...    data = await resp.read()
        <ClientResponse(https://www.python.org/) [200 OK]>
        """
    connector_owner = False
# WARNING: Decompyle incomplete
