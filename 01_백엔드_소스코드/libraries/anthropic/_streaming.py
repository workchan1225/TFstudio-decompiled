# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _streaming.pyc (Python 3.11)

from __future__ import annotations
import abc
import json
import inspect
import warnings
from types import TracebackType
from typing import TYPE_CHECKING, Any, Generic, TypeVar, Iterator, AsyncIterator, cast
from typing_extensions import Self, Protocol, TypeGuard, override, get_origin, runtime_checkable
import httpx
from _utils import is_dict, extract_type_var_from_base
if TYPE_CHECKING:
    from _client import Anthropic, AsyncAnthropic
_T = TypeVar('_T')

class _SyncStreamMeta(abc.ABCMeta):
    __instancecheck__ = (lambda self = None, instance = None: MessageStream = MessageStreamimport lib.streamingif isinstance(instance, MessageStream):
warnings.warn('Using `isinstance()` to check if a `MessageStream` object is an instance of `Stream` is deprecated & will be removed in the next major version', DeprecationWarning, stacklevel = 2)True)()


def Stream():
    '''Stream'''
    _decoder: 'SSEBytesDecoder' = 'Provides the core interface to iterate over a synchronous stream response.'
    
    def __init__(self = None, *, cast_to, response, client):
        self.response = response
        self._cast_to = cast_to
        self._client = client
        self._decoder = client._make_sse_decoder()
        self._iterator = self.__stream__()

    
    def __next__(self = None):
        return self._iterator.__next__()

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _iter_events(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __stream__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        self.close()

    
    def close(self = None):
        '''
        Close the response and release the connection.

        Automatically called if the response body is read to completion.
        '''
        self.response.close()


Stream = <NODE:27>(Stream, 'Stream', Generic[_T], metaclass = _SyncStreamMeta)

class _AsyncStreamMeta(abc.ABCMeta):
    __instancecheck__ = (lambda self = None, instance = None: AsyncMessageStream = AsyncMessageStreamimport lib.streamingif isinstance(instance, AsyncMessageStream):
warnings.warn('Using `isinstance()` to check if a `AsyncMessageStream` object is an instance of `AsyncStream` is deprecated & will be removed in the next major version', DeprecationWarning, stacklevel = 2)True)()


def AsyncStream():
    '''AsyncStream'''
    _decoder: 'SSEDecoder | SSEBytesDecoder' = 'Provides the core interface to iterate over an asynchronous stream response.'
    
    def __init__(self = None, *, cast_to, response, client):
        self.response = response
        self._cast_to = cast_to
        self._client = client
        self._decoder = client._make_sse_decoder()
        self._iterator = self.__stream__()

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _iter_events(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __stream__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    async def close(self = None):
        '''
        Close the response and release the connection.

        Automatically called if the response body is read to completion.
        '''
        pass
    # WARNING: Decompyle incomplete


AsyncStream = <NODE:27>(AsyncStream, 'AsyncStream', Generic[_T], metaclass = _AsyncStreamMeta)

class ServerSentEvent:
    
    def __init__(self = None, *, event, data, id, retry):
        pass
    # WARNING: Decompyle incomplete

    event = (lambda self = None: self._event)()
    id = (lambda self = None: self._id)()
    retry = (lambda self = None: self._retry)()
    data = (lambda self = None: self._data)()
    
    def json(self = None):
        return json.loads(self.data)

    __repr__ = (lambda self = None: f'''ServerSentEvent(event={self.event}, data={self.data}, id={self.id}, retry={self.retry})''')()


class SSEDecoder:
    _last_event_id: 'str | None' = 'SSEDecoder'
    
    def __init__(self = None):
        self._event = None
        self._data = []
        self._last_event_id = None
        self._retry = None

    
    def iter_bytes(self = None, iterator = None):
        '''Given an iterator that yields raw binary data, iterate over it & yield every event encountered'''
        pass
    # WARNING: Decompyle incomplete

    
    def _iter_chunks(self = None, iterator = None):
        '''Given an iterator that yields raw binary data, iterate over it and yield individual SSE chunks'''
        pass
    # WARNING: Decompyle incomplete

    
    def aiter_bytes(self = None, iterator = None):
        '''Given an iterator that yields raw binary data, iterate over it & yield every event encountered'''
        pass
    # WARNING: Decompyle incomplete

    
    def _aiter_chunks(self = None, iterator = None):
        '''Given an iterator that yields raw binary data, iterate over it and yield individual SSE chunks'''
        pass
    # WARNING: Decompyle incomplete

    
    def decode(self = None, line = None):
        pass
    # WARNING: Decompyle incomplete


SSEBytesDecoder = <NODE:12>()

def is_stream_class_type(typ = None):
