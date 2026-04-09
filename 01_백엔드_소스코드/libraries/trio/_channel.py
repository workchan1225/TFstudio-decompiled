# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _channel.pyc (Python 3.11)

from __future__ import annotations
import sys
from collections import OrderedDict, deque
from collections.abc import AsyncGenerator, Callable
from contextlib import AbstractAsyncContextManager, asynccontextmanager
from functools import wraps
from math import inf
from typing import TYPE_CHECKING, Generic
import attrs
from outcome import Error, Value
import trio
from _abc import ReceiveChannel, ReceiveType, SendChannel, SendType, T
from _core import Abort, BrokenResourceError, RaiseCancelT, Task, enable_ki_protection
from _util import MultipleExceptionError, NoPublicConstructor, final, raise_single_exception_from_group
if sys.version_info < (3, 11):
    from exceptiongroup import BaseExceptionGroup
if TYPE_CHECKING:
    from types import TracebackType
    from typing_extensions import ParamSpec, Self
    P = ParamSpec('P')
elif 'sphinx.ext.autodoc' in sys.modules:
    
    try:
        from typing_extensions import ParamSpec
        P = ParamSpec('P')
    except ImportError:
        P = ...

    
    def open_memory_channel():
        '''open_memory_channel'''
        __doc__ = "Open a channel for passing objects between tasks within a process.\n\n    Memory channels are lightweight, cheap to allocate, and entirely\n    in-memory. They don't involve any operating-system resources, or any kind\n    of serialization. They just pass Python objects directly between tasks\n    (with a possible stop in an internal buffer along the way).\n\n    Channel objects can be closed by calling `~trio.abc.AsyncResource.aclose`\n    or using ``async with``. They are *not* automatically closed when garbage\n    collected. Closing memory channels isn't mandatory, but it is generally a\n    good idea, because it helps avoid situations where tasks get stuck waiting\n    on a channel when there's no-one on the other side. See\n    :ref:`channel-shutdown` for details.\n\n    Memory channel operations are all atomic with respect to\n    cancellation, either `~trio.abc.ReceiveChannel.receive` will\n    successfully return an object, or it will raise :exc:`Cancelled`\n    while leaving the channel unchanged.\n\n    Args:\n      max_buffer_size (int or math.inf): The maximum number of items that can\n        be buffered in the channel before :meth:`~trio.abc.SendChannel.send`\n        blocks. Choosing a sensible value here is important to ensure that\n        backpressure is communicated promptly and avoid unnecessary latency;\n        see :ref:`channel-buffering` for more details. If in doubt, use 0.\n\n    Returns:\n      A pair ``(send_channel, receive_channel)``. If you have\n      trouble remembering which order these go in, remember: data\n      flows from left → right.\n\n    In addition to the standard channel methods, all memory channel objects\n    provide a ``statistics()`` method, which returns an object with the\n    following fields:\n\n    * ``current_buffer_used``: The number of items currently stored in the\n      channel buffer.\n    * ``max_buffer_size``: The maximum number of items allowed in the buffer,\n      as passed to :func:`open_memory_channel`.\n    * ``open_send_channels``: The number of open\n      :class:`MemorySendChannel` endpoints pointing to this channel.\n      Initially 1, but can be increased by\n      :meth:`MemorySendChannel.clone`.\n    * ``open_receive_channels``: Likewise, but for open\n      :class:`MemoryReceiveChannel` endpoints.\n    * ``tasks_waiting_send``: The number of tasks blocked in ``send`` on this\n      channel (summing over all clones).\n    * ``tasks_waiting_receive``: The number of tasks blocked in ``receive`` on\n      this channel (summing over all clones).\n    "
        
        def __new__(cls = None, max_buffer_size = None):
            if not max_buffer_size != inf and isinstance(max_buffer_size, int):
                raise TypeError('max_buffer_size must be an integer or math.inf')
            if max_buffer_size < 0:
                raise ValueError('max_buffer_size must be >= 0')
            state = MemoryChannelState(max_buffer_size)
            return (MemorySendChannel[T]._create(state), MemoryReceiveChannel[T]._create(state))

        
        def __init__(self = None, max_buffer_size = None):
            pass


    open_memory_channel = <NODE:27>(open_memory_channel, 'open_memory_channel', tuple[('MemorySendChannel[T]', 'MemoryReceiveChannel[T]')])()
    MemoryChannelStatistics = <NODE:12>()
    
    def MemoryChannelState():
        '''MemoryChannelState'''
        max_buffer_size: 'int | float' = 'MemoryChannelState'
        data: 'deque[T]' = attrs.Factory(deque)
        open_send_channels: 'int' = 0
        open_receive_channels: 'int' = 0
        send_tasks: 'OrderedDict[Task, T]' = attrs.Factory(OrderedDict)
        receive_tasks: 'OrderedDict[Task, None]' = attrs.Factory(OrderedDict)
        
        def statistics(self = None):
            return MemoryChannelStatistics(current_buffer_used = len(self.data), max_buffer_size = self.max_buffer_size, open_send_channels = self.open_send_channels, open_receive_channels = self.open_receive_channels, tasks_waiting_send = len(self.send_tasks), tasks_waiting_receive = len(self.receive_tasks))


    MemoryChannelState = <NODE:27>(MemoryChannelState, 'MemoryChannelState', Generic[T])()
    
    def MemorySendChannel():
        '''MemorySendChannel'''
        _state: 'MemoryChannelState[SendType]' = 'MemorySendChannel'
        _closed: 'bool' = False
        _tasks: 'set[Task]' = attrs.Factory(set)
        
        def __attrs_post_init__(self = None):
            pass

        
        def __repr__(self = None):
            return f'''<send channel at {id(self):#x}, using buffer at {id(self._state):#x}>'''

        
        def statistics(self = None):
            '''Returns a `MemoryChannelStatistics` for the memory channel this is
        associated with.'''
            return self._state.statistics()

        send_nowait = (lambda self = None, value = None: if self._closed:
raise trio.ClosedResourceErrorif self._state.open_receive_channels == 0:
raise trio.BrokenResourceError# WARNING: Decompyle incomplete
)()
        send = (lambda self = None, value = None: pass# WARNING: Decompyle incomplete
)()
        clone = (lambda self = None: if self._closed:
raise trio.ClosedResourceErrorMemorySendChannel._create(self._state))()
        
        def __enter__(self = None):
            return self

        
        def __exit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
            self.close()

        close = (lambda self = None: if self._closed:
Noneself._closed = None# WARNING: Decompyle incomplete
)()
        aclose = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

    MemorySendChannel = <NODE:27>(MemorySendChannel, 'MemorySendChannel', SendChannel[SendType], metaclass = NoPublicConstructor)()()
    
    def MemoryReceiveChannel():
        '''MemoryReceiveChannel'''
        _state: 'MemoryChannelState[ReceiveType]' = 'MemoryReceiveChannel'
        _closed: 'bool' = False
        _tasks: 'set[trio._core._run.Task]' = attrs.Factory(set)
        
        def __attrs_post_init__(self = None):
            pass

        
        def statistics(self = None):
            '''Returns a `MemoryChannelStatistics` for the memory channel this is
        associated with.'''
            return self._state.statistics()

        
        def __repr__(self = None):
            return f'''<receive channel at {id(self):#x}, using buffer at {id(self._state):#x}>'''

        receive_nowait = (lambda self = None: if self._closed:
raise trio.ClosedResourceErrorif self._state.send_tasks:
(task, value) = self._state.send_tasks.popitem(last = False)task.custom_sleep_data._tasks.remove(task)trio.lowlevel.reschedule(task)self._state.data.append(value)if self._state.data:
self._state.data.popleft()if not None._state.open_send_channels:
raise trio.EndOfChannelraise trio.WouldBlock)()
        receive = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
        clone = (lambda self = None: if self._closed:
raise trio.ClosedResourceErrorMemoryReceiveChannel._create(self._state))()
        
        def __enter__(self = None):
            return self

        
        def __exit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
            self.close()

        close = (lambda self = None: if self._closed:
Noneself._closed = None# WARNING: Decompyle incomplete
)()
        aclose = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

    MemoryReceiveChannel = <NODE:27>(MemoryReceiveChannel, 'MemoryReceiveChannel', ReceiveChannel[ReceiveType], metaclass = NoPublicConstructor)()()
    
    def RecvChanWrapper():
        '''RecvChanWrapper'''
        
        def __init__(self = None, recv_chan = None, send_semaphore = None):
            self._recv_chan = recv_chan
            self._send_semaphore = send_semaphore

        
        async def receive(self = None):
            pass
        # WARNING: Decompyle incomplete

        
        async def aclose(self = None):
            pass
        # WARNING: Decompyle incomplete

        
        def __enter__(self = None):
            return self

        
        def __exit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
            self._recv_chan.close()


    RecvChanWrapper = <NODE:27>(RecvChanWrapper, 'RecvChanWrapper', ReceiveChannel[T])
    
    def as_safe_channel(fn = attrs.define(eq = False, repr = False, slots = False)):
        '''Decorate an async generator function to make it cancellation-safe.

    The ``yield`` keyword offers a very convenient way to write iterators...
    which makes it really unfortunate that async generators are so difficult
    to call correctly.  Yielding from the inside of a cancel scope or a nursery
    to the outside `violates structured concurrency <https://xkcd.com/292/>`_
    with consequences explained in :pep:`789`.  Even then, resource cleanup
    errors remain common (:pep:`533`) unless you wrap every call in
    :func:`~contextlib.aclosing`.

    This decorator gives you the best of both worlds: with careful exception
    handling and a background task we preserve structured concurrency by
    offering only the safe interface, and you can still write your iterables
    with the convenience of ``yield``.  For example::

        @as_safe_channel
        async def my_async_iterable(arg, *, kwarg=True):
            while ...:
                item = await ...
                yield item

        async with my_async_iterable(...) as recv_chan:
            async for item in recv_chan:
                ...

    While the combined async-with-async-for can be inconvenient at first,
    the context manager is indispensable for both correctness and for prompt
    cleanup of resources.
    '''
        pass
    # WARNING: Decompyle incomplete

    return None
