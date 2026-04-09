# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cache.pyc (Python 3.11)

''' Caching facility for SymPy '''
from importlib import import_module
from typing import Callable

class _cache(list):
    ''' List of cached functions '''
    
    def print_cache(self):
        '''print cache info'''
        pass
    # WARNING: Decompyle incomplete

    
    def clear_cache(self):
        '''clear cache content'''
        pass
    # WARNING: Decompyle incomplete


CACHE = _cache()
print_cache = CACHE.print_cache
clear_cache = CACHE.clear_cache
from functools import lru_cache, wraps

def __cacheit(maxsize):
    """caching decorator.

        important: the result of cached function must be *immutable*


        Examples
        ========

        >>> from sympy import cacheit
        >>> @cacheit
        ... def f(a, b):
        ...    return a+b

        >>> @cacheit
        ... def f(a, b): # noqa: F811
        ...    return [a, b] # <-- WRONG, returns mutable object

        to force cacheit to check returned results mutability and consistency,
        set environment variable SYMPY_USE_CACHE to 'debug'
    """
    pass
# WARNING: Decompyle incomplete


def __cacheit_nocache(func):
    return func


def __cacheit_debug(maxsize):
    '''cacheit + code to check cache consistency'''
    pass
# WARNING: Decompyle incomplete


def _getenv(key, default = (None,)):
    getenv = getenv
    import os
    return getenv(key, default)

USE_CACHE = _getenv('SYMPY_USE_CACHE', 'yes').lower()
scs = _getenv('SYMPY_CACHE_SIZE', '1000')
if scs.lower() == 'none':
    SYMPY_CACHE_SIZE = None
else:
    
    try:
        SYMPY_CACHE_SIZE = int(scs)
    except ValueError:
        raise RuntimeError('SYMPY_CACHE_SIZE must be a valid integer or None. ' + 'Got: %s' % SYMPY_CACHE_SIZE)

    if USE_CACHE == 'no':
        cacheit = __cacheit_nocache
    elif USE_CACHE == 'yes':
        cacheit = __cacheit(SYMPY_CACHE_SIZE)
    elif USE_CACHE == 'debug':
        cacheit = __cacheit_debug(SYMPY_CACHE_SIZE)
    else:
        raise RuntimeError('unrecognized value for SYMPY_USE_CACHE: %s' % USE_CACHE)
    
    def cached_property(func):
        '''Decorator to cache property method'''
        pass
    # WARNING: Decompyle incomplete

    
    def lazy_function(module = None, name = None):
        '''Create a lazy proxy for a function in a module.

    The module containing the function is not imported until the function is used.

    '''
        pass
    # WARNING: Decompyle incomplete

    return None
