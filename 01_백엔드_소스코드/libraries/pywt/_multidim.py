# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _multidim.pyc (Python 3.11)

'''
2D and nD Discrete Wavelet Transforms and Inverse Discrete Wavelet Transforms.
'''
from itertools import product
import numpy as np
from _c99_config import _have_c99_complex
from _extensions._dwt import dwt_axis, idwt_axis
from _utils import AxisError, _modes_per_axis, _wavelets_per_axis
__all__ = [
    'dwt2',
    'idwt2',
    'dwtn',
    'idwtn']

def dwt2(data, wavelet, mode, axes = ('symmetric', (-2, -1))):
    """
    2D Discrete Wavelet Transform.

    Parameters
    ----------
    data : array_like
        2D array with input data
    wavelet : Wavelet object or name string, or 2-tuple of wavelets
        Wavelet to use.  This can also be a tuple containing a wavelet to
        apply along each axis in ``axes``.
    mode : str or 2-tuple of strings, optional
        Signal extension mode, see :ref:`Modes <ref-modes>`. This can
        also be a tuple of modes specifying the mode to use on each axis in
        ``axes``.
    axes : 2-tuple of ints, optional
        Axes over which to compute the DWT. Repeated elements mean the DWT will
        be performed multiple times along these axes.

    Returns
    -------
    (cA, (cH, cV, cD)) : tuple
        Approximation, horizontal detail, vertical detail and diagonal
        detail coefficients respectively.  Horizontal refers to array axis 0
        (or ``axes[0]`` for user-specified ``axes``).

    Examples
    --------
    >>> import numpy as np
    >>> import pywt
    >>> data = np.ones((4,4), dtype=np.float64)
    >>> coeffs = pywt.dwt2(data, 'haar')
    >>> cA, (cH, cV, cD) = coeffs
    >>> cA
    array([[ 2.,  2.],
           [ 2.,  2.]])
    >>> cV
    array([[ 0.,  0.],
           [ 0.,  0.]])

    """
    axes = tuple(axes)
    data = np.asarray(data)
    if len(axes) != 2:
        raise ValueError('Expected 2 axes')
    if data.ndim < len(np.unique(axes)):
        raise ValueError('Input array has fewer dimensions than the specified axes')
    coefs = dwtn(data, wavelet, mode, axes)
    return (coefs['aa'], (coefs['da'], coefs['ad'], coefs['dd']))


def idwt2(coeffs, wavelet, mode, axes = ('symmetric', (-2, -1))):
    """
    2-D Inverse Discrete Wavelet Transform.

    Reconstructs data from coefficient arrays.

    Parameters
    ----------
    coeffs : tuple
        (cA, (cH, cV, cD)) A tuple with approximation coefficients and three
        details coefficients 2D arrays like from ``dwt2``.  If any of these
        components are set to ``None``, it will be treated as zeros.
    wavelet : Wavelet object or name string, or 2-tuple of wavelets
        Wavelet to use.  This can also be a tuple containing a wavelet to
        apply along each axis in ``axes``.
    mode : str or 2-tuple of strings, optional
        Signal extension mode, see :ref:`Modes <ref-modes>`. This can
        also be a tuple of modes specifying the mode to use on each axis in
        ``axes``.
    axes : 2-tuple of ints, optional
        Axes over which to compute the IDWT. Repeated elements mean the IDWT
        will be performed multiple times along these axes.

    Examples
    --------
    >>> import numpy as np
    >>> import pywt
    >>> data = np.array([[1,2], [3,4]], dtype=np.float64)
    >>> coeffs = pywt.dwt2(data, 'haar')
    >>> pywt.idwt2(coeffs, 'haar')
    array([[ 1.,  2.],
           [ 3.,  4.]])

    """
    (HL, LH, HH) = (LL,)
    axes = tuple(axes)
    if len(axes) != 2:
        raise ValueError('Expected 2 axes')
    coeffs = {
        'aa': LL,
        'da': HL,
        'ad': LH,
        'dd': HH }
    return idwtn(coeffs, wavelet, mode, axes)


def dwtn(data, wavelet, mode, axes = ('symmetric', None)):
    """
    Single-level n-dimensional Discrete Wavelet Transform.

    Parameters
    ----------
    data : array_like
        n-dimensional array with input data.
    wavelet : Wavelet object or name string, or tuple of wavelets
        Wavelet to use.  This can also be a tuple containing a wavelet to
        apply along each axis in ``axes``.
    mode : str or tuple of string, optional
        Signal extension mode used in the decomposition,
        see :ref:`Modes <ref-modes>`. This can also be a tuple of modes
        specifying the mode to use on each axis in ``axes``.
    axes : sequence of ints, optional
        Axes over which to compute the DWT. Repeated elements mean the DWT will
        be performed multiple times along these axes. A value of ``None`` (the
        default) selects all axes.

        Axes may be repeated, but information about the original size may be
        lost if it is not divisible by ``2 ** nrepeats``. The reconstruction
        will be larger, with additional values derived according to the
        ``mode`` parameter. ``pywt.wavedecn`` should be used for multilevel
        decomposition.

    Returns
    -------
    coeffs : dict
        Results are arranged in a dictionary, where key specifies
        the transform type on each dimension and value is a n-dimensional
        coefficients array.

        For example, for a 2D case the result will look something like this::

            {'aa': <coeffs>  # A(LL) - approx. on 1st dim, approx. on 2nd dim
             'ad': <coeffs>  # V(LH) - approx. on 1st dim, det. on 2nd dim
             'da': <coeffs>  # H(HL) - det. on 1st dim, approx. on 2nd dim
             'dd': <coeffs>  # D(HH) - det. on 1st dim, det. on 2nd dim
            }

        For user-specified ``axes``, the order of the characters in the
        dictionary keys map to the specified ``axes``.

    """
    pass
# WARNING: Decompyle incomplete


def _fix_coeffs(coeffs):
    missing_keys = coeffs.items()()
    if missing_keys:
        raise ValueError(f'''The following detail coefficients were set to None:\n{missing_keys}\nFor multilevel transforms, rather than setting\n\tcoeffs[key] = None\nuse\n\tcoeffs[key] = np.zeros_like(coeffs[key])\n''')
    invalid_keys = coeffs.items()()
    if invalid_keys:
        raise ValueError(f'''The following invalid keys were found in the detail coefficient dictionary: {invalid_keys}.''')
    key_lengths = coeffs()
    if len(np.unique(key_lengths)) > 1:
        raise ValueError('All detail coefficient names must have equal length.')
    return coeffs.items()()


def idwtn(coeffs, wavelet, mode, axes = ('symmetric', None)):
    '''
    Single-level n-dimensional Inverse Discrete Wavelet Transform.

    Parameters
    ----------
    coeffs: dict
        Dictionary as in output of ``dwtn``. Missing or ``None`` items
        will be treated as zeros.
    wavelet : Wavelet object or name string, or tuple of wavelets
        Wavelet to use.  This can also be a tuple containing a wavelet to
        apply along each axis in ``axes``.
    mode : str or list of string, optional
        Signal extension mode used in the decomposition,
        see :ref:`Modes <ref-modes>`. This can also be a tuple of modes
        specifying the mode to use on each axis in ``axes``.
    axes : sequence of ints, optional
        Axes over which to compute the IDWT. Repeated elements mean the IDWT
        will be performed multiple times along these axes. A value of ``None``
        (the default) selects all axes.

        For the most accurate reconstruction, the axes should be provided in
        the same order as they were provided to ``dwtn``.

    Returns
    -------
    data: ndarray
        Original signal reconstructed from input data.

    '''
    pass
# WARNING: Decompyle incomplete
