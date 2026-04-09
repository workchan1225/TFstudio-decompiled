# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _thread_cache.pyc (Python 3.11)

from __future__ import annotations
import ctypes
import ctypes.util as ctypes
import os
import sys
import traceback
from functools import partial
from itertools import count
from threading import Lock, Thread
from typing import TYPE_CHECKING, Any, Generic, TypeVar
import outcome
if TYPE_CHECKING:
    from collections.abc import Callable
RetT = TypeVar('RetT')

def _to_os_thread_name(name = None):
    return name.encode('ascii', errors = 'replace')[:15]


def get_os_thread_name_func():
    
    def namefunc(setname = None, ident = None, name = None):
        pass
    # WARNING: Decompyle incomplete

    
    def darwin_namefunc(setname = None, ident = None, name = None):
        pass
    # WARNING: Decompyle incomplete

    libpthread_path = ctypes.util.find_library('pthread')
    if not libpthread_path:
        libpthread_path = 'libc.so'
    
    try:
        libpthread = ctypes.CDLL(libpthread_path)
    except Exception:
        return None

    pthread_setname_np = getattr(libpthread, 'pthread_setname_np', None)
# WARNING: Decompyle incomplete

set_os_thread_name = get_os_thread_name_func()
IDLE_TIMEOUT = 10
name_counter = count()

def WorkerThread():
    '''WorkerThread'''
    __slots__ = ('_default_name', '_job', '_thread', '_thread_cache', '_worker_lock')
    
    def __init__(self = None, thread_cache = None):
        self._job = None
        self._thread_cache = thread_cache
        self._worker_lock = Lock()
        self._worker_lock.acquire()
        self._default_name = f'''Trio thread {next(name_counter)}'''
        self._thread = Thread(target = self._work, name = self._default_name, daemon = True)
        if set_os_thread_name:
            set_os_thread_name(self._thread.ident, self._default_name)
        self._thread.start()

    
    def _handle_job(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _work(self = None):
        if self._worker_lock.acquire(timeout = IDLE_TIMEOUT):
            self._handle_job()
        else:
            
            try:
                del self._thread_cache._idle_workers[self]
                return None
            except KeyError:
                continue
                continue



WorkerThread = <NODE:27>(WorkerThread, 'WorkerThread', Generic[RetT])

class ThreadCache:
    __slots__ = ('_idle_workers',)
    
    def __init__(self = None):
        self._idle_workers = { }

    
    def start_thread_soon(self = None, fn = None, deliver = None, name = (None,)):
        
        try:
            (worker, _) = self._idle_workers.popitem()
        except KeyError:
            worker = WorkerThread(self)

        worker._job = (fn, deliver, name)
        worker._worker_lock.release()


THREAD_CACHE = ThreadCache()

def start_thread_soon(fn = None, deliver = None, name = None):
    """Runs ``deliver(outcome.capture(fn))`` in a worker thread.

    Generally ``fn`` does some blocking work, and ``deliver`` delivers the
    result back to whoever is interested.

    This is a low-level, no-frills interface, very similar to using
    `threading.Thread` to spawn a thread directly. The main difference is
    that this function tries to reuse threads when possible, so it can be
    a bit faster than `threading.Thread`.

    Worker threads have the `~threading.Thread.daemon` flag set, which means
    that if your main thread exits, worker threads will automatically be
    killed. If you want to make sure that your ``fn`` runs to completion, then
    you should make sure that the main thread remains alive until ``deliver``
    is called.

    It is safe to call this function simultaneously from multiple threads.

    Args:

        fn (sync function): Performs arbitrary blocking work.

        deliver (sync function): Takes the `outcome.Outcome` of ``fn``, and
          delivers it. *Must not block.*

    Because worker threads are cached and reused for multiple calls, neither
    function should mutate thread-level state, like `threading.local` objects
    – or if they do, they should be careful to revert their changes before
    returning.

    Note:

        The split between ``fn`` and ``deliver`` serves two purposes. First,
        it's convenient, since most callers need something like this anyway.

        Second, it avoids a small race condition that could cause too many
        threads to be spawned. Consider a program that wants to run several
        jobs sequentially on a thread, so the main thread submits a job, waits
        for it to finish, submits another job, etc. In theory, this program
        should only need one worker thread. But what could happen is:

        1. Worker thread: First job finishes, and calls ``deliver``.

        2. Main thread: receives notification that the job finished, and calls
           ``start_thread_soon``.

        3. Main thread: sees that no worker threads are marked idle, so spawns
           a second worker thread.

        4. Original worker thread: marks itself as idle.

        To avoid this, threads mark themselves as idle *before* calling
        ``deliver``.

        Is this potential extra thread a major problem? Maybe not, but it's
        easy enough to avoid, and we figure that if the user is trying to
        limit how many threads they're using then it's polite to respect that.

    """
    THREAD_CACHE.start_thread_soon(fn, deliver, name)


def clear_worker_threads():
    THREAD_CACHE._idle_workers.clear()

if hasattr(os, 'register_at_fork'):
    os.register_at_fork(after_in_child = clear_worker_threads)
    return None
