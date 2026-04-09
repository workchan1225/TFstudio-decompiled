# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: frequencies.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING
import numpy as np
from pandas._libs import lib
from pandas._libs.algos import unique_deltas
from pandas._libs.tslibs import Timestamp, get_unit_from_dtype, periods_per_day, tz_convert_from_utc
from pandas._libs.tslibs.ccalendar import DAYS, MONTH_ALIASES, MONTH_NUMBERS, MONTHS, int_to_weekday
from pandas._libs.tslibs.dtypes import OFFSET_TO_PERIOD_FREQSTR
from pandas._libs.tslibs.fields import build_field_sarray, month_position_check
from pandas._libs.tslibs.offsets import DateOffset, Day, to_offset
from pandas._libs.tslibs.parsing import get_rule_month
from pandas.util._decorators import cache_readonly, set_module
from pandas.core.dtypes.common import is_numeric_dtype
from pandas.core.dtypes.dtypes import ArrowDtype, DatetimeTZDtype, PeriodDtype
from pandas.core.dtypes.generic import ABCIndex, ABCSeries
from pandas.core.algorithms import unique
if TYPE_CHECKING:
    from pandas._typing import npt
    from pandas import DatetimeIndex, Series, TimedeltaIndex
    from pandas.core.arrays.datetimelike import DatetimeLikeArrayMixin
_need_suffix = [
    'QS',
    'BQE',
    'BQS',
    'YS',
    'BYE',
    'BYS']
for _prefix in _need_suffix:
    for _m in MONTHS:
        key = f'''{_prefix}-{_m}'''
        OFFSET_TO_PERIOD_FREQSTR[key] = OFFSET_TO_PERIOD_FREQSTR[_prefix]
        for _prefix in ('Y', 'Q'):
            for _m in MONTHS:
                _alias = f'''{_prefix}-{_m}'''
                OFFSET_TO_PERIOD_FREQSTR[_alias] = _alias
                for _d in DAYS:
                    OFFSET_TO_PERIOD_FREQSTR[f'''W-{_d}'''] = f'''W-{_d}'''
                    
                    def get_period_alias(offset_str = None):
                        '''
    Alias to closest period strings BQ->Q etc.
    '''
                        return OFFSET_TO_PERIOD_FREQSTR.get(offset_str, None)

                    infer_freq = (lambda index = None: DatetimeIndex = DatetimeIndeximport pandas.core.apiif isinstance(index, ABCSeries):
values = index._valuesif isinstance(index.dtype, ArrowDtype):
import pyarrow as paif pa.types.is_timestamp(values.dtype.pyarrow_dtype):
values = values._to_datetimearray()if not lib.is_np_dtype(values.dtype, 'mM') and isinstance(values.dtype, DatetimeTZDtype) and values.dtype == object:
raise TypeError(f'''cannot infer freq from a non-convertible dtype on a Series of {index.dtype}''')index = valuesif not hasattr(index, 'dtype'):
passelif isinstance(index.dtype, PeriodDtype):
raise TypeError('PeriodIndex given. Check the `freq` attribute instead of using infer_freq.')if lib.is_np_dtype(index.dtype, 'm'):
inferer = _TimedeltaFrequencyInferer(index)inferer.get_freq()if None(index.dtype):
raise TypeError(f'''cannot infer freq from a non-convertible index of dtype {index.dtype}''')if not isinstance(index, DatetimeIndex):
index = DatetimeIndex(index, copy = False)inferer = _FrequencyInferer(index)inferer.get_freq())()
                    
                    class _FrequencyInferer:
                        '''
    Not sure if I can avoid the state machine here
    '''
                        
                        def __init__(self = None, index = None):
                            self.index = index
                            self.i8values = index.asi8
                            if isinstance(index, ABCIndex):
                                self._creso = get_unit_from_dtype(index._data._ndarray.dtype)
                            else:
                                self._creso = get_unit_from_dtype(index._ndarray.dtype)
                        # WARNING: Decompyle incomplete

                        deltas = (lambda self = None: unique_deltas(self.i8values))()
                        deltas_asi8 = (lambda self = None: unique_deltas(self.index.asi8))()
                        is_unique = (lambda self = None: len(self.deltas) == 1)()
                        is_unique_asi8 = (lambda self = None: len(self.deltas_asi8) == 1)()
                        
                        def get_freq(self = None):
                            '''
        Find the appropriate frequency string to describe the inferred
        frequency of self.i8values

        Returns
        -------
        str or None
        '''
                            if not self.is_monotonic or self.index._is_unique:
                                return None
                            delta = None.deltas[0]
                            ppd = periods_per_day(self._creso)
                            if delta and _is_multiple(delta, ppd):
                                return self._infer_daily_rule()
                            if None.hour_deltas in ([
                                1,
                                17], [
                                1,
                                65], [
                                1,
                                17,
                                65]):
                                return 'bh'
                            if not None.is_unique_asi8:
                                return None
                            delta = None.deltas_asi8[0]
                            pph = ppd // 24
                            ppm = pph // 60
                            pps = ppm // 60
                            if _is_multiple(delta, pph):
                                return _maybe_add_count('h', delta / pph)
                            if None(delta, ppm):
                                return _maybe_add_count('min', delta / ppm)
                            if None(delta, pps):
                                return _maybe_add_count('s', delta / pps)
                            if None(delta, pps // 1000):
                                return _maybe_add_count('ms', delta / (pps // 1000))
                            if None(delta, pps // 1000000):
                                return _maybe_add_count('us', delta / (pps // 1000000))
                            return None('ns', delta)

                        day_deltas = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
                        hour_deltas = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
                        fields = (lambda self = None: build_field_sarray(self.i8values, reso = self._creso))()
                        rep_stamp = (lambda self = None: Timestamp(self.i8values[0], unit = self.index.unit))()
                        
                        def month_position_check(self = None):
                            return month_position_check(self.fields, self.index.dayofweek)

                        mdiffs = (lambda self = None: nmonths = self.fields['Y'] * 12 + self.fields['M']unique_deltas(nmonths.astype('i8')))()
                        ydiffs = (lambda self = None: unique_deltas(self.fields['Y'].astype('i8')))()
                        
                        def _infer_daily_rule(self = None):
                            annual_rule = self._get_annual_rule()
                            if annual_rule:
                                nyears = self.ydiffs[0]
                                month = MONTH_ALIASES[self.rep_stamp.month]
                                alias = f'''{annual_rule}-{month}'''
                                return _maybe_add_count(alias, nyears)
                            quarterly_rule = None._get_quarterly_rule()
                            if quarterly_rule:
                                nquarters = self.mdiffs[0] / 3
                                mod_dict = {
                                    0: 12,
                                    2: 11,
                                    1: 10 }
                                month = MONTH_ALIASES[mod_dict[self.rep_stamp.month % 3]]
                                alias = f'''{quarterly_rule}-{month}'''
                                return _maybe_add_count(alias, nquarters)
                            monthly_rule = None._get_monthly_rule()
                            if monthly_rule:
                                return _maybe_add_count(monthly_rule, self.mdiffs[0])
                            if None.is_unique:
                                return self._get_daily_rule()
                            if None._is_business_daily():
                                return 'B'
                            wom_rule = None._get_wom_rule()
                            if wom_rule:
                                return wom_rule

                        
                        def _get_daily_rule(self = None):
                            ppd = periods_per_day(self._creso)
                            days = self.deltas[0] / ppd
                            if days % 7 == 0:
                                wd = int_to_weekday[self.rep_stamp.weekday()]
                                alias = f'''W-{wd}'''
                                return _maybe_add_count(alias, days / 7)
                            return None('D', days)

                        
                        def _get_annual_rule(self = None):
                            if len(self.ydiffs) > 1:
                                return None
                            if None(unique(self.fields['M'])) > 1:
                                return None
                            pos_check = None.month_position_check()
                        # WARNING: Decompyle incomplete

                        
                        def _get_quarterly_rule(self = None):
                            if len(self.mdiffs) > 1:
                                return None
                            if not None.mdiffs[0] % 3 == 0:
                                return None
                            pos_check = None.month_position_check()
                        # WARNING: Decompyle incomplete

                        
                        def _get_monthly_rule(self = None):
                            if len(self.mdiffs) > 1:
                                return None
                            pos_check = None.month_position_check()
                        # WARNING: Decompyle incomplete

                        
                        def _is_business_daily(self = None):
                            if self.day_deltas != [
                                1,
                                3]:
                                return False
                            first_weekday = None.index[0].weekday()
                            shifts = np.diff(self.i8values)
                            ppd = periods_per_day(self._creso)
                            shifts = np.floor_divide(shifts, ppd)
                            weekdays = np.mod(first_weekday + np.cumsum(shifts), 7)
                            return bool(np.all((weekdays == 0) & (shifts == 3) | (weekdays > 0) & (weekdays <= 4) & (shifts == 1)))

                        
                        def _get_wom_rule(self = None):
                            weekdays = unique(self.index.weekday)
                            if len(weekdays) > 1:
                                return None
                            week_of_months = None((self.index.day - 1) // 7)
                            week_of_months = week_of_months[week_of_months < 4]
                            if len(week_of_months) == 0 or len(week_of_months) > 1:
                                return None
                            week = None[0] + 1
                            wd = int_to_weekday[weekdays[0]]
                            return f'''WOM-{week}{wd}'''


                    
                    class _TimedeltaFrequencyInferer(_FrequencyInferer):
                        
                        def _infer_daily_rule(self):
                            if self.is_unique:
                                return self._get_daily_rule()


                    
                    def _is_multiple(us = None, mult = None):
                        return us % mult == 0

                    
                    def _maybe_add_count(base = None, count = None):
                        pass
                    # WARNING: Decompyle incomplete

                    
                    def is_subperiod(source = None, target = None):
                        '''
    Returns True if downsampling is possible between source and target
    frequencies

    Parameters
    ----------
    source : str or DateOffset
        Frequency converting from
    target : str or DateOffset
        Frequency converting to

    Returns
    -------
    bool
    '''
                        pass
                    # WARNING: Decompyle incomplete

                    
                    def is_superperiod(source = None, target = None):
                        '''
    Returns True if upsampling is possible between source and target
    frequencies

    Parameters
    ----------
    source : str or DateOffset
        Frequency converting from
    target : str or DateOffset
        Frequency converting to

    Returns
    -------
    bool
    '''
                        pass
                    # WARNING: Decompyle incomplete

                    
                    def _maybe_coerce_freq(code = None):
                        '''we might need to coerce a code to a rule_code
    and uppercase it

    Parameters
    ----------
    source : str or DateOffset
        Frequency converting from

    Returns
    -------
    str
    '''
                        pass
                    # WARNING: Decompyle incomplete

                    
                    def _quarter_months_conform(source = None, target = None):
                        snum = MONTH_NUMBERS[source]
                        tnum = MONTH_NUMBERS[target]
                        return snum % 3 == tnum % 3

                    
                    def _is_annual(rule = None):
