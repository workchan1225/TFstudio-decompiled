# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: keys.pyc (Python 3.11)

'''Key functions for memoizing decorators.'''
__all__ = ('hashkey', 'methodkey', 'typedkey', 'typedmethodkey')

class _HashedTuple(tuple):
    '''A tuple that ensures that hash() will be called no more than once
    per element, since cache decorators will hash the key multiple
    times on a cache miss.  See also _HashedSeq in the standard
    library functools implementation.

    '''
    _HashedTuple__hashvalue = None
    
    def __hash__(self, hash = (tuple.__hash__,)):
        hashvalue = self._HashedTuple__hashvalue
    # WARNING: Decompyle incomplete

    
    def __add__(self, other, add = (tuple.__add__,)):
        return _HashedTuple(add(self, other))

    
    def __radd__(self, other, add = (tuple.__add__,)):
        return _HashedTuple(add(other, self))

    
    def __getstate__(self):
        return { }


_kwmark = (_HashedTuple,)

def hashkey(*args, **kwargs):
    '''Return a cache key for the specified hashable arguments.'''
    if kwargs:
        return _HashedTuple(args + sum(sorted(kwargs.items()), _kwmark))
    return None(args)


def methodkey(self, *args, **kwargs):
    '''Return a cache key for use with cached methods.'''
    pass
# WARNING: Decompyle incomplete


def typedkey(*args, **kwargs):
    '''Return a typed cache key for the specified hashable arguments.'''
    pass
# WARNING: Decompyle incomplete


def typedmethodkey(self, *args, **kwargs):
    '''Return a typed cache key for use with cached methods.'''
    pass
# WARNING: Decompyle incomplete
