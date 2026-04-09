# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: concurrency.pyc (Python 3.11)

'''asyncio-related concurrency functions.'''
from __future__ import annotations
import asyncio
import typing
from typing import Any
from typing import Callable
from typing import Coroutine
from typing import TypeVar
have_greenlet = False
greenlet_error = None

try:
    import greenlet
    have_greenlet = True
    from _concurrency_py3k import await_only
    from _concurrency_py3k import await_fallback
    from _concurrency_py3k import in_greenlet
    from _concurrency_py3k import greenlet_spawn
    from _concurrency_py3k import is_exit_exception
    from _concurrency_py3k import AsyncAdaptedLock
    from _concurrency_py3k import _Runner
except ImportError:
    e = None
    greenlet_error = str(e)
    e = None
    del e
except:
    e = None
    del e

_T = TypeVar('_T')

class _AsyncUtil:
    '''Asyncio util for test suite/ util only'''
    
    def __init__(self = None):
        if have_greenlet:
            self.runner = _Runner()
            return None

    
    def run(self = None, fn = None, *args, **kwargs):
        '''Run coroutine on the loop'''
        pass
    # WARNING: Decompyle incomplete

    
    def run_in_greenlet(self = None, fn = None, *args, **kwargs):
        '''Run sync function in greenlet. Support nested calls'''
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        if have_greenlet:
            self.runner.close()
            return None


if not typing.TYPE_CHECKING or have_greenlet:
    
    def _not_implemented():
        if have_greenlet:
            return None
        raise None('the greenlet library is required to use this function. %s' % greenlet_error if greenlet_error else '')

    
    def is_exit_exception(e):
        return not isinstance(e, Exception)

    
    def await_only(thing):
        _not_implemented()

    
    def await_fallback(thing):
        return thing

    
    def in_greenlet():
        _not_implemented()

    
    def greenlet_spawn(fn, *args, **kw):
        _not_implemented()

    
    def AsyncAdaptedLock(*args, **kw):
        _not_implemented()

    
    def _util_async_run(fn, *arg, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def _util_async_run_coroutine_function(fn, *arg, **kw):
        _not_implemented()

    return None
return None
