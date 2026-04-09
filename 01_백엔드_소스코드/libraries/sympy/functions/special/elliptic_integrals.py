# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: elliptic_integrals.pyc (Python 3.11)

''' Elliptic Integrals. '''
from sympy.core import S, pi, I, Rational
from sympy.core.function import Function, ArgumentIndexError
from sympy.core.symbol import Dummy, uniquely_named_symbol
from sympy.functions.elementary.complexes import sign
from sympy.functions.elementary.hyperbolic import atanh
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.functions.elementary.trigonometric import sin, tan
from sympy.functions.special.gamma_functions import gamma
from sympy.functions.special.hyper import hyper, meijerg

class elliptic_k(Function):
    '''
    The complete elliptic integral of the first kind, defined by

    .. math:: K(m) = F\\left(\\tfrac{\\pi}{2}\\middle| m\\right)

    where $F\\left(z\\middle| m\\right)$ is the Legendre incomplete
    elliptic integral of the first kind.

    Explanation
    ===========

    The function $K(m)$ is a single-valued function on the complex
    plane with branch cut along the interval $(1, \\infty)$.

    Note that our notation defines the incomplete elliptic integral
    in terms of the parameter $m$ instead of the elliptic modulus
    (eccentricity) $k$.
    In this case, the parameter $m$ is defined as $m=k^2$.

    Examples
    ========

    >>> from sympy import elliptic_k, I
    >>> from sympy.abc import m
    >>> elliptic_k(0)
    pi/2
    >>> elliptic_k(1.0 + I)
    1.50923695405127 + 0.625146415202697*I
    >>> elliptic_k(m).series(n=3)
    pi/2 + pi*m/8 + 9*pi*m**2/128 + O(m**3)

    See Also
    ========

    elliptic_f

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Elliptic_integrals
    .. [2] https://functions.wolfram.com/EllipticIntegrals/EllipticK

    '''
    eval = (lambda cls, m: if m.is_zero:
pi * S.Halfif None is S.Half:
8 * pi ** Rational(3, 2) / gamma(Rational(-1, 4)) ** 2if None is S.One:
S.ComplexInfinityif None is S.NegativeOne:
gamma(Rational(1, 4)) ** 2 / (4 * sqrt(2 * pi))if None in (S.Infinity, S.NegativeInfinity, I * S.Infinity, I * S.NegativeInfinity, S.ComplexInfinity):
S.Zero)()
    
    def fdiff(self, argindex = (1,)):
        m = self.args[0]
        return (elliptic_e(m) - (1 - m) * elliptic_k(m)) / (2 * m * (1 - m))

    
    def _eval_conjugate(self):
        m = self.args[0]
        if m.is_real or (m - 1).is_positive is False:
            return self.func(m.conjugate())

    
    def _eval_nseries(self, x, n, logx, cdir = (0,)):
        hyperexpand = hyperexpand
        import sympy.simplify
        return hyperexpand(self.rewrite(hyper)._eval_nseries(x, n = n, logx = logx))

    
    def _eval_rewrite_as_hyper(self, m, **kwargs):
        return pi * S.Half * hyper((S.Half, S.Half), (S.One,), m)

    
    def _eval_rewrite_as_meijerg(self, m, **kwargs):
        return meijerg(((S.Half, S.Half), []), ((S.Zero,), (S.Zero,)), -m) / 2

    
    def _eval_is_zero(self):
        m = self.args[0]
        if m.is_infinite:
            return True

    
    def _eval_rewrite_as_Integral(self, *args, **kwargs):
        Integral = Integral
        import sympy.integrals.integrals
        t = Dummy(uniquely_named_symbol('t', args).name)
        m = self.args[0]
        return Integral(1 / sqrt(1 - m * sin(t) ** 2), (t, 0, pi / 2))



class elliptic_f(Function):
    '''
    The Legendre incomplete elliptic integral of the first
    kind, defined by

    .. math:: F\\left(z\\middle| m\\right) =
              \\int_0^z \\frac{dt}{\\sqrt{1 - m \\sin^2 t}}

    Explanation
    ===========

    This function reduces to a complete elliptic integral of
    the first kind, $K(m)$, when $z = \\pi/2$.

    Note that our notation defines the incomplete elliptic integral
    in terms of the parameter $m$ instead of the elliptic modulus
    (eccentricity) $k$.
    In this case, the parameter $m$ is defined as $m=k^2$.

    Examples
    ========

    >>> from sympy import elliptic_f, I
    >>> from sympy.abc import z, m
    >>> elliptic_f(z, m).series(z)
    z + z**5*(3*m**2/40 - m/30) + m*z**3/6 + O(z**6)
    >>> elliptic_f(3.0 + I/2, 1.0 + I)
    2.909449841483 + 1.74720545502474*I

    See Also
    ========

    elliptic_k

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Elliptic_integrals
    .. [2] https://functions.wolfram.com/EllipticIntegrals/EllipticF

    '''
    eval = (lambda cls, z, m: if z.is_zero:
S.Zeroif None.is_zero:
zk = None * z / piif k.is_integer:
k * elliptic_k(m)if None in (S.Infinity, S.NegativeInfinity):
S.Zeroif None.could_extract_minus_sign():
-elliptic_f(-z, m))()
    
    def fdiff(self, argindex = (1,)):
        (z, m) = self.args
        fm = sqrt(1 - m * sin(z) ** 2)
        if argindex == 1:
            return 1 / fm
        if None == 2:
            return elliptic_e(z, m) / (2 * m * (1 - m)) - elliptic_f(z, m) / (2 * m) - sin(2 * z) / (4 * (1 - m) * fm)
        raise None(self, argindex)

    
    def _eval_conjugate(self):
        (z, m) = self.args
        if m.is_real or (m - 1).is_positive is False:
            return self.func(z.conjugate(), m.conjugate())

    
    def _eval_rewrite_as_Integral(self, *args, **kwargs):
        Integral = Integral
        import sympy.integrals.integrals
        t = Dummy(uniquely_named_symbol('t', args).name)
        m = self.args[1]
        z = self.args[0]
        return Integral(1 / sqrt(1 - m * sin(t) ** 2), (t, 0, z))

    
    def _eval_is_zero(self):
        (z, m) = self.args
        if z.is_zero:
            return True
        if None.is_extended_real or m.is_infinite:
            return True
        return None



class elliptic_e(Function):
    pass
# WARNING: Decompyle incomplete


class elliptic_pi(Function):
    '''
    Called with three arguments $n$, $z$ and $m$, evaluates the
    Legendre incomplete elliptic integral of the third kind, defined by

    .. math:: \\Pi\\left(n; z\\middle| m\\right) = \\int_0^z \\frac{dt}
              {\\left(1 - n \\sin^2 t\\right) \\sqrt{1 - m \\sin^2 t}}

    Called with two arguments $n$ and $m$, evaluates the complete
    elliptic integral of the third kind:

    .. math:: \\Pi\\left(n\\middle| m\\right) =
              \\Pi\\left(n; \\tfrac{\\pi}{2}\\middle| m\\right)

    Explanation
    ===========

    Note that our notation defines the incomplete elliptic integral
    in terms of the parameter $m$ instead of the elliptic modulus
    (eccentricity) $k$.
    In this case, the parameter $m$ is defined as $m=k^2$.

    Examples
    ========

    >>> from sympy import elliptic_pi, I
    >>> from sympy.abc import z, n, m
    >>> elliptic_pi(n, z, m).series(z, n=4)
    z + z**3*(m/6 + n/3) + O(z**4)
    >>> elliptic_pi(0.5 + I, 1.0 - I, 1.2)
    2.50232379629182 - 0.760939574180767*I
    >>> elliptic_pi(0, 0)
    pi/2
    >>> elliptic_pi(1.0 - I/3, 2.0 + I)
    3.29136443417283 + 0.32555634906645*I

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Elliptic_integrals
    .. [2] https://functions.wolfram.com/EllipticIntegrals/EllipticPi3
    .. [3] https://functions.wolfram.com/EllipticIntegrals/EllipticPi

    '''
    eval = (lambda cls, n, m, z = (None,): pass# WARNING: Decompyle incomplete
)()
    
    def _eval_conjugate(self):
        if len(self.args) == 3:
            (n, z, m) = self.args
            if n.is_real or (n - 1).is_positive is False:
                if m.is_real or (m - 1).is_positive is False:
                    return self.func(n.conjugate(), z.conjugate(), m.conjugate())
                return None
            return None
        (n, m) = None.args
        return self.func(n.conjugate(), m.conjugate())

    
    def fdiff(self, argindex = (1,)):
        if len(self.args) == 3:
            (n, z, m) = self.args
            fn = 1 - n * sin(z) ** 2
            fm = sqrt(1 - m * sin(z) ** 2)
            if argindex == 1:
                return (elliptic_e(z, m) + (m - n) * elliptic_f(z, m) / n + (n ** 2 - m) * elliptic_pi(n, z, m) / n - n * fm * sin(2 * z) / (2 * fn)) / (2 * (m - n) * (n - 1))
            if None == 2:
                return 1 / (fm * fn)
            if None == 3:
                return (elliptic_e(z, m) / (m - 1) + elliptic_pi(n, z, m) - m * sin(2 * z) / (2 * (m - 1) * fm)) / (2 * (n - m))
        (n, m) = self.args
        if argindex == 1:
            return (elliptic_e(m) + (m - n) * elliptic_k(m) / n + (n ** 2 - m) * elliptic_pi(n, m) / n) / (2 * (m - n) * (n - 1))
        if None == 2:
            return (elliptic_e(m) / (m - 1) + elliptic_pi(n, m)) / (2 * (n - m))
        raise None(self, argindex)

    
    def _eval_rewrite_as_Integral(self, *args, **kwargs):
        Integral = Integral
        import sympy.integrals.integrals
        if len(self.args) == 2:
            z = pi / 2
            m = self.args[1]
            n = self.args[0]
        else:
            (n, z, m) = self.args
        t = Dummy(uniquely_named_symbol('t', args).name)
        return Integral(1 / ((1 - n * sin(t) ** 2) * sqrt(1 - m * sin(t) ** 2)), (t, 0, z))
