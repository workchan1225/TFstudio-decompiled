# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: resample.pyc (Python 3.11)

from __future__ import annotations
import copy
from typing import TYPE_CHECKING, Concatenate, Literal, Self, cast, final, no_type_check, overload
import warnings
import numpy as np
from pandas._libs import lib
from pandas._libs.tslibs import BaseOffset, IncompatibleFrequency, NaT, Period, Timedelta, Timestamp, to_offset
from pandas._typing import NDFrameT
from pandas.errors import AbstractMethodError, Pandas4Warning
from pandas.util._decorators import set_module
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.dtypes import ArrowDtype, PeriodDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCSeries

algorithms
from pandas.core.apply import ResamplerWindowApply
import pandas.core.algorithms, core
from pandas.core.arrays import ArrowExtensionArray
from pandas.core.base import PandasObject, SelectionMixin
from pandas.core.generic import NDFrame
from pandas.core.groupby.groupby import BaseGroupBy, GroupBy, get_groupby
from pandas.core.groupby.grouper import Grouper
from pandas.core.groupby.ops import BinGrouper
from pandas.core.indexes.api import MultiIndex
from pandas.core.indexes.base import Index
from pandas.core.indexes.datetimes import DatetimeIndex, date_range
from pandas.core.indexes.period import PeriodIndex, period_range
from pandas.core.indexes.timedeltas import TimedeltaIndex, timedelta_range
from pandas.core.reshape.concat import concat
from pandas.tseries.frequencies import is_subperiod, is_superperiod
from pandas.tseries.offsets import Day, Tick
if TYPE_CHECKING:
    from collections.abc import Callable, Hashable
    from pandas._typing import Any, AnyArrayLike, Axis, FreqIndexT, Frequency, IndexLabel, InterpolateOptions, P, T, TimedeltaConvertibleTypes, TimeGrouperOrigin, TimestampConvertibleTypes, TimeUnit, npt
    from pandas import DataFrame, Series
    from pandas.core.generic import NDFrame
_shared_docs_kwargs: 'dict[str, str]' = { }
Resampler = <NODE:12>()

class _GroupByMixin(SelectionMixin, PandasObject):
    _attributes: 'list[str]' = '\n    Provide the groupby facilities.\n    '
    _timegrouper: 'TimeGrouper' = None
    
    def __init__(self = None, *, parent, groupby, key, selection):
        pass
    # WARNING: Decompyle incomplete

    _apply = (lambda self, f: pass# WARNING: Decompyle incomplete
)()
    _upsample = _apply
    _downsample = _apply
    _groupby_and_aggregate = _apply
    _gotitem = (lambda self, key, ndim, subset = (None,): pass# WARNING: Decompyle incomplete
)()


class DatetimeIndexResampler(Resampler):
    pass
# WARNING: Decompyle incomplete

DatetimeIndexResamplerGroupby = <NODE:12>()

class PeriodIndexResampler(DatetimeIndexResampler):
    pass
# WARNING: Decompyle incomplete

PeriodIndexResamplerGroupby = <NODE:12>()

class TimedeltaIndexResampler(DatetimeIndexResampler):
    ax: 'TimedeltaIndex' = 'TimedeltaIndexResampler'
    _resampler_for_grouping = (lambda self: TimedeltaIndexResamplerGroupby)()
    
    def _get_binner_for_time(self):
        return self._timegrouper._get_time_delta_bins(self.ax)

    
    def _adjust_binner_for_upsample(self, binner):
        """
        Adjust our binner when upsampling.

        The range of a new index is allowed to be greater than original range
        so we don't need to change the length of a binner, GH 13022
        """
        return binner


TimedeltaIndexResamplerGroupby = <NODE:12>()

def get_resampler(obj = set_module('pandas.api.typing'), **kwds):
    '''
    Create a TimeGrouper and return our resampler.
    '''
    pass
# WARNING: Decompyle incomplete

get_resampler.__doc__ = Resampler.__doc__

def get_resampler_for_grouping(groupby, rule = None, how = set_module('pandas.api.typing'), fill_method = None, limit = (None, None, None, None), on = ('groupby', 'GroupBy', 'limit', 'int | None', 'return', 'Resampler'), **kwargs):
    '''
    Return our appropriate resampler when grouping as well.
    '''
    pass
# WARNING: Decompyle incomplete

TimeGrouper = <NODE:12>()
_take_new_index = (lambda obj = None, indexer = set_module('pandas.api.typing'), new_index = overload: pass)()
_take_new_index = (lambda obj = None, indexer = set_module('pandas.api.typing'), new_index = overload: pass)()

def _take_new_index(obj = None, indexer = None, new_index = None):
    if isinstance(obj, ABCSeries):
        new_values = algos.take_nd(obj._values, indexer)
        return obj._constructor(new_values, index = new_index, name = obj.name)
    if None(obj, ABCDataFrame):
        new_mgr = obj._mgr.reindex_indexer(new_axis = new_index, indexer = indexer, axis = 1)
        return obj._constructor_from_mgr(new_mgr, axes = new_mgr.axes)
    raise None("'obj' should be either a Series or a DataFrame")


def _get_timestamp_range_edges(first, last, freq = None, unit = None, closed = None, origin = ('left', 'start_day', None), offset = ('first', 'Timestamp', 'last', 'Timestamp', 'freq', 'BaseOffset', 'unit', 'TimeUnit', 'closed', "Literal['right', 'left']", 'origin', 'TimeGrouperOrigin', 'offset', 'Timedelta | None', 'return', 'tuple[Timestamp, Timestamp]')):
    '''
    Adjust the `first` Timestamp to the preceding Timestamp that resides on
    the provided offset. Adjust the `last` Timestamp to the following
    Timestamp that resides on the provided offset. Input Timestamps that
    already reside on the offset will be adjusted depending on the type of
    offset and the `closed` parameter.

    Parameters
    ----------
    first : pd.Timestamp
        The beginning Timestamp of the range to be adjusted.
    last : pd.Timestamp
        The ending Timestamp of the range to be adjusted.
    freq : pd.DateOffset
        The dateoffset to which the Timestamps will be adjusted.
    closed : {\'right\', \'left\'}, default "left"
        Which side of bin interval is closed.
    origin : {\'epoch\', \'start\', \'start_day\'} or Timestamp, default \'start_day\'
        The timestamp on which to adjust the grouping. The timezone of origin must
        match the timezone of the index.
        If a timestamp is not used, these values are also supported:

        - \'epoch\': `origin` is 1970-01-01
        - \'start\': `origin` is the first value of the timeseries
        - \'start_day\': `origin` is the first day at midnight of the timeseries
    offset : pd.Timedelta, default is None
        An offset timedelta added to the origin.

    Returns
    -------
    A tuple of length 2, containing the adjusted pd.Timestamp objects.
    '''
    if isinstance(freq, Tick):
        index_tz = first.tz
        if isinstance(origin, Timestamp) and (origin.tz is None) != (index_tz is None):
            raise ValueError('The origin must have the same timezone as the index.')
        if origin == 'epoch':
            origin = Timestamp('1970-01-01', tz = index_tz)
        (first, last) = _adjust_dates_anchored(first, last, freq, closed = closed, origin = origin, offset = offset, unit = unit)
    else:
        first = first.normalize()
        last = last.normalize()
        if closed == 'left':
            first = Timestamp(freq.rollback(first))
        else:
            first = Timestamp(first - freq)
        last = Timestamp(last + freq)
    return (first, last)


def _get_period_range_edges(first, last = None, freq = None, closed = None, origin = ('left', 'start_day', None), offset = ('first', 'Period', 'last', 'Period', 'freq', 'BaseOffset', 'closed', "Literal['right', 'left']", 'origin', 'TimeGrouperOrigin', 'offset', 'Timedelta | None', 'return', 'tuple[Period, Period]')):
    '''
    Adjust the provided `first` and `last` Periods to the respective Period of
    the given offset that encompasses them.

    Parameters
    ----------
    first : pd.Period
        The beginning Period of the range to be adjusted.
    last : pd.Period
        The ending Period of the range to be adjusted.
    freq : pd.DateOffset
        The freq to which the Periods will be adjusted.
    closed : {\'right\', \'left\'}, default "left"
        Which side of bin interval is closed.
    origin : {\'epoch\', \'start\', \'start_day\'}, Timestamp, default \'start_day\'
        The timestamp on which to adjust the grouping. The timezone of origin must
        match the timezone of the index.

        If a timestamp is not used, these values are also supported:

        - \'epoch\': `origin` is 1970-01-01
        - \'start\': `origin` is the first value of the timeseries
        - \'start_day\': `origin` is the first day at midnight of the timeseries
    offset : pd.Timedelta, default is None
        An offset timedelta added to the origin.

    Returns
    -------
    A tuple of length 2, containing the adjusted pd.Period objects.
    '''
    if not (lambda .0: pass# WARNING: Decompyle incomplete
)((first, last)()):
        raise TypeError("'first' and 'last' must be instances of type Period")
    first_ts = first.to_timestamp()
    last_ts = last.to_timestamp()
    adjust_first = not freq.is_on_offset(first_ts)
    adjust_last = freq.is_on_offset(last_ts)
    (first_ts, last_ts) = _get_timestamp_range_edges(first_ts, last_ts, freq, unit = 'ns', closed = closed, origin = origin, offset = offset)
    first = (first_ts + int(adjust_first) * freq).to_period(freq)
    last = (last_ts - int(adjust_last) * freq).to_period(freq)
    return (first, last)


def _insert_nat_bin(binner = None, bins = None, labels = None, nat_count = ('binner', 'PeriodIndex', 'bins', 'np.ndarray', 'labels', 'PeriodIndex', 'nat_count', 'int', 'return', 'tuple[PeriodIndex, np.ndarray, PeriodIndex]')):
    pass
# WARNING: Decompyle incomplete


def _adjust_dates_anchored(first, last, freq = None, closed = None, origin = None, offset = ('right', 'start_day', None, 'ns'), unit = ('first', 'Timestamp', 'last', 'Timestamp', 'freq', 'Tick', 'closed', "Literal['right', 'left']", 'origin', 'TimeGrouperOrigin', 'offset', 'Timedelta | None', 'unit', 'TimeUnit', 'return', 'tuple[Timestamp, Timestamp]')):
    first = first.as_unit(unit)
    last = last.as_unit(unit)
# WARNING: Decompyle incomplete


def asfreq(obj, freq = None, method = None, how = None, normalize = (None, None, False, None), fill_value = ('obj', 'NDFrameT', 'normalize', 'bool', 'return', 'NDFrameT')):
    '''
    Utility frequency conversion method for Series/DataFrame.

    See :meth:`pandas.NDFrame.asfreq` for full documentation.
    '''
    pass
# WARNING: Decompyle incomplete


def _asfreq_compat(index = None, freq = None):
    '''
    Helper to mimic asfreq on (empty) DatetimeIndex and TimedeltaIndex.

    Parameters
    ----------
    index : PeriodIndex, DatetimeIndex, or TimedeltaIndex
    freq : DateOffset

    Returns
    -------
    same type as index
    '''
    if len(index) != 0:
        raise ValueError('Can only set arbitrary freq for empty DatetimeIndex or TimedeltaIndex')
    if isinstance(index, PeriodIndex):
        new_index = index.asfreq(freq = freq)
    elif isinstance(index, DatetimeIndex):
        new_index = DatetimeIndex([], dtype = index.dtype, freq = freq, name = index.name)
    elif isinstance(index, TimedeltaIndex):
        new_index = TimedeltaIndex([], dtype = index.dtype, freq = freq, name = index.name)
    else:
        raise TypeError(type(index))
    return new_index
