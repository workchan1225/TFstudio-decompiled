# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: masked_reductions.pyc (Python 3.11)

'''
masked_reductions.py is for reduction algorithms using a mask-based approach
for missing values.
'''
from __future__ import annotations
from typing import TYPE_CHECKING
import warnings
import numpy as np
from pandas._libs import missing as libmissing
from pandas.core.nanops import check_below_min_count
if TYPE_CHECKING:
    from collections.abc import Callable
    from pandas._typing import AxisInt, npt

def _reductions(func = None, values = None, mask = None, *, skipna, min_count, axis, **kwargs):
    '''
    Sum, mean or product for 1D masked array.

    Parameters
    ----------
    func : np.sum or np.prod
    values : np.ndarray
        Numpy array with the values (can be of any dtype that support the
        operation).
    mask : np.ndarray[bool]
        Boolean numpy array (True values indicate missing values).
    skipna : bool, default True
        Whether to skip NA.
    min_count : int, default 0
        The required number of valid values to perform the operation. If fewer than
        ``min_count`` non-NA values are present the result will be NA.
    axis : int, optional, default None
    '''
    pass
# WARNING: Decompyle incomplete


def sum(values = None, mask = None, *, skipna, min_count, axis):
    return _reductions(np.sum, values = values, mask = mask, skipna = skipna, min_count = min_count, axis = axis)


def prod(values = None, mask = None, *, skipna, min_count, axis):
    return _reductions(np.prod, values = values, mask = mask, skipna = skipna, min_count = min_count, axis = axis)


def _minmax(func = None, values = None, mask = None, *, skipna, axis):
    '''
    Reduction for 1D masked array.

    Parameters
    ----------
    func : np.min or np.max
    values : np.ndarray
        Numpy array with the values (can be of any dtype that support the
        operation).
    mask : np.ndarray[bool]
        Boolean numpy array (True values indicate missing values).
    skipna : bool, default True
        Whether to skip NA.
    axis : int, optional, default None
    '''
    if not skipna:
        if not mask.any() or values.size:
            return libmissing.NA
        return func(values, axis = axis)
    subset = None[~mask]
    if subset.size:
        return func(subset, axis = axis)
    return None.NA


def min(values = None, mask = None, *, skipna, axis):
    return _minmax(np.min, values = values, mask = mask, skipna = skipna, axis = axis)


def max(values = None, mask = None, *, skipna, axis):
    return _minmax(np.max, values = values, mask = mask, skipna = skipna, axis = axis)


def mean(values = None, mask = None, *, skipna, axis):
    if values.size or mask.all():
        return libmissing.NA
    return None(np.mean, values = values, mask = mask, skipna = skipna, axis = axis)


def var(values = None, mask = None, *, skipna, axis, ddof):
    if values.size or mask.all():
        return libmissing.NA
    None.catch_warnings()
    warnings.simplefilter('ignore', RuntimeWarning)
    None(None, None)
    return 
    with None:
        if not None, _reductions(np.var, values = values, mask = mask, skipna = skipna, axis = axis, ddof = ddof):
            pass


def std(values = None, mask = None, *, skipna, axis, ddof):
    if values.size or mask.all():
        return libmissing.NA
    None.catch_warnings()
    warnings.simplefilter('ignore', RuntimeWarning)
    None(None, None)
    return 
    with None:
        if not None, _reductions(np.std, values = values, mask = mask, skipna = skipna, axis = axis, ddof = ddof):
            pass
