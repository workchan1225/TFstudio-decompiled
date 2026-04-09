# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: default.pyc (Python 3.11)

'''
Custom transports, with nicely configured defaults.

The following additional keyword arguments are currently supported by httpcore...

* uds: str
* local_address: str
* retries: int

Example usages...

# Disable HTTP/2 on a single specific domain.
mounts = {
    "all://": httpx.HTTPTransport(http2=True),
    "all://*example.org": httpx.HTTPTransport()
}

# Using advanced httpcore configuration, with connection retries.
transport = httpx.HTTPTransport(retries=1)
client = httpx.Client(transport=transport)

# Using advanced httpcore configuration, with unix domain sockets.
transport = httpx.HTTPTransport(uds="socket.uds")
client = httpx.Client(transport=transport)
'''
from __future__ import annotations
import contextlib
import typing
from types import TracebackType
if typing.TYPE_CHECKING:
    import ssl
    import httpx
from _config import DEFAULT_LIMITS, Limits, Proxy, create_ssl_context
from _exceptions import ConnectError, ConnectTimeout, LocalProtocolError, NetworkError, PoolTimeout, ProtocolError, ProxyError, ReadError, ReadTimeout, RemoteProtocolError, TimeoutException, UnsupportedProtocol, WriteError, WriteTimeout
from _models import Request, Response
from _types import AsyncByteStream, CertTypes, ProxyTypes, SyncByteStream
from _urls import URL
from base import AsyncBaseTransport, BaseTransport
T = typing.TypeVar('T', bound = 'HTTPTransport')
A = typing.TypeVar('A', bound = 'AsyncHTTPTransport')
SOCKET_OPTION = typing.Union[(typing.Tuple[(int, int, int)], typing.Tuple[(int, int, typing.Union[(bytes, bytearray)])], typing.Tuple[(int, int, None, int)])]
__all__ = [
    'AsyncHTTPTransport',
    'HTTPTransport']
HTTPCORE_EXC_MAP: 'dict[type[Exception], type[httpx.HTTPError]]' = { }

def _load_httpcore_exceptions():
    import httpcore
    return {
        httpcore.RemoteProtocolError: RemoteProtocolError,
        httpcore.LocalProtocolError: LocalProtocolError,
        httpcore.ProtocolError: ProtocolError,
        httpcore.UnsupportedProtocol: UnsupportedProtocol,
        httpcore.ProxyError: ProxyError,
        httpcore.WriteError: WriteError,
        httpcore.ReadError: ReadError,
        httpcore.ConnectError: ConnectError,
        httpcore.NetworkError: NetworkError,
        httpcore.PoolTimeout: PoolTimeout,
        httpcore.WriteTimeout: WriteTimeout,
        httpcore.ReadTimeout: ReadTimeout,
        httpcore.ConnectTimeout: ConnectTimeout,
        httpcore.TimeoutException: TimeoutException }

map_httpcore_exceptions = (lambda : pass# WARNING: Decompyle incomplete
)()

class ResponseStream(SyncByteStream):
    
    def __init__(self = None, httpcore_stream = None):
        self._httpcore_stream = httpcore_stream

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        if hasattr(self._httpcore_stream, 'close'):
            self._httpcore_stream.close()
            return None



class HTTPTransport(BaseTransport):
    
    def __init__(self, verify, cert, trust_env, http1, http2, limits, proxy = None, uds = None, local_address = None, retries = (True, None, True, True, False, DEFAULT_LIMITS, None, None, None, 0, None), socket_options = ('verify', 'ssl.SSLContext | str | bool', 'cert', 'CertTypes | None', 'trust_env', 'bool', 'http1', 'bool', 'http2', 'bool', 'limits', 'Limits', 'proxy', 'ProxyTypes | None', 'uds', 'str | None', 'local_address', 'str | None', 'retries', 'int', 'socket_options', 'typing.Iterable[SOCKET_OPTION] | None', 'return', 'None')):
        import httpcore
        proxy = Proxy(url = proxy) if isinstance(proxy, (str, URL)) else proxy
        ssl_context = create_ssl_context(verify = verify, cert = cert, trust_env = trust_env)
    # WARNING: Decompyle incomplete

    
    def __enter__(self = None):
        self._pool.__enter__()
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = (None, None, None)):
        map_httpcore_exceptions()
        self._pool.__exit__(exc_type, exc_value, traceback)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def handle_request(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        self._pool.close()



class AsyncResponseStream(AsyncByteStream):
    
    def __init__(self = None, httpcore_stream = None):
        self._httpcore_stream = httpcore_stream

    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def aclose(self = None):
        pass
    # WARNING: Decompyle incomplete



class AsyncHTTPTransport(AsyncBaseTransport):
    
    def __init__(self, verify, cert, trust_env, http1, http2, limits, proxy = None, uds = None, local_address = None, retries = (True, None, True, True, False, DEFAULT_LIMITS, None, None, None, 0, None), socket_options = ('verify', 'ssl.SSLContext | str | bool', 'cert', 'CertTypes | None', 'trust_env', 'bool', 'http1', 'bool', 'http2', 'bool', 'limits', 'Limits', 'proxy', 'ProxyTypes | None', 'uds', 'str | None', 'local_address', 'str | None', 'retries', 'int', 'socket_options', 'typing.Iterable[SOCKET_OPTION] | None', 'return', 'None')):
        import httpcore
        proxy = Proxy(url = proxy) if isinstance(proxy, (str, URL)) else proxy
        ssl_context = create_ssl_context(verify = verify, cert = cert, trust_env = trust_env)
    # WARNING: Decompyle incomplete

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_value = None, traceback = (None, None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    async def handle_async_request(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def aclose(self = None):
        pass
    # WARNING: Decompyle incomplete
