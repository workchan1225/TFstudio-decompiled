# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ctx_mp_python.pyc (Python 3.11)

from libmp.backend import basestring, exec_
from libmp import MPZ, MPZ_ZERO, MPZ_ONE, int_types, repr_dps, round_floor, round_ceiling, dps_to_prec, round_nearest, prec_to_dps, ComplexResult, to_pickable, from_pickable, normalize, from_int, from_float, from_npfloat, from_Decimal, from_str, to_int, to_float, to_str, from_rational, from_man_exp, fone, fzero, finf, fninf, fnan, mpf_abs, mpf_pos, mpf_neg, mpf_add, mpf_sub, mpf_mul, mpf_mul_int, mpf_div, mpf_rdiv_int, mpf_pow_int, mpf_mod, mpf_eq, mpf_cmp, mpf_lt, mpf_gt, mpf_le, mpf_ge, mpf_hash, mpf_rand, mpf_sum, bitcount, to_fixed, mpc_to_str, mpc_to_complex, mpc_hash, mpc_pos, mpc_is_nonzero, mpc_neg, mpc_conjugate, mpc_abs, mpc_add, mpc_add_mpf, mpc_sub, mpc_sub_mpf, mpc_mul, mpc_mul_mpf, mpc_mul_int, mpc_div, mpc_div_mpf, mpc_pow, mpc_pow_mpf, mpc_pow_int, mpc_mpf_div, mpf_pow, mpf_pi, mpf_degree, mpf_e, mpf_phi, mpf_ln2, mpf_ln10, mpf_euler, mpf_catalan, mpf_apery, mpf_khinchin, mpf_glaisher, mpf_twinprime, mpf_mertens, int_types
from  import rational
from  import function_docs
new = object.__new__

class mpnumeric(object):
    '''Base class for mpf and mpc.'''
    __slots__ = []
    
    def __new__(cls, val):
        raise NotImplementedError



class _mpf(mpnumeric):
    '''
    An mpf instance holds a real-valued floating-point number. mpf:s
    work analogously to Python floats, but support arbitrary-precision
    arithmetic.
    '''
    __slots__ = [
        '_mpf_']
    
    def __new__(cls, val = (fzero,), **kwargs):
        '''A new mpf can be created from a Python float, an int, a
        or a decimal string representing a number in floating-point
        format.'''
        (prec, rounding) = cls.context._prec_rounding
        if kwargs:
            prec = kwargs.get('prec', prec)
            if 'dps' in kwargs:
                prec = dps_to_prec(kwargs['dps'])
            rounding = kwargs.get('rounding', rounding)
        if type(val) is cls:
            (sign, man, exp, bc) = val._mpf_
            if man and exp:
                return val
            v = None(cls)
            v._mpf_ = normalize(sign, man, exp, bc, prec, rounding)
            return v
        if None(val) is tuple:
            if len(val) == 2:
                v = new(cls)
                v._mpf_ = from_man_exp(val[0], val[1], prec, rounding)
                return v
            if None(val) == 4:
                if val not in (finf, fninf, fnan):
                    (sign, man, exp, bc) = val
                    val = normalize(sign, MPZ(man), exp, bc, prec, rounding)
                v = new(cls)
                v._mpf_ = val
                return v
            raise None
        v = new(cls)
        v._mpf_ = mpf_pos(cls.mpf_convert_arg(val, prec, rounding), prec, rounding)
        return v

    mpf_convert_arg = (lambda cls, x, prec, rounding: if isinstance(x, int_types):
from_int(x)if None(x, float):
from_float(x)if None(x, basestring):
from_str(x, prec, rounding)if None(x, cls.context.constant):
x.func(prec, rounding)if None(x, '_mpf_'):
x._mpf_if None(x, '_mpmath_'):
t = cls.context.convert(x._mpmath_(prec, rounding))if hasattr(t, '_mpf_'):
t._mpf_if None(x, '_mpi_'):
(a, b) = x._mpi_if a == b:
araise None('can only create mpf from zero-width interval')raise TypeError('cannot create mpf from ' + repr(x)))()
    mpf_convert_rhs = (lambda cls, x: if isinstance(x, int_types):
from_int(x)if None(x, float):
from_float(x)if None(x, complex_types):
cls.context.mpc(x)if None(x, rational.mpq):
(p, q) = x._mpq_from_rational(p, q, cls.context.prec)if None(x, '_mpf_'):
x._mpf_# WARNING: Decompyle incomplete
)()
    mpf_convert_lhs = (lambda cls, x: x = cls.mpf_convert_rhs(x)if type(x) is tuple:
cls.context.make_mpf(x))()
    man_exp = property((lambda self: self._mpf_[1:3]))
    man = property((lambda self: self._mpf_[1]))
    exp = property((lambda self: self._mpf_[2]))
    bc = property((lambda self: self._mpf_[3]))
    real = property((lambda self: self))
    imag = property((lambda self: self.context.zero))
    
    conjugate = lambda self: self
    
    def __getstate__(self):
        return to_pickable(self._mpf_)

    
    def __setstate__(self, val):
        self._mpf_ = from_pickable(val)

    
    def __repr__(s):
        if s.context.pretty:
            return str(s)
        return None % to_str(s._mpf_, s.context._repr_digits)

    
    def __str__(s):
        return to_str(s._mpf_, s.context._str_digits)

    
    def __hash__(s):
        return mpf_hash(s._mpf_)

    
    def __int__(s):
        return int(to_int(s._mpf_))

    
    def __long__(s):
        return long(to_int(s._mpf_))

    
    def __float__(s):
        return to_float(s._mpf_, rnd = s.context._prec_rounding[1])

    
    def __complex__(s):
        return complex(float(s))

    
    def __nonzero__(s):
        return s._mpf_ != fzero

    __bool__ = __nonzero__
    
    def __abs__(s):
        (prec, rounding) = (cls, new)
        v = new(cls)
        v._mpf_ = mpf_abs(s._mpf_, prec, rounding)
        return v

    
    def __pos__(s):
        (prec, rounding) = (cls, new)
        v = new(cls)
        v._mpf_ = mpf_pos(s._mpf_, prec, rounding)
        return v

    
    def __neg__(s):
        (prec, rounding) = (cls, new)
        v = new(cls)
        v._mpf_ = mpf_neg(s._mpf_, prec, rounding)
        return v

    
    def _cmp(s, t, func):
