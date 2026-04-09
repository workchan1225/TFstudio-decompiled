# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _utility_functions.pyc (Python 3.11)

from __future__ import annotations
from _array_object import Array
from typing import Optional, Tuple, Union
import numpy as np

def all(x = None, *, axis, keepdims):
    '''
    Array API compatible wrapper for :py:func:`np.all <numpy.all>`.

    See its docstring for more information.
    '''
    return Array._new(np.asarray(np.all(x._array, axis = axis, keepdims = keepdims)))


def any(x = None, *, axis, keepdims):
    '''
    Array API compatible wrapper for :py:func:`np.any <numpy.any>`.

    See its docstring for more information.
    '''
    return Array._new(np.asarray(np.any(x._array, axis = axis, keepdims = keepdims)))
