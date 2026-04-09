# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _eventloop.pyc (Python 3.11)

from __future__ import annotations
import math
import sys
import threading
from collections.abc import Awaitable, Callable, Generator
from contextlib import contextmanager
from contextvars import Token
from importlib import import_module
from typing import TYPE_CHECKING, Any, TypeVar
if sys.version_info >= (3, 11):
    from typing import TypeVarTuple, Unpack
else:
    from typing_extensions import TypeVarTuple, Unpack
sniffio: 'Any'

try:
    import sniffio
except ModuleNotFoundError:
    sniffio = None

if TYPE_CHECKING:
    from abc import AsyncBackend
BACKENDS = ('asyncio', 'trio')
T_Retval = TypeVar('T_Retval')
PosArgsT = TypeVarTuple('PosArgsT')
threadlocals = threading.local()
loaded_backends: 'dict[str, type[AsyncBackend]]' = { }

def run(func = None, *, backend, backend_options, *args):
    '''
    Run the given coroutine function in an asynchronous event loop.

    The current thread must not be already running an event loop.

    :param func: a coroutine function
    :param args: positional arguments to ``func``
    :param backend: name of the asynchronous event loop implementation – currently
        either ``asyncio`` or ``trio``
    :param backend_options: keyword arguments to call the backend ``run()``
        implementation with (documented :ref:`here <backend options>`)
    :return: the return value of the coroutine function
    :raises RuntimeError: if an asynchronous event loop is already running in this
        thread
    :raises LookupError: if the named backend is not found

    '''
    asynclib_name = current_async_library()
    if current_async_library():
        raise RuntimeError(f'''Already running {asynclib_name} in this thread''')
    
    try:
        async_backend = get_async_backend(backend)
    except ImportError:
        exc = None
        raise LookupError(f'''No such backend: {backend}'''), exc
        exc = None
        del exc

    token = None
# WARNING: Decompyle incomplete


async def sleep(delay = None):
    '''
    Pause the current task for the specified duration.

    :param delay: the duration, in seconds

    '''
    pass
# WARNING: Decompyle incomplete


async def sleep_forever():
    """
    Pause the current task until it's cancelled.

    This is a shortcut for ``sleep(math.inf)``.

    .. versionadded:: 3.1

    """
    pass
# WARNING: Decompyle incomplete


async def sleep_until(deadline = None):
    '''
    Pause the current task until the given time.

    :param deadline: the absolute time to wake up at (according to the internal
        monotonic clock of the event loop)

    .. versionadded:: 3.1

    '''
    pass
# WARNING: Decompyle incomplete


def current_time():
    """
    Return the current value of the event loop's internal clock.

    :return: the clock value (seconds)

    """
    return get_async_backend().current_time()


def get_all_backends():
    '''Return a tuple of the names of all built-in backends.'''
    return BACKENDS


def get_available_backends():
    '''
    Test for the availability of built-in backends.

    :return a tuple of the built-in backend names that were successfully imported

    .. versionadded:: 4.12

    '''
    available_backends = []
    for backend_name in get_all_backends():
        get_async_backend(backend_name)
    except ImportError:
        continue
    available_backends.append(backend_name)
    continue
    return tuple(available_backends)


def get_cancelled_exc_class():
    """Return the current async library's cancellation exception class."""
    return get_async_backend().cancelled_exception_class()

claim_worker_thread = (lambda backend_class = None, token = None: pass# WARNING: Decompyle incomplete
)()

class NoCurrentAsyncBackend(Exception):
    pass
# WARNING: Decompyle incomplete


def get_async_backend(asynclib_name = None):
    pass
# WARNING: Decompyle incomplete


def current_async_library():
    pass
# WARNING: Decompyle incomplete


def set_current_async_library(asynclib_name = None):
    pass
# WARNING: Decompyle incomplete


def reset_current_async_library(token = None):
    pass
# WARNING: Decompyle incomplete
