# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _legacy_response.pyc (Python 3.11)

from __future__ import annotations
import os
import inspect
import logging
import datetime
import functools
from typing import TYPE_CHECKING, Any, Union, Generic, TypeVar, Callable, Iterator, AsyncIterator, cast, overload
from typing_extensions import Awaitable, ParamSpec, override, deprecated, get_origin
import anyio
import httpx
import pydantic
from _types import NoneType
from _utils import is_given, extract_type_arg, is_annotated_type, is_type_alias_type
from _models import BaseModel, is_basemodel, add_request_id
from _constants import RAW_RESPONSE_HEADER
from _streaming import Stream, AsyncStream, is_stream_class_type, extract_stream_chunk_type
from _exceptions import APIResponseValidationError
if TYPE_CHECKING:
    from _models import FinalRequestOptions
    from _base_client import BaseClient
P = ParamSpec('P')
R = TypeVar('R')
_T = TypeVar('_T')
log: 'logging.Logger' = logging.getLogger(__name__)

def LegacyAPIResponse():
    '''LegacyAPIResponse'''
    retries_taken: 'int' = 'This is a legacy class as it will be replaced by `APIResponse`\n    and `AsyncAPIResponse` in the `_response.py` file in the next major\n    release.\n\n    For the sync client this will mostly be the same with the exception\n    of `content` & `text` will be methods instead of properties. In the\n    async client, all methods will be async.\n\n    A migration script will be provided & the migration in general should\n    be smooth.\n    '
    
    def __init__(self = None, *, raw, cast_to, client, stream, stream_cls, options, retries_taken):
        self._cast_to = cast_to
        self._client = client
        self._parsed_by_type = { }
        self._stream = stream
        self._stream_cls = stream_cls
        self._options = options
        self.http_response = raw
        self.retries_taken = retries_taken

    request_id = (lambda self = None: self.http_response.headers.get('x-request-id'))()
    parse = (lambda self = None, *, to: pass)()
    parse = (lambda self = None: pass)()
    
    def parse(self = None, *, to):
        """Returns the rich python representation of this response's data.

        NOTE: For the async client: this will become a coroutine in the next major version.

        For lower-level control, see `.read()`, `.json()`, `.iter_bytes()`.

        You can customise the type that the response is parsed into through
        the `to` argument, e.g.

        ```py
        from openai import BaseModel


        class MyModel(BaseModel):
            foo: str


        obj = response.parse(to=MyModel)
        print(obj.foo)
        ```

        We support parsing:
          - `BaseModel`
          - `dict`
          - `list`
          - `Union`
          - `str`
          - `int`
          - `float`
          - `httpx.Response`
        """
        pass
    # WARNING: Decompyle incomplete

    headers = (lambda self = None: self.http_response.headers)()
    http_request = (lambda self = None: self.http_response.request)()
    status_code = (lambda self = None: self.http_response.status_code)()
    url = (lambda self = None: self.http_response.url)()
    method = (lambda self = None: self.http_request.method)()
    content = (lambda self = None: self.http_response.content)()
    text = (lambda self = None: self.http_response.text)()
    http_version = (lambda self = None: self.http_response.http_version)()
    is_closed = (lambda self = None: self.http_response.is_closed)()
    elapsed = (lambda self = None: self.http_response.elapsed)()
    
    def _parse(self = None, *, to):
        pass
    # WARNING: Decompyle incomplete

    __repr__ = (lambda self = None: f'''<APIResponse [{self.status_code} {self.http_response.reason_phrase}] type={self._cast_to}>''')()

LegacyAPIResponse = <NODE:27>(LegacyAPIResponse, 'LegacyAPIResponse', Generic[R])

class MissingStreamClassError(TypeError):
    pass
# WARNING: Decompyle incomplete


def to_raw_response_wrapper(func = None):
    '''Higher order function that takes one of our bound API methods and wraps it
    to support returning the raw `APIResponse` object directly.
    '''
    pass
# WARNING: Decompyle incomplete


def async_to_raw_response_wrapper(func = None):
    '''Higher order function that takes one of our bound API methods and wraps it
    to support returning the raw `APIResponse` object directly.
    '''
    pass
# WARNING: Decompyle incomplete


class HttpxBinaryResponseContent:
    response: 'httpx.Response' = 'HttpxBinaryResponseContent'
    
    def __init__(self = None, response = None):
        self.response = response

    content = (lambda self = None: self.response.content)()
    text = (lambda self = None: self.response.text)()
    encoding = (lambda self = None: self.response.encoding)()
    charset_encoding = (lambda self = None: self.response.charset_encoding)()
    
    def json(self = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def read(self = None):
        return self.response.read()

    
    def iter_bytes(self = None, chunk_size = None):
        return self.response.iter_bytes(chunk_size)

    
    def iter_text(self = None, chunk_size = None):
        return self.response.iter_text(chunk_size)

    
    def iter_lines(self = None):
        return self.response.iter_lines()

    
    def iter_raw(self = None, chunk_size = None):
        return self.response.iter_raw(chunk_size)

    
    def write_to_file(self = None, file = None):
        """Write the output to the given file.

        Accepts a filename or any path-like object, e.g. pathlib.Path

        Note: if you want to stream the data to the file instead of writing
        all at once then you should use `.with_streaming_response` when making
        the API request, e.g. `client.with_streaming_response.foo().stream_to_file('my_filename.txt')`
        """
        f = open(file, mode = 'wb')
        for data in self.response.iter_bytes():
            f.write(data)
            None(None, None)
            return None
            with None:
                if not None:
                    pass

    stream_to_file = (lambda self = None, file = None, *, chunk_size, f = None: f = open(file, mode = 'wb')for data in self.response.iter_bytes(chunk_size):
f.write(data)None(None, None)Nonewith None:
if not None:
pass)()
    
    def close(self = None):
        return self.response.close()

    
    async def aread(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def aiter_bytes(self = None, chunk_size = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def aiter_text(self = None, chunk_size = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def aiter_lines(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def aiter_raw(self = None, chunk_size = None):
        pass
    # WARNING: Decompyle incomplete

    astream_to_file = (lambda self = None, file = None, *, chunk_size, path = None: pass# WARNING: Decompyle incomplete
)()
    
    async def aclose(self = None):
        pass
    # WARNING: Decompyle incomplete
