# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _cachedmethod.pyc (Python 3.11)

'''Method decorator helpers.'''
import functools
import weakref

def warn_cache_none():
    warn = warn
    import warnings
    warn('returning `None` from `cache(self)` is deprecated', DeprecationWarning, stacklevel = 3)


def _condition(method, cache, key, lock, cond):
    pass
# WARNING: Decompyle incomplete


def _locked(method, cache, key, lock):
    pass
# WARNING: Decompyle incomplete


def _unlocked(method, cache, key):
    pass
# WARNING: Decompyle incomplete


def _wrapper(method, cache, key, lock, cond = (None, None)):
    pass
# WARNING: Decompyle incomplete
