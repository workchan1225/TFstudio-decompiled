# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: logging_pool.pyc (Python 3.11)

'''A thread pool that logs exceptions raised by tasks executed within it.'''
from concurrent import futures
import logging
_LOGGER = logging.getLogger(__name__)

def _wrap(behavior):
    '''Wraps an arbitrary callable behavior in exception-logging.'''
    pass
# WARNING: Decompyle incomplete


class _LoggingPool(object):
    '''An exception-logging futures.ThreadPoolExecutor-compatible thread pool.'''
    
    def __init__(self, backing_pool):
        self._backing_pool = backing_pool

    
    def __enter__(self):
        return self

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._backing_pool.shutdown(wait = True)

    
    def submit(self, fn, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def map(self, func, *iterables, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def shutdown(self, wait = (True,)):
        self._backing_pool.shutdown(wait = wait)



def pool(max_workers):
    '''Creates a thread pool that logs exceptions raised by the tasks within it.

    Args:
      max_workers: The maximum number of worker threads to allow the pool.

    Returns:
      A futures.ThreadPoolExecutor-compatible thread pool that logs exceptions
        raised by the tasks executed within it.
    '''
    return _LoggingPool(futures.ThreadPoolExecutor(max_workers))
