# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: process_executor.pyc (Python 3.11)

'''Implements ProcessPoolExecutor.

The follow diagram and text describe the data-flow through the system:

|======================= In-process =====================|== Out-of-process ==|

+----------+     +----------+       +--------+     +-----------+    +---------+
|          |  => | Work Ids |       |        |     | Call Q    |    | Process |
|          |     +----------+       |        |     +-----------+    |  Pool   |
|          |     | ...      |       |        |     | ...       |    +---------+
|          |     | 6        |    => |        |  => | 5, call() | => |         |
|          |     | 7        |       |        |     | ...       |    |         |
| Process  |     | ...      |       | Local  |     +-----------+    | Process |
|  Pool    |     +----------+       | Worker |                      |  #1..n  |
| Executor |                        | Thread |                      |         |
|          |     +----------- +     |        |     +-----------+    |         |
|          | <=> | Work Items | <=> |        | <=  | Result Q  | <= |         |
|          |     +------------+     |        |     +-----------+    |         |
|          |     | 6: call()  |     |        |     | ...       |    |         |
|          |     |    future  |     +--------+     | 4, result |    |         |
|          |     | ...        |                    | 3, except |    |         |
+----------+     +------------+                    +-----------+    +---------+

Executor.submit() called:
- creates a uniquely numbered _WorkItem and adds it to the "Work Items" dict
- adds the id of the _WorkItem to the "Work Ids" queue

Local worker thread:
- reads work ids from the "Work Ids" queue and looks up the corresponding
  WorkItem from the "Work Items" dict: if the work item has been cancelled then
  it is simply removed from the dict, otherwise it is repackaged as a
  _CallItem and put in the "Call Q". New _CallItems are put in the "Call Q"
  until "Call Q" is full. NOTE: the size of the "Call Q" is kept small because
  calls placed in the "Call Q" can no longer be cancelled with Future.cancel().
- reads _ResultItems from "Result Q", updates the future stored in the
  "Work Items" dict and deletes the dict entry

Process #1..n:
- reads _CallItems from "Call Q", executes the calls, and puts the resulting
  _ResultItems in "Result Q"
'''
__author__ = 'Thomas Moreau (thomas.moreau.2010@gmail.com)'
import faulthandler
import os
import gc
import sys
import queue
import struct
import weakref
import warnings
import itertools
import traceback
import threading
from time import time, sleep
import multiprocessing as mp
from functools import partial
from pickle import PicklingError
from concurrent.futures import Executor
from concurrent.futures._base import LOGGER
from concurrent.futures.process import BrokenProcessPool as _BPPException
from multiprocessing.connection import wait
from _base import Future
from backend import get_context
from backend.context import cpu_count, _MAX_WINDOWS_WORKERS
from backend.queues import Queue, SimpleQueue
from backend.reduction import set_loky_pickler, get_loky_pickler_name
from backend.utils import kill_process_tree, get_exitcodes_terminated_worker
from initializers import _prepare_initializer
MAX_DEPTH = int(os.environ.get('LOKY_MAX_DEPTH', 10))
_CURRENT_DEPTH = 0
_MEMORY_LEAK_CHECK_DELAY = 1
_MAX_MEMORY_LEAK_SIZE = int(3e+08)

try:
    from psutil import Process
    _USE_PSUTIL = True
    
    def _get_memory_usage(pid, force_gc = (False,)):
        if force_gc:
            gc.collect()
        mem_size = Process(pid).memory_info().rss
        mp.util.debug(f'''psutil return memory size: {mem_size}''')
        return mem_size

except ImportError:
    _USE_PSUTIL = False


class _ThreadWakeup:
    
    def __init__(self):
        self._closed = False
        (self._reader, self._writer) = mp.Pipe(duplex = False)

    
    def close(self):
        if not self._closed:
            self._closed = True
            self._writer.close()
            self._reader.close()
            return None

    
    def wakeup(self):
        if not self._closed:
            self._writer.send_bytes(b'')
            return None

    
    def clear(self):
        pass
    # WARNING: Decompyle incomplete



class _ExecutorFlags:
    '''necessary references to maintain executor states without preventing gc

    It permits to keep the information needed by executor_manager_thread
    and crash_detection_thread to maintain the pool without preventing the
    garbage collection of unreferenced executors.
    '''
    
    def __init__(self, shutdown_lock):
        self.shutdown = False
        self.broken = None
        self.kill_workers = False
        self.shutdown_lock = shutdown_lock

    
    def flag_as_shutting_down(self, kill_workers = (None,)):
        self.shutdown_lock
        self.shutdown = True
    # WARNING: Decompyle incomplete

    
    def flag_as_broken(self, broken):
        self.shutdown_lock
        self.shutdown = True
        self.broken = broken
        None(None, None)
        return None
        with None:
            if not None:
                pass


_global_shutdown = False
_global_shutdown_lock = threading.Lock()
_threads_wakeups = weakref.WeakKeyDictionary()

def _python_exit():
    global _global_shutdown
    _global_shutdown = True
    items = list(_threads_wakeups.items())
    if len(items) > 0:
        mp.util.debug(f'''Interpreter shutting down. Waking up {len(items)}executor_manager_thread:\n{items}''')
    for shutdown_lock, thread_wakeup in items:
        shutdown_lock
        thread_wakeup.wakeup()
        None(None, None)
    with None:
        if not None:
            pass
    continue
    for thread, _ in items:
        _global_shutdown_lock
        thread.join()
        None(None, None)
    with None:
        if not None:
            pass
    continue

mp.util.register_after_fork(_threads_wakeups, (lambda obj: obj.clear()))
process_pool_executor_at_exit = None
EXTRA_QUEUED_CALLS = 1

class _RemoteTraceback(Exception):
    '''Embed stringification of remote traceback in local traceback'''
    
    def __init__(self, tb = (None,)):
        self.tb = f'''\n"""\n{tb}"""'''

    
    def __str__(self):
        return self.tb



class _ExceptionWithTraceback:
    
    def __init__(self, exc):
        tb = getattr(exc, '__traceback__', None)
    # WARNING: Decompyle incomplete

    
    def __reduce__(self):
        return (_rebuild_exc, (self.exc, self.tb))



def _rebuild_exc(exc, tb):
    exc.__cause__ = _RemoteTraceback(tb)
    return exc


class _WorkItem:
    __slots__ = [
        'future',
        'fn',
        'args',
        'kwargs']
    
    def __init__(self, future, fn, args, kwargs):
        self.future = future
        self.fn = fn
        self.args = args
        self.kwargs = kwargs



class _ResultItem:
    
    def __init__(self, work_id, exception, result = (None, None)):
        self.work_id = work_id
        self.exception = exception
        self.result = result



class _CallItem:
    
    def __init__(self, work_id, fn, args, kwargs):
        self.work_id = work_id
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.loky_pickler = get_loky_pickler_name()

    
    def __call__(self):
        set_loky_pickler(self.loky_pickler)
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return f'''CallItem({self.work_id}, {self.fn}, {self.args}, {self.kwargs})'''



class _SafeQueue(Queue):
    pass
# WARNING: Decompyle incomplete


def _get_chunks(chunksize, *iterables):
    '''Iterates over zip()ed iterables in chunks.'''
    pass
# WARNING: Decompyle incomplete


def _process_chunk(fn, chunk):
    '''Processes a chunk of an iterable passed to map.

    Runs the function passed to map() on a chunk of the
    iterable passed to map.

    This function is run in a separate process.

    '''
    pass
# WARNING: Decompyle incomplete


def _sendback_result(result_queue, work_id, result, exception = (None, None)):
    '''Safely send back the given result or exception'''
    
    try:
        result_queue.put(_ResultItem(work_id, result = result, exception = exception))
        return None
    except BaseException:
        e = None
        exc = _ExceptionWithTraceback(e)
        result_queue.put(_ResultItem(work_id, exception = exc))
        e = None
        del e
        return None
        e = None
        del e



def _enable_faulthandler_if_needed():
    if 'PYTHONFAULTHANDLER' in os.environ:
        mp.util.debug(f'''faulthandler explicitly configured by environment variable: PYTHONFAULTHANDLER={os.environ['PYTHONFAULTHANDLER']}.''')
        return None
    if None.is_enabled():
        mp.util.debug('faulthandler already enabled.')
        return None
    None.util.debug('Enabling faulthandler to report tracebacks on worker crashes.')
    faulthandler.enable()


def _process_worker(call_queue, result_queue, initializer, initargs, processes_management_lock, timeout, worker_exit_lock, current_depth):
    '''Evaluates calls from call_queue and places the results in result_queue.

    This worker is run in a separate process.

    Args:
        call_queue: A ctx.Queue of _CallItems that will be read and
            evaluated by the worker.
        result_queue: A ctx.Queue of _ResultItems that will written
            to by the worker.
        initializer: A callable initializer, or None
        initargs: A tuple of args for the initializer
        processes_management_lock: A ctx.Lock avoiding worker timeout while
            some workers are being spawned.
        timeout: maximum time to wait for a new item in the call_queue. If that
            time is expired, the worker will shutdown.
        worker_exit_lock: Lock to avoid flagging the executor as broken on
            workers timeout.
        current_depth: Nested parallelism level, to avoid infinite spawning.
    '''
    pass
# WARNING: Decompyle incomplete


class _ExecutorManagerThread(threading.Thread):
    pass
# WARNING: Decompyle incomplete

_system_limits_checked = False
_system_limited = None

def _check_system_limits():
    global _system_limits_checked, _system_limited
    if _system_limits_checked and _system_limited:
        raise NotImplementedError(_system_limited)
    _system_limits_checked = True
    
    try:
        nsems_max = os.sysconf('SC_SEM_NSEMS_MAX')
    except (AttributeError, ValueError):
        return None

    if nsems_max == -1:
        return None
    if None >= 256:
        return None
    _system_limited = f'''{nsems_max} available, 256 necessary)'''
    raise NotImplementedError(_system_limited)


def _chain_from_iterable_of_lists(iterable):
    '''
    Specialized implementation of itertools.chain.from_iterable.
    Each item in *iterable* should be a list.  This function is
    careful not to keep references to yielded objects.
    '''
    pass
# WARNING: Decompyle incomplete


def _check_max_depth(context):
    if context.get_start_method() == 'fork' and _CURRENT_DEPTH > 0:
        raise LokyRecursionError("Could not spawn extra nested processes at depth superior to MAX_DEPTH=1. It is not possible to increase this limit when using the 'fork' start method.")
    if 0 < MAX_DEPTH or _CURRENT_DEPTH + 1 > MAX_DEPTH:
        raise LokyRecursionError(f'''Could not spawn extra nested processes at depth superior to MAX_DEPTH={MAX_DEPTH}. If this is intendend, you can change this limit with the LOKY_MAX_DEPTH environment variable.''')
    return None


class LokyRecursionError(RuntimeError):
    '''A process tries to spawn too many levels of nested processes.'''
    pass


class BrokenProcessPool(_BPPException):
    '''
    Raised when the executor is broken while a future was in the running state.
    The cause can an error raised when unpickling the task in the worker
    process or when unpickling the result value in the parent process. It can
    also be caused by a worker process being terminated unexpectedly.
    '''
    pass


class TerminatedWorkerError(BrokenProcessPool):
    '''
    Raised when a process in a ProcessPoolExecutor terminated abruptly
    while a future was in the running state.
    '''
    pass

BrokenExecutor = BrokenProcessPool

class ShutdownExecutorError(RuntimeError):
    '''
    Raised when a ProcessPoolExecutor is shutdown while a future was in the
    running or pending state.
    '''
    pass


class ProcessPoolExecutor(Executor):
    pass
# WARNING: Decompyle incomplete
