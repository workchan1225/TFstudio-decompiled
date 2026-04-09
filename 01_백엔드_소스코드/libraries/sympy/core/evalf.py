# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: evalf.pyc (Python 3.11)

'''
Adaptive numerical evaluation of SymPy expressions, using mpmath
for mathematical functions.
'''
from __future__ import annotations
from typing import Tuple as tTuple, Optional, Union as tUnion, Callable, List, Dict as tDict, Type, TYPE_CHECKING, Any, overload
import math
from mpmath.libmp import libmp
from mpmath import make_mpc, make_mpf, mp, mpc, mpf, nsum, quadts, quadosc, workprec
from mpmath import inf as mpmath_inf
from mpmath.libmp import from_int, from_man_exp, from_rational, fhalf, fnan, finf, fninf, fnone, fone, fzero, mpf_abs, mpf_add, mpf_atan, mpf_atan2, mpf_cmp, mpf_cos, mpf_e, mpf_exp, mpf_log, mpf_lt, mpf_mul, mpf_neg, mpf_pi, mpf_pow, mpf_pow_int, mpf_shift, mpf_sin, mpf_sqrt, normalize, round_nearest, to_int, to_str
from mpmath.libmp import bitcount as mpmath_bitcount
from mpmath.libmp.backend import MPZ
from mpmath.libmp.libmpc import _infs_nan
from mpmath.libmp.libmpf import dps_to_prec, prec_to_dps
from sympify import sympify
from singleton import S
from sympy.external.gmpy import SYMPY_INTS
from sympy.utilities.iterables import is_sequence
from sympy.utilities.lambdify import lambdify
from sympy.utilities.misc import as_int
if TYPE_CHECKING:
    from sympy.core.expr import Expr
    from sympy.core.add import Add
    from sympy.core.mul import Mul
    from sympy.core.power import Pow
    from sympy.core.symbol import Symbol
    from sympy.integrals.integrals import Integral
    from sympy.concrete.summations import Sum
    from sympy.concrete.products import Product
    from sympy.functions.elementary.exponential import exp, log
    from sympy.functions.elementary.complexes import Abs, re, im
    from sympy.functions.elementary.integers import ceiling, floor
    from sympy.functions.elementary.trigonometric import atan
    from numbers import Float, Rational, Integer, AlgebraicNumber, Number
LG10 = math.log2(10)
rnd = round_nearest

def bitcount(n):
    '''Return smallest integer, b, such that |n|/2**b < 1.
    '''
    return mpmath_bitcount(abs(int(n)))

INF = float(mpmath_inf)
MINUS_INF = float(-mpmath_inf)
DEFAULT_MAXPREC = 333

class PrecisionExhausted(ArithmeticError):
    pass

MPF_TUP = tTuple[(int, int, int, int)]
TMP_RES = Any
OPT_DICT = tDict[(str, Any)]

def fastlog(x = None):
    '''Fast approximation of log2(x) for an mpf value tuple x.

    Explanation
    ===========

    Calculated as exponent + width of mantissa. This is an
    approximation for two reasons: 1) it gives the ceil(log2(abs(x)))
    value and 2) it is too high by 1 in the case that x is an exact
    power of 2. Although this is easy to remedy by testing to see if
    the odd mpf mantissa is 1 (indicating that one was dealing with
    an exact power of 2) that would decrease the speed and is not
    necessary as this is only being used as an approximation for the
    number of bits in x. The correct return value could be written as
    "x[2] + (x[3] if x[1] != 1 else 0)".
        Since mpf tuples always have an odd mantissa, no check is done
    to see if the mantissa is a multiple of 2 (in which case the
    result would be too large by 1).

    Examples
    ========

    >>> from sympy import log
    >>> from sympy.core.evalf import fastlog, bitcount
    >>> s, m, e = 0, 5, 1
    >>> bc = bitcount(m)
    >>> n = [1, -1][s]*m*2**e
    >>> n, (log(n)/log(2)).evalf(2), fastlog((s, m, e, bc))
    (10, 3.3, 4)
    '''
    if x or x == fzero:
        return MINUS_INF
    return None[2] + x[3]


def pure_complex(v = None, or_real = None):
    '''Return a and b if v matches a + I*b where b is not zero and
    a and b are Numbers, else None. If `or_real` is True then 0 will
    be returned for `b` if `v` is a real number.

    Examples
    ========

    >>> from sympy.core.evalf import pure_complex
    >>> from sympy import sqrt, I, S
    >>> a, b, surd = S(2), S(3), sqrt(2)
    >>> pure_complex(a)
    >>> pure_complex(a, or_real=True)
    (2, 0)
    >>> pure_complex(surd)
    >>> pure_complex(a + b*I)
    (2, 3)
    >>> pure_complex(I)
    (0, 1)
    '''
    (h, t) = v.as_coeff_Add()
    if t:
        (c, i) = t.as_coeff_Mul()
        if i is S.ImaginaryUnit:
            return (h, c)
    if or_real:
        return (h, S.Zero)

SCALED_ZERO_TUP = tTuple[(List[int], int, int, int)]
scaled_zero = (lambda mag = None, sign = None: pass)()
scaled_zero = (lambda mag = None, sign = None: pass)()

def scaled_zero(mag = None, sign = None):
    '''Return an mpf representing a power of two with magnitude ``mag``
    and -1 for precision. Or, if ``mag`` is a scaled_zero tuple, then just
    remove the sign from within the list that it was initially wrapped
    in.

    Examples
    ========

    >>> from sympy.core.evalf import scaled_zero
    >>> from sympy import Float
    >>> z, p = scaled_zero(100)
    >>> z, p
    (([0], 1, 100, 1), -1)
    >>> ok = scaled_zero(z)
    >>> ok
    (0, 1, 100, 1)
    >>> Float(ok)
    1.26765060022823e+30
    >>> Float(ok, p)
    0.e+30
    >>> ok, p = scaled_zero(100, -1)
    >>> Float(scaled_zero(ok), p)
    -0.e+30
    '''
    if isinstance(mag, tuple) and len(mag) == 4 and iszero(mag, scaled = True):
        return (mag[0][0],) + mag[1:]
    if None(mag, SYMPY_INTS):
        if sign not in (-1, 1):
            raise ValueError('sign must be +/-1')
        p = -1
        rv = mpf_shift(fone, mag)
        s = 0 if sign == 1 else 1
        rv = ([
            s],) + rv[1:]
        return (rv, p)
    raise None('scaled zero expects int or scaled_zero tuple.')


def iszero(mpf = None, scaled = None):
    if not scaled:
        if not not mpf:
            if not mpf[1]:
                return not mpf[-1]
            if not mpf[1]:
                if isinstance(mpf[0], list):
                    pass
    return None if  == mpf[1], mpf[-1] else None, mpf[1], mpf[-1] == 1


def complex_accuracy(result = None):
    '''
    Returns relative accuracy of a complex number with given accuracies
    for the real and imaginary parts. The relative accuracy is defined
    in the complex norm sense as ||z|+|error|| / |z| where error
    is equal to (real absolute error) + (imag absolute error)*i.

    The full expression for the (logarithmic) error can be approximated
    easily by using the max norm to approximate the complex norm.

    In the worst case (re and im equal), this is wrong by a factor
    sqrt(2), or by log2(sqrt(2)) = 0.5 bit.
    '''
    if result is S.ComplexInfinity:
        return INF
    (re, im, re_acc, im_acc) = None
    if not im:
        if not re:
            return INF
        return None
    if not None:
        return im_acc
    re_size = None(re)
    im_size = fastlog(im)
    absolute_error = max(re_size - re_acc, im_size - im_acc)
    relative_error = absolute_error - max(re_size, im_size)
    return -relative_error


def get_abs(expr = None, prec = None, options = None):
    result = evalf(expr, prec + 2, options)
    if result is S.ComplexInfinity:
        return (finf, None, prec, None)
    (re, im, re_acc, im_acc) = None
    if not re:
        (re, re_acc, im, im_acc) = (im, im_acc, re, re_acc)
    if im:
        if expr.is_number:
            (abs_expr, _, acc, _) = evalf(abs(N(expr, prec + 2)), prec + 2, options)
            return (abs_expr, None, acc, None)
        if None in options:
            return (libmp.mpc_abs((re, im), prec), None, re_acc, None)
        return (None(expr), None, prec, None)
    if None:
        return (mpf_abs(re), None, re_acc, None)


def get_complex_part(expr = None, no = None, prec = None, options = ('expr', "'Expr'", 'no', 'int', 'prec', 'int', 'options', 'OPT_DICT', 'return', 'TMP_RES')):
    '''no = 0 for real part, no = 1 for imaginary part'''
    workprec = prec
    i = 0
    res = evalf(expr, workprec, options)
    if res is S.ComplexInfinity:
        return (fnan, None, prec, None)
    (value, accuracy) = None[no::2]
    if value and accuracy >= prec or -value[2] > prec:
        return (value, None, accuracy, None)
    None += max(30, 2 ** i)
    i += 1
    continue


def evalf_abs(expr = None, prec = None, options = None):
    return get_abs(expr.args[0], prec, options)


def evalf_re(expr = None, prec = None, options = None):
    return get_complex_part(expr.args[0], 0, prec, options)


def evalf_im(expr = None, prec = None, options = None):
    return get_complex_part(expr.args[0], 1, prec, options)


def finalize_complex(re = None, im = None, prec = None):
    if re == fzero and im == fzero:
        raise ValueError('got complex zero with unknown accuracy')
    if re == fzero:
        return (None, im, None, prec)
    if None == fzero:
        return (re, None, prec, None)
    size_re = None(re)
    size_im = fastlog(im)
    if size_re > size_im:
        re_acc = prec
        im_acc = prec + min(-(size_re - size_im), 0)
    else:
        im_acc = prec
        re_acc = prec + min(-(size_im - size_re), 0)
    return (re, im, re_acc, im_acc)


def chop_parts(value = None, prec = None):
    '''
    Chop off tiny real or complex parts.
    '''
    if value is S.ComplexInfinity:
        return value
    (re, im, re_acc, im_acc) = None
    if re and re not in _infs_nan and fastlog(re) < -prec + 4:
        (re, re_acc) = (None, None)
    if im and im not in _infs_nan and fastlog(im) < -prec + 4:
        (im, im_acc) = (None, None)
    if re and im:
        delta = fastlog(re) - fastlog(im)
        if re_acc < 2 and delta - re_acc <= -prec + 4:
            (re, re_acc) = (None, None)
        if im_acc < 2 and delta - im_acc >= prec - 4:
            (im, im_acc) = (None, None)
    return (re, im, re_acc, im_acc)


def check_target(expr = None, result = None, prec = None):
    a = complex_accuracy(result)
    if a < prec:
        raise PrecisionExhausted('Failed to distinguish the expression: \n\n%s\n\nfrom zero. Try simplifying the input, using chop=True, or providing a higher maxn for evalf' % expr)


def get_integer_part(expr = None, no = None, options = None, return_ints = (False,)):
    '''
    With no = 1, computes ceiling(expr)
    With no = -1, computes floor(expr)

    Note: this function either gives the exact result or signals failure.
    '''
    pass
# WARNING: Decompyle incomplete


def evalf_ceiling(expr = None, prec = None, options = None):
    return get_integer_part(expr.args[0], 1, options)


def evalf_floor(expr = None, prec = None, options = None):
    return get_integer_part(expr.args[0], -1, options)


def evalf_float(expr = None, prec = None, options = None):
    return (expr._mpf_, None, prec, None)


def evalf_rational(expr = None, prec = None, options = None):
    return (from_rational(expr.p, expr.q, prec), None, prec, None)


def evalf_integer(expr = None, prec = None, options = None):
    return (from_int(expr.p, prec), None, prec, None)


def add_terms(terms = None, prec = None, target_prec = None):
    '''
    Helper for evalf_add. Adds a list of (mpfval, accuracy) terms.

    Returns
    =======

    - None, None if there are no non-zero terms;
    - terms[0] if there is only 1 term;
    - scaled_zero if the sum of the terms produces a zero by cancellation
      e.g. mpfs representing 1 and -1 would produce a scaled zero which need
      special handling since they are not actually zero and they are purposely
      malformed to ensure that they cannot be used in anything but accuracy
      calculations;
    - a tuple that is scaled to target_prec that corresponds to the
      sum of the terms.

    The returned mpf tuple will be normalized to target_prec; the input
    prec is used to define the working precision.

    XXX explain why this is needed and why one cannot just loop using mpf_add
    '''
    terms = terms()
    if not terms:
        return (None, None)
    if (lambda .0: pass# WARNING: Decompyle incomplete
)(terms) == 1:
        return terms[0]
    special = None
    Float = Float
    import numbers
# WARNING: Decompyle incomplete


def evalf_add(v = None, prec = None, options = None):
    pass
# WARNING: Decompyle incomplete


def evalf_mul(v = None, prec = None, options = None):
    res = pure_complex(v)
    if res:
        (_, h) = res
        (im, _, im_acc, _) = evalf(h, prec, options)
        return (None, im, None, im_acc)
    args = None(v.args)
    has_zero = False
    special = []
    Float = Float
    import numbers
# WARNING: Decompyle incomplete


def evalf_pow(v = None, prec = None, options = None):
