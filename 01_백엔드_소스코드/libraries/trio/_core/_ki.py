# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _ki.pyc (Python 3.11)

from __future__ import annotations
import signal
import sys
import weakref
from typing import TYPE_CHECKING, Generic, Protocol, TypeGuard, TypeVar
import attrs
from _util import is_main_thread
from _run_context import GLOBAL_RUN_CONTEXT
if TYPE_CHECKING:
    import types
    from collections.abc import Callable
    from typing_extensions import Self
_T = TypeVar('_T')

def _IdRef():
    '''_IdRef'''
    _hash: 'int' = ('_hash',)
    
    def __new__(cls = None, ob = None, callback = None):
        self = weakref.ref.__new__(cls, ob, callback)
        self._hash = object.__hash__(ob)
        return self

    
    def __eq__(self = None, other = None):
        if self is other:
            return True
        if not None(other, _IdRef):
            return NotImplemented
        my_obj = None
        
        try:
            my_obj = self()
            if my_obj is not None:
                del my_obj
                return my_obj is other()
            del my_obj


    
    def __ne__(self = None, other = None):
        return not (self == other)

    
    def __hash__(self = None):
        return self._hash


_IdRef = <NODE:27>(_IdRef, '_IdRef', weakref.ref[_T])
_KT = TypeVar('_KT')
_VT = TypeVar('_VT')

def WeakKeyIdentityDictionary():
    '''WeakKeyIdentityDictionary'''
    
    def __init__(self = None):
        self._data = { }
        
        def remove(k = None, selfref = None):
            self = selfref()
        # WARNING: Decompyle incomplete

        self._remove = remove

    
    def __getitem__(self = None, k = None):
        return self._data[_IdRef(k)]

    
    def __setitem__(self = None, k = None, v = None):
        self._data[_IdRef(k, self._remove)] = v


WeakKeyIdentityDictionary = <NODE:27>(WeakKeyIdentityDictionary, 'WeakKeyIdentityDictionary', Generic[(_KT, _VT)])
_CODE_KI_PROTECTION_STATUS_WMAP: 'WeakKeyIdentityDictionary[types.CodeType, bool]' = WeakKeyIdentityDictionary()

def legacy_isasyncgenfunction(obj = None):
    return getattr(obj, '_async_gen_function', None) == id(obj)


def ki_protection_enabled(frame = None):
    
    try:
        task = GLOBAL_RUN_CONTEXT.task
        task_ki_protected = task._ki_protected
        task_frame = task.coro.cr_frame
    except AttributeError:
        task_ki_protected = False
        task_frame = None

# WARNING: Decompyle incomplete


def currently_ki_protected():
    """Check whether the calling code has :exc:`KeyboardInterrupt` protection
    enabled.

    It's surprisingly easy to think that one's :exc:`KeyboardInterrupt`
    protection is enabled when it isn't, or vice-versa. This function tells
    you what Trio thinks of the matter, which makes it useful for ``assert``\\s
    and unit tests.

    Returns:
      bool: True if protection is enabled, and False otherwise.

    """
    return ki_protection_enabled(sys._getframe())


class _SupportsCode(Protocol):
    __code__: 'types.CodeType' = '_SupportsCode'

_T_supports_code = TypeVar('_T_supports_code', bound = _SupportsCode)

def enable_ki_protection(f = None):
    '''Decorator to enable KI protection.'''
    orig = f
    if legacy_isasyncgenfunction(f):
        f = f.__wrapped__
    _CODE_KI_PROTECTION_STATUS_WMAP[f.__code__] = True
    return orig


def disable_ki_protection(f = None):
    '''Decorator to disable KI protection.'''
    orig = f
    if legacy_isasyncgenfunction(f):
        f = f.__wrapped__
    _CODE_KI_PROTECTION_STATUS_WMAP[f.__code__] = False
    return orig

KIManager = <NODE:12>()
