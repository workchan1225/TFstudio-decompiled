# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _content.pyc (Python 3.11)

from __future__ import annotations
import inspect
import warnings
from json import dumps as json_dumps
from typing import Any, AsyncIterable, AsyncIterator, Iterable, Iterator, Mapping
from urllib.parse import urlencode
from _exceptions import StreamClosed, StreamConsumed
from _multipart import MultipartStream
from _types import AsyncByteStream, RequestContent, RequestData, RequestFiles, ResponseContent, SyncByteStream
from _utils import peek_filelike_length, primitive_value_to_str
__all__ = [
    'ByteStream']

class ByteStream(SyncByteStream, AsyncByteStream):
    
    def __init__(self = None, stream = None):
        self._stream = stream

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete



class IteratorByteStream(SyncByteStream):
    CHUNK_SIZE = 65536
    
    def __init__(self = None, stream = None):
        self._stream = stream
        self._is_stream_consumed = False
        self._is_generator = inspect.isgenerator(stream)

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete



class AsyncIteratorByteStream(AsyncByteStream):
    CHUNK_SIZE = 65536
    
    def __init__(self = None, stream = None):
        self._stream = stream
        self._is_stream_consumed = False
        self._is_generator = inspect.isasyncgen(stream)

    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete



class UnattachedStream(SyncByteStream, AsyncByteStream):
    '''
    If a request or response is serialized using pickle, then it is no longer
    attached to a stream for I/O purposes. Any stream operations should result
    in `httpx.StreamClosed`.
    '''
    
    def __iter__(self = None):
        raise StreamClosed()

    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete



def encode_content(content = None):
    if isinstance(content, (bytes, str)):
        body = content.encode('utf-8') if isinstance(content, str) else content
        content_length = len(body)
        headers = {
            'Content-Length': str(content_length) } if body else { }
        return (headers, ByteStream(body))
# WARNING: Decompyle incomplete


def encode_urlencoded_data(data = None):
    pass
# WARNING: Decompyle incomplete


def encode_multipart_data(data = None, files = None, boundary = None):
    multipart = MultipartStream(data = data, files = files, boundary = boundary)
    headers = multipart.get_headers()
    return (headers, multipart)


def encode_text(text = None):
    body = text.encode('utf-8')
    content_length = str(len(body))
    content_type = 'text/plain; charset=utf-8'
    headers = {
        'Content-Length': content_length,
        'Content-Type': content_type }
    return (headers, ByteStream(body))


def encode_html(html = None):
    body = html.encode('utf-8')
    content_length = str(len(body))
    content_type = 'text/html; charset=utf-8'
    headers = {
        'Content-Length': content_length,
        'Content-Type': content_type }
    return (headers, ByteStream(body))


def encode_json(json = None):
    body = json_dumps(json, ensure_ascii = False, separators = (',', ':'), allow_nan = False).encode('utf-8')
    content_length = str(len(body))
    content_type = 'application/json'
    headers = {
        'Content-Length': content_length,
        'Content-Type': content_type }
    return (headers, ByteStream(body))


def encode_request(content = None, data = None, files = None, json = (None, None, None, None, None), boundary = ('content', 'RequestContent | None', 'data', 'RequestData | None', 'files', 'RequestFiles | None', 'json', 'Any | None', 'boundary', 'bytes | None', 'return', 'tuple[dict[str, str], SyncByteStream | AsyncByteStream]')):
    '''
    Handles encoding the given `content`, `data`, `files`, and `json`,
    returning a two-tuple of (<headers>, <stream>).
    '''
    pass
# WARNING: Decompyle incomplete


def encode_response(content = None, text = None, html = None, json = (None, None, None, None)):
    '''
    Handles encoding the given `content`, returning a two-tuple of
    (<headers>, <stream>).
    '''
    pass
# WARNING: Decompyle incomplete
