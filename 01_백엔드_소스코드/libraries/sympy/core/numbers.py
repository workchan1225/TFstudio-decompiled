# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: numbers.pyc (Python 3.11)

from __future__ import annotations
import numbers
import decimal
import fractions
import math
from containers import Tuple
from sympify import SympifyError, _sympy_converter, sympify, _convert_numpy_types, _sympify, _is_numpy_instance
from singleton import S, Singleton
from basic import Basic
from expr import Expr, AtomicExpr
from evalf import pure_complex
from cache import cacheit, clear_cache
from decorators import _sympifyit
from intfunc import num_digits, igcd, ilcm, mod_inverse, integer_nthroot
from logic import fuzzy_not
from kind import NumberKind
from sympy.external.gmpy import SYMPY_INTS, gmpy, flint
from sympy.multipledispatch import dispatch
import mpmath
from mpmath.libmp import libmp as mlib
from mpmath.libmp import bitcount, round_nearest as rnd
from mpmath.libmp.backend import MPZ
from mpmath.libmp import mpf_pow, mpf_pi, mpf_e, phi_fixed
from mpmath.ctx_mp_python import mpnumeric
from mpmath.libmp.libmpf import finf as _mpf_inf, fninf as _mpf_ninf, fnan as _mpf_nan, fzero, _normalize as mpf_normalize, prec_to_dps, dps_to_prec
from sympy.utilities.misc import debug
from parameters import global_parameters
_LOG2 = math.log(2)

def comp(z1, z2, tol = (None,)):
    """Return a bool indicating whether the error between z1 and z2
    is $\\le$ ``tol``.

    Examples
    ========

    If ``tol`` is ``None`` then ``True`` will be returned if
    :math:`|z1 - z2|\\times 10^p \\le 5` where $p$ is minimum value of the
    decimal precision of each value.

    >>> from sympy import comp, pi
    >>> pi4 = pi.n(4); pi4
    3.142
    >>> comp(_, 3.142)
    True
    >>> comp(pi4, 3.141)
    False
    >>> comp(pi4, 3.143)
    False

    A comparison of strings will be made
    if ``z1`` is a Number and ``z2`` is a string or ``tol`` is ''.

    >>> comp(pi4, 3.1415)
    True
    >>> comp(pi4, 3.1415, '')
    False

    When ``tol`` is provided and $z2$ is non-zero and
    :math:`|z1| > 1` the error is normalized by :math:`|z1|`:

    >>> abs(pi4 - 3.14)/pi4
    0.000509791731426756
    >>> comp(pi4, 3.14, .001)  # difference less than 0.1%
    True
    >>> comp(pi4, 3.14, .0005)  # difference less than 0.1%
    False

    When :math:`|z1| \\le 1` the absolute error is used:

    >>> 1/pi4
    0.3183
    >>> abs(1/pi4 - 0.3183)/(1/pi4)
    3.07371499106316e-5
    >>> abs(1/pi4 - 0.3183)
    9.78393554684764e-6
    >>> comp(1/pi4, 0.3183, 1e-5)
    True

    To see if the absolute error between ``z1`` and ``z2`` is less
    than or equal to ``tol``, call this as ``comp(z1 - z2, 0, tol)``
    or ``comp(z1 - z2, tol=tol)``:

    >>> abs(pi4 - 3.14)
    0.00160156249999988
    >>> comp(pi4 - 3.14, 0, .002)
    True
    >>> comp(pi4 - 3.14, 0, .001)
    False
    """
    if isinstance(z2, str):
        if not pure_complex(z1, or_real = True):
            raise ValueError('when z2 is a str z1 must be a Number')
        return str(z1) == z2
    if not None:
        z2 = z1
        z1 = z2
    if not z1:
        return True
# WARNING: Decompyle incomplete


def mpf_norm(mpf, prec):
    '''Return the mpf tuple normalized appropriately for the indicated
    precision after doing a check to see if zero should be returned or
    not when the mantissa is 0. ``mpf_normlize`` always assumes that this
    is zero, but it may not be since the mantissa for mpf\'s values "+inf",
    "-inf" and "nan" have a mantissa of zero, too.

    Note: this is not intended to validate a given mpf tuple, so sending
    mpf tuples that were not created by mpmath may produce bad results. This
    is only a wrapper to ``mpf_normalize`` which provides the check for non-
    zero mpfs that have a 0 for the mantissa.
    '''
    (sign, man, expt, bc) = mpf
    if not man:
        if not bc:
            return fzero
        return None
    MPZ = MPZ
    import mpmath.libmp.backend
    rv = mpf_normalize(sign, MPZ(man), expt, bc, prec, rnd)
    return rv

_errdict = {
    'divide': False }

def seterr(divide = (False,)):
    '''
    Should SymPy raise an exception on 0/0 or return a nan?

    divide == True .... raise an exception
    divide == False ... return nan
    '''
    if _errdict['divide'] != divide:
        clear_cache()
        _errdict['divide'] = divide
        return None


def _as_integer_ratio(p):
    (neg_pow, man, expt, _) = getattr(p, '_mpf_', mpmath.mpf(p)._mpf_)
    p = [
        1,
        -1][neg_pow % 2] * man
    if expt < 0:
        q = 2 ** (-expt)
    else:
        q = 1
        p *= 2 ** expt
    return (int(p), int(q))


def _decimal_to_Rational_prec(dec):
    '''Convert an ordinary decimal instance to a Rational.'''
    if not dec.is_finite():
        raise TypeError('dec must be finite, got %s.' % dec)
    (s, d, e) = dec.as_tuple()
    prec = len(d)
    return (rv, prec)

_dig = str.maketrans(dict.fromkeys('1234567890'))

def _literal_float(s):
    '''return True if s is space-trimmed number literal else False

    Python allows underscore as digit separators: there must be a
    digit on each side. So neither a leading underscore nor a
    double underscore are valid as part of a number. A number does
    not have to precede the decimal point, but there must be a
    digit before the optional "e" or "E" that begins the signs
    exponent of the number which must be an integer, perhaps with
    underscore separators.

    SymPy allows space as a separator; if the calling routine replaces
    them with underscores then the same semantics will be enforced
    for them as for underscores: there can only be 1 *between* digits.

    We don\'t check for error from float(s) because we don\'t know
    whether s is malicious or not. A regex for this could maybe
    be written but will it be understood by most who read it?
    '''
    parts = s.split('e')
    if len(parts) > 2:
        return False
    if None(parts) == 2:
        (m, e) = parts
        if e.startswith(tuple('+-')):
            e = e[1:]
        if not e:
            return False
    e = '1'
    m = s
    parts = m.split('.')
    if len(parts) > 2:
        return False
    if None(parts) == 2:
        (i, f) = parts
    else:
        f = '1'
        i = m
    if not i and f:
        return False
    if None and i[0] in '+-':
        i = i[1:]
    if not i:
        i = '1'
    if not f:
        f = '1'
        for n in (i, f, e):
            for g in n.split('_'):
                if g or g.translate(_dig):
                    return False
                return True


class Number(AtomicExpr):
    pass
# WARNING: Decompyle incomplete


class Float(Number):
    '''Represent a floating-point number of arbitrary precision.

    Examples
    ========

    >>> from sympy import Float
    >>> Float(3.5)
    3.50000000000000
    >>> Float(3)
    3.00000000000000

    Creating Floats from strings (and Python ``int`` and ``long``
    types) will give a minimum precision of 15 digits, but the
    precision will automatically increase to capture all digits
    entered.

    >>> Float(1)
    1.00000000000000
    >>> Float(10**20)
    100000000000000000000.
    >>> Float(\'1e20\')
    100000000000000000000.

    However, *floating-point* numbers (Python ``float`` types) retain
    only 15 digits of precision:

    >>> Float(1e20)
    1.00000000000000e+20
    >>> Float(1.23456789123456789)
    1.23456789123457

    It may be preferable to enter high-precision decimal numbers
    as strings:

    >>> Float(\'1.23456789123456789\')
    1.23456789123456789

    The desired number of digits can also be specified:

    >>> Float(\'1e-3\', 3)
    0.00100
    >>> Float(100, 4)
    100.0

    Float can automatically count significant figures if a null string
    is sent for the precision; spaces or underscores are also allowed. (Auto-
    counting is only allowed for strings, ints and longs).

    >>> Float(\'123 456 789.123_456\', \'\')
    123456789.123456
    >>> Float(\'12e-3\', \'\')
    0.012
    >>> Float(3, \'\')
    3.

    If a number is written in scientific notation, only the digits before the
    exponent are considered significant if a decimal appears, otherwise the
    "e" signifies only how to move the decimal:

    >>> Float(\'60.e2\', \'\')  # 2 digits significant
    6.0e+3
    >>> Float(\'60e2\', \'\')  # 4 digits significant
    6000.
    >>> Float(\'600e-2\', \'\')  # 3 digits significant
    6.00

    Notes
    =====

    Floats are inexact by their nature unless their value is a binary-exact
    value.

    >>> approx, exact = Float(.1, 1), Float(.125, 1)

    For calculation purposes, evalf needs to be able to change the precision
    but this will not increase the accuracy of the inexact value. The
    following is the most accurate 5-digit approximation of a value of 0.1
    that had only 1 digit of precision:

    >>> approx.evalf(5)
    0.099609

    By contrast, 0.125 is exact in binary (as it is in base 10) and so it
    can be passed to Float or evalf to obtain an arbitrary precision with
    matching accuracy:

    >>> Float(exact, 5)
    0.12500
    >>> exact.evalf(20)
    0.12500000000000000000

    Trying to make a high-precision Float from a float is not disallowed,
    but one must keep in mind that the *underlying float* (not the apparent
    decimal value) is being obtained with high precision. For example, 0.3
    does not have a finite binary representation. The closest rational is
    the fraction 5404319552844595/2**54. So if you try to obtain a Float of
    0.3 to 20 digits of precision you will not see the same thing as 0.3
    followed by 19 zeros:

    >>> Float(0.3, 20)
    0.29999999999999998890

    If you want a 20-digit value of the decimal 0.3 (not the floating point
    approximation of 0.3) you should send the 0.3 as a string. The underlying
    representation is still binary but a higher precision than Python\'s float
    is used:

    >>> Float(\'0.3\', 20)
    0.30000000000000000000

    Although you can increase the precision of an existing Float using Float
    it will not increase the accuracy -- the underlying value is not changed:

    >>> def show(f): # binary rep of Float
    ...     from sympy import Mul, Pow
    ...     s, m, e, b = f._mpf_
    ...     v = Mul(int(m), Pow(2, int(e), evaluate=False), evaluate=False)
    ...     print(\'%s at prec=%s\' % (v, f._prec))
    ...
    >>> t = Float(\'0.3\', 3)
    >>> show(t)
    4915/2**14 at prec=13
    >>> show(Float(t, 20)) # higher prec, not higher accuracy
    4915/2**14 at prec=70
    >>> show(Float(t, 2)) # lower prec
    307/2**10 at prec=10

    The same thing happens when evalf is used on a Float:

    >>> show(t.evalf(20))
    4915/2**14 at prec=70
    >>> show(t.evalf(2))
    307/2**10 at prec=10

    Finally, Floats can be instantiated with an mpf tuple (n, c, p) to
    produce the number (-1)**n*c*2**p:

    >>> n, c, p = 1, 5, 0
    >>> (-1)**n*c*2**p
    -5
    >>> Float((1, 5, 0))
    -5.00000000000000

    An actual mpf tuple also contains the number of bits in c as the last
    element of the tuple:

    >>> _._mpf_
    (1, 5, 0, 3)

    This is not needed for instantiation and is not the same thing as the
    precision. The mpf tuple and the precision are two separate quantities
    that Float tracks.

    In SymPy, a Float is a number that can be computed with arbitrary
    precision. Although floating point \'inf\' and \'nan\' are not such
    numbers, Float can create these numbers:

    >>> Float(\'-inf\')
    -oo
    >>> _.is_Float
    False

    Zero in Float only has a single value. Values are not separate for
    positive and negative zeroes.
    '''
    _mpf_: 'tuple[int, int, int, int]' = ('_mpf_', '_prec')
    is_rational = None
    is_irrational = None
    is_number = True
    is_real = True
    is_extended_real = True
    is_Float = True
    _remove_non_digits = str.maketrans(dict.fromkeys('-+_.'))
    
    def __new__(cls, num, dps, precision = (None, None)):
        pass
    # WARNING: Decompyle incomplete

    _new = (lambda cls, _mpf_, _prec, zero = (True,): if zero and _mpf_ == fzero:
S.Zeroif None == _mpf_nan:
S.NaNif None == _mpf_inf:
S.Infinityif None == _mpf_ninf:
S.NegativeInfinityobj = None.__new__(cls)obj._mpf_ = mpf_norm(_mpf_, _prec)obj._prec = _precobj)()
    
    def __getnewargs_ex__(self):
        (sign, man, exp, bc) = self._mpf_
        arg = (sign, hex(man)[2:], exp, bc)
        kwargs = {
            'precision': self._prec }
        return ((arg,), kwargs)

    
    def _hashable_content(self):
        return (self._mpf_, self._prec)

    
    def floor(self):
        return Integer(int(mlib.to_int(mlib.mpf_floor(self._mpf_, self._prec))))

    
    def ceiling(self):
        return Integer(int(mlib.to_int(mlib.mpf_ceil(self._mpf_, self._prec))))

    
    def __floor__(self):
        return self.floor()

    
    def __ceil__(self):
        return self.ceiling()

    num = (lambda self: mpmath.mpf(self._mpf_))()
    
    def _as_mpf_val(self, prec):
        rv = mpf_norm(self._mpf_, prec)
        if rv != self._mpf_ and self._prec == prec:
            debug(self._mpf_, rv)
        return rv

    
    def _as_mpf_op(self, prec):
        return (self._mpf_, max(prec, self._prec))

    
    def _eval_is_finite(self):
        if self._mpf_ in (_mpf_inf, _mpf_ninf):
            return False

    
    def _eval_is_infinite(self):
        if self._mpf_ in (_mpf_inf, _mpf_ninf):
            return True

    
    def _eval_is_integer(self):
        if self._mpf_ == fzero:
            return True
        if not None(self):
            return False

    
    def _eval_is_negative(self):
        if self._mpf_ in (_mpf_ninf, _mpf_inf):
            return False
        return None.num < 0

    
    def _eval_is_positive(self):
        if self._mpf_ in (_mpf_ninf, _mpf_inf):
            return False
        return None.num > 0

    
    def _eval_is_extended_negative(self):
        if self._mpf_ == _mpf_ninf:
            return True
        if None._mpf_ == _mpf_inf:
            return False
        return None.num < 0

    
    def _eval_is_extended_positive(self):
        if self._mpf_ == _mpf_inf:
            return True
        if None._mpf_ == _mpf_ninf:
            return False
        return None.num > 0

    
    def _eval_is_zero(self):
        return self._mpf_ == fzero

    
    def __bool__(self):
        return self._mpf_ != fzero

    
    def __neg__(self):
        if not self:
            return self
        return None._new(mlib.mpf_neg(self._mpf_), self._prec)

    __add__ = (lambda self, other: if isinstance(other, Number) and global_parameters.evaluate:
(rhs, prec) = other._as_mpf_op(self._prec)Float._new(mlib.mpf_add(self._mpf_, rhs, prec, rnd), prec)None.__add__(self, other))()
    __sub__ = (lambda self, other: if isinstance(other, Number) and global_parameters.evaluate:
(rhs, prec) = other._as_mpf_op(self._prec)Float._new(mlib.mpf_sub(self._mpf_, rhs, prec, rnd), prec)None.__sub__(self, other))()
    __mul__ = (lambda self, other: if isinstance(other, Number) and global_parameters.evaluate:
(rhs, prec) = other._as_mpf_op(self._prec)Float._new(mlib.mpf_mul(self._mpf_, rhs, prec, rnd), prec)None.__mul__(self, other))()
    __truediv__ = (lambda self, other: if isinstance(other, Number) and other != 0 and global_parameters.evaluate:
(rhs, prec) = other._as_mpf_op(self._prec)Float._new(mlib.mpf_div(self._mpf_, rhs, prec, rnd), prec)None.__truediv__(self, other))()
    __mod__ = (lambda self, other:
