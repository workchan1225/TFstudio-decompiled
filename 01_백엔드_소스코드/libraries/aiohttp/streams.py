# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: streams.pyc (Python 3.11)

import asyncio
import collections
import warnings
from typing import Awaitable, Callable, Deque, Final, Generic, List, Optional, Tuple, TypeVar
from base_protocol import BaseProtocol
from helpers import _EXC_SENTINEL, BaseTimerContext, TimerNoop, set_exception, set_result
from log import internal_logger
__all__ = ('EMPTY_PAYLOAD', 'EofStream', 'StreamReader', 'DataQueue')
_T = TypeVar('_T')

class EofStream(Exception):
    '''eof stream indication.'''
    pass


def AsyncStreamIterator():
    '''AsyncStreamIterator'''
    __slots__ = ('read_func',)
    
    def __init__(self = None, read_func = None):
        self.read_func = read_func

    
    def __aiter__(self = None):
        return self

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete


AsyncStreamIterator = <NODE:27>(AsyncStreamIterator, 'AsyncStreamIterator', Generic[_T])

class ChunkTupleAsyncStreamIterator:
    __slots__ = ('_stream',)
    
    def __init__(self = None, stream = None):
        self._stream = stream

    
    def __aiter__(self = None):
        return self

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete



class AsyncStreamReaderMixin:
    __slots__ = ()
    
    def __aiter__(self = None):
        return AsyncStreamIterator(self.readline)

    
    def iter_chunked(self = None, n = None):
        '''Returns an asynchronous iterator that yields chunks of size n.'''
        pass
    # WARNING: Decompyle incomplete

    
    def iter_any(self = None):
        '''Yield all available data as soon as it is received.'''
        return AsyncStreamIterator(self.readany)

    
    def iter_chunks(self = None):
        '''Yield chunks of data as they are received by the server.

        The yielded objects are tuples
        of (bytes, bool) as returned by the StreamReader.readchunk method.
        '''
        return ChunkTupleAsyncStreamIterator(self)



class StreamReader(AsyncStreamReaderMixin):
    '''An enhancement of asyncio.StreamReader.

    Supports asynchronous iteration by line, chunk or as available::

        async for line in reader:
            ...
        async for chunk in reader.iter_chunked(1024):
            ...
        async for slice in reader.iter_any():
            ...

    '''
    __slots__ = ('_protocol', '_low_water', '_high_water', '_loop', '_size', '_cursor', '_http_chunk_splits', '_buffer', '_buffer_offset', '_eof', '_waiter', '_eof_waiter', '_exception', '_timer', '_eof_callbacks', '_eof_counter', 'total_bytes', 'total_compressed_bytes')
    
    def __init__(self = None, protocol = None, limit = None, *, timer, loop):
        self._protocol = protocol
        self._low_water = limit
        self._high_water = limit * 2
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        info = [
            self.__class__.__name__]
        if self._size:
            info.append('%d bytes' % self._size)
        if self._eof:
            info.append('eof')
        if self._low_water != 65536:
            info.append('low=%d high=%d' % (self._low_water, self._high_water))
        if self._waiter:
            info.append('w=%r' % self._waiter)
        if self._exception:
            info.append('e=%r' % self._exception)
        return '<%s>' % ' '.join(info)

    
    def get_read_buffer_limits(self = None):
        return (self._low_water, self._high_water)

    
    def exception(self = None):
        return self._exception

    
    def set_exception(self = None, exc = None, exc_cause = None):
        self._exception = exc
        self._eof_callbacks.clear()
        waiter = self._waiter
    # WARNING: Decompyle incomplete

    
    def on_eof(self = None, callback = None):
        if self._eof:
            
            try:
                callback()
                return None
            except Exception:
                internal_logger.exception('Exception in eof callback')
                return None
                self._eof_callbacks.append(callback)
                return None


    
    def feed_eof(self = None):
        self._eof = True
        waiter = self._waiter
    # WARNING: Decompyle incomplete

    
    def is_eof(self = None):
        """Return True if  'feed_eof' was called."""
        return self._eof

    
    def at_eof(self = None):
