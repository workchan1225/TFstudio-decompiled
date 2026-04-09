# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _asyncio.pyc (Python 3.11)

from __future__ import annotations
import array
import asyncio
import concurrent.futures as concurrent
import contextvars
import math
import os
import socket
import sys
import threading
import weakref
from asyncio import AbstractEventLoop, CancelledError, all_tasks, create_task, current_task, get_running_loop, sleep
from asyncio.base_events import _run_until_complete_cb
from collections import OrderedDict, deque
from collections.abc import AsyncGenerator, AsyncIterator, Awaitable, Callable, Collection, Coroutine, Iterable, Sequence
from concurrent.futures import Future
from contextlib import AbstractContextManager, suppress
from contextvars import Context, copy_context
from dataclasses import dataclass, field
from functools import partial, wraps
from inspect import CORO_RUNNING, CORO_SUSPENDED, getcoroutinestate, iscoroutine
from io import IOBase
from os import PathLike
from queue import Queue
from signal import Signals
from socket import AddressFamily, SocketKind
from threading import Thread
from types import CodeType, TracebackType
from typing import IO, TYPE_CHECKING, Any, Optional, TypeVar, cast
from weakref import WeakKeyDictionary
from  import CapacityLimiterStatistics, EventStatistics, LockStatistics, TaskInfo, abc
from _core._eventloop import claim_worker_thread, set_current_async_library, threadlocals
from _core._exceptions import BrokenResourceError, BusyResourceError, ClosedResourceError, EndOfStream, RunFinishedError, WouldBlock, iterate_exceptions
from _core._sockets import convert_ipv6_sockaddr
from _core._streams import create_memory_object_stream
from _core._synchronization import CapacityLimiter as BaseCapacityLimiter
from _core._synchronization import Event as BaseEvent
from _core._synchronization import Lock as BaseLock
from _core._synchronization import ResourceGuard, SemaphoreStatistics
from _core._synchronization import Semaphore as BaseSemaphore
from _core._tasks import CancelScope as BaseCancelScope
from abc import AsyncBackend, IPSockAddrType, SocketListener, UDPPacketType, UNIXDatagramPacketType
from abc._eventloop import StrOrBytesPath
from lowlevel import RunVar
from streams.memory import MemoryObjectReceiveStream, MemoryObjectSendStream
if TYPE_CHECKING:
    from _typeshed import FileDescriptorLike
else:
    FileDescriptorLike = object
if sys.version_info >= (3, 10):
    from typing import ParamSpec
else:
    from typing_extensions import ParamSpec
if sys.version_info >= (3, 11):
    from asyncio import Runner
    from typing import TypeVarTuple, Unpack
else:
    import contextvars
    import enum
    import signal
    from asyncio import coroutines, events, exceptions, tasks
    from exceptiongroup import BaseExceptionGroup
    from typing_extensions import TypeVarTuple, Unpack
    
    class _State(enum.Enum):
        CREATED = 'created'
        INITIALIZED = 'initialized'
        CLOSED = 'closed'

    
    class Runner:
        
        def __init__(self = None, *, debug, loop_factory):
            self._state = _State.CREATED
            self._debug = debug
            self._loop_factory = loop_factory
            self._loop = None
            self._context = None
            self._interrupt_count = 0
            self._set_event_loop = False

        
        def __enter__(self = None):
            self._lazy_init()
            return self

        
        def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
            self.close()

        
        def close(self = None):
            '''Shutdown and close event loop.'''
            loop = self._loop
        # WARNING: Decompyle incomplete

        
        def get_loop(self = None):
            '''Return embedded event loop.'''
            self._lazy_init()
            return self._loop

        
        def run(self = None, coro = None, *, context):
            '''Run a coroutine inside the embedded event loop.'''
            if not coroutines.iscoroutine(coro):
                raise ValueError(f'''a coroutine was expected, got {coro!r}''')
        # WARNING: Decompyle incomplete

        
        def _lazy_init(self = None):
            if self._state is _State.CLOSED:
                raise RuntimeError('Runner is closed')
            if self._state is _State.INITIALIZED:
                return None
        # WARNING: Decompyle incomplete

        
        def _on_sigint(self = None, signum = None, frame = None, main_task = ('main_task', 'asyncio.Task', 'return', 'None')):
            if not self._interrupt_count == 1 and main_task.done():
                main_task.cancel()
                self._loop.call_soon_threadsafe((lambda : pass))
                return None
            raise self, self._interrupt_count += 1, ._interrupt_count()


    
    def _cancel_all_tasks(loop = None):
        to_cancel = tasks.all_tasks(loop)
        if not to_cancel:
            return None
    # WARNING: Decompyle incomplete

    
    async def _shutdown_default_executor(loop = None):
        '''Schedule the shutdown of the default executor.'''
        pass
    # WARNING: Decompyle incomplete

T_Retval = TypeVar('T_Retval')
T_contra = TypeVar('T_contra', contravariant = True)
PosArgsT = TypeVarTuple('PosArgsT')
P = ParamSpec('P')
_root_task: 'RunVar[asyncio.Task | None]' = RunVar('_root_task')

def find_root_task():
    root_task = _root_task.get(None)
# WARNING: Decompyle incomplete


def get_callable_name(func = None):
    module = getattr(func, '__module__', None)
    qualname = getattr(func, '__qualname__', None)
    return (lambda .0: pass# WARNING: Decompyle incomplete
)((module, qualname)())

_run_vars: 'WeakKeyDictionary[asyncio.AbstractEventLoop, Any]' = WeakKeyDictionary()

def _task_started(task = None):
    '''Return ``True`` if the task has been started and has not finished.'''
    coro = task.get_coro()
# WARNING: Decompyle incomplete


def is_anyio_cancellation(exc = None):
    if exc.args and isinstance(exc.args[0], str) and exc.args[0].startswith('Cancelled via cancel scope '):
        return True
    if None(exc.__context__, CancelledError):
        exc = exc.__context__
        continue
    return False


class CancelScope(BaseCancelScope):
    
    def __new__(cls = None, *, deadline, shield):
        return object.__new__(cls)

    
    def __init__(self = None, deadline = None, shield = None):
        self._deadline = deadline
        self._shield = shield
        self._parent_scope = None
        self._child_scopes = set()
        self._cancel_called = False
        self._cancel_reason = None
        self._cancelled_caught = False
        self._active = False
        self._timeout_handle = None
        self._cancel_handle = None
        self._tasks = set()
        self._host_task = None
        if sys.version_info >= (3, 11):
            self._pending_uncancellations = 0
            return None
        self._pending_uncancellations = None

    
    def __enter__(self = None):
        if self._active:
            raise RuntimeError("Each CancelScope may only be used for a single 'with' block")
        self._host_task = cast(asyncio.Task, current_task())
        host_task = cast(asyncio.Task, current_task())
        self._tasks.add(host_task)
    # WARNING: Decompyle incomplete

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'bool')):
        del exc_tb
        if not self._active:
            raise RuntimeError('This cancel scope is not active')
        if current_task() is not self._host_task:
            raise RuntimeError('Attempted to exit cancel scope in a different task than it was entered in')
    # WARNING: Decompyle incomplete

    _effectively_cancelled = (lambda self = None: cancel_scope = self# WARNING: Decompyle incomplete
)()
    _parent_cancellation_is_visible_to_us = (lambda self = None:
