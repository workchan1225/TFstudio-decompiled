# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: type_check.pyc (Python 3.11)

__doc__ = 'Automatically adapted for numpy Sep 19, 2005 by convertcode.py\n\n'
import functools
__all__ = [
    'iscomplexobj',
    'isrealobj',
    'imag',
    'iscomplex',
    'isreal',
    'nan_to_num',
    'real',
    'real_if_close',
    'typename',
    'asfarray',
    'mintypecode',
    'common_type']
from _utils import set_module

numeric
from numpy.core.numeric import asarray, asanyarray, isnan, zeros
asanyarray = asanyarray
isnan = isnan
zeros = zeros
import numpy.core.numeric, core
from numpy.core import overrides, getlimits
from ufunclike import isneginf, isposinf
array_function_dispatch = functools.partial(overrides.array_function_dispatch, module = 'numpy')
_typecodes_by_elsize = 'GDFgdfQqLlIiHhBb?'
mintypecode = (lambda typechars, typeset, default = ('GDFgdf', 'd'): pass# WARNING: Decompyle incomplete
)()

def _asfarray_dispatcher(a, dtype = (None,)):
    return (a,)

asfarray = (lambda a, dtype = (_nx.float_,): if not _nx.issubdtype(dtype, _nx.inexact):
dtype = _nx.float_asarray(a, dtype = dtype))()

def _real_dispatcher(val):
    return (val,)

real = (lambda val: try:
val.realexcept AttributeError:
)()

def _imag_dispatcher(val):
    return (val,)

imag = (lambda val: try:
val.imagexcept AttributeError:
)()

def _is_type_dispatcher(x):
    return (x,)

iscomplex = (lambda x: ax = asanyarray(x)if issubclass(ax.dtype.type, _nx.complexfloating):
ax.imag != 0res = None(ax.shape, bool)res[()])()
isreal = (lambda x: imag(x) == 0)()
iscomplexobj = (lambda x: try:
dtype = x.dtypetype_ = dtype.typeexcept AttributeError:
type_ = asarray(x).dtype.typeissubclass(type_, _nx.complexfloating))()
isrealobj = (lambda x: not iscomplexobj(x))()

def _getmaxmin(t):
    getlimits = getlimits
    import numpy.core
    f = getlimits.finfo(t)
    return (f.max, f.min)


def _nan_to_num_dispatcher(x, copy, nan, posinf, neginf = (None, None, None, None)):
    return (x,)

nan_to_num = (lambda x, copy, nan, posinf, neginf = (True, 0, None, None): x = _nx.array(x, subok = True, copy = copy)xtype = x.dtype.typeisscalar = x.ndim == 0if not issubclass(xtype, _nx.inexact):
x[()] if isscalar else xiscomplex = None(xtype, _nx.complexfloating)dest = (x.real, x.imag) if iscomplex else (x,)(maxf, minf) = _getmaxmin(x.real.dtype)# WARNING: Decompyle incomplete
)()

def _real_if_close_dispatcher(a, tol = (None,)):
    return (a,)

real_if_close = (lambda a, tol = (100,): a = asanyarray(a)type_ = a.dtype.typeif not issubclass(type_, _nx.complexfloating):
aif None > 1:
f = getlimits.finfo(type_)tol = f.eps * tolif _nx.all(_nx.absolute(a.imag) < tol):
a = a.reala)()
# WARNING: Decompyle incomplete
