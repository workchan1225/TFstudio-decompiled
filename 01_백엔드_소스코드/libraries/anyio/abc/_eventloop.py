# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _eventloop.pyc (Python 3.11)

from __future__ import annotations
import math
import sys
from abc import ABCMeta, abstractmethod
from collections.abc import AsyncIterator, Awaitable, Callable, Sequence
from contextlib import AbstractContextManager
from os import PathLike
from signal import Signals
from socket import AddressFamily, SocketKind, socket
from typing import IO, TYPE_CHECKING, Any, TypeVar, Union, overload
if sys.version_info >= (3, 11):
    from typing import TypeVarTuple, Unpack
else:
    from typing_extensions import TypeVarTuple, Unpack
if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias
if TYPE_CHECKING:
    from _typeshed import FileDescriptorLike
    from _core._synchronization import CapacityLimiter, Event, Lock, Semaphore
    from _core._tasks import CancelScope
    from _core._testing import TaskInfo
    from from_thread import BlockingPortal
    from _sockets import ConnectedUDPSocket, ConnectedUNIXDatagramSocket, IPSockAddrType, SocketListener, SocketStream, UDPSocket, UNIXDatagramSocket, UNIXSocketStream
    from _subprocesses import Process
    from _tasks import TaskGroup
    from _testing import TestRunner
T_Retval = TypeVar('T_Retval')
PosArgsT = TypeVarTuple('PosArgsT')
StrOrBytesPath: 'TypeAlias' = Union[(str, bytes, 'PathLike[str]', 'PathLike[bytes]')]

def AsyncBackend():
    '''AsyncBackend'''
    run = (lambda cls, func = None, args = classmethod, kwargs = abstractmethod, options = ('func', 'Callable[[Unpack[PosArgsT]], Awaitable[T_Retval]]', 'args', 'tuple[Unpack[PosArgsT]]', 'kwargs', 'dict[str, Any]', 'options', 'dict[str, Any]', 'return', 'T_Retval'): pass)()()
    current_token = (lambda cls = None: pass)()()
    current_time = (lambda cls = None: pass)()()
    cancelled_exception_class = (lambda cls = None: pass)()()
    checkpoint = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()()
    checkpoint_if_cancelled = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    cancel_shielded_checkpoint = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    sleep = (lambda cls = None, delay = classmethod: pass# WARNING: Decompyle incomplete
)()()
    create_cancel_scope = (lambda cls = None, *, deadline: pass)()()
    current_effective_deadline = (lambda cls = None: pass)()()
    create_task_group = (lambda cls = None: pass)()()
    create_event = (lambda cls = None: pass)()()
    create_lock = (lambda cls = None, *, fast_acquire: pass)()()
    create_semaphore = (lambda cls = None, initial_value = None, *, max_value, fast_acquire: pass)()()
    create_capacity_limiter = (lambda cls = None, total_tokens = classmethod: pass)()()
    run_sync_in_worker_thread = (lambda cls = None, func = classmethod, args = abstractmethod, abandon_on_cancel = (False, None), limiter = ('func', 'Callable[[Unpack[PosArgsT]], T_Retval]', 'args', 'tuple[Unpack[PosArgsT]]', 'abandon_on_cancel', 'bool', 'limiter', 'CapacityLimiter | None', 'return', 'T_Retval'): pass# WARNING: Decompyle incomplete
)()()
    check_cancelled = (lambda cls = None: pass)()()
    run_async_from_thread = (lambda cls = None, func = classmethod, args = abstractmethod, token = ('func', 'Callable[[Unpack[PosArgsT]], Awaitable[T_Retval]]', 'args', 'tuple[Unpack[PosArgsT]]', 'token', 'object', 'return', 'T_Retval'): pass)()()
    run_sync_from_thread = (lambda cls = None, func = classmethod, args = abstractmethod, token = ('func', 'Callable[[Unpack[PosArgsT]], T_Retval]', 'args', 'tuple[Unpack[PosArgsT]]', 'token', 'object', 'return', 'T_Retval'): pass)()()
    create_blocking_portal = (lambda cls = None: pass)()()
    open_process = (lambda cls = None, command = classmethod, *, stdin, stdout: pass# WARNING: Decompyle incomplete
)()()
    setup_process_pool_exit_at_shutdown = (lambda cls = None, workers = classmethod: pass)()()
    connect_tcp = (lambda cls = None, host = classmethod, port = abstractmethod, local_address = (None,): pass# WARNING: Decompyle incomplete
)()()
    connect_unix = (lambda cls = None, path = classmethod: pass# WARNING: Decompyle incomplete
)()()
    create_tcp_listener = (lambda cls = None, sock = classmethod: pass)()()
    create_unix_listener = (lambda cls = None, sock = classmethod: pass)()()
    create_udp_socket = (lambda cls, family = None, local_address = classmethod, remote_address = abstractmethod, reuse_port = ('family', 'AddressFamily', 'local_address', 'IPSockAddrType | None', 'remote_address', 'IPSockAddrType | None', 'reuse_port', 'bool', 'return', 'UDPSocket | ConnectedUDPSocket'): pass# WARNING: Decompyle incomplete
)()()
    create_unix_datagram_socket = (lambda cls = None, raw_socket = classmethod, remote_path = overload: pass# WARNING: Decompyle incomplete
)()()
    create_unix_datagram_socket = (lambda cls = None, raw_socket = classmethod, remote_path = overload: pass# WARNING: Decompyle incomplete
)()()
    create_unix_datagram_socket = (lambda cls = None, raw_socket = classmethod, remote_path = abstractmethod: pass# WARNING: Decompyle incomplete
)()()
    getaddrinfo = (lambda cls = None, host = None, port = classmethod, *, family, type, proto: pass# WARNING: Decompyle incomplete
)()()
    getnameinfo = (lambda cls = None, sockaddr = classmethod, flags = abstractmethod: pass# WARNING: Decompyle incomplete
)()()
    wait_readable = (lambda cls = None, obj = classmethod: pass# WARNING: Decompyle incomplete
)()()
    wait_writable = (lambda cls = None, obj = classmethod: pass# WARNING: Decompyle incomplete
)()()
    notify_closing = (lambda cls = None, obj = classmethod: pass)()()
    wrap_listener_socket = (lambda cls = None, sock = classmethod: pass# WARNING: Decompyle incomplete
)()()
    wrap_stream_socket = (lambda cls = None, sock = classmethod: pass# WARNING: Decompyle incomplete
)()()
    wrap_unix_stream_socket = (lambda cls = None, sock = classmethod: pass# WARNING: Decompyle incomplete
)()()
    wrap_udp_socket = (lambda cls = None, sock = classmethod: pass# WARNING: Decompyle incomplete
)()()
    wrap_connected_udp_socket = (lambda cls = None, sock = classmethod: pass# WARNING: Decompyle incomplete
)()()
    wrap_unix_datagram_socket = (lambda cls = None, sock = classmethod: pass# WARNING: Decompyle incomplete
)()()
    wrap_connected_unix_datagram_socket = (lambda cls = None, sock = classmethod: pass# WARNING: Decompyle incomplete
)()()
    current_default_thread_limiter = (lambda cls = None: pass)()()
    open_signal_receiver = (lambda cls = None: pass)()()
    get_current_task = (lambda cls = None: pass)()()
    get_running_tasks = (lambda cls = None: pass)()()
    wait_all_tasks_blocked = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()()
    create_test_runner = (lambda cls = None, options = classmethod: pass)()()

AsyncBackend = <NODE:27>(AsyncBackend, 'AsyncBackend', metaclass = ABCMeta)
