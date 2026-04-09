# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: datetimes.pyc (Python 3.11)

from __future__ import annotations
from collections import abc
from datetime import date
from functools import partial
from itertools import islice
from typing import TYPE_CHECKING, TypeAlias, TypedDict, Union, cast, overload
import warnings
import numpy as np
from pandas._libs import lib, tslib
from pandas._libs.tslibs import NaT, OutOfBoundsDatetime, Timedelta, Timestamp, astype_overflowsafe, get_supported_dtype, is_supported_dtype, timezones as libtimezones
from pandas._libs.tslibs.conversion import cast_from_unit_vectorized
from pandas._libs.tslibs.parsing import DateParseError, guess_datetime_format
from pandas._libs.tslibs.strptime import array_strptime
from pandas._typing import AnyArrayLike, ArrayLike, DateTimeErrorChoices
from pandas.util._decorators import set_module
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.common import ensure_object, is_float, is_float_dtype, is_integer, is_integer_dtype, is_list_like, is_numeric_dtype
from pandas.core.dtypes.dtypes import ArrowDtype, DatetimeTZDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCSeries
from pandas.arrays import DatetimeArray, IntegerArray, NumpyExtensionArray
from pandas.core.algorithms import unique
from pandas.core.arrays import ArrowExtensionArray
from pandas.core.arrays.base import ExtensionArray
from pandas.core.arrays.datetimes import maybe_convert_dtype, objects_to_datetime64, tz_to_dtype
from pandas.core.construction import extract_array
from pandas.core.indexes.base import Index
from pandas.core.indexes.datetimes import DatetimeIndex
if TYPE_CHECKING:
    from collections.abc import Callable, Hashable
    from pandas._libs.tslibs.nattype import NaTType
    from pandas._libs.tslibs.timedeltas import UnitChoices
    from pandas._typing import TimeUnit
    from pandas import DataFrame, Series
ArrayConvertible: 'TypeAlias' = list | tuple | AnyArrayLike
Scalar: 'TypeAlias' = float | str
DatetimeScalar: 'TypeAlias' = Scalar | date | np.datetime64
DatetimeScalarOrArrayConvertible: 'TypeAlias' = DatetimeScalar | ArrayConvertible
DatetimeDictArg: 'TypeAlias' = list[Scalar] | tuple[(Scalar, ...)] | AnyArrayLike

def YearMonthDayDict():
    '''YearMonthDayDict'''
    day: 'DatetimeDictArg' = 'YearMonthDayDict'

YearMonthDayDict = <NODE:27>(YearMonthDayDict, 'YearMonthDayDict', TypedDict, total = True)

def FulldatetimeDict():
    '''FulldatetimeDict'''
    ns: 'DatetimeDictArg' = 'FulldatetimeDict'

FulldatetimeDict = <NODE:27>(FulldatetimeDict, 'FulldatetimeDict', YearMonthDayDict, total = False)
DictConvertible = Union[(FulldatetimeDict, 'DataFrame')]
start_caching_at = 50

def _guess_datetime_format_for_array(arr = None, dayfirst = None):
    first_non_null = tslib.first_non_null(arr)
# WARNING: Decompyle incomplete


def should_cache(arg = None, unique_share = None, check_count = None):
    """
    Decides whether to do caching.

    If the percent of unique elements among `check_count` elements less
    than `unique_share * 100` then we can do caching.

    Parameters
    ----------
    arg: listlike, tuple, 1-d array, Series
    unique_share: float, default=0.7, optional
        0 < unique_share < 1
    check_count: int, optional
        0 <= check_count <= len(arg)

    Returns
    -------
    do_caching: bool

    Notes
    -----
    By default for a sequence of less than 50 items in size, we don't do
    caching; for the number of elements less than 5000, we take ten percent of
    all elements to check for a uniqueness share; if the sequence size is more
    than 5000, then we check only the first 500 elements.
    All constants were chosen empirically by.
    """
    do_caching = True
# WARNING: Decompyle incomplete


def _maybe_cache(arg = None, format = None, cache = None, convert_listlike = ('arg', 'ArrayConvertible', 'format', 'str | None', 'cache', 'bool', 'convert_listlike', 'Callable', 'return', 'Series')):
    '''
    Create a cache of unique dates from an array of dates

    Parameters
    ----------
    arg : listlike, tuple, 1-d array, Series
    format : string
        Strftime format to parse time
    cache : bool
        True attempts to create a cache of converted values
    convert_listlike : function
        Conversion function to apply on dates

    Returns
    -------
    cache_array : Series
        Cache of converted, unique dates. Can be empty
    '''
    Series = Series
    import pandas
    cache_array = Series(dtype = object)
    if cache:
        if not should_cache(arg):
            return cache_array
        if not None(arg, (np.ndarray, ExtensionArray, Index, ABCSeries)):
            arg = np.array(arg)
        unique_dates = unique(arg)
        if len(unique_dates) < len(arg):
            cache_dates = convert_listlike(unique_dates, format)
            
            try:
                cache_array = Series(cache_dates, index = unique_dates, copy = False)
            except OutOfBoundsDatetime:
                return 

            if not cache_array.index.is_unique:
                pass
    return cache_array


def _box_as_indexlike(dt_array = None, utc = None, name = None):
    '''
    Properly boxes the ndarray of datetimes to DatetimeIndex
    if it is possible or to generic Index instead

    Parameters
    ----------
    dt_array: 1-d array
        Array of datetimes to be wrapped in an Index.
    utc : bool
        Whether to convert/localize timestamps to UTC.
    name : string, default None
        Name for a resulting index

    Returns
    -------
    result : datetime of converted dates
        - DatetimeIndex if convertible to sole datetime64 type
        - general Index otherwise
    '''
    if lib.is_np_dtype(dt_array.dtype, 'M'):
        tz = 'utc' if utc else None
        return DatetimeIndex(dt_array, tz = tz, name = name)
    return None(dt_array, name = name, dtype = dt_array.dtype)


def _convert_and_box_cache(arg = None, cache_array = None, name = None):
    '''
    Convert array of dates with a cache and wrap the result in an Index.

    Parameters
    ----------
    arg : integer, float, string, datetime, list, tuple, 1-d array, Series
    cache_array : Series
        Cache of converted, unique dates
    name : string, default None
        Name for a DatetimeIndex

    Returns
    -------
    result : Index-like of converted dates
    '''
    Series = Series
    import pandas
    result = Series(arg, dtype = cache_array.index.dtype).map(cache_array)
    return _box_as_indexlike(result._values, utc = False, name = name)


def _convert_listlike_datetimes(arg, format, name, utc, unit = None, errors = None, dayfirst = None, yearfirst = (None, False, None, 'raise', None, None, True), exact = ('format', 'str | None', 'name', 'Hashable | None', 'utc', 'bool', 'unit', 'str | None', 'errors', 'DateTimeErrorChoices', 'dayfirst', 'bool | None', 'yearfirst', 'bool | None', 'exact', 'bool')):
    """
    Helper function for to_datetime. Performs the conversions of 1D listlike
    of dates

    Parameters
    ----------
    arg : list, tuple, ndarray, Series, Index
        date to be parsed
    name : object
        None or string for the Index name
    utc : bool
        Whether to convert/localize timestamps to UTC.
    unit : str
        None or string of the frequency of the passed data
    errors : str
        error handing behaviors from to_datetime, 'raise', 'coerce'
    dayfirst : bool
        dayfirst parsing behavior from to_datetime
    yearfirst : bool
        yearfirst parsing behavior from to_datetime
    exact : bool, default True
        exact format matching behavior from to_datetime

    Returns
    -------
    Index-like of parsed dates
    """
    if isinstance(arg, (list, tuple)):
        arg = np.array(arg, dtype = 'O')
    elif isinstance(arg, NumpyExtensionArray):
        arg = np.array(arg)
    arg_dtype = getattr(arg, 'dtype', None)
    tz = 'utc' if utc else None
    if isinstance(arg_dtype, DatetimeTZDtype):
        if not isinstance(arg, (DatetimeArray, DatetimeIndex)):
            return DatetimeIndex(arg, tz = tz, name = name)
        if None:
            arg = arg.tz_convert(None).tz_localize('utc')
        return arg
# WARNING: Decompyle incomplete


def _array_strptime_with_fallback(arg, name, utc = None, fmt = None, exact = None, errors = ('utc', 'bool', 'fmt', 'str', 'exact', 'bool', 'errors', 'str', 'return', 'Index')):
    """
    Call array_strptime, with fallback behavior depending on 'errors'.
    """
    (result, tz_out) = array_strptime(arg, fmt, exact = exact, errors = errors, utc = utc)
# WARNING: Decompyle incomplete


def _to_datetime_with_unit(arg, unit = None, name = None, utc = None, errors = ('utc', 'bool', 'errors', 'str', 'return', 'Index')):
