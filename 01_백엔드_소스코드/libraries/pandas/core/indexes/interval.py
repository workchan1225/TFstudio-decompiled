# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: interval.pyc (Python 3.11)

'''define the IntervalIndex'''
from __future__ import annotations
from operator import le, lt
from typing import TYPE_CHECKING, Any, Literal, Self
import numpy as np
from pandas._libs import lib
from pandas._libs.interval import Interval, IntervalMixin, IntervalTree
from pandas._libs.tslibs import BaseOffset, Period, Timedelta, Timestamp, to_offset
from pandas.errors import InvalidIndexError
from pandas.util._decorators import cache_readonly, set_module
from pandas.util._exceptions import rewrite_exception
from pandas.core.dtypes.cast import find_common_type, infer_dtype_from_scalar, maybe_box_datetimelike, maybe_downcast_numeric, maybe_unbox_numpy_scalar, maybe_upcast_numeric_to_64bit
from pandas.core.dtypes.common import ensure_platform_int, is_float_dtype, is_integer, is_integer_dtype, is_list_like, is_number, is_object_dtype, is_scalar, is_string_dtype, pandas_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype, IntervalDtype
from pandas.core.dtypes.missing import is_valid_na_for_dtype
from pandas.core.algorithms import unique
from pandas.core.arrays.datetimelike import validate_periods
from pandas.core.arrays.interval import IntervalArray

common
from pandas.core.indexers import is_valid_positional_slice
import pandas.core.common, core
from pandas.core.indexes.base import Index, ensure_index, maybe_extract_name
from pandas.core.indexes.datetimes import DatetimeIndex, date_range
from pandas.core.indexes.extension import ExtensionIndex, inherit_names
from pandas.core.indexes.multi import MultiIndex
from pandas.core.indexes.timedeltas import TimedeltaIndex, timedelta_range
if TYPE_CHECKING:
    from collections.abc import Hashable
    from pandas._typing import Dtype, DtypeObj, IntervalClosedType, npt

def _get_next_label(label):
    dtype = getattr(label, 'dtype', type(label))
    if isinstance(label, (Timestamp, Timedelta)):
        dtype = 'datetime64[ns]'
    dtype = pandas_dtype(dtype)
    if lib.is_np_dtype(dtype, 'mM') or isinstance(dtype, DatetimeTZDtype):
        return label + np.timedelta64(1, 'ns')
    if None(dtype):
        return label + 1
    if None(dtype):
        return np.nextafter(label, np.inf)
    raise None(f'''cannot determine next label for type {type(label)!r}''')


def _get_prev_label(label):
    dtype = getattr(label, 'dtype', type(label))
    if isinstance(label, (Timestamp, Timedelta)):
        dtype = 'datetime64[ns]'
    dtype = pandas_dtype(dtype)
    if lib.is_np_dtype(dtype, 'mM') or isinstance(dtype, DatetimeTZDtype):
        return label - np.timedelta64(1, 'ns')
    if None(dtype):
        return label - 1
    if None(dtype):
        return np.nextafter(label, -(np.inf))
    raise None(f'''cannot determine next label for type {type(label)!r}''')


def _new_IntervalIndex(cls, d):
    """
    This is called upon unpickling, rather than the default which doesn't have
    arguments and breaks __new__.
    """
    pass
# WARNING: Decompyle incomplete

IntervalIndex = <NODE:12>()()()()

def _is_valid_endpoint(endpoint = inherit_names([
    '__array__',
    'overlaps',
    'contains',
    'closed_left',
    'closed_right',
    'open_left',
    'open_right',
    'is_empty'], IntervalArray)):
    '''
    Helper for interval_range to check if start/end are valid types.
    '''
    return any([
        is_number(endpoint),
        isinstance(endpoint, Timestamp),
        isinstance(endpoint, Timedelta),
        endpoint is None])


def _is_type_compatible(a = None, b = None):
