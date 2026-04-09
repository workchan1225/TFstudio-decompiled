# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _synchronization.pyc (Python 3.11)

from __future__ import annotations
import threading
import types
from _exceptions import ExceptionMapping, PoolTimeout, map_exceptions

try:
    import trio
except (ImportError, NotImplementedError):
    trio = None


try:
    import anyio
except ImportError:
    anyio = None


def current_async_library():
    
    try:
        import sniffio
        environment = sniffio.current_async_library()
    except ImportError:
        environment = 'asyncio'

    if environment not in ('asyncio', 'trio'):
        raise RuntimeError('Running under an unsupported async environment.')
# WARNING: Decompyle incomplete


class AsyncLock:
    '''
    This is a standard lock.

    In the sync case `Lock` provides thread locking.
    In the async case `AsyncLock` provides async locking.
    '''
    
    def __init__(self = None):
        self._backend = ''

    
    def setup(self = None):
        """
        Detect if we're running under 'asyncio' or 'trio' and create
        a lock with the correct implementation.
        """
        self._backend = current_async_library()
        if self._backend == 'trio':
            self._trio_lock = trio.Lock()
            return None
        if None._backend == 'asyncio':
            self._anyio_lock = anyio.Lock()
            return None

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_value = None, traceback = (None, None, None)):
        pass
    # WARNING: Decompyle incomplete



class AsyncThreadLock:
    '''
    This is a threading-only lock for no-I/O contexts.

    In the sync case `ThreadLock` provides thread locking.
    In the async case `AsyncThreadLock` is a no-op.
    '''
    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = (None, None, None)):
        pass



class AsyncEvent:
    
    def __init__(self = None):
        self._backend = ''

    
    def setup(self = None):
        """
        Detect if we're running under 'asyncio' or 'trio' and create
        a lock with the correct implementation.
        """
        self._backend = current_async_library()
        if self._backend == 'trio':
            self._trio_event = trio.Event()
            return None
        if None._backend == 'asyncio':
            self._anyio_event = anyio.Event()
            return None

    
    def set(self = None):
        if not self._backend:
            self.setup()
        if self._backend == 'trio':
            self._trio_event.set()
            return None
        if None._backend == 'asyncio':
            self._anyio_event.set()
            return None

    
    async def wait(self = None, timeout = None):
        pass
    # WARNING: Decompyle incomplete



class AsyncSemaphore:
    
    def __init__(self = None, bound = None):
        self._bound = bound
        self._backend = ''

    
    def setup(self = None):
        """
        Detect if we're running under 'asyncio' or 'trio' and create
        a semaphore with the correct implementation.
        """
        self._backend = current_async_library()
        if self._backend == 'trio':
            self._trio_semaphore = trio.Semaphore(initial_value = self._bound, max_value = self._bound)
            return None
        if None._backend == 'asyncio':
            self._anyio_semaphore = anyio.Semaphore(initial_value = self._bound, max_value = self._bound)
            return None

    
    async def acquire(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def release(self = None):
        pass
    # WARNING: Decompyle incomplete



class AsyncShieldCancellation:
    
    def __init__(self = None):
        """
        Detect if we're running under 'asyncio' or 'trio' and create
        a shielded scope with the correct implementation.
        """
        self._backend = current_async_library()
        if self._backend == 'trio':
            self._trio_shield = trio.CancelScope(shield = True)
            return None
        if None._backend == 'asyncio':
            self._anyio_shield = anyio.CancelScope(shield = True)
            return None

    
    def __enter__(self = None):
        if self._backend == 'trio':
            self._trio_shield.__enter__()
        elif self._backend == 'asyncio':
            self._anyio_shield.__enter__()
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = (None, None, None)):
        if self._backend == 'trio':
            self._trio_shield.__exit__(exc_type, exc_value, traceback)
            return None
        if None._backend == 'asyncio':
            self._anyio_shield.__exit__(exc_type, exc_value, traceback)
            return None



class Lock:
    '''
    This is a standard lock.

    In the sync case `Lock` provides thread locking.
    In the async case `AsyncLock` provides async locking.
    '''
    
    def __init__(self = None):
        self._lock = threading.Lock()

    
    def __enter__(self = None):
        self._lock.acquire()
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = (None, None, None)):
        self._lock.release()



class ThreadLock:
    '''
    This is a threading-only lock for no-I/O contexts.

    In the sync case `ThreadLock` provides thread locking.
    In the async case `AsyncThreadLock` is a no-op.
    '''
    
    def __init__(self = None):
        self._lock = threading.Lock()

    
    def __enter__(self = None):
        self._lock.acquire()
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = (None, None, None)):
        self._lock.release()



class Event:
    
    def __init__(self = None):
        self._event = threading.Event()

    
    def set(self = None):
        self._event.set()

    
    def wait(self = None, timeout = None):
        if timeout == float('inf'):
            timeout = None
        if not self._event.wait(timeout = timeout):
            raise PoolTimeout()



class Semaphore:
    
    def __init__(self = None, bound = None):
        self._semaphore = threading.Semaphore(value = bound)

    
    def acquire(self = None):
        self._semaphore.acquire()

    
    def release(self = None):
        self._semaphore.release()



class ShieldCancellation:
    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = (None, None, None)):
        pass
