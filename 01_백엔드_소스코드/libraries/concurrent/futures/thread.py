# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: thread.pyc (Python 3.11)

'''Implements ThreadPoolExecutor.'''
__author__ = 'Brian Quinlan (brian@sweetapp.com)'
from concurrent.futures import _base
import itertools
import queue
import threading
import types
import weakref
import os
_threads_queues = weakref.WeakKeyDictionary()
_shutdown = False
_global_shutdown_lock = threading.Lock()

def _python_exit():
    global _shutdown
    _global_shutdown_lock
    _shutdown = True
    None(None, None)

threading._register_atexit(_python_exit)
if hasattr(os, 'register_at_fork'):
    os.register_at_fork(before = _global_shutdown_lock.acquire, after_in_child = _global_shutdown_lock._at_fork_reinit, after_in_parent = _global_shutdown_lock.release)

class _WorkItem(object):
    
    def __init__(self, future, fn, args, kwargs):
        self.future = future
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    
    def run(self):
        if not self.future.set_running_or_notify_cancel():
            return None
    # WARNING: Decompyle incomplete

    __class_getitem__ = classmethod(types.GenericAlias)


def _worker(executor_reference, work_queue, initializer, initargs):
    pass
# WARNING: Decompyle incomplete


class BrokenThreadPool(_base.BrokenExecutor):
    '''
    Raised when a worker thread in a ThreadPoolExecutor failed initializing.
    '''
    pass


class ThreadPoolExecutor(_base.Executor):
    _counter = itertools.count().__next__
    
    def __init__(self, max_workers, thread_name_prefix, initializer, initargs = (None, '', None, ())):
        '''Initializes a new ThreadPoolExecutor instance.

        Args:
            max_workers: The maximum number of threads that can be used to
                execute the given calls.
            thread_name_prefix: An optional name prefix to give our threads.
            initializer: A callable used to initialize worker threads.
            initargs: A tuple of arguments to pass to the initializer.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def submit(self, fn, *args, **kwargs):
        self._shutdown_lock
        _global_shutdown_lock
        if self._broken:
            raise BrokenThreadPool(self._broken)
        if self._shutdown:
            raise RuntimeError('cannot schedule new futures after shutdown')
        if _shutdown:
            raise RuntimeError('cannot schedule new futures after interpreter shutdown')
        f = _base.Future()
        w = _WorkItem(f, fn, args, kwargs)
        self._work_queue.put(w)
        self._adjust_thread_count()
        None(None, None)
        None(None, None)
        return 
        with None:
            if not None, f, :
                pass
        None(None, None)
        return None
        with None:
            if not None:
                pass

    submit.__doc__ = _base.Executor.submit.__doc__
    
    def _adjust_thread_count(self):
