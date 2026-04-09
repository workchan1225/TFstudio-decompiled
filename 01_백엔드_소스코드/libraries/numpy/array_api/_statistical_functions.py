# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _statistical_functions.pyc (Python 3.11)

from __future__ import annotations
from _dtypes import _real_floating_dtypes, _real_numeric_dtypes, _numeric_dtypes
from _array_object import Array
from _dtypes import float32, float64, complex64, complex128
from typing import TYPE_CHECKING, Optional, Tuple, Union
if TYPE_CHECKING:
    from _typing import Dtype
import numpy as np

def max(x = None, *, axis, keepdims):
    if x.dtype not in _real_numeric_dtypes:
        raise TypeError('Only real numeric dtypes are allowed in max')
    return Array._new(np.max(x._array, axis = axis, keepdims = keepdims))


def mean(x = None, *, axis, keepdims):
    if x.dtype not in _real_floating_dtypes:
        raise TypeError('Only real floating-point dtypes are allowed in mean')
    return Array._new(np.mean(x._array, axis = axis, keepdims = keepdims))


def min(x = None, *, axis, keepdims):
    if x.dtype not in _real_numeric_dtypes:
        raise TypeError('Only real numeric dtypes are allowed in min')
    return Array._new(np.min(x._array, axis = axis, keepdims = keepdims))


def prod(x = None, *, axis, dtype, keepdims):
    if x.dtype not in _numeric_dtypes:
        raise TypeError('Only numeric dtypes are allowed in prod')
# WARNING: Decompyle incomplete


def std(x = None, *, axis, correction, keepdims):
    if x.dtype not in _real_floating_dtypes:
        raise TypeError('Only real floating-point dtypes are allowed in std')
    return Array._new(np.std(x._array, axis = axis, ddof = correction, keepdims = keepdims))


def sum(x = None, *, axis, dtype, keepdims):
    if x.dtype not in _numeric_dtypes:
        raise TypeError('Only numeric dtypes are allowed in sum')
# WARNING: Decompyle incomplete


def var(x = None, *, axis, correction, keepdims):
    if x.dtype not in _real_floating_dtypes:
        raise TypeError('Only real floating-point dtypes are allowed in var')
    return Array._new(np.var(x._array, axis = axis, ddof = correction, keepdims = keepdims))
