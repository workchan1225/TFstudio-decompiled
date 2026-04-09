# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _generated_run.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING
from _ki import enable_ki_protection
from _run import _NO_SEND, GLOBAL_RUN_CONTEXT, RunStatistics, Task
if TYPE_CHECKING:
    import contextvars
    from collections.abc import Awaitable, Callable
    from outcome import Outcome
    from typing_extensions import Unpack
    from _abc import Clock
    from _entry_queue import TrioToken
    from _run import PosArgT
__all__ = [
    'current_clock',
    'current_root_task',
    'current_statistics',
    'current_time',
    'current_trio_token',
    'reschedule',
    'spawn_system_task',
    'wait_all_tasks_blocked']
current_statistics = (lambda : try:
GLOBAL_RUN_CONTEXT.runner.current_statistics()except AttributeError:
raise RuntimeError('must be called from async context'), None)()
current_time = (lambda : try:
GLOBAL_RUN_CONTEXT.runner.current_time()except AttributeError:
raise RuntimeError('must be called from async context'), None)()
current_clock = (lambda : try:
GLOBAL_RUN_CONTEXT.runner.current_clock()except AttributeError:
raise RuntimeError('must be called from async context'), None)()
current_root_task = (lambda : try:
GLOBAL_RUN_CONTEXT.runner.current_root_task()except AttributeError:
raise RuntimeError('must be called from async context'), None)()
reschedule = (lambda task = None, next_send = None: try:
GLOBAL_RUN_CONTEXT.runner.reschedule(task, next_send)except AttributeError:
raise RuntimeError('must be called from async context'), None)()
spawn_system_task = (lambda async_fn = None, *, name: pass# WARNING: Decompyle incomplete
)()
current_trio_token = (lambda : try:
GLOBAL_RUN_CONTEXT.runner.current_trio_token()except AttributeError:
raise RuntimeError('must be called from async context'), None)()
wait_all_tasks_blocked = (lambda cushion = None: pass# WARNING: Decompyle incomplete
)()
