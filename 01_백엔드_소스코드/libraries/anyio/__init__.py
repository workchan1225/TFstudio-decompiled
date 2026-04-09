# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import annotations
from _core._contextmanagers import AsyncContextManagerMixin
from _core._contextmanagers import ContextManagerMixin
from _core._eventloop import current_time
from _core._eventloop import get_all_backends
from _core._eventloop import get_available_backends
from _core._eventloop import get_cancelled_exc_class
from _core._eventloop import run
from _core._eventloop import sleep
from _core._eventloop import sleep_forever
from _core._eventloop import sleep_until
from _core._exceptions import BrokenResourceError
from _core._exceptions import BrokenWorkerInterpreter
from _core._exceptions import BrokenWorkerProcess
from _core._exceptions import BusyResourceError
from _core._exceptions import ClosedResourceError
from _core._exceptions import ConnectionFailed
from _core._exceptions import DelimiterNotFound
from _core._exceptions import EndOfStream
from _core._exceptions import IncompleteRead
from _core._exceptions import NoEventLoopError
from _core._exceptions import RunFinishedError
from _core._exceptions import TypedAttributeLookupError
from _core._exceptions import WouldBlock
from _core._fileio import AsyncFile
from _core._fileio import Path
from _core._fileio import open_file
from _core._fileio import wrap_file
from _core._resources import aclose_forcefully
from _core._signals import open_signal_receiver
from _core._sockets import TCPConnectable
from _core._sockets import UNIXConnectable
from _core._sockets import as_connectable
from _core._sockets import connect_tcp
from _core._sockets import connect_unix
from _core._sockets import create_connected_udp_socket
from _core._sockets import create_connected_unix_datagram_socket
from _core._sockets import create_tcp_listener
from _core._sockets import create_udp_socket
from _core._sockets import create_unix_datagram_socket
from _core._sockets import create_unix_listener
from _core._sockets import getaddrinfo
from _core._sockets import getnameinfo
from _core._sockets import notify_closing
from _core._sockets import wait_readable
from _core._sockets import wait_socket_readable
from _core._sockets import wait_socket_writable
from _core._sockets import wait_writable
from _core._streams import create_memory_object_stream
from _core._subprocesses import open_process
from _core._subprocesses import run_process
from _core._synchronization import CapacityLimiter
from _core._synchronization import CapacityLimiterStatistics
from _core._synchronization import Condition
from _core._synchronization import ConditionStatistics
from _core._synchronization import Event
from _core._synchronization import EventStatistics
from _core._synchronization import Lock
from _core._synchronization import LockStatistics
from _core._synchronization import ResourceGuard
from _core._synchronization import Semaphore
from _core._synchronization import SemaphoreStatistics
from _core._tasks import TASK_STATUS_IGNORED
from _core._tasks import CancelScope
from _core._tasks import create_task_group
from _core._tasks import current_effective_deadline
from _core._tasks import fail_after
from _core._tasks import move_on_after
from _core._tempfile import NamedTemporaryFile
from _core._tempfile import SpooledTemporaryFile
from _core._tempfile import TemporaryDirectory
from _core._tempfile import TemporaryFile
from _core._tempfile import gettempdir
from _core._tempfile import gettempdirb
from _core._tempfile import mkdtemp
from _core._tempfile import mkstemp
from _core._testing import TaskInfo
from _core._testing import get_current_task
from _core._testing import get_running_tasks
from _core._testing import wait_all_tasks_blocked
from _core._typedattr import TypedAttributeProvider
from _core._typedattr import TypedAttributeSet
from _core._typedattr import typed_attribute
for __value in list(locals().values()):
    if getattr(__value, '__module__', '').startswith('anyio.'):
        __value.__module__ = __name__
    del __value
    
    def __getattr__(attr = None):
        '''Support deprecated aliases.'''
        if attr == 'BrokenWorkerIntepreter':
            import warnings
            warnings.warn("The 'BrokenWorkerIntepreter' alias is deprecated, use 'BrokenWorkerInterpreter' instead.", DeprecationWarning, stacklevel = 2)
            return BrokenWorkerInterpreter
        raise None(f'''module {__name__!r} has no attribute {attr!r}''')

    return None
