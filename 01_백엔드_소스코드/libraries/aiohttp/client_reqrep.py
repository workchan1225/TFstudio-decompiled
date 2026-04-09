# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client_reqrep.pyc (Python 3.11)

import asyncio
import codecs
import contextlib
import functools
import io
import re
import sys
import traceback
import warnings
from collections.abc import Mapping
from hashlib import md5, sha1, sha256
from http.cookies import Morsel, SimpleCookie
from types import MappingProxyType, TracebackType
from typing import TYPE_CHECKING, Any, Callable, Dict, Iterable, List, Literal, NamedTuple, Optional, Tuple, Type, Union
import attr
from multidict import CIMultiDict, CIMultiDictProxy, MultiDict, MultiDictProxy
from yarl import URL
from  import hdrs, helpers, http, multipart, payload
from _cookie_helpers import parse_cookie_header, parse_set_cookie_headers, preserve_morsel_with_coded_value
from abc import AbstractStreamWriter
from client_exceptions import ClientConnectionError, ClientOSError, ClientResponseError, ContentTypeError, InvalidURL, ServerFingerprintMismatch
from compression_utils import HAS_BROTLI, HAS_ZSTD
from formdata import FormData
from helpers import _SENTINEL, BaseTimerContext, BasicAuth, HeadersMixin, TimerNoop, noop, reify, sentinel, set_exception, set_result
from http import SERVER_SOFTWARE, HttpVersion, HttpVersion10, HttpVersion11, StreamWriter
from streams import StreamReader
from typedefs import DEFAULT_JSON_DECODER, JSONDecoder, LooseCookies, LooseHeaders, Query, RawHeaders
if TYPE_CHECKING:
    import ssl
    from ssl import SSLContext
else:
    
    try:
        import ssl
        from ssl import SSLContext
    except ImportError:
        ssl = None
        SSLContext = object

    __all__ = ('ClientRequest', 'ClientResponse', 'RequestInfo', 'Fingerprint')
    if TYPE_CHECKING:
        from client import ClientSession
        from connector import Connection
        from tracing import Trace
_CONNECTION_CLOSED_EXCEPTION = ClientConnectionError('Connection closed')
_CONTAINS_CONTROL_CHAR_RE = re.compile("[^-!#$%&'*+.^_`|~0-9a-zA-Z]")
json_re = re.compile('^application/(?:[\\w.+-]+?\\+)?json')

def _gen_default_accept_encoding():
    encodings = [
        'gzip',
        'deflate']
    if HAS_BROTLI:
        encodings.append('br')
    if HAS_ZSTD:
        encodings.append('zstd')
    return ', '.join(encodings)

ContentDisposition = <NODE:12>()

class _RequestInfo(NamedTuple):
    real_url: URL = '_RequestInfo'


class RequestInfo(_RequestInfo):
    
    def __new__(cls = None, url = None, method = None, headers = (sentinel,), real_url = ('url', URL, 'method', str, 'headers', 'CIMultiDictProxy[str]', 'real_url', Union[(URL, _SENTINEL)], 'return', 'RequestInfo')):
        '''Create a new RequestInfo instance.

        For backwards compatibility, the real_url parameter is optional.
        '''
        return tuple.__new__(cls, (url, method, headers, url if real_url is sentinel else real_url))



class Fingerprint:
    HASHFUNC_BY_DIGESTLEN = {
        16: md5,
        20: sha1,
        32: sha256 }
    
    def __init__(self = None, fingerprint = None):
        digestlen = len(fingerprint)
        hashfunc = self.HASHFUNC_BY_DIGESTLEN.get(digestlen)
        if not hashfunc:
            raise ValueError('fingerprint has invalid length')
        if hashfunc is md5 or hashfunc is sha1:
            raise ValueError('md5 and sha1 are insecure and not supported. Use sha256.')
        self._hashfunc = hashfunc
        self._fingerprint = fingerprint

    fingerprint = (lambda self = None: self._fingerprint)()
    
    def check(self = None, transport = None):
        if not transport.get_extra_info('sslcontext'):
            return None
        sslobj = None.get_extra_info('ssl_object')
        cert = sslobj.getpeercert(binary_form = True)
        got = self._hashfunc(cert).digest()
    # WARNING: Decompyle incomplete


# WARNING: Decompyle incomplete
