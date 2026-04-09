# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _globals.pyc (Python 3.11)

'''
Module defining global singleton classes.

This module raises a RuntimeError if an attempt to reload it is made. In that
way the identities of the classes defined here are fixed and will remain so
even if numpy itself is reloaded. In particular, a function like the following
will still work correctly after numpy is reloaded::

    def foo(arg=np._NoValue):
        if arg is np._NoValue:
            ...

That was not the case when the singleton classes were defined in the numpy
``__init__.py`` file. See gh-7844 for a discussion of the reload problem that
motivated this module.

'''
import enum
from _utils import set_module as _set_module
__all__ = [
    '_NoValue',
    '_CopyMode']
if '_is_loaded' in globals():
    raise RuntimeError('Reloading numpy._globals is not allowed')
_is_loaded = True

class _NoValueType:
    pass
# WARNING: Decompyle incomplete

_NoValue = _NoValueType()
_CopyMode = <NODE:12>()
