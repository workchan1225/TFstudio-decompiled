# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: period.pyc (Python 3.11)

from __future__ import annotations
from datetime import timedelta
import operator
from typing import TYPE_CHECKING, Any, Literal, Self, TypeVar, cast, overload
import warnings
import numpy as np
from pandas._libs import algos as libalgos, lib
from pandas._libs.arrays import NDArrayBacked
from pandas._libs.tslibs import BaseOffset, Day, NaT, NaTType, Timedelta, add_overflowsafe, astype_overflowsafe, dt64arr_to_periodarr as c_dt64arr_to_periodarr, get_unit_from_dtype, iNaT, parsing, period as libperiod, to_offset
from pandas._libs.tslibs.dtypes import FreqGroup, PeriodDtypeBase
from pandas._libs.tslibs.fields import isleapyear_arr
from pandas._libs.tslibs.offsets import Tick, delta_to_tick
from pandas._libs.tslibs.period import DIFFERENT_FREQ, IncompatibleFrequency, Period, get_period_field_arr, period_asfreq_arr
from pandas.util._decorators import cache_readonly, doc, set_module
from pandas.core.dtypes.common import ensure_object, pandas_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype, PeriodDtype
from pandas.core.dtypes.generic import ABCIndex, ABCPeriodIndex, ABCSeries, ABCTimedeltaArray
from pandas.core.dtypes.missing import isna
from pandas.core.arrays import datetimelike as dtl

common
if TYPE_CHECKING:
    from collections.abc import Callable, Sequence
    Sequence = Sequence
    import pandas.core.common, core
    from pandas._typing import AnyArrayLike, Dtype, DtypeObj, FillnaOptions, NpDtype, NumpySorter, NumpyValueArrayLike, npt
    from pandas.core.dtypes.dtypes import ExtensionDtype
    from pandas.core.arrays import DatetimeArray, TimedeltaArray
    from pandas.core.arrays.base import ExtensionArray
BaseOffsetT = TypeVar('BaseOffsetT', bound = BaseOffset)
_shared_doc_kwargs = {
    'klass': 'PeriodArray' }

def _field_accessor(name = None, docstring = None):
    pass
# WARNING: Decompyle incomplete

PeriodArray = <NODE:12>()

def raise_on_incompatible(left = None, right = None):
    '''
    Helper function to render a consistent error message when raising
    IncompatibleFrequency.

    Parameters
    ----------
    left : PeriodArray
    right : None, DateOffset, Period, ndarray, or timedelta-like

    Returns
    -------
    IncompatibleFrequency
        Exception to be raised by the caller.
    '''
    pass
# WARNING: Decompyle incomplete


def period_array(data = None, freq = None, copy = None):
    '''
    Construct a new PeriodArray from a sequence of Period scalars.

    Parameters
    ----------
    data : Sequence of Period objects
        A sequence of Period objects. These are required to all have
        the same ``freq.`` Missing values can be indicated by ``None``
        or ``pandas.NaT``.
    freq : str, Tick, or Offset
        The frequency of every element of the array. This can be specified
        to avoid inferring the `freq` from `data`.
    copy : bool, default False
        Whether to ensure a copy of the data is made.

    Returns
    -------
    PeriodArray

    See Also
    --------
    PeriodArray
    pandas.PeriodIndex

    Examples
    --------
    >>> period_array([pd.Period("2017", freq="Y"), pd.Period("2018", freq="Y")])
    <PeriodArray>
    [\'2017\', \'2018\']
    Length: 2, dtype: period[Y-DEC]

    >>> period_array([pd.Period("2017", freq="Y"), pd.Period("2018", freq="Y"), pd.NaT])
    <PeriodArray>
    [\'2017\', \'2018\', \'NaT\']
    Length: 3, dtype: period[Y-DEC]

    Integers that look like years are handled

    >>> period_array([2000, 2001, 2002], freq="D")
    <PeriodArray>
    [\'2000-01-01\', \'2001-01-01\', \'2002-01-01\']
    Length: 3, dtype: period[D]

    Datetime-like strings may also be passed

    >>> period_array(["2000-Q1", "2000-Q2", "2000-Q3", "2000-Q4"], freq="Q")
    <PeriodArray>
    [\'2000Q1\', \'2000Q2\', \'2000Q3\', \'2000Q4\']
    Length: 4, dtype: period[Q-DEC]
    '''
    data_dtype = getattr(data, 'dtype', None)
    if lib.is_np_dtype(data_dtype, 'M'):
        return PeriodArray._from_datetime64(data, freq)
# WARNING: Decompyle incomplete

validate_dtype_freq = (lambda dtype = None, freq = None: pass)()
validate_dtype_freq = (lambda dtype = None, freq = None: pass)()

def validate_dtype_freq(dtype = None, freq = None):
    '''
    If both a dtype and a freq are available, ensure they match.  If only
    dtype is available, extract the implied freq.

    Parameters
    ----------
    dtype : dtype
    freq : DateOffset or None

    Returns
    -------
    freq : DateOffset

    Raises
    ------
    ValueError : non-period dtype
    IncompatibleFrequency : mismatch between dtype and freq
    '''
    pass
# WARNING: Decompyle incomplete


def dt64arr_to_periodarr(data = None, freq = None, tz = None):
    """
    Convert a datetime-like array to values Period ordinals.

    Parameters
    ----------
    data : Union[Series[datetime64[ns]], DatetimeIndex, ndarray[datetime64ns]]
    freq : Optional[Union[str, Tick]]
        Must match the `freq` on the `data` if `data` is a DatetimeIndex
        or Series.
    tz : Optional[tzinfo]

    Returns
    -------
    ordinals : ndarray[int64]
    freq : Tick
        The frequency extracted from the Series or DatetimeIndex if that's
        used.

    """
    if isinstance(data.dtype, np.dtype) or data.dtype.kind != 'M':
        raise ValueError(f'''Wrong dtype: {data.dtype}''')
# WARNING: Decompyle incomplete


def _get_ordinal_range(start = None, end = None, periods = None, freq = (1,), mult = ('mult', 'int')):
    if com.count_not_none(start, end, periods) != 2:
        raise ValueError('Of the three parameters: start, end, and periods, exactly two must be specified')
# WARNING: Decompyle incomplete


def _range_from_fields(year, month, quarter, day = None, hour = None, minute = None, second = (None, None, None, None, None, None, None, None), freq = ('return', 'tuple[np.ndarray, BaseOffset]')):
    pass
# WARNING: Decompyle incomplete


def _make_field_arrays(*fields):
    pass
# WARNING: Decompyle incomplete
