# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _response.pyc (Python 3.11)

from __future__ import annotations
import os
import inspect
import logging
import datetime
import functools
from types import TracebackType
from typing import TYPE_CHECKING, Any, Union, Generic, TypeVar, Callable, Iterator, AsyncIterator, cast, overload
from typing_extensions import Awaitable, ParamSpec, override, get_origin
import anyio
import httpx
import pydantic
from _types import NoneType
from _utils import is_given, extract_type_arg, is_annotated_type, is_type_alias_type, extract_type_var_from_base
from _models import BaseModel, is_basemodel, add_request_id
from _constants import RAW_RESPONSE_HEADER, OVERRIDE_CAST_TO_HEADER
from _streaming import Stream, AsyncStream, is_stream_class_type, extract_stream_chunk_type
from _exceptions import OpenAIError, APIResponseValidationError
if TYPE_CHECKING:
    from _models import FinalRequestOptions
    from _base_client import BaseClient
P = ParamSpec('P')
R = TypeVar('R')
_T = TypeVar('_T')
_APIResponseT = TypeVar('_APIResponseT', bound = 'APIResponse[Any]')
_AsyncAPIResponseT = TypeVar('_AsyncAPIResponseT', bound = 'AsyncAPIResponse[Any]')
log: 'logging.Logger' = logging.getLogger(__name__)

def BaseAPIResponse():
    '''BaseAPIResponse'''
    retries_taken: 'int' = 'BaseAPIResponse'
    
    def __init__(self = None, *, raw, cast_to, client, stream, stream_cls, options, retries_taken):
        self._cast_to = cast_to
        self._client = client
        self._parsed_by_type = { }
        self._is_sse_stream = stream
        self._stream_cls = stream_cls
        self._options = options
        self.http_response = raw
        self.retries_taken = retries_taken

    headers = (lambda self = None: self.http_response.headers)()
    http_request = (lambda self = None: self.http_response.request)()
    status_code = (lambda self = None: self.http_response.status_code)()
    url = (lambda self = None: self.http_response.url)()
    method = (lambda self = None: self.http_request.method)()
    http_version = (lambda self = None: self.http_response.http_version)()
    elapsed = (lambda self = None: self.http_response.elapsed)()
    is_closed = (lambda self = None: self.http_response.is_closed)()
    __repr__ = (lambda self = None: f'''<{self.__class__.__name__} [{self.status_code} {self.http_response.reason_phrase}] type={self._cast_to}>''')()
    
    def _parse(self = None, *, to):
        pass
    # WARNING: Decompyle incomplete


BaseAPIResponse = <NODE:27>(BaseAPIResponse, 'BaseAPIResponse', Generic[R])

def APIResponse():
    '''APIResponse'''
    request_id = (lambda self = None: self.http_response.headers.get('x-request-id'))()
    parse = (lambda self = None, *, to: pass)()
    parse = (lambda self = None: pass)()
    
    def parse(self = None, *, to):
        """Returns the rich python representation of this response's data.

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

    
    def read(self = None):
        '''Read and return the binary response content.'''
        
        try:
            return self.http_response.read()
        except httpx.StreamConsumed:
            exc = None
            raise StreamAlreadyConsumed(), exc
            exc = None
            del exc


    
    def text(self = None):
        '''Read and decode the response content into a string.'''
        self.read()
        return self.http_response.text

    
    def json(self = None):
        '''Read and decode the JSON response content.'''
        self.read()
        return self.http_response.json()

    
    def close(self = None):
        '''Close the response and release the connection.

        Automatically called if the response body is read to completion.
        '''
        self.http_response.close()

    
    def iter_bytes(self = None, chunk_size = None):
        '''
        A byte-iterator over the decoded response content.

        This automatically handles gzip, deflate and brotli encoded responses.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def iter_text(self = None, chunk_size = None):
        """A str-iterator over the decoded response content
        that handles both gzip, deflate, etc but also detects the content's
        string encoding.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def iter_lines(self = None):
        '''Like `iter_text()` but will only yield chunks for each line'''
        pass
    # WARNING: Decompyle incomplete


APIResponse = <NODE:27>(APIResponse, 'APIResponse', BaseAPIResponse[R])

def AsyncAPIResponse():
    '''AsyncAPIResponse'''
    request_id = (lambda self = None: self.http_response.headers.get('x-request-id'))()
    parse = (lambda self = None, *, to: pass# WARNING: Decompyle incomplete
)()
    parse = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    async def parse(self = None, *, to):
        """Returns the rich python representation of this response's data.

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
          - `httpx.Response`
        """
        pass
    # WARNING: Decompyle incomplete

    
    async def read(self = None):
        '''Read and return the binary response content.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def text(self = None):
        '''Read and decode the response content into a string.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def json(self = None):
        '''Read and decode the JSON response content.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def close(self = None):
        '''Close the response and release the connection.

        Automatically called if the response body is read to completion.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def iter_bytes(self = None, chunk_size = None):
        '''
        A byte-iterator over the decoded response content.

        This automatically handles gzip, deflate and brotli encoded responses.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def iter_text(self = None, chunk_size = None):
        """A str-iterator over the decoded response content
        that handles both gzip, deflate, etc but also detects the content's
        string encoding.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def iter_lines(self = None):
        '''Like `iter_text()` but will only yield chunks for each line'''
        pass
    # WARNING: Decompyle incomplete


AsyncAPIResponse = <NODE:27>(AsyncAPIResponse, 'AsyncAPIResponse', BaseAPIResponse[R])

def BinaryAPIResponse():
    '''BinaryAPIResponse'''
    __doc__ = 'Subclass of APIResponse providing helpers for dealing with binary data.\n\n    Note: If you want to stream the response data instead of eagerly reading it\n    all at once then you should use `.with_streaming_response` when making\n    the API request, e.g. `.with_streaming_response.get_binary_response()`\n    '
    
    def write_to_file(self = None, file = None):
        '''Write the output to the given file.

        Accepts a filename or any path-like object, e.g. pathlib.Path

        Note: if you want to stream the data to the file instead of writing
        all at once then you should use `.with_streaming_response` when making
        the API request, e.g. `.with_streaming_response.get_binary_response()`
        '''
        f = open(file, mode = 'wb')
        for data in self.iter_bytes():
            f.write(data)
            None(None, None)
            return None
            with None:
                if not None:
                    pass


BinaryAPIResponse = <NODE:27>(BinaryAPIResponse, 'BinaryAPIResponse', APIResponse[bytes])

def AsyncBinaryAPIResponse():
    '''AsyncBinaryAPIResponse'''
    __doc__ = 'Subclass of APIResponse providing helpers for dealing with binary data.\n\n    Note: If you want to stream the response data instead of eagerly reading it\n    all at once then you should use `.with_streaming_response` when making\n    the API request, e.g. `.with_streaming_response.get_binary_response()`\n    '
    
    async def write_to_file(self = None, file = None):
        '''Write the output to the given file.

        Accepts a filename or any path-like object, e.g. pathlib.Path

        Note: if you want to stream the data to the file instead of writing
        all at once then you should use `.with_streaming_response` when making
        the API request, e.g. `.with_streaming_response.get_binary_response()`
        '''
        pass
    # WARNING: Decompyle incomplete


AsyncBinaryAPIResponse = <NODE:27>(AsyncBinaryAPIResponse, 'AsyncBinaryAPIResponse', AsyncAPIResponse[bytes])

def StreamedBinaryAPIResponse():
    '''StreamedBinaryAPIResponse'''
    
    def stream_to_file(self = None, file = None, *, chunk_size):
        '''Streams the output to the given file.

        Accepts a filename or any path-like object, e.g. pathlib.Path
        '''
        f = open(file, mode = 'wb')
        for data in self.iter_bytes(chunk_size):
            f.write(data)
            None(None, None)
            return None
            with None:
                if not None:
                    pass


StreamedBinaryAPIResponse = <NODE:27>(StreamedBinaryAPIResponse, 'StreamedBinaryAPIResponse', APIResponse[bytes])

def AsyncStreamedBinaryAPIResponse():
    '''AsyncStreamedBinaryAPIResponse'''
    
    async def stream_to_file(self = None, file = None, *, chunk_size):
        '''Streams the output to the given file.

        Accepts a filename or any path-like object, e.g. pathlib.Path
        '''
        pass
    # WARNING: Decompyle incomplete


AsyncStreamedBinaryAPIResponse = <NODE:27>(AsyncStreamedBinaryAPIResponse, 'AsyncStreamedBinaryAPIResponse', AsyncAPIResponse[bytes])

class MissingStreamClassError(TypeError):
    pass
# WARNING: Decompyle incomplete


class StreamAlreadyConsumed(OpenAIError):
    pass
# WARNING: Decompyle incomplete


def ResponseContextManager():
    '''ResponseContextManager'''
    __doc__ = 'Context manager for ensuring that a request is not made\n    until it is entered and that the response will always be closed\n    when the context manager exits\n    '
    
    def __init__(self = None, request_func = None):
        self._request_func = request_func
        self._ResponseContextManager__response = None

    
    def __enter__(self = None):
        self._ResponseContextManager__response = self._request_func()
        return self._ResponseContextManager__response

    
    def __exit__(self = None, exc_type = None, exc = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete


ResponseContextManager = <NODE:27>(ResponseContextManager, 'ResponseContextManager', Generic[_APIResponseT])

def AsyncResponseContextManager():
    '''AsyncResponseContextManager'''
    __doc__ = 'Context manager for ensuring that a request is not made\n    until it is entered and that the response will always be closed\n    when the context manager exits\n    '
    
    def __init__(self = None, api_request = None):
        self._api_request = api_request
        self._AsyncResponseContextManager__response = None

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete


AsyncResponseContextManager = <NODE:27>(AsyncResponseContextManager, 'AsyncResponseContextManager', Generic[_AsyncAPIResponseT])

def to_streamed_response_wrapper(func = None):
    '''Higher order function that takes one of our bound API methods and wraps it
    to support streaming and returning the raw `APIResponse` object directly.
    '''
    pass
# WARNING: Decompyle incomplete


def async_to_streamed_response_wrapper(func = None):
    '''Higher order function that takes one of our bound API methods and wraps it
    to support streaming and returning the raw `APIResponse` object directly.
    '''
    pass
# WARNING: Decompyle incomplete


def to_custom_streamed_response_wrapper(func = None, response_cls = None):
    '''Higher order function that takes one of our bound API methods and an `APIResponse` class
    and wraps the method to support streaming and returning the given response class directly.

    Note: the given `response_cls` *must* be concrete, e.g. `class BinaryAPIResponse(APIResponse[bytes])`
    '''
    pass
# WARNING: Decompyle incomplete


def async_to_custom_streamed_response_wrapper(func = None, response_cls = None):
    '''Higher order function that takes one of our bound API methods and an `APIResponse` class
    and wraps the method to support streaming and returning the given response class directly.

    Note: the given `response_cls` *must* be concrete, e.g. `class BinaryAPIResponse(APIResponse[bytes])`
    '''
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


def to_custom_raw_response_wrapper(func = None, response_cls = None):
    '''Higher order function that takes one of our bound API methods and an `APIResponse` class
    and wraps the method to support returning the given response class directly.

    Note: the given `response_cls` *must* be concrete, e.g. `class BinaryAPIResponse(APIResponse[bytes])`
    '''
    pass
# WARNING: Decompyle incomplete


def async_to_custom_raw_response_wrapper(func = None, response_cls = None):
    '''Higher order function that takes one of our bound API methods and an `APIResponse` class
    and wraps the method to support returning the given response class directly.

    Note: the given `response_cls` *must* be concrete, e.g. `class BinaryAPIResponse(APIResponse[bytes])`
    '''
    pass
# WARNING: Decompyle incomplete


def extract_response_type(typ = None):
    '''Given a type like `APIResponse[T]`, returns the generic type variable `T`.

    This also handles the case where a concrete subclass is given, e.g.
    ```py
    class MyResponse(APIResponse[bytes]):
        ...

    extract_response_type(MyResponse) -> bytes
    ```
    '''
    return extract_type_var_from_base(typ, generic_bases = cast('tuple[type, ...]', (BaseAPIResponse, APIResponse, AsyncAPIResponse)), index = 0)
