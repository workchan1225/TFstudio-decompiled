# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: coroutines.pyc (Python 3.11)

__all__ = ('iscoroutinefunction', 'iscoroutine')
import collections.abc as collections
import inspect
import os
import sys
import traceback
import types

def _is_debug_mode():
    if not sys.flags.dev_mode:
        if not (sys.flags.ignore_environment):
            pass
    return bool(os.environ.get('PYTHONASYNCIODEBUG'))

_is_coroutine = object()

def iscoroutinefunction(func):
    '''Return True if func is a decorated coroutine function.'''
    if not inspect.iscoroutinefunction(func):
        pass
    return getattr(func, '_is_coroutine', None) is _is_coroutine

_COROUTINE_TYPES = (types.CoroutineType, types.GeneratorType, collections.abc.Coroutine)
_iscoroutine_typecache = set()

def iscoroutine(obj):
    '''Return True if obj is a coroutine object.'''
    if type(obj) in _iscoroutine_typecache:
        return True
    if None(obj, _COROUTINE_TYPES):
        if len(_iscoroutine_typecache) < 100:
            _iscoroutine_typecache.add(type(obj))
        return True


def _format_coroutine(coro):
    pass
# WARNING: Decompyle incomplete
