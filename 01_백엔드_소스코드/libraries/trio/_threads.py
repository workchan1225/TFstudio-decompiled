# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _threads.pyc (Python 3.11)

from __future__ import annotations
import contextlib
import contextvars
import inspect
import queue as stdlib_queue
import threading
from itertools import count
from typing import TYPE_CHECKING, Generic, TypeVar
import attrs
import outcome
from attrs import define
from sniffio import current_async_library_cvar
import trio
from _core import RunVar, TrioToken, checkpoint, disable_ki_protection, enable_ki_protection, start_thread_soon
from _sync import CapacityLimiter, Event
from _util import coroutine_or_error
if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable, Generator
    from typing_extensions import TypeVarTuple, Unpack
    from trio._core._traps import RaiseCancelT
    Ts = TypeVarTuple('Ts')
RetT = TypeVar('RetT')

class _ParentTaskData(threading.local):
    task_register: 'list[trio.lowlevel.Task | None]' = 'Global due to Threading API, thread local storage for data related to the\n    parent task of native Trio threads.'

PARENT_TASK_DATA = _ParentTaskData()
_limiter_local: 'RunVar[CapacityLimiter]' = RunVar('limiter')
DEFAULT_LIMIT = 40
_thread_counter = count()
_ActiveThreadCount = <NODE:12>()
_active_threads_local: 'RunVar[_ActiveThreadCount]' = RunVar('active_threads')
_track_active_thread = (lambda : pass# WARNING: Decompyle incomplete
)()

async def wait_all_threads_completed():
    '''Wait until no threads are still running tasks.

    This is intended to be used when testing code with trio.to_thread to
    make sure no tasks are still making progress in a thread. See the
    following code for a usage example::

        async def wait_all_settled():
            while True:
                await trio.testing.wait_all_threads_complete()
                await trio.testing.wait_all_tasks_blocked()
                if trio.testing.active_thread_count() == 0:
                    break
    '''
    pass
# WARNING: Decompyle incomplete


def active_thread_count():
    '''Returns the number of threads that are currently running a task

    See `trio.testing.wait_all_threads_completed`
    '''
    
    try:
        return _active_threads_local.get().count
    except LookupError:
        return 0



def current_default_thread_limiter():
    '''Get the default `~trio.CapacityLimiter` used by
    `trio.to_thread.run_sync`.

    The most common reason to call this would be if you want to modify its
    :attr:`~trio.CapacityLimiter.total_tokens` attribute.

    '''
    
    try:
        limiter = _limiter_local.get()
    except LookupError:
        limiter = CapacityLimiter(DEFAULT_LIMIT)
        _limiter_local.set(limiter)

    return limiter

ThreadPlaceholder = <NODE:12>()

def Run():
    '''Run'''
    args: 'tuple[object, ...]' = 'Run'
    context: 'contextvars.Context' = attrs.field(init = False, factory = contextvars.copy_context)
    queue: 'stdlib_queue.SimpleQueue[outcome.Outcome[RetT]]' = attrs.field(init = False, factory = stdlib_queue.SimpleQueue)
    unprotected_afn = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    async def run(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def run_system(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def run_in_host_task(self = None, token = None):
        pass
    # WARNING: Decompyle incomplete

    
    def run_in_system_nursery(self = None, token = None):
        pass
    # WARNING: Decompyle incomplete


Run = <NODE:27>(Run, 'Run', Generic[RetT])()

def RunSync():
    '''RunSync'''
    args: 'tuple[object, ...]' = 'RunSync'
    context: 'contextvars.Context' = attrs.field(init = False, factory = contextvars.copy_context)
    queue: 'stdlib_queue.SimpleQueue[outcome.Outcome[RetT]]' = attrs.field(init = False, factory = stdlib_queue.SimpleQueue)
    unprotected_fn = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def run_sync(self = None):
        result = outcome.capture(self.unprotected_fn)
        self.queue.put_nowait(result)

    
    def run_in_host_task(self = None, token = None):
        pass
    # WARNING: Decompyle incomplete

    
    def run_in_system_nursery(self = None, token = None):
        token.run_sync_soon(self.run_sync)


RunSync = <NODE:27>(RunSync, 'RunSync', Generic[RetT])()
to_thread_run_sync = (lambda sync_fn = attrs.frozen(eq = False, slots = False), *, thread_name: pass# WARNING: Decompyle incomplete
)()

def from_thread_check_cancelled():
    '''Raise `trio.Cancelled` if the associated Trio task entered a cancelled status.

     Only applicable to threads spawned by `trio.to_thread.run_sync`. Poll to allow
     ``abandon_on_cancel=False`` threads to raise :exc:`~trio.Cancelled` at a suitable
     place, or to end abandoned ``abandon_on_cancel=True`` threads sooner than they may
     otherwise.

    Raises:
        Cancelled: If the corresponding call to `trio.to_thread.run_sync` has had a
            delivery of cancellation attempted against it, regardless of the value of
            ``abandon_on_cancel`` supplied as an argument to it.
        RuntimeError: If this thread is not spawned from `trio.to_thread.run_sync`.

    .. note::

       To be precise, :func:`~trio.from_thread.check_cancelled` checks whether the task
       running :func:`trio.to_thread.run_sync` has ever been cancelled since the last
       time it was running a :func:`trio.from_thread.run` or :func:`trio.from_thread.run_sync`
       function. It may raise `trio.Cancelled` even if a cancellation occurred that was
       later hidden by a modification to `trio.CancelScope.shield` between the cancelled
       `~trio.CancelScope` and :func:`trio.to_thread.run_sync`. This differs from the
       behavior of normal Trio checkpoints, which raise `~trio.Cancelled` only if the
       cancellation is still active when the checkpoint executes. The distinction here is
       *exceedingly* unlikely to be relevant to your application, but we mention it
       for completeness.
    '''
    
    try:
        raise_cancel = PARENT_TASK_DATA.cancel_register[0]
    except AttributeError:
        raise RuntimeError("this thread wasn't created by Trio, can't check for cancellation"), None

# WARNING: Decompyle incomplete


def _send_message_to_trio(trio_token = None, message_to_trio = None):
    '''Shared logic of from_thread functions'''
    token_provided = trio_token is not None
    if not token_provided:
        
        try:
            trio_token = PARENT_TASK_DATA.token
        except AttributeError:
            raise RuntimeError("this thread wasn't created by Trio, pass kwarg trio_token=..."), None
            if not isinstance(trio_token, TrioToken):
                raise RuntimeError('Passed kwarg trio_token is not of type TrioToken')

        
        try:
            trio.lowlevel.current_task()
            raise RuntimeError('this is a blocking function; call it from a thread')
        except RuntimeError:
            pass

        if token_provided or PARENT_TASK_DATA.abandon_on_cancel:
            message_to_trio.run_in_system_nursery(trio_token)
        else:
            message_to_trio.run_in_host_task(trio_token)
    return message_to_trio.queue.get().unwrap()


def from_thread_run(afn = None, *, trio_token, *args):
    '''Run the given async function in the parent Trio thread, blocking until it
    is complete.

    Returns:
      Whatever ``afn(*args)`` returns.

    Returns or raises whatever the given function returns or raises. It
    can also raise exceptions of its own:

    Raises:
        RunFinishedError: if the corresponding call to :func:`trio.run` has
            already completed, or if the run has started its final cleanup phase
            and can no longer spawn new system tasks.
        Cancelled: If the original call to :func:`trio.to_thread.run_sync` is cancelled
            (if *trio_token* is None) or the call to :func:`trio.run` completes
            (if *trio_token* is not None) while ``afn(*args)`` is running,
            then *afn* is likely to raise :exc:`trio.Cancelled`.
        RuntimeError: if you try calling this from inside the Trio thread,
            which would otherwise cause a deadlock, or if no ``trio_token`` was
            provided, and we can\'t infer one from context.
        TypeError: if ``afn`` is not an asynchronous function.

    **Locating a TrioToken**: There are two ways to specify which
    `trio.run` loop to reenter:

        - Spawn this thread from `trio.to_thread.run_sync`. Trio will
          automatically capture the relevant Trio token and use it
          to re-enter the same Trio task.
        - Pass a keyword argument, ``trio_token`` specifying a specific
          `trio.run` loop to re-enter. This is useful in case you have a
          "foreign" thread, spawned using some other framework, and still want
          to enter Trio, or if you want to use a new system task to call ``afn``,
          maybe to avoid the cancellation context of a corresponding
          `trio.to_thread.run_sync` task. You can get this token from
          :func:`trio.lowlevel.current_trio_token`.
    '''
    return _send_message_to_trio(trio_token, Run(afn, args))


def from_thread_run_sync(fn = None, *, trio_token, *args):
    '''Run the given sync function in the parent Trio thread, blocking until it
    is complete.

    Returns:
      Whatever ``fn(*args)`` returns.

    Returns or raises whatever the given function returns or raises. It
    can also raise exceptions of its own:

    Raises:
        RunFinishedError: if the corresponding call to `trio.run` has
            already completed.
        RuntimeError: if you try calling this from inside the Trio thread,
            which would otherwise cause a deadlock or if no ``trio_token`` was
            provided, and we can\'t infer one from context.
        TypeError: if ``fn`` is an async function.

    **Locating a TrioToken**: There are two ways to specify which
    `trio.run` loop to reenter:

        - Spawn this thread from `trio.to_thread.run_sync`. Trio will
          automatically capture the relevant Trio token and use it when you
          want to re-enter Trio.
        - Pass a keyword argument, ``trio_token`` specifying a specific
          `trio.run` loop to re-enter. This is useful in case you have a
          "foreign" thread, spawned using some other framework, and still want
          to enter Trio, or if you want to use a new system task to call ``fn``,
          maybe to avoid the cancellation context of a corresponding
          `trio.to_thread.run_sync` task.
    '''
    return _send_message_to_trio(trio_token, RunSync(fn, args))
