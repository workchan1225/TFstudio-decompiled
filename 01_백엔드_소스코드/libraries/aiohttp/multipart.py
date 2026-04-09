# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: multipart.pyc (Python 3.11)

import base64
import binascii
import json
import re
import sys
import uuid
import warnings
from collections import deque
from collections.abc import Mapping, Sequence
from types import TracebackType
from typing import TYPE_CHECKING, Any, Deque, Dict, Iterator, List, Optional, Tuple, Type, Union, cast
from urllib.parse import parse_qsl, unquote, urlencode
from multidict import CIMultiDict, CIMultiDictProxy
from compression_utils import ZLibCompressor, ZLibDecompressor
from hdrs import CONTENT_DISPOSITION, CONTENT_ENCODING, CONTENT_LENGTH, CONTENT_TRANSFER_ENCODING, CONTENT_TYPE
from helpers import CHAR, TOKEN, parse_mimetype, reify
from http import HeadersParser
from log import internal_logger
from payload import JsonPayload, LookupError, Order, Payload, StringPayload, get_payload, payload_type
from streams import StreamReader
if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing import TypeVar
    Self = TypeVar('Self', bound = 'BodyPartReader')
__all__ = ('MultipartReader', 'MultipartWriter', 'BodyPartReader', 'BadContentDispositionHeader', 'BadContentDispositionParam', 'parse_content_disposition', 'content_disposition_filename')
if TYPE_CHECKING:
    from client_reqrep import ClientResponse

class BadContentDispositionHeader(RuntimeWarning):
    pass


class BadContentDispositionParam(RuntimeWarning):
    pass


def parse_content_disposition(header = None):
    pass
# WARNING: Decompyle incomplete


def content_disposition_filename(params = None, name = None):
    pass
# WARNING: Decompyle incomplete


class MultipartResponseWrapper:
    '''Wrapper around the MultipartReader.

    It takes care about
    underlying connection and close it when it needs in.
    '''
    
    def __init__(self = None, resp = None, stream = None):
        self.resp = resp
        self.stream = stream

    
    def __aiter__(self = None):
        return self

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def at_eof(self = None):
        '''Returns True when all response data had been read.'''
        return self.resp.content.at_eof()

    
    async def next(self = None):
        '''Emits next multipart reader object.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def release(self = None):
        '''Release the connection gracefully.

        All remaining content is read to the void.
        '''
        pass
    # WARNING: Decompyle incomplete



class BodyPartReader:
    '''Multipart reader for single body part.'''
    chunk_size = 8192
    
    def __init__(self = None, boundary = None, headers = None, content = None, *, subtype, default_charset):
        self.headers = headers
        self._boundary = boundary
        self._boundary_len = len(boundary) + 2
        self._content = content
        self._default_charset = default_charset
        self._at_eof = False
        self._is_form_data = subtype == 'form-data'
        length = None if self._is_form_data else self.headers.get(CONTENT_LENGTH, None)
    # WARNING: Decompyle incomplete

    
    def __aiter__(self = None):
        return self

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def next(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def read(self = None, *, decode):
        '''Reads body part data.

        decode: Decodes data following by encoding
                method from Content-Encoding header. If it missed
                data remains untouched
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def read_chunk(self = None, size = None):
        '''Reads body part content chunk of the specified size.

        size: chunk size
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _read_chunk_from_length(self = None, size = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def _read_chunk_from_stream(self = None, size = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def readline(self = None):
        '''Reads body part by line by line.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def release(self = None):
        '''Like read(), but reads all the data to the void.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def text(self = None, *, encoding):
        '''Like read(), but assumes that body part contains text data.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def json(self = None, *, encoding):
        '''Like read(), but assumes that body parts contains JSON data.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def form(self = None, *, encoding):
        '''Like read(), but assumes that body parts contain form urlencoded data.'''
        pass
    # WARNING: Decompyle incomplete

    
    def at_eof(self = None):
        '''Returns True if the boundary was reached or False otherwise.'''
        return self._at_eof

    
    def decode(self = None, data = None):
        '''Decodes data.

        Decoding is done according the specified Content-Encoding
        or Content-Transfer-Encoding headers value.
        '''
        if CONTENT_TRANSFER_ENCODING in self.headers:
            data = self._decode_content_transfer(data)
        if self._is_form_data and CONTENT_ENCODING in self.headers:
            return self._decode_content(data)

    
    def _decode_content(self = None, data = None):
        encoding = self.headers.get(CONTENT_ENCODING, '').lower()
        if encoding == 'identity':
            return data
        if None in frozenset({'gzip', 'deflate'}):
            return ZLibDecompressor(encoding = encoding, suppress_deflate_header = True).decompress_sync(data)
        raise None(f'''unknown content encoding: {encoding}''')

    
    def _decode_content_transfer(self = None, data = None):
        encoding = self.headers.get(CONTENT_TRANSFER_ENCODING, '').lower()
        if encoding == 'base64':
            return base64.b64decode(data)
        if None == 'quoted-printable':
            return binascii.a2b_qp(data)
        if None in ('binary', '8bit', '7bit'):
            return data
        raise None(f'''unknown content transfer encoding: {encoding}''')

    
    def get_charset(self = None, default = None):
