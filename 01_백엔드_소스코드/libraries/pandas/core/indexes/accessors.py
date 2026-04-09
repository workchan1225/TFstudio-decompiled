# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: accessors.pyc (Python 3.11)

'''
datetimelike delegation
'''
from __future__ import annotations
from typing import TYPE_CHECKING, NoReturn, cast
import warnings
import numpy as np
from pandas._libs import lib
from pandas.errors import Pandas4Warning
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.common import is_integer_dtype, is_list_like
from pandas.core.dtypes.dtypes import ArrowDtype, CategoricalDtype, DatetimeTZDtype, PeriodDtype
from pandas.core.dtypes.generic import ABCSeries
from pandas.core.accessor import PandasDelegate, delegate_names
from pandas.core.arrays import DatetimeArray, PeriodArray, TimedeltaArray
from pandas.core.arrays.arrow.array import ArrowExtensionArray
from pandas.core.base import NoNewAttributesMixin, PandasObject
from pandas.core.indexes.datetimes import DatetimeIndex
from pandas.core.indexes.timedeltas import TimedeltaIndex
if TYPE_CHECKING:
    from pandas import DataFrame, Series

class Properties(NoNewAttributesMixin, PandasObject, PandasDelegate):
    _hidden_attrs = PandasObject._hidden_attrs | {
        'orig',
        'name'}
    
    def __init__(self = None, data = None, orig = None):
        if not isinstance(data, ABCSeries):
            raise TypeError(f'''cannot convert an object of type {type(data)} to a datetimelike index''')
        self._parent = data
        self.orig = orig
        self.name = getattr(data, 'name', None)
        self._freeze()

    
    def _get_values(self):
        data = self._parent
        if lib.is_np_dtype(data.dtype, 'M'):
            return DatetimeIndex(data, copy = False, name = self.name)
        if None(data.dtype, DatetimeTZDtype):
            return DatetimeIndex(data, copy = False, name = self.name)
        if None.is_np_dtype(data.dtype, 'm'):
            return TimedeltaIndex(data, copy = False, name = self.name)
        if None(data.dtype, PeriodDtype):
            return PeriodArray(data, copy = False)
        raise None(f'''cannot convert an object of type {type(data)} to a datetimelike index''')

    
    def _delegate_property_get(self = None, name = None):
        Series = Series
        import pandas
        values = self._get_values()
        result = getattr(values, name)
        if isinstance(result, np.ndarray):
            if is_integer_dtype(result):
                result = result.astype('int64')
            elif not is_list_like(result):
                return result
        result = np.asarray(result)
    # WARNING: Decompyle incomplete

    
    def _delegate_property_set(self = None, name = None, value = None, *args, **kwargs):
        raise ValueError('modifications to a property of a datetimelike object are not supported. Change values on the original.')

    
    def _delegate_method(self = None, name = None, *args, **kwargs):
        Series = Series
        import pandas
        values = self._get_values()
        method = getattr(values, name)
    # WARNING: Decompyle incomplete


ArrowTemporalProperties = <NODE:12>()()()()
DatetimeProperties = <NODE:12>()()
TimedeltaProperties = <NODE:12>()()
PeriodProperties = <NODE:12>()()

class CombinedDatetimelikeProperties(PeriodProperties, TimedeltaProperties, DatetimeProperties):
    '''
    Accessor object for Series values\' datetime-like, timedelta and period properties.

    See Also
    --------
    DatetimeIndex : Index of datetime64 data.

    Examples
    --------
    >>> dates = pd.Series(
    ...     ["2024-01-01", "2024-01-15", "2024-02-5"], dtype="datetime64[ns]"
    ... )
    >>> dates.dt.day
    0     1
    1    15
    2     5
    dtype: int32
    >>> dates.dt.month
    0    1
    1    1
    2    2
    dtype: int32

    >>> dates = pd.Series(
    ...     ["2024-01-01", "2024-01-15", "2024-02-5"], dtype="datetime64[ns, UTC]"
    ... )
    >>> dates.dt.day
    0     1
    1    15
    2     5
    dtype: int32
    >>> dates.dt.month
    0    1
    1    1
    2    2
    dtype: int32
    '''
    
    def __new__(cls = None, data = None):
        if not isinstance(data, ABCSeries):
            raise TypeError(f'''cannot convert an object of type {type(data)} to a datetimelike index''')
        orig = data if isinstance(data.dtype, CategoricalDtype) else None
    # WARNING: Decompyle incomplete
