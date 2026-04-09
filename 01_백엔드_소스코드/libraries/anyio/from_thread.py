# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: from_thread.pyc (Python 3.11)

from __future__ import annotations
__all__ = ('BlockingPortal', 'BlockingPortalProvider', 'check_cancelled', 'run', 'run_sync', 'start_blocking_portal')
import sys
from collections.abc import Awaitable, Callable, Generator
from concurrent.futures import Future
from contextlib import AbstractAsyncContextManager, AbstractContextManager, contextmanager
from dataclasses import dataclass, field
from inspect import isawaitable
from threading import Lock, Thread, current_thread, get_ident
from types import TracebackType
from typing import Any, Generic, TypeVar, cast, overload
from _core._eventloop import get_async_backend, get_cancelled_exc_class, threadlocals
from _core._eventloop import run as run_eventloop
from _core._exceptions import NoEventLoopError
from _core._synchronization import Event
from _core._tasks import CancelScope, create_task_group
from abc._tasks import TaskStatus
from lowlevel import EventLoopToken
if sys.version_info >= (3, 11):
    from typing import TypeVarTuple, Unpack
else:
    from typing_extensions import TypeVarTuple, Unpack
T_Retval = TypeVar('T_Retval')
T_co = TypeVar('T_co', covariant = True)
PosArgsT = TypeVarTuple('PosArgsT')

def _token_or_error(token = None):
    pass
# WARNING: Decompyle incomplete


def run(func = None, *, token, *args):
    '''
    Call a coroutine function from a worker thread.

    :param func: a coroutine function
    :param args: positional arguments for the callable
    :param token: an event loop token to use to get back to the event loop thread
        (required if calling this function from outside an AnyIO worker thread)
    :return: the return value of the coroutine function
    :raises MissingTokenError: if no token was provided and called from outside an
        AnyIO worker thread
    :raises RunFinishedError: if the event loop tied to ``token`` is no longer running

    .. versionchanged:: 4.11.0
        Added the ``token`` parameter.

    '''
    explicit_token = token is not None
    token = _token_or_error(token)
    return token.backend_class.run_async_from_thread(func, args, token = token.native_token if explicit_token else None)


def run_sync(func = None, *, token, *args):
    '''
    Call a function in the event loop thread from a worker thread.

    :param func: a callable
    :param args: positional arguments for the callable
    :param token: an event loop token to use to get back to the event loop thread
        (required if calling this function from outside an AnyIO worker thread)
    :return: the return value of the callable
    :raises MissingTokenError: if no token was provided and called from outside an
        AnyIO worker thread
    :raises RunFinishedError: if the event loop tied to ``token`` is no longer running

    .. versionchanged:: 4.11.0
        Added the ``token`` parameter.

    '''
    explicit_token = token is not None
    token = _token_or_error(token)
    return token.backend_class.run_sync_from_thread(func, args, token = token.native_token if explicit_token else None)


def _BlockingAsyncContextManager():
    '''_BlockingAsyncContextManager'''
    _exit_event: 'Event' = '_BlockingAsyncContextManager'
    _exit_exc_info: 'tuple[type[BaseException] | None, BaseException | None, TracebackType | None]' = (None, None, None)
    
    def __init__(self = None, async_cm = None, portal = None):
        self._async_cm = async_cm
        self._portal = portal

    
    async def run_async_cm(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __enter__(self = None):
        self._enter_future = Future()
        self._exit_future = self._portal.start_task_soon(self.run_async_cm)
        return self._enter_future.result()

    
    def __exit__(self = None, _BlockingAsyncContextManager__exc_type = None, _BlockingAsyncContextManager__exc_value = None, _BlockingAsyncContextManager__traceback = ('_BlockingAsyncContextManager__exc_type', 'type[BaseException] | None', '_BlockingAsyncContextManager__exc_value', 'BaseException | None', '_BlockingAsyncContextManager__traceback', 'TracebackType | None', 'return', 'bool | None')):
        self._exit_exc_info = (_BlockingAsyncContextManager__exc_type, _BlockingAsyncContextManager__exc_value, _BlockingAsyncContextManager__traceback)
        self._portal.call(self._exit_event.set)
        return self._exit_future.result()


_BlockingAsyncContextManager = <NODE:27>(_BlockingAsyncContextManager, '_BlockingAsyncContextManager', Generic[T_co], AbstractContextManager)

class _BlockingPortalTaskStatus(TaskStatus):
    
    def __init__(self = None, future = None):
        self._future = future

    
    def started(self = None, value = None):
        self._future.set_result(value)



class BlockingPortal:
    '''An object that lets external threads run code in an asynchronous event loop.'''
    
    def __new__(cls = None):
        return get_async_backend().create_blocking_portal()

    
    def __init__(self = None):
        self._event_loop_thread_id = get_ident()
        self._stop_event = Event()
        self._task_group = create_task_group()
        self._cancelled_exc_class = get_cancelled_exc_class()

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'bool')):
        pass
    # WARNING: Decompyle incomplete

    
    def _check_running(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def sleep_until_stopped(self = None):
        '''Sleep until :meth:`stop` is called.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def stop(self = None, cancel_remaining = None):
        '''
        Signal the portal to shut down.

        This marks the portal as no longer accepting new calls and exits from
        :meth:`sleep_until_stopped`.

        :param cancel_remaining: ``True`` to cancel all the remaining tasks, ``False``
            to let them finish before returning

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def _call_func(self, func = None, args = None, kwargs = None, future = ('func', 'Callable[[Unpack[PosArgsT]], Awaitable[T_Retval] | T_Retval]', 'args', 'tuple[Unpack[PosArgsT]]', 'kwargs', 'dict[str, Any]', 'future', 'Future[T_Retval]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _spawn_task_from_thread(self, func, args = None, kwargs = None, name = None, future = ('func', 'Callable[[Unpack[PosArgsT]], Awaitable[T_Retval] | T_Retval]', 'args', 'tuple[Unpack[PosArgsT]]', 'kwargs', 'dict[str, Any]', 'name', 'object', 'future', 'Future[T_Retval]', 'return', 'None')):
        '''
        Spawn a new task using the given callable.

        Implementers must ensure that the future is resolved when the task finishes.

        :param func: a callable
        :param args: positional arguments to be passed to the callable
        :param kwargs: keyword arguments to be passed to the callable
        :param name: name of the task (will be coerced to a string if not ``None``)
        :param future: a future that will resolve to the return value of the callable,
            or the exception raised during its execution

        '''
        raise NotImplementedError

    call = (lambda self = None, func = None: pass)()
    call = (lambda self = None, func = None: pass)()
    
    def call(self = None, func = None, *args):
        '''
        Call the given function in the event loop thread.

        If the callable returns a coroutine object, it is awaited on.

        :param func: any callable
        :raises RuntimeError: if the portal is not running or if this method is called
            from within the event loop thread

        '''
        pass
    # WARNING: Decompyle incomplete

    start_task_soon = (lambda self = None, func = None, *, name, args = None: pass)()
    start_task_soon = (lambda self = None, func = None, *, name, args = None: pass)()
    
    def start_task_soon(self = None, func = None, *, name, *args):
        """
        Start a task in the portal's task group.

        The task will be run inside a cancel scope which can be cancelled by cancelling
        the returned future.

        :param func: the target function
        :param args: positional arguments passed to ``func``
        :param name: name of the task (will be coerced to a string if not ``None``)
        :return: a future that resolves with the return value of the callable if the
            task completes successfully, or with the exception raised in the task
        :raises RuntimeError: if the portal is not running or if this method is called
            from within the event loop thread
        :rtype: concurrent.futures.Future[T_Retval]

        .. versionadded:: 3.0

        """
        self._check_running()
        f = Future()
        self._spawn_task_from_thread(func, args, { }, name, f)
        return f

    
    def start_task(self = None, func = None, *, name, *args):
        """
        Start a task in the portal's task group and wait until it signals for readiness.

        This method works the same way as :meth:`.abc.TaskGroup.start`.

        :param func: the target function
        :param args: positional arguments passed to ``func``
        :param name: name of the task (will be coerced to a string if not ``None``)
        :return: a tuple of (future, task_status_value) where the ``task_status_value``
            is the value passed to ``task_status.started()`` from within the target
            function
        :rtype: tuple[concurrent.futures.Future[T_Retval], Any]

        .. versionadded:: 3.0

        """
        pass
    # WARNING: Decompyle incomplete

    
    def wrap_async_context_manager(self = None, cm = None):
        '''
        Wrap an async context manager as a synchronous context manager via this portal.

        Spawns a task that will call both ``__aenter__()`` and ``__aexit__()``, stopping
        in the middle until the synchronous context manager exits.

        :param cm: an asynchronous context manager
        :return: a synchronous context manager

        .. versionadded:: 2.1

        '''
        return _BlockingAsyncContextManager(cm, self)


BlockingPortalProvider = <NODE:12>()
start_blocking_portal = (lambda backend = None, backend_options = None, *, name, run_blocking_portal = None: pass# WARNING: Decompyle incomplete
)()

def check_cancelled():
    """
    Check if the cancel scope of the host task's running the current worker thread has
    been cancelled.

    If the host task's current cancel scope has indeed been cancelled, the
    backend-specific cancellation exception will be raised.

    :raises RuntimeError: if the current thread was not spawned by
        :func:`.to_thread.run_sync`

    """
    
    try:
        token = threadlocals.current_token
    except AttributeError:
        raise NoEventLoopError('This function can only be called inside an AnyIO worker thread'), None

    token.backend_class.check_cancelled()
