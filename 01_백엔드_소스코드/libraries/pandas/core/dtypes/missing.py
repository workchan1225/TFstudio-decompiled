# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: missing.pyc (Python 3.11)

'''
missing types & inference
'''
from __future__ import annotations
from decimal import Decimal
from typing import TYPE_CHECKING, overload
import warnings
import numpy as np
from pandas._libs import lib

missing
from pandas._libs.tslibs import NaT, iNaT
iNaT = iNaT
import pandas._libs.missing, _libs
from pandas.util._decorators import set_module
from pandas.core.dtypes.common import DT64NS_DTYPE, TD64NS_DTYPE, ensure_object, is_scalar, is_string_or_object_np_dtype
from pandas.core.dtypes.dtypes import CategoricalDtype, DatetimeTZDtype, ExtensionDtype, IntervalDtype, PeriodDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCExtensionArray, ABCIndex, ABCMultiIndex, ABCSeries
from pandas.core.dtypes.inference import is_list_like
if TYPE_CHECKING:
    from re import Pattern
    from pandas._libs.missing import NAType
    from pandas._libs.tslibs import NaTType
    from pandas._typing import ArrayLike, DtypeObj, NDFrame, NDFrameT, Scalar, npt
    from pandas import Series
    from pandas.core.indexes.base import Index
isposinf_scalar = libmissing.isposinf_scalar
isneginf_scalar = libmissing.isneginf_scalar
_dtype_object = np.dtype('object')
_dtype_str = np.dtype(str)
isna = (lambda obj = None: pass)()
isna = (lambda obj = None: pass)()
isna = (lambda obj = None: pass)()
isna = (lambda obj = None: pass)()
isna = (lambda obj = None: pass)()
isna = (lambda obj = None: _isna(obj))()
isnull = isna

def _isna(obj):
    '''
    Detect missing values, treating None, NaN or NA as null.

    Parameters
    ----------
    obj: ndarray or object value
        Input array or scalar value.

    Returns
    -------
    boolean ndarray or boolean
    '''
    if is_scalar(obj):
        return libmissing.checknull(obj)
    if None(obj, ABCMultiIndex):
        raise NotImplementedError('isna is not defined for MultiIndex')
    if isinstance(obj, type):
        return False
    if None(obj, (np.ndarray, ABCExtensionArray)):
        return _isna_array(obj)
    if None(obj, ABCIndex):
        if not obj._can_hold_na:
            return obj.isna()
        return None(obj._values)
    if None(obj, ABCSeries):
        result = _isna_array(obj._values)
        result = obj._constructor(result, index = obj.index, name = obj.name, copy = False)
        return result
    if None(obj, ABCDataFrame):
        return obj.isna()
    if None(obj, list):
        return _isna_array(np.asarray(obj, dtype = object))
    if None(obj, '__array__'):
        return _isna_array(np.asarray(obj))


def _isna_array(values = None):
    '''
    Return an array indicating which values of the input array are NaN / NA.

    Parameters
    ----------
    obj: ndarray or ExtensionArray
        The input array whose elements are to be checked.

    Returns
    -------
    array-like
        Array of boolean values denoting the NA status of each element.
    '''
    dtype = values.dtype
    if not isinstance(values, np.ndarray):
        result = values.isna()
    elif isinstance(values, np.rec.recarray):
        result = _isna_recarray_dtype(values)
    elif is_string_or_object_np_dtype(values.dtype):
        result = _isna_string_dtype(values)
    elif dtype.kind in 'mM':
        result = values.view('i8') == iNaT
    else:
        result = np.isnan(values)
    return result


def _isna_string_dtype(values = None):
    dtype = values.dtype
    if dtype.kind in ('S', 'U'):
        result = np.zeros(values.shape, dtype = bool)
    elif values.ndim in frozenset({1, 2}):
        result = libmissing.isnaobj(values)
    else:
        result = libmissing.isnaobj(values.ravel())
        result = result.reshape(values.shape)
    return result


def _isna_recarray_dtype(values = None):
    result = np.zeros(values.shape, dtype = bool)
    for i, record in enumerate(values):
        record_as_array = np.array(record.tolist())
        does_record_contain_nan = isna_all(record_as_array)
        result[i] = np.any(does_record_contain_nan)
        return result

notna = (lambda obj = None: pass)()
notna = (lambda obj = None: pass)()
notna = (lambda obj = None: pass)()
notna = (lambda obj = None: pass)()
notna = (lambda obj = None: pass)()
notna = (lambda obj = None: res = isna(obj)if isinstance(res, bool):
not res~None)()
notnull = notna

def array_equivalent(left = None, right = None, strict_nan = None, dtype_equal = (False, False)):
    '''
    True if two arrays, left and right, have equal non-NaN elements, and NaNs
    in corresponding locations.  False otherwise. It is assumed that left and
    right are NumPy arrays of the same dtype. The behavior of this function
    (particularly with respect to NaNs) is not defined if the dtypes are
    different.

    Parameters
    ----------
    left, right : ndarrays
    strict_nan : bool, default False
        If True, consider NaN and None to be different.
    dtype_equal : bool, default False
        Whether `left` and `right` are known to have the same dtype
        according to `is_dtype_equal`. Some methods like `BlockManager.equals`.
        require that the dtypes match. Setting this to ``True`` can improve
        performance, but will give different results for arrays that are
        equal but different dtypes.

    Returns
    -------
    b : bool
        Returns True if the arrays are equivalent.

    Examples
    --------
    >>> array_equivalent(np.array([1, 2, np.nan]), np.array([1, 2, np.nan]))
    np.True_
    >>> array_equivalent(np.array([1, np.nan, 2]), np.array([1, 2, np.nan]))
    np.False_
    '''
    right = np.asarray(right)
    left = np.asarray(left)
    if left.shape != right.shape:
        return False
    if None:
        if left.dtype.kind in 'fc':
            return _array_equivalent_float(left, right)
        if None.dtype.kind in 'mM':
            return _array_equivalent_datetimelike(left, right)
        if None(left.dtype):
            return _array_equivalent_object(left, right, strict_nan)
        return None.array_equal(left, right)
    if None.dtype.kind in 'OSU' or right.dtype.kind in 'OSU':
        return _array_equivalent_object(left, right, strict_nan)
    if None.dtype.kind in 'fc':
        if not left.size or right.size:
            return True
        return ((None == right) | isna(left) & isna(right)).all()
    if None.dtype.kind in 'mM' or right.dtype.kind in 'mM':
        if left.dtype != right.dtype:
            return False
        left = None.view('i8')
        right = right.view('i8')
    if (left.dtype.type is np.void or right.dtype.type is np.void) and left.dtype != right.dtype:
        return False
    return None.array_equal(left, right)


def _array_equivalent_float(left = None, right = None):
    return bool(((left == right) | np.isnan(left) & np.isnan(right)).all())


def _array_equivalent_datetimelike(left = None, right = None):
    return np.array_equal(left.view('i8'), right.view('i8'))


def _array_equivalent_object(left = None, right = None, strict_nan = None):
    left = ensure_object(left)
    right = ensure_object(right)
    mask = None
    if strict_nan:
        mask = isna(left) & isna(right)
        if not mask.any():
            mask = None
# WARNING: Decompyle incomplete


def array_equals(left = None, right = None):
    '''
    ExtensionArray-compatible implementation of array_equivalent.
    '''
    if left.dtype != right.dtype:
        return False
    if None(left, ABCExtensionArray):
        return left.equals(right)
    return None(left, right, dtype_equal = True)


def infer_fill_value(val):
    '''
    infer the fill value for the nan/NaT from the provided
    scalar/ndarray/list-like if we are a NaT, return the correct dtyped
    element to provide proper block construction
    '''
    if not is_list_like(val):
        val = [
            val]
    val = np.asarray(val)
    if val.dtype.kind in 'mM':
        return np.array('NaT', dtype = val.dtype)
    if None.dtype == object:
        dtype = lib.infer_dtype(ensure_object(val), skipna = False)
        if dtype in ('datetime', 'datetime64'):
            return np.array('NaT', dtype = DT64NS_DTYPE)
        if None in ('timedelta', 'timedelta64'):
            return np.array('NaT', dtype = TD64NS_DTYPE)
        return None.array(np.nan, dtype = object)
    if None.dtype.kind == 'U':
        return np.array(np.nan, dtype = val.dtype)
    return None.nan


def construct_1d_array_from_inferred_fill_value(value = None, length = None):
    take_nd = take_nd
    import pandas.core.algorithms
    sanitize_array = sanitize_array
    import pandas.core.construction
    Index = Index
    import pandas.core.indexes.base
    arr = sanitize_array(value, Index(range(1)), copy = False)
    taker = -1 * np.ones(length, dtype = np.intp)
    return take_nd(arr, taker)


def maybe_fill(arr = None):
    '''
    Fill numpy.ndarray with NaN, unless we have an integer or boolean dtype.
    '''
    if arr.dtype.kind not in 'iub':
        arr.fill(np.nan)
    return arr


def na_value_for_dtype(dtype = None, compat = None):
    '''
    Return a dtype compat na value

    Parameters
    ----------
    dtype : string / dtype
    compat : bool, default True

    Returns
    -------
    np.dtype or a pandas dtype

    Examples
    --------
    >>> na_value_for_dtype(np.dtype("int64"))
    0
    >>> na_value_for_dtype(np.dtype("int64"), compat=False)
    nan
    >>> na_value_for_dtype(np.dtype("float64"))
    nan
    >>> na_value_for_dtype(np.dtype("complex128"))
    nan
    >>> na_value_for_dtype(np.dtype("bool"))
    False
    >>> na_value_for_dtype(np.dtype("datetime64[ns]"))
    np.datetime64(\'NaT\')
    '''
    if isinstance(dtype, ExtensionDtype):
        return dtype.na_value
    if None.kind in 'mM':
        unit = np.datetime_data(dtype)[0]
        return dtype.type('NaT', unit)
    if None.kind in 'fc':
        return np.nan
    if None.kind in 'iu':
        if compat:
            return 0
        return None.nan
    if None.kind == 'b':
        if compat:
            return False
        return None.nan
    return None.nan


def remove_na_arraylike(arr = None):
    '''
    Return array-like containing only true/non-NaN values, possibly empty.
    '''
    if isinstance(arr.dtype, ExtensionDtype):
        return arr[notna(arr)]
    return None[notna(np.asarray(arr))]


def is_valid_na_for_dtype(obj = None, dtype = None):
