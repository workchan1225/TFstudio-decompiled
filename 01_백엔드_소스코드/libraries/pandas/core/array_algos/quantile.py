# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: quantile.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING
import numpy as np
from pandas.core.dtypes.missing import isna, na_value_for_dtype
if TYPE_CHECKING:
    from pandas._typing import ArrayLike, Scalar, npt

def quantile_compat(values = None, qs = None, interpolation = None):
    '''
    Compute the quantiles of the given values for each quantile in `qs`.

    Parameters
    ----------
    values : np.ndarray or ExtensionArray
    qs : np.ndarray[float64]
    interpolation : str

    Returns
    -------
    np.ndarray or ExtensionArray
    '''
    if isinstance(values, np.ndarray):
        fill_value = na_value_for_dtype(values.dtype, compat = False)
        mask = isna(values)
        return quantile_with_mask(values, mask, fill_value, qs, interpolation)
    return None._quantile(qs, interpolation)


def quantile_with_mask(values, mask = None, fill_value = None, qs = None, interpolation = ('values', 'np.ndarray', 'mask', 'npt.NDArray[np.bool_]', 'qs', 'npt.NDArray[np.float64]', 'interpolation', 'str', 'return', 'np.ndarray')):
    '''
    Compute the quantiles of the given values for each quantile in `qs`.

    Parameters
    ----------
    values : np.ndarray
        For ExtensionArray, this is _values_for_factorize()[0]
    mask : np.ndarray[bool]
        mask = isna(values)
        For ExtensionArray, this is computed before calling _value_for_factorize
    fill_value : Scalar
        The value to interpret fill NA entries with
        For ExtensionArray, this is _values_for_factorize()[1]
    qs : np.ndarray[float64]
    interpolation : str
        Type of interpolation

    Returns
    -------
    np.ndarray

    Notes
    -----
    Assumes values is already 2D.  For ExtensionArray this means np.atleast_2d
    has been called on _values_for_factorize()[0]

    Quantile is computed along axis=1.
    '''
    pass
# WARNING: Decompyle incomplete


def _nanquantile_1d(values, mask = None, qs = None, na_value = None, interpolation = ('values', 'np.ndarray', 'mask', 'npt.NDArray[np.bool_]', 'qs', 'npt.NDArray[np.float64]', 'na_value', 'Scalar', 'interpolation', 'str', 'return', 'Scalar | np.ndarray')):
    '''
    Wrapper for np.quantile that skips missing values, specialized to
    1-dimensional case.

    Parameters
    ----------
    values : array over which to find quantiles
    mask : ndarray[bool]
        locations in values that should be considered missing
    qs : np.ndarray[float64] of quantile indices to find
    na_value : scalar
        value to return for empty or all-null values
    interpolation : str

    Returns
    -------
    quantiles : scalar or array
    '''
    values = values[~mask]
    if len(values) == 0:
        return np.full(len(qs), na_value)
    return None.quantile(values, qs, method = interpolation)


def _nanquantile(values = None, qs = None, *, na_value, mask, interpolation):
    '''
    Wrapper for np.quantile that skips missing values.

    Parameters
    ----------
    values : np.ndarray[ndim=2]  over which to find quantiles
    qs : np.ndarray[float64] of quantile indices to find
    na_value : scalar
        value to return for empty or all-null values
    mask : np.ndarray[bool]
        locations in values that should be considered missing
    interpolation : str

    Returns
    -------
    quantiles : scalar or array
    '''
    pass
# WARNING: Decompyle incomplete
