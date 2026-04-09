# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reduction.pyc (Python 3.11)

import copyreg
import io
import functools
import types
import sys
import os
from multiprocessing import util
from pickle import loads, HIGHEST_PROTOCOL
_dispatch_table = { }

def register(type_, reduce_function):
    _dispatch_table[type_] = reduce_function


def _reduce_method(m):
    pass
# WARNING: Decompyle incomplete


class _C:
    
    def f(self):
        pass

    h = (lambda cls: pass)()

register(type(_C().f), _reduce_method)
register(type(_C.h), _reduce_method)

def _reduce_method_descriptor(m):
    return (getattr, (m.__objclass__, m.__name__))

register(type(list.append), _reduce_method_descriptor)
register(type(int.__add__), _reduce_method_descriptor)

def _reduce_partial(p):
