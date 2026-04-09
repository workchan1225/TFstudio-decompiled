# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: missing.pyc (Python 3.11)

'''
Routines for filling missing data.
'''
from __future__ import annotations
from functools import wraps
from typing import TYPE_CHECKING, Any, Literal, cast, overload
import numpy as np
from pandas._config import is_nan_na
from pandas._libs import NaT, algos, lib
from pandas._typing import ArrayLike, AxisInt, F, ReindexMethod, npt
from pandas.compat._optional import import_optional_dependency
from pandas.core.dtypes.cast import infer_dtype_from
from pandas.core.dtypes.common import is_array_like, is_bool_dtype, is_numeric_dtype, is_object_dtype, needs_i8_conversion
from pandas.core.dtypes.dtypes import ArrowDtype, BaseMaskedDtype, DatetimeTZDtype
from pandas.core.dtypes.missing import is_valid_na_for_dtype, isna, na_value_for_dtype
if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import TypeAlias
    from pandas import Index
    _CubicBC: 'TypeAlias' = Literal[('not-a-knot', 'clamped', 'natural', 'periodic')]

def check_value_size(value = None, mask = None, length = None):
    '''
    Validate the size of the values passed to ExtensionArray.fillna.
    '''
    if is_array_like(value):
        if len(value) != length:
            raise ValueError(f'''Length of \'value\' does not match. Got ({len(value)})  expected {length}''')
        value = value[mask]
    return value


def mask_missing(arr = None, value = None):
    '''
    Return a masking array of same size/shape as arr
    with entries equaling value set to True.

    Parameters
    ----------
    arr : ArrayLike
    value : scalar-like
        Caller has ensured `not is_list_like(value)` and that it can be held
        by `arr`.

    Returns
    -------
    np.ndarray[bool]
    '''
    (dtype, value) = infer_dtype_from(value)
    if not isinstance(arr.dtype, (BaseMaskedDtype, ArrowDtype)) and lib.is_float(value) and np.isnan(value) and is_nan_na():
        if arr.dtype.kind == 'f':
            if isinstance(arr.dtype, BaseMaskedDtype):
                mask = np.isnan(arr._data) & ~arr.isna()
                return mask
            pc = compute
            import pyarrow.compute
            mask = pc.is_nan(arr._pa_array).fill_null(False).to_numpy()
            return mask
        if None.dtype.kind in 'iu':
            mask = np.zeros(arr.shape, dtype = bool)
            return mask
        if None(value):
            return isna(arr)
        mask = None.zeros(arr.shape, dtype = bool)
        if is_numeric_dtype(arr.dtype) and is_bool_dtype(arr.dtype) and lib.is_bool(value):
            pass
        elif not is_bool_dtype(arr.dtype) and is_numeric_dtype(dtype) and lib.is_bool(value):
            pass
        elif is_numeric_dtype(arr.dtype) and isinstance(value, str):
            pass
        elif is_object_dtype(arr.dtype):
            arr_mask = ~isna(arr)
            mask[arr_mask] = arr[arr_mask] == value
        else:
            new_mask = arr == value
            if not isinstance(new_mask, np.ndarray):
                new_mask = new_mask.to_numpy(dtype = bool, na_value = False)
            mask = new_mask
    return mask

clean_fill_method = (lambda method = None, *, allow_nearest: pass)()
clean_fill_method = (lambda method = None, *, allow_nearest: pass)()

def clean_fill_method(method = None, *, allow_nearest):
    if isinstance(method, str):
        method = method.lower()
        if method == 'ffill':
            method = 'pad'
        elif method == 'bfill':
            method = 'backfill'
    valid_methods = [
        'pad',
        'backfill']
    expecting = 'pad (ffill) or backfill (bfill)'
    if allow_nearest:
        valid_methods.append('nearest')
        expecting = 'pad (ffill), backfill (bfill) or nearest'
    if method not in valid_methods:
        raise ValueError(f'''Invalid fill method. Expecting {expecting}. Got {method}''')
    return method

NP_METHODS = [
    'linear',
    'time',
    'index',
    'values']
SP_METHODS = [
    'nearest',
    'zero',
    'slinear',
    'quadratic',
    'cubic',
    'barycentric',
    'krogh',
    'spline',
    'polynomial',
    'from_derivatives',
    'piecewise_polynomial',
    'pchip',
    'akima',
    'cubicspline']

def clean_interp_method(method = None, index = None, **kwargs):
    order = kwargs.get('order')
# WARNING: Decompyle incomplete


def find_valid_index(how = None, is_valid = None):
    """
    Retrieves the positional index of the first valid value.

    Parameters
    ----------
    how : {'first', 'last'}
        Use this parameter to change between the first or last valid index.
    is_valid: np.ndarray
        Mask to find na_values.

    Returns
    -------
    int or None
    """
    pass
# WARNING: Decompyle incomplete


def validate_limit_direction(limit_direction = None):
    valid_limit_directions = [
        'forward',
        'backward',
        'both']
    limit_direction = limit_direction.lower()
    if limit_direction not in valid_limit_directions:
        raise ValueError(f'''Invalid limit_direction: expecting one of {valid_limit_directions}, got \'{limit_direction}\'.''')
    return limit_direction


def validate_limit_area(limit_area = None):
    pass
# WARNING: Decompyle incomplete


def infer_limit_direction(limit_direction = None, method = None):
    pass
# WARNING: Decompyle incomplete


def get_interp_index(method = None, index = None):
