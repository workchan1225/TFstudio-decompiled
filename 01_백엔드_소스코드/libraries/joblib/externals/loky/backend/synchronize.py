# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: synchronize.pyc (Python 3.11)

import os
import sys
import tempfile
import threading
import _multiprocessing
from time import time as _time
from multiprocessing import process, util
from multiprocessing.context import assert_spawning
from  import resource_tracker
__all__ = [
    'Lock',
    'RLock',
    'Semaphore',
    'BoundedSemaphore',
    'Condition',
    'Event']

try:
    from _multiprocessing import SemLock as _SemLock
    from _multiprocessing import sem_unlink
except ImportError:
    raise ImportError('This platform lacks a functioning sem_open implementation, therefore, the required synchronization primitives needed will not function, see issue 3770.')

(RECURSIVE_MUTEX, SEMAPHORE) = range(2)
SEM_VALUE_MAX = _multiprocessing.SemLock.SEM_VALUE_MAX

class SemLock:
    _rand = tempfile._RandomNameSequence()
    
    def __init__(self, kind, value, maxvalue, name = (None,)):
        unlink_now = False
    # WARNING: Decompyle incomplete

    _cleanup = (lambda name: try:
sem_unlink(name)try:
passexcept FileNotFoundError:
try:
passtry:
resource_tracker.unregister(name, 'semlock')Noneexcept:
resource_tracker.unregister(name, 'semlock'))()
    
    def _make_methods(self):
        self.acquire = self._semlock.acquire
        self.release = self._semlock.release

    
    def __enter__(self):
        return self._semlock.acquire()

    
    def __exit__(self, *args):
        return self._semlock.release()

    
    def __getstate__(self):
        assert_spawning(self)
        sl = self._semlock
        h = sl.handle
        return (h, sl.kind, sl.maxvalue, sl.name)

    
    def __setstate__(self, state):
        pass
    # WARNING: Decompyle incomplete

    _make_name = (lambda : f'''/loky-{os.getpid()}-{next(SemLock._rand)}''')()


class Semaphore(SemLock):
    
    def __init__(self, value = (1,)):
        SemLock.__init__(self, SEMAPHORE, value, SEM_VALUE_MAX)

    
    def get_value(self):
        if sys.platform == 'darwin':
            raise NotImplementedError('OSX does not implement sem_getvalue')
        return self._semlock._get_value()

    
    def __repr__(self):
        
        try:
            value = self._semlock._get_value()
        except Exception:
            value = 'unknown'

        return f'''<{self.__class__.__name__}(value={value})>'''



class BoundedSemaphore(Semaphore):
    
    def __init__(self, value = (1,)):
        SemLock.__init__(self, SEMAPHORE, value, value)

    
    def __repr__(self):
        
        try:
            value = self._semlock._get_value()
        except Exception:
            value = 'unknown'

        return f'''<{self.__class__.__name__}(value={value}, maxvalue={self._semlock.maxvalue})>'''



class Lock(SemLock):
    pass
# WARNING: Decompyle incomplete


class RLock(SemLock):
    pass
# WARNING: Decompyle incomplete


class Condition:
    
    def __init__(self, lock = (None,)):
        if not lock:
            pass
        self._lock = RLock()
        self._sleeping_count = Semaphore(0)
        self._woken_count = Semaphore(0)
        self._wait_semaphore = Semaphore(0)
        self._make_methods()

    
    def __getstate__(self):
        assert_spawning(self)
        return (self._lock, self._sleeping_count, self._woken_count, self._wait_semaphore)

    
    def __setstate__(self, state):
        (self._lock, self._sleeping_count, self._woken_count, self._wait_semaphore) = state
        self._make_methods()

    
    def __enter__(self):
        return self._lock.__enter__()

    
    def __exit__(self, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def _make_methods(self):
        self.acquire = self._lock.acquire
        self.release = self._lock.release

    
    def __repr__(self):
        
        try:
            num_waiters = self._sleeping_count._semlock._get_value() - self._woken_count._semlock._get_value()
        except Exception:
            num_waiters = 'unknown'

        return f'''<{self.__class__.__name__}({self._lock}, {num_waiters})>'''

    
    def wait(self, timeout = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def notify(self):
        pass
    # WARNING: Decompyle incomplete

    
    def notify_all(self):
        pass
    # WARNING: Decompyle incomplete

    
    def wait_for(self, predicate, timeout = (None,)):
        result = predicate()
        if result:
            return result
    # WARNING: Decompyle incomplete



class Event:
    
    def __init__(self):
        self._cond = Condition(Lock())
        self._flag = Semaphore(0)

    
    def is_set(self):
        self._cond
        if self._flag.acquire(False):
            self._flag.release()
            None(None, None)
            return True
        None(None, None)
        return False
        with None:
            if not None:
                pass

    
    def set(self):
        self._cond
        self._flag.acquire(False)
        self._flag.release()
        self._cond.notify_all()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def clear(self):
        self._cond
        self._flag.acquire(False)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def wait(self, timeout = (None,)):
        self._cond
        if self._flag.acquire(False):
            self._flag.release()
        else:
            self._cond.wait(timeout)
        if self._flag.acquire(False):
            self._flag.release()
            None(None, None)
            return True
        None(None, None)
        return False
        with None:
            if not None:
                pass
