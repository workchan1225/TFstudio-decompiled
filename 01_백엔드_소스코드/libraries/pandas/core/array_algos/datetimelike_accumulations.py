# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: datetimelike_accumulations.pyc (Python 3.11)

'''
datetimelke_accumulations.py is for accumulations of datetimelike extension arrays
'''
from __future__ import annotations
from typing import TYPE_CHECKING
import numpy as np
from pandas._libs import iNaT
from pandas.core.dtypes.missing import isna
if TYPE_CHECKING:
    from collections.abc import Callable

def _cum_func(func = None, values = None, *, skipna):
    '''
    Accumulations for 1D datetimelike arrays.

    Parameters
    ----------
    func : np.cumsum, np.maximum.accumulate, np.minimum.accumulate
    values : np.ndarray
        Numpy array with the values (can be of any dtype that support the
        operation). Values is changed is modified inplace.
    skipna : bool, default True
        Whether to skip NA.
    '''
    
    try:
        fill_value = {
            np.minimum.accumulate: np.iinfo(np.int64).max,
            np.cumsum: 0,
            np.maximum.accumulate: np.iinfo(np.int64).min }[func]
    except KeyError:
        err = None
        raise ValueError(f'''No accumulation for {func} implemented on BaseMaskedArray'''), err
        err = None
        del err

    mask = isna(values)
    y = values.view('i8')
    y[mask] = fill_value
    if not skipna:
        mask = np.maximum.accumulate(mask)
    result = func(y, axis = 0)
    result[mask] = iNaT
    if values.dtype.kind in 'mM':
        return result.view(values.dtype.base)


def cumsum(values = None, *, skipna):
    return _cum_func(np.cumsum, values, skipna = skipna)


def cummin(values = None, *, skipna):
    return _cum_func(np.minimum.accumulate, values, skipna = skipna)


def cummax(values = None, *, skipna):
    return _cum_func(np.maximum.accumulate, values, skipna = skipna)
