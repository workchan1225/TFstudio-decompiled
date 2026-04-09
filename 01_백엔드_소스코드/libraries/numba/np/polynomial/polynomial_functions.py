# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: polynomial_functions.pyc (Python 3.11)

'''
Implementation of operations involving polynomials.
'''
import numpy as np
from numpy.polynomial import polynomial as poly
from numpy.polynomial import polyutils as pu
from numba import literal_unroll
from numba.core import types, errors
from numba.core.extending import overload
from numba.np.numpy_support import type_can_asarray, as_dtype, from_dtype
roots_impl = (lambda p: pass# WARNING: Decompyle incomplete
)()
polyutils_trimseq = (lambda seq: if not type_can_asarray(seq):
msg = 'The argument "seq" must be array-like'raise errors.TypingError(msg)if isinstance(seq, types.BaseTuple):
msg = 'Unsupported type %r for argument "seq"'raise errors.TypingError(msg % seq)if np.ndim(seq) > 1:
msg = 'Coefficient array is not 1-d'raise errors.NumbaValueError(msg)
def impl(seq):
if len(seq) == 0:
seqfor i in None(len(seq) - 1, -1, -1):
if seq[i] != 0:
passseq[:i + 1]impl)()
polyutils_as_series = (lambda alist, trim = (True,): pass# WARNING: Decompyle incomplete
)()

def _get_list_type(l):
    dt = l.dtype
    if isinstance(dt, types.Number) and type_can_asarray(dt):
        return _get_list_type(dt)


def _poly_result_dtype(*args):
    res_dtype = np.float64
# WARNING: Decompyle incomplete

numpy_polyadd = (lambda c1, c2: if not type_can_asarray(c1):
msg = 'The argument "c1" must be array-like'raise errors.TypingError(msg)if not type_can_asarray(c2):
msg = 'The argument "c2" must be array-like'raise errors.TypingError(msg)
def impl(c1, c2):
(arr1, arr2) = pu.as_series((c1, c2))diff = len(arr2) - len(arr1)if diff > 0:
zr = np.zeros(diff)arr1 = np.concatenate((arr1, zr))if diff < 0:
zr = np.zeros(-diff)arr2 = np.concatenate((arr2, zr))val = arr1 + arr2pu.trimseq(val)impl)()
numpy_polysub = (lambda c1, c2: if not type_can_asarray(c1):
msg = 'The argument "c1" must be array-like'raise errors.TypingError(msg)if not type_can_asarray(c2):
msg = 'The argument "c2" must be array-like'raise errors.TypingError(msg)
def impl(c1, c2):
(arr1, arr2) = pu.as_series((c1, c2))diff = len(arr2) - len(arr1)if diff > 0:
zr = np.zeros(diff)arr1 = np.concatenate((arr1, zr))if diff < 0:
zr = np.zeros(-diff)arr2 = np.concatenate((arr2, zr))val = arr1 - arr2pu.trimseq(val)impl)()
numpy_polymul = (lambda c1, c2: if not type_can_asarray(c1):
msg = 'The argument "c1" must be array-like'raise errors.TypingError(msg)if not type_can_asarray(c2):
msg = 'The argument "c2" must be array-like'raise errors.TypingError(msg)
def impl(c1, c2):
(arr1, arr2) = pu.as_series((c1, c2))val = np.convolve(arr1, arr2)pu.trimseq(val)impl)()
poly_polyval = (lambda x, c, tensor = (True,): pass# WARNING: Decompyle incomplete
)()
poly_polyint = (lambda c, m = (1,): pass# WARNING: Decompyle incomplete
)()
numpy_polydiv = (lambda c1, c2: if not type_can_asarray(c1):
msg = 'The argument "c1" must be array-like'raise errors.TypingError(msg)if not type_can_asarray(c2):
msg = 'The argument "c2" must be array-like'raise errors.TypingError(msg)
def impl(c1, c2):
(arr1, arr2) = pu.as_series((c1, c2))if arr2[-1] == 0:
raise ZeroDivisionError()l1 = len(arr1)l2 = len(arr2)if l1 < l2:
(arr1[:1] * 0, arr1)if None == 1:
(arr1 / arr2[-1], arr1[:1] * 0)dlen = None - l2scl = arr2[-1]arr2 = arr2[:-1] / scli = dlenj = l1 - 1# WARNING: Decompyle incomplete
impl)()
