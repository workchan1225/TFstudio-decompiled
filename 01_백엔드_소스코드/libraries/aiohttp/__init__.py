# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

__version__ = '3.13.2'
from typing import TYPE_CHECKING, Tuple
from  import hdrs
from client import BaseConnector, ClientConnectionError, ClientConnectionResetError, ClientConnectorCertificateError, ClientConnectorDNSError, ClientConnectorError, ClientConnectorSSLError, ClientError, ClientHttpProxyError, ClientOSError, ClientPayloadError, ClientProxyConnectionError, ClientRequest, ClientResponse, ClientResponseError, ClientSession, ClientSSLError, ClientTimeout, ClientWebSocketResponse, ClientWSTimeout, ConnectionTimeoutError, ContentTypeError, Fingerprint, InvalidURL, InvalidUrlClientError, InvalidUrlRedirectClientError, NamedPipeConnector, NonHttpUrlClientError, NonHttpUrlRedirectClientError, RedirectClientError, RequestInfo, ServerConnectionError, ServerDisconnectedError, ServerFingerprintMismatch, ServerTimeoutError, SocketTimeoutError, TCPConnector, TooManyRedirects, UnixConnector, WSMessageTypeError, WSServerHandshakeError, request
from client_middleware_digest_auth import DigestAuthMiddleware
from client_middlewares import ClientHandlerType, ClientMiddlewareType
from compression_utils import set_zlib_backend
from connector import AddrInfoType, SocketFactoryType
from cookiejar import CookieJar, DummyCookieJar
from formdata import FormData
from helpers import BasicAuth, ChainMapProxy, ETag
from http import HttpVersion, HttpVersion10, HttpVersion11, WebSocketError, WSCloseCode, WSMessage, WSMsgType
from multipart import BadContentDispositionHeader, BadContentDispositionParam, BodyPartReader, MultipartReader, MultipartWriter, content_disposition_filename, parse_content_disposition
from payload import PAYLOAD_REGISTRY, AsyncIterablePayload, BufferedReaderPayload, BytesIOPayload, BytesPayload, IOBasePayload, JsonPayload, Payload, StringIOPayload, StringPayload, TextIOPayload, get_payload, payload_type
from payload_streamer import streamer
from resolver import AsyncResolver, DefaultResolver, ThreadedResolver
from streams import EMPTY_PAYLOAD, DataQueue, EofStream, FlowControlDataQueue, StreamReader
from tracing import TraceConfig, TraceConnectionCreateEndParams, TraceConnectionCreateStartParams, TraceConnectionQueuedEndParams, TraceConnectionQueuedStartParams, TraceConnectionReuseconnParams, TraceDnsCacheHitParams, TraceDnsCacheMissParams, TraceDnsResolveHostEndParams, TraceDnsResolveHostStartParams, TraceRequestChunkSentParams, TraceRequestEndParams, TraceRequestExceptionParams, TraceRequestHeadersSentParams, TraceRequestRedirectParams, TraceRequestStartParams, TraceResponseChunkReceivedParams
if TYPE_CHECKING:
    GunicornUVLoopWebWorker = GunicornUVLoopWebWorker
    GunicornWebWorker = GunicornWebWorker
    import worker
__all__: Tuple[(str, ...)] = ('hdrs', 'AddrInfoType', 'BaseConnector', 'ClientConnectionError', 'ClientConnectionResetError', 'ClientConnectorCertificateError', 'ClientConnectorDNSError', 'ClientConnectorError', 'ClientConnectorSSLError', 'ClientError', 'ClientHttpProxyError', 'ClientOSError', 'ClientPayloadError', 'ClientProxyConnectionError', 'ClientResponse', 'ClientRequest', 'ClientResponseError', 'ClientSSLError', 'ClientSession', 'ClientTimeout', 'ClientWebSocketResponse', 'ClientWSTimeout', 'ConnectionTimeoutError', 'ContentTypeError', 'Fingerprint', 'FlowControlDataQueue', 'InvalidURL', 'InvalidUrlClientError', 'InvalidUrlRedirectClientError', 'NonHttpUrlClientError', 'NonHttpUrlRedirectClientError', 'RedirectClientError', 'RequestInfo', 'ServerConnectionError', 'ServerDisconnectedError', 'ServerFingerprintMismatch', 'ServerTimeoutError', 'SocketFactoryType', 'SocketTimeoutError', 'TCPConnector', 'TooManyRedirects', 'UnixConnector', 'NamedPipeConnector', 'WSServerHandshakeError', 'request', 'ClientMiddlewareType', 'ClientHandlerType', 'CookieJar', 'DummyCookieJar', 'FormData', 'BasicAuth', 'ChainMapProxy', 'DigestAuthMiddleware', 'ETag', 'set_zlib_backend', 'HttpVersion', 'HttpVersion10', 'HttpVersion11', 'WSMsgType', 'WSCloseCode', 'WSMessage', 'WebSocketError', 'BadContentDispositionHeader', 'BadContentDispositionParam', 'BodyPartReader', 'MultipartReader', 'MultipartWriter', 'content_disposition_filename', 'parse_content_disposition', 'AsyncIterablePayload', 'BufferedReaderPayload', 'BytesIOPayload', 'BytesPayload', 'IOBasePayload', 'JsonPayload', 'PAYLOAD_REGISTRY', 'Payload', 'StringIOPayload', 'StringPayload', 'TextIOPayload', 'get_payload', 'payload_type', 'streamer', 'AsyncResolver', 'DefaultResolver', 'ThreadedResolver', 'DataQueue', 'EMPTY_PAYLOAD', 'EofStream', 'StreamReader', 'TraceConfig', 'TraceConnectionCreateEndParams', 'TraceConnectionCreateStartParams', 'TraceConnectionQueuedEndParams', 'TraceConnectionQueuedStartParams', 'TraceConnectionReuseconnParams', 'TraceDnsCacheHitParams', 'TraceDnsCacheMissParams', 'TraceDnsResolveHostEndParams', 'TraceDnsResolveHostStartParams', 'TraceRequestChunkSentParams', 'TraceRequestEndParams', 'TraceRequestExceptionParams', 'TraceRequestHeadersSentParams', 'TraceRequestRedirectParams', 'TraceRequestStartParams', 'TraceResponseChunkReceivedParams', 'GunicornUVLoopWebWorker', 'GunicornWebWorker', 'WSMessageTypeError')

def __dir__():
    return __all__ + ('__doc__',)


def __getattr__(name = None):
    global GunicornUVLoopWebWorker, GunicornWebWorker
    if name in ('GunicornUVLoopWebWorker', 'GunicornWebWorker'):
        
        try:
            guv = GunicornUVLoopWebWorker
            gw = GunicornWebWorker
            import worker
        except ImportError:
            return None

        GunicornUVLoopWebWorker = guv
        GunicornWebWorker = gw
        return guv if name == 'GunicornUVLoopWebWorker' else gw
    raise AttributeError(f'''module {__name__} has no attribute {name}''')
