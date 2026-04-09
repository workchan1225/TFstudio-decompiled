# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _creation_functions.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional, Tuple, Union
if TYPE_CHECKING:
    from _typing import Array, Device, Dtype, NestedSequence, SupportsBufferProtocol
    from collections.abc import Sequence
from _dtypes import _all_dtypes
import numpy as np

def _check_valid_dtype(dtype):
    for d in (None,) + _all_dtypes:
        if dtype is d:
            return None
        raise ValueError('dtype must be one of the supported dtypes')


def asarray(obj = None, *, dtype, device, copy):
    '''
    Array API compatible wrapper for :py:func:`np.asarray <numpy.asarray>`.

    See its docstring for more information.
    '''
    Array = Array
    import _array_object
    _check_valid_dtype(dtype)
    if device not in ('cpu', None):
        raise ValueError(f'''Unsupported device {device!r}''')
    if copy in (False, np._CopyMode.IF_NEEDED):
        raise NotImplementedError('copy=False is not yet implemented')
# WARNING: Decompyle incomplete


def arange(start = None, stop = None, step = None, *, dtype, device):
    '''
    Array API compatible wrapper for :py:func:`np.arange <numpy.arange>`.

    See its docstring for more information.
    '''
    Array = Array
    import _array_object
    _check_valid_dtype(dtype)
    if device not in ('cpu', None):
        raise ValueError(f'''Unsupported device {device!r}''')
    return Array._new(np.arange(start, stop = stop, step = step, dtype = dtype))


def empty(shape = None, *, dtype, device):
    '''
    Array API compatible wrapper for :py:func:`np.empty <numpy.empty>`.

    See its docstring for more information.
    '''
    Array = Array
    import _array_object
    _check_valid_dtype(dtype)
    if device not in ('cpu', None):
        raise ValueError(f'''Unsupported device {device!r}''')
    return Array._new(np.empty(shape, dtype = dtype))


def empty_like(x = None, *, dtype, device):
    '''
    Array API compatible wrapper for :py:func:`np.empty_like <numpy.empty_like>`.

    See its docstring for more information.
    '''
    Array = Array
    import _array_object
    _check_valid_dtype(dtype)
    if device not in ('cpu', None):
        raise ValueError(f'''Unsupported device {device!r}''')
    return Array._new(np.empty_like(x._array, dtype = dtype))


def eye(n_rows = None, n_cols = None, *, k, dtype, device):
    '''
    Array API compatible wrapper for :py:func:`np.eye <numpy.eye>`.

    See its docstring for more information.
    '''
    Array = Array
    import _array_object
    _check_valid_dtype(dtype)
    if device not in ('cpu', None):
        raise ValueError(f'''Unsupported device {device!r}''')
    return Array._new(np.eye(n_rows, M = n_cols, k = k, dtype = dtype))


def from_dlpack(x = None):
    Array = Array
    import _array_object
    return Array._new(np.from_dlpack(x))


def full(shape = None, fill_value = None, *, dtype, device):
    '''
    Array API compatible wrapper for :py:func:`np.full <numpy.full>`.

    See its docstring for more information.
    '''
    Array = Array
    import _array_object
    _check_valid_dtype(dtype)
    if device not in ('cpu', None):
        raise ValueError(f'''Unsupported device {device!r}''')
    if isinstance(fill_value, Array) and fill_value.ndim == 0:
        fill_value = fill_value._array
    res = np.full(shape, fill_value, dtype = dtype)
    if res.dtype not in _all_dtypes:
        raise TypeError('Invalid input to full')
    return Array._new(res)


def full_like(x = None, fill_value = None, *, dtype, device):
    '''
    Array API compatible wrapper for :py:func:`np.full_like <numpy.full_like>`.

    See its docstring for more information.
    '''
    Array = Array
    import _array_object
    _check_valid_dtype(dtype)
    if device not in ('cpu', None):
        raise ValueError(f'''Unsupported device {device!r}''')
    res = np.full_like(x._array, fill_value, dtype = dtype)
    if res.dtype not in _all_dtypes:
        raise TypeError('Invalid input to full_like')
    return Array._new(res)


def linspace(start = None, stop = None, num = None, *, dtype, device, endpoint):
    '''
    Array API compatible wrapper for :py:func:`np.linspace <numpy.linspace>`.

    See its docstring for more information.
    '''
    Array = Array
    import _array_object
    _check_valid_dtype(dtype)
    if device not in ('cpu', None):
        raise ValueError(f'''Unsupported device {device!r}''')
    return Array._new(np.linspace(start, stop, num, dtype = dtype, endpoint = endpoint))


def meshgrid(*, indexing, *arrays):
    '''
    Array API compatible wrapper for :py:func:`np.meshgrid <numpy.meshgrid>`.

    See its docstring for more information.
    '''
    pass
# WARNING: Decompyle incomplete


def ones(shape = None, *, dtype, device):
    '''
    Array API compatible wrapper for :py:func:`np.ones <numpy.ones>`.

    See its docstring for more information.
    '''
    Array = Array
    import _array_object
    _check_valid_dtype(dtype)
    if device not in ('cpu', None):
        raise ValueError(f'''Unsupported device {device!r}''')
    return Array._new(np.ones(shape, dtype = dtype))


def ones_like(x = None, *, dtype, device):
    '''
    Array API compatible wrapper for :py:func:`np.ones_like <numpy.ones_like>`.

    See its docstring for more information.
    '''
    Array = Array
    import _array_object
    _check_valid_dtype(dtype)
    if device not in ('cpu', None):
        raise ValueError(f'''Unsupported device {device!r}''')
    return Array._new(np.ones_like(x._array, dtype = dtype))


def tril(x = None, *, k):
    '''
    Array API compatible wrapper for :py:func:`np.tril <numpy.tril>`.

    See its docstring for more information.
    '''
    Array = Array
    import _array_object
    if x.ndim < 2:
        raise ValueError('x must be at least 2-dimensional for tril')
    return Array._new(np.tril(x._array, k = k))


def triu(x = None, *, k):
    '''
    Array API compatible wrapper for :py:func:`np.triu <numpy.triu>`.

    See its docstring for more information.
    '''
    Array = Array
    import _array_object
    if x.ndim < 2:
        raise ValueError('x must be at least 2-dimensional for triu')
    return Array._new(np.triu(x._array, k = k))


def zeros(shape = None, *, dtype, device):
    '''
    Array API compatible wrapper for :py:func:`np.zeros <numpy.zeros>`.

    See its docstring for more information.
    '''
    Array = Array
    import _array_object
    _check_valid_dtype(dtype)
    if device not in ('cpu', None):
        raise ValueError(f'''Unsupported device {device!r}''')
    return Array._new(np.zeros(shape, dtype = dtype))


def zeros_like(x = None, *, dtype, device):
    '''
    Array API compatible wrapper for :py:func:`np.zeros_like <numpy.zeros_like>`.

    See its docstring for more information.
    '''
    Array = Array
    import _array_object
    _check_valid_dtype(dtype)
    if device not in ('cpu', None):
        raise ValueError(f'''Unsupported device {device!r}''')
    return Array._new(np.zeros_like(x._array, dtype = dtype))
