# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _data_type_functions.pyc (Python 3.11)

from __future__ import annotations
from _array_object import Array
from _dtypes import _all_dtypes, _boolean_dtypes, _signed_integer_dtypes, _unsigned_integer_dtypes, _integer_dtypes, _real_floating_dtypes, _complex_floating_dtypes, _numeric_dtypes, _result_type
from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Tuple, Union
if TYPE_CHECKING:
    from _typing import Dtype
    from collections.abc import Sequence
import numpy as np

def astype(x = None, dtype = None, *, copy):
    if copy and dtype == x.dtype:
        return x
    return None._new(x._array.astype(dtype = dtype, copy = copy))


def broadcast_arrays(*arrays):
    '''
    Array API compatible wrapper for :py:func:`np.broadcast_arrays <numpy.broadcast_arrays>`.

    See its docstring for more information.
    '''
    pass
# WARNING: Decompyle incomplete


def broadcast_to(x = None, shape = None):
    '''
    Array API compatible wrapper for :py:func:`np.broadcast_to <numpy.broadcast_to>`.

    See its docstring for more information.
    '''
    Array = Array
    import _array_object
    return Array._new(np.broadcast_to(x._array, shape))


def can_cast(from_ = None, to = None):
    '''
    Array API compatible wrapper for :py:func:`np.can_cast <numpy.can_cast>`.

    See its docstring for more information.
    '''
    if isinstance(from_, Array):
        from_ = from_.dtype
    elif from_ not in _all_dtypes:
        raise TypeError(f'''from_={from_!r}, but should be an array_api array or dtype''')
    if to not in _all_dtypes:
        raise TypeError(f'''to={to!r}, but should be a dtype''')
    
    try:
        dtype = _result_type(from_, to)
        return to == dtype
    except TypeError:
        return False


finfo_object = <NODE:12>()
iinfo_object = <NODE:12>()

def finfo(type = None):
    '''
    Array API compatible wrapper for :py:func:`np.finfo <numpy.finfo>`.

    See its docstring for more information.
    '''
    fi = np.finfo(type)
    return finfo_object(fi.bits, float(fi.eps), float(fi.max), float(fi.min), float(fi.smallest_normal), fi.dtype)


def iinfo(type = None):
    '''
    Array API compatible wrapper for :py:func:`np.iinfo <numpy.iinfo>`.

    See its docstring for more information.
    '''
    ii = np.iinfo(type)
    return iinfo_object(ii.bits, ii.max, ii.min, ii.dtype)


def isdtype(dtype = None, kind = None):
    '''
    Returns a boolean indicating whether a provided dtype is of a specified data type ``kind``.

    See
    https://data-apis.org/array-api/latest/API_specification/generated/array_api.isdtype.html
    for more details
    '''
    pass
# WARNING: Decompyle incomplete


def result_type(*arrays_and_dtypes):
    '''
    Array API compatible wrapper for :py:func:`np.result_type <numpy.result_type>`.

    See its docstring for more information.
    '''
    A = []
    for a in arrays_and_dtypes:
        if isinstance(a, Array):
            a = a.dtype
        elif isinstance(a, np.ndarray) or a not in _all_dtypes:
            raise TypeError('result_type() inputs must be array_api arrays or dtypes')
        A.append(a)
        if len(A) == 0:
            raise ValueError('at least one array or dtype is required')
        if len(A) == 1:
            return A[0]
        t = None[0]
        for t2 in A[1:]:
            t = _result_type(t, t2)
            return t
