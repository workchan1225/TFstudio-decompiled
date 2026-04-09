# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _concurrency_py3k.pyc (Python 3.11)

from __future__ import annotations
import asyncio
from contextvars import Context
import sys
import typing
from typing import Any
from typing import Awaitable
from typing import Callable
from typing import Coroutine
from typing import Optional
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from langhelpers import memoized_property
from  import exc
from util import py311
from util.typing import Literal
from util.typing import Protocol
from util.typing import Self
from util.typing import TypeGuard
_T = TypeVar('_T')
if typing.TYPE_CHECKING:
    
    class greenlet(Protocol):
        gr_context: 'Optional[Context]' = 'greenlet'
        
        def __init__(self = None, fn = None, driver = None):
            pass

        
        def throw(self = None, *arg):
            pass

        
        def switch(self = None, value = None):
            pass


    
    def getcurrent():
        pass

else:
    from greenlet import getcurrent
    from greenlet import greenlet
_has_gr_context = hasattr(getcurrent(), 'gr_context')

def is_exit_exception(e = None):
    if not not isinstance(e, Exception):
        pass
    return isinstance(e, (asyncio.TimeoutError, asyncio.CancelledError))


class _AsyncIoGreenlet(greenlet):
    dead: 'bool' = '_AsyncIoGreenlet'
    __sqlalchemy_greenlet_provider__ = True
    
    def __init__(self = None, fn = None, driver = None):
        greenlet.__init__(self, fn, driver)
        if _has_gr_context:
            self.gr_context = driver.gr_context
            return None


_T_co = TypeVar('_T_co', covariant = True)

def _safe_cancel_awaitable(awaitable = None):
    if iscoroutine(awaitable):
        awaitable.close()
        return None


def in_greenlet():
    current = getcurrent()
    return getattr(current, '__sqlalchemy_greenlet_provider__', False)


def await_only(awaitable = None):
    '''Awaits an async function in a sync method.

    The sync method must be inside a :func:`greenlet_spawn` context.
    :func:`await_only` calls cannot be nested.

    :param awaitable: The coroutine to call.

    '''
    current = getcurrent()
    if not getattr(current, '__sqlalchemy_greenlet_provider__', False):
        _safe_cancel_awaitable(awaitable)
        raise exc.MissingGreenlet("greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place?")
    return current.parent.switch(awaitable)


def await_fallback(awaitable = None):
    '''Awaits an async function in a sync method.

    The sync method must be inside a :func:`greenlet_spawn` context.
    :func:`await_fallback` calls cannot be nested.

    :param awaitable: The coroutine to call.

    .. deprecated:: 2.0.24 The ``await_fallback()`` function will be removed
       in SQLAlchemy 2.1.  Use :func:`_util.await_only` instead, running the
       function / program / etc. within a top-level greenlet that is set up
       using :func:`_util.greenlet_spawn`.

    '''
    current = getcurrent()
    if not getattr(current, '__sqlalchemy_greenlet_provider__', False):
        loop = get_event_loop()
        if loop.is_running():
            _safe_cancel_awaitable(awaitable)
            raise exc.MissingGreenlet("greenlet_spawn has not been called and asyncio event loop is already running; can't call await_fallback() here. Was IO attempted in an unexpected place?")
        return loop.run_until_complete(awaitable)
    return None.parent.switch(awaitable)


async def greenlet_spawn(fn = None, *, _require_await, *args, **kwargs):
    '''Runs a sync function ``fn`` in a new greenlet.

    The sync function can then use :func:`await_only` to wait for async
    functions.

    :param fn: The sync callable to call.
    :param \\*args: Positional arguments to pass to the ``fn`` callable.
    :param \\*\\*kwargs: Keyword arguments to pass to the ``fn`` callable.
    '''
    pass
# WARNING: Decompyle incomplete


class AsyncAdaptedLock:
    mutex = (lambda self = None: asyncio.Lock())()
    
    def __enter__(self = None):
        return await_fallback(self.mutex.acquire())

    
    def __exit__(self = None, *arg, **kw):
        self.mutex.release()



def get_event_loop():
    '''vendor asyncio.get_event_loop() for python 3.7 and above.

    Python 3.10 deprecates get_event_loop() as a standalone.

    '''
    
    try:
        return asyncio.get_running_loop()
    except RuntimeError:
        pass

    return asyncio.get_event_loop_policy().get_event_loop()

if TYPE_CHECKING and py311:
    _Runner = asyncio.Runner
    return None

class _Runner:
    _loop: 'Union[None, asyncio.AbstractEventLoop, Literal[False]]' = 'Runner implementation for test only'
    
    def __init__(self = None):
        self._loop = None

    
    def __enter__(self = None):
        self._lazy_init()
        return self

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'Any', 'exc_val', 'Any', 'exc_tb', 'Any', 'return', 'None')):
        self.close()

    
    def close(self = None):
        if self._loop:
            
            try:
                self._loop.run_until_complete(self._loop.shutdown_asyncgens())
                self._loop.close()
                self._loop = False
                return None
            except:
                self._loop.close()
                self._loop = False
                return None


    
    def get_loop(self = None):
        '''Return embedded event loop.'''
        self._lazy_init()
    # WARNING: Decompyle incomplete

    
    def run(self = None, coro = None):
        self._lazy_init()
    # WARNING: Decompyle incomplete

    
    def _lazy_init(self = None):
        if self._loop is False:
            raise RuntimeError('Runner is closed')
    # WARNING: Decompyle incomplete
