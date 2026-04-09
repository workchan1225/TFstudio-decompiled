# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _aliases.pyc (Python 3.11)

from __future__ import annotations
from builtins import bool as py_bool
from collections.abc import Callable
from typing import TYPE_CHECKING, Any
if TYPE_CHECKING:
    from typing_extensions import TypeIs
from dask.array import array as da
import numpy as np
from numpy import bool_ as bool
from numpy import can_cast, complex64, complex128, float32, float64, int8, int16, int32, int64, result_type, uint8, uint16, uint32, uint64
from _internal import get_xp
from common import _aliases, _helpers, array_namespace
from common._typing import Array, Device, DType, NestedSequence, SupportsBufferProtocol
from _info import __array_namespace_info__
isdtype = get_xp(np)(_aliases.isdtype)
unstack = get_xp(da)(_aliases.unstack)

def astype(x = None, dtype = None, *, copy, device):
    '''
    Array API compatibility wrapper for astype().

    See the corresponding documentation in the array library and/or the array API
    specification for more details.
    '''
    _helpers._check_device(da, device)
    if copy and dtype == x.dtype:
        return x
    x = None.astype(dtype)
    return x.copy() if copy else x


def arange(start = None, stop = None, step = None, *, dtype, device, **kwargs):
    '''
    Array API compatibility wrapper for arange().

    See the corresponding documentation in the array library and/or the array API
    specification for more details.
    '''
    _helpers._check_device(da, device)
    args = [
        start]
# WARNING: Decompyle incomplete

eye = get_xp(da)(_aliases.eye)
linspace = get_xp(da)(_aliases.linspace)
UniqueAllResult = get_xp(da)(_aliases.UniqueAllResult)
UniqueCountsResult = get_xp(da)(_aliases.UniqueCountsResult)
UniqueInverseResult = get_xp(da)(_aliases.UniqueInverseResult)
unique_all = get_xp(da)(_aliases.unique_all)
unique_counts = get_xp(da)(_aliases.unique_counts)
unique_inverse = get_xp(da)(_aliases.unique_inverse)
unique_values = get_xp(da)(_aliases.unique_values)
permute_dims = get_xp(da)(_aliases.permute_dims)
std = get_xp(da)(_aliases.std)
var = get_xp(da)(_aliases.var)
cumulative_sum = get_xp(da)(_aliases.cumulative_sum)
cumulative_prod = get_xp(da)(_aliases.cumulative_prod)
empty = get_xp(da)(_aliases.empty)
empty_like = get_xp(da)(_aliases.empty_like)
full = get_xp(da)(_aliases.full)
full_like = get_xp(da)(_aliases.full_like)
ones = get_xp(da)(_aliases.ones)
ones_like = get_xp(da)(_aliases.ones_like)
zeros = get_xp(da)(_aliases.zeros)
zeros_like = get_xp(da)(_aliases.zeros_like)
reshape = get_xp(da)(_aliases.reshape)
matrix_transpose = get_xp(da)(_aliases.matrix_transpose)
vecdot = get_xp(da)(_aliases.vecdot)
nonzero = get_xp(da)(_aliases.nonzero)
ceil = get_xp(np)(_aliases.ceil)
floor = get_xp(np)(_aliases.floor)
trunc = get_xp(np)(_aliases.trunc)
matmul = get_xp(np)(_aliases.matmul)
tensordot = get_xp(np)(_aliases.tensordot)
sign = get_xp(np)(_aliases.sign)
finfo = get_xp(np)(_aliases.finfo)
iinfo = get_xp(np)(_aliases.iinfo)

def asarray(obj = None, *, dtype, device, copy, **kwargs):
    '''
    Array API compatibility wrapper for asarray().

    See the corresponding documentation in the array library and/or the array API
    specification for more details.
    '''
    _helpers._check_device(da, device)
# WARNING: Decompyle incomplete

from dask.array import arccos as acos
from dask.array import arccosh as acosh
from dask.array import arcsin as asin
from dask.array import arcsinh as asinh
from dask.array import arctan as atan
from dask.array import arctan2 as atan2
from dask.array import arctanh as atanh
from dask.array import concatenate as concat
from dask.array import invert as bitwise_invert
from dask.array import left_shift as bitwise_left_shift
from dask.array import power as pow
from dask.array import right_shift as bitwise_right_shift

def clip(x = None, min = None, max = None):
    '''
    Array API compatibility wrapper for clip().

    See the corresponding documentation in the array library and/or the array API
    specification for more details.
    '''
    
    def _isscalar(a = None):
        if not a is None:
            pass
        return isinstance(a, (int, float))

    min_shape = () if _isscalar(min) else min.shape
    max_shape = () if _isscalar(max) else max.shape
    result_shape = np.broadcast_shapes(x.shape, min_shape, max_shape)
# WARNING: Decompyle incomplete


def _ensure_single_chunk(x = None, axis = None):
    '''
    Make sure that Array is not broken into multiple chunks along axis.

    Returns
    -------
    x : Array
        The input Array with a single chunk along axis.
    restore : Callable[Array, Array]
        function to apply to the output to rechunk it back into reasonable chunks
    '''
    pass
# WARNING: Decompyle incomplete


def sort(x = None, *, axis, descending, stable):
    '''
    Array API compatibility layer around the lack of sort() in Dask.

    Warnings
    --------
    This function temporarily rechunks the array along `axis` to a single chunk.
    This can be extremely inefficient and can lead to out-of-memory errors.

    See the corresponding documentation in the array library and/or the array API
    specification for more details.
    '''
    (x, restore) = _ensure_single_chunk(x, axis)
    meta_xp = array_namespace(x._meta)
    x = da.map_blocks(meta_xp.sort, x, axis = axis, meta = x._meta, dtype = x.dtype, descending = descending, stable = stable)
    return restore(x)


def argsort(x = None, *, axis, descending, stable):
    '''
    Array API compatibility layer around the lack of argsort() in Dask.

    See the corresponding documentation in the array library and/or the array API
    specification for more details.

    Warnings
    --------
    This function temporarily rechunks the array along `axis` into a single chunk.
    This can be extremely inefficient and can lead to out-of-memory errors.
    '''
    (x, restore) = _ensure_single_chunk(x, axis)
    meta_xp = array_namespace(x._meta)
    dtype = meta_xp.argsort(x._meta).dtype
    meta = meta_xp.astype(x._meta, dtype)
    x = da.map_blocks(meta_xp.argsort, x, axis = axis, meta = meta, dtype = dtype, descending = descending, stable = stable)
    return restore(x)


def count_nonzero(x = None, axis = None, keepdims = None):
    result = da.count_nonzero(x, axis)
# WARNING: Decompyle incomplete

__all__ = [
    '__array_namespace_info__',
    'count_nonzero',
    'bool',
    'int8',
    'int16',
    'int32',
    'int64',
    'uint8',
    'uint16',
    'uint32',
    'uint64',
    'float32',
    'float64',
    'complex64',
    'complex128',
    'asarray',
    'astype',
    'can_cast',
    'result_type',
    'pow',
    'concat',
    'acos',
    'acosh',
    'asin',
    'asinh',
    'atan',
    'atan2',
    'atanh',
    'bitwise_left_shift',
    'bitwise_right_shift',
    'bitwise_invert']
__all__ += _aliases.__all__
_all_ignore = [
    'array_namespace',
    'get_xp',
    'da',
    'np']

def __dir__():
    return __all__
