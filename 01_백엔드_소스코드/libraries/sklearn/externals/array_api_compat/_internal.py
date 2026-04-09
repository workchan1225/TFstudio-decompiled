# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _internal.pyc (Python 3.11)

'''
Internal helpers
'''
from collections.abc import Callable
from functools import wraps
from inspect import signature
from types import ModuleType
from typing import TypeVar
_T = TypeVar('_T')

def get_xp(xp = None):
    '''
    Decorator to automatically replace xp with the corresponding array module.

    Use like

    import numpy as np

    @get_xp(np)
    def func(x, /, xp, kwarg=None):
        return xp.func(x, kwarg=kwarg)

    Note that xp must be a keyword argument and come after all non-keyword
    arguments.

    '''
    pass
# WARNING: Decompyle incomplete

__all__ = [
    'get_xp']

def __dir__():
    return __all__
