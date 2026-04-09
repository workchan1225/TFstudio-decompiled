# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _contextmanagers.pyc (Python 3.11)

from __future__ import annotations
from abc import abstractmethod
from contextlib import AbstractAsyncContextManager, AbstractContextManager
from inspect import isasyncgen, iscoroutine, isgenerator
from types import TracebackType
from typing import Protocol, TypeVar, cast, final
_T_co = TypeVar('_T_co', covariant = True)
_ExitT_co = TypeVar('_ExitT_co', covariant = True, bound = 'bool | None')

def _SupportsCtxMgr():
    '''_SupportsCtxMgr'''
    
    def __contextmanager__(self = None):
        pass


_SupportsCtxMgr = <NODE:27>(_SupportsCtxMgr, '_SupportsCtxMgr', Protocol[(_T_co, _ExitT_co)])

def _SupportsAsyncCtxMgr():
    '''_SupportsAsyncCtxMgr'''
    
    def __asynccontextmanager__(self = None):
        pass


_SupportsAsyncCtxMgr = <NODE:27>(_SupportsAsyncCtxMgr, '_SupportsAsyncCtxMgr', Protocol[(_T_co, _ExitT_co)])

class ContextManagerMixin:
    """
    Mixin class providing context manager functionality via a generator-based
    implementation.

    This class allows you to implement a context manager via :meth:`__contextmanager__`
    which should return a generator. The mechanics are meant to mirror those of
    :func:`@contextmanager <contextlib.contextmanager>`.

    .. note:: Classes using this mix-in are not reentrant as context managers, meaning
        that once you enter it, you can't re-enter before first exiting it.

    .. seealso:: :doc:`contextmanagers`
    """
    __cm: 'AbstractContextManager[object, bool | None] | None' = None
    __enter__ = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    __exit__ = (lambda self = None, exc_type = None, exc_val = final, exc_tb = ('self', '_SupportsCtxMgr[object, _ExitT_co]', 'exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', '_ExitT_co'): pass# WARNING: Decompyle incomplete
)()
    __contextmanager__ = (lambda self = None: pass)()


class AsyncContextManagerMixin:
    """
    Mixin class providing async context manager functionality via a generator-based
    implementation.

    This class allows you to implement a context manager via
    :meth:`__asynccontextmanager__`. The mechanics are meant to mirror those of
    :func:`@asynccontextmanager <contextlib.asynccontextmanager>`.

    .. note:: Classes using this mix-in are not reentrant as context managers, meaning
        that once you enter it, you can't re-enter before first exiting it.

    .. seealso:: :doc:`contextmanagers`
    """
    __cm: 'AbstractAsyncContextManager[object, bool | None] | None' = None
    __aenter__ = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    __aexit__ = (lambda self = None, exc_type = None, exc_val = final, exc_tb = ('self', '_SupportsAsyncCtxMgr[object, _ExitT_co]', 'exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', '_ExitT_co'): pass# WARNING: Decompyle incomplete
)()
    __asynccontextmanager__ = (lambda self = None: pass)()
