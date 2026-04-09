# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: functools.pyc (Python 3.11)

'''functools.py - Tools for working with functions and callable objects
'''
__all__ = [
    'update_wrapper',
    'wraps',
    'WRAPPER_ASSIGNMENTS',
    'WRAPPER_UPDATES',
    'total_ordering',
    'cache',
    'cmp_to_key',
    'lru_cache',
    'reduce',
    'partial',
    'partialmethod',
    'singledispatch',
    'singledispatchmethod',
    'cached_property']
from abc import get_cache_token
from collections import namedtuple
from reprlib import recursive_repr
from _thread import RLock
from types import GenericAlias
WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__')
WRAPPER_UPDATES = ('__dict__',)

def update_wrapper(wrapper, wrapped, assigned, updated = (WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES)):
    '''Update a wrapper function to look like the wrapped function

       wrapper is the function to be updated
       wrapped is the original function
       assigned is a tuple naming the attributes assigned directly
       from the wrapped function to the wrapper function (defaults to
       functools.WRAPPER_ASSIGNMENTS)
       updated is a tuple naming the attributes of the wrapper that
       are updated with the corresponding attribute from the wrapped
       function (defaults to functools.WRAPPER_UPDATES)
    '''
    for attr in assigned:
        value = getattr(wrapped, attr)
        setattr(wrapper, attr, value)
        except AttributeError:
            continue
        for attr in updated:
            getattr(wrapper, attr).update(getattr(wrapped, attr, { }))
            wrapper.__wrapped__ = wrapped
            return wrapper


def wraps(wrapped, assigned, updated = (WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES)):
    '''Decorator factory to apply update_wrapper() to a wrapper function

       Returns a decorator that invokes update_wrapper() with the decorated
       function as the wrapper argument and the arguments to wraps() as the
       remaining arguments. Default arguments are as for update_wrapper().
       This is a convenience function to simplify applying partial() to
       update_wrapper().
    '''
    return partial(update_wrapper, wrapped = wrapped, assigned = assigned, updated = updated)


def _gt_from_lt(self, other):
