# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: take.pyc (Python 3.11)

from __future__ import annotations
import functools
from typing import TYPE_CHECKING, cast, overload
import numpy as np
from pandas._libs import algos as libalgos, lib
from pandas.core.dtypes.cast import maybe_promote
from pandas.core.dtypes.common import ensure_platform_int, is_1d_only_ea_dtype
from pandas.core.dtypes.missing import na_value_for_dtype
from pandas.core.construction import ensure_wrapped_if_datetimelike
if TYPE_CHECKING:
    from pandas._typing import ArrayLike, AxisInt, npt
    from pandas.core.arrays._mixins import NDArrayBackedExtensionArray
    from pandas.core.arrays.base import ExtensionArray
take_nd = (lambda arr = None, indexer = None, axis = overload, fill_value = (..., ..., ...), allow_fill = ('arr', 'np.ndarray', 'axis', 'AxisInt', 'allow_fill', 'bool', 'return', 'np.ndarray'): pass)()
take_nd = (lambda arr = None, indexer = None, axis = overload, fill_value = (..., ..., ...), allow_fill = ('arr', 'ExtensionArray', 'axis', 'AxisInt', 'allow_fill', 'bool', 'return', 'ArrayLike'): pass)()

def take_nd(arr = None, indexer = None, axis = None, fill_value = (0, lib.no_default, True), allow_fill = ('arr', 'ArrayLike', 'axis', 'AxisInt', 'allow_fill', 'bool', 'return', 'ArrayLike')):
    '''
    Specialized Cython take which sets NaN values in one pass

    This dispatches to ``take`` defined on ExtensionArrays.

    Note: this function assumes that the indexer is a valid(ated) indexer with
    no out of bound indices.

    Parameters
    ----------
    arr : np.ndarray or ExtensionArray
        Input array.
    indexer : ndarray
        1-D array of indices to take, subarrays corresponding to -1 value
        indices are filed with fill_value
    axis : int, default 0
        Axis to take from
    fill_value : any, default np.nan
        Fill value to replace -1 values with
    allow_fill : bool, default True
        If False, indexer is assumed to contain no -1 values so no filling
        will be done.  This short-circuits computation of a mask.  Result is
        undefined if allow_fill == False and -1 is present in indexer.

    Returns
    -------
    subarray : np.ndarray or ExtensionArray
        May be the same type as the input, or cast to an ndarray.
    '''
    if fill_value is lib.no_default:
        fill_value = na_value_for_dtype(arr.dtype, compat = False)
    elif lib.is_np_dtype(arr.dtype, 'mM'):
        (dtype, fill_value) = maybe_promote(arr.dtype, fill_value)
        if arr.dtype != dtype:
            arr = arr.astype(dtype)
    if not isinstance(arr, np.ndarray):
        if not is_1d_only_ea_dtype(arr.dtype):
            arr = cast('NDArrayBackedExtensionArray', arr)
            return arr.take(indexer, fill_value = fill_value, allow_fill = allow_fill, axis = axis)
        return None.take(indexer, fill_value = fill_value, allow_fill = allow_fill)
    arr = None.asarray(arr)
    return _take_nd_ndarray(arr, indexer, axis, fill_value, allow_fill)


def _take_nd_ndarray(arr, indexer = None, axis = None, fill_value = None, allow_fill = ('arr', 'np.ndarray', 'indexer', 'npt.NDArray[np.intp] | None', 'axis', 'AxisInt', 'allow_fill', 'bool', 'return', 'np.ndarray')):
    pass
# WARNING: Decompyle incomplete


def take_2d_multi(arr = None, indexer = None, fill_value = None):
    '''
    Specialized Cython take which sets NaN values in one pass.
    '''
    pass
# WARNING: Decompyle incomplete

_get_take_nd_function_cached = (lambda ndim = None, arr_dtype = None, out_dtype = functools.lru_cache, axis = ('ndim', 'int', 'arr_dtype', 'np.dtype', 'out_dtype', 'np.dtype', 'axis', 'AxisInt'): tup = (arr_dtype.name, out_dtype.name)if ndim == 1:
func = _take_1d_dict.get(tup, None)elif ndim == 2:
if axis == 0:
func = _take_2d_axis0_dict.get(tup, None)else:
func = _take_2d_axis1_dict.get(tup, None)# WARNING: Decompyle incomplete
)()

def _get_take_nd_function(ndim = None, arr_dtype = None, out_dtype = None, axis = (0, None), mask_info = ('ndim', 'int', 'arr_dtype', 'np.dtype', 'out_dtype', 'np.dtype', 'axis', 'AxisInt')):
    '''
    Get the appropriate "take" implementation for the given dimension, axis
    and dtypes.
    '''
    pass
# WARNING: Decompyle incomplete


def _view_wrapper(f, arr_dtype, out_dtype, fill_wrap = (None, None, None)):
    pass
# WARNING: Decompyle incomplete


def _convert_wrapper(f, conv_dtype):
    pass
# WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete
