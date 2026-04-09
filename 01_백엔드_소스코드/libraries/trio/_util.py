# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _util.pyc (Python 3.11)

from __future__ import annotations
import collections.abc as collections
import inspect
import signal
from abc import ABCMeta
from collections.abc import Awaitable, Callable, Sequence
from typing import TYPE_CHECKING, Any, NoReturn, TypeVar, final as std_final
from sniffio import thread_local as sniffio_loop
import trio
CallT = TypeVar('CallT', bound = Callable[(..., Any)])
T = TypeVar('T')
RetT = TypeVar('RetT')
if TYPE_CHECKING:
    import sys
    from types import AsyncGeneratorType, TracebackType
    from typing_extensions import TypeVarTuple, Unpack
    if sys.version_info < (3, 11):
        from exceptiongroup import BaseExceptionGroup
    PosArgsT = TypeVarTuple('PosArgsT')

def is_main_thread():
    '''Attempt to reliably check if we are in the main thread.'''
    
    try:
        signal.signal(signal.SIGINT, signal.getsignal(signal.SIGINT))
        return True
    except (TypeError, ValueError):
        return False



def coroutine_or_error(async_fn = None, *args):
    
    def _return_value_looks_like_wrong_library(value = None):
        if isinstance(value, collections.abc.Generator):
            return True
    # WARNING: Decompyle incomplete

    prev_loop, sniffio_loop.name = sniffio_loop.name, 'trio'
# WARNING: Decompyle incomplete


class ConflictDetector:
    """Detect when two tasks are about to perform operations that would
    conflict.

    Use as a synchronous context manager; if two tasks enter it at the same
    time then the second one raises an error. You can use it when there are
    two pieces of code that *would* collide and need a lock if they ever were
    called at the same time, but that should never happen.

    We use this in particular for things like, making sure that two different
    tasks don't call sendall simultaneously on the same stream.

    """
    
    def __init__(self = None, msg = None):
        self._msg = msg
        self._held = False

    
    def __enter__(self = None):
        if self._held:
            raise trio.BusyResourceError(self._msg)
        self._held = True

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
        self._held = False



def async_wraps(cls = None, wrapped_cls = None, attr_name = None):
    '''Similar to wraps, but for async wrappers of non-async functions.'''
    pass
# WARNING: Decompyle incomplete


def fixup_module_metadata(module_name = None, namespace = None):
    pass
# WARNING: Decompyle incomplete


def _init_final_cls(cls = None):
    '''Raises an exception when a final class is subclassed.'''
    raise TypeError(f'''{cls.__module__}.{cls.__qualname__} does not support subclassing''')


def _final_impl(decorated = None):
    '''Decorator that enforces a class to be final (i.e., subclass not allowed).

    If a class uses this metaclass like this::

        @final
        class SomeClass:
            pass

    The metaclass will ensure that no subclass can be created.

    Raises
    ------
    - TypeError if a subclass is created
    '''
    decorated.__init_subclass__ = classmethod(_init_final_cls)
    return std_final(decorated)

if TYPE_CHECKING:
    from typing import final
else:
    final = _final_impl
NoPublicConstructor = <NODE:12>()

def name_asyncgen(agen = None):
    '''Return the fully-qualified name of the async generator function
    that produced the async generator iterator *agen*.
    '''
    if not hasattr(agen, 'ag_code'):
        return repr(agen)
    
    try:
        module = agen.ag_frame.f_globals['__name__']
    except (AttributeError, KeyError):
        module = f'''<{agen.ag_code.co_filename}>'''

    
    try:
        qualname = agen.__qualname__
    except AttributeError:
        qualname = agen.ag_code.co_name

    return f'''{module}.{qualname}'''

if TYPE_CHECKING:
    Fn = TypeVar('Fn', bound = Callable[(..., object)])
    
    def wraps(wrapped = None, assigned = None, updated = None):
        pass

else:
    from functools import wraps

def raise_saving_context(exc = None):
    '''This helper allows re-raising an exception without __context__ being set.'''
    __tracebackhide__ = True
    context = exc.__context__
    
    try:
        raise exc
    except:
        exc.__context__ = context
        del exc
        del context



class MultipleExceptionError(Exception):
    '''Raised by raise_single_exception_from_group if encountering multiple
    non-cancelled exceptions.'''
    pass


def raise_single_exception_from_group(eg = None):
    '''This function takes an exception group that is assumed to have at most
    one non-cancelled exception, which it reraises as a standalone exception.

    This exception may be an exceptiongroup itself, in which case it will not be unwrapped.

    If a :exc:`KeyboardInterrupt` is encountered, a new KeyboardInterrupt is immediately
    raised with the entire group as cause.

    If the group only contains :exc:`Cancelled` it reraises the first one encountered.

    It will retain context and cause of the contained exception, and entirely discard
    the cause/context of the group(s).

    If multiple non-cancelled exceptions are encountered, it raises
    :exc:`AssertionError`.
    '''
    pass
# WARNING: Decompyle incomplete
