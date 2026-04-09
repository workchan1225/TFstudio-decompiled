# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _searching_functions.pyc (Python 3.11)

from __future__ import annotations
from _array_object import Array
from _dtypes import _result_type, _real_numeric_dtypes
from typing import Optional, Tuple
import numpy as np

def argmax(x = None, *, axis, keepdims):
    '''
    Array API compatible wrapper for :py:func:`np.argmax <numpy.argmax>`.

    See its docstring for more information.
    '''
    if x.dtype not in _real_numeric_dtypes:
        raise TypeError('Only real numeric dtypes are allowed in argmax')
    return Array._new(np.asarray(np.argmax(x._array, axis = axis, keepdims = keepdims)))


def argmin(x = None, *, axis, keepdims):
    '''
    Array API compatible wrapper for :py:func:`np.argmin <numpy.argmin>`.

    See its docstring for more information.
    '''
    if x.dtype not in _real_numeric_dtypes:
        raise TypeError('Only real numeric dtypes are allowed in argmin')
    return Array._new(np.asarray(np.argmin(x._array, axis = axis, keepdims = keepdims)))


def nonzero(x = None):
    '''
    Array API compatible wrapper for :py:func:`np.nonzero <numpy.nonzero>`.

    See its docstring for more information.
    '''
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(np.nonzero(x._array)())


def where(condition = None, x1 = None, x2 = None):
    '''
    Array API compatible wrapper for :py:func:`np.where <numpy.where>`.

    See its docstring for more information.
    '''
    _result_type(x1.dtype, x2.dtype)
    (x1, x2) = Array._normalize_two_args(x1, x2)
    return Array._new(np.where(condition._array, x1._array, x2._array))
