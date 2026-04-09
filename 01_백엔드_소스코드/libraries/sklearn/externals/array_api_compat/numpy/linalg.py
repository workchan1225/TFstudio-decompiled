# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: linalg.pyc (Python 3.11)

from __future__ import annotations
import numpy as np
from numpy.linalg import LinAlgError, cond, det, eig, eigvals, eigvalsh, inv, lstsq, matrix_power, multi_dot, norm, tensorinv, tensorsolve
from _internal import get_xp
from common import _linalg
from _aliases import matmul, matrix_transpose, tensordot, vecdot
from _typing import Array
cross = get_xp(np)(_linalg.cross)
outer = get_xp(np)(_linalg.outer)
EighResult = _linalg.EighResult
QRResult = _linalg.QRResult
SlogdetResult = _linalg.SlogdetResult
SVDResult = _linalg.SVDResult
eigh = get_xp(np)(_linalg.eigh)
qr = get_xp(np)(_linalg.qr)
slogdet = get_xp(np)(_linalg.slogdet)
svd = get_xp(np)(_linalg.svd)
cholesky = get_xp(np)(_linalg.cholesky)
matrix_rank = get_xp(np)(_linalg.matrix_rank)
pinv = get_xp(np)(_linalg.pinv)
matrix_norm = get_xp(np)(_linalg.matrix_norm)
svdvals = get_xp(np)(_linalg.svdvals)
diagonal = get_xp(np)(_linalg.diagonal)
trace = get_xp(np)(_linalg.trace)

def solve(x1 = None, x2 = None):
    
    try:
        _assert_stacked_2d = _assert_stacked_2d
        _assert_stacked_square = _assert_stacked_square
        _commonType = _commonType
        _makearray = _makearray
        _raise_linalgerror_singular = _raise_linalgerror_singular
        isComplexType = isComplexType
        import numpy.linalg._linalg
    except ImportError:
        _assert_stacked_2d = _assert_stacked_2d
        _assert_stacked_square = _assert_stacked_square
        _commonType = _commonType
        _makearray = _makearray
        _raise_linalgerror_singular = _raise_linalgerror_singular
        isComplexType = isComplexType
        import numpy.linalg.linalg

    _umath_linalg = _umath_linalg
    import numpy.linalg
    (x1, _) = _makearray(x1)
    _assert_stacked_2d(x1)
    _assert_stacked_square(x1)
    (x2, wrap) = _makearray(x2)
    (t, result_t) = _commonType(x1, x2)
    if x2.ndim == 1:
        gufunc = _umath_linalg.solve1
    else:
        gufunc = _umath_linalg.solve
    signature = 'DD->D' if isComplexType(t) else 'dd->d'
    np.errstate(call = _raise_linalgerror_singular, invalid = 'call', over = 'ignore', divide = 'ignore', under = 'ignore')
    r = gufunc(x1, x2, signature = signature)
    None(None, None)

if hasattr(np.linalg, 'vector_norm'):
    vector_norm = np.linalg.vector_norm
else:
    vector_norm = get_xp(np)(_linalg.vector_norm)
__all__ = [
    'LinAlgError',
    'cond',
    'det',
    'eig',
    'eigvals',
    'eigvalsh',
    'inv',
    'lstsq',
    'matrix_power',
    'multi_dot',
    'norm',
    'tensorinv',
    'tensorsolve']
__all__ += _linalg.__all__
__all__ += [
    'solve',
    'vector_norm']

def __dir__():
    return __all__
