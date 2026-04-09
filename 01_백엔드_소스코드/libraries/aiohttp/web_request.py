# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_request.pyc (Python 3.11)

import asyncio
import datetime
import io
import re
import socket
import string
import tempfile
import types
import warnings
from types import MappingProxyType
from typing import TYPE_CHECKING, Any, Dict, Final, Iterator, Mapping, MutableMapping, Optional, Pattern, Tuple, Union, cast
from urllib.parse import parse_qsl
import attr
from multidict import CIMultiDict, CIMultiDictProxy, MultiDict, MultiDictProxy, MultiMapping
from yarl import URL
from  import hdrs
from _cookie_helpers import parse_cookie_header
from abc import AbstractStreamWriter
from helpers import _SENTINEL, DEBUG, ETAG_ANY, LIST_QUOTED_ETAG_RE, ChainMapProxy, ETag, HeadersMixin, parse_http_date, reify, sentinel, set_exception
from http_parser import RawRequestMessage
from http_writer import HttpVersion
from multipart import BodyPartReader, MultipartReader
from streams import EmptyStreamReader, StreamReader
from typedefs import DEFAULT_JSON_DECODER, JSONDecoder, LooseHeaders, RawHeaders, StrOrURL
from web_exceptions import HTTPRequestEntityTooLarge
from web_response import StreamResponse
__all__ = ('BaseRequest', 'FileField', 'Request')
if TYPE_CHECKING:
    from web_app import Application
    from web_protocol import RequestHandler
    from web_urldispatcher import UrlMappingMatchInfo
FileField = <NODE:12>()
_TCHAR: Final[str] = string.digits + string.ascii_letters + "!#$%&'*+.^_`|~-"
_TOKEN: Final[str] = f'''[{_TCHAR}]+'''
_QDTEXT: Final[str] = ''.join((lambda .0: pass# WARNING: Decompyle incomplete
)((9, 32, 33) + tuple(range(35, 127))()))
_QUOTED_PAIR: Final[str] = '\\\\[\\t !-~]'
_QUOTED_STRING: Final[str] = '"(?:{quoted_pair}|{qdtext})*"'.format(qdtext = _QDTEXT, quoted_pair = _QUOTED_PAIR)
_FORWARDED_PAIR: Final[str] = '({token})=({token}|{quoted_string})(:\\d{{1,4}})?'.format(token = _TOKEN, quoted_string = _QUOTED_STRING)
_QUOTED_PAIR_REPLACE_RE: Final[Pattern[str]] = re.compile('\\\\([\\t !-~])')
_FORWARDED_PAIR_RE: Final[Pattern[str]] = re.compile(_FORWARDED_PAIR)

def BaseRequest():
    '''BaseRequest'''
    POST_METHODS = {
        hdrs.METH_PATCH,
        hdrs.METH_POST,
        hdrs.METH_PUT,
        hdrs.METH_TRACE,
        hdrs.METH_DELETE}
    ATTRS = HeadersMixin.ATTRS | frozenset([
        '_message',
        '_protocol',
        '_payload_writer',
        '_payload',
        '_headers',
        '_method',
        '_version',
        '_rel_url',
        '_post',
        '_read_bytes',
        '_state',
        '_cache',
        '_task',
        '_client_max_size',
        '_loop',
        '_transport_sslcontext',
        '_transport_peername'])
    _post: Optional[MultiDictProxy[Union[(str, bytes, FileField)]]] = None
    _read_bytes: Optional[bytes] = None
    
    def __init__(self, message = None, payload = None, protocol = None, payload_writer = None, task = {
        'client_max_size': 1048576,
        'state': None,
        'scheme': None,
        'host': None,
        'remote': None }, loop = ('message', RawRequestMessage, 'payload', StreamReader, 'protocol', 'RequestHandler', 'payload_writer', AbstractStreamWriter, 'task', 'asyncio.Task[None]', 'loop', asyncio.AbstractEventLoop, 'client_max_size', int, 'state', Optional[Dict[(str, Any)]], 'scheme', Optional[str], 'host', Optional[str], 'remote', Optional[str], 'return', None), *, client_max_size, state, scheme, host, remote):
        self._message = message
        self._protocol = protocol
        self._payload_writer = payload_writer
        self._payload = payload
        self._headers = message.headers
        self._method = message.method
        self._version = message.version
        self._cache = { }
        url = message.url
    # WARNING: Decompyle incomplete

    
    def clone(self = None, *, method, rel_url, headers, scheme, host, remote, client_max_size):
        '''Clone itself with replacement some attributes.

        Creates and returns a new instance of Request object. If no parameters
        are given, an exact copy is returned. If a parameter is not passed, it
        will reuse the one from the current request object.
        '''
        if self._read_bytes:
            raise RuntimeError('Cannot clone request after reading its content')
        dct = { }
        if method is not sentinel:
            dct['method'] = method
        if rel_url is not sentinel:
            new_url = URL(rel_url)
            dct['url'] = new_url
            dct['path'] = str(new_url)
        if headers is not sentinel:
            dct['headers'] = CIMultiDictProxy(CIMultiDict(headers))
            dct['raw_headers'] = (lambda .0: pass# WARNING: Decompyle incomplete
)(dct['headers'].items()())
    # WARNING: Decompyle incomplete

    task = (lambda self = None: self._task)()
    protocol = (lambda self = None: self._protocol)()
    transport = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    writer = (lambda self = None: self._payload_writer)()
    client_max_size = (lambda self = None: self._client_max_size)()
    message = (lambda self = None: warnings.warn('Request.message is deprecated', DeprecationWarning, stacklevel = 3)self._message)()
    rel_url = (lambda self = None: self._rel_url)()
    loop = (lambda self = None: warnings.warn('request.loop property is deprecated', DeprecationWarning, stacklevel = 2)self._loop)()
    
    def __getitem__(self = None, key = None):
        return self._state[key]

    
    def __setitem__(self = None, key = None, value = None):
        self._state[key] = value

    
    def __delitem__(self = None, key = None):
        del self._state[key]

    
    def __len__(self = None):
        return len(self._state)

    
    def __iter__(self = None):
        return iter(self._state)

    secure = (lambda self = None: self.scheme == 'https')()
    forwarded = (lambda self = None: elems = []# WARNING: Decompyle incomplete
)()
    scheme = (lambda self = None: if self._transport_sslcontext:
'https')()
    method = (lambda self = None: self._method)()
    version = (lambda self = None: self._version)()
    host = (lambda self = None: host = self._message.headers.get(hdrs.HOST)# WARNING: Decompyle incomplete
)()
    remote = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    url = (lambda self = None: URL.build(scheme = self.scheme, authority = self.host).join(self._rel_url))()
    path = (lambda self = None: self._rel_url.path)()
    path_qs = (lambda self = None: str(self._rel_url))()
    raw_path = (lambda self = None: self._message.path)()
    query = (lambda self = None: self._rel_url.query)()
    query_string = (lambda self = None: self._rel_url.query_string)()
    headers = (lambda self = None: self._headers)()
    raw_headers = (lambda self = None: self._message.raw_headers)()
    if_modified_since = (lambda self = None: parse_http_date(self.headers.get(hdrs.IF_MODIFIED_SINCE)))()
    if_unmodified_since = (lambda self = None: parse_http_date(self.headers.get(hdrs.IF_UNMODIFIED_SINCE)))()
    _etag_values = (lambda etag_header = None: pass# WARNING: Decompyle incomplete
)()
    _if_match_or_none_impl = (lambda cls = None, header_value = None: if not header_value:
NoneNone(cls._etag_values(header_value)))()
    if_match = (lambda self = None: self._if_match_or_none_impl(self.headers.get(hdrs.IF_MATCH)))()
    if_none_match = (lambda self = None: self._if_match_or_none_impl(self.headers.get(hdrs.IF_NONE_MATCH)))()
    if_range = (lambda self = None: parse_http_date(self.headers.get(hdrs.IF_RANGE)))()
    keep_alive = (lambda self = None: not (self._message.should_close))()
    cookies = (lambda self = None: parsed = parse_cookie_header(self.headers.get(hdrs.COOKIE, ''))(lambda .0: pass# WARNING: Decompyle incomplete
)(parsed())
)()
    http_range = (lambda self = None: rng = self._headers.get(hdrs.RANGE)(start, end) = (None, None)# WARNING: Decompyle incomplete
)()
    content = (lambda self = None: self._payload)()
    has_body = (lambda self = None: warnings.warn('Deprecated, use .can_read_body #2005', DeprecationWarning, stacklevel = 2)not self._payload.at_eof())()
    can_read_body = (lambda self = None: not self._payload.at_eof())()
    body_exists = (lambda self = None: type(self._payload) is not EmptyStreamReader)()
    
    async def release(self = None):
        '''Release request.

        Eat unread part of HTTP BODY if present.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def read(self = None):
        '''Read request body if present.

        Returns bytes object with full request content.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def text(self = None):
        '''Return BODY as text using encoding from .charset.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def json(self = None, *, loads):
        '''Return BODY as JSON.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def multipart(self = None):
        '''Return async iterator to process BODY as multipart.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def post(self = None):
        '''Return POST parameters.'''
        pass
    # WARNING: Decompyle incomplete

    
    def get_extra_info(self = None, name = None, default = None):
        '''Extra info from protocol transport'''
        protocol = self._protocol
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        ascii_encodable_path = self.path.encode('ascii', 'backslashreplace').decode('ascii')
        return '<{} {} {} >'.format(self.__class__.__name__, self._method, ascii_encodable_path)

    
    def __eq__(self = None, other = None):
        return id(self) == id(other)

    
    def __bool__(self = None):
        return True

    
    async def _prepare_hook(self = None, response = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _cancel(self = None, exc = None):
        set_exception(self._payload, exc)

    
    def _finish(self = None):
        pass
    # WARNING: Decompyle incomplete


BaseRequest = <NODE:27>(BaseRequest, 'BaseRequest', MutableMapping[(str, Any)], HeadersMixin)

class Request(BaseRequest):
    pass
# WARNING: Decompyle incomplete
