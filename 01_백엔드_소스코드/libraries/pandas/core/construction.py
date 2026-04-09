# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: construction.pyc (Python 3.11)

'''
Constructor functions intended to be shared by pd.array, Series.__init__,
and Index.__new__.

These should not depend on core.internals.
'''
from __future__ import annotations
from typing import TYPE_CHECKING, cast, overload
import numpy as np
from numpy import ma
from pandas._config import using_string_dtype
from pandas._libs import lib
from pandas._libs.tslibs import get_supported_dtype, is_supported_dtype
from pandas.util._decorators import set_module
from pandas.core.dtypes.base import ExtensionDtype
from pandas.core.dtypes.cast import construct_1d_arraylike_from_scalar, construct_1d_object_array_from_listlike, maybe_cast_to_datetime, maybe_cast_to_integer_array, maybe_convert_platform, maybe_promote
from pandas.core.dtypes.common import ensure_object, is_list_like, is_object_dtype, pandas_dtype
from pandas.core.dtypes.dtypes import NumpyEADtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCExtensionArray, ABCIndex, ABCSeries
from pandas.core.dtypes.missing import isna

common
if TYPE_CHECKING:
    from collections.abc import Sequence
    import pandas.core.common, core
    from pandas._typing import AnyArrayLike, ArrayLike, Dtype, DtypeObj, T
    from pandas import Index, Series
    from pandas.core.arrays import DatetimeArray, ExtensionArray, TimedeltaArray
array = (lambda data = None, dtype = None, copy = set_module('pandas'): BooleanArray = BooleanArrayDatetimeArray = DatetimeArrayExtensionArray = ExtensionArrayFloatingArray = FloatingArrayIntegerArray = IntegerArrayNumpyExtensionArray = NumpyExtensionArrayTimedeltaArray = TimedeltaArrayimport pandas.core.arraysStringDtype = StringDtypeimport pandas.core.arrays.string_if lib.is_scalar(data):
msg = f'''Cannot pass scalar \'{data}\' to \'pandas.array\'.'''raise ValueError(msg)if isinstance(data, ABCDataFrame):
raise TypeError("Cannot pass DataFrame to 'pandas.array'")# WARNING: Decompyle incomplete
)()
_typs = frozenset({
    'index',
    'series',
    'multiindex',
    'rangeindex',
    'periodindex',
    'datetimeindex',
    'intervalindex',
    'timedeltaindex',
    'categoricalindex'})
extract_array = (lambda obj = None, extract_numpy = None, extract_range = overload: pass)()
extract_array = (lambda obj = None, extract_numpy = None, extract_range = overload: pass)()

def extract_array(obj = None, extract_numpy = None, extract_range = None):
    '''
    Extract the ndarray or ExtensionArray from a Series or Index.

    For all other types, `obj` is just returned as is.

    Parameters
    ----------
    obj : object
        For Series / Index, the underlying ExtensionArray is unboxed.

    extract_numpy : bool, default False
        Whether to extract the ndarray from a NumpyExtensionArray.

    extract_range : bool, default False
        If we have a RangeIndex, return range._values if True
        (which is a materialized integer ndarray), otherwise return unchanged.

    Returns
    -------
    arr : object

    Examples
    --------
    >>> extract_array(pd.Series(["a", "b", "c"], dtype="category"))
    [\'a\', \'b\', \'c\']
    Categories (3, str): [\'a\', \'b\', \'c\']

    Other objects like lists, arrays, and DataFrames are just passed through.

    >>> extract_array([1, 2, 3])
    [1, 2, 3]

    For an ndarray-backed Series / Index the ndarray is returned.

    >>> extract_array(pd.Series([1, 2, 3]))
    array([1, 2, 3])

    To extract all the way down to the ndarray, pass ``extract_numpy=True``.

    >>> extract_array(pd.Series([1, 2, 3]), extract_numpy=True)
    array([1, 2, 3])
    '''
    typ = getattr(obj, '_typ', None)
    if typ in _typs:
        if typ == 'rangeindex':
            if extract_range:
                return obj._values
            return None
        return None._values
    if None and typ == 'npy_extension':
        return obj.to_numpy()


def ensure_wrapped_if_datetimelike(arr):
