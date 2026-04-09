# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: synchronize.pyc (Python 3.11)

__all__ = [
    'Lock',
    'RLock',
    'Semaphore',
    'BoundedSemaphore',
    'Condition',
    'Event']
import threading
import sys
import tempfile
import _multiprocessing
import time
from  import context
from  import process
from  import util

try:
    from _multiprocessing import SemLock, sem_unlink
except ImportError:
    raise ImportError('This platform lacks a functioning sem_open implementation, therefore, the required synchronization primitives needed will not function, see issue 3770.')

(RECURSIVE_MUTEX, SEMAPHORE) = list(range(2))
SEM_VALUE_MAX = _multiprocessing.SemLock.SEM_VALUE_MAX

class SemLock(object):
    _rand = tempfile._RandomNameSequence()
    
    def __init__(self, kind, value, maxvalue, *, ctx):
        pass
    # WARNING: Decompyle incomplete

    _cleanup = (lambda name: unregister = unregisterimport resource_trackersem_unlink(name)unregister(name, 'semaphore'))()
    
    def _make_methods(self):
        self.acquire = self._semlock.acquire
        self.release = self._semlock.release

    
    def __enter__(self):
        return self._semlock.__enter__()

    
    def __exit__(self, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def __getstate__(self):
        context.assert_spawning(self)
        sl = self._semlock
        if sys.platform == 'win32':
            h = context.get_spawning_popen().duplicate_for_child(sl.handle)
        elif self._is_fork_ctx:
            raise RuntimeError('A SemLock created in a fork context is being shared with a process in a spawn context. This is not supported. Please use the same context to create multiprocessing objects and Process.')
        h = sl.handle
        return (h, sl.kind, sl.maxvalue, sl.name)

    
    def __setstate__(self, state):
        pass
    # WARNING: Decompyle incomplete

    _make_name = (lambda : f'''{process.current_process()._config['semprefix']!s}-{next(SemLock._rand)!s}''')()


class Semaphore(SemLock):
    
    def __init__(self, value = (1,), *, ctx):
        SemLock.__init__(self, SEMAPHORE, value, SEM_VALUE_MAX, ctx = ctx)

    
    def get_value(self):
        return self._semlock._get_value()

    
    def __repr__(self):
        
        try:
            value = self._semlock._get_value()
        except Exception:
            value = 'unknown'

        return f'''<{self.__class__.__name__!s}(value={value!s})>'''



class BoundedSemaphore(Semaphore):
    
    def __init__(self, value = (1,), *, ctx):
        SemLock.__init__(self, SEMAPHORE, value, value, ctx = ctx)

    
    def __repr__(self):
        
        try:
            value = self._semlock._get_value()
        except Exception:
            value = 'unknown'

        return f'''<{self.__class__.__name__!s}(value={value!s}, maxvalue={self._semlock.maxvalue!s})>'''



class Lock(SemLock):
    
    def __init__(self, *, ctx):
        SemLock.__init__(self, SEMAPHORE, 1, 1, ctx = ctx)

    
    def __repr__(self):
