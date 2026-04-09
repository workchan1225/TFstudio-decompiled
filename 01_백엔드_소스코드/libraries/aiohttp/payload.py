# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: payload.pyc (Python 3.11)

import asyncio
import enum
import io
import json
import mimetypes
import os
import sys
import warnings
from abc import ABC, abstractmethod
from collections.abc import Iterable
from itertools import chain
from typing import IO, TYPE_CHECKING, Any, Dict, Final, List, Optional, Set, TextIO, Tuple, Type, Union
from multidict import CIMultiDict
from  import hdrs
from abc import AbstractStreamWriter
from helpers import _SENTINEL, content_disposition_header, guess_filename, parse_mimetype, sentinel
from streams import StreamReader
from typedefs import JSONEncoder, _CIMultiDict
__all__ = ('PAYLOAD_REGISTRY', 'get_payload', 'payload_type', 'Payload', 'BytesPayload', 'StringPayload', 'IOBasePayload', 'BytesIOPayload', 'BufferedReaderPayload', 'TextIOPayload', 'StringIOPayload', 'JsonPayload', 'AsyncIterablePayload')
TOO_LARGE_BYTES_BODY: Final[int] = 1048576
READ_SIZE: Final[int] = 65536
_CLOSE_FUTURES: Set[asyncio.Future[None]] = set()

class LookupError(Exception):
    '''Raised when no payload factory is found for the given data type.'''
    pass


class Order(enum.Enum, str):
    normal = 'normal'
    try_first = 'try_first'
    try_last = 'try_last'


def get_payload(data = None, *args, **kwargs):
    pass
# WARNING: Decompyle incomplete


def register_payload(factory = None, type = None, *, order):
    PAYLOAD_REGISTRY.register(factory, type, order = order)


class payload_type:
    
    def __init__(self = None, type = None, *, order):
        self.type = type
        self.order = order

    
    def __call__(self = None, factory = None):
        register_payload(factory, self.type, order = self.order)
        return factory


PayloadType = Type['Payload']
_PayloadRegistryItem = Tuple[(PayloadType, Any)]

class PayloadRegistry:
    '''Payload registry.

    note: we need zope.interface for more efficient adapter search
    '''
    __slots__ = ('_first', '_normal', '_last', '_normal_lookup')
    
    def __init__(self = None):
        self._first = []
        self._normal = []
        self._last = []
        self._normal_lookup = { }

    
    def get(self = None, data = None, *, _CHAIN, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def register(self = None, factory = None, type = None, *, order):
        if order is Order.try_first:
            self._first.append((factory, type))
            return None
        if None is Order.normal:
            self._normal.append((factory, type))
            if isinstance(type, Iterable):
                for t in type:
                    self._normal_lookup[t] = factory
                    return None
                    self._normal_lookup[type] = factory
                    return None
                    if order is Order.try_last:
                        self._last.append((factory, type))
                        return None
                    raise None(f'''Unsupported order {order!r}''')



class Payload(ABC):
    _default_content_type: str = 'application/octet-stream'
    _size: Optional[int] = None
    _consumed: bool = False
    _autoclose: bool = False
    
    def __init__(self, value = None, headers = None, content_type = None, filename = (None, sentinel, None, None), encoding = ('value', Any, 'headers', Optional[Union[(_CIMultiDict, Dict[(str, str)], Iterable[Tuple[(str, str)]])]], 'content_type', Union[(str, None, _SENTINEL)], 'filename', Optional[str], 'encoding', Optional[str], 'kwargs', Any, 'return', None), **kwargs):
        self._encoding = encoding
        self._filename = filename
        self._headers = CIMultiDict()
        self._value = value
    # WARNING: Decompyle incomplete

    size = (lambda self = None: self._size)()
    filename = (lambda self = None: self._filename)()
    headers = (lambda self = None: self._headers)()
    _binary_headers = (lambda self = None: (lambda .0: [ k + ': ' + v + '\r\n' for k, v in .0 ])(self.headers.items()()).encode('utf-8') + b'\r\n'
)()
    encoding = (lambda self = None: self._encoding)()
    content_type = (lambda self = None: self._headers[hdrs.CONTENT_TYPE])()
    consumed = (lambda self = None: self._consumed)()
    autoclose = (lambda self = None: self._autoclose)()
    
    def set_content_disposition(self = None, disptype = None, quote_fields = None, _charset = (True, 'utf-8'), **params):
        '''Sets ``Content-Disposition`` header.'''
        pass
    # WARNING: Decompyle incomplete

    decode = (lambda self = None, encoding = None, errors = abstractmethod: pass)()
    write = (lambda self = None, writer = None: pass# WARNING: Decompyle incomplete
)()
    
    async def write_with_length(self = None, writer = None, content_length = None):
        """
        Write payload with a specific content length constraint.

        Args:
            writer: An AbstractStreamWriter instance that handles the actual writing
            content_length: Maximum number of bytes to write (None for unlimited)

        This method allows writing payload content with a specific length constraint,
        which is particularly useful for HTTP responses with Content-Length header.

        Note:
            This is the base implementation that provides backwards compatibility
            for subclasses that don't override this method. Specific payload types
            should override this method to implement proper length-constrained writing.

        """
        pass
    # WARNING: Decompyle incomplete

    
    async def as_bytes(self = None, encoding = None, errors = None):
        '''
        Return bytes representation of the value.

        This is a convenience method that calls decode() and encodes the result
        to bytes using the specified encoding.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _close(self = None):
        '''
        Async safe synchronous close operations for backwards compatibility.

        This method exists only for backwards compatibility with code that
        needs to clean up payloads synchronously. In the future, we will
        drop this method and only support the async close() method.

        WARNING: This method must be safe to call from within the event loop
        without blocking. Subclasses should not perform any blocking I/O here.

        WARNING: This method must be called from within an event loop for
        certain payload types (e.g., IOBasePayload). Calling it outside an
        event loop may raise RuntimeError.
        '''
        pass

    
    async def close(self = None):
        '''
        Close the payload if it holds any resources.

        IMPORTANT: This method must not await anything that might not finish
        immediately, as it may be called during cleanup/cancellation. Schedule
        any long-running operations without awaiting them.

        In the future, this will be the only close method supported.
        '''
        pass
    # WARNING: Decompyle incomplete



class BytesPayload(Payload):
    pass
# WARNING: Decompyle incomplete


class StringPayload(BytesPayload):
    pass
# WARNING: Decompyle incomplete


class StringIOPayload(StringPayload):
    pass
# WARNING: Decompyle incomplete


class IOBasePayload(Payload):
    pass
# WARNING: Decompyle incomplete


class TextIOPayload(IOBasePayload):
    pass
# WARNING: Decompyle incomplete


class BytesIOPayload(IOBasePayload):
    pass
# WARNING: Decompyle incomplete


class BufferedReaderPayload(IOBasePayload):
    _value: io.BufferedIOBase = 'BufferedReaderPayload'
    
    def decode(self = None, encoding = None, errors = None):
        self._set_or_restore_start_position()
        return self._value.read().decode(encoding, errors)



class JsonPayload(BytesPayload):
    pass
# WARNING: Decompyle incomplete


class AsyncIterablePayload(Payload):
    pass
# WARNING: Decompyle incomplete


class StreamReaderPayload(AsyncIterablePayload):
    pass
# WARNING: Decompyle incomplete

PAYLOAD_REGISTRY = PayloadRegistry()
PAYLOAD_REGISTRY.register(BytesPayload, (bytes, bytearray, memoryview))
PAYLOAD_REGISTRY.register(StringPayload, str)
PAYLOAD_REGISTRY.register(StringIOPayload, io.StringIO)
PAYLOAD_REGISTRY.register(TextIOPayload, io.TextIOBase)
PAYLOAD_REGISTRY.register(BytesIOPayload, io.BytesIO)
PAYLOAD_REGISTRY.register(BufferedReaderPayload, (io.BufferedReader, io.BufferedRandom))
PAYLOAD_REGISTRY.register(IOBasePayload, io.IOBase)
PAYLOAD_REGISTRY.register(StreamReaderPayload, StreamReader)
PAYLOAD_REGISTRY.register(AsyncIterablePayload, AsyncIterable, order = Order.try_last)
