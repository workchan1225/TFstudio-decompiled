# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: datetimelike.pyc (Python 3.11)

'''
Base and utility classes for tseries type pandas objects.
'''
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Literal, Self, cast, final
import numpy as np
from pandas._libs import NaT, lib
from pandas._libs.tslibs import BaseOffset, Resolution, Tick, Timedelta, Timestamp, parsing, to_offset
from pandas._libs.tslibs.dtypes import abbrev_to_npy_unit
from pandas.compat.numpy import function as nv
from pandas.errors import InvalidIndexError, NullFrequencyError, OutOfBoundsDatetime, OutOfBoundsTimedelta
from pandas.util._decorators import cache_readonly
from pandas.core.dtypes.common import is_integer, is_list_like
from pandas.core.dtypes.concat import concat_compat
from pandas.core.dtypes.dtypes import CategoricalDtype, PeriodDtype
from pandas.core.arrays import DatetimeArray, ExtensionArray, PeriodArray, TimedeltaArray

common


base
from pandas.core.indexes.base import Index
import pandas.core.indexes.base, core, indexes
from pandas.core.indexes.extension import NDArrayBackedExtensionIndex
from pandas.core.indexes.range import RangeIndex
from pandas.core.tools.timedeltas import to_timedelta
if TYPE_CHECKING:
    from collections.abc import Sequence
    from datetime import datetime
    from pandas._typing import Axis, JoinHow, TimeUnit, npt
    from pandas import CategoricalIndex
_index_doc_kwargs = dict(ibase._index_doc_kwargs)

class DatetimeIndexOpsMixin(ABC, NDArrayBackedExtensionIndex):
    pass
# WARNING: Decompyle incomplete


class DatetimeTimedeltaMixin(ABC, DatetimeIndexOpsMixin):
    pass
# WARNING: Decompyle incomplete
