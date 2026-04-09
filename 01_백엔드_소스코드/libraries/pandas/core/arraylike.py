# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: arraylike.pyc (Python 3.11)

'''
Methods that can be shared by many array-like classes or subclasses:
    Series
    Index
    ExtensionArray
'''
from __future__ import annotations
import operator
from typing import Any
import numpy as np
from pandas._libs import lib
from pandas._libs.ops_dispatch import maybe_dispatch_ufunc_to_dunder_op
from pandas.core.dtypes.cast import maybe_unbox_numpy_scalar
from pandas.core.dtypes.generic import ABCNDFrame
from pandas.core import roperator
from pandas.core.construction import extract_array
from pandas.core.ops.common import unpack_zerodim_and_defer
REDUCTION_ALIASES = {
    'maximum': 'max',
    'minimum': 'min',
    'add': 'sum',
    'multiply': 'prod' }

class OpsMixin:
    
    def _cmp_method(self, other, op):
        return NotImplemented

    __eq__ = (lambda self, other: self._cmp_method(other, operator.eq))()
    __ne__ = (lambda self, other: self._cmp_method(other, operator.ne))()
    __lt__ = (lambda self, other: self._cmp_method(other, operator.lt))()
    __le__ = (lambda self, other: self._cmp_method(other, operator.le))()
    __gt__ = (lambda self, other: self._cmp_method(other, operator.gt))()
    __ge__ = (lambda self, other: self._cmp_method(other, operator.ge))()
    
    def _logical_method(self, other, op):
        return NotImplemented

    __and__ = (lambda self, other: self._logical_method(other, operator.and_))()
    __rand__ = (lambda self, other: self._logical_method(other, roperator.rand_))()
    __or__ = (lambda self, other: self._logical_method(other, operator.or_))()
    __ror__ = (lambda self, other: self._logical_method(other, roperator.ror_))()
    __xor__ = (lambda self, other: self._logical_method(other, operator.xor))()
    __rxor__ = (lambda self, other: self._logical_method(other, roperator.rxor))()
    
    def _arith_method(self, other, op):
        return NotImplemented

    __add__ = (lambda self, other: self._arith_method(other, operator.add))()
    __radd__ = (lambda self, other: self._arith_method(other, roperator.radd))()
    __sub__ = (lambda self, other: self._arith_method(other, operator.sub))()
    __rsub__ = (lambda self, other: self._arith_method(other, roperator.rsub))()
    __mul__ = (lambda self, other: self._arith_method(other, operator.mul))()
    __rmul__ = (lambda self, other: self._arith_method(other, roperator.rmul))()
    __truediv__ = (lambda self, other: self._arith_method(other, operator.truediv))()
    __rtruediv__ = (lambda self, other: self._arith_method(other, roperator.rtruediv))()
    __floordiv__ = (lambda self, other: self._arith_method(other, operator.floordiv))()
    __rfloordiv__ = (lambda self, other: self._arith_method(other, roperator.rfloordiv))()
    __mod__ = (lambda self, other: self._arith_method(other, operator.mod))()
    __rmod__ = (lambda self, other: self._arith_method(other, roperator.rmod))()
    __divmod__ = (lambda self, other: self._arith_method(other, divmod))()
    __rdivmod__ = (lambda self, other: self._arith_method(other, roperator.rdivmod))()
    __pow__ = (lambda self, other: self._arith_method(other, operator.pow))()
    __rpow__ = (lambda self, other: self._arith_method(other, roperator.rpow))()


def array_ufunc(self = None, ufunc = None, method = None, *inputs, **kwargs):
    '''
    Compatibility with numpy ufuncs.

    See also
    --------
    numpy.org/doc/stable/reference/arrays.classes.html#numpy.class.__array_ufunc__
    '''
    pass
# WARNING: Decompyle incomplete


def _standardize_out_kwarg(**kwargs):
    '''
    If kwargs contain "out1" and "out2", replace that with a tuple "out"

    np.divmod, np.modf, np.frexp can have either `out=(out1, out2)` or
    `out1=out1, out2=out2)`
    '''
    if 'out' not in kwargs and 'out1' in kwargs and 'out2' in kwargs:
        out1 = kwargs.pop('out1')
        out2 = kwargs.pop('out2')
        out = (out1, out2)
        kwargs['out'] = out
    return kwargs


def dispatch_ufunc_with_out(self = None, ufunc = None, method = None, *inputs, **kwargs):
    '''
    If we have an `out` keyword, then call the ufunc without `out` and then
    set the result into the given `out`.
    '''
    out = kwargs.pop('out')
    where = kwargs.pop('where', None)
# WARNING: Decompyle incomplete


def _assign_where(out = None, result = None, where = None):
    """
    Set a ufunc result into 'out', masking with a 'where' argument if necessary.
    """
    pass
# WARNING: Decompyle incomplete


def default_array_ufunc(self = None, ufunc = None, method = None, *inputs, **kwargs):
    '''
    Fallback to the behavior we would get if we did not define __array_ufunc__.

    Notes
    -----
    We are assuming that `self` is among `inputs`.
    '''
    pass
# WARNING: Decompyle incomplete


def dispatch_reduction_ufunc(self = None, ufunc = None, method = None, *inputs, **kwargs):
    """
    Dispatch ufunc reductions to self's reduction methods.
    """
    pass
# WARNING: Decompyle incomplete
