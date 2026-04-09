# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _methods.pyc (Python 3.11)

'''
Array methods which are called by both the C-code for the method
and the Python code for the NumPy-namespace function

'''
import warnings
from contextlib import nullcontext
from numpy.core import multiarray as mu
from numpy.core import umath as um
from numpy.core.multiarray import asanyarray
from numpy.core import numerictypes as nt
from numpy.core import _exceptions
from numpy.core._ufunc_config import _no_nep50_warning
from numpy._globals import _NoValue
from numpy.compat import pickle, os_fspath
umr_maximum = um.maximum.reduce
umr_minimum = um.minimum.reduce
umr_sum = um.add.reduce
umr_prod = um.multiply.reduce
umr_any = um.logical_or.reduce
umr_all = um.logical_and.reduce
_complex_to_float = {
    nt.dtype(nt.cdouble): nt.dtype(nt.double),
    nt.dtype(nt.csingle): nt.dtype(nt.single) }
if nt.dtype(nt.longdouble) != nt.dtype(nt.double):
    _complex_to_float.update({
        nt.dtype(nt.clongdouble): nt.dtype(nt.longdouble) })

def _amax(a, axis, out, keepdims, initial, where = (None, None, False, _NoValue, True)):
    return umr_maximum(a, axis, None, out, keepdims, initial, where)


def _amin(a, axis, out, keepdims, initial, where = (None, None, False, _NoValue, True)):
    return umr_minimum(a, axis, None, out, keepdims, initial, where)


def _sum(a, axis, dtype, out, keepdims, initial, where = (None, None, None, False, _NoValue, True)):
    return umr_sum(a, axis, dtype, out, keepdims, initial, where)


def _prod(a, axis, dtype, out, keepdims, initial, where = (None, None, None, False, _NoValue, True)):
    return umr_prod(a, axis, dtype, out, keepdims, initial, where)


def _any(a, axis, dtype = None, out = (None, None, None, False), keepdims = {
    'where': True }, *, where):
    if where is True:
        return umr_any(a, axis, dtype, out, keepdims)
    return None(a, axis, dtype, out, keepdims, where = where)


def _all(a, axis, dtype = None, out = (None, None, None, False), keepdims = {
    'where': True }, *, where):
    if where is True:
        return umr_all(a, axis, dtype, out, keepdims)
    return None(a, axis, dtype, out, keepdims, where = where)


def _count_reduce_items(arr, axis, keepdims, where = (False, True)):
    pass
# WARNING: Decompyle incomplete


def _clip(a, min, max, out = (None, None, None), **kwargs):
    pass
# WARNING: Decompyle incomplete


def _mean(a, axis, dtype = None, out = (None, None, None, False), keepdims = {
    'where': True }, *, where):
    arr = asanyarray(a)
    is_float16_result = False
    rcount = _count_reduce_items(arr, axis, keepdims = keepdims, where = where)
    if where is True or rcount == 0:
        pass
    elif umr_any(rcount == 0, axis = None):
        warnings.warn('Mean of empty slice.', RuntimeWarning, stacklevel = 2)
# WARNING: Decompyle incomplete


def _var(a, axis, dtype, out = None, ddof = (None, None, None, 0, False), keepdims = {
    'where': True }, *, where):
    arr = asanyarray(a)
    rcount = _count_reduce_items(arr, axis, keepdims = keepdims, where = where)
    if where is True or ddof >= rcount:
        pass
    elif umr_any(ddof >= rcount, axis = None):
        warnings.warn('Degrees of freedom <= 0 for slice', RuntimeWarning, stacklevel = 2)
# WARNING: Decompyle incomplete


def _std(a, axis, dtype, out = None, ddof = (None, None, None, 0, False), keepdims = {
    'where': True }, *, where):
    ret = _var(a, axis = axis, dtype = dtype, out = out, ddof = ddof, keepdims = keepdims, where = where)
    if isinstance(ret, mu.ndarray):
        ret = um.sqrt(ret, out = ret)
    elif hasattr(ret, 'dtype'):
        ret = ret.dtype.type(um.sqrt(ret))
    else:
        ret = um.sqrt(ret)
    return ret


def _ptp(a, axis, out, keepdims = (None, None, False)):
    return um.subtract(umr_maximum(a, axis, None, out, keepdims), umr_minimum(a, axis, None, None, keepdims), out)


def _dump(self, file, protocol = (2,)):
    if hasattr(file, 'write'):
        ctx = nullcontext(file)
    else:
        ctx = open(os_fspath(file), 'wb')
    f = ctx
    pickle.dump(self, f, protocol = protocol)
    None(None, None)
    return None
    with None:
        if not None:
            pass


def _dumps(self, protocol = (2,)):
    return pickle.dumps(self, protocol = protocol)
