# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: queue.pyc (Python 3.11)

"""An adaptation of Py2.3/2.4's Queue module which supports reentrant
behavior, using RLock instead of Lock for its mutex object.  The
Queue object is used exclusively by the sqlalchemy.pool.QueuePool
class.

This is to support the connection pool's usage of weakref callbacks to return
connections to the underlying Queue, which can in extremely
rare cases be invoked within the ``get()`` method of the Queue itself,
producing a ``put()`` inside the ``get()`` and therefore a reentrant
condition.

"""
from __future__ import annotations
import asyncio
from collections import deque
import threading
from time import time as _time
import typing
from typing import Any
from typing import Awaitable
from typing import Deque
from typing import Generic
from typing import Optional
from typing import TypeVar
from concurrency import await_fallback
from concurrency import await_only
from langhelpers import memoized_property
_T = TypeVar('_T', bound = Any)
__all__ = [
    'Empty',
    'Full',
    'Queue']

class Empty(Exception):
    '''Exception raised by Queue.get(block=0)/get_nowait().'''
    pass


class Full(Exception):
    '''Exception raised by Queue.put(block=0)/put_nowait().'''
    pass


def QueueCommon():
    '''QueueCommon'''
    use_lifo: 'bool' = 'QueueCommon'
    
    def __init__(self = None, maxsize = None, use_lifo = None):
        pass

    
    def empty(self = None):
        raise NotImplementedError()

    
    def full(self = None):
        raise NotImplementedError()

    
    def qsize(self = None):
        raise NotImplementedError()

    
    def put_nowait(self = None, item = None):
        raise NotImplementedError()

    
    def put(self = None, item = None, block = None, timeout = (True, None)):
        raise NotImplementedError()

    
    def get_nowait(self = None):
        raise NotImplementedError()

    
    def get(self = None, block = None, timeout = None):
        raise NotImplementedError()


QueueCommon = <NODE:27>(QueueCommon, 'QueueCommon', Generic[_T])

def Queue():
    '''Queue'''
    queue: 'Deque[_T]' = 'Queue'
    
    def __init__(self = None, maxsize = None, use_lifo = None):
        '''Initialize a queue object with a given maximum size.

        If `maxsize` is <= 0, the queue size is infinite.

        If `use_lifo` is True, this Queue acts like a Stack (LIFO).
        '''
        self._init(maxsize)
        self.mutex = threading.RLock()
        self.not_empty = threading.Condition(self.mutex)
        self.not_full = threading.Condition(self.mutex)
        self.use_lifo = use_lifo

    
    def qsize(self = None):
        '''Return the approximate size of the queue (not reliable!).'''
        self.mutex
        None(None, None)
        return 
        with None:
            if not None, self._qsize():
                pass

    
    def empty(self = None):
        '''Return True if the queue is empty, False otherwise (not
        reliable!).'''
        self.mutex
        None(None, None)
        return 
        with None:
            if not None, self._empty():
                pass

    
    def full(self = None):
        '''Return True if the queue is full, False otherwise (not
        reliable!).'''
        self.mutex
        None(None, None)
        return 
        with None:
            if not None, self._full():
                pass

    
    def put(self = None, item = None, block = None, timeout = (True, None)):
        '''Put an item into the queue.

        If optional args `block` is True and `timeout` is None (the
        default), block if necessary until a free slot is
        available. If `timeout` is a positive number, it blocks at
        most `timeout` seconds and raises the ``Full`` exception if no
        free slot was available within that time.  Otherwise (`block`
        is false), put an item on the queue if a free slot is
        immediately available, else raise the ``Full`` exception
        (`timeout` is ignored in that case).
        '''
        self.not_full
        if not block:
            if self._full():
                raise Full
    # WARNING: Decompyle incomplete

    
    def put_nowait(self = None, item = None):
        '''Put an item into the queue without blocking.

        Only enqueue the item if a free slot is immediately available.
        Otherwise raise the ``Full`` exception.
        '''
        return self.put(item, False)

    
    def get(self = None, block = None, timeout = None):
        '''Remove and return an item from the queue.

        If optional args `block` is True and `timeout` is None (the
        default), block if necessary until an item is available. If
        `timeout` is a positive number, it blocks at most `timeout`
        seconds and raises the ``Empty`` exception if no item was
        available within that time.  Otherwise (`block` is false),
        return an item if one is immediately available, else raise the
        ``Empty`` exception (`timeout` is ignored in that case).

        '''
        self.not_empty
        if not block:
            if self._empty():
                raise Empty
    # WARNING: Decompyle incomplete

    
    def get_nowait(self = None):
        '''Remove and return an item from the queue without blocking.

        Only get an item if one is immediately available. Otherwise
        raise the ``Empty`` exception.
        '''
        return self.get(False)

    
    def _init(self = None, maxsize = None):
        self.maxsize = maxsize
        self.queue = deque()

    
    def _qsize(self = None):
        return len(self.queue)

    
    def _empty(self = None):
        return not (self.queue)

    
    def _full(self = None):
        if self.maxsize > 0:
            pass
        return len(self.queue) == self.maxsize

    
    def _put(self = None, item = None):
        self.queue.append(item)

    
    def _get(self = None):
        if self.use_lifo:
            return self.queue.pop()
        return None.queue.popleft()


Queue = <NODE:27>(Queue, 'Queue', QueueCommon[_T])

def AsyncAdaptedQueue():
    '''AsyncAdaptedQueue'''
    if typing.TYPE_CHECKING:
        await_ = (lambda coroutine = None: pass)()
    else:
        await_ = staticmethod(await_only)
    
    def __init__(self = None, maxsize = None, use_lifo = None):
        self.use_lifo = use_lifo
        self.maxsize = maxsize

    
    def empty(self = None):
        return self._queue.empty()

    
    def full(self):
        return self._queue.full()

    
    def qsize(self):
        return self._queue.qsize()

    _queue = (lambda self = None: if self.use_lifo:
queue = asyncio.LifoQueue(maxsize = self.maxsize)else:
queue = asyncio.Queue(maxsize = self.maxsize)queue)()
    
    def put_nowait(self = None, item = None):
        
        try:
            self._queue.put_nowait(item)
            return None
        except asyncio.QueueFull:
            err = None
            raise Full(), err
            err = None
            del err


    
    def put(self = None, item = None, block = None, timeout = (True, None)):
        if not block:
            return self.put_nowait(item)
    # WARNING: Decompyle incomplete

    
    def get_nowait(self = None):
        
        try:
            return self._queue.get_nowait()
        except asyncio.QueueEmpty:
            err = None
            raise Empty(), err
            err = None
            del err


    
    def get(self = None, block = None, timeout = None):
        if not block:
            return self.get_nowait()
    # WARNING: Decompyle incomplete


AsyncAdaptedQueue = <NODE:27>(AsyncAdaptedQueue, 'AsyncAdaptedQueue', QueueCommon[_T])

def FallbackAsyncAdaptedQueue():
    '''FallbackAsyncAdaptedQueue'''
    if not typing.TYPE_CHECKING:
        await_ = staticmethod(await_fallback)
        return None

FallbackAsyncAdaptedQueue = <NODE:27>(FallbackAsyncAdaptedQueue, 'FallbackAsyncAdaptedQueue', AsyncAdaptedQueue[_T])
