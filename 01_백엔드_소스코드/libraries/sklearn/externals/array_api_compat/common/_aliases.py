# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _aliases.pyc (Python 3.11)

'''
These are functions that are just aliases of existing functions in NumPy.
'''
from __future__ import annotations
import inspect
from typing import TYPE_CHECKING, Any, NamedTuple, Optional, Sequence, cast
from _helpers import _check_device, array_namespace
from _helpers import device as _get_device
from _helpers import is_cupy_namespace as _is_cupy_namespace
from _typing import Array, Device, DType, Namespace
if TYPE_CHECKING:
    from typing_extensions import TypeIs

def arange(start = None, stop = None, step = None, *, xp, dtype, device, **kwargs):
    _check_device(xp, device)
# WARNING: Decompyle incomplete


def empty(shape = None, xp = None, *, dtype, device, **kwargs):
    _check_device(xp, device)
# WARNING: Decompyle incomplete


def empty_like(x = None, xp = None, *, dtype, device, **kwargs):
    _check_device(xp, device)
# WARNING: Decompyle incomplete


def eye(n_rows = None, n_cols = None, *, xp, k, dtype, device, **kwargs):
    _check_device(xp, device)
# WARNING: Decompyle incomplete


def full(shape = None, fill_value = None, xp = None, *, dtype, device, **kwargs):
    _check_device(xp, device)
# WARNING: Decompyle incomplete


def full_like(x = None, fill_value = None, *, xp, dtype, device, **kwargs):
    _check_device(xp, device)
# WARNING: Decompyle incomplete


def linspace(start = None, stop = None, num = None, *, xp, dtype, device, endpoint, **kwargs):
    _check_device(xp, device)
# WARNING: Decompyle incomplete


def ones(shape = None, xp = None, *, dtype, device, **kwargs):
    _check_device(xp, device)
# WARNING: Decompyle incomplete


def ones_like(x = None, xp = None, *, dtype, device, **kwargs):
    _check_device(xp, device)
# WARNING: Decompyle incomplete


def zeros(shape = None, xp = None, *, dtype, device, **kwargs):
    _check_device(xp, device)
# WARNING: Decompyle incomplete


def zeros_like(x = None, xp = None, *, dtype, device, **kwargs):
    _check_device(xp, device)
# WARNING: Decompyle incomplete


class UniqueAllResult(NamedTuple):
    counts: 'Array' = 'UniqueAllResult'


class UniqueCountsResult(NamedTuple):
    counts: 'Array' = 'UniqueCountsResult'


class UniqueInverseResult(NamedTuple):
    inverse_indices: 'Array' = 'UniqueInverseResult'


def _unique_kwargs(xp = None):
    s = inspect.signature(xp.unique)
    if 'equal_nan' in s.parameters:
        return {
            'equal_nan': False }


def unique_all(x = None, xp = None):
    kwargs = _unique_kwargs(xp)
# WARNING: Decompyle incomplete


def unique_counts(x = None, xp = None):
    kwargs = _unique_kwargs(xp)
# WARNING: Decompyle incomplete


def unique_inverse(x = None, xp = None):
    kwargs = _unique_kwargs(xp)
# WARNING: Decompyle incomplete


def unique_values(x = None, xp = None):
    kwargs = _unique_kwargs(xp)
# WARNING: Decompyle incomplete


def std(x = None, xp = None, *, axis, correction, keepdims, **kwargs):
    pass
# WARNING: Decompyle incomplete


def var(x = None, xp = None, *, axis, correction, keepdims, **kwargs):
    pass
# WARNING: Decompyle incomplete


def cumulative_sum(x = None, xp = None, *, axis, dtype, include_initial, **kwargs):
    wrapped_xp = array_namespace(x)
# WARNING: Decompyle incomplete


def cumulative_prod(x = None, xp = None, *, axis, dtype, include_initial, **kwargs):
    wrapped_xp = array_namespace(x)
# WARNING: Decompyle incomplete


def clip(x = None, min = None, max = None, *, xp, out):
    
    def _isscalar(a = None):
        return isinstance(a, (int, float, type(None)))

    min_shape = () if _isscalar(min) else min.shape
    max_shape = () if _isscalar(max) else max.shape
    wrapped_xp = array_namespace(x)
    result_shape = xp.broadcast_shapes(x.shape, min_shape, max_shape)
    if wrapped_xp.isdtype(x.dtype, 'integral'):
        if type(min) is int and min <= wrapped_xp.iinfo(x.dtype).min:
            min = None
        if type(max) is int and max >= wrapped_xp.iinfo(x.dtype).max:
            max = None
    dev = _get_device(x)
# WARNING: Decompyle incomplete


def permute_dims(x = None, axes = None, xp = None):
    return xp.transpose(x, axes)


def reshape(x = None, shape = None, xp = None, *, copy, **kwargs):
    if copy is True:
        x = x.copy()
    elif copy is False:
        y = x.view()
        y.shape = shape
        return y
# WARNING: Decompyle incomplete


def argsort(x = None, xp = None, *, axis, descending, stable, **kwargs):
    if stable:
        kwargs['kind'] = 'stable'
# WARNING: Decompyle incomplete


def sort(x = None, xp = None, *, axis, descending, stable, **kwargs):
    if stable:
        kwargs['kind'] = 'stable'
# WARNING: Decompyle incomplete


def nonzero(x = None, xp = None, **kwargs):
    if x.ndim == 0:
        raise ValueError('nonzero() does not support zero-dimensional arrays')
# WARNING: Decompyle incomplete


def ceil(x = None, xp = None, **kwargs):
    if xp.issubdtype(x.dtype, xp.integer):
        return x
# WARNING: Decompyle incomplete


def floor(x = None, xp = None, **kwargs):
    if xp.issubdtype(x.dtype, xp.integer):
        return x
# WARNING: Decompyle incomplete


def trunc(x = None, xp = None, **kwargs):
    if xp.issubdtype(x.dtype, xp.integer):
        return x
# WARNING: Decompyle incomplete


def matmul(x1 = None, x2 = None, xp = None, **kwargs):
    pass
# WARNING: Decompyle incomplete


def matrix_transpose(x = None, xp = None):
    if x.ndim < 2:
        raise ValueError('x must be at least 2-dimensional for matrix_transpose')
    return xp.swapaxes(x, -1, -2)


def tensordot(x1 = None, x2 = None, xp = None, *, axes, **kwargs):
    pass
# WARNING: Decompyle incomplete


def vecdot(x1 = None, x2 = None, xp = None, *, axis):
    if x1.shape[axis] != x2.shape[axis]:
        raise ValueError('x1 and x2 must have the same size along the given axis')
    if hasattr(xp, 'broadcast_tensors'):
        _broadcast = xp.broadcast_tensors
    else:
        _broadcast = xp.broadcast_arrays
    x1_ = xp.moveaxis(x1, axis, -1)
    x2_ = xp.moveaxis(x2, axis, -1)
    (x1_, x2_) = _broadcast(x1_, x2_)
    res = xp.conj(x1_[(..., None, :)]) @ x2_[(..., None)]
    return res[(..., 0, 0)]


def isdtype(dtype = None, kind = None, xp = None, *, _tuple):
    '''
    Returns a boolean indicating whether a provided dtype is of a specified data type ``kind``.

    Note that outside of this function, this compat library does not yet fully
    support complex numbers.

    See
    https://data-apis.org/array-api/latest/API_specification/generated/array_api.isdtype.html
    for more details
    '''
    pass
# WARNING: Decompyle incomplete


def unstack(x = None, xp = None, *, axis):
    if x.ndim == 0:
        raise ValueError('Input array must be at least 1-d.')
    return tuple(xp.moveaxis(x, axis, 0))


def sign(x = None, xp = None, **kwargs):
    pass
# WARNING: Decompyle incomplete


def finfo(type_ = None, xp = None):
    
    try:
        return xp.finfo(type_)
    except (ValueError, TypeError):
        return 



def iinfo(type_ = None, xp = None):
    
    try:
        return xp.iinfo(type_)
    except (ValueError, TypeError):
        return 


__all__ = [
    'arange',
    'empty',
    'empty_like',
    'eye',
    'full',
    'full_like',
    'linspace',
    'ones',
    'ones_like',
    'zeros',
    'zeros_like',
    'UniqueAllResult',
    'UniqueCountsResult',
    'UniqueInverseResult',
    'unique_all',
    'unique_counts',
    'unique_inverse',
    'unique_values',
    'std',
    'var',
    'cumulative_sum',
    'cumulative_prod',
    'clip',
    'permute_dims',
    'reshape',
    'argsort',
    'sort',
    'nonzero',
    'ceil',
    'floor',
    'trunc',
    'matmul',
    'matrix_transpose',
    'tensordot',
    'vecdot',
    'isdtype',
    'unstack',
    'sign',
    'finfo',
    'iinfo']
_all_ignore = [
    'inspect',
    'array_namespace',
    'NamedTuple']

def __dir__():
    return __all__
