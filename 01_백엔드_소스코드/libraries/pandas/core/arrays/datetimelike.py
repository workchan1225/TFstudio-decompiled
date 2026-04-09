# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: datetimelike.pyc (Python 3.11)

from __future__ import annotations
from datetime import datetime, timedelta
from functools import wraps
import operator
from typing import TYPE_CHECKING, Any, Literal, Self, TypeAlias, Union, cast, final, overload
import warnings
import numpy as np
from pandas._config import using_string_dtype
from pandas._config.config import get_option
from pandas._libs import algos, lib
from pandas._libs.tslibs import BaseOffset, Day, IncompatibleFrequency, NaT, NaTType, Period, Resolution, Tick, Timedelta, Timestamp, add_overflowsafe, astype_overflowsafe, get_unit_from_dtype, iNaT, ints_to_pydatetime, ints_to_pytimedelta, periods_per_day, timezones, to_offset
from pandas._libs.tslibs.fields import RoundTo, round_nsint64
from pandas._libs.tslibs.np_datetime import compare_mismatched_resolutions
from pandas._libs.tslibs.timedeltas import get_unit_for_round
from pandas._libs.tslibs.timestamps import integer_op_not_supported
from pandas._typing import ArrayLike, AxisInt, DatetimeLikeScalar, Dtype, DtypeObj, F, InterpolateOptions, NpDtype, PositionalIndexer2D, PositionalIndexerTuple, ScalarIndexer, SequenceIndexer, TakeIndexer, TimeAmbiguous, TimeNonexistent, npt
from pandas.compat.numpy import function as nv
from pandas.errors import AbstractMethodError, InvalidComparison, PerformanceWarning
from pandas.util._decorators import cache_readonly
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.cast import construct_1d_object_array_from_listlike
from pandas.core.dtypes.common import is_all_strings, is_integer_dtype, is_list_like, is_object_dtype, is_string_dtype, pandas_dtype
from pandas.core.dtypes.dtypes import ArrowDtype, CategoricalDtype, DatetimeTZDtype, ExtensionDtype, PeriodDtype
from pandas.core.dtypes.generic import ABCCategorical, ABCMultiIndex
from pandas.core.dtypes.missing import is_valid_na_for_dtype, isna
from pandas.core import algorithms, missing, nanops, ops
from pandas.core.algorithms import isin, map_array, unique1d
from pandas.core.array_algos import datetimelike_accumulations
from pandas.core.arraylike import OpsMixin
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray, ravel_compat
from pandas.core.arrays.arrow.array import ArrowExtensionArray
from pandas.core.arrays.base import ExtensionArray
from pandas.core.arrays.integer import IntegerArray

common
from pandas.core.construction import array, ensure_wrapped_if_datetimelike, extract_array
ensure_wrapped_if_datetimelike = ensure_wrapped_if_datetimelike
extract_array = extract_array
import pandas.core.common, core
from pandas.core.indexers import check_array_indexer, check_setitem_lengths
from pandas.core.ops.common import unpack_zerodim_and_defer
from pandas.core.ops.invalid import invalid_comparison, make_invalid_op
from pandas.tseries import frequencies
if TYPE_CHECKING:
    from collections.abc import Callable, Iterator, Sequence
    from pandas._typing import TimeUnit
    from pandas import Index
    from pandas.core.arrays import DatetimeArray, PeriodArray, TimedeltaArray
DTScalarOrNaT: 'TypeAlias' = DatetimeLikeScalar | NaTType

def _make_unpacked_invalid_op(op_name = None):
    op = make_invalid_op(op_name)
    return unpack_zerodim_and_defer(op_name)(op)


def _period_dispatch(meth = None):
    '''
    For PeriodArray methods, dispatch to DatetimeArray and re-wrap the results
    in PeriodArray.  We cannot use ._ndarray directly for the affected
    methods because the i8 data has different semantics on NaT values.
    '''
    pass
# WARNING: Decompyle incomplete


class DatetimeLikeArrayMixin(NDArrayBackedExtensionArray, OpsMixin):
    pass
# WARNING: Decompyle incomplete


class DatelikeOps(DatetimeLikeArrayMixin):
    '''
    Common ops for DatetimeIndex/PeriodIndex, but not TimedeltaIndex.
    '''
    
    def strftime(self = None, date_format = None):
        '''
        Convert to Index using specified date_format.

        Return an Index of formatted strings specified by date_format, which
        supports the same string format as the python standard library. Details
        of the string format can be found in `python string format
        doc <https://docs.python.org/3/library/datetime.html
        #strftime-and-strptime-behavior>`__.

        Formats supported by the C `strftime` API but not by the python string format
        doc (such as `"%R"`, `"%r"`) are not officially supported and should be
        preferably replaced with their supported equivalents (such as `"%H:%M"`,
        `"%I:%M:%S %p"`).

        Note that `PeriodIndex` support additional directives, detailed in
        `Period.strftime`.

        Parameters
        ----------
        date_format : str
            Date format string (e.g. "%%Y-%%m-%%d").

        Returns
        -------
        ndarray[object]
            NumPy ndarray of formatted strings.

        See Also
        --------
        to_datetime : Convert the given argument to datetime.
        DatetimeIndex.normalize : Return DatetimeIndex with times to midnight.
        DatetimeIndex.round : Round the DatetimeIndex to the specified freq.
        DatetimeIndex.floor : Floor the DatetimeIndex to the specified freq.
        Timestamp.strftime : Format a single Timestamp.
        Period.strftime : Format a single Period.

        Examples
        --------
        >>> rng = pd.date_range(pd.Timestamp("2018-03-10 09:00"), periods=3, freq="s")
        >>> rng.strftime("%B %d, %Y, %r")
        Index([\'March 10, 2018, 09:00:00 AM\', \'March 10, 2018, 09:00:01 AM\',
               \'March 10, 2018, 09:00:02 AM\'],
              dtype=\'str\')
        '''
        result = self._format_native_types(date_format = date_format, na_rep = np.nan)
        if using_string_dtype():
            StringDtype = StringDtype
            import pandas
            return pd_array(result, dtype = StringDtype(na_value = np.nan))
        return None.astype(object, copy = False)



class TimelikeOps(DatetimeLikeArrayMixin):
    pass
# WARNING: Decompyle incomplete


def ensure_arraylike_for_datetimelike(data = None, copy = None, cls_name = None):
    if not hasattr(data, 'dtype'):
        if isinstance(data, (list, tuple)) and np.ndim(data) == 0:
            data = list(data)
        data = construct_1d_object_array_from_listlike(data)
        copy = False
    elif isinstance(data, ABCMultiIndex):
        raise TypeError(f'''Cannot create a {cls_name} from a MultiIndex.''')
    data = extract_array(data, extract_numpy = True)
    if (isinstance(data, IntegerArray) or isinstance(data, ArrowExtensionArray)) and data.dtype.kind in 'iu':
        data = data.to_numpy('int64', na_value = iNaT)
        copy = False
    elif isinstance(data, ArrowExtensionArray):
        data = data._maybe_convert_datelike_array()
        data = data.to_numpy()
        copy = False
    elif not isinstance(data, (np.ndarray, ExtensionArray)):
        data = np.asarray(data)
    elif isinstance(data, ABCCategorical):
        data = data.categories.take(data.codes, fill_value = NaT)._values
        copy = False
    return (data, copy)

validate_periods = (lambda periods = None: pass)()
validate_periods = (lambda periods = None: pass)()

def validate_periods(periods = None):
    '''
    If a `periods` argument is passed to the Datetime/Timedelta Array/Index
    constructor, cast it to an integer.

    Parameters
    ----------
    periods : None, int

    Returns
    -------
    periods : None or int

    Raises
    ------
    TypeError
        if periods is not None or int
    '''
    pass
# WARNING: Decompyle incomplete


def _validate_inferred_freq(freq = None, inferred_freq = None):
    '''
    If the user passes a freq and another freq is inferred from passed data,
    require that they match.

    Parameters
    ----------
    freq : DateOffset or None
    inferred_freq : DateOffset or None

    Returns
    -------
    freq : DateOffset or None
    '''
    pass
# WARNING: Decompyle incomplete


def dtype_to_unit(dtype = None):
    """
    Return the unit str corresponding to the dtype's resolution.

    Parameters
    ----------
    dtype : DatetimeTZDtype or np.dtype
        If np.dtype, we assume it is a datetime64 dtype.

    Returns
    -------
    str
    """
    if isinstance(dtype, DatetimeTZDtype):
        return dtype.unit
    if None(dtype, ArrowDtype):
        if dtype.kind not in 'mM':
            raise ValueError(f'''dtype={dtype!r} does not have a resolution.''')
        return dtype.pyarrow_dtype.unit
    return None.datetime_data(dtype)[0]
