# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: polynomial.pyc (Python 3.11)

'''
Functions to operate on polynomials.

'''
__all__ = [
    'poly',
    'roots',
    'polyint',
    'polyder',
    'polyadd',
    'polysub',
    'polymul',
    'polydiv',
    'polyval',
    'poly1d',
    'polyfit',
    'RankWarning']
import functools
import re
import warnings
from _utils import set_module

numeric
from numpy.core import isscalar, abs, finfo, atleast_1d, hstack, dot, array, ones
abs = abs
finfo = finfo
atleast_1d = atleast_1d
hstack = hstack
dot = dot
array = array
ones = ones
import numpy.core.numeric, core
from numpy.core import overrides
from numpy.lib.twodim_base import diag, vander
from numpy.lib.function_base import trim_zeros
from numpy.lib.type_check import iscomplex, real, imag, mintypecode
from numpy.linalg import eigvals, lstsq, inv
array_function_dispatch = functools.partial(overrides.array_function_dispatch, module = 'numpy')
RankWarning = <NODE:12>()

def _poly_dispatcher(seq_of_zeros):
    return seq_of_zeros

poly = (lambda seq_of_zeros: seq_of_zeros = atleast_1d(seq_of_zeros)sh = seq_of_zeros.shapeif len(sh) == 2 and sh[0] == sh[1] and sh[0] != 0:
seq_of_zeros = eigvals(seq_of_zeros)elif len(sh) == 1:
dt = seq_of_zeros.dtypeif dt != object:
seq_of_zeros = seq_of_zeros.astype(mintypecode(dt.char))else:
raise ValueError('input must be 1d or non-empty square 2d array.')if len(seq_of_zeros) == 0:
1dt = None.dtypea = ones((1,), dtype = dt)for zero in seq_of_zeros:
a = NX.convolve(a, array([
1,
-zero], dtype = dt), mode = 'full')if issubclass(a.dtype.type, NX.complexfloating):
roots = NX.asarray(seq_of_zeros, complex)if NX.all(NX.sort(roots) == NX.sort(roots.conjugate())):
a = a.real.copy()a)()

def _roots_dispatcher(p):
    return p

roots = (lambda p: p = atleast_1d(p)if p.ndim != 1:
raise ValueError('Input must be a rank-1 array.')non_zero = NX.nonzero(NX.ravel(p))[0]if len(non_zero) == 0:
NX.array([])trailing_zeros = None(p) - non_zero[-1] - 1p = p[int(non_zero[0]):int(non_zero[-1]) + 1]if not issubclass(p.dtype.type, (NX.floating, NX.complexfloating)):
p = p.astype(float)N = len(p)if N > 1:
A = diag(NX.ones((N - 2,), p.dtype), -1)A[(0, :)] = -p[1:] / p[0]roots = eigvals(A)else:
roots = NX.array([])roots = hstack((roots, NX.zeros(trailing_zeros, roots.dtype)))roots)()

def _polyint_dispatcher(p, m, k = (None, None)):
    return (p,)

polyint = (lambda p, m, k = (1, None): m = int(m)if m < 0:
raise ValueError('Order of integral must be positive (see polyder)')# WARNING: Decompyle incomplete
)()

def _polyder_dispatcher(p, m = (None,)):
    return (p,)

polyder = (lambda p, m = (1,): m = int(m)if m < 0:
raise ValueError('Order of derivative must be positive (see polyint)')truepoly = isinstance(p, poly1d)p = NX.asarray(p)n = len(p) - 1y = p[:-1] * NX.arange(n, 0, -1)if m == 0:
val = pelse:
val = polyder(y, m - 1)if truepoly:
val = poly1d(val)val)()

def _polyfit_dispatcher(x, y, deg, rcond, full, w, cov = (None, None, None, None)):
    return (x, y, w)

polyfit = (lambda x, y, deg, rcond, full, w, cov = (None, False, None, False): order = int(deg) + 1x = NX.asarray(x) + 0y = NX.asarray(y) + 0if deg < 0:
raise ValueError('expected deg >= 0')if x.ndim != 1:
raise TypeError('expected 1D vector for x')if x.size == 0:
raise TypeError('expected non-empty vector for x')if y.ndim < 1 or y.ndim > 2:
raise TypeError('expected 1D or 2D array for y')if x.shape[0] != y.shape[0]:
raise TypeError('expected x and y to have same length')# WARNING: Decompyle incomplete
)()

def _polyval_dispatcher(p, x):
    return (p, x)

polyval = (lambda p, x: p = NX.asarray(p)if isinstance(x, poly1d):
y = 0else:
x = NX.asanyarray(x)y = NX.zeros_like(x)for pv in p:
y = y * x + pvy)()

def _binary_op_dispatcher(a1, a2):
    return (a1, a2)

polyadd = (lambda a1, a2: if not isinstance(a1, poly1d):
truepoly = isinstance(a2, poly1d)a1 = atleast_1d(a1)a2 = atleast_1d(a2)diff = len(a2) - len(a1)if diff == 0:
val = a1 + a2elif diff > 0:
zr = NX.zeros(diff, a1.dtype)val = NX.concatenate((zr, a1)) + a2else:
zr = NX.zeros(abs(diff), a2.dtype)val = a1 + NX.concatenate((zr, a2))if truepoly:
val = poly1d(val)val)()
polysub = (lambda a1, a2: if not isinstance(a1, poly1d):
truepoly = isinstance(a2, poly1d)a1 = atleast_1d(a1)a2 = atleast_1d(a2)diff = len(a2) - len(a1)if diff == 0:
val = a1 - a2elif diff > 0:
zr = NX.zeros(diff, a1.dtype)val = NX.concatenate((zr, a1)) - a2else:
zr = NX.zeros(abs(diff), a2.dtype)val = a1 - NX.concatenate((zr, a2))if truepoly:
val = poly1d(val)val)()
polymul = (lambda a1, a2: if not isinstance(a1, poly1d):
truepoly = isinstance(a2, poly1d)a2 = poly1d(a2)a1 = poly1d(a1)val = NX.convolve(a1, a2)if truepoly:
val = poly1d(val)val)()

def _polydiv_dispatcher(u, v):
    return (u, v)

polydiv = (lambda u, v: pass# WARNING: Decompyle incomplete
)()
_poly_mat = re.compile('\\*\\*([0-9]*)')

def _raise_power(astr, wrap = (70,)):
    n = 0
    line1 = ''
    line2 = ''
    output = ' '
    mat = _poly_mat.search(astr, n)
# WARNING: Decompyle incomplete

poly1d = <NODE:12>()
warnings.simplefilter('always', RankWarning)
