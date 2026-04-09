# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: nanfunctions.pyc (Python 3.11)

'''
Functions that ignore NaN.

Functions
---------

- `nanmin` -- minimum non-NaN value
- `nanmax` -- maximum non-NaN value
- `nanargmin` -- index of minimum non-NaN value
- `nanargmax` -- index of maximum non-NaN value
- `nansum` -- sum of non-NaN values
- `nanprod` -- product of non-NaN values
- `nancumsum` -- cumulative sum of non-NaN values
- `nancumprod` -- cumulative product of non-NaN values
- `nanmean` -- mean of non-NaN values
- `nanvar` -- variance of non-NaN values
- `nanstd` -- standard deviation of non-NaN values
- `nanmedian` -- median of non-NaN values
- `nanquantile` -- qth quantile of non-NaN values
- `nanpercentile` -- qth percentile of non-NaN values

'''
import functools
import warnings
import numpy as np
from numpy.lib import function_base
from numpy.core import overrides
array_function_dispatch = functools.partial(overrides.array_function_dispatch, module = 'numpy')
__all__ = [
    'nansum',
    'nanmax',
    'nanmin',
    'nanargmax',
    'nanargmin',
    'nanmean',
    'nanmedian',
    'nanpercentile',
    'nanvar',
    'nanstd',
    'nanprod',
    'nancumsum',
    'nancumprod',
    'nanquantile']

def _nan_mask(a, out = (None,)):
    """
    Parameters
    ----------
    a : array-like
        Input array with at least 1 dimension.
    out : ndarray, optional
        Alternate output array in which to place the result.  The default
        is ``None``; if provided, it must have the same shape as the
        expected output and will prevent the allocation of a new array.

    Returns
    -------
    y : bool ndarray or True
        A bool array where ``np.nan`` positions are marked with ``False``
        and other positions are marked with ``True``. If the type of ``a``
        is such that it can't possibly contain ``np.nan``, returns ``True``.
    """
    if a.dtype.kind not in 'fc':
        return True
    y = None.isnan(a, out = out)
    y = np.invert(y, out = y)
    return y


def _replace_nan(a, val):
    '''
    If `a` is of inexact type, make a copy of `a`, replace NaNs with
    the `val` value, and return the copy together with a boolean mask
    marking the locations where NaNs were present. If `a` is not of
    inexact type, do nothing and return `a` together with a mask of None.

    Note that scalars will end up as array scalars, which is important
    for using the result as the value of the out argument in some
    operations.

    Parameters
    ----------
    a : array-like
        Input array.
    val : float
        NaN values are set to val before doing the operation.

    Returns
    -------
    y : ndarray
        If `a` is of inexact type, return a copy of `a` with the NaNs
        replaced by the fill value, otherwise return `a`.
    mask: {bool, None}
        If `a` is of inexact type, return a boolean mask marking locations of
        NaNs, otherwise return None.

    '''
    a = np.asanyarray(a)
    if a.dtype == np.object_:
        mask = np.not_equal(a, a, dtype = bool)
    elif issubclass(a.dtype.type, np.inexact):
        mask = np.isnan(a)
    else:
        mask = None
# WARNING: Decompyle incomplete


def _copyto(a, val, mask):
    '''
    Replace values in `a` with NaN where `mask` is True.  This differs from
    copyto in that it will deal with the case where `a` is a numpy scalar.

    Parameters
    ----------
    a : ndarray or numpy scalar
        Array or numpy scalar some of whose values are to be replaced
        by val.
    val : numpy scalar
        Value used a replacement.
    mask : ndarray, scalar
        Boolean array. Where True the corresponding element of `a` is
        replaced by `val`. Broadcasts.

    Returns
    -------
    res : ndarray, scalar
        Array with elements replaced or scalar `val`.

    '''
    if isinstance(a, np.ndarray):
        np.copyto(a, val, where = mask, casting = 'unsafe')
    else:
        a = a.dtype.type(val)
    return a


def _remove_nan_1d(arr1d, overwrite_input = (False,)):
    '''
    Equivalent to arr1d[~arr1d.isnan()], but in a different order

    Presumably faster as it incurs fewer copies

    Parameters
    ----------
    arr1d : ndarray
        Array to remove nans from
    overwrite_input : bool
        True if `arr1d` can be modified in place

    Returns
    -------
    res : ndarray
        Array with nan elements removed
    overwrite_input : bool
        True if `res` can be modified in place, given the constraint on the
        input
    '''
    if arr1d.dtype == object:
        c = np.not_equal(arr1d, arr1d, dtype = bool)
    else:
        c = np.isnan(arr1d)
    s = np.nonzero(c)[0]
    if s.size == arr1d.size:
        warnings.warn('All-NaN slice encountered', RuntimeWarning, stacklevel = 6)
        return (arr1d[:0], True)
    if None.size == 0:
        return (arr1d, overwrite_input)
    if not None:
        arr1d = arr1d.copy()
    enonan = arr1d[-(s.size):][~c[-(s.size):]]
    arr1d[s[:enonan.size]] = enonan
    return (arr1d[:-(s.size)], True)


def _divide_by_count(a, b, out = (None,)):
    '''
    Compute a/b ignoring invalid results. If `a` is an array the division
    is done in place. If `a` is a scalar, then its type is preserved in the
    output. If out is None, then a is used instead so that the division
    is in place. Note that this is only called with `a` an inexact type.

    Parameters
    ----------
    a : {ndarray, numpy scalar}
        Numerator. Expected to be of inexact type but not checked.
    b : {ndarray, numpy scalar}
        Denominator.
    out : ndarray, optional
        Alternate output array in which to place the result.  The default
        is ``None``; if provided, it must have the same shape as the
        expected output, but the type will be cast if necessary.

    Returns
    -------
    ret : {ndarray, numpy scalar}
        The return value is a/b. If `a` was an ndarray the division is done
        in place. If `a` is a numpy scalar, the division preserves its type.

    '''
    np.errstate(invalid = 'ignore', divide = 'ignore')
# WARNING: Decompyle incomplete


def _nanmin_dispatcher(a, axis, out, keepdims, initial, where = (None, None, None, None, None)):
    return (a, out)

nanmin = (lambda a, axis, out, keepdims, initial, where = (None, None, np._NoValue, np._NoValue, np._NoValue): kwargs = { }if keepdims is not np._NoValue:
kwargs['keepdims'] = keepdimsif initial is not np._NoValue:
kwargs['initial'] = initialif where is not np._NoValue:
kwargs['where'] = where# WARNING: Decompyle incomplete
)()

def _nanmax_dispatcher(a, axis, out, keepdims, initial, where = (None, None, None, None, None)):
    return (a, out)

nanmax = (lambda a, axis, out, keepdims, initial, where = (None, None, np._NoValue, np._NoValue, np._NoValue): kwargs = { }if keepdims is not np._NoValue:
kwargs['keepdims'] = keepdimsif initial is not np._NoValue:
kwargs['initial'] = initialif where is not np._NoValue:
kwargs['where'] = where# WARNING: Decompyle incomplete
)()

def _nanargmin_dispatcher(a = array_function_dispatch(_nanmax_dispatcher), axis = (None, None), out = {
    'keepdims': None }, *, keepdims):
    return (a,)

nanargmin = (lambda a = array_function_dispatch(_nanargmin_dispatcher), axis = (None, None), out = {
    'keepdims': np._NoValue }, *, keepdims, mask = None, res = None: (a, mask) = _replace_nan(a, np.inf)# WARNING: Decompyle incomplete
)()

def _nanargmax_dispatcher(a = array_function_dispatch(_nanmin_dispatcher), axis = (None, None), out = {
    'keepdims': None }, *, keepdims):
    return (a,)

nanargmax = (lambda a = array_function_dispatch(_nanargmax_dispatcher), axis = (None, None), out = {
    'keepdims': np._NoValue }, *, keepdims, mask = None, res = None: (a, mask) = _replace_nan(a, -(np.inf))# WARNING: Decompyle incomplete
)()

def _nansum_dispatcher(a, axis, dtype, out, keepdims, initial, where = (None, None, None, None, None, None)):
    return (a, out)

nansum = (lambda a, axis, dtype, out, keepdims, initial, where = (None, None, None, np._NoValue, np._NoValue, np._NoValue): (a, mask) = _replace_nan(a, 0)np.sum(a, axis = axis, dtype = dtype, out = out, keepdims = keepdims, initial = initial, where = where))()

def _nanprod_dispatcher(a, axis, dtype, out, keepdims, initial, where = (None, None, None, None, None, None)):
    return (a, out)

nanprod = (lambda a, axis, dtype, out, keepdims, initial, where = (None, None, None, np._NoValue, np._NoValue, np._NoValue): (a, mask) = _replace_nan(a, 1)np.prod(a, axis = axis, dtype = dtype, out = out, keepdims = keepdims, initial = initial, where = where))()

def _nancumsum_dispatcher(a, axis, dtype, out = (None, None, None)):
    return (a, out)

nancumsum = (lambda a, axis, dtype, out = (None, None, None): (a, mask) = _replace_nan(a, 0)np.cumsum(a, axis = axis, dtype = dtype, out = out))()

def _nancumprod_dispatcher(a, axis, dtype, out = (None, None, None)):
    return (a, out)

nancumprod = (lambda a, axis, dtype, out = (None, None, None): (a, mask) = _replace_nan(a, 1)np.cumprod(a, axis = axis, dtype = dtype, out = out))()

def _nanmean_dispatcher(a, axis, dtype = array_function_dispatch(_nancumprod_dispatcher), out = (None, None, None, None), keepdims = {
    'where': None }, *, where):
    return (a, out)

nanmean = (lambda a, axis, dtype = array_function_dispatch(_nanmean_dispatcher), out = (None, None, None, np._NoValue), keepdims = {
    'where': np._NoValue }, *, where, arr = None, mask = None, cnt = None, tot = None: (arr, mask) = _replace_nan(a, 0)# WARNING: Decompyle incomplete
)()

def _nanmedian1d(arr1d, overwrite_input = (False,)):
    '''
    Private function for rank 1 arrays. Compute the median ignoring NaNs.
    See nanmedian for parameter usage
    '''
    (arr1d_parsed, overwrite_input) = _remove_nan_1d(arr1d, overwrite_input = overwrite_input)
    if arr1d_parsed.size == 0:
        return arr1d[-1]
    return None.median(arr1d_parsed, overwrite_input = overwrite_input)


def _nanmedian(a, axis, out, overwrite_input = (None, None, False)):
    """
    Private function that doesn't support extended axis or keepdims.
    These methods are extended to this function using _ureduce
    See nanmedian for parameter usage

    """
    pass
# WARNING: Decompyle incomplete


def _nanmedian_small(a, axis, out, overwrite_input = (None, None, False)):
    '''
    sort + indexing median, faster for small medians along multiple
    dimensions due to the high overhead of apply_along_axis

    see nanmedian for parameter usage
    '''
    a = np.ma.masked_array(a, np.isnan(a))
    m = np.ma.median(a, axis = axis, overwrite_input = overwrite_input)
    for i in range(np.count_nonzero(m.mask.ravel())):
        warnings.warn('All-NaN slice encountered', RuntimeWarning, stacklevel = 5)
    fill_value = np.timedelta64('NaT') if m.dtype.kind == 'm' else np.nan
# WARNING: Decompyle incomplete


def _nanmedian_dispatcher(a, axis, out, overwrite_input, keepdims = (None, None, None, None)):
    return (a, out)

nanmedian = (lambda a, axis, out, overwrite_input, keepdims = (None, None, False, np._NoValue): a = np.asanyarray(a)if a.size == 0:
np.nanmean(a, axis, out = out, keepdims = keepdims)None._ureduce(a, func = _nanmedian, keepdims = keepdims, axis = axis, out = out, overwrite_input = overwrite_input))()

def _nanpercentile_dispatcher(a, q, axis, out, overwrite_input = array_function_dispatch(_nanmedian_dispatcher), method = (None, None, None, None, None), keepdims = {
    'interpolation': None }, *, interpolation):
    return (a, q, out)

nanpercentile = (lambda a, q, axis, out, overwrite_input = array_function_dispatch(_nanpercentile_dispatcher), method = (None, None, False, 'linear', np._NoValue), keepdims = {
    'interpolation': None }, *, interpolation,
