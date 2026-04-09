# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _trio.pyc (Python 3.11)

from __future__ import annotations
import array
import math
import os
import socket
import sys
import types
import weakref
from collections.abc import AsyncGenerator, AsyncIterator, Awaitable, Callable, Collection, Coroutine, Iterable, Sequence
from concurrent.futures import Future
from contextlib import AbstractContextManager
from dataclasses import dataclass
from functools import partial
from io import IOBase
from os import PathLike
from signal import Signals
from socket import AddressFamily, SocketKind
from types import TracebackType
from typing import IO, TYPE_CHECKING, Any, Generic, NoReturn, TypeVar, cast, overload
import trio.from_thread as trio
import trio.lowlevel as trio
from outcome import Error, Outcome, Value
from trio.lowlevel import current_root_task, current_task, notify_closing, wait_readable, wait_writable
from trio.socket import SocketType as TrioSocketType
from trio.to_thread import run_sync
from  import CapacityLimiterStatistics, EventStatistics, LockStatistics, RunFinishedError, TaskInfo, WouldBlock, abc
from _core._eventloop import claim_worker_thread
from _core._exceptions import BrokenResourceError, BusyResourceError, ClosedResourceError, EndOfStream
from _core._sockets import convert_ipv6_sockaddr
from _core._streams import create_memory_object_stream
from _core._synchronization import CapacityLimiter as BaseCapacityLimiter
from _core._synchronization import Event as BaseEvent
from _core._synchronization import Lock as BaseLock
from _core._synchronization import ResourceGuard, SemaphoreStatistics
from _core._synchronization import Semaphore as BaseSemaphore
from _core._tasks import CancelScope as BaseCancelScope
from abc import IPSockAddrType, UDPPacketType, UNIXDatagramPacketType
from abc._eventloop import AsyncBackend, StrOrBytesPath
from streams.memory import MemoryObjectSendStream
if TYPE_CHECKING:
    from _typeshed import FileDescriptorLike
if sys.version_info >= (3, 10):
    from typing import ParamSpec
else:
    from typing_extensions import ParamSpec
if sys.version_info >= (3, 11):
    from typing import TypeVarTuple, Unpack
else:
    from exceptiongroup import BaseExceptionGroup
    from typing_extensions import TypeVarTuple, Unpack
T = TypeVar('T')
T_Retval = TypeVar('T_Retval')
T_SockAddr = TypeVar('T_SockAddr', str, IPSockAddrType)
PosArgsT = TypeVarTuple('PosArgsT')
P = ParamSpec('P')
RunVar = trio.lowlevel.RunVar

class CancelScope(BaseCancelScope):
    
    def __new__(cls = None, original = None, **kwargs):
        return object.__new__(cls)

    
    def __init__(self = None, original = None, **kwargs):
        if not original:
            pass
    # WARNING: Decompyle incomplete

    
    def __enter__(self = None):
        self._CancelScope__original.__enter__()
        return self

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'bool')):
        return self._CancelScope__original.__exit__(exc_type, exc_val, exc_tb)

    
    def cancel(self = None, reason = None):
        self._CancelScope__original.cancel(reason)

    deadline = (lambda self = None: self._CancelScope__original.deadline)()
    deadline = (lambda self = None, value = None: self._CancelScope__original.deadline = value)()
    cancel_called = (lambda self = None: self._CancelScope__original.cancel_called)()
    cancelled_caught = (lambda self = None: self._CancelScope__original.cancelled_caught)()
    shield = (lambda self = None: self._CancelScope__original.shield)()
    shield = (lambda self = None, value = None: self._CancelScope__original.shield = value)()


class TaskGroup(abc.TaskGroup):
    
    def __init__(self = None):
        self._active = False
        self._nursery_manager = trio.open_nursery(strict_exception_groups = True)
        self.cancel_scope = None

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'bool')):
        pass
    # WARNING: Decompyle incomplete

    
    def start_soon(self = None, func = None, *, name, *args):
        if not self._active:
            raise RuntimeError('This task group is not active; no new tasks can be started.')
    # WARNING: Decompyle incomplete

    
    async def start(self = None, func = None, *, name, *args):
        pass
    # WARNING: Decompyle incomplete



class BlockingPortal(abc.BlockingPortal):
    pass
# WARNING: Decompyle incomplete

ReceiveStreamWrapper = <NODE:12>()
SendStreamWrapper = <NODE:12>()
Process = <NODE:12>()

class _ProcessPoolShutdownInstrument(trio.abc.Instrument):
    pass
# WARNING: Decompyle incomplete

current_default_worker_process_limiter: 'trio.lowlevel.RunVar' = RunVar('current_default_worker_process_limiter')

async def _shutdown_process_pool(workers = dataclass(eq = False)):
    pass
# WARNING: Decompyle incomplete


def _TrioSocketMixin():
    '''_TrioSocketMixin'''
    
    def __init__(self = None, trio_socket = None):
        self._trio_socket = trio_socket
        self._closed = False

    
    def _check_closed(self = None):
        if self._closed:
            raise ClosedResourceError
        if self._trio_socket.fileno() < 0:
            raise BrokenResourceError

    _raw_socket = (lambda self = None: self._trio_socket._sock)()
    
    async def aclose(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _convert_socket_error(self = None, exc = None):
        if isinstance(exc, trio.ClosedResourceError):
            raise ClosedResourceError, exc
        if self._trio_socket.fileno() < 0 and self._closed:
            raise ClosedResourceError, None
        if isinstance(exc, OSError):
            raise BrokenResourceError, exc
        raise exc


_TrioSocketMixin = <NODE:27>(_TrioSocketMixin, '_TrioSocketMixin', Generic[T_SockAddr])

class SocketStream(abc.SocketStream, _TrioSocketMixin):
    pass
# WARNING: Decompyle incomplete


class UNIXSocketStream(abc.UNIXSocketStream, SocketStream):
    
    async def receive_fds(self = None, msglen = None, maxfds = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_fds(self = None, message = None, fds = None):
        pass
    # WARNING: Decompyle incomplete



class TCPSocketListener(abc.SocketListener, _TrioSocketMixin):
    pass
# WARNING: Decompyle incomplete


class UNIXSocketListener(abc.SocketListener, _TrioSocketMixin):
    pass
# WARNING: Decompyle incomplete


def UDPSocket():
    '''UDPSocket'''
    pass
# WARNING: Decompyle incomplete

UDPSocket = <NODE:27>(UDPSocket, 'UDPSocket', _TrioSocketMixin[IPSockAddrType], abc.UDPSocket)

def ConnectedUDPSocket():
    '''ConnectedUDPSocket'''
    pass
# WARNING: Decompyle incomplete

ConnectedUDPSocket = <NODE:27>(ConnectedUDPSocket, 'ConnectedUDPSocket', _TrioSocketMixin[IPSockAddrType], abc.ConnectedUDPSocket)

def UNIXDatagramSocket():
    '''UNIXDatagramSocket'''
    pass
# WARNING: Decompyle incomplete

UNIXDatagramSocket = <NODE:27>(UNIXDatagramSocket, 'UNIXDatagramSocket', _TrioSocketMixin[str], abc.UNIXDatagramSocket)

def ConnectedUNIXDatagramSocket():
    '''ConnectedUNIXDatagramSocket'''
    pass
# WARNING: Decompyle incomplete

ConnectedUNIXDatagramSocket = <NODE:27>(ConnectedUNIXDatagramSocket, 'ConnectedUNIXDatagramSocket', _TrioSocketMixin[str], abc.ConnectedUNIXDatagramSocket)

class Event(BaseEvent):
    
    def __new__(cls = None):
        return object.__new__(cls)

    
    def __init__(self = None):
        self._Event__original = trio.Event()

    
    def is_set(self = None):
        return self._Event__original.is_set()

    
    async def wait(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def statistics(self = None):
        orig_statistics = self._Event__original.statistics()
        return EventStatistics(tasks_waiting = orig_statistics.tasks_waiting)

    
    def set(self = None):
        self._Event__original.set()



class Lock(BaseLock):
    
    def __new__(cls = None, *, fast_acquire):
        return object.__new__(cls)

    
    def __init__(self = None, *, fast_acquire):
        self._fast_acquire = fast_acquire
        self._Lock__original = trio.Lock()

    _convert_runtime_error_msg = (lambda exc = None: if exc.args == ('attempt to re-acquire an already held Lock',):
exc.args = ('Attempted to acquire an already held Lock',)None)()
    
    async def acquire(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def acquire_nowait(self = None):
        
        try:
            self._Lock__original.acquire_nowait()
            return None
        except trio.WouldBlock:
            raise WouldBlock, None
            except RuntimeError:
                exc = None
                self._convert_runtime_error_msg(exc)
                raise 
                exc = None
                del exc


    
    def locked(self = None):
        return self._Lock__original.locked()

    
    def release(self = None):
        self._Lock__original.release()

    
    def statistics(self = None):
        orig_statistics = self._Lock__original.statistics()
        owner = TrioTaskInfo(orig_statistics.owner) if orig_statistics.owner else None
        return LockStatistics(orig_statistics.locked, owner, orig_statistics.tasks_waiting)



class Semaphore(BaseSemaphore):
    pass
# WARNING: Decompyle incomplete


class CapacityLimiter(BaseCapacityLimiter):
    
    def __new__(cls = None, total_tokens = None, *, original):
        return object.__new__(cls)

    
    def __init__(self = None, total_tokens = None, *, original):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    total_tokens = (lambda self = None: self._CapacityLimiter__original.total_tokens)()
    total_tokens = (lambda self = None, value = None: self._CapacityLimiter__original.total_tokens = value)()
    borrowed_tokens = (lambda self = None: self._CapacityLimiter__original.borrowed_tokens)()
    available_tokens = (lambda self = None: self._CapacityLimiter__original.available_tokens)()
    
    def acquire_nowait(self = None):
        self._CapacityLimiter__original.acquire_nowait()

    
    def acquire_on_behalf_of_nowait(self = None, borrower = None):
        self._CapacityLimiter__original.acquire_on_behalf_of_nowait(borrower)

    
    async def acquire(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def acquire_on_behalf_of(self = None, borrower = None):
        pass
    # WARNING: Decompyle incomplete

    
    def release(self = None):
        return self._CapacityLimiter__original.release()

    
    def release_on_behalf_of(self = None, borrower = None):
        return self._CapacityLimiter__original.release_on_behalf_of(borrower)

    
    def statistics(self = None):
        orig = self._CapacityLimiter__original.statistics()
        return CapacityLimiterStatistics(borrowed_tokens = orig.borrowed_tokens, total_tokens = orig.total_tokens, borrowers = tuple(orig.borrowers), tasks_waiting = orig.tasks_waiting)


_capacity_limiter_wrapper: 'trio.lowlevel.RunVar' = RunVar('_capacity_limiter_wrapper')

class _SignalReceiver:
    _iterator: 'AsyncIterator[int]' = '_SignalReceiver'
    
    def __init__(self = None, signals = None):
        self._signals = signals

    
    def __enter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'bool | None')):
        return self._cm.__exit__(exc_type, exc_val, exc_tb)

    
    def __aiter__(self = None):
        return self

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete



class TestRunner(abc.TestRunner):
    
    def __init__(self = None, **options):
        Queue = Queue
        import queue
        self._call_queue = Queue()
        self._send_stream = None
        self._options = options

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'types.TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    async def _run_tests_and_fixtures(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _main_task_finished(self = None, outcome = None):
        self._send_stream = None

    
    def _call_in_runner_task(self = None, func = None, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def run_asyncgen_fixture(self = None, fixture_func = None, kwargs = None):
        pass
    # WARNING: Decompyle incomplete

    
    def run_fixture(self = None, fixture_func = None, kwargs = None):
        pass
    # WARNING: Decompyle incomplete

    
    def run_test(self = None, test_func = None, kwargs = None):
        pass
    # WARNING: Decompyle incomplete



class TrioTaskInfo(TaskInfo):
    pass
# WARNING: Decompyle incomplete


class TrioBackend(AsyncBackend):
    run = (lambda cls, func = None, args = None, kwargs = classmethod, options = ('func', 'Callable[[Unpack[PosArgsT]], Awaitable[T_Retval]]', 'args', 'tuple[Unpack[PosArgsT]]', 'kwargs', 'dict[str, Any]', 'options', 'dict[str, Any]', 'return', 'T_Retval'): pass# WARNING: Decompyle incomplete
)()
    current_token = (lambda cls = None: trio.lowlevel.current_trio_token())()
    current_time = (lambda cls = None: trio.current_time())()
    cancelled_exception_class = (lambda cls = None: trio.Cancelled)()
    checkpoint = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    checkpoint_if_cancelled = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    cancel_shielded_checkpoint = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    sleep = (lambda cls = None, delay = None: pass# WARNING: Decompyle incomplete
)()
    create_cancel_scope = (lambda cls = None, *, deadline: CancelScope(deadline = deadline, shield = shield))()
    current_effective_deadline = (lambda cls = None: trio.current_effective_deadline())()
    create_task_group = (lambda cls = None: TaskGroup())()
    create_event = (lambda cls = None: Event())()
    create_lock = (lambda cls = None, *, fast_acquire: Lock(fast_acquire = fast_acquire))()
    create_semaphore = (lambda cls = None, initial_value = None, *, max_value, fast_acquire: Semaphore(initial_value, max_value = max_value, fast_acquire = fast_acquire))()
    create_capacity_limiter = (lambda cls = None, total_tokens = None: CapacityLimiter(total_tokens))()
    run_sync_in_worker_thread = (lambda cls = None, func = None, args = classmethod, abandon_on_cancel = (False, None), limiter = ('func', 'Callable[[Unpack[PosArgsT]], T_Retval]', 'args', 'tuple[Unpack[PosArgsT]]', 'abandon_on_cancel', 'bool', 'limiter', 'abc.CapacityLimiter | None', 'return', 'T_Retval'): pass# WARNING: Decompyle incomplete
)()
    check_cancelled = (lambda cls = None: trio.from_thread.check_cancelled())()
    run_async_from_thread = (lambda cls = None, func = None, args = classmethod, token = ('func', 'Callable[[Unpack[PosArgsT]], Awaitable[T_Retval]]', 'args', 'tuple[Unpack[PosArgsT]]', 'token', 'object', 'return', 'T_Retval'): trio_token = cast('trio.lowlevel.TrioToken | None', token)# WARNING: Decompyle incomplete
)()
    run_sync_from_thread = (lambda cls = None, func = None, args = classmethod, token = ('func', 'Callable[[Unpack[PosArgsT]], T_Retval]', 'args', 'tuple[Unpack[PosArgsT]]', 'token', 'object', 'return', 'T_Retval'): trio_token = cast('trio.lowlevel.TrioToken | None', token)# WARNING: Decompyle incomplete
)()
    create_blocking_portal = (lambda cls = None: BlockingPortal())()
    open_process = (lambda cls = None, command = None, *, stdin, stdout: pass# WARNING: Decompyle incomplete
)()
    setup_process_pool_exit_at_shutdown = (lambda cls = None, workers = None: trio.lowlevel.spawn_system_task(_shutdown_process_pool, workers))()
    connect_tcp = (lambda cls = None, host = None, port = classmethod, local_address = (None,): pass# WARNING: Decompyle incomplete
)()
    connect_unix = (lambda cls = None, path = None: pass# WARNING: Decompyle incomplete
)()
    create_tcp_listener = (lambda cls = None, sock = None: TCPSocketListener(sock))()
    create_unix_listener = (lambda cls = None, sock = None: UNIXSocketListener(sock))()
    create_udp_socket = (lambda cls, family = None, local_address = None, remote_address = classmethod, reuse_port = ('family', 'socket.AddressFamily', 'local_address', 'IPSockAddrType | None', 'remote_address', 'IPSockAddrType | None', 'reuse_port', 'bool', 'return', 'UDPSocket | ConnectedUDPSocket'): pass# WARNING: Decompyle incomplete
)()
    create_unix_datagram_socket = (lambda cls = None, raw_socket = classmethod, remote_path = overload: pass# WARNING: Decompyle incomplete
)()()
    create_unix_datagram_socket = (lambda cls = None, raw_socket = classmethod, remote_path = overload: pass# WARNING: Decompyle incomplete
)()()
    create_unix_datagram_socket = (lambda cls = None, raw_socket = None, remote_path = classmethod: pass# WARNING: Decompyle incomplete
)()
    getaddrinfo = (lambda cls = None, host = None, port = None, *, family, type, proto: pass# WARNING: Decompyle incomplete
)()
    getnameinfo = (lambda cls = None, sockaddr = None, flags = classmethod: pass# WARNING: Decompyle incomplete
)()
    wait_readable = (lambda cls = None, obj = None: pass# WARNING: Decompyle incomplete
)()
    wait_writable = (lambda cls = None, obj = None: pass# WARNING: Decompyle incomplete
)()
    notify_closing = (lambda cls = None, obj = None: notify_closing(obj))()
    wrap_listener_socket = (lambda cls = None, sock = None: pass# WARNING: Decompyle incomplete
)()
    wrap_stream_socket = (lambda cls = None, sock = None: pass# WARNING: Decompyle incomplete
)()
    wrap_unix_stream_socket = (lambda cls = None, sock = None: pass# WARNING: Decompyle incomplete
)()
    wrap_udp_socket = (lambda cls = None, sock = None: pass# WARNING: Decompyle incomplete
)()
    wrap_connected_udp_socket = (lambda cls = None, sock = None: pass# WARNING: Decompyle incomplete
)()
    wrap_unix_datagram_socket = (lambda cls = None, sock = None: pass# WARNING: Decompyle incomplete
)()
    wrap_connected_unix_datagram_socket = (lambda cls = None, sock = None: pass# WARNING: Decompyle incomplete
)()
    current_default_thread_limiter = (lambda cls = None: try:
_capacity_limiter_wrapper.get()except LookupError:
limiter = CapacityLimiter(original = trio.to_thread.current_default_thread_limiter())_capacity_limiter_wrapper.set(limiter))()
    open_signal_receiver = (lambda cls = None: _SignalReceiver(signals))()
    get_current_task = (lambda cls = None: task = current_task()TrioTaskInfo(task))()
    get_running_tasks = (lambda cls = None: root_task = current_root_task()# WARNING: Decompyle incomplete
)()
    wait_all_tasks_blocked = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    create_test_runner = (lambda cls = None, options = None: pass# WARNING: Decompyle incomplete
)()

backend_class = TrioBackend
