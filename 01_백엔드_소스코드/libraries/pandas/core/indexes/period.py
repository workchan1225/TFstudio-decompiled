# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: period.pyc (Python 3.11)

from __future__ import annotations
from datetime import datetime, timedelta
from typing import TYPE_CHECKING, Self
import numpy as np
from pandas._libs import index as libindex
from pandas._libs.tslibs import BaseOffset, Day, NaT, Period, Resolution, Tick
from pandas._libs.tslibs.dtypes import OFFSET_TO_PERIOD_FREQSTR
from pandas.util._decorators import cache_readonly, doc, set_module
from pandas.core.dtypes.common import is_integer
from pandas.core.dtypes.dtypes import PeriodDtype
from pandas.core.dtypes.generic import ABCSeries
from pandas.core.dtypes.missing import is_valid_na_for_dtype
from pandas.core.arrays.period import PeriodArray, period_array, raise_on_incompatible, validate_dtype_freq

common


base
from pandas.core.indexes.base import maybe_extract_name
import pandas.core.indexes.base, core, indexes
from pandas.core.indexes.datetimelike import DatetimeIndexOpsMixin
from pandas.core.indexes.datetimes import DatetimeIndex, Index
from pandas.core.indexes.extension import inherit_names
if TYPE_CHECKING:
    from collections.abc import Hashable
    from pandas._typing import Dtype, DtypeObj, npt
_index_doc_kwargs = dict(ibase._index_doc_kwargs)
_index_doc_kwargs.update({
    'target_klass': 'PeriodIndex or list of Periods' })
_shared_doc_kwargs = {
    'klass': 'PeriodArray' }

def _new_PeriodIndex(cls, **d):
    values = d.pop('data')
# WARNING: Decompyle incomplete

PeriodIndex = <NODE:12>()()()
period_range = (lambda start = inherit_names([
    'is_leap_year'], PeriodArray), end = set_module('pandas'), periods = set_module('pandas'), freq = (None, None, None, None, None), name = ('periods', 'int | None', 'name', 'Hashable | None', 'return', 'PeriodIndex'): if com.count_not_none(start, end, periods) != 2:
raise ValueError('Of the three parameters: start, end, and periods, exactly two must be specified')# WARNING: Decompyle incomplete
)()
