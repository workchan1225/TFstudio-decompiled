# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: datetimes.pyc (Python 3.11)

from __future__ import annotations
from datetime import datetime, timedelta, tzinfo
from typing import TYPE_CHECKING, Self, TypeVar, cast, overload
import warnings
import numpy as np
from pandas._config import using_string_dtype
from pandas._config.config import get_option
from pandas._libs import lib, tslib
from pandas._libs.tslibs import BaseOffset, NaT, NaTType, Resolution, Timestamp, astype_overflowsafe, fields, get_resolution, get_supported_dtype, get_unit_from_dtype, ints_to_pydatetime, is_date_array_normalized, is_supported_dtype, is_unitless, normalize_i8_timestamps, timezones, to_offset, tz_convert_from_utc, tzconversion
from pandas._libs.tslibs.dtypes import abbrev_to_npy_unit
from pandas.errors import PerformanceWarning
from pandas.util._decorators import set_module
from pandas.util._exceptions import find_stack_level
from pandas.util._validators import validate_inclusive
from pandas.core.dtypes.common import DT64NS_DTYPE, INT64_DTYPE, is_bool_dtype, is_float_dtype, is_string_dtype, pandas_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype, ExtensionDtype, PeriodDtype
from pandas.core.dtypes.missing import isna
from pandas.core.arrays import datetimelike as dtl
from pandas.core.arrays._ranges import generate_regular_range

common
from pandas.tseries.frequencies import get_period_alias
import pandas.core.common, core
from pandas.tseries.offsets import Day, Tick
if TYPE_CHECKING:
    from collections.abc import Callable, Generator, Iterator
    from pandas._typing import ArrayLike, DateTimeErrorChoices, DtypeObj, IntervalClosedType, TimeAmbiguous, TimeNonexistent, TimeUnit, npt
    from pandas import DataFrame, Timedelta
    from pandas.core.arrays import PeriodArray
    _TimestampNoneT1 = TypeVar('_TimestampNoneT1', Timestamp, None)
    _TimestampNoneT2 = TypeVar('_TimestampNoneT2', Timestamp, None)
_ITER_CHUNKSIZE = 10000
tz_to_dtype = (lambda tz = None, unit = None: pass)()
tz_to_dtype = (lambda tz = None, unit = None: pass)()

def tz_to_dtype(tz = None, unit = None):
    '''
    Return a datetime64[ns] dtype appropriate for the given timezone.

    Parameters
    ----------
    tz : tzinfo or None
    unit : str, default "ns"

    Returns
    -------
    np.dtype or Datetime64TZDType
    '''
    pass
# WARNING: Decompyle incomplete


def _field_accessor(name = None, field = None, docstring = None):
    pass
# WARNING: Decompyle incomplete

DatetimeArray = <NODE:12>()

def _sequence_to_dt64(data = None, *, copy, tz, dayfirst, yearfirst, ambiguous, out_unit):
    '''
    Parameters
    ----------
    data : np.ndarray or ExtensionArray
        dtl.ensure_arraylike_for_datetimelike has already been called.
    copy : bool, default False
    tz : tzinfo or None, default None
    dayfirst : bool, default False
    yearfirst : bool, default False
    ambiguous : str, bool, or arraylike, default \'raise\'
        See pandas._libs.tslibs.tzconversion.tz_localize_to_utc.
    out_unit : str or None, default None
        Desired output resolution.

    Returns
    -------
    result : numpy.ndarray
        The sequence converted to a numpy array with dtype ``datetime64[unit]``.
        Where `unit` is "ns" unless specified otherwise by `out_unit`.
    tz : tzinfo or None
        Either the user-provided tzinfo or one inferred from the data.

    Raises
    ------
    TypeError : PeriodDType data is passed
    '''
    (data, copy) = maybe_convert_dtype(data, copy, tz = tz)
    data_dtype = getattr(data, 'dtype', None)
    out_dtype = DT64NS_DTYPE
# WARNING: Decompyle incomplete


def _construct_from_dt64_naive(data = None, *, tz, copy, ambiguous):
    '''
    Convert datetime64 data to a supported dtype, localizing if necessary.
    '''
    new_dtype = data.dtype
    if not is_supported_dtype(new_dtype):
        new_dtype = get_supported_dtype(new_dtype)
        data = astype_overflowsafe(data, dtype = new_dtype, copy = False)
        copy = False
    if data.dtype.byteorder == '>':
        data = data.astype(data.dtype.newbyteorder('<'))
        new_dtype = data.dtype
        copy = False
# WARNING: Decompyle incomplete


def objects_to_datetime64(data, dayfirst, yearfirst = None, utc = None, errors = None, allow_object = (False, 'raise', False, None), out_unit = ('data', 'np.ndarray', 'utc', 'bool', 'errors', 'DateTimeErrorChoices', 'allow_object', 'bool', 'out_unit', 'str | None', 'return', 'tuple[np.ndarray, tzinfo | None]')):
    """
    Convert data to array of timestamps.

    Parameters
    ----------
    data : np.ndarray[object]
    dayfirst : bool
    yearfirst : bool
    utc : bool, default False
        Whether to convert/localize timestamps to UTC.
    errors : {'raise', 'coerce'}
    allow_object : bool
        Whether to return an object-dtype ndarray instead of raising if the
        data contains more than one timezone.
    out_unit : str or None, default None
        None indicates we should do resolution inference.

    Returns
    -------
    result : ndarray
        np.datetime64[out_unit] if returned values represent wall times or UTC
        timestamps.
        object if mixed timezones
    inferred_tz : tzinfo or None
        If not None, then the datetime64 values in `result` denote UTC timestamps.

    Raises
    ------
    ValueError : if data cannot be converted to datetimes
    TypeError  : When a type cannot be converted to datetime
    """
    pass
# WARNING: Decompyle incomplete


def maybe_convert_dtype(data = None, copy = None, tz = None):
    '''
    Convert data based on dtype conventions, issuing
    errors where appropriate.

    Parameters
    ----------
    data : np.ndarray or pd.Index
    copy : bool
    tz : tzinfo or None, default None

    Returns
    -------
    data : np.ndarray or pd.Index
    copy : bool

    Raises
    ------
    TypeError : PeriodDType data is passed
    '''
    if not hasattr(data, 'dtype'):
        return (data, copy)
    if None(data.dtype):
        data = data.astype(DT64NS_DTYPE).view('i8')
        copy = False
    elif lib.is_np_dtype(data.dtype, 'm') or is_bool_dtype(data.dtype):
        raise TypeError(f'''dtype {data.dtype} cannot be converted to datetime64[ns]''')
    if isinstance(data.dtype, PeriodDtype):
        raise TypeError('Passing PeriodDtype data is invalid. Use `data.to_timestamp()` instead')
    if not isinstance(data.dtype, ExtensionDtype) and isinstance(data.dtype, DatetimeTZDtype):
        data = np.array(data, dtype = np.object_)
        copy = False
    return (data, copy)


def _maybe_infer_tz(tz = None, inferred_tz = None):
    '''
    If a timezone is inferred from data, check that it is compatible with
    the user-provided timezone, if any.

    Parameters
    ----------
    tz : tzinfo or None
    inferred_tz : tzinfo or None

    Returns
    -------
    tz : tzinfo or None

    Raises
    ------
    TypeError : if both timezones are present but do not match
    '''
    pass
# WARNING: Decompyle incomplete


def _validate_dt64_dtype(dtype):
    '''
    Check that a dtype, if passed, represents either a numpy datetime64[ns]
    dtype or a pandas DatetimeTZDtype.

    Parameters
    ----------
    dtype : object

    Returns
    -------
    dtype : None, numpy.dtype, or DatetimeTZDtype

    Raises
    ------
    ValueError : invalid dtype

    Notes
    -----
    Unlike _validate_tz_from_dtype, this does _not_ allow non-existent
    tz errors to go through
    '''
    pass
# WARNING: Decompyle incomplete


def _validate_tz_from_dtype(dtype = None, tz = None, explicit_tz_none = None):
    '''
    If the given dtype is a DatetimeTZDtype, extract the implied
    tzinfo object from it and check that it does not conflict with the given
    tz.

    Parameters
    ----------
    dtype : dtype, str
    tz : None, tzinfo
    explicit_tz_none : bool, default False
        Whether tz=None was passed explicitly, as opposed to lib.no_default.

    Returns
    -------
    tz : consensus tzinfo

    Raises
    ------
    ValueError : on tzinfo mismatch
    '''
    pass
# WARNING: Decompyle incomplete


def _infer_tz_from_endpoints(start = None, end = None, tz = None):
    '''
    If a timezone is not explicitly given via `tz`, see if one can
    be inferred from the `start` and `end` endpoints.  If more than one
    of these inputs provides a timezone, require that they all agree.

    Parameters
    ----------
    start : Timestamp
    end : Timestamp
    tz : tzinfo or None

    Returns
    -------
    tz : tzinfo or None

    Raises
    ------
    TypeError : if start and end timezones do not agree
    '''
    
    try:
        inferred_tz = timezones.infer_tzinfo(start, end)
    except AssertionError:
        err = None
        raise TypeError('Start and end cannot both be tz-aware with different timezones'), err
        err = None
        del err

    inferred_tz = timezones.maybe_get_tz(inferred_tz)
    tz = timezones.maybe_get_tz(tz)
# WARNING: Decompyle incomplete


def _maybe_normalize_endpoints(start = None, end = None, normalize = None):
    pass
# WARNING: Decompyle incomplete


def _maybe_localize_point(ts, freq = None, tz = None, ambiguous = None, nonexistent = ('ts', 'Timestamp | None', 'return', 'Timestamp | None')):
    '''
    Localize a start or end Timestamp to the timezone of the corresponding
    start or end Timestamp

    Parameters
    ----------
    ts : start or end Timestamp to potentially localize
    freq : Tick, DateOffset, or None
    tz : str, timezone object or None
    ambiguous: str, localization behavior for ambiguous times
    nonexistent: str, localization behavior for nonexistent times

    Returns
    -------
    ts : Timestamp
    '''
    pass
# WARNING: Decompyle incomplete


def _generate_range(start = None, end = None, periods = None, offset = ('start', 'Timestamp | None', 'end', 'Timestamp | None', 'periods', 'int | None', 'offset', 'BaseOffset', 'unit', 'TimeUnit', 'return', 'Generator[Timestamp]'), *, unit):
    '''
    Generates a sequence of dates corresponding to the specified time
    offset. Similar to dateutil.rrule except uses pandas DateOffset
    objects to represent time increments.

    Parameters
    ----------
    start : Timestamp or None
    end : Timestamp or None
    periods : int or None
    offset : DateOffset
    unit : str

    Notes
    -----
    * This method is faster for generating weekdays than dateutil.rrule
    * At least two of (start, end, periods) must be specified.
    * If both start and end are specified, the returned dates will
    satisfy start <= date <= end.

    Returns
    -------
    dates : generator object
    '''
    pass
# WARNING: Decompyle incomplete
