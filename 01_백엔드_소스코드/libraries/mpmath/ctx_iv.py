# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ctx_iv.pyc (Python 3.11)

import operator
from  import libmp
from libmp.backend import basestring
from libmp import int_types, MPZ_ONE, prec_to_dps, dps_to_prec, repr_dps, round_floor, round_ceiling, fzero, finf, fninf, fnan, mpf_le, mpf_neg, from_int, from_float, from_str, from_rational, mpi_mid, mpi_delta, mpi_str, mpi_abs, mpi_pos, mpi_neg, mpi_add, mpi_sub, mpi_mul, mpi_div, mpi_pow_int, mpi_pow, mpi_from_str, mpci_pos, mpci_neg, mpci_add, mpci_sub, mpci_mul, mpci_div, mpci_pow, mpci_abs, mpci_pow, mpci_exp, mpci_log, ComplexResult, mpf_hash, mpc_hash
from matrices.matrices import _matrix
mpi_zero = (fzero, fzero)
from ctx_base import StandardBaseContext
new = object.__new__

def convert_mpf_(x, prec, rounding):
    if hasattr(x, '_mpf_'):
        return x._mpf_
    if None(x, int_types):
        return from_int(x, prec, rounding)
    if None(x, float):
        return from_float(x, prec, rounding)
    if None(x, basestring):
        return from_str(x, prec, rounding)
    raise None


class ivmpf(object):
    '''
    Interval arithmetic class. Precision is controlled by iv.prec.
    '''
    
    def __new__(cls, x = (0,)):
        return cls.ctx.convert(x)

    
    def cast(self, cls, f_convert):
        (a, b) = self._mpi_
        if a == b:
            return cls(f_convert(a))
        raise None

    
    def __int__(self):
        return self.cast(int, libmp.to_int)

    
    def __float__(self):
        return self.cast(float, libmp.to_float)

    
    def __complex__(self):
        return self.cast(complex, libmp.to_float)

    
    def __hash__(self):
        (a, b) = self._mpi_
        if a == b:
            return mpf_hash(a)
        return None(self._mpi_)

    real = (lambda self: self)()
    imag = (lambda self: self.ctx.zero)()
    
    def conjugate(self):
        return self

    a = (lambda self: (a, b) = self._mpi_self.ctx.make_mpf((a, a)))()
    b = (lambda self: (a, b) = self._mpi_self.ctx.make_mpf((b, b)))()
    mid = (lambda self: ctx = self.ctxv = mpi_mid(self._mpi_, ctx.prec)ctx.make_mpf((v, v)))()
    delta = (lambda self: ctx = self.ctxv = mpi_delta(self._mpi_, ctx.prec)ctx.make_mpf((v, v)))()
    _mpci_ = (lambda self: (self._mpi_, mpi_zero))()
    
    def _compare(*args):
        raise TypeError('no ordering relation is defined for intervals')

    __gt__ = _compare
    __le__ = _compare
    __gt__ = _compare
    __ge__ = _compare
    
    def __contains__(self, t):
