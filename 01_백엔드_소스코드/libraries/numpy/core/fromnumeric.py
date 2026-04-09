# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fromnumeric.pyc (Python 3.11)

'''Module containing non-deprecated functions borrowed from Numeric.

'''
import functools
import types
import warnings
import numpy as np
from _utils import set_module
from  import multiarray as mu
from  import overrides
from  import umath as um
from  import numerictypes as nt
from multiarray import asarray, array, asanyarray, concatenate
from  import _methods
_dt_ = nt.sctype2char
__all__ = [
    'all',
    'alltrue',
    'amax',
    'amin',
    'any',
    'argmax',
    'argmin',
    'argpartition',
    'argsort',
    'around',
    'choose',
    'clip',
    'compress',
    'cumprod',
    'cumproduct',
    'cumsum',
    'diagonal',
    'mean',
    'max',
    'min',
    'ndim',
    'nonzero',
    'partition',
    'prod',
    'product',
    'ptp',
    'put',
    'ravel',
    'repeat',
    'reshape',
    'resize',
    'round',
    'round_',
    'searchsorted',
    'shape',
    'size',
    'sometrue',
    'sort',
    'squeeze',
    'std',
    'sum',
    'swapaxes',
    'take',
    'trace',
    'transpose',
    'var']
_gentype = types.GeneratorType
_sum_ = sum
array_function_dispatch = functools.partial(overrides.array_function_dispatch, module = 'numpy')

def _wrapit(obj, method, *args, **kwds):
    
    try:
        wrap = obj.__array_wrap__
    except AttributeError:
        wrap = None

# WARNING: Decompyle incomplete


def _wrapfunc(obj, method, *args, **kwds):
    bound = getattr(obj, method, None)
# WARNING: Decompyle incomplete


def _wrapreduction(obj, ufunc, method, axis, dtype, out, **kwargs):
    passkwargs = kwargs.items()()
# WARNING: Decompyle incomplete


def _take_dispatcher(a, indices, axis, out, mode = (None, None, None)):
    return (a, out)

take = (lambda a, indices, axis, out, mode = (None, None, 'raise'): _wrapfunc(a, 'take', indices, axis = axis, out = out, mode = mode))()

def _reshape_dispatcher(a, newshape, order = (None,)):
    return (a,)

reshape = (lambda a, newshape, order = ('C',): _wrapfunc(a, 'reshape', newshape, order = order))()

def _choose_dispatcher(a, choices, out, mode = (None, None)):
    pass
# WARNING: Decompyle incomplete

choose = (lambda a, choices, out, mode = (None, 'raise'): _wrapfunc(a, 'choose', choices, out = out, mode = mode))()

def _repeat_dispatcher(a, repeats, axis = (None,)):
    return (a,)

repeat = (lambda a, repeats, axis = (None,): _wrapfunc(a, 'repeat', repeats, axis = axis))()

def _put_dispatcher(a, ind, v, mode = (None,)):
    return (a, ind, v)

put = (lambda a, ind, v, mode = ('raise',): try:
put = a.putexcept AttributeError:
e = Noneraise TypeError('argument 1 must be numpy.ndarray, not {name}'.format(name = type(a).__name__)), ee = Nonedel eput(ind, v, mode = mode))()

def _swapaxes_dispatcher(a, axis1, axis2):
    return (a,)

swapaxes = (lambda a, axis1, axis2: _wrapfunc(a, 'swapaxes', axis1, axis2))()

def _transpose_dispatcher(a, axes = (None,)):
    return (a,)

transpose = (lambda a, axes = (None,): _wrapfunc(a, 'transpose', axes))()

def _partition_dispatcher(a, kth, axis, kind, order = (None, None, None)):
    return (a,)

partition = (lambda a, kth, axis, kind, order = (-1, 'introselect', None): pass# WARNING: Decompyle incomplete
)()

def _argpartition_dispatcher(a, kth, axis, kind, order = (None, None, None)):
    return (a,)

argpartition = (lambda a, kth, axis, kind, order = (-1, 'introselect', None): _wrapfunc(a, 'argpartition', kth, axis = axis, kind = kind, order = order))()

def _sort_dispatcher(a, axis, kind, order = (None, None, None)):
    return (a,)

sort = (lambda a, axis, kind, order = (-1, None, None): pass# WARNING: Decompyle incomplete
)()

def _argsort_dispatcher(a, axis, kind, order = (None, None, None)):
    return (a,)

argsort = (lambda a, axis, kind, order = (-1, None, None): _wrapfunc(a, 'argsort', axis = axis, kind = kind, order = order))()

def _argmax_dispatcher(a = array_function_dispatch(_argsort_dispatcher), axis = (None, None), out = {
    'keepdims': np._NoValue }, *, keepdims):
    return (a, out)

argmax = (lambda a = array_function_dispatch(_argmax_dispatcher), axis = (None, None), out = {
    'keepdims': np._NoValue }, *, keepdims, kwds = None,
