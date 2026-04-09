# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: linalg.pyc (Python 3.11)

from __future__ import annotations
from _dtypes import _floating_dtypes, _numeric_dtypes, float32, float64, complex64, complex128
from _manipulation_functions import reshape
from _elementwise_functions import conj
from _array_object import Array
from core.numeric import normalize_axis_tuple
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from _typing import Literal, Optional, Sequence, Tuple, Union, Dtype
from typing import NamedTuple
import numpy.linalg as numpy
import numpy as np

class EighResult(NamedTuple):
    eigenvectors: 'Array' = 'EighResult'


class QRResult(NamedTuple):
    R: 'Array' = 'QRResult'


class SlogdetResult(NamedTuple):
    logabsdet: 'Array' = 'SlogdetResult'


class SVDResult(NamedTuple):
    Vh: 'Array' = 'SVDResult'


def cholesky(x = None, *, upper):
    '''
    Array API compatible wrapper for :py:func:`np.linalg.cholesky <numpy.linalg.cholesky>`.

    See its docstring for more information.
    '''
    if x.dtype not in _floating_dtypes:
        raise TypeError('Only floating-point dtypes are allowed in cholesky')
    L = np.linalg.cholesky(x._array)
    if upper:
        U = Array._new(L).mT
        if U.dtype in (complex64, complex128):
            U = conj(U)
        return U
    return None._new(L)


def cross(x1 = None, x2 = None, *, axis):
    '''
    Array API compatible wrapper for :py:func:`np.cross <numpy.cross>`.

    See its docstring for more information.
    '''
    if x1.dtype not in _numeric_dtypes or x2.dtype not in _numeric_dtypes:
        raise TypeError('Only numeric dtypes are allowed in cross')
    if x1.shape != x2.shape:
        raise ValueError('x1 and x2 must have the same shape')
    if x1.ndim == 0:
        raise ValueError('cross() requires arrays of dimension at least 1')
    if x1.shape[axis] != 3:
        raise ValueError('cross() dimension must equal 3')
    return Array._new(np.cross(x1._array, x2._array, axis = axis))


def det(x = None):
    '''
    Array API compatible wrapper for :py:func:`np.linalg.det <numpy.linalg.det>`.

    See its docstring for more information.
    '''
    if x.dtype not in _floating_dtypes:
        raise TypeError('Only floating-point dtypes are allowed in det')
    return Array._new(np.linalg.det(x._array))


def diagonal(x = None, *, offset):
    '''
    Array API compatible wrapper for :py:func:`np.diagonal <numpy.diagonal>`.

    See its docstring for more information.
    '''
    return Array._new(np.diagonal(x._array, offset = offset, axis1 = -2, axis2 = -1))


def eigh(x = None):
    '''
    Array API compatible wrapper for :py:func:`np.linalg.eigh <numpy.linalg.eigh>`.

    See its docstring for more information.
    '''
    if x.dtype not in _floating_dtypes:
        raise TypeError('Only floating-point dtypes are allowed in eigh')
# WARNING: Decompyle incomplete


def eigvalsh(x = None):
    '''
    Array API compatible wrapper for :py:func:`np.linalg.eigvalsh <numpy.linalg.eigvalsh>`.

    See its docstring for more information.
    '''
    if x.dtype not in _floating_dtypes:
        raise TypeError('Only floating-point dtypes are allowed in eigvalsh')
    return Array._new(np.linalg.eigvalsh(x._array))


def inv(x = None):
    '''
    Array API compatible wrapper for :py:func:`np.linalg.inv <numpy.linalg.inv>`.

    See its docstring for more information.
    '''
    if x.dtype not in _floating_dtypes:
        raise TypeError('Only floating-point dtypes are allowed in inv')
    return Array._new(np.linalg.inv(x._array))


def matmul(x1 = None, x2 = None):
    '''
    Array API compatible wrapper for :py:func:`np.matmul <numpy.matmul>`.

    See its docstring for more information.
    '''
    if x1.dtype not in _numeric_dtypes or x2.dtype not in _numeric_dtypes:
        raise TypeError('Only numeric dtypes are allowed in matmul')
    return Array._new(np.matmul(x1._array, x2._array))


def matrix_norm(x = None, *, keepdims, ord):
    '''
    Array API compatible wrapper for :py:func:`np.linalg.norm <numpy.linalg.norm>`.

    See its docstring for more information.
    '''
    if x.dtype not in _floating_dtypes:
        raise TypeError('Only floating-point dtypes are allowed in matrix_norm')
    return Array._new(np.linalg.norm(x._array, axis = (-2, -1), keepdims = keepdims, ord = ord))


def matrix_power(x = None, n = None):
    '''
    Array API compatible wrapper for :py:func:`np.matrix_power <numpy.matrix_power>`.

    See its docstring for more information.
    '''
    if x.dtype not in _floating_dtypes:
        raise TypeError('Only floating-point dtypes are allowed for the first argument of matrix_power')
    return Array._new(np.linalg.matrix_power(x._array, n))


def matrix_rank(x = None, *, rtol):
    '''
    Array API compatible wrapper for :py:func:`np.matrix_rank <numpy.matrix_rank>`.

    See its docstring for more information.
    '''
    if x.ndim < 2:
        raise np.linalg.LinAlgError('1-dimensional array given. Array must be at least two-dimensional')
    S = np.linalg.svd(x._array, compute_uv = False)
# WARNING: Decompyle incomplete


def matrix_transpose(x = None):
    if x.ndim < 2:
        raise ValueError('x must be at least 2-dimensional for matrix_transpose')
    return Array._new(np.swapaxes(x._array, -1, -2))


def outer(x1 = None, x2 = None):
    '''
    Array API compatible wrapper for :py:func:`np.outer <numpy.outer>`.

    See its docstring for more information.
    '''
    if x1.dtype not in _numeric_dtypes or x2.dtype not in _numeric_dtypes:
        raise TypeError('Only numeric dtypes are allowed in outer')
    if x1.ndim != 1 or x2.ndim != 1:
        raise ValueError('The input arrays to outer must be 1-dimensional')
    return Array._new(np.outer(x1._array, x2._array))


def pinv(x = None, *, rtol):
    '''
    Array API compatible wrapper for :py:func:`np.linalg.pinv <numpy.linalg.pinv>`.

    See its docstring for more information.
    '''
    if x.dtype not in _floating_dtypes:
        raise TypeError('Only floating-point dtypes are allowed in pinv')
# WARNING: Decompyle incomplete


def qr(x = None, *, mode):
    '''
    Array API compatible wrapper for :py:func:`np.linalg.qr <numpy.linalg.qr>`.

    See its docstring for more information.
    '''
    if x.dtype not in _floating_dtypes:
        raise TypeError('Only floating-point dtypes are allowed in qr')
# WARNING: Decompyle incomplete


def slogdet(x = None):
    '''
    Array API compatible wrapper for :py:func:`np.linalg.slogdet <numpy.linalg.slogdet>`.

    See its docstring for more information.
    '''
    if x.dtype not in _floating_dtypes:
        raise TypeError('Only floating-point dtypes are allowed in slogdet')
# WARNING: Decompyle incomplete


def _solve(a, b):
    _makearray = _makearray
    _assert_stacked_2d = _assert_stacked_2d
    _assert_stacked_square = _assert_stacked_square
    _commonType = _commonType
    isComplexType = isComplexType
    get_linalg_error_extobj = get_linalg_error_extobj
    _raise_linalgerror_singular = _raise_linalgerror_singular
    import linalg.linalg
    _umath_linalg = _umath_linalg
    import linalg
    (a, _) = _makearray(a)
    _assert_stacked_2d(a)
    _assert_stacked_square(a)
    (b, wrap) = _makearray(b)
    (t, result_t) = _commonType(a, b)
    if b.ndim == 1:
        gufunc = _umath_linalg.solve1
    else:
        gufunc = _umath_linalg.solve
    signature = 'DD->D' if isComplexType(t) else 'dd->d'
    np.errstate(call = _raise_linalgerror_singular, invalid = 'call', over = 'ignore', divide = 'ignore', under = 'ignore')
    r = gufunc(a, b, signature = signature)
    None(None, None)


def solve(x1 = None, x2 = None):
    '''
    Array API compatible wrapper for :py:func:`np.linalg.solve <numpy.linalg.solve>`.

    See its docstring for more information.
    '''
    if x1.dtype not in _floating_dtypes or x2.dtype not in _floating_dtypes:
        raise TypeError('Only floating-point dtypes are allowed in solve')
    return Array._new(_solve(x1._array, x2._array))


def svd(x = None, *, full_matrices):
    '''
    Array API compatible wrapper for :py:func:`np.linalg.svd <numpy.linalg.svd>`.

    See its docstring for more information.
    '''
    if x.dtype not in _floating_dtypes:
        raise TypeError('Only floating-point dtypes are allowed in svd')
# WARNING: Decompyle incomplete


def svdvals(x = None):
    if x.dtype not in _floating_dtypes:
        raise TypeError('Only floating-point dtypes are allowed in svdvals')
    return Array._new(np.linalg.svd(x._array, compute_uv = False))


def tensordot(x1 = None, x2 = None, *, axes):
    if x1.dtype not in _numeric_dtypes or x2.dtype not in _numeric_dtypes:
        raise TypeError('Only numeric dtypes are allowed in tensordot')
    return Array._new(np.tensordot(x1._array, x2._array, axes = axes))


def trace(x = None, *, offset, dtype):
    '''
    Array API compatible wrapper for :py:func:`np.trace <numpy.trace>`.

    See its docstring for more information.
    '''
    if x.dtype not in _numeric_dtypes:
        raise TypeError('Only numeric dtypes are allowed in trace')
# WARNING: Decompyle incomplete


def vecdot(x1 = None, x2 = None, *, axis):
    if x1.dtype not in _numeric_dtypes or x2.dtype not in _numeric_dtypes:
        raise TypeError('Only numeric dtypes are allowed in vecdot')
    ndim = max(x1.ndim, x2.ndim)
    x1_shape = (1,) * (ndim - x1.ndim) + tuple(x1.shape)
    x2_shape = (1,) * (ndim - x2.ndim) + tuple(x2.shape)
    if x1_shape[axis] != x2_shape[axis]:
        raise ValueError('x1 and x2 must have the same size along the given axis')
    (x1_, x2_) = np.broadcast_arrays(x1._array, x2._array)
    x1_ = np.moveaxis(x1_, axis, -1)
    x2_ = np.moveaxis(x2_, axis, -1)
    res = x1_[(..., None, :)] @ x2_[(..., None)]
    return Array._new(res[(..., 0, 0)])


def vector_norm(x = None, *, axis, keepdims, ord):
    '''
    Array API compatible wrapper for :py:func:`np.linalg.norm <numpy.linalg.norm>`.

    See its docstring for more information.
    '''
    pass
# WARNING: Decompyle incomplete

__all__ = [
    'cholesky',
    'cross',
    'det',
    'diagonal',
    'eigh',
    'eigvalsh',
    'inv',
    'matmul',
    'matrix_norm',
    'matrix_power',
    'matrix_rank',
    'matrix_transpose',
    'outer',
    'pinv',
    'qr',
    'slogdet',
    'solve',
    'svd',
    'svdvals',
    'tensordot',
    'trace',
    'vecdot',
    'vector_norm']
