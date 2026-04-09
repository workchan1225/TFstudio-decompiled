# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _run.pyc (Python 3.11)

from __future__ import annotations
import enum
import functools
import gc
import itertools
import random
import select
import sys
import warnings
from collections import deque
from contextlib import AbstractAsyncContextManager, contextmanager, suppress
from contextvars import copy_context
from heapq import heapify, heappop, heappush
from math import inf, isnan
from time import perf_counter
from typing import TYPE_CHECKING, Any, Final, NoReturn, Protocol, cast, overload
import attrs
from outcome import Error, Outcome, Value, capture
from sniffio import thread_local as sniffio_library
from sortedcontainers import SortedDict
from  import _core
from _abc import Clock, Instrument
from _deprecate import warn_deprecated
from _util import NoPublicConstructor, coroutine_or_error, final
from _asyncgens import AsyncGenerators
from _concat_tb import concat_tb
from _entry_queue import EntryQueue, TrioToken
from _exceptions import Cancelled, CancelReasonLiteral, RunFinishedError, TrioInternalError
from _instrumentation import Instruments
from _ki import KIManager, enable_ki_protection
from _parking_lot import GLOBAL_PARKING_LOT_BREAKER
from _run_context import GLOBAL_RUN_CONTEXT
from _thread_cache import start_thread_soon
from _traps import Abort, CancelShieldedCheckpoint, PermanentlyDetachCoroutineObject, WaitTaskRescheduled, cancel_shielded_checkpoint, wait_task_rescheduled
if sys.version_info < (3, 11):
    from exceptiongroup import BaseExceptionGroup
if TYPE_CHECKING:
    import contextvars
    import types
    from collections.abc import Awaitable, Callable, Generator, Iterator, Sequence
    from types import TracebackType
    import outcome
    from typing_extensions import Self, TypeVar, TypeVarTuple, Unpack
    PosArgT = TypeVarTuple('PosArgT')
    StatusT = TypeVar('StatusT', default = None)
    StatusT_contra = TypeVar('StatusT_contra', contravariant = True, default = None)
    BaseExcT = TypeVar('BaseExcT', bound = BaseException)
else:
    from typing import TypeVar
    StatusT = TypeVar('StatusT')
    StatusT_contra = TypeVar('StatusT_contra', contravariant = True)
RetT = TypeVar('RetT')
DEADLINE_HEAP_MIN_PRUNE_THRESHOLD: 'Final' = 1000
_NO_SEND: 'Final[Outcome[object]]' = cast('Outcome[object]', object())
NONSTRICT_EXCEPTIONGROUP_NOTE = 'This is a "loose" ExceptionGroup, and may be collapsed by Trio if it only contains one exception - typically after `Cancelled` has been stripped from it. Note this has consequences for exception handling, and strict_exception_groups=True is recommended.'

def _NoStatus():
    '''_NoStatus'''
    __doc__ = 'Sentinel for unset TaskStatus._value.'

_NoStatus = <NODE:27>(_NoStatus, '_NoStatus', metaclass = NoPublicConstructor)()

def _public(fn = None):
    return fn

_ALLOW_DETERMINISTIC_SCHEDULING: 'Final' = False
_r = random.Random()

def _hypothesis_plugin_setup():
    pass
# WARNING: Decompyle incomplete


def _count_context_run_tb_frames():
    """Count implementation dependent traceback frames from Context.run()

    On CPython, Context.run() is implemented in C and doesn't show up in
    tracebacks. On PyPy, it is implemented in Python and adds 1 frame to
    tracebacks.

    Returns:
        int: Traceback frame count

    """
    
    def function_with_unique_name_xyzzy():
        
        try:
            1 / 0
            raise TrioInternalError("A ZeroDivisionError should have been raised, but it wasn't.")
        except ZeroDivisionError:
            raise 


    ctx = copy_context()
# WARNING: Decompyle incomplete

CONTEXT_RUN_TB_FRAMES: 'Final' = _count_context_run_tb_frames()
SystemClock = <NODE:12>()

class IdlePrimedTypes(enum.Enum):
    WAITING_FOR_IDLE = 1
    AUTOJUMP_CLOCK = 2


def collapse_exception_group(excgroup = None):
    '''Recursively collapse any single-exception groups into that single contained
    exception.

    '''
    exceptions = list(excgroup.exceptions)
    modified = False
    for i, exc in enumerate(exceptions):
        if isinstance(exc, BaseExceptionGroup):
            new_exc = collapse_exception_group(exc)
            if new_exc is not exc:
                modified = True
                exceptions[i] = new_exc
        if len(exceptions) == 1 and isinstance(excgroup, BaseExceptionGroup) and NONSTRICT_EXCEPTIONGROUP_NOTE in getattr(excgroup, '__notes__', ()):
            exceptions[0].__traceback__ = concat_tb(excgroup.__traceback__, exceptions[0].__traceback__)
            return exceptions[0]
        if None:
            return excgroup.derive(exceptions)
        return None

Deadlines = <NODE:12>()
CancelReason = <NODE:12>()
CancelStatus = <NODE:12>()
MISNESTING_ADVICE = "\nThis is probably a bug in your code, that has caused Trio's internal state to\nbecome corrupted. We'll do our best to recover, but from now on there are\nno guarantees.\n\nTypically this is caused by one of the following:\n  - yielding within a generator or async generator that's opened a cancel\n    scope or nursery (unless the generator is a @contextmanager or\n    @asynccontextmanager); see https://github.com/python-trio/trio/issues/638\n  - manually calling __enter__ or __exit__ on a trio.CancelScope, or\n    __aenter__ or __aexit__ on the object returned by trio.open_nursery();\n    doing so correctly is difficult and you should use @[async]contextmanager\n    instead, or maybe [Async]ExitStack\n  - using [Async]ExitStack to interleave the entries/exits of cancel scopes\n    and/or nurseries in a way that couldn't be achieved by some nesting of\n    'with' and 'async with' blocks\n  - using the low-level coroutine object protocol to execute some parts of\n    an async function in a different cancel scope/nursery context than\n    other parts\nIf you don't believe you're doing any of these things, please file a bug:\nhttps://github.com/python-trio/trio/issues/new\n"
CancelScope = <NODE:12>()()

def TaskStatus():
    '''TaskStatus'''
    __doc__ = 'The interface provided by :meth:`Nursery.start()` to the spawned task.\n\n    This is provided via the ``task_status`` keyword-only parameter.\n    '
    started = (lambda self = None: pass)()
    started = (lambda self = None, value = None: pass)()
    
    def started(self = None, value = None):
        '''Tasks call this method to indicate that they have initialized.

        See `nursery.start() <trio.Nursery.start>` for more information.
        '''
        pass


TaskStatus = <NODE:27>(TaskStatus, 'TaskStatus', Protocol[StatusT_contra])

def _TaskStatus():
    '''_TaskStatus'''
    _new_nursery: 'Nursery' = '_TaskStatus'
    _value: 'StatusT | type[_NoStatus]' = _NoStatus
    
    def __repr__(self = None):
        return f'''<Task status object at {id(self):#x}>'''

    started = (lambda self = None: pass)()
    started = (lambda self = None, value = None: pass)()
    
    def started(self = None, value = None):
        if self._value is not _NoStatus:
            raise RuntimeError("called 'started' twice on the same task status")
        self._value = cast('StatusT', value)
    # WARNING: Decompyle incomplete


_TaskStatus = <NODE:27>(_TaskStatus, '_TaskStatus', TaskStatus[StatusT])()
NurseryManager = <NODE:12>()

def open_nursery(strict_exception_groups = attrs.define(eq = False, repr = False)):
    '''Returns an async context manager which must be used to create a
    new `Nursery`.

    It does not block on entry; on exit it blocks until all child tasks
    have exited. If no child tasks are running on exit, it will insert a
    schedule point (but no cancellation point) - equivalent to
    :func:`trio.lowlevel.cancel_shielded_checkpoint`. This means a nursery
    is never the source of a cancellation exception, it only propagates it
    from sub-tasks.

    Args:
      strict_exception_groups (bool): Unless set to False, even a single raised exception
          will be wrapped in an exception group. If not specified, uses the value passed
          to :func:`run`, which defaults to true. Setting it to False will be deprecated
          and ultimately removed in a future version of Trio.

    '''
    pass
# WARNING: Decompyle incomplete


def Nursery():
    '''Nursery'''
    __doc__ = 'A context which may be used to spawn (or cancel) child tasks.\n\n    Not constructed directly, use `open_nursery` instead.\n\n    The nursery will remain open until all child tasks have completed,\n    or until it is cancelled, at which point it will cancel all its\n    remaining child tasks and close.\n\n    Nurseries ensure the absence of orphaned Tasks, since all running\n    tasks will belong to an open Nursery.\n\n    Attributes:\n        cancel_scope:\n            Creating a nursery also implicitly creates a cancellation scope,\n            which is exposed as the :attr:`cancel_scope` attribute. This is\n            used internally to implement the logic where if an error occurs\n            then ``__aexit__`` cancels all children, but you can use it for\n            other things, e.g. if you want to explicitly cancel all children\n            in response to some external event.\n    '
    
    def __init__(self = None, parent_task = None, cancel_scope = None, strict_exception_groups = ('parent_task', 'Task', 'cancel_scope', 'CancelScope', 'strict_exception_groups', 'bool', 'return', 'None')):
        self._parent_task = parent_task
        self._strict_exception_groups = strict_exception_groups
        parent_task._child_nurseries.append(self)
        self._cancel_status = parent_task._cancel_status
        self.cancel_scope = cancel_scope
    # WARNING: Decompyle incomplete

    child_tasks = (lambda self = None: frozenset(self._children))()
    parent_task = (lambda self = None: self._parent_task)()
    
    def _add_exc(self = None, exc = None, reason = None):
        self._pending_excs.append(exc)
        self.cancel_scope._cancel(reason)

    
    def _check_nursery_closed(self = None):
        if not any([
            self._nested_child_running,
            self._children,
            self._pending_starts]):
            self._closed = True
            if self._parent_waiting_in_aexit:
                self._parent_waiting_in_aexit = False
                GLOBAL_RUN_CONTEXT.runner.reschedule(self._parent_task)
                return None
            return None

    
    def _child_finished(self = None, task = None, outcome = None):
        self._children.remove(task)
        if not self._closed and hasattr(self, '_pending_excs'):
            return None
        if None(outcome, Error):
            self._add_exc(outcome.error, CancelReason(source = 'nursery', source_task = repr(task), reason = f'''child task raised exception {outcome.error!r}'''))
        self._check_nursery_closed()

    
    async def _nested_child_finished(self = None, nested_child_exc = None):
        pass
    # WARNING: Decompyle incomplete

    
    def start_soon(self = None, async_fn = None, *, name, *args):
        """Creates a child task, scheduling ``await async_fn(*args)``.

        If you want to run a function and immediately wait for its result,
        then you don't need a nursery; just use ``await async_fn(*args)``.
        If you want to wait for the task to initialize itself before
        continuing, see :meth:`start`, the other fundamental method for
        creating concurrent tasks in Trio.

        Note that this is *not* an async function and you don't use await
        when calling it. It sets up the new task, but then returns
        immediately, *before* the new task has a chance to do anything.
        New tasks may start running in any order, and at any checkpoint the
        scheduler chooses - at latest when the nursery is waiting to exit.

        It's possible to pass a nursery object into another task, which
        allows that task to start new child tasks in the first task's
        nursery.

        The child task inherits its parent nursery's cancel scopes.

        Args:
            async_fn: An async callable.
            args: Positional arguments for ``async_fn``. If you want
                  to pass keyword arguments, use
                  :func:`functools.partial`.
            name: The name for this task. Only used for
                  debugging/introspection
                  (e.g. ``repr(task_obj)``). If this isn't a string,
                  :meth:`start_soon` will try to make it one. A
                  common use case is if you're wrapping a function
                  before spawning a new task, you might pass the
                  original function as the ``name=`` to make
                  debugging easier.

        Raises:
            RuntimeError: If this nursery is no longer open
                          (i.e. its ``async with`` block has
                          exited).
        """
        GLOBAL_RUN_CONTEXT.runner.spawn_impl(async_fn, args, self, name)

    
    async def start(self = None, async_fn = None, *, name, *args):
        """Creates and initializes a child task.

        Like :meth:`start_soon`, but blocks until the new task has
        finished initializing itself, and optionally returns some
        information from it.

        The ``async_fn`` must accept a ``task_status`` keyword argument,
        and it must make sure that it (or someone) eventually calls
        :meth:`task_status.started() <TaskStatus.started>`.

        The conventional way to define ``async_fn`` is like::

            async def async_fn(arg1, arg2, *, task_status=trio.TASK_STATUS_IGNORED):
                ...  # Caller is blocked waiting for this code to run
                task_status.started()
                ...  # This async code can be interleaved with the caller

        :attr:`trio.TASK_STATUS_IGNORED` is a special global object with
        a do-nothing ``started`` method. This way your function supports
        being called either like ``await nursery.start(async_fn, arg1,
        arg2)`` or directly like ``await async_fn(arg1, arg2)``, and
        either way it can call :meth:`task_status.started() <TaskStatus.started>`
        without worrying about which mode it's in. Defining your function like
        this will make it obvious to readers that it supports being used
        in both modes.

        Before the child calls :meth:`task_status.started() <TaskStatus.started>`,
        it's effectively run underneath the call to :meth:`start`: if it
        raises an exception then that exception is reported by
        :meth:`start`, and does *not* propagate out of the nursery. If
        :meth:`start` is cancelled, then the child task is also
        cancelled.

        When the child calls :meth:`task_status.started() <TaskStatus.started>`,
        it's moved out from underneath :meth:`start` and into the given nursery.

        If the child task passes a value to :meth:`task_status.started(value) <TaskStatus.started>`,
        then :meth:`start` returns this value. Otherwise, it returns ``None``.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def __del__(self = None):
        pass
    # WARNING: Decompyle incomplete


Nursery = <NODE:27>(Nursery, 'Nursery', metaclass = NoPublicConstructor)()

def Task():
    '''Task'''
    context: 'contextvars.Context' = 'Task'
    _ki_protected: 'bool' = attrs.field(init = False, factory = itertools.count().__next__)
    _next_send_fn: 'Callable[[Any], object] | None' = None
    _next_send: 'Outcome[Any] | BaseException | None' = None
    _abort_func: 'Callable[[_core.RaiseCancelT], Abort] | None' = None
    custom_sleep_data: 'Any' = None
    _child_nurseries: 'list[Nursery]' = attrs.Factory(list)
    _eventual_parent_nursery: 'Nursery | None' = None
    _cancel_points: 'int' = 0
    _schedule_points: 'int' = 0
    
    def __repr__(self = None):
        return f'''<Task {self.name!r} at {id(self):#x}>'''

    parent_nursery = (lambda self = None: self._parent_nursery)()
    eventual_parent_nursery = (lambda self = None: self._eventual_parent_nursery)()
    child_nurseries = (lambda self = None: list(self._child_nurseries))()
    
    def iter_await_frames(self = None):
        '''Iterates recursively over the coroutine-like objects this
        task is waiting on, yielding the frame and line number at each
        frame.

        This is similar to `traceback.walk_stack` in a synchronous
        context. Note that `traceback.walk_stack` returns frames from
        the bottom of the call stack to the top, while this function
        starts from `Task.coro <trio.lowlevel.Task.coro>` and works it
        way down.

        Example usage: extracting a stack trace::

            import traceback

            def print_stack_for_task(task):
                ss = traceback.StackSummary.extract(task.iter_await_frames())
                print("".join(ss.format()))

        '''
        pass
    # WARNING: Decompyle incomplete

    _cancel_status: 'CancelStatus' = attrs.field(default = None, repr = False)
    
    def _activate_cancel_status(self = None, cancel_status = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _attempt_abort(self = None, raise_cancel = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _attempt_delivery_of_any_pending_cancel(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _attempt_delivery_of_pending_ki(self = None):
        pass
    # WARNING: Decompyle incomplete


Task = <NODE:27>(Task, 'Task', metaclass = NoPublicConstructor)()()
RunStatistics = <NODE:12>()
GuestState = <NODE:12>()
Runner = <NODE:12>()

def setup_runner(clock = attrs.frozen, instruments = attrs.define(eq = False), restrict_keyboard_interrupt_to_checkpoints = attrs.define(eq = False), strict_exception_groups = ('clock', 'Clock | None', 'instruments', 'Sequence[Instrument]', 'restrict_keyboard_interrupt_to_checkpoints', 'bool', 'strict_exception_groups', 'bool', 'return', 'Runner')):
    '''Create a Runner object and install it as the GLOBAL_RUN_CONTEXT.'''
    if in_trio_run():
        raise RuntimeError('Attempted to call run() from inside a run()')
# WARNING: Decompyle incomplete


def run(async_fn = final, *, clock, instruments, restrict_keyboard_interrupt_to_checkpoints, strict_exception_groups, *args):
    """Run a Trio-flavored async function, and return the result.

    Calling::

       run(async_fn, *args)

    is the equivalent of::

       await async_fn(*args)

    except that :func:`run` can (and must) be called from a synchronous
    context.

    This is Trio's main entry point. Almost every other function in Trio
    requires that you be inside a call to :func:`run`.

    Args:
      async_fn: An async function.

      args: Positional arguments to be passed to *async_fn*. If you need to
          pass keyword arguments, then use :func:`functools.partial`.

      clock: ``None`` to use the default system-specific monotonic clock;
          otherwise, an object implementing the :class:`trio.abc.Clock`
          interface, like (for example) a :class:`trio.testing.MockClock`
          instance.

      instruments (list of :class:`trio.abc.Instrument` objects): Any
          instrumentation you want to apply to this run. This can also be
          modified during the run; see :ref:`instrumentation`.

      restrict_keyboard_interrupt_to_checkpoints (bool): What happens if the
          user hits control-C while :func:`run` is running? If this argument
          is False (the default), then you get the standard Python behavior: a
          :exc:`KeyboardInterrupt` exception will immediately interrupt
          whatever task is running (or if no task is running, then Trio will
          wake up a task to be interrupted). Alternatively, if you set this
          argument to True, then :exc:`KeyboardInterrupt` delivery will be
          delayed: it will be *only* be raised at :ref:`checkpoints
          <checkpoints>`, like a :exc:`Cancelled` exception.

          The default behavior is nice because it means that even if you
          accidentally write an infinite loop that never executes any
          checkpoints, then you can still break out of it using control-C.
          The alternative behavior is nice if you're paranoid about a
          :exc:`KeyboardInterrupt` at just the wrong place leaving your
          program in an inconsistent state, because it means that you only
          have to worry about :exc:`KeyboardInterrupt` at the exact same
          places where you already have to worry about :exc:`Cancelled`.

          This setting has no effect if your program has registered a custom
          SIGINT handler, or if :func:`run` is called from anywhere but the
          main thread (this is a Python limitation), or if you use
          :func:`open_signal_receiver` to catch SIGINT.

      strict_exception_groups (bool): Unless set to False, nurseries will always wrap
          even a single raised exception in an exception group. This can be overridden
          on the level of individual nurseries. Setting it to False will be deprecated
          and ultimately removed in a future version of Trio.

    Returns:
      Whatever ``async_fn`` returns.

    Raises:
      TrioInternalError: if an unexpected error is encountered inside Trio's
          internal machinery. This is a bug and you should `let us know
          <https://github.com/python-trio/trio/issues>`__.

      Anything else: if ``async_fn`` raises an exception, then :func:`run`
          propagates it.

    """
    pass
# WARNING: Decompyle incomplete


def start_guest_run(async_fn = None, *, run_sync_soon_threadsafe, done_callback, run_sync_soon_not_threadsafe, host_uses_signal_set_wakeup_fd, clock, instruments, restrict_keyboard_interrupt_to_checkpoints, strict_exception_groups, *args):
    '''Start a "guest" run of Trio on top of some other "host" event loop.

    Each host loop can only have one guest run at a time.

    You should always let the Trio run finish before stopping the host loop;
    if not, it may leave Trio\'s internal data structures in an inconsistent
    state. You might be able to get away with it if you immediately exit the
    program, but it\'s safest not to go there in the first place.

    Generally, the best way to do this is wrap this in a function that starts
    the host loop and then immediately starts the guest run, and then shuts
    down the host when the guest run completes.

    Once :func:`start_guest_run` returns successfully, the guest run
    has been set up enough that you can invoke sync-colored Trio
    functions such as :func:`~trio.current_time`, :func:`spawn_system_task`,
    and :func:`current_trio_token`. If a `~trio.TrioInternalError` occurs
    during this early setup of the guest run, it will be raised out of
    :func:`start_guest_run`.  All other errors, including all errors
    raised by the *async_fn*, will be delivered to your
    *done_callback* at some point after :func:`start_guest_run` returns
    successfully.

    Args:

      run_sync_soon_threadsafe: An arbitrary callable, which will be passed a
         function as its sole argument::

            def my_run_sync_soon_threadsafe(fn):
                ...

         This callable should schedule ``fn()`` to be run by the host on its
         next pass through its loop. **Must support being called from
         arbitrary threads.**

      done_callback: An arbitrary callable::

            def my_done_callback(run_outcome):
                ...

         When the Trio run has finished, Trio will invoke this callback to let
         you know. The argument is an `outcome.Outcome`, reporting what would
         have been returned or raised by `trio.run`. This function can do
         anything you want, but commonly you\'ll want it to shut down the
         host loop, unwrap the outcome, etc.

      run_sync_soon_not_threadsafe: Like ``run_sync_soon_threadsafe``, but
         will only be called from inside the host loop\'s main thread.
         Optional, but if your host loop allows you to implement this more
         efficiently than ``run_sync_soon_threadsafe`` then passing it will
         make things a bit faster.

      host_uses_signal_set_wakeup_fd (bool): Pass `True` if your host loop
         uses `signal.set_wakeup_fd`, and `False` otherwise. For more details,
         see :ref:`guest-run-implementation`.

    For the meaning of other arguments, see `trio.run`.

    '''
    pass
# WARNING: Decompyle incomplete

_MAX_TIMEOUT: 'Final' = 86400
unrolled_run = (lambda runner = None, async_fn = None, args = enable_ki_protection, host_uses_signal_set_wakeup_fd = (False,): pass# WARNING: Decompyle incomplete
)()

def _TaskStatusIgnored():
    '''_TaskStatusIgnored'''
    
    def __repr__(self = None):
        return 'TASK_STATUS_IGNORED'

    
    def started(self = None, value = None):
        pass


_TaskStatusIgnored = <NODE:27>(_TaskStatusIgnored, '_TaskStatusIgnored', TaskStatus[object])
TASK_STATUS_IGNORED: 'Final[TaskStatus[object]]' = _TaskStatusIgnored()

def current_task():
    '''Return the :class:`Task` object representing the current task.

    Returns:
      Task: the :class:`Task` that called :func:`current_task`.

    '''
    
    try:
        return GLOBAL_RUN_CONTEXT.task
    except AttributeError:
        raise RuntimeError('must be called from async context'), None



def current_effective_deadline():
    """Returns the current effective deadline for the current task.

    This function examines all the cancellation scopes that are currently in
    effect (taking into account shielding), and returns the deadline that will
    expire first.

    One example of where this might be is useful is if your code is trying to
    decide whether to begin an expensive operation like an RPC call, but wants
    to skip it if it knows that it can't possibly complete in the available
    time. Another example would be if you're using a protocol like gRPC that
    `propagates timeout information to the remote peer
    <http://www.grpc.io/docs/guides/concepts.html#deadlines>`__; this function
    gives a way to fetch that information so you can send it along.

    If this is called in a context where a cancellation is currently active
    (i.e., a blocking call will immediately raise :exc:`Cancelled`), then
    returned deadline is ``-inf``. If it is called in a context where no
    scopes have a deadline set, it returns ``inf``.

    Returns:
        float: the effective deadline, as an absolute time.

    """
    return current_task()._cancel_status.effective_deadline()


async def checkpoint():
    '''A pure :ref:`checkpoint <checkpoints>`.

    This checks for cancellation and allows other tasks to be scheduled,
    without otherwise blocking.

    Note that the scheduler has the option of ignoring this and continuing to
    run the current task if it decides this is appropriate (e.g. for increased
    efficiency).

    Equivalent to ``await trio.sleep(0)`` (which is implemented by calling
    :func:`checkpoint`.)

    '''
    pass
# WARNING: Decompyle incomplete


async def checkpoint_if_cancelled():
    '''Issue a :ref:`checkpoint <checkpoints>` if the calling context has been
    cancelled.

    Equivalent to (but potentially more efficient than)::

        if trio.current_effective_deadline() == -inf:
            await trio.lowlevel.checkpoint()

    This is either a no-op, or else it allow other tasks to be scheduled and
    then raises :exc:`trio.Cancelled`.

    Typically used together with :func:`cancel_shielded_checkpoint`.

    '''
    pass
# WARNING: Decompyle incomplete


def in_trio_run():
    '''Check whether we are in a Trio run.
    This returns `True` if and only if :func:`~trio.current_time` will succeed.

    See also the discussion of differing ways of :ref:`detecting Trio <trio_contexts>`.
    '''
    return hasattr(GLOBAL_RUN_CONTEXT, 'runner')


def in_trio_task():
    '''Check whether we are in a Trio task.
    This returns `True` if and only if :func:`~trio.lowlevel.current_task` will succeed.

    See also the discussion of differing ways of :ref:`detecting Trio <trio_contexts>`.
    '''
    return hasattr(GLOBAL_RUN_CONTEXT, 'task')

if 'sphinx.ext.autodoc' in sys.modules:
    from _generated_io_epoll import *
    from _generated_io_kqueue import *
    from _generated_io_windows import *
if sys.platform == 'win32':
    from _generated_io_windows import *
    from _io_windows import EventResult, WindowsIOManager as TheIOManager, _WindowsStatistics as IOStatistics
elif (sys.platform == 'linux' or TYPE_CHECKING) and hasattr(select, 'epoll'):
    from _generated_io_epoll import *
    from _io_epoll import EpollIOManager as TheIOManager, EventResult, _EpollStatistics as IOStatistics
elif TYPE_CHECKING or hasattr(select, 'kqueue'):
    from _generated_io_kqueue import *
    from _io_kqueue import EventResult, KqueueIOManager as TheIOManager, _KqueueStatistics as IOStatistics
else:
    _patchers = sorted({
        'eventlet',
        'gevent'}.intersection(sys.modules))
    if _patchers:
        raise NotImplementedError('unsupported platform or primitives Trio depends on are monkey-patched out by ' + ', '.join(_patchers))
    raise NotImplementedError('unsupported platform')
from _generated_instrumentation import *
from _generated_run import *
