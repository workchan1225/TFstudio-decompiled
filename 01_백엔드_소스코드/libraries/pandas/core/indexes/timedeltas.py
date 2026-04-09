# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: timedeltas.pyc (Python 3.11)

'''implement the TimedeltaIndex'''
from __future__ import annotations
from typing import TYPE_CHECKING, cast
from pandas._libs import index as libindex, lib
from pandas._libs.tslibs import Resolution, Timedelta, to_offset
from pandas._libs.tslibs.dtypes import abbrev_to_npy_unit
from pandas.util._decorators import set_module
from pandas.core.dtypes.common import is_scalar, pandas_dtype
from pandas.core.dtypes.dtypes import ArrowDtype
from pandas.core.dtypes.generic import ABCSeries
from pandas.core.arrays.timedeltas import TimedeltaArray

common
from pandas.core.indexes.base import Index, maybe_extract_name
maybe_extract_name = maybe_extract_name
import pandas.core.common, core
from pandas.core.indexes.datetimelike import DatetimeTimedeltaMixin
from pandas.core.indexes.extension import inherit_names
if TYPE_CHECKING:
    from pandas._libs import NaTType
    from pandas._libs.tslibs import Day, Tick
    from pandas._typing import DtypeObj, TimeUnit
TimedeltaIndex = <NODE:12>()()()
timedelta_range = (lambda start = None(inherit_names, TimedeltaArray, wrap = True), end = inherit_names([
    'components',
    'to_pytimedelta',
    'sum',
    'std',
    'median'], TimedeltaArray), periods = set_module('pandas'), freq = set_module('pandas'), name = (None, None, None, None, None, None), closed = {
    'unit': None }, *, unit, creso = None, tdarr = None,
