# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

from __future__ import annotations
import abc
import functools
from typing import Any
from typing import AsyncGenerator
from typing import AsyncIterator
from typing import Awaitable
from typing import Callable
from typing import ClassVar
from typing import Dict
from typing import Generator
from typing import Generic
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Tuple
from typing import TypeVar
import weakref
from  import exc as async_exc
from  import util
from util.typing import Literal
from util.typing import Self
_T = TypeVar('_T', bound = Any)
_T_co = TypeVar('_T_co', bound = Any, covariant = True)
_PT = TypeVar('_PT', bound = Any)

def ReversibleProxy():
    '''ReversibleProxy'''
    _proxy_objects: 'ClassVar[Dict[weakref.ref[Any], weakref.ref[ReversibleProxy[Any]]]]' = { }
    __slots__ = ('__weakref__',)
    _assign_proxied = (lambda self = None, target = None: pass)()
    _assign_proxied = (lambda self = None, target = None: pass)()
    
    def _assign_proxied(self = None, target = None):
        pass
    # WARNING: Decompyle incomplete

    _target_gced = (lambda cls = None, ref = None, proxy_ref = classmethod: cls._proxy_objects.pop(ref, None))()
    _regenerate_proxy_for_target = (lambda cls = None, target = None: raise NotImplementedError())()
    _retrieve_proxy_for_target = (lambda cls = None, target = overload, regenerate = classmethod: pass)()()
    _retrieve_proxy_for_target = (lambda cls = None, target = overload, regenerate = classmethod: pass)()()
    _retrieve_proxy_for_target = (lambda cls = None, target = None, regenerate = classmethod: pass# WARNING: Decompyle incomplete
)()

ReversibleProxy = <NODE:27>(ReversibleProxy, 'ReversibleProxy', Generic[_PT])

def StartableContext():
    '''StartableContext'''
    __slots__ = ()
    start = (lambda self = None, is_ctxmanager = None: pass# WARNING: Decompyle incomplete
)()
    
    def __await__(self = None):
        return self.start().__await__()

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    __aexit__ = (lambda self = None, type_ = None, value = abc.abstractmethod, traceback = ('type_', 'Any', 'value', 'Any', 'traceback', 'Any', 'return', 'Optional[bool]'): pass# WARNING: Decompyle incomplete
)()
    
    def _raise_for_not_started(self = None):
        raise async_exc.AsyncContextNotStarted('%s context has not been started and object has not been awaited.' % self.__class__.__name__)


StartableContext = <NODE:27>(StartableContext, 'StartableContext', Awaitable[_T_co], abc.ABC)

def GeneratorStartableContext():
    '''GeneratorStartableContext'''
    gen: 'AsyncGenerator[_T_co, Any]' = ('gen',)
    
    def __init__(self = None, func = None, args = None, kwds = ('func', 'Callable[..., AsyncIterator[_T_co]]', 'args', 'Tuple[Any, ...]', 'kwds', 'Dict[str, Any]')):
        pass
    # WARNING: Decompyle incomplete

    
    async def start(self = None, is_ctxmanager = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, typ = None, value = None, traceback = ('typ', 'Any', 'value', 'Any', 'traceback', 'Any', 'return', 'Optional[bool]')):
        pass
    # WARNING: Decompyle incomplete


GeneratorStartableContext = <NODE:27>(GeneratorStartableContext, 'GeneratorStartableContext', StartableContext[_T_co])

def asyncstartablecontext(func = None):
    """@asyncstartablecontext decorator.

    the decorated function can be called either as ``async with fn()``, **or**
    ``await fn()``.   This is decidedly different from what
    ``@contextlib.asynccontextmanager`` supports, and the usage pattern
    is different as well.

    Typical usage:

    .. sourcecode:: text

        @asyncstartablecontext
        async def some_async_generator(<arguments>):
            <setup>
            try:
                yield <value>
            except GeneratorExit:
                # return value was awaited, no context manager is present
                # and caller will .close() the resource explicitly
                pass
            else:
                <context manager cleanup>


    Above, ``GeneratorExit`` is caught if the function were used as an
    ``await``.  In this case, it's essential that the cleanup does **not**
    occur, so there should not be a ``finally`` block.

    If ``GeneratorExit`` is not invoked, this means we're in ``__aexit__``
    and we were invoked as a context manager, and cleanup should proceed.


    """
    pass
# WARNING: Decompyle incomplete


def ProxyComparable():
    '''ProxyComparable'''
    __slots__ = ()
    _proxied = (lambda self = None: raise NotImplementedError())()
    
    def __hash__(self = None):
        return id(self)

    
    def __eq__(self = None, other = None):
