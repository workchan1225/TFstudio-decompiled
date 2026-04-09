# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ewm.pyc (Python 3.11)

from __future__ import annotations
import datetime
from functools import partial
from typing import TYPE_CHECKING, cast
import numpy as np
from pandas._libs.tslibs import Timedelta


aggregations
from pandas.util._decorators import set_module
import pandas._libs.window.aggregations, _libs, window
from pandas.core.dtypes.common import is_datetime64_dtype, is_numeric_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype
from pandas.core.dtypes.generic import ABCSeries
from pandas.core.dtypes.missing import isna
from pandas.core import common
from pandas.core.arrays.datetimelike import dtype_to_unit
from pandas.core.indexers.objects import BaseIndexer, ExponentialMovingWindowIndexer, GroupbyIndexer
from pandas.core.util.numba_ import get_jit_arguments, maybe_use_numba
from pandas.core.window.common import zsqrt
from pandas.core.window.numba_ import generate_numba_ewm_func, generate_numba_ewm_table_func
from pandas.core.window.online import EWMMeanState, generate_online_numba_ewma_func
from pandas.core.window.rolling import BaseWindow, BaseWindowGroupby
if TYPE_CHECKING:
    from pandas._typing import TimedeltaConvertibleTypes, TimeUnit, npt
    from pandas import DataFrame, Series
    from pandas.core.generic import NDFrame

def get_center_of_mass(comass = None, span = None, halflife = None, alpha = ('comass', 'float | None', 'span', 'float | None', 'halflife', 'float | None', 'alpha', 'float | None', 'return', 'float')):
    valid_count = common.count_not_none(comass, span, halflife, alpha)
    if valid_count > 1:
        raise ValueError('comass, span, halflife, and alpha are mutually exclusive')
# WARNING: Decompyle incomplete


def _calculate_deltas(times = None, halflife = None):
    '''
    Return the diff of the times divided by the half-life. These values are used in
    the calculation of the ewm mean.

    Parameters
    ----------
    times : np.ndarray, Series
        Times corresponding to the observations. Must be monotonically increasing
        and ``datetime64[ns]`` dtype.
    halflife : float, str, timedelta, optional
        Half-life specifying the decay

    Returns
    -------
    np.ndarray
        Diff of the times divided by the half-life
    '''
    unit = dtype_to_unit(times.dtype)
    unit = cast('TimeUnit', unit)
    if isinstance(times, ABCSeries):
        times = times._values
    _times = np.asarray(times.view(np.int64), dtype = np.float64)
    _halflife = float(Timedelta(halflife).as_unit(unit)._value)
    return np.diff(_times) / _halflife

ExponentialMovingWindow = <NODE:12>()
ExponentialMovingWindowGroupby = <NODE:12>()

class OnlineExponentialMovingWindow(ExponentialMovingWindow):
    pass
# WARNING: Decompyle incomplete
