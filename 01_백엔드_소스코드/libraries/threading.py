# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: threading.pyc (Python 3.11)

"""Thread module emulating a subset of Java's threading model."""
import os as _os
import sys as _sys
import _thread
import functools
from time import monotonic as _time
from _weakrefset import WeakSet
from itertools import islice as _islice, count as _count

try:
    from _collections import deque as _deque
except ImportError:
    from collections import deque as _deque

__all__ = [
    'get_ident',
    'active_count',
    'Condition',
    'current_thread',
    'enumerate',
    'main_thread',
    'TIMEOUT_MAX',
    'Event',
    'Lock',
    'RLock',
    'Semaphore',
    'BoundedSemaphore',
    'Thread',
    'Barrier',
    'BrokenBarrierError',
    'Timer',
    'ThreadError',
    'setprofile',
    'settrace',
    'local',
    'stack_size',
    'excepthook',
    'ExceptHookArgs',
    'gettrace',
    'getprofile']
_start_new_thread = _thread.start_new_thread
_allocate_lock = _thread.allocate_lock
_set_sentinel = _thread._set_sentinel
get_ident = _thread.get_ident

try:
    get_native_id = _thread.get_native_id
    _HAVE_THREAD_NATIVE_ID = True
    __all__.append('get_native_id')
except AttributeError:
    _HAVE_THREAD_NATIVE_ID = False

ThreadError = _thread.error

try:
    _CRLock = _thread.RLock
except AttributeError:
    _CRLock = None

TIMEOUT_MAX = _thread.TIMEOUT_MAX
del _thread
_profile_hook = None
_trace_hook = None

def setprofile(func):
    '''Set a profile function for all threads started from the threading module.

    The func will be passed to sys.setprofile() for each thread, before its
    run() method is called.

    '''
    global _profile_hook
    _profile_hook = func


def getprofile():
    '''Get the profiler function as set by threading.setprofile().'''
    return _profile_hook


def settrace(func):
    '''Set a trace function for all threads started from the threading module.

    The func will be passed to sys.settrace() for each thread, before its run()
    method is called.

    '''
    global _trace_hook
    _trace_hook = func


def gettrace():
    '''Get the trace function as set by threading.settrace().'''
    return _trace_hook

Lock = _allocate_lock

def RLock(*args, **kwargs):
    '''Factory function that returns a new reentrant lock.

    A reentrant lock must be released by the thread that acquired it. Once a
    thread has acquired a reentrant lock, the same thread may acquire it again
    without blocking; the thread must release it once for each time it has
    acquired it.

    '''
    pass
# WARNING: Decompyle incomplete


class _RLock:
    '''This class implements reentrant lock objects.

    A reentrant lock must be released by the thread that acquired it. Once a
    thread has acquired a reentrant lock, the same thread may acquire it
    again without blocking; the thread must release it once for each time it
    has acquired it.

    '''
    
    def __init__(self):
        self._block = _allocate_lock()
        self._owner = None
        self._count = 0

    
    def __repr__(self):
        owner = self._owner
        
        try:
            owner = _active[owner].name
        except KeyError:
            pass

        return '<%s %s.%s object owner=%r count=%d at %s>' % ('locked' if self._block.locked() else 'unlocked', self.__class__.__module__, self.__class__.__qualname__, owner, self._count, hex(id(self)))

    
    def _at_fork_reinit(self):
        self._block._at_fork_reinit()
        self._owner = None
        self._count = 0

    
    def acquire(self, blocking, timeout = (True, -1)):
        '''Acquire a lock, blocking or non-blocking.

        When invoked without arguments: if this thread already owns the lock,
        increment the recursion level by one, and return immediately. Otherwise,
        if another thread owns the lock, block until the lock is unlocked. Once
        the lock is unlocked (not owned by any thread), then grab ownership, set
        the recursion level to one, and return. If more than one thread is
        blocked waiting until the lock is unlocked, only one at a time will be
        able to grab ownership of the lock. There is no return value in this
        case.

        When invoked with the blocking argument set to true, do the same thing
        as when called without arguments, and return true.

        When invoked with the blocking argument set to false, do not block. If a
        call without an argument would block, return false immediately;
        otherwise, do the same thing as when called without arguments, and
        return true.

        When invoked with the floating-point timeout argument set to a positive
        value, block for at most the number of seconds specified by timeout
        and as long as the lock cannot be acquired.  Return true if the lock has
        been acquired, false if the timeout has elapsed.

        '''
        me = get_ident()
        if self._owner == me:
            return 1
        None._block.acquire(blocking, timeout) = None
        if rc:
            self._owner = me
            self._count = 1
        return rc

    __enter__ = acquire
    
    def release(self):
        '''Release a lock, decrementing the recursion level.

        If after the decrement it is zero, reset the lock to unlocked (not owned
        by any thread), and if any other threads are blocked waiting for the
        lock to become unlocked, allow exactly one of them to proceed. If after
        the decrement the recursion level is still nonzero, the lock remains
        locked and owned by the calling thread.

        Only call this method when the calling thread owns the lock. A
        RuntimeError is raised if this method is called when the lock is
        unlocked.

        There is no return value.

        '''
        if self._owner != get_ident():
            raise RuntimeError('cannot release un-acquired lock')
        self._count = self._count - 1
        count = self._count - 1
        if not count:
            self._owner = None
            self._block.release()
            return None

    
    def __exit__(self, t, v, tb):
        self.release()

    
    def _acquire_restore(self, state):
        self._block.acquire()
        (self._count, self._owner) = state

    
    def _release_save(self):
        if self._count == 0:
            raise RuntimeError('cannot release un-acquired lock')
        count = self._count
        self._count = 0
        owner = self._owner
        self._owner = None
        self._block.release()
        return (count, owner)

    
    def _is_owned(self):
        return self._owner == get_ident()

    
    def _recursion_count(self):
        if self._owner != get_ident():
            return 0
        return None._count


_PyRLock = _RLock

class Condition:
    '''Class that implements a condition variable.

    A condition variable allows one or more threads to wait until they are
    notified by another thread.

    If the lock argument is given and not None, it must be a Lock or RLock
    object, and it is used as the underlying lock. Otherwise, a new RLock object
    is created and used as the underlying lock.

    '''
    
    def __init__(self, lock = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _at_fork_reinit(self):
        self._lock._at_fork_reinit()
        self._waiters.clear()

    
    def __enter__(self):
        return self._lock.__enter__()

    
    def __exit__(self, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return '<Condition(%s, %d)>' % (self._lock, len(self._waiters))

    
    def _release_save(self):
        self._lock.release()

    
    def _acquire_restore(self, x):
        self._lock.acquire()

    
    def _is_owned(self):
        if self._lock.acquire(False):
            self._lock.release()
            return False

    
    def wait(self, timeout = (None,)):
        '''Wait until notified or until a timeout occurs.

        If the calling thread has not acquired the lock when this method is
        called, a RuntimeError is raised.

        This method releases the underlying lock, and then blocks until it is
        awakened by a notify() or notify_all() call for the same condition
        variable in another thread, or until the optional timeout occurs. Once
        awakened or timed out, it re-acquires the lock and returns.

        When the timeout argument is present and not None, it should be a
        floating point number specifying a timeout for the operation in seconds
        (or fractions thereof).

        When the underlying lock is an RLock, it is not released using its
        release() method, since this may not actually unlock the lock when it
        was acquired multiple times recursively. Instead, an internal interface
        of the RLock class is used, which really unlocks it even when it has
        been recursively acquired several times. Another internal interface is
        then used to restore the recursion level when the lock is reacquired.

        '''
        if not self._is_owned():
            raise RuntimeError('cannot wait on un-acquired lock')
        waiter = _allocate_lock()
        waiter.acquire()
        self._waiters.append(waiter)
        saved_state = self._release_save()
        gotit = False
    # WARNING: Decompyle incomplete

    
    def wait_for(self, predicate, timeout = (None,)):
        '''Wait until a condition evaluates to True.

        predicate should be a callable which result will be interpreted as a
        boolean value.  A timeout may be provided giving the maximum time to
        wait.

        '''
        endtime = None
        waittime = timeout
        result = predicate()
    # WARNING: Decompyle incomplete

    
    def notify(self, n = (1,)):
        '''Wake up one or more threads waiting on this condition, if any.

        If the calling thread has not acquired the lock when this method is
        called, a RuntimeError is raised.

        This method wakes up at most n of the threads waiting for the condition
        variable; it is a no-op if no threads are waiting.

        '''
        if not self._is_owned():
            raise RuntimeError('cannot notify on un-acquired lock')
        waiters = self._waiters
    # WARNING: Decompyle incomplete

    
    def notify_all(self):
        '''Wake up all threads waiting on this condition.

        If the calling thread has not acquired the lock when this method
        is called, a RuntimeError is raised.

        '''
        self.notify(len(self._waiters))

    
    def notifyAll(self):
        '''Wake up all threads waiting on this condition.

        This method is deprecated, use notify_all() instead.

        '''
        import warnings
        warnings.warn('notifyAll() is deprecated, use notify_all() instead', DeprecationWarning, stacklevel = 2)
        self.notify_all()



class Semaphore:
    '''This class implements semaphore objects.

    Semaphores manage a counter representing the number of release() calls minus
    the number of acquire() calls, plus an initial value. The acquire() method
    blocks if necessary until it can return without making the counter
    negative. If not given, value defaults to 1.

    '''
    
    def __init__(self, value = (1,)):
        if value < 0:
            raise ValueError('semaphore initial value must be >= 0')
        self._cond = Condition(Lock())
        self._value = value

    
    def __repr__(self):
        cls = self.__class__
        return f'''<{cls.__module__}.{cls.__qualname__} at {id(self):#x}: value={self._value}>'''

    
    def acquire(self, blocking, timeout = (True, None)):
        '''Acquire a semaphore, decrementing the internal counter by one.

        When invoked without arguments: if the internal counter is larger than
        zero on entry, decrement it by one and return immediately. If it is zero
        on entry, block, waiting until some other thread has called release() to
        make it larger than zero. This is done with proper interlocking so that
        if multiple acquire() calls are blocked, release() will wake exactly one
        of them up. The implementation may pick one at random, so the order in
        which blocked threads are awakened should not be relied on. There is no
        return value in this case.

        When invoked with blocking set to true, do the same thing as when called
        without arguments, and return true.

        When invoked with blocking set to false, do not block. If a call without
        an argument would block, return false immediately; otherwise, do the
        same thing as when called without arguments, and return true.

        When invoked with a timeout other than None, it will block for at
        most timeout seconds.  If acquire does not complete successfully in
        that interval, return false.  Return true otherwise.

        '''
        pass
    # WARNING: Decompyle incomplete

    __enter__ = acquire
    
    def release(self, n = (1,)):
        '''Release a semaphore, incrementing the internal counter by one or more.

        When the counter is zero on entry and another thread is waiting for it
        to become larger than zero again, wake up that thread.

        '''
        if n < 1:
            raise ValueError('n must be one or more')
        self._cond
        for None in range(n):
            self._cond.notify()
            None(None, None)
            return None
            with None:
                if not None:
                    pass

    
    def __exit__(self, t, v, tb):
        self.release()



class BoundedSemaphore(Semaphore):
    """Implements a bounded semaphore.

    A bounded semaphore checks to make sure its current value doesn't exceed its
    initial value. If it does, ValueError is raised. In most situations
    semaphores are used to guard resources with limited capacity.

    If the semaphore is released too many times it's a sign of a bug. If not
    given, value defaults to 1.

    Like regular semaphores, bounded semaphores manage a counter representing
    the number of release() calls minus the number of acquire() calls, plus an
    initial value. The acquire() method blocks if necessary until it can return
    without making the counter negative. If not given, value defaults to 1.

    """
    
    def __init__(self, value = (1,)):
        Semaphore.__init__(self, value)
        self._initial_value = value

    
    def __repr__(self):
        cls = self.__class__
        return f'''<{cls.__module__}.{cls.__qualname__} at {id(self):#x}: value={self._value}/{self._initial_value}>'''

    
    def release(self, n = (1,)):
        '''Release a semaphore, incrementing the internal counter by one or more.

        When the counter is zero on entry and another thread is waiting for it
        to become larger than zero again, wake up that thread.

        If the number of releases exceeds the number of acquires,
        raise a ValueError.

        '''
        if n < 1:
            raise ValueError('n must be one or more')
        self._cond
        if self._value + n > self._initial_value:
            raise ValueError('Semaphore released too many times')
        for None in range(n):
            self._cond.notify()
            None(None, None)
            return None
            with None:
                if not None:
                    pass



class Event:
    '''Class implementing event objects.

    Events manage a flag that can be set to true with the set() method and reset
    to false with the clear() method. The wait() method blocks until the flag is
    true.  The flag is initially false.

    '''
    
    def __init__(self):
        self._cond = Condition(Lock())
        self._flag = False

    
    def __repr__(self):
        cls = self.__class__
        status = 'set' if self._flag else 'unset'
        return f'''<{cls.__module__}.{cls.__qualname__} at {id(self):#x}: {status}>'''

    
    def _at_fork_reinit(self):
        self._cond._at_fork_reinit()

    
    def is_set(self):
        '''Return true if and only if the internal flag is true.'''
        return self._flag

    
    def isSet(self):
        '''Return true if and only if the internal flag is true.

        This method is deprecated, use is_set() instead.

        '''
        import warnings
        warnings.warn('isSet() is deprecated, use is_set() instead', DeprecationWarning, stacklevel = 2)
        return self.is_set()

    
    def set(self):
        '''Set the internal flag to true.

        All threads waiting for it to become true are awakened. Threads
        that call wait() once the flag is true will not block at all.

        '''
        self._cond
        self._flag = True
        self._cond.notify_all()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def clear(self):
        '''Reset the internal flag to false.

        Subsequently, threads calling wait() will block until set() is called to
        set the internal flag to true again.

        '''
        self._cond
        self._flag = False
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def wait(self, timeout = (None,)):
        '''Block until the internal flag is true.

        If the internal flag is true on entry, return immediately. Otherwise,
        block until another thread calls set() to set the flag to true, or until
        the optional timeout occurs.

        When the timeout argument is present and not None, it should be a
        floating point number specifying a timeout for the operation in seconds
        (or fractions thereof).

        This method returns the internal flag on exit, so it will always return
        True except if a timeout is given and the operation times out.

        '''
        self._cond
        signaled = self._flag
        if not signaled:
            signaled = self._cond.wait(timeout)
        None(None, None)
        return 
        with None:
            if not None, signaled:
                pass



class Barrier:
    """Implements a Barrier.

    Useful for synchronizing a fixed number of threads at known synchronization
    points.  Threads block on 'wait()' and are simultaneously awoken once they
    have all made that call.

    """
    
    def __init__(self, parties, action, timeout = (None, None)):
        """Create a barrier, initialised to 'parties' threads.

        'action' is a callable which, when supplied, will be called by one of
        the threads after they have all entered the barrier and just prior to
        releasing them all. If a 'timeout' is provided, it is used as the
        default for all subsequent 'wait()' calls.

        """
        self._cond = Condition(Lock())
        self._action = action
        self._timeout = timeout
        self._parties = parties
        self._state = 0
        self._count = 0

    
    def __repr__(self):
        cls = self.__class__
        if self.broken:
            return f'''<{cls.__module__}.{cls.__qualname__} at {id(self):#x}: broken>'''
        return f'''{cls.__module__}.{cls.__qualname__} at {id(self):#x}: waiters={self.n_waiting}/{self.parties}>'''

    
    def wait(self, timeout = (None,)):
        """Wait for the barrier.

        When the specified number of threads have started waiting, they are all
        simultaneously awoken. If an 'action' was provided for the barrier, one
        of the threads will have executed that callback prior to returning.
        Returns an individual index number from 0 to 'parties-1'.

        """
        pass
    # WARNING: Decompyle incomplete

    
    def _enter(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _release(self):
        
        try:
            if self._action:
                self._action()
            self._state = 1
            self._cond.notify_all()
            return None
        except:
            self._break()
            raise 


    
    def _wait(self, timeout):
        pass
    # WARNING: Decompyle incomplete

    
    def _exit(self):
        if self._count == 0 or self._state in (-1, 1):
            self._state = 0
            self._cond.notify_all()
            return None
        return None

    
    def reset(self):
        '''Reset the barrier to the initial state.

        Any threads currently waiting will get the BrokenBarrier exception
        raised.

        '''
        self._cond
        if self._count > 0:
            if self._state == 0:
                self._state = -1
            elif self._state == -2:
                self._state = -1
            else:
                self._state = 0
        self._cond.notify_all()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def abort(self):
        """Place the barrier into a 'broken' state.

        Useful in case of error.  Any currently waiting threads and threads
        attempting to 'wait()' will have BrokenBarrierError raised.

        """
        self._cond
        self._break()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _break(self):
        self._state = -2
        self._cond.notify_all()

    parties = (lambda self: self._parties)()
    n_waiting = (lambda self: if self._state == 0:
self._count)()
    broken = (lambda self: self._state == -2)()


class BrokenBarrierError(RuntimeError):
    pass

_counter = _count(1).__next__

def _newname(name_template):
    return name_template % _counter()

_active_limbo_lock = RLock()
_active = { }
_limbo = { }
_dangling = WeakSet()
_shutdown_locks_lock = _allocate_lock()
_shutdown_locks = set()

def _maintain_shutdown_locks():
    """
    Drop any shutdown locks that don't correspond to running threads anymore.

    Calling this from time to time avoids an ever-growing _shutdown_locks
    set when Thread objects are not joined explicitly. See bpo-37788.

    This must be called with _shutdown_locks_lock acquired.
    """
    to_remove = _shutdown_locks()
    _shutdown_locks.difference_update(to_remove)


class Thread:
    '''A class that represents a thread of control.

    This class can be safely subclassed in a limited fashion. There are two ways
    to specify the activity: by passing a callable object to the constructor, or
    by overriding the run() method in a subclass.

    '''
    _initialized = False
    
    def __init__(self, group, target, name = None, args = (None, None, None, (), None), kwargs = {
        'daemon': None }, *, daemon):
        '''This constructor should always be called with keyword arguments. Arguments are:

        *group* should be None; reserved for future extension when a ThreadGroup
        class is implemented.

        *target* is the callable object to be invoked by the run()
        method. Defaults to None, meaning nothing is called.

        *name* is the thread name. By default, a unique name is constructed of
        the form "Thread-N" where N is a small decimal number.

        *args* is a list or tuple of arguments for the target invocation. Defaults to ().

        *kwargs* is a dictionary of keyword arguments for the target
        invocation. Defaults to {}.

        If a subclass overrides the constructor, it must make sure to invoke
        the base class constructor (Thread.__init__()) before doing anything
        else to the thread.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _reset_internal_locks(self, is_alive):
        self._started._at_fork_reinit()
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def start(self):
