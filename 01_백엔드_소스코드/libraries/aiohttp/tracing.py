# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tracing.pyc (Python 3.11)

from types import SimpleNamespace
from typing import TYPE_CHECKING, Mapping, Optional, Type, TypeVar
import attr
from aiosignal import Signal
from multidict import CIMultiDict
from yarl import URL
from client_reqrep import ClientResponse
if TYPE_CHECKING:
    from client import ClientSession
    _ParamT_contra = TypeVar('_ParamT_contra', contravariant = True)
    _TracingSignal = Signal[(ClientSession, SimpleNamespace, _ParamT_contra)]
__all__ = ('TraceConfig', 'TraceRequestStartParams', 'TraceRequestEndParams', 'TraceRequestExceptionParams', 'TraceConnectionQueuedStartParams', 'TraceConnectionQueuedEndParams', 'TraceConnectionCreateStartParams', 'TraceConnectionCreateEndParams', 'TraceConnectionReuseconnParams', 'TraceDnsResolveHostStartParams', 'TraceDnsResolveHostEndParams', 'TraceDnsCacheHitParams', 'TraceDnsCacheMissParams', 'TraceRequestRedirectParams', 'TraceRequestChunkSentParams', 'TraceResponseChunkReceivedParams', 'TraceRequestHeadersSentParams')

class TraceConfig:
    '''First-class used to trace requests launched via ClientSession objects.'''
    
    def __init__(self = None, trace_config_ctx_factory = None):
        self._on_request_start = Signal(self)
        self._on_request_chunk_sent = Signal(self)
        self._on_response_chunk_received = Signal(self)
        self._on_request_end = Signal(self)
        self._on_request_exception = Signal(self)
        self._on_request_redirect = Signal(self)
        self._on_connection_queued_start = Signal(self)
        self._on_connection_queued_end = Signal(self)
        self._on_connection_create_start = Signal(self)
        self._on_connection_create_end = Signal(self)
        self._on_connection_reuseconn = Signal(self)
        self._on_dns_resolvehost_start = Signal(self)
        self._on_dns_resolvehost_end = Signal(self)
        self._on_dns_cache_hit = Signal(self)
        self._on_dns_cache_miss = Signal(self)
        self._on_request_headers_sent = Signal(self)
        self._trace_config_ctx_factory = trace_config_ctx_factory

    
    def trace_config_ctx(self = None, trace_request_ctx = None):
        '''Return a new trace_config_ctx instance'''
        return self._trace_config_ctx_factory(trace_request_ctx = trace_request_ctx)

    
    def freeze(self = None):
        self._on_request_start.freeze()
        self._on_request_chunk_sent.freeze()
        self._on_response_chunk_received.freeze()
        self._on_request_end.freeze()
        self._on_request_exception.freeze()
        self._on_request_redirect.freeze()
        self._on_connection_queued_start.freeze()
        self._on_connection_queued_end.freeze()
        self._on_connection_create_start.freeze()
        self._on_connection_create_end.freeze()
        self._on_connection_reuseconn.freeze()
        self._on_dns_resolvehost_start.freeze()
        self._on_dns_resolvehost_end.freeze()
        self._on_dns_cache_hit.freeze()
        self._on_dns_cache_miss.freeze()
        self._on_request_headers_sent.freeze()

    on_request_start = (lambda self = None: self._on_request_start)()
    on_request_chunk_sent = (lambda self = None: self._on_request_chunk_sent)()
    on_response_chunk_received = (lambda self = None: self._on_response_chunk_received)()
    on_request_end = (lambda self = None: self._on_request_end)()
    on_request_exception = (lambda self = None: self._on_request_exception)()
    on_request_redirect = (lambda self = None: self._on_request_redirect)()
    on_connection_queued_start = (lambda self = None: self._on_connection_queued_start)()
    on_connection_queued_end = (lambda self = None: self._on_connection_queued_end)()
    on_connection_create_start = (lambda self = None: self._on_connection_create_start)()
    on_connection_create_end = (lambda self = None: self._on_connection_create_end)()
    on_connection_reuseconn = (lambda self = None: self._on_connection_reuseconn)()
    on_dns_resolvehost_start = (lambda self = None: self._on_dns_resolvehost_start)()
    on_dns_resolvehost_end = (lambda self = None: self._on_dns_resolvehost_end)()
    on_dns_cache_hit = (lambda self = None: self._on_dns_cache_hit)()
    on_dns_cache_miss = (lambda self = None: self._on_dns_cache_miss)()
    on_request_headers_sent = (lambda self = None: self._on_request_headers_sent)()

TraceRequestStartParams = <NODE:12>()
TraceRequestChunkSentParams = <NODE:12>()
TraceResponseChunkReceivedParams = <NODE:12>()
TraceRequestEndParams = <NODE:12>()
TraceRequestExceptionParams = <NODE:12>()
TraceRequestRedirectParams = <NODE:12>()
TraceConnectionQueuedStartParams = <NODE:12>()
TraceConnectionQueuedEndParams = <NODE:12>()
TraceConnectionCreateStartParams = <NODE:12>()
TraceConnectionCreateEndParams = <NODE:12>()
TraceConnectionReuseconnParams = <NODE:12>()
TraceDnsResolveHostStartParams = <NODE:12>()
TraceDnsResolveHostEndParams = <NODE:12>()
TraceDnsCacheHitParams = <NODE:12>()
TraceDnsCacheMissParams = <NODE:12>()
TraceRequestHeadersSentParams = <NODE:12>()

class Trace:
    '''Internal dependency holder class.

    Used to keep together the main dependencies used
    at the moment of send a signal.
    '''
    
    def __init__(self = None, session = None, trace_config = None, trace_config_ctx = ('session', 'ClientSession', 'trace_config', TraceConfig, 'trace_config_ctx', SimpleNamespace, 'return', None)):
        self._trace_config = trace_config
        self._trace_config_ctx = trace_config_ctx
        self._session = session

    
    async def send_request_start(self = None, method = None, url = None, headers = ('method', str, 'url', URL, 'headers', 'CIMultiDict[str]', 'return', None)):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_request_chunk_sent(self = None, method = None, url = None, chunk = ('method', str, 'url', URL, 'chunk', bytes, 'return', None)):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_response_chunk_received(self = None, method = None, url = None, chunk = ('method', str, 'url', URL, 'chunk', bytes, 'return', None)):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_request_end(self, method = None, url = None, headers = None, response = ('method', str, 'url', URL, 'headers', 'CIMultiDict[str]', 'response', ClientResponse, 'return', None)):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_request_exception(self, method = None, url = None, headers = None, exception = ('method', str, 'url', URL, 'headers', 'CIMultiDict[str]', 'exception', BaseException, 'return', None)):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_request_redirect(self, method = None, url = None, headers = None, response = ('method', str, 'url', URL, 'headers', 'CIMultiDict[str]', 'response', ClientResponse, 'return', None)):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_connection_queued_start(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_connection_queued_end(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_connection_create_start(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_connection_create_end(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_connection_reuseconn(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_dns_resolvehost_start(self = None, host = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_dns_resolvehost_end(self = None, host = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_dns_cache_hit(self = None, host = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_dns_cache_miss(self = None, host = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_request_headers(self = None, method = None, url = None, headers = ('method', str, 'url', URL, 'headers', 'CIMultiDict[str]', 'return', None)):
        pass
    # WARNING: Decompyle incomplete
