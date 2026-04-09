# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: datetimes.pyc (Python 3.11)

from __future__ import annotations
import datetime as dt
import operator
from typing import TYPE_CHECKING, Self
import warnings
import numpy as np
from pandas._libs import NaT, Period, Timestamp, index as libindex, lib
from pandas._libs.tslibs import Resolution, Tick, Timedelta, periods_per_day, timezones, to_offset
from pandas._libs.tslibs.dtypes import abbrev_to_npy_unit
from pandas._libs.tslibs.offsets import DateOffset, prefix_mapping
from pandas.errors import Pandas4Warning
from pandas.util._decorators import cache_readonly, set_module
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.common import is_scalar
from pandas.core.dtypes.dtypes import ArrowDtype, DatetimeTZDtype
from pandas.core.dtypes.generic import ABCSeries
from pandas.core.dtypes.missing import is_valid_na_for_dtype
from pandas.core.arrays.datetimes import DatetimeArray, tz_to_dtype

common
from pandas.core.indexes.base import Index, maybe_extract_name
maybe_extract_name = maybe_extract_name
import pandas.core.common, core
from pandas.core.indexes.datetimelike import DatetimeTimedeltaMixin
from pandas.core.indexes.extension import inherit_names
from pandas.core.tools.times import to_time
if TYPE_CHECKING:
    from collections.abc import Hashable
    from pandas._typing import Dtype, DtypeObj, Frequency, IntervalClosedType, TimeAmbiguous, TimeNonexistent, npt, TimeUnit
    from pandas.core.api import DataFrame, PeriodIndex
from pandas._libs.tslibs.dtypes import OFFSET_TO_PERIOD_FREQSTR

def _new_DatetimeIndex(cls, d):
    """
    This is called upon unpickling, rather than the default which doesn't
    have arguments and breaks __new__
    """
    pass
# WARNING: Decompyle incomplete

DatetimeIndex = <NODE:12>()()()()
date_range = (lambda start, end = inherit_names([
    'is_normalized'], DatetimeArray, cache = True), periods = None(inherit_names, DatetimeArray), freq = set_module('pandas'), tz = set_module('pandas'), normalize = (None, None, None, None, None, False, None, 'both'), name = {
    'unit': None }, inclusive = ('normalize', 'bool', 'name', 'Hashable | None', 'inclusive', 'IntervalClosedType', 'unit', 'TimeUnit | None', 'return', 'DatetimeIndex'), *, unit, kwargs = None, creso = None, td = None, dtarr = None,
