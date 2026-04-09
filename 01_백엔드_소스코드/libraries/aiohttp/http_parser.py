# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: http_parser.pyc (Python 3.11)

import abc
import asyncio
import re
import string
from contextlib import suppress
from enum import IntEnum
from typing import Any, ClassVar, Final, Generic, List, Literal, NamedTuple, Optional, Pattern, Set, Tuple, Type, TypeVar, Union
from multidict import CIMultiDict, CIMultiDictProxy, istr
from yarl import URL
from  import hdrs
from base_protocol import BaseProtocol
from compression_utils import HAS_BROTLI, HAS_ZSTD, BrotliDecompressor, ZLibDecompressor, ZSTDDecompressor
from helpers import _EXC_SENTINEL, DEBUG, EMPTY_BODY_METHODS, EMPTY_BODY_STATUS_CODES, NO_EXTENSIONS, BaseTimerContext, set_exception
from http_exceptions import BadHttpMessage, BadHttpMethod, BadStatusLine, ContentEncodingError, ContentLengthError, InvalidHeader, InvalidURLError, LineTooLong, TransferEncodingError
from http_writer import HttpVersion, HttpVersion10
from streams import EMPTY_PAYLOAD, StreamReader
from typedefs import RawHeaders
__all__ = ('HeadersParser', 'HttpParser', 'HttpRequestParser', 'HttpResponseParser', 'RawRequestMessage', 'RawResponseMessage')
_SEP = Literal[(b'\r\n', b'\n')]
ASCIISET: Final[Set[str]] = set(string.printable)
_TCHAR_SPECIALS: Final[str] = re.escape("!#$%&'*+-.^_`|~")
TOKENRE: Final[Pattern[str]] = re.compile(f'''[0-9A-Za-z{_TCHAR_SPECIALS}]+''')
VERSRE: Final[Pattern[str]] = re.compile('HTTP/(\\d)\\.(\\d)', re.ASCII)
DIGITS: Final[Pattern[str]] = re.compile('\\d+', re.ASCII)
HEXDIGITS: Final[Pattern[bytes]] = re.compile(b'[0-9a-fA-F]+')

class RawRequestMessage(NamedTuple):
    url: URL = 'RawRequestMessage'


class RawResponseMessage(NamedTuple):
    chunked: bool = 'RawResponseMessage'

_MsgT = TypeVar('_MsgT', RawRequestMessage, RawResponseMessage)

class ParseState(IntEnum):
    PARSE_NONE = 0
    PARSE_LENGTH = 1
    PARSE_CHUNKED = 2
    PARSE_UNTIL_EOF = 3


class ChunkState(IntEnum):
    PARSE_CHUNKED_SIZE = 0
    PARSE_CHUNKED_CHUNK = 1
    PARSE_CHUNKED_CHUNK_EOF = 2
    PARSE_MAYBE_TRAILERS = 3
    PARSE_TRAILERS = 4


class HeadersParser:
    
    def __init__(self = None, max_line_size = None, max_headers = None, max_field_size = (8190, 32768, 8190, False), lax = ('max_line_size', int, 'max_headers', int, 'max_field_size', int, 'lax', bool, 'return', None)):
        self.max_line_size = max_line_size
        self.max_headers = max_headers
        self.max_field_size = max_field_size
        self._lax = lax

    
    def parse_headers(self = None, lines = None):
        headers = CIMultiDict()
        raw_headers = []
        lines_idx = 0
        line = lines[lines_idx]
        line_count = len(lines)
    # WARNING: Decompyle incomplete



def _is_supported_upgrade(headers = None):
    '''Check if the upgrade header is supported.'''
    return headers.get(hdrs.UPGRADE, '').lower() in frozenset({'tcp', 'websocket'})


def HttpParser():
    '''HttpParser'''
    lax: ClassVar[bool] = False
    
    def __init__(self, protocol, loop, limit, max_line_size, max_headers, max_field_size, timer, code, method = None, payload_exception = None, response_with_body = None, read_until_eof = (None, None, 65536, 8190, 32768, 8190, None, None, None, None, True, False, True), auto_decompress = ('protocol', Optional[BaseProtocol], 'loop', Optional[asyncio.AbstractEventLoop], 'limit', int, 'max_line_size', int, 'max_headers', int, 'max_field_size', int, 'timer', Optional[BaseTimerContext], 'code', Optional[int], 'method', Optional[str], 'payload_exception', Optional[Type[BaseException]], 'response_with_body', bool, 'read_until_eof', bool, 'auto_decompress', bool, 'return', None)):
        self.protocol = protocol
        self.loop = loop
        self.max_line_size = max_line_size
        self.max_headers = max_headers
        self.max_field_size = max_field_size
        self.timer = timer
        self.code = code
        self.method = method
        self.payload_exception = payload_exception
        self.response_with_body = response_with_body
        self.read_until_eof = read_until_eof
        self._lines = []
        self._tail = b''
        self._upgraded = False
        self._payload = None
        self._payload_parser = None
        self._auto_decompress = auto_decompress
        self._limit = limit
        self._headers_parser = HeadersParser(max_line_size, max_headers, max_field_size, self.lax)

    parse_message = (lambda self = None, lines = None: pass)()
    _is_chunked_te = (lambda self = None, te = None: pass)()
    
    def feed_eof(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def feed_data(self, data, SEP = None, EMPTY = None, CONTENT_LENGTH = None, METH_CONNECT = (b'\r\n', b'', hdrs.CONTENT_LENGTH, hdrs.METH_CONNECT, hdrs.SEC_WEBSOCKET_KEY1), SEC_WEBSOCKET_KEY1 = ('data', bytes, 'SEP', _SEP, 'EMPTY', bytes, 'CONTENT_LENGTH', istr, 'METH_CONNECT', str, 'SEC_WEBSOCKET_KEY1', istr, 'return', Tuple[(List[Tuple[(_MsgT, StreamReader)]], bool, bytes)])):
        pass
    # WARNING: Decompyle incomplete

    
    def parse_headers(self = None, lines = None):
        '''Parses RFC 5322 headers from a stream.

        Line continuations are supported. Returns list of header name
        and value pairs. Header name is in upper case.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def set_upgraded(self = None, val = None):
        '''Set connection upgraded (to websocket) mode.

        :param bool val: new state.
        '''
        self._upgraded = val


HttpParser = <NODE:27>(HttpParser, 'HttpParser', abc.ABC, Generic[_MsgT])

def HttpRequestParser():
    '''HttpRequestParser'''
    __doc__ = 'Read request status line.\n\n    Exception .http_exceptions.BadStatusLine\n    could be raised in case of any errors in status line.\n    Returns RawRequestMessage.\n    '
    
    def parse_message(self = None, lines = None):
        line = lines[0].decode('utf-8', 'surrogateescape')
        
        try:
            (method, path, version) = line.split(' ', maxsplit = 2)
        except ValueError:
            raise BadHttpMethod(line), None

        if len(path) > self.max_line_size:
            raise LineTooLong('Status line is too long', str(self.max_line_size), str(len(path)))
        if not TOKENRE.fullmatch(method):
            raise BadHttpMethod(method)
        match = VERSRE.fullmatch(version)
    # WARNING: Decompyle incomplete

    
    def _is_chunked_te(self = None, te = None):
        if te.rsplit(',', maxsplit = 1)[-1].strip(' \t').lower() == 'chunked':
            return True
        raise None('Request has invalid `Transfer-Encoding`')


HttpRequestParser = <NODE:27>(HttpRequestParser, 'HttpRequestParser', HttpParser[RawRequestMessage])

def HttpResponseParser():
    '''HttpResponseParser'''
    pass
# WARNING: Decompyle incomplete

HttpResponseParser = <NODE:27>(HttpResponseParser, 'HttpResponseParser', HttpParser[RawResponseMessage])

class HttpPayloadParser:
    
    def __init__(self, payload, length, chunked, compression, code = None, method = None, response_with_body = None, auto_decompress = (None, False, None, None, None, True, True, False), lax = ('payload', StreamReader, 'length', Optional[int], 'chunked', bool, 'compression', Optional[str], 'code', Optional[int], 'method', Optional[str], 'response_with_body', bool, 'auto_decompress', bool, 'lax', bool, 'headers_parser', HeadersParser, 'return', None), *, headers_parser):
        self._length = 0
        self._type = ParseState.PARSE_UNTIL_EOF
        self._chunk = ChunkState.PARSE_CHUNKED_SIZE
        self._chunk_size = 0
        self._chunk_tail = b''
        self._auto_decompress = auto_decompress
        self._lax = lax
        self._headers_parser = headers_parser
        self._trailer_lines = []
        self.done = False
        if response_with_body and compression and self._auto_decompress:
            real_payload = DeflateBuffer(payload, compression)
        else:
            real_payload = payload
        if not response_with_body:
            self._type = ParseState.PARSE_NONE
            real_payload.feed_eof()
            self.done = True
        elif chunked:
            self._type = ParseState.PARSE_CHUNKED
    # WARNING: Decompyle incomplete

    
    def feed_eof(self = None):
        if self._type == ParseState.PARSE_UNTIL_EOF:
            self.payload.feed_eof()
            return None
        if None._type == ParseState.PARSE_LENGTH:
            raise ContentLengthError('Not enough data to satisfy content length header.')
        if self._type == ParseState.PARSE_CHUNKED:
            raise TransferEncodingError('Not enough data to satisfy transfer length header.')

    
    def feed_data(self = None, chunk = None, SEP = None, CHUNK_EXT = (b'\r\n', b';')):
        if self._type == ParseState.PARSE_LENGTH:
            required = self._length
            chunk_len = len(chunk)
            if required >= chunk_len:
                self._length = required - chunk_len
                self.payload.feed_data(chunk, chunk_len)
                if self._length == 0:
                    self.payload.feed_eof()
                    return (True, b'')
            self._length = 0
            self.payload.feed_data(chunk[:required], required)
            self.payload.feed_eof()
            return (True, chunk[required:])
    # WARNING: Decompyle incomplete



class DeflateBuffer:
    decompressor: Any = 'DeflateStream decompress stream and feed data into specified stream.'
    
    def __init__(self = None, out = None, encoding = None):
        self.out = out
        self.size = 0
        out.total_compressed_bytes = self.size
        self.encoding = encoding
        self._started_decoding = False
        self
        if encoding == 'br':
            if not HAS_BROTLI:
                raise ContentEncodingError('Can not decode content-encoding: brotli (br). Please install `Brotli`')
            self.decompressor = BrotliDecompressor()
            return None
        if None == 'zstd':
            if not HAS_ZSTD:
                raise ContentEncodingError('Can not decode content-encoding: zstandard (zstd). Please install `backports.zstd`')
            self.decompressor = ZSTDDecompressor()
            return None
        self.decompressor = None(encoding = encoding)

    
    def set_exception(self = None, exc = None, exc_cause = None):
        set_exception(self.out, exc, exc_cause)

    
    def feed_data(self = None, chunk = None, size = None):
        if not size:
            return None
        self.size = None, None.size += size, .size
        if self._started_decoding and self.encoding == 'deflate' and chunk[0] & 15 != 8:
            self.decompressor = ZLibDecompressor(encoding = self.encoding, suppress_deflate_header = True)
        
        try:
            chunk = self.decompressor.decompress_sync(chunk)
        except Exception:
            raise ContentEncodingError('Can not decode content-encoding: %s' % self.encoding)

        self._started_decoding = True
        if chunk:
            self.out.feed_data(chunk, len(chunk))
            return None

    
    def feed_eof(self = None):
        chunk = self.decompressor.flush()
        if chunk or self.size > 0:
            self.out.feed_data(chunk, len(chunk))
            if not self.encoding == 'deflate' and self.decompressor.eof:
                raise ContentEncodingError('deflate')
        self.out.feed_eof()

    
    def begin_http_chunk_receiving(self = None):
        self.out.begin_http_chunk_receiving()

    
    def end_http_chunk_receiving(self = None):
        self.out.end_http_chunk_receiving()


HttpRequestParserPy = HttpRequestParser
HttpResponseParserPy = HttpResponseParser
RawRequestMessagePy = RawRequestMessage
RawResponseMessagePy = RawResponseMessage

try:
    if not NO_EXTENSIONS:
        from _http_parser import HttpRequestParser, HttpResponseParser, RawRequestMessage, RawResponseMessage
        HttpRequestParserC = HttpRequestParser
        HttpResponseParserC = HttpResponseParser
        RawRequestMessageC = RawRequestMessage
        RawResponseMessageC = RawResponseMessage
        return None
    return None
except ImportError:
    return None
