# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _utilities.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import abc as c
import inspect
import typing as t
from weakref import ref
from weakref import WeakMethod
T = t.TypeVar('T')

class Symbol:
    pass
# WARNING: Decompyle incomplete


def make_id(obj = None):
    '''Get a stable identifier for a receiver or sender, to be used as a dict
    key or in a set.
    '''
    if inspect.ismethod(obj):
        return (id(obj.__func__), id(obj.__self__))
    if None(obj, (str, int)):
        return obj
    return None(obj)


def make_ref(obj = None, callback = None):
    if inspect.ismethod(obj):
        return WeakMethod(obj, callback)
    return None(obj, callback)
