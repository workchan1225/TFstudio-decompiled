# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _synchronization.pyc (Python 3.11)

from __future__ import annotations
import math
from collections import deque
from collections.abc import Callable
from dataclasses import dataclass
from types import TracebackType
from typing import TypeVar
from lowlevel import checkpoint_if_cancelled
from _eventloop import NoCurrentAsyncBackend, get_async_backend
from _exceptions import BusyResourceError
from _tasks import CancelScope
from _testing import TaskInfo, get_current_task
T = TypeVar('T')
EventStatistics = <NODE:12>()
CapacityLimiterStatistics = <NODE:12>()
LockStatistics = <NODE:12>()
ConditionStatistics = <NODE:12>()
SemaphoreStatistics = <NODE:12>()

class Event:
    
    def __new__(cls = None):
        
        try:
            return get_async_backend().create_event()
        except NoCurrentAsyncBackend:
            return 


    
    def set(self = None):
        '''Set the flag, notifying all listeners.'''
        raise NotImplementedError

    
    def is_set(self = None):
        '''Return ``True`` if the flag is set, ``False`` if not.'''
        raise NotImplementedError

    
    async def wait(self = None):
        '''
        Wait until the flag has been set.

        If the flag has already been set when this method is called, it returns
        immediately.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def statistics(self = None):
        '''Return statistics about the current state of this event.'''
        raise NotImplementedError



class EventAdapter(Event):
    _internal_event: 'Event | None' = None
    _is_set: 'bool' = False
    
    def __new__(cls = None):
        return object.__new__(cls)

    _event = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def set(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_set(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def wait(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def statistics(self = None):
        pass
    # WARNING: Decompyle incomplete



class Lock:
    
    def __new__(cls = None, *, fast_acquire):
        
        try:
            return get_async_backend().create_lock(fast_acquire = fast_acquire)
        except NoCurrentAsyncBackend:
            return 


    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    async def acquire(self = None):
        '''Acquire the lock.'''
        pass
    # WARNING: Decompyle incomplete

    
    def acquire_nowait(self = None):
        '''
        Acquire the lock, without blocking.

        :raises ~anyio.WouldBlock: if the operation would block

        '''
        raise NotImplementedError

    
    def release(self = None):
        '''Release the lock.'''
        raise NotImplementedError

    
    def locked(self = None):
        '''Return True if the lock is currently held.'''
        raise NotImplementedError

    
    def statistics(self = None):
        '''
        Return statistics about the current state of this lock.

        .. versionadded:: 3.0
        '''
        raise NotImplementedError



class LockAdapter(Lock):
    _internal_lock: 'Lock | None' = None
    
    def __new__(cls = None, *, fast_acquire):
        return object.__new__(cls)

    
    def __init__(self = None, *, fast_acquire):
        self._fast_acquire = fast_acquire

    _lock = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    async def acquire(self = None):
        '''Acquire the lock.'''
        pass
    # WARNING: Decompyle incomplete

    
    def acquire_nowait(self = None):
        '''
        Acquire the lock, without blocking.

        :raises ~anyio.WouldBlock: if the operation would block

        '''
        self._lock.acquire_nowait()

    
    def release(self = None):
        '''Release the lock.'''
        self._lock.release()

    
    def locked(self = None):
        '''Return True if the lock is currently held.'''
        return self._lock.locked()

    
    def statistics(self = None):
        '''
        Return statistics about the current state of this lock.

        .. versionadded:: 3.0

        '''
        pass
    # WARNING: Decompyle incomplete



class Condition:
    _owner_task: 'TaskInfo | None' = None
    
    def __init__(self = None, lock = None):
        if not lock:
            pass
        self._lock = Lock()
        self._waiters = deque()

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _check_acquired(self = None):
        if self._owner_task != get_current_task():
            raise RuntimeError('The current task is not holding the underlying lock')

    
    async def acquire(self = None):
        '''Acquire the underlying lock.'''
        pass
    # WARNING: Decompyle incomplete

    
    def acquire_nowait(self = None):
        '''
        Acquire the underlying lock, without blocking.

        :raises ~anyio.WouldBlock: if the operation would block

        '''
        self._lock.acquire_nowait()
        self._owner_task = get_current_task()

    
    def release(self = None):
        '''Release the underlying lock.'''
        self._lock.release()

    
    def locked(self = None):
        '''Return True if the lock is set.'''
        return self._lock.locked()

    
    def notify(self = None, n = None):
        '''Notify exactly n listeners.'''
        self._check_acquired()
        for _ in range(n):
            event = self._waiters.popleft()
        except IndexError:
            return None
        event.set()
        continue

    
    def notify_all(self = None):
        '''Notify all the listeners.'''
        self._check_acquired()
        for event in self._waiters:
            event.set()
            self._waiters.clear()
            return None

    
    async def wait(self = None):
        '''Wait for a notification.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def wait_for(self = None, predicate = None):
        '''
        Wait until a predicate becomes true.

        :param predicate: a callable that returns a truthy value when the condition is
            met
        :return: the result of the predicate

        .. versionadded:: 4.11.0

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def statistics(self = None):
        '''
        Return statistics about the current state of this condition.

        .. versionadded:: 3.0
        '''
        return ConditionStatistics(len(self._waiters), self._lock.statistics())



class Semaphore:
    
    def __new__(cls = None, initial_value = None, *, max_value, fast_acquire):
        
        try:
            return get_async_backend().create_semaphore(initial_value, max_value = max_value, fast_acquire = fast_acquire)
        except NoCurrentAsyncBackend:
            return 


    
    def __init__(self = None, initial_value = None, *, max_value, fast_acquire):
        if not isinstance(initial_value, int):
            raise TypeError('initial_value must be an integer')
        if initial_value < 0:
            raise ValueError('initial_value must be >= 0')
    # WARNING: Decompyle incomplete

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    async def acquire(self = None):
        '''Decrement the semaphore value, blocking if necessary.'''
        pass
    # WARNING: Decompyle incomplete

    
    def acquire_nowait(self = None):
        '''
        Acquire the underlying lock, without blocking.

        :raises ~anyio.WouldBlock: if the operation would block

        '''
        raise NotImplementedError

    
    def release(self = None):
        '''Increment the semaphore value.'''
        raise NotImplementedError

    value = (lambda self = None: raise NotImplementedError)()
    max_value = (lambda self = None: raise NotImplementedError)()
    
    def statistics(self = None):
        '''
        Return statistics about the current state of this semaphore.

        .. versionadded:: 3.0
        '''
        raise NotImplementedError



class SemaphoreAdapter(Semaphore):
    pass
# WARNING: Decompyle incomplete


class CapacityLimiter:
    
    def __new__(cls = None, total_tokens = None):
        
        try:
            return get_async_backend().create_capacity_limiter(total_tokens)
        except NoCurrentAsyncBackend:
            return 


    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    total_tokens = (lambda self = None: raise NotImplementedError)()
    total_tokens = (lambda self = None, value = None: raise NotImplementedError)()
    borrowed_tokens = (lambda self = None: raise NotImplementedError)()
    available_tokens = (lambda self = None: raise NotImplementedError)()
    
    def acquire_nowait(self = None):
        '''
        Acquire a token for the current task without waiting for one to become
        available.

        :raises ~anyio.WouldBlock: if there are no tokens available for borrowing

        '''
        raise NotImplementedError

    
    def acquire_on_behalf_of_nowait(self = None, borrower = None):
        '''
        Acquire a token without waiting for one to become available.

        :param borrower: the entity borrowing a token
        :raises ~anyio.WouldBlock: if there are no tokens available for borrowing

        '''
        raise NotImplementedError

    
    async def acquire(self = None):
        '''
        Acquire a token for the current task, waiting if necessary for one to become
        available.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def acquire_on_behalf_of(self = None, borrower = None):
        '''
        Acquire a token, waiting if necessary for one to become available.

        :param borrower: the entity borrowing a token

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def release(self = None):
        '''
        Release the token held by the current task.

        :raises RuntimeError: if the current task has not borrowed a token from this
            limiter.

        '''
        raise NotImplementedError

    
    def release_on_behalf_of(self = None, borrower = None):
        '''
        Release the token held by the given borrower.

        :raises RuntimeError: if the borrower has not borrowed a token from this
            limiter.

        '''
        raise NotImplementedError

    
    def statistics(self = None):
        '''
        Return statistics about the current state of this limiter.

        .. versionadded:: 3.0

        '''
        raise NotImplementedError



class CapacityLimiterAdapter(CapacityLimiter):
    _internal_limiter: 'CapacityLimiter | None' = None
    
    def __new__(cls = None, total_tokens = None):
        return object.__new__(cls)

    
    def __init__(self = None, total_tokens = None):
        self.total_tokens = total_tokens

    _limiter = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    total_tokens = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    total_tokens = (lambda self = None, value = None: if isinstance(value, int) and value is not math.inf:
raise TypeError('total_tokens must be an int or math.inf')if value < 1:
raise ValueError('total_tokens must be >= 1')# WARNING: Decompyle incomplete
)()
    borrowed_tokens = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    available_tokens = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def acquire_nowait(self = None):
        self._limiter.acquire_nowait()

    
    def acquire_on_behalf_of_nowait(self = None, borrower = None):
        self._limiter.acquire_on_behalf_of_nowait(borrower)

    
    async def acquire(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def acquire_on_behalf_of(self = None, borrower = None):
        pass
    # WARNING: Decompyle incomplete

    
    def release(self = None):
        self._limiter.release()

    
    def release_on_behalf_of(self = None, borrower = None):
        self._limiter.release_on_behalf_of(borrower)

    
    def statistics(self = None):
        pass
    # WARNING: Decompyle incomplete



class ResourceGuard:
    '''
    A context manager for ensuring that a resource is only used by a single task at a
    time.

    Entering this context manager while the previous has not exited it yet will trigger
    :exc:`BusyResourceError`.

    :param action: the action to guard against (visible in the :exc:`BusyResourceError`
        when triggered, e.g. "Another task is already {action} this resource")

    .. versionadded:: 4.1
    '''
    __slots__ = ('action', '_guarded')
    
    def __init__(self = None, action = None):
        self.action = action
        self._guarded = False

    
    def __enter__(self = None):
        if self._guarded:
            raise BusyResourceError(self.action)
        self._guarded = True

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        self._guarded = False
