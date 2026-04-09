# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lowlevel.pyc (Python 3.11)

"""
This namespace represents low-level functionality not intended for daily use,
but useful for extending Trio's functionality.
"""
import select as _select
import sys
import typing as _t
from _core import Abort, ParkingLot, ParkingLotStatistics, RaiseCancelT, RunStatistics, RunVar, RunVarToken, Task, TrioToken, UnboundedQueue, UnboundedQueueStatistics, add_instrument, add_parking_lot_breaker, cancel_shielded_checkpoint, checkpoint, checkpoint_if_cancelled, current_clock, current_root_task, current_statistics, current_task, current_trio_token, currently_ki_protected, disable_ki_protection, enable_ki_protection, in_trio_run, in_trio_task, notify_closing, permanently_detach_coroutine_object, reattach_detached_coroutine_object, remove_instrument, remove_parking_lot_breaker, reschedule, spawn_system_task, start_guest_run, start_thread_soon, temporarily_detach_coroutine_object, wait_readable, wait_task_rescheduled, wait_writable
from _subprocess import open_process
if (sys.platform == 'win32' or _t.TYPE_CHECKING) and 'sphinx.ext.autodoc' in sys.modules:
    from _core import current_iocp, monitor_completion_key, readinto_overlapped, register_with_iocp, wait_overlapped, write_overlapped
    if sys.platform == 'win32':
        from _wait_for_object import WaitForSingleObject
if (sys.platform != 'win32' or _t.TYPE_CHECKING) and 'sphinx.ext.autodoc' in sys.modules:
    from _unix_pipes import FdStream
    if ((sys.platform != 'linux' or _t.TYPE_CHECKING) and hasattr(_select, 'epoll') or _t.TYPE_CHECKING) and 'sphinx.ext.autodoc' in sys.modules:
        from _core import current_kqueue, monitor_kevent, wait_kevent
del sys
