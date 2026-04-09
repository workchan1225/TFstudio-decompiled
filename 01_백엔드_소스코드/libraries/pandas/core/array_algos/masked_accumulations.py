# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: masked_accumulations.pyc (Python 3.11)

'''
masked_accumulations.py is for accumulation algorithms using a mask-based approach
for missing values.
'''
from __future__ import annotations
from typing import TYPE_CHECKING
import numpy as np
if TYPE_CHECKING:
    from collections.abc import Callable
    from pandas._typing import npt

def _cum_func(func = None, values = None, mask = None, *, skipna):
    '''
    Accumulations for 1D masked array.

    We will modify values in place to replace NAs with the appropriate fill value.

    Parameters
    ----------
    func : np.cumsum, np.cumprod, np.maximum.accumulate, np.minimum.accumulate
    values : np.ndarray
        Numpy array with the values (can be of any dtype that support the
        operation).
    mask : np.ndarray
        Boolean numpy array (True values indicate missing values).
    skipna : bool, default True
        Whether to skip NA.
    '''
    if values.dtype.kind == 'f':
        dtype_info = np.finfo(values.dtype.type)
    elif values.dtype.kind in 'iu':
        dtype_info = np.iinfo(values.dtype.type)
    elif values.dtype.kind == 'b':
        dtype_info = np.iinfo(np.uint8)
    else:
        raise NotImplementedError(f'''No masked accumulation defined for dtype {values.dtype.type}''')
    
    try:
        fill_value = {
            np.minimum.accumulate: dtype_info.max,
            np.cumsum: 0,
            np.maximum.accumulate: dtype_info.min,
            np.cumprod: 1 }[func]
    except KeyError:
        err = None
        raise NotImplementedError(f'''No accumulation for {func} implemented on BaseMaskedArray'''), err
        err = None
        del err

    values[mask] = fill_value
    if not skipna:
        mask = np.maximum.accumulate(mask)
    values = func(values)
    return (values, mask)


def cumsum(values = None, mask = None, *, skipna):
    return _cum_func(np.cumsum, values, mask, skipna = skipna)


def cumprod(values = None, mask = None, *, skipna):
    return _cum_func(np.cumprod, values, mask, skipna = skipna)


def cummin(values = None, mask = None, *, skipna):
    return _cum_func(np.minimum.accumulate, values, mask, skipna = skipna)


def cummax(values = None, mask = None, *, skipna):
    return _cum_func(np.maximum.accumulate, values, mask, skipna = skipna)
