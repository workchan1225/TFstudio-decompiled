# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: nanops.pyc (Python 3.11)

from __future__ import annotations
import functools
import itertools
from typing import TYPE_CHECKING, Any, cast
import warnings
import numpy as np
from pandas._config import get_option
from pandas._libs import NaT, NaTType, iNaT, lib
from pandas._typing import ArrayLike, AxisInt, CorrelationMethod, Dtype, DtypeObj, F, Scalar, Shape, npt
from pandas.compat._optional import import_optional_dependency
from pandas.core.dtypes.common import is_complex, is_float, is_float_dtype, is_integer, is_numeric_dtype, is_object_dtype, needs_i8_conversion, pandas_dtype
from pandas.core.dtypes.missing import isna, na_value_for_dtype, notna
if TYPE_CHECKING:
    from collections.abc import Callable
bn = import_optional_dependency('bottleneck', errors = 'warn')
_BOTTLENECK_INSTALLED = bn is not None
_USE_BOTTLENECK = False

def set_use_bottleneck(v = None):
    global _USE_BOTTLENECK
    if _BOTTLENECK_INSTALLED:
        _USE_BOTTLENECK = v
        return None

set_use_bottleneck(get_option('compute.use_bottleneck'))

class disallow:
    pass
# WARNING: Decompyle incomplete


class bottleneck_switch:
    
    def __init__(self = None, name = None, **kwargs):
        self.name = name
        self.kwargs = kwargs

    
    def __call__(self = None, alt = None):
        pass
    # WARNING: Decompyle incomplete



def _bn_ok_dtype(dtype = None, name = None):
    if not dtype != object and needs_i8_conversion(dtype):
        return name not in ('nansum', 'nanprod', 'nanmean')


def _has_infs(result = None):
    if isinstance(result, np.ndarray) and result.dtype in ('f8', 'f4'):
        return lib.has_infs(result.ravel('K'))
    
    try:
        return np.isinf(result).any()
    except (TypeError, NotImplementedError):
        return False



def _get_fill_value(dtype = None, fill_value = None, fill_value_typ = None):
    '''return the correct fill value for the dtype of the values'''
    pass
# WARNING: Decompyle incomplete


def _maybe_get_mask(values = None, skipna = None, mask = None):
    '''
    Compute a mask if and only if necessary.

    This function will compute a mask iff it is necessary. Otherwise,
    return the provided mask (potentially None) when a mask does not need to be
    computed.

    A mask is never necessary if the values array is of boolean or integer
    dtypes, as these are incapable of storing NaNs. If passing a NaN-capable
    dtype that is interpretable as either boolean or integer data (eg,
    timedelta64), a mask must be provided.

    If the skipna parameter is False, a new mask will not be computed.

    The mask is computed using isna() by default. Setting invert=True selects
    notna() as the masking function.

    Parameters
    ----------
    values : ndarray
        input array to potentially compute mask for
    skipna : bool
        boolean for whether NaNs should be skipped
    mask : Optional[ndarray]
        nan-mask if known

    Returns
    -------
    Optional[np.ndarray[bool]]
    '''
    pass
# WARNING: Decompyle incomplete


def _get_values(values = None, skipna = None, fill_value = None, fill_value_typ = (None, None, None), mask = ('values', 'np.ndarray', 'skipna', 'bool', 'fill_value', 'Any', 'fill_value_typ', 'str | None', 'mask', 'npt.NDArray[np.bool_] | None', 'return', 'tuple[np.ndarray, npt.NDArray[np.bool_] | None]')):
    """
    Utility to get the values view, mask, dtype, dtype_max, and fill_value.

    If both mask and fill_value/fill_value_typ are not None and skipna is True,
    the values array will be copied.

    For input arrays of boolean or integer dtypes, copies will only occur if a
    precomputed mask, a fill_value/fill_value_typ, and skipna=True are
    provided.

    Parameters
    ----------
    values : ndarray
        input array to potentially compute mask for
    skipna : bool
        boolean for whether NaNs should be skipped
    fill_value : Any
        value to fill NaNs with
    fill_value_typ : str
        Set to '+inf' or '-inf' to handle dtype-specific infinities
    mask : Optional[np.ndarray[bool]]
        nan-mask if known

    Returns
    -------
    values : ndarray
        Potential copy of input value array
    mask : Optional[ndarray[bool]]
        Mask for values, if deemed necessary to compute
    """
    mask = _maybe_get_mask(values, skipna, mask)
    dtype = values.dtype
    datetimelike = False
    if values.dtype.kind in 'mM':
        values = np.asarray(values.view('i8'))
        datetimelike = True
# WARNING: Decompyle incomplete


def _get_dtype_max(dtype = None):
    dtype_max = dtype
    if dtype.kind in 'bi':
        dtype_max = np.dtype(np.int64)
    elif dtype.kind == 'u':
        dtype_max = np.dtype(np.uint64)
    elif dtype.kind == 'f':
        dtype_max = np.dtype(np.float64)
    return dtype_max


def _na_ok_dtype(dtype = None):
    if needs_i8_conversion(dtype):
        return False
    return not None(dtype.type, np.integer)


def _wrap_results(result = None, dtype = None, fill_value = None):
    '''wrap our results if needed'''
    if result is NaT:
        pass
# WARNING: Decompyle incomplete


def _datetimelike_compat(func = None):
    '''
    If we have datetime64 or timedelta64 values, ensure we have a correct
    mask before calling the wrapped function, then cast back afterwards.
    '''
    pass
# WARNING: Decompyle incomplete


def _na_for_min_count(values = None, axis = None):
    '''
    Return the missing value for `values`.

    Parameters
    ----------
    values : ndarray
    axis : int or None
        axis for the reduction, required if values.ndim > 1.

    Returns
    -------
    result : scalar or ndarray
        For 1-D values, returns a scalar of the correct missing type.
        For 2-D values, returns a 1-D array where each element is missing.
    '''
    if values.dtype.kind in 'iufcb':
        values = values.astype('float64')
    fill_value = na_value_for_dtype(values.dtype)
    if values.ndim == 1:
        return fill_value
# WARNING: Decompyle incomplete


def maybe_operate_rowwise(func = None):
    '''
    NumPy operations on C-contiguous ndarrays with axis=1 can be
    very slow if axis 1 >> axis 0.
    Operate row-by-row and concatenate the results.
    '''
    pass
# WARNING: Decompyle incomplete


def nanany(values = None, *, axis, skipna, mask):
    '''
    Check if any elements along an axis evaluate to True.

    Parameters
    ----------
    values : ndarray
    axis : int, optional
    skipna : bool, default True
    mask : ndarray[bool], optional
        nan-mask if known

    Returns
    -------
    result : bool

    Examples
    --------
    >>> from pandas.core import nanops
    >>> s = pd.Series([1, 2])
    >>> nanops.nanany(s.values)
    np.True_

    >>> from pandas.core import nanops
    >>> s = pd.Series([np.nan])
    >>> nanops.nanany(s.values)
    np.False_
    '''
    pass
# WARNING: Decompyle incomplete


def nanall(values = None, *, axis, skipna, mask):
    '''
    Check if all elements along an axis evaluate to True.

    Parameters
    ----------
    values : ndarray
    axis : int, optional
    skipna : bool, default True
    mask : ndarray[bool], optional
        nan-mask if known

    Returns
    -------
    result : bool

    Examples
    --------
    >>> from pandas.core import nanops
    >>> s = pd.Series([1, 2, np.nan])
    >>> nanops.nanall(s.values)
    np.True_

    >>> from pandas.core import nanops
    >>> s = pd.Series([1, 0])
    >>> nanops.nanall(s.values)
    np.False_
    '''
    pass
# WARNING: Decompyle incomplete

nansum = (lambda values = None, *, axis: dtype = values.dtype(values, mask) = _get_values(values, skipna, fill_value = 0, mask = mask)dtype_sum = _get_dtype_max(dtype)if dtype.kind == 'f':
dtype_sum = dtypeelif dtype.kind == 'm':
dtype_sum = np.dtype(np.float64)the_sum = values.sum(axis, dtype = dtype_sum)the_sum = _maybe_null_out(the_sum, axis, mask, values.shape, min_count = min_count)the_sum)()()()

def _mask_datetimelike_result(result = None, axis = None, mask = None, orig_values = ('result', 'np.ndarray | np.datetime64 | np.timedelta64', 'axis', 'AxisInt | None', 'mask', 'npt.NDArray[np.bool_]', 'orig_values', 'np.ndarray', 'return', 'np.ndarray | np.datetime64 | np.timedelta64 | NaTType')):
    if isinstance(result, np.ndarray):
        result = result.astype('i8').view(orig_values.dtype)
        axis_mask = mask.any(axis = axis)
        result[axis_mask] = iNaT
    elif mask.any():
        return np.int64(iNaT).view(orig_values.dtype)
    return result

nanmean = (lambda values = None, *, axis: pass# WARNING: Decompyle incomplete
)()()
nanmedian = (lambda values = None, *, axis: pass# WARNING: Decompyle incomplete
)()

def _get_empty_reduction_result(shape = None, axis = None):
    '''
    The result from a reduction on an empty ndarray.

    Parameters
    ----------
    shape : Tuple[int, ...]
    axis : int

    Returns
    -------
    np.ndarray
    '''
    shp = np.array(shape)
    dims = np.arange(len(shape))
    ret = np.empty(shp[dims != axis], dtype = np.float64)
    ret.fill(np.nan)
    return ret


def _get_counts_nanvar(values_shape = None, mask = None, axis = None, ddof = (np.dtype(np.float64),), dtype = ('values_shape', 'Shape', 'mask', 'npt.NDArray[np.bool_] | None', 'axis', 'AxisInt | None', 'ddof', 'int', 'dtype', 'np.dtype', 'return', 'tuple[float | np.ndarray, float | np.ndarray]')):
    '''
    Get the count of non-null values along an axis, accounting
    for degrees of freedom.

    Parameters
    ----------
    values_shape : Tuple[int, ...]
        shape tuple from values ndarray, used if mask is None
    mask : Optional[ndarray[bool]]
        locations in values that should be considered missing
    axis : Optional[int]
        axis to count along
    ddof : int
        degrees of freedom
    dtype : type, optional
        type to use for count

    Returns
    -------
    count : int, np.nan or np.ndarray
    d : int, np.nan or np.ndarray
    '''
    count = _get_counts(values_shape, mask, axis, dtype = dtype)
    d = count - dtype.type(ddof)
    if is_float(count):
        if count <= ddof:
            count = np.nan
            d = np.nan
        else:
            count = cast(np.ndarray, count)
            mask = count <= ddof
            if mask.any():
                np.putmask(d, mask, np.nan)
                np.putmask(count, mask, np.nan)
    return (count, d)

nanstd = (lambda values = None, *, axis: if values.dtype.kind == 'M':
unit = np.datetime_data(values.dtype)[0]values = values.view(f'''m8[{unit}]''')orig_dtype = values.dtype(values, mask) = _get_values(values, skipna, mask = mask)result = np.sqrt(nanvar(values, axis = axis, skipna = skipna, ddof = ddof, mask = mask))_wrap_results(result, orig_dtype))()
nanvar = (lambda values = None, *, axis: dtype = values.dtypemask = _maybe_get_mask(values, skipna, mask)# WARNING: Decompyle incomplete
)()()
nansem = (lambda values = None, *, axis: nanvar(values, axis = axis, skipna = skipna, ddof = ddof, mask = mask)mask = _maybe_get_mask(values, skipna, mask)if values.dtype.kind != 'f':
values = values.astype('f8')# WARNING: Decompyle incomplete
)()

def _nanminmax(meth, fill_value_typ):
    pass
# WARNING: Decompyle incomplete

nanmin = _nanminmax('min', fill_value_typ = '+inf')
nanmax = _nanminmax('max', fill_value_typ = '-inf')

def nanargmax(values = None, *, axis, skipna, mask):
    '''
    Parameters
    ----------
    values : ndarray
    axis : int, optional
    skipna : bool, default True
    mask : ndarray[bool], optional
        nan-mask if known

    Returns
    -------
    result : int or ndarray[int]
        The index/indices  of max value in specified axis or -1 in the NA case

    Examples
    --------
    >>> from pandas.core import nanops
    >>> arr = np.array([1, 2, 3, np.nan, 4])
    >>> nanops.nanargmax(arr)
    np.int64(4)

    >>> arr = np.array(range(12), dtype=np.float64).reshape(4, 3)
    >>> arr[2:, 2] = np.nan
    >>> arr
    array([[ 0.,  1.,  2.],
           [ 3.,  4.,  5.],
           [ 6.,  7., nan],
           [ 9., 10., nan]])
    >>> nanops.nanargmax(arr, axis=1)
    array([2, 2, 1, 1])
    '''
    (values, mask) = _get_values(values, True, fill_value_typ = '-inf', mask = mask)
    result = values.argmax(axis)
    result = _maybe_arg_null_out(result, axis, mask, skipna)
    return result


def nanargmin(values = None, *, axis, skipna, mask):
    '''
    Parameters
    ----------
    values : ndarray
    axis : int, optional
    skipna : bool, default True
    mask : ndarray[bool], optional
        nan-mask if known

    Returns
    -------
    result : int or ndarray[int]
        The index/indices of min value in specified axis or -1 in the NA case

    Examples
    --------
    >>> from pandas.core import nanops
    >>> arr = np.array([1, 2, 3, np.nan, 4])
    >>> nanops.nanargmin(arr)
    np.int64(0)

    >>> arr = np.array(range(12), dtype=np.float64).reshape(4, 3)
    >>> arr[2:, 0] = np.nan
    >>> arr
    array([[ 0.,  1.,  2.],
           [ 3.,  4.,  5.],
           [nan,  7.,  8.],
           [nan, 10., 11.]])
    >>> nanops.nanargmin(arr, axis=1)
    array([0, 0, 1, 1])
    '''
    (values, mask) = _get_values(values, True, fill_value_typ = '+inf', mask = mask)
    result = values.argmin(axis)
    result = _maybe_arg_null_out(result, axis, mask, skipna)
    return result

nanskew = (lambda values = None, *, axis: mask = _maybe_get_mask(values, skipna, mask)if values.dtype.kind != 'f':
values = values.astype('f8')count = _get_counts(values.shape, mask, axis)else:
count = _get_counts(values.shape, mask, axis, dtype = values.dtype)# WARNING: Decompyle incomplete
)()()
nankurt = (lambda values = None, *, axis: mask = _maybe_get_mask(values, skipna, mask)if values.dtype.kind != 'f':
values = values.astype('f8')count = _get_counts(values.shape, mask, axis)else:
count = _get_counts(values.shape, mask, axis, dtype = values.dtype)# WARNING: Decompyle incomplete
)()()
nanprod = (lambda values = None, *, axis: mask = _maybe_get_mask(values, skipna, mask)# WARNING: Decompyle incomplete
)()()

def _maybe_arg_null_out(result = None, axis = None, mask = None, skipna = ('result', 'np.ndarray', 'axis', 'AxisInt | None', 'mask', 'npt.NDArray[np.bool_] | None', 'skipna', 'bool', 'return', 'np.ndarray | int')):
    pass
# WARNING: Decompyle incomplete


def _get_counts(values_shape = None, mask = None, axis = None, dtype = (np.dtype(np.float64),)):
    '''
    Get the count of non-null values along an axis

    Parameters
    ----------
    values_shape : tuple of int
        shape tuple from values ndarray, used if mask is None
    mask : Optional[ndarray[bool]]
        locations in values that should be considered missing
    axis : Optional[int]
        axis to count along
    dtype : type, optional
        type to use for count

    Returns
    -------
    count : scalar or array
    '''
    pass
# WARNING: Decompyle incomplete


def _maybe_null_out(result, axis = None, mask = None, shape = None, min_count = (1, False), datetimelike = ('result', 'np.ndarray | float | NaTType', 'axis', 'AxisInt | None', 'mask', 'npt.NDArray[np.bool_] | None', 'shape', 'tuple[int, ...]', 'min_count', 'int', 'datetimelike', 'bool', 'return', 'np.ndarray | float | NaTType')):
    '''
    Returns
    -------
    Dtype
        The product of all elements on a given axis. ( NaNs are treated as 1)
    '''
    pass
# WARNING: Decompyle incomplete


def check_below_min_count(shape = None, mask = None, min_count = None):
    '''
    Check for the `min_count` keyword. Returns True if below `min_count` (when
    missing value should be returned from the reduction).

    Parameters
    ----------
    shape : tuple
        The shape of the values (`values.shape`).
    mask : ndarray[bool] or None
        Boolean numpy array (typically of same shape as `shape`) or None.
    min_count : int
        Keyword passed through from sum/prod call.

    Returns
    -------
    bool
    '''
    pass
# WARNING: Decompyle incomplete


def _zero_out_fperr(arg = None, tol = None):
    if isinstance(arg, np.ndarray):
        return np.where(np.abs(arg) < tol, 0, arg)
    return arg.dtype.type(0) if None.abs(arg) < tol else arg

nancorr = (lambda a = None, b = None, *, method, min_periods: if len(a) != len(b):
raise AssertionError('Operands to nancorr must have same size')# WARNING: Decompyle incomplete
)()

def get_corr_func(method = None):
    pass
# WARNING: Decompyle incomplete

nancov = (lambda a = None, b = None, *, min_periods, ddof: if len(a) != len(b):
raise AssertionError('Operands to nancov must have same size')# WARNING: Decompyle incomplete
)()

def _ensure_numeric(x):
    if isinstance(x, np.ndarray):
        if x.dtype.kind in 'biu':
            x = x.astype(np.float64)
        elif x.dtype == object:
            inferred = lib.infer_dtype(x)
            if inferred in ('string', 'mixed'):
                raise TypeError(f'''Could not convert {x} to numeric''')
            
            try:
                x = x.astype(np.complex128)
                if not np.any(np.imag(x)):
                    x = x.real
                else:
                    except (TypeError, ValueError):
                        x = x.astype(np.float64)
                    except ValueError:
                        err = None
                        raise TypeError(f'''Could not convert {x} to numeric'''), err
                        err = None
                        del err
            except:
                pass
            except:
                pass

    return x


def na_accum_func(values = None, accum_func = None, *, skipna):
    '''
    Cumulative function with skipna support.

    Parameters
    ----------
    values : np.ndarray or ExtensionArray
    accum_func : {np.cumprod, np.maximum.accumulate, np.cumsum, np.minimum.accumulate}
    skipna : bool

    Returns
    -------
    np.ndarray or ExtensionArray
    '''
    (mask_a, mask_b) = {
        np.minimum.accumulate: (np.inf, np.nan),
        np.cumsum: (0, np.nan),
        np.maximum.accumulate: (-(np.inf), np.nan),
        np.cumprod: (1, np.nan) }[accum_func]
# WARNING: Decompyle incomplete
