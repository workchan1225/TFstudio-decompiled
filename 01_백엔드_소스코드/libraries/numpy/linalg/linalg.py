# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: linalg.pyc (Python 3.11)

'''Lite version of scipy.linalg.

Notes
-----
This module is a lite version of the linalg.py module in SciPy which
contains high-level Python interface to the LAPACK library.  The lite
version only accesses the following LAPACK functions: dgesv, zgesv,
dgeev, zgeev, dgesdd, zgesdd, dgelsd, zgelsd, dsyevd, zheevd, dgetrf,
zgetrf, dpotrf, zpotrf, dgeqrf, zgeqrf, zungqr, dorgqr.
'''
__all__ = [
    'matrix_power',
    'solve',
    'tensorsolve',
    'tensorinv',
    'inv',
    'cholesky',
    'eigvals',
    'eigvalsh',
    'pinv',
    'slogdet',
    'det',
    'svd',
    'eig',
    'eigh',
    'lstsq',
    'norm',
    'qr',
    'cond',
    'matrix_rank',
    'LinAlgError',
    'multi_dot']
import functools
import operator
import warnings
from typing import NamedTuple, Any
from _utils import set_module
from numpy.core import array, asarray, zeros, empty, empty_like, intc, single, double, csingle, cdouble, inexact, complexfloating, newaxis, all, Inf, dot, add, multiply, sqrt, sum, isfinite, finfo, errstate, geterrobj, moveaxis, amin, amax, prod, abs, atleast_2d, intp, asanyarray, object_, matmul, swapaxes, divide, count_nonzero, isnan, sign, argsort, sort, reciprocal
from numpy.core.multiarray import normalize_axis_index
from numpy.core import overrides
from numpy.lib.twodim_base import triu, eye
from numpy.linalg import _umath_linalg
from numpy._typing import NDArray

class EigResult(NamedTuple):
    eigenvectors: NDArray[Any] = 'EigResult'


class EighResult(NamedTuple):
    eigenvectors: NDArray[Any] = 'EighResult'


class QRResult(NamedTuple):
    R: NDArray[Any] = 'QRResult'


class SlogdetResult(NamedTuple):
    logabsdet: NDArray[Any] = 'SlogdetResult'


class SVDResult(NamedTuple):
    Vh: NDArray[Any] = 'SVDResult'

array_function_dispatch = functools.partial(overrides.array_function_dispatch, module = 'numpy.linalg')
fortran_int = intc
LinAlgError = <NODE:12>()

def _determine_error_states():
    errobj = geterrobj()
    bufsize = errobj[0]
    errstate(invalid = 'call', over = 'ignore', divide = 'ignore', under = 'ignore')
    invalid_call_errmask = geterrobj()[1]
    None(None, None)

_linalg_error_extobj = _determine_error_states()
del _determine_error_states

def _raise_linalgerror_singular(err, flag):
    raise LinAlgError('Singular matrix')


def _raise_linalgerror_nonposdef(err, flag):
    raise LinAlgError('Matrix is not positive definite')


def _raise_linalgerror_eigenvalues_nonconvergence(err, flag):
    raise LinAlgError('Eigenvalues did not converge')


def _raise_linalgerror_svd_nonconvergence(err, flag):
    raise LinAlgError('SVD did not converge')


def _raise_linalgerror_lstsq(err, flag):
    raise LinAlgError('SVD did not converge in Linear Least Squares')


def _raise_linalgerror_qr(err, flag):
    raise LinAlgError('Incorrect argument found while performing QR factorization')


def get_linalg_error_extobj(callback):
    extobj = list(_linalg_error_extobj)
    extobj[2] = callback
    return extobj


def _makearray(a):
    new = asarray(a)
    wrap = getattr(a, '__array_prepare__', new.__array_wrap__)
    return (new, wrap)


def isComplexType(t):
    return issubclass(t, complexfloating)

_real_types_map = {
    cdouble: double,
    csingle: single,
    double: double,
    single: single }
_complex_types_map = {
    cdouble: cdouble,
    csingle: csingle,
    double: cdouble,
    single: csingle }

def _realType(t, default = (double,)):
    return _real_types_map.get(t, default)


def _complexType(t, default = (cdouble,)):
    return _complex_types_map.get(t, default)


def _commonType(*arrays):
    result_type = single
    is_complex = False
# WARNING: Decompyle incomplete


def _to_native_byte_order(*arrays):
    ret = []
    for arr in arrays:
        if arr.dtype.byteorder not in ('=', '|'):
            ret.append(asarray(arr, dtype = arr.dtype.newbyteorder('=')))
            continue
        ret.append(arr)
        if len(ret) == 1:
            return ret[0]
        return None


def _assert_2d(*arrays):
    for a in arrays:
        if a.ndim != 2:
            raise LinAlgError('%d-dimensional array given. Array must be two-dimensional' % a.ndim)
        return None


def _assert_stacked_2d(*arrays):
    for a in arrays:
        if a.ndim < 2:
            raise LinAlgError('%d-dimensional array given. Array must be at least two-dimensional' % a.ndim)
        return None


def _assert_stacked_square(*arrays):
    for a in arrays:
        (m, n) = a.shape[-2:]
        if m != n:
            raise LinAlgError('Last 2 dimensions of the array must be square')
        return None


def _assert_finite(*arrays):
    for a in arrays:
        if not isfinite(a).all():
            raise LinAlgError('Array must not contain infs or NaNs')
        return None


def _is_empty_2d(arr):
    if arr.size == 0:
        pass
    return prod(arr.shape[-2:]) == 0


def transpose(a):
    '''
    Transpose each matrix in a stack of matrices.

    Unlike np.transpose, this only swaps the last two axes, rather than all of
    them

    Parameters
    ----------
    a : (...,M,N) array_like

    Returns
    -------
    aT : (...,N,M) ndarray
    '''
    return swapaxes(a, -1, -2)


def _tensorsolve_dispatcher(a, b, axes = (None,)):
    return (a, b)

tensorsolve = (lambda a, b, axes = (None,): (a, wrap) = _makearray(a)b = asarray(b)an = a.ndim# WARNING: Decompyle incomplete
)()

def _solve_dispatcher(a, b):
    return (a, b)

solve = (lambda a, b: (a, _) = _makearray(a)_assert_stacked_2d(a)_assert_stacked_square(a)(b, wrap) = _makearray(b)(t, result_t) = _commonType(a, b)if b.ndim == a.ndim - 1:
gufunc = _umath_linalg.solve1else:
gufunc = _umath_linalg.solvesignature = 'DD->D' if isComplexType(t) else 'dd->d'extobj = get_linalg_error_extobj(_raise_linalgerror_singular)r = gufunc(a, b, signature = signature, extobj = extobj)wrap(r.astype(result_t, copy = False)))()

def _tensorinv_dispatcher(a, ind = (None,)):
    return (a,)

tensorinv = (lambda a, ind = (2,): a = asarray(a)oldshape = a.shapeprod = 1if ind > 0:
invshape = oldshape[ind:] + oldshape[:ind]for k in oldshape[ind:]:
prod *= kraise ValueError('Invalid ind argument.')a = a.reshape(prod, -1)ia = inv(a)# WARNING: Decompyle incomplete
)()

def _unary_dispatcher(a):
    return (a,)

inv = (lambda a: (a, wrap) = _makearray(a)_assert_stacked_2d(a)_assert_stacked_square(a)(t, result_t) = _commonType(a)signature = 'D->D' if isComplexType(t) else 'd->d'extobj = get_linalg_error_extobj(_raise_linalgerror_singular)ainv = _umath_linalg.inv(a, signature = signature, extobj = extobj)wrap(ainv.astype(result_t, copy = False)))()

def _matrix_power_dispatcher(a, n):
    return (a,)

matrix_power = (lambda a, n: a = asanyarray(a)_assert_stacked_2d(a)_assert_stacked_square(a)try:
n = operator.index(n)except TypeError:
e = Noneraise TypeError('exponent must be an integer'), ee = Nonedel eif a.dtype != object:
fmatmul = matmulelif a.ndim == 2:
fmatmul = dotelse:
raise NotImplementedError('matrix_power not supported for stacks of object arrays')if n == 0:
a = empty_like(a)a[...] = eye(a.shape[-2], dtype = a.dtype)aif None < 0:
a = inv(a)n = abs(n)if n == 1:
aif None == 2:
fmatmul(a, a)if None == 3:
fmatmul(fmatmul(a, a), a)z = Noneresult = None# WARNING: Decompyle incomplete
)()
cholesky = (lambda a: extobj = get_linalg_error_extobj(_raise_linalgerror_nonposdef)gufunc = _umath_linalg.cholesky_lo(a, wrap) = _makearray(a)_assert_stacked_2d(a)_assert_stacked_square(a)(t, result_t) = _commonType(a)signature = 'D->D' if isComplexType(t) else 'd->d'r = gufunc(a, signature = signature, extobj = extobj)wrap(r.astype(result_t, copy = False)))()

def _qr_dispatcher(a, mode = (None,)):
    return (a,)

qr = (lambda a, mode = ('reduced',): if mode not in ('reduced', 'complete', 'r', 'raw'):
if mode in ('f', 'full'):
msg = ''.join(("The 'full' option is deprecated in favor of 'reduced'.\n", 'For backward compatibility let mode default.'))warnings.warn(msg, DeprecationWarning, stacklevel = 2)mode = 'reduced'elif mode in ('e', 'economic'):
msg = "The 'economic' option is deprecated."warnings.warn(msg, DeprecationWarning, stacklevel = 2)mode = 'economic'else:
raise ValueError(f'''Unrecognized mode \'{mode}\'''')(a, wrap) = _makearray(a)_assert_stacked_2d(a)(m, n) = a.shape[-2:](t, result_t) = _commonType(a)a = a.astype(t, copy = True)a = _to_native_byte_order(a)mn = min(m, n)if m <= n:
gufunc = _umath_linalg.qr_r_raw_melse:
gufunc = _umath_linalg.qr_r_raw_nsignature = 'D->D' if isComplexType(t) else 'd->d'extobj = get_linalg_error_extobj(_raise_linalgerror_qr)tau = gufunc(a, signature = signature, extobj = extobj)if mode == 'r':
r = triu(a[(..., :mn, :)])r = r.astype(result_t, copy = False)wrap(r)if None == 'raw':
q = transpose(a)q = q.astype(result_t, copy = False)tau = tau.astype(result_t, copy = False)(wrap(q), tau)if None == 'economic':
a = a.astype(result_t, copy = False)wrap(a)if None == 'complete' and m > n:
mc = mgufunc = _umath_linalg.qr_completeelse:
mc = mngufunc = _umath_linalg.qr_reducedsignature = 'DD->D' if isComplexType(t) else 'dd->d'extobj = get_linalg_error_extobj(_raise_linalgerror_qr)q = gufunc(a, tau, signature = signature, extobj = extobj)r = triu(a[(..., :mc, :)])q = q.astype(result_t, copy = False)r = r.astype(result_t, copy = False)QRResult(wrap(q), wrap(r)))()
eigvals = (lambda a: (a, wrap) = _makearray(a)_assert_stacked_2d(a)_assert_stacked_square(a)_assert_finite(a)(t, result_t) = _commonType(a)extobj = get_linalg_error_extobj(_raise_linalgerror_eigenvalues_nonconvergence)signature = 'D->D' if isComplexType(t) else 'd->D'w = _umath_linalg.eigvals(a, signature = signature, extobj = extobj)if not isComplexType(t):
if all(w.imag == 0):
w = w.realresult_t = _realType(result_t)else:
result_t = _complexType(result_t)w.astype(result_t, copy = False))()

def _eigvalsh_dispatcher(a, UPLO = (None,)):
    return (a,)

eigvalsh = (lambda a, UPLO = ('L',): UPLO = UPLO.upper()if UPLO not in ('L', 'U'):
raise ValueError("UPLO argument must be 'L' or 'U'")extobj = get_linalg_error_extobj(_raise_linalgerror_eigenvalues_nonconvergence)if UPLO == 'L':
gufunc = _umath_linalg.eigvalsh_loelse:
gufunc = _umath_linalg.eigvalsh_up(a, wrap) = _makearray(a)_assert_stacked_2d(a)_assert_stacked_square(a)(t, result_t) = _commonType(a)signature = 'D->d' if isComplexType(t) else 'd->d'w = gufunc(a, signature = signature, extobj = extobj)w.astype(_realType(result_t), copy = False))()

def _convertarray(a):
    (t, result_t) = _commonType(a)
    a = a.astype(t).T.copy()
    return (a, t, result_t)

eig = (lambda a: (a, wrap) = _makearray(a)_assert_stacked_2d(a)_assert_stacked_square(a)_assert_finite(a)(t, result_t) = _commonType(a)extobj = get_linalg_error_extobj(_raise_linalgerror_eigenvalues_nonconvergence)signature = 'D->DD' if isComplexType(t) else 'd->DD'(w, vt) = _umath_linalg.eig(a, signature = signature, extobj = extobj)if isComplexType(t) and all(w.imag == 0):
w = w.realvt = vt.realresult_t = _realType(result_t)else:
result_t = _complexType(result_t)vt = vt.astype(result_t, copy = False)EigResult(w.astype(result_t, copy = False), wrap(vt)))()
eigh = (lambda a, UPLO = ('L',): UPLO = UPLO.upper()if UPLO not in ('L', 'U'):
raise ValueError("UPLO argument must be 'L' or 'U'")(a, wrap) = _makearray(a)_assert_stacked_2d(a)_assert_stacked_square(a)(t, result_t) = _commonType(a)extobj = get_linalg_error_extobj(_raise_linalgerror_eigenvalues_nonconvergence)if UPLO == 'L':
gufunc = _umath_linalg.eigh_loelse:
gufunc = _umath_linalg.eigh_upsignature = 'D->dD' if isComplexType(t) else 'd->dd'(w, vt) = gufunc(a, signature = signature, extobj = extobj)w = w.astype(_realType(result_t), copy = False)vt = vt.astype(result_t, copy = False)EighResult(w, wrap(vt)))()

def _svd_dispatcher(a, full_matrices, compute_uv, hermitian = (None, None, None)):
    return (a,)

svd = (lambda a, full_matrices, compute_uv, hermitian = (True, True, False): import numpy as _nx(a, wrap) = _makearray(a)if hermitian:
if compute_uv:
(s, u) = eigh(a)sgn = sign(s)s = abs(s)sidx = argsort(s)[(..., ::-1)]sgn = _nx.take_along_axis(sgn, sidx, axis = -1)s = _nx.take_along_axis(s, sidx, axis = -1)u = _nx.take_along_axis(u, sidx[(..., None, :)], axis = -1)vt = transpose(u * sgn[(..., None, :)]).conjugate()SVDResult(wrap(u), s, wrap(vt))s = None(a)s = abs(s)sort(s)[(..., ::-1)]None(a)(t, result_t) = _commonType(a)extobj = get_linalg_error_extobj(_raise_linalgerror_svd_nonconvergence)(m, n) = a.shape[-2:]if compute_uv:
if full_matrices:
if m < n:
gufunc = _umath_linalg.svd_m_felse:
gufunc = _umath_linalg.svd_n_felif m < n:
gufunc = _umath_linalg.svd_m_selse:
gufunc = _umath_linalg.svd_n_ssignature = 'D->DdD' if isComplexType(t) else 'd->ddd'(u, s, vh) = gufunc(a, signature = signature, extobj = extobj)u = u.astype(result_t, copy = False)s = s.astype(_realType(result_t), copy = False)vh = vh.astype(result_t, copy = False)SVDResult(wrap(u), s, wrap(vh))if None < n:
gufunc = _umath_linalg.svd_melse:
gufunc = _umath_linalg.svd_nsignature = 'D->d' if isComplexType(t) else 'd->d's = gufunc(a, signature = signature, extobj = extobj)s = s.astype(_realType(result_t), copy = False)s)()

def _cond_dispatcher(x, p = (None,)):
    return (x,)

cond = (lambda x, p = (None,): x = asarray(x)if _is_empty_2d(x):
raise LinAlgError('cond is not defined on empty arrays')# WARNING: Decompyle incomplete
)()

def _matrix_rank_dispatcher(A, tol, hermitian = (None, None)):
    return (A,)

matrix_rank = (lambda A, tol, hermitian = (None, False): A = asarray(A)if A.ndim < 2:
int(not all(A == 0))S = None(A, compute_uv = False, hermitian = hermitian)# WARNING: Decompyle incomplete
)()

def _pinv_dispatcher(a, rcond, hermitian = (None, None)):
    return (a,)

pinv = (lambda a, rcond, hermitian = (1e-15, False): (a, wrap) = _makearray(a)rcond = asarray(rcond)if _is_empty_2d(a):
(m, n) = a.shape[-2:]res = empty(a.shape[:-2] + (n, m), dtype = a.dtype)wrap(res)a = None.conjugate()(u, s, vt) = svd(a, full_matrices = False, hermitian = hermitian)cutoff = rcond[(..., newaxis)] * amax(s, axis = -1, keepdims = True)large = s > cutoffs = divide(1, s, where = large, out = s)s[~large] = 0res = matmul(transpose(vt), multiply(s[(..., newaxis)], transpose(u)))wrap(res))()
slogdet = (lambda a: a = asarray(a)_assert_stacked_2d(a)_assert_stacked_square(a)(t, result_t) = _commonType(a)real_t = _realType(result_t)signature = 'D->Dd' if isComplexType(t) else 'd->dd'(sign, logdet) = _umath_linalg.slogdet(a, signature = signature)sign = sign.astype(result_t, copy = False)logdet = logdet.astype(real_t, copy = False)SlogdetResult(sign, logdet))()
det = (lambda a: a = asarray(a)_assert_stacked_2d(a)_assert_stacked_square(a)(t, result_t) = _commonType(a)signature = 'D->D' if isComplexType(t) else 'd->d'r = _umath_linalg.det(a, signature = signature)r = r.astype(result_t, copy = False)r)()

def _lstsq_dispatcher(a, b, rcond = (None,)):
    return (a, b)

lstsq = (lambda a, b, rcond = ('warn',): (a, _) = _makearray(a)(b, wrap) = _makearray(b)is_1d = b.ndim == 1if is_1d:
b = b[(:, newaxis)]_assert_2d(a, b)(m, n) = a.shape[-2:](m2, n_rhs) = b.shape[-2:]if m != m2:
raise LinAlgError('Incompatible dimensions')(t, result_t) = _commonType(a, b)result_real_t = _realType(result_t)if rcond == 'warn':
warnings.warn('`rcond` parameter will change to the default of machine precision times ``max(M, N)`` where M and N are the input matrix dimensions.\nTo use the future default and silence this warning we advise to pass `rcond=None`, to keep using the old, explicitly pass `rcond=-1`.', FutureWarning, stacklevel = 2)rcond = -1# WARNING: Decompyle incomplete
)()

def _multi_svd_norm(x, row_axis, col_axis, op):
    '''Compute a function of the singular values of the 2-D matrices in `x`.

    This is a private utility function used by `numpy.linalg.norm()`.

    Parameters
    ----------
    x : ndarray
    row_axis, col_axis : int
        The axes of `x` that hold the 2-D matrices.
    op : callable
        This should be either numpy.amin or `numpy.amax` or `numpy.sum`.

    Returns
    -------
    result : float or ndarray
        If `x` is 2-D, the return values is a float.
        Otherwise, it is an array with ``x.ndim - 2`` dimensions.
        The return values are either the minimum or maximum or sum of the
        singular values of the matrices, depending on whether `op`
        is `numpy.amin` or `numpy.amax` or `numpy.sum`.

    '''
    y = moveaxis(x, (row_axis, col_axis), (-2, -1))
    result = op(svd(y, compute_uv = False), axis = -1)
    return result


def _norm_dispatcher(x, ord, axis, keepdims = (None, None, None)):
    return (x,)

norm = (lambda x, ord, axis, keepdims = (None, None, False): x = asarray(x)if not issubclass(x.dtype.type, (inexact, object_)):
x = x.astype(float)# WARNING: Decompyle incomplete
)()

def _multidot_dispatcher(arrays = array_function_dispatch(_norm_dispatcher), *, out):
    pass
# WARNING: Decompyle incomplete

multi_dot = (lambda arrays = array_function_dispatch(_multidot_dispatcher), *, out:
