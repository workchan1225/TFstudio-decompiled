# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: algorithms.pyc (Python 3.11)

'''
Generic data algorithms. This module is experimental at the moment and not
intended for public consumption
'''
from __future__ import annotations
import decimal
import operator
from typing import TYPE_CHECKING, Literal, TypeVar, cast, overload
import warnings
import numpy as np
from pandas._libs import algos, hashtable as htable, iNaT, lib
from pandas._libs.missing import NA
from pandas._typing import AnyArrayLike, ArrayLike, ArrayLikeT, AxisInt, DtypeObj, TakeIndexer, npt
from pandas.util._decorators import set_module
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.cast import construct_1d_object_array_from_listlike, np_find_common_type
from pandas.core.dtypes.common import ensure_float64, ensure_object, ensure_platform_int, is_bool_dtype, is_complex_dtype, is_dict_like, is_dtype_equal, is_extension_array_dtype, is_float, is_float_dtype, is_integer, is_integer_dtype, is_list_like, is_object_dtype, is_signed_integer_dtype, needs_i8_conversion
from pandas.core.dtypes.concat import concat_compat
from pandas.core.dtypes.dtypes import BaseMaskedDtype, CategoricalDtype, ExtensionDtype, NumpyEADtype
from pandas.core.dtypes.generic import ABCDatetimeArray, ABCExtensionArray, ABCIndex, ABCMultiIndex, ABCNumpyExtensionArray, ABCSeries, ABCTimedeltaArray
from pandas.core.dtypes.missing import isna, na_value_for_dtype
from pandas.core.array_algos.take import take_nd
from pandas.core.construction import array as pd_array, ensure_wrapped_if_datetimelike, extract_array
from pandas.core.indexers import validate_indices
if TYPE_CHECKING:
    from pandas._typing import ListLike, NumpySorter, NumpyValueArrayLike
    from pandas import Categorical, Index, Series
    from pandas.core.arrays import BaseMaskedArray, ExtensionArray
    T = TypeVar('T', bound = Index | Categorical | ExtensionArray)

def _ensure_data(values = None):
    '''
    routine to ensure that our data is of the correct
    input dtype for lower-level routines

    This will coerce:
    - ints -> int64
    - uint -> uint64
    - bool -> uint8
    - datetimelike -> i8
    - datetime64tz -> i8 (in local tz)
    - categorical -> codes

    Parameters
    ----------
    values : np.ndarray or ExtensionArray

    Returns
    -------
    np.ndarray
    '''
    if not isinstance(values, ABCMultiIndex):
        values = extract_array(values, extract_numpy = True)
    if is_object_dtype(values.dtype):
        return ensure_object(np.asarray(values))
    if None(values.dtype, BaseMaskedDtype):
        values = cast('BaseMaskedArray', values)
        if not values._hasna:
            return _ensure_data(values._data)
        return None.asarray(values)
    if None(values.dtype, CategoricalDtype):
        values = cast('Categorical', values)
        return values.codes
    if None(values.dtype):
        if isinstance(values, np.ndarray):
            return np.asarray(values).view('uint8')
        return None.asarray(values).astype('uint8', copy = False)
    if None(values.dtype):
        return np.asarray(values)
    if None(values.dtype):
        if values.dtype.itemsize in (2, 12, 16):
            return ensure_float64(values)
        return None.asarray(values)
    if None(values.dtype):
        return cast(np.ndarray, values)
    if None(values.dtype):
        npvalues = values.view('i8')
        npvalues = cast(np.ndarray, npvalues)
        return npvalues
    values = None.asarray(values, dtype = object)
    return ensure_object(values)


def _reconstruct_data(values = None, dtype = None, original = None):
    '''
    reverse of _ensure_data

    Parameters
    ----------
    values : np.ndarray or ExtensionArray
    dtype : np.dtype or ExtensionDtype
    original : AnyArrayLike

    Returns
    -------
    ExtensionArray or np.ndarray
    '''
    if isinstance(values, ABCExtensionArray) and values.dtype == dtype:
        return values
    if not None(dtype, np.dtype):
        cls = dtype.construct_array_type()
        return cls._from_sequence(values, dtype = dtype)
    return None.astype(dtype, copy = False)


def _ensure_arraylike(values = None, func_name = None):
    '''
    ensure that we are arraylike if not already
    '''
    if not isinstance(values, (ABCIndex, ABCSeries, ABCExtensionArray, np.ndarray, ABCNumpyExtensionArray)):
        if func_name != 'isin-targets':
            raise TypeError(f'''{func_name} requires a Series, Index, ExtensionArray, np.ndarray or NumpyExtensionArray got {type(values).__name__}.''')
        inferred = lib.infer_dtype(values, skipna = False)
        if inferred in ('mixed', 'string', 'mixed-integer'):
            if isinstance(values, tuple):
                values = list(values)
            values = construct_1d_object_array_from_listlike(values)
        else:
            values = np.asarray(values)
    return values

_hashtables = {
    'complex128': htable.Complex128HashTable,
    'complex64': htable.Complex64HashTable,
    'float64': htable.Float64HashTable,
    'float32': htable.Float32HashTable,
    'uint64': htable.UInt64HashTable,
    'uint32': htable.UInt32HashTable,
    'uint16': htable.UInt16HashTable,
    'uint8': htable.UInt8HashTable,
    'int64': htable.Int64HashTable,
    'int32': htable.Int32HashTable,
    'int16': htable.Int16HashTable,
    'int8': htable.Int8HashTable,
    'string': htable.StringHashTable,
    'object': htable.PyObjectHashTable }

def _get_hashtable_algo(values = None):
    '''
    Parameters
    ----------
    values : np.ndarray

    Returns
    -------
    htable : HashTable subclass
    values : ndarray
    '''
    values = _ensure_data(values)
    ndtype = _check_object_for_strings(values)
    hashtable = _hashtables[ndtype]
    return (hashtable, values)


def _check_object_for_strings(values = None):
    '''
    Check if we can use string hashtable instead of object hashtable.

    Parameters
    ----------
    values : ndarray

    Returns
    -------
    str
    '''
    ndtype = values.dtype.name
    if ndtype == 'object' and lib.is_string_array(values, skipna = False):
        ndtype = 'string'
    return ndtype

unique = (lambda values = None: pass)()
unique = (lambda values = None: pass)()
unique = (lambda values: unique_with_mask(values))()

def nunique_ints(values = None):
    '''
    Return the number of unique values for integer array-likes.

    Significantly faster than pandas.unique for long enough sequences.
    No checks are done to ensure input is integral.

    Parameters
    ----------
    values : 1d array-like

    Returns
    -------
    int : The number of unique values in ``values``
    '''
    if len(values) == 0:
        return 0
    values = None(values)
    result = (np.bincount(values.ravel().astype('intp')) != 0).sum()
    return result


def unique_with_mask(values = None, mask = None):
    '''See algorithms.unique for docs. Takes a mask for masked arrays.'''
    values = _ensure_arraylike(values, func_name = 'unique')
    if isinstance(values.dtype, ExtensionDtype):
        return values.unique()
    if None(values, ABCIndex):
        return values.unique()
    original = None
    (hashtable, values) = _get_hashtable_algo(values)
    table = hashtable(len(values))
# WARNING: Decompyle incomplete

unique1d = unique
_MINIMUM_COMP_ARR_LEN = 1000000

def isin(comps = None, values = None):
    '''
    Compute the isin boolean array.

    Parameters
    ----------
    comps : list-like
    values : list-like

    Returns
    -------
    ndarray[bool]
        Same length as `comps`.
    '''
    if not is_list_like(comps):
        raise TypeError(f'''only list-like objects are allowed to be passed to isin(), you passed a `{type(comps).__name__}`''')
    if not is_list_like(values):
        raise TypeError(f'''only list-like objects are allowed to be passed to isin(), you passed a `{type(values).__name__}`''')
    if not isinstance(values, (ABCIndex, ABCSeries, ABCExtensionArray, np.ndarray)):
        orig_values = list(values)
        values = _ensure_arraylike(orig_values, func_name = 'isin-targets')
        if not len(values) > 0 and values.dtype.kind in 'iufcb' and is_signed_integer_dtype(comps) and is_dtype_equal(values, comps):
            values = construct_1d_object_array_from_listlike(orig_values)
        elif isinstance(values, ABCMultiIndex):
            values = np.array(values)
        else:
            values = extract_array(values, extract_numpy = True, extract_range = True)
    comps_array = _ensure_arraylike(comps, func_name = 'isin')
    comps_array = extract_array(comps_array, extract_numpy = True)
    if not isinstance(comps_array, np.ndarray):
        return comps_array.isin(values)
    if None(comps_array.dtype):
        return pd_array(comps_array).isin(values)
    if not None(values.dtype) and is_object_dtype(comps_array.dtype):
        return np.zeros(comps_array.shape, dtype = bool)
    if None(values.dtype):
        return isin(comps_array, values.astype(object))
    if None(values.dtype, ExtensionDtype):
        return isin(np.asarray(comps_array), np.asarray(values))
    return f(comps_array, values)


def factorize_array(values = None, use_na_sentinel = None, size_hint = None, na_value = (True, None, None, None), mask = ('values', 'np.ndarray', 'use_na_sentinel', 'bool', 'size_hint', 'int | None', 'na_value', 'object', 'mask', 'npt.NDArray[np.bool_] | None', 'return', 'tuple[npt.NDArray[np.intp], np.ndarray]')):
