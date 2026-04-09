# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: gamma_functions.pyc (Python 3.11)

from math import prod
from sympy.core import Add, S, Dummy, expand_func
from sympy.core.expr import Expr
from sympy.core.function import Function, ArgumentIndexError, PoleError
from sympy.core.logic import fuzzy_and, fuzzy_not
from sympy.core.numbers import Rational, pi, oo, I
from sympy.core.power import Pow
from sympy.functions.special.zeta_functions import zeta
from sympy.functions.special.error_functions import erf, erfc, Ei
from sympy.functions.elementary.complexes import re, unpolarify
from sympy.functions.elementary.exponential import exp, log
from sympy.functions.elementary.integers import ceiling, floor
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.functions.elementary.trigonometric import sin, cos, cot
from sympy.functions.combinatorial.numbers import bernoulli, harmonic
from sympy.functions.combinatorial.factorials import factorial, rf, RisingFactorial
from sympy.utilities.misc import as_int
from mpmath import mp, workprec
from mpmath.libmp.libmpf import prec_to_dps

def intlike(n):
    
    try:
        as_int(n, strict = False)
        return True
    except ValueError:
        return False



class gamma(Function):
    pass
# WARNING: Decompyle incomplete


class lowergamma(Function):
    pass
# WARNING: Decompyle incomplete


class uppergamma(Function):
    '''
    The upper incomplete gamma function.

    Explanation
    ===========

    It can be defined as the meromorphic continuation of

    .. math::
        \\Gamma(s, x) := \\int_x^\\infty t^{s-1} e^{-t} \\mathrm{d}t = \\Gamma(s) - \\gamma(s, x).

    where $\\gamma(s, x)$ is the lower incomplete gamma function,
    :class:`lowergamma`. This can be shown to be the same as

    .. math::
        \\Gamma(s, x) = \\Gamma(s) - \\frac{x^s}{s} {}_1F_1\\left({s \\atop s+1} \\middle| -x\\right),

    where ${}_1F_1$ is the (confluent) hypergeometric function.

    The upper incomplete gamma function is also essentially equivalent to the
    generalized exponential integral:

    .. math::
        \\operatorname{E}_{n}(x) = \\int_{1}^{\\infty}{\\frac{e^{-xt}}{t^n} \\, dt} = x^{n-1}\\Gamma(1-n,x).

    Examples
    ========

    >>> from sympy import uppergamma, S
    >>> from sympy.abc import s, x
    >>> uppergamma(s, x)
    uppergamma(s, x)
    >>> uppergamma(3, x)
    2*(x**2/2 + x + 1)*exp(-x)
    >>> uppergamma(-S(1)/2, x)
    -2*sqrt(pi)*erfc(sqrt(x)) + 2*exp(-x)/sqrt(x)
    >>> uppergamma(-2, x)
    expint(3, x)/x**2

    See Also
    ========

    gamma: Gamma function.
    lowergamma: Lower incomplete gamma function.
    polygamma: Polygamma function.
    loggamma: Log Gamma function.
    digamma: Digamma function.
    trigamma: Trigamma function.
    sympy.functions.special.beta_functions.beta: Euler Beta function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Incomplete_gamma_function#Upper_incomplete_gamma_function
    .. [2] Abramowitz, Milton; Stegun, Irene A., eds. (1965), Chapter 6,
           Section 5, Handbook of Mathematical Functions with Formulas, Graphs,
           and Mathematical Tables
    .. [3] https://dlmf.nist.gov/8
    .. [4] https://functions.wolfram.com/GammaBetaErf/Gamma2/
    .. [5] https://functions.wolfram.com/GammaBetaErf/Gamma3/
    .. [6] https://en.wikipedia.org/wiki/Exponential_integral#Relation_with_other_functions

    '''
    
    def fdiff(self, argindex = (2,)):
        meijerg = meijerg
        import sympy.functions.special.hyper
        if argindex == 2:
            (a, z) = self.args
            return -exp(-unpolarify(z)) * z ** (a - 1)
        if None == 1:
            (a, z) = self.args
            return uppergamma(a, z) * log(z) + meijerg([], [
                1,
                1], [
                0,
                0,
                a], [], z)
        raise None(self, argindex)

    
    def _eval_evalf(self, prec):
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args()):
            a = self.args[0]._to_mpmath(prec)
            z = self.args[1]._to_mpmath(prec)
            workprec(prec)
            res = mp.gammainc(a, z, mp.inf)
            None(None, None)
        else:
            with None:
                if not all:
                    pass
        return Expr._from_mpmath(res, prec)
        return self

    eval = (lambda cls, a, z: pass# WARNING: Decompyle incomplete
)()
    
    def _eval_conjugate(self):
        z = self.args[1]
        if z not in (S.Zero, S.NegativeInfinity):
            return self.func(self.args[0].conjugate(), z.conjugate())

    
    def _eval_is_meromorphic(self, x, a):
        return lowergamma._eval_is_meromorphic(self, x, a)

    
    def _eval_rewrite_as_lowergamma(self, s, x, **kwargs):
        return gamma(s) - lowergamma(s, x)

    
    def _eval_rewrite_as_tractable(self, s, x, **kwargs):
        return exp(loggamma(s)) - lowergamma(s, x)

    
    def _eval_rewrite_as_expint(self, s, x, **kwargs):
        expint = expint
        import sympy.functions.special.error_functions
        return expint(1 - s, x) * x ** s



class polygamma(Function):
    pass
# WARNING: Decompyle incomplete


class loggamma(Function):
    pass
# WARNING: Decompyle incomplete


class digamma(Function):
    """
    The ``digamma`` function is the first derivative of the ``loggamma``
    function

    .. math::
        \\psi(x) := \\frac{\\mathrm{d}}{\\mathrm{d} z} \\log\\Gamma(z)
                = \\frac{\\Gamma'(z)}{\\Gamma(z) }.

    In this case, ``digamma(z) = polygamma(0, z)``.

    Examples
    ========

    >>> from sympy import digamma
    >>> digamma(0)
    zoo
    >>> from sympy import Symbol
    >>> z = Symbol('z')
    >>> digamma(z)
    polygamma(0, z)

    To retain ``digamma`` as it is:

    >>> digamma(0, evaluate=False)
    digamma(0)
    >>> digamma(z, evaluate=False)
    digamma(z)

    See Also
    ========

    gamma: Gamma function.
    lowergamma: Lower incomplete gamma function.
    uppergamma: Upper incomplete gamma function.
    polygamma: Polygamma function.
    loggamma: Log Gamma function.
    trigamma: Trigamma function.
    sympy.functions.special.beta_functions.beta: Euler Beta function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Digamma_function
    .. [2] https://mathworld.wolfram.com/DigammaFunction.html
    .. [3] https://functions.wolfram.com/GammaBetaErf/PolyGamma2/

    """
    
    def _eval_evalf(self, prec):
        z = self.args[0]
        nprec = prec_to_dps(prec)
        return polygamma(0, z).evalf(n = nprec)

    
    def fdiff(self, argindex = (1,)):
        z = self.args[0]
        return polygamma(0, z).fdiff()

    
    def _eval_is_real(self):
        z = self.args[0]
        return polygamma(0, z).is_real

    
    def _eval_is_positive(self):
        z = self.args[0]
        return polygamma(0, z).is_positive

    
    def _eval_is_negative(self):
        z = self.args[0]
        return polygamma(0, z).is_negative

    
    def _eval_aseries(self, n, args0, x, logx):
        as_polygamma = self.rewrite(polygamma)
        args0 = [
            S.Zero] + args0
        return as_polygamma._eval_aseries(n, args0, x, logx)

    eval = (lambda cls, z: polygamma(0, z))()
    
    def _eval_expand_func(self, **hints):
        z = self.args[0]
        return polygamma(0, z).expand(func = True)

    
    def _eval_rewrite_as_harmonic(self, z, **kwargs):
        return harmonic(z - 1) - S.EulerGamma

    
    def _eval_rewrite_as_polygamma(self, z, **kwargs):
        return polygamma(0, z)

    
    def _eval_as_leading_term(self, x, logx, cdir = (None, 0)):
        z = self.args[0]
        return polygamma(0, z).as_leading_term(x)



class trigamma(Function):
    """
    The ``trigamma`` function is the second derivative of the ``loggamma``
    function

    .. math::
        \\psi^{(1)}(z) := \\frac{\\mathrm{d}^{2}}{\\mathrm{d} z^{2}} \\log\\Gamma(z).

    In this case, ``trigamma(z) = polygamma(1, z)``.

    Examples
    ========

    >>> from sympy import trigamma
    >>> trigamma(0)
    zoo
    >>> from sympy import Symbol
    >>> z = Symbol('z')
    >>> trigamma(z)
    polygamma(1, z)

    To retain ``trigamma`` as it is:

    >>> trigamma(0, evaluate=False)
    trigamma(0)
    >>> trigamma(z, evaluate=False)
    trigamma(z)


    See Also
    ========

    gamma: Gamma function.
    lowergamma: Lower incomplete gamma function.
    uppergamma: Upper incomplete gamma function.
    polygamma: Polygamma function.
    loggamma: Log Gamma function.
    digamma: Digamma function.
    sympy.functions.special.beta_functions.beta: Euler Beta function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Trigamma_function
    .. [2] https://mathworld.wolfram.com/TrigammaFunction.html
    .. [3] https://functions.wolfram.com/GammaBetaErf/PolyGamma2/

    """
    
    def _eval_evalf(self, prec):
        z = self.args[0]
        nprec = prec_to_dps(prec)
        return polygamma(1, z).evalf(n = nprec)

    
    def fdiff(self, argindex = (1,)):
        z = self.args[0]
        return polygamma(1, z).fdiff()

    
    def _eval_is_real(self):
        z = self.args[0]
        return polygamma(1, z).is_real

    
    def _eval_is_positive(self):
        z = self.args[0]
        return polygamma(1, z).is_positive

    
    def _eval_is_negative(self):
        z = self.args[0]
        return polygamma(1, z).is_negative

    
    def _eval_aseries(self, n, args0, x, logx):
        as_polygamma = self.rewrite(polygamma)
        args0 = [
            S.One] + args0
        return as_polygamma._eval_aseries(n, args0, x, logx)

    eval = (lambda cls, z: polygamma(1, z))()
    
    def _eval_expand_func(self, **hints):
        z = self.args[0]
        return polygamma(1, z).expand(func = True)

    
    def _eval_rewrite_as_zeta(self, z, **kwargs):
        return zeta(2, z)

    
    def _eval_rewrite_as_polygamma(self, z, **kwargs):
        return polygamma(1, z)

    
    def _eval_rewrite_as_harmonic(self, z, **kwargs):
        return -harmonic(z - 1, 2) + pi ** 2 / 6

    
    def _eval_as_leading_term(self, x, logx, cdir = (None, 0)):
        z = self.args[0]
        return polygamma(1, z).as_leading_term(x)



class multigamma(Function):
    """
    The multivariate gamma function is a generalization of the gamma function

    .. math::
        \\Gamma_p(z) = \\pi^{p(p-1)/4}\\prod_{k=1}^p \\Gamma[z + (1 - k)/2].

    In a special case, ``multigamma(x, 1) = gamma(x)``.

    Examples
    ========

    >>> from sympy import S, multigamma
    >>> from sympy import Symbol
    >>> x = Symbol('x')
    >>> p = Symbol('p', positive=True, integer=True)

    >>> multigamma(x, p)
    pi**(p*(p - 1)/4)*Product(gamma(-_k/2 + x + 1/2), (_k, 1, p))

    Several special values are known:

    >>> multigamma(1, 1)
    1
    >>> multigamma(4, 1)
    6
    >>> multigamma(S(3)/2, 1)
    sqrt(pi)/2

    Writing ``multigamma`` in terms of the ``gamma`` function:

    >>> multigamma(x, 1)
    gamma(x)

    >>> multigamma(x, 2)
    sqrt(pi)*gamma(x)*gamma(x - 1/2)

    >>> multigamma(x, 3)
    pi**(3/2)*gamma(x)*gamma(x - 1)*gamma(x - 1/2)

    Parameters
    ==========

    p : order or dimension of the multivariate gamma function

    See Also
    ========

    gamma, lowergamma, uppergamma, polygamma, loggamma, digamma, trigamma,
    sympy.functions.special.beta_functions.beta

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Multivariate_gamma_function

    """
    unbranched = True
    
    def fdiff(self, argindex = (2,)):
        Sum = Sum
        import sympy.concrete.summations
        if argindex == 2:
            (x, p) = self.args
            k = Dummy('k')
            return self.func(x, p) * Sum(polygamma(0, x + (1 - k) / 2), (k, 1, p))
        raise None(self, argindex)

    eval = (lambda cls, x, p: Product = Productimport sympy.concrete.productsif p.is_positive is False or p.is_integer is False:
raise ValueError('Order parameter p must be positive integer.')k = Dummy('k')(pi ** (p * (p - 1) / 4) * Product(gamma(x + (1 - k) / 2), (k, 1, p))).doit())()
    
    def _eval_conjugate(self):
        (x, p) = self.args
        return self.func(x.conjugate(), p)

    
    def _eval_is_real(self):
        (x, p) = self.args
        y = 2 * x
        if y.is_integer and y <= p - 1 is True:
            return False
        if None(y) and y <= p - 1:
            return False
        if None > p - 1 or y.is_noninteger:
            return True
