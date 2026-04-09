# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _swt.pyc (Python 3.11)

import warnings
from itertools import product
import numpy as np
from _c99_config import _have_c99_complex
from _extensions._dwt import idwt_single
from _extensions._pywt import Modes, Wavelet, _check_dtype
from _extensions._swt import swt as _swt
from _extensions._swt import swt_axis as _swt_axis
from _extensions._swt import swt_max_level
from _multidim import idwt2, idwtn
from _utils import AxisError, _as_wavelet, _wavelets_per_axis
__all__ = [
    'swt',
    'swt_max_level',
    'iswt',
    'swt2',
    'iswt2',
    'swtn',
    'iswtn']

def _rescale_wavelet_filterbank(wavelet, sf):
    pass
# WARNING: Decompyle incomplete


def swt(data, wavelet, level, start_level, axis, trim_approx, norm = (None, 0, -1, False, False)):
    '''
    Multilevel 1D stationary wavelet transform.

    Parameters
    ----------
    data :
        Input signal
    wavelet :
        Wavelet to use (Wavelet object or name)
    level : int, optional
        The number of decomposition steps to perform.
    start_level : int, optional
        The level at which the decomposition will begin (it allows one to
        skip a given number of transform steps and compute
        coefficients starting from start_level) (default: 0)
    axis: int, optional
        Axis over which to compute the SWT. If not given, the
        last axis is used.
    trim_approx : bool, optional
        If True, approximation coefficients at the final level are retained.
    norm : bool, optional
        If True, transform is normalized so that the energy of the coefficients
        will be equal to the energy of ``data``. In other words,
        ``np.linalg.norm(data.ravel())`` will equal the norm of the
        concatenated transform coefficients when ``trim_approx`` is True.

    Returns
    -------
    coeffs : list
        List of approximation and details coefficients pairs in order
        similar to wavedec function::

            [(cAn, cDn), ..., (cA2, cD2), (cA1, cD1)]

        where n equals input parameter ``level``.

        If ``start_level = m`` is given, then the beginning m steps are
        skipped::

            [(cAm+n, cDm+n), ..., (cAm+1, cDm+1), (cAm, cDm)]

        If ``trim_approx`` is ``True``, then the output list is exactly as in
        ``pywt.wavedec``, where the first coefficient in the list is the
        approximation coefficient at the final level and the rest are the
        detail coefficients::

            [cAn, cDn, ..., cD2, cD1]

    Notes
    -----
    The implementation here follows the "algorithm a-trous" and requires that
    the signal length along the transformed axis be a multiple of ``2**level``.
    If this is not the case, the user should pad up to an appropriate size
    using a function such as ``numpy.pad``.

    A primary benefit of this transform in comparison to its decimated
    counterpart (``pywt.wavedecn``), is that it is shift-invariant. This comes
    at cost of redundancy in the transform (the size of the output coefficients
    is larger than the input).

    When the following three conditions are true:

        1. The wavelet is orthogonal
        2. ``swt`` is called with ``norm=True``
        3. ``swt`` is called with ``trim_approx=True``

    the transform has the following additional properties that may be
    desirable in applications:

        1. energy is conserved
        2. variance is partitioned across scales

    When used with ``norm=True``, this transform is closely related to the
    multiple-overlap DWT (MODWT) as popularized for time-series analysis,
    although the underlying implementation is slightly different from the one
    published in [1]_. Specifically, the implementation used here requires a
    signal that is a multiple of ``2**level`` in length.

    References
    ----------
    .. [1] DB Percival and AT Walden. Wavelet Methods for Time Series Analysis.
        Cambridge University Press, 2000.
    '''
    pass
# WARNING: Decompyle incomplete


def iswt(coeffs, wavelet, norm, axis = (False, -1)):
    """
    Multilevel 1D inverse discrete stationary wavelet transform.

    Parameters
    ----------
    coeffs : array_like
        Coefficients list of tuples::

            [(cAn, cDn), ..., (cA2, cD2), (cA1, cD1)]

        where cA is approximation, cD is details.  Index 1 corresponds to
        ``start_level`` from ``pywt.swt``.
    wavelet : Wavelet object or name string
        Wavelet to use
    norm : bool, optional
        Controls the normalization used by the inverse transform. This must
        be set equal to the value that was used by ``pywt.swt`` to preserve the
        energy of a round-trip transform.

    Returns
    -------
    1D array of reconstructed data.

    Examples
    --------
    >>> import pywt
    >>> coeffs = pywt.swt([1,2,3,4,5,6,7,8], 'db2', level=2)
    >>> pywt.iswt(coeffs, 'db2')
    array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.])
    """
    trim_approx = not isinstance(coeffs[0], (tuple, list))
    cA = coeffs[0] if trim_approx else coeffs[0][0]
    if cA.ndim > 1:
        return iswtn(coeffs_nd, wavelet, axes = (axis,), norm = norm)
    if None != 0 and axis != -1:
        raise AxisError('Axis greater than data dimensions')
# WARNING: Decompyle incomplete


def swt2(data, wavelet, level, start_level, axes, trim_approx, norm = (0, (-2, -1), False, False)):
    '''
    Multilevel 2D stationary wavelet transform.

    Parameters
    ----------
    data : array_like
        2D array with input data
    wavelet : Wavelet object or name string, or 2-tuple of wavelets
        Wavelet to use.  This can also be a tuple of wavelets to apply per
        axis in ``axes``.
    level : int
        The number of decomposition steps to perform.
    start_level : int, optional
        The level at which the decomposition will start (default: 0)
    axes : 2-tuple of ints, optional
        Axes over which to compute the SWT. Repeated elements are not allowed.
    trim_approx : bool, optional
        If True, approximation coefficients at the final level are retained.
    norm : bool, optional
        If True, transform is normalized so that the energy of the coefficients
        will be equal to the energy of ``data``. In other words,
        ``np.linalg.norm(data.ravel())`` will equal the norm of the
        concatenated transform coefficients when ``trim_approx`` is True.

    Returns
    -------
    coeffs : list
        Approximation and details coefficients (for ``start_level = m``).
        If ``trim_approx`` is ``False``, approximation coefficients are
        retained for all levels::

            [
                (cA_m+level,
                    (cH_m+level, cV_m+level, cD_m+level)
                ),
                ...,
                (cA_m+1,
                    (cH_m+1, cV_m+1, cD_m+1)
                ),
                (cA_m,
                    (cH_m, cV_m, cD_m)
                )
            ]

        where cA is approximation, cH is horizontal details, cV is
        vertical details, cD is diagonal details and m is ``start_level``.

        If ``trim_approx`` is ``True``, approximation coefficients are only
        retained at the final level of decomposition. This matches the format
        used by ``pywt.wavedec2``::

            [
                cA_m+level,
                (cH_m+level, cV_m+level, cD_m+level),
                ...,
                (cH_m+1, cV_m+1, cD_m+1),
                (cH_m, cV_m, cD_m),
            ]

    Notes
    -----
    The implementation here follows the "algorithm a-trous" and requires that
    the signal length along the transformed axes be a multiple of ``2**level``.
    If this is not the case, the user should pad up to an appropriate size
    using a function such as ``numpy.pad``.

    A primary benefit of this transform in comparison to its decimated
    counterpart (``pywt.wavedecn``), is that it is shift-invariant. This comes
    at cost of redundancy in the transform (the size of the output coefficients
    is larger than the input).

    When the following three conditions are true:

        1. The wavelet is orthogonal
        2. ``swt2`` is called with ``norm=True``
        3. ``swt2`` is called with ``trim_approx=True``

    the transform has the following additional properties that may be
    desirable in applications:

        1. energy is conserved
        2. variance is partitioned across scales

    '''
    axes = tuple(axes)
    data = np.asarray(data)
    if len(axes) != 2:
        raise ValueError('Expected 2 axes')
    if len(axes) != len(set(axes)):
        raise ValueError('The axes passed to swt2 must be unique.')
    if data.ndim < len(np.unique(axes)):
        raise ValueError('Input array has fewer dimensions than the specified axes')
    coefs = swtn(data, wavelet, level, start_level, axes, trim_approx, norm)
    ret = []
    if trim_approx:
        ret.append(coefs[0])
        coefs = coefs[1:]
    for c in coefs:
        if trim_approx:
            ret.append((c['da'], c['ad'], c['dd']))
            continue
        ret.append((c['aa'], (c['da'], c['ad'], c['dd'])))
        return ret


def iswt2(coeffs, wavelet, norm, axes = (False, (-2, -1))):
    """
    Multilevel 2D inverse discrete stationary wavelet transform.

    Parameters
    ----------
    coeffs : list
        Approximation and details coefficients::

            [
                (cA_n,
                    (cH_n, cV_n, cD_n)
                ),
                ...,
                (cA_2,
                    (cH_2, cV_2, cD_2)
                ),
                (cA_1,
                    (cH_1, cV_1, cD_1)
                )
            ]

        where cA is approximation, cH is horizontal details, cV is
        vertical details, cD is diagonal details and n is the number of
        levels.  Index 1 corresponds to ``start_level`` from ``pywt.swt2``.
    wavelet : Wavelet object or name string, or 2-tuple of wavelets
        Wavelet to use.  This can also be a 2-tuple of wavelets to apply per
        axis.
    norm : bool, optional
        Controls the normalization used by the inverse transform. This must
        be set equal to the value that was used by ``pywt.swt2`` to preserve
        the energy of a round-trip transform.

    Returns
    -------
    2D array of reconstructed data.

    Examples
    --------
    >>> import pywt
    >>> coeffs = pywt.swt2([[1,2,3,4],[5,6,7,8],
    ...                     [9,10,11,12],[13,14,15,16]],
    ...                    'db1', level=2)
    >>> pywt.iswt2(coeffs, 'db1')
    array([[  1.,   2.,   3.,   4.],
           [  5.,   6.,   7.,   8.],
           [  9.,  10.,  11.,  12.],
           [ 13.,  14.,  15.,  16.]])

    """
    trim_approx = not isinstance(coeffs[0], (tuple, list))
    cA = coeffs[0] if trim_approx else coeffs[0][0]
    if cA.ndim != 2 or axes != (-2, -1):
        return iswtn(coeffs_nd, wavelet, axes = axes, norm = norm)
# WARNING: Decompyle incomplete


def swtn(data, wavelet, level, start_level, axes, trim_approx, norm = (0, None, False, False)):
    '''
    n-dimensional stationary wavelet transform.

    Parameters
    ----------
    data : array_like
        n-dimensional array with input data.
    wavelet : Wavelet object or name string, or tuple of wavelets
        Wavelet to use.  This can also be a tuple of wavelets to apply per
        axis in ``axes``.
    level : int
        The number of decomposition steps to perform.
    start_level : int, optional
        The level at which the decomposition will start (default: 0)
    axes : sequence of ints, optional
        Axes over which to compute the SWT. A value of ``None`` (the
        default) selects all axes. Axes may not be repeated.
    trim_approx : bool, optional
        If True, approximation coefficients at the final level are retained.
    norm : bool, optional
        If True, transform is normalized so that the energy of the coefficients
        will be equal to the energy of ``data``. In other words,
        ``np.linalg.norm(data.ravel())`` will equal the norm of the
        concatenated transform coefficients when ``trim_approx`` is True.

    Returns
    -------
    [{coeffs_level_n}, ..., {coeffs_level_1}]: list of dict
        Results for each level are arranged in a dictionary, where the key
        specifies the transform type on each dimension and value is a
        n-dimensional coefficients array.

        For example, for a 2D case the result at a given level will look
        something like this::

            {\'aa\': <coeffs>  # A(LL) - approx. on 1st dim, approx. on 2nd dim
             \'ad\': <coeffs>  # V(LH) - approx. on 1st dim, det. on 2nd dim
             \'da\': <coeffs>  # H(HL) - det. on 1st dim, approx. on 2nd dim
             \'dd\': <coeffs>  # D(HH) - det. on 1st dim, det. on 2nd dim
            }

        For user-specified ``axes``, the order of the characters in the
        dictionary keys map to the specified ``axes``.

        If ``trim_approx`` is ``True``, the first element of the list contains
        the array of approximation coefficients from the final level of
        decomposition, while the remaining coefficient dictionaries contain
        only detail coefficients. This matches the behavior of `pywt.wavedecn`.

    Notes
    -----
    The implementation here follows the "algorithm a-trous" and requires that
    the signal length along the transformed axes be a multiple of ``2**level``.
    If this is not the case, the user should pad up to an appropriate size
    using a function such as ``numpy.pad``.

    A primary benefit of this transform in comparison to its decimated
    counterpart (``pywt.wavedecn``), is that it is shift-invariant. This comes
    at cost of redundancy in the transform (the size of the output coefficients
    is larger than the input).

    When the following three conditions are true:

        1. The wavelet is orthogonal
        2. ``swtn`` is called with ``norm=True``
        3. ``swtn`` is called with ``trim_approx=True``

    the transform has the following additional properties that may be
    desirable in applications:

        1. energy is conserved
        2. variance is partitioned across scales

    '''
    pass
# WARNING: Decompyle incomplete


def iswtn(coeffs, wavelet, axes, norm = (None, False)):
    """
    Multilevel nD inverse discrete stationary wavelet transform.

    Parameters
    ----------
    coeffs : list
        [{coeffs_level_n}, ..., {coeffs_level_1}]: list of dict
    wavelet : Wavelet object or name string, or tuple of wavelets
        Wavelet to use.  This can also be a tuple of wavelets to apply per
        axis in ``axes``.
    axes : sequence of ints, optional
        Axes over which to compute the inverse SWT. Axes may not be repeated.
        The default is ``None``, which means transform all axes
        (``axes = range(data.ndim)``).
    norm : bool, optional
        Controls the normalization used by the inverse transform. This must
        be set equal to the value that was used by ``pywt.swtn`` to preserve
        the energy of a round-trip transform.

    Returns
    -------
    nD array of reconstructed data.

    Examples
    --------
    >>> import pywt
    >>> coeffs = pywt.swtn([[1,2,3,4],[5,6,7,8],
    ...                     [9,10,11,12],[13,14,15,16]],
    ...                    'db1', level=2)
    >>> pywt.iswtn(coeffs, 'db1')
    array([[  1.,   2.,   3.,   4.],
           [  5.,   6.,   7.,   8.],
           [  9.,  10.,  11.,  12.],
           [ 13.,  14.,  15.,  16.]])

    """
    pass
# WARNING: Decompyle incomplete
