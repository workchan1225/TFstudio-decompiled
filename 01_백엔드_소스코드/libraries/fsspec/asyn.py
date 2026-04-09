# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: asyn.pyc (Python 3.11)

import asyncio
import asyncio.events as asyncio
import functools
import inspect
import io
import numbers
import os
import re
import threading
from collections.abc import Iterable
from glob import has_magic
from typing import TYPE_CHECKING
from callbacks import DEFAULT_CALLBACK
from exceptions import FSTimeoutError
from implementations.local import LocalFileSystem, make_path_posix, trailing_sep
from spec import AbstractBufferedFile, AbstractFileSystem
from utils import glob_translate, is_exception, other_paths
private = re.compile('_[^_]')
iothread = [
    None]
loop = [
    None]
_lock = None
get_running_loop = asyncio.get_running_loop

def get_lock():
    '''Allocate or return a threading lock.

    The lock is allocated on first use to allow setting one lock per forked process.
    '''
    global _lock
    if not _lock:
        _lock = threading.Lock()
    return _lock


def reset_lock():
    '''Reset the global lock.

    This should be called only on the init of a forked process to reset the lock to
    None, enabling the new forked process to get a new lock.
    '''
    global _lock
    iothread[0] = None
    loop[0] = None
    _lock = None


async def _runner(event, coro, result, timeout = (None,)):
    pass
# WARNING: Decompyle incomplete


def sync(loop = None, func = {
    'timeout': None }, *, timeout, *args, **kwargs):
    '''
    Make loop run coroutine until it returns. Runs in other thread

    Examples
    --------
    >>> fsspec.asyn.sync(fsspec.asyn.get_loop(), func, *args,
                         timeout=timeout, **kwargs)
    '''
    timeout = timeout if timeout else None
# WARNING: Decompyle incomplete


def sync_wrapper(func, obj = (None,)):
    '''Given a function, make so can be called in blocking contexts

    Leave obj=None if defining within a class. Pass the instance if attaching
    as an attribute of the instance.
    '''
    pass
# WARNING: Decompyle incomplete


def get_loop():
    '''Create or return the default fsspec IO loop

    The loop will be running on a separate thread.
    '''
    pass
# WARNING: Decompyle incomplete


def reset_after_fork():
    global lock
    loop[0] = None
    iothread[0] = None
    lock = None

if hasattr(os, 'register_at_fork'):
    os.register_at_fork(after_in_child = reset_after_fork)
if TYPE_CHECKING:
    import resource
    ResourceError = resource.error
else:
    
    try:
        import resource
        ResourceError = getattr(resource, 'error', OSError)
    except ImportError:
        resource = None
        ResourceError = OSError

    _DEFAULT_BATCH_SIZE = 128
    _NOFILES_DEFAULT_BATCH_SIZE = 1280
    
    def _get_batch_size(nofiles = (False,)):
        conf = conf
        import fsspec.config
        if nofiles:
            if 'nofiles_gather_batch_size' in conf:
                return conf['nofiles_gather_batch_size']
        if 'gather_batch_size' in conf:
            return conf['gather_batch_size']
        if None:
            return _NOFILES_DEFAULT_BATCH_SIZE
    # WARNING: Decompyle incomplete

    
    def running_async():
        '''Being executed by an event loop?'''
        
        try:
            asyncio.get_running_loop()
            return True
        except RuntimeError:
            return False


    
    async def _run_coros_in_chunks(coros, batch_size, callback, timeout, return_exceptions, nofiles = (None, DEFAULT_CALLBACK, None, False, False)):
        '''Run the given coroutines in  chunks.

    Parameters
    ----------
    coros: list of coroutines to run
    batch_size: int or None
        Number of coroutines to submit/wait on simultaneously.
        If -1, then it will not be any throttling. If
        None, it will be inferred from _get_batch_size()
    callback: fsspec.callbacks.Callback instance
        Gets a relative_update when each coroutine completes
    timeout: number or None
        If given, each coroutine times out after this time. Note that, since
        there are multiple batches, the total run time of this function will in
        general be longer
    return_exceptions: bool
        Same meaning as in asyncio.gather
    nofiles: bool
        If inferring the batch_size, does this operation involve local files?
        If yes, you normally expect smaller batches.
    '''
        pass
    # WARNING: Decompyle incomplete

    async_methods = [
        '_ls',
        '_cat_file',
        '_get_file',
        '_put_file',
        '_rm_file',
        '_cp_file',
        '_pipe_file',
        '_expand_path',
        '_info',
        '_isfile',
        '_isdir',
        '_exists',
        '_walk',
        '_glob',
        '_find',
        '_du',
        '_size',
        '_mkdir',
        '_makedirs']
    
    class AsyncFileSystem(AbstractFileSystem):
        pass
    # WARNING: Decompyle incomplete

    
    def mirror_sync_methods(obj):
        '''Populate sync and async methods for obj

    For each method will create a sync version if the name refers to an async method
    (coroutine) and there is no override in the child class; will create an async
    method for the corresponding sync method if there is no implementation.

    Uses the methods specified in
    - async_methods: the set that an implementation is expected to provide
    - default_async_methods: that can be derived from their sync version in
      AbstractFileSystem
    - AsyncFileSystem: async-specific default coroutines
    '''
        AbstractFileSystem = AbstractFileSystem
        import fsspec
        for method in async_methods + dir(AsyncFileSystem):
            if not method.startswith('_'):
                continue
            smethod = method[1:]
            if private.match(method):
                isco = inspect.iscoroutinefunction(getattr(obj, method, None))
                unsync = getattr(getattr(obj, smethod, False), '__func__', None)
                is_default = unsync is getattr(AbstractFileSystem, smethod, '')
                if isco and is_default:
                    mth = sync_wrapper(getattr(obj, method), obj = obj)
                    setattr(obj, smethod, mth)
                    if not mth.__doc__:
                        mth.__doc__ = getattr(getattr(AbstractFileSystem, smethod, None), '__doc__', '')
            return None

    
    class FSSpecCoroutineCancel(Exception):
        pass

    
    def _dump_running_tasks(printout, cancel, exc, with_task = (True, True, FSSpecCoroutineCancel, False)):
        pass
    # WARNING: Decompyle incomplete

    
    class AbstractAsyncStreamedFile(AbstractBufferedFile):
        
        async def read(self, length = (-1,)):
            '''
        Return data from cache, or fetch pieces as necessary

        Parameters
        ----------
        length: int (-1)
            Number of bytes to read; if <0, all remaining bytes.
        '''
            pass
        # WARNING: Decompyle incomplete

        
        async def write(self, data):
            '''
        Write data to buffer.

        Buffer only sent on flush() or if buffer is greater than
        or equal to blocksize.

        Parameters
        ----------
        data: bytes
            Set of bytes to be written.
        '''
            pass
        # WARNING: Decompyle incomplete

        
        async def close(self):
            '''Close file

        Finalizes writes, discards cache
        '''
            pass
        # WARNING: Decompyle incomplete

        
        async def flush(self, force = (False,)):
            pass
        # WARNING: Decompyle incomplete

        
        async def __aenter__(self):
            pass
        # WARNING: Decompyle incomplete

        
        async def __aexit__(self, exc_type, exc_val, exc_tb):
            pass
        # WARNING: Decompyle incomplete

        
        async def _fetch_range(self, start, end):
            pass
        # WARNING: Decompyle incomplete

        
        async def _initiate_upload(self):
            pass
        # WARNING: Decompyle incomplete

        
        async def _upload_chunk(self, final = (False,)):
            pass
        # WARNING: Decompyle incomplete


    return None
