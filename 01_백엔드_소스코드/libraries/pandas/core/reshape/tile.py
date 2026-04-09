# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tile.pyc (Python 3.11)

'''
Quantilization functions and related stuff
'''
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Literal, cast
import numpy as np
from pandas._libs import Timedelta, Timestamp, lib
from pandas.util._decorators import set_module
from pandas.core.dtypes.common import ensure_platform_int, is_bool_dtype, is_integer, is_list_like, is_numeric_dtype, is_scalar
from pandas.core.dtypes.dtypes import CategoricalDtype, DatetimeTZDtype, ExtensionDtype
from pandas.core.dtypes.generic import ABCSeries
from pandas.core.dtypes.missing import isna
from pandas import Categorical, Index, IntervalIndex

algorithms
from pandas.core.arrays.datetimelike import dtype_to_unit
import pandas.core.algorithms, core
from pandas.core.col import Expression
if TYPE_CHECKING:
    from collections.abc import Callable
    from pandas._typing import DtypeObj, IntervalLeftRight, TimeUnit
cut = (lambda x, bins, right, labels, retbins = None, precision = None, include_lowest = set_module('pandas'), duplicates = (True, None, False, 3, False, 'raise', True), ordered = ('right', 'bool', 'retbins', 'bool', 'precision', 'int', 'include_lowest', 'bool', 'duplicates', 'str', 'ordered', 'bool'): original = xx_idx = _preprocess_for_cut(x)(x_idx, _) = _coerce_to_type(x_idx)if not np.iterable(bins):
bins = _nbins_to_bins(x_idx, bins, right)elif isinstance(bins, IntervalIndex):
if bins.is_overlapping:
raise ValueError('Overlapping IntervalIndex is not accepted.')else:
bins = Index(bins)if not bins.is_monotonic_increasing:
raise ValueError('bins must increase monotonically.')(fac, bins) = _bins_to_cuts(x_idx, bins, right = right, labels = labels, precision = precision, include_lowest = include_lowest, duplicates = duplicates, ordered = ordered)_postprocess_for_cut(fac, bins, retbins, original))()
qcut = (lambda x, q = None, labels = None, retbins = set_module('pandas'), precision = (None, False, 3, 'raise'), duplicates = ('retbins', 'bool', 'precision', 'int', 'duplicates', 'str'): if isinstance(x, Expression):
x._call_with_func(qcut, x = x, q = q, labels = labels, retbins = retbins, precision = precision)original = Nonex_idx = _preprocess_for_cut(x)(x_idx, _) = _coerce_to_type(x_idx)if is_integer(q):
quantiles = np.linspace(0, 1, q + 1)np.putmask(quantiles, q * quantiles != np.arange(q + 1), np.nextafter(quantiles, 1))else:
quantiles = qbins = x_idx.to_series().dropna().quantile(quantiles)(fac, bins) = _bins_to_cuts(x_idx, Index(bins), labels = labels, precision = precision, include_lowest = True, duplicates = duplicates)_postprocess_for_cut(fac, bins, retbins, original))()

def _nbins_to_bins(x_idx = None, nbins = None, right = None):
    '''
    If a user passed an integer N for bins, convert this to a sequence of N
    equal(ish)-sized bins.
    '''
    if is_scalar(nbins) and nbins < 1:
        raise ValueError('`bins` should be a positive integer.')
    if x_idx.size == 0:
        raise ValueError('Cannot cut empty array')
    rng = (x_idx.min(), x_idx.max())
    (mn, mx) = rng
    if is_numeric_dtype(x_idx.dtype):
        if np.isinf(mn) or np.isinf(mx):
            raise ValueError('cannot specify integer `bins` when input data contains infinity')
    if mn == mx:
        if _is_dt_or_td(x_idx.dtype):
            unit = dtype_to_unit(x_idx.dtype)
            td = Timedelta(seconds = 1).as_unit(cast('TimeUnit', unit))
            bins = x_idx._values._generate_range(start = mn - td, end = mx + td, periods = nbins + 1, freq = None, unit = unit)
        elif mn != 0:
            pass
        
        0.001 * abs(mn) -= 0.001
        mx += 0.001 * abs(mx) if mx != 0 else 0.001
        bins = np.linspace(mn, mx, nbins + 1, endpoint = True)
    elif _is_dt_or_td(x_idx.dtype):
        unit = dtype_to_unit(x_idx.dtype)
        bins = x_idx._values._generate_range(start = mn, end = mx, periods = nbins + 1, freq = None, unit = unit)
    else:
        bins = np.linspace(mn, mx, nbins + 1, endpoint = True)
    adj = (mx - mn) * 0.001
    return Index(bins, copy = False)


def _bins_to_cuts(x_idx, bins, right, labels = None, precision = None, include_lowest = None, duplicates = (True, None, 3, False, 'raise', True), ordered = ('x_idx', 'Index', 'bins', 'Index', 'right', 'bool', 'precision', 'int', 'include_lowest', 'bool', 'duplicates', 'str', 'ordered', 'bool')):
    pass
# WARNING: Decompyle incomplete


def _coerce_to_type(x = None):
    '''
    if the passed data is of datetime/timedelta, bool or nullable int type,
    this method converts it to numeric so that cut or qcut method can
    handle it
    '''
    dtype = None
    if _is_dt_or_td(x.dtype):
        dtype = x.dtype
    elif is_bool_dtype(x.dtype):
        x = x.astype(np.int64)
    elif isinstance(x.dtype, ExtensionDtype) and is_numeric_dtype(x.dtype):
        x_arr = x.to_numpy(dtype = np.float64, na_value = np.nan)
        x = Index(x_arr, copy = False)
    return (Index(x), dtype)


def _is_dt_or_td(dtype = None):
