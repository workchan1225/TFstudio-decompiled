# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: asyn_wrapper.pyc (Python 3.11)

import asyncio
import functools
import inspect
import fsspec
from fsspec.asyn import AsyncFileSystem, running_async
from chained import ChainedFileSystem

def async_wrapper(func, obj, semaphore = (None, None)):
    '''
    Wraps a synchronous function to make it awaitable.

    Parameters
    ----------
    func : callable
        The synchronous function to wrap.
    obj : object, optional
        The instance to bind the function to, if applicable.
    semaphore : asyncio.Semaphore, optional
        A semaphore to limit concurrent calls.

    Returns
    -------
    coroutine
        An awaitable version of the function.
    '''
    pass
# WARNING: Decompyle incomplete


class AsyncFileSystemWrapper(ChainedFileSystem, AsyncFileSystem):
    pass
# WARNING: Decompyle incomplete
