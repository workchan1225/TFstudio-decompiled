# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: polynomials.pyc (Python 3.11)

'''
This module mainly implements special orthogonal polynomials.

See also functions.combinatorial.numbers which contains some
combinatorial polynomials.

'''
from sympy.core import Rational
from sympy.core.function import Function, ArgumentIndexError
from sympy.core.singleton import S
from sympy.core.symbol import Dummy
from sympy.functions.combinatorial.factorials import binomial, factorial, RisingFactorial
from sympy.functions.elementary.complexes import re
from sympy.functions.elementary.exponential import exp
from sympy.functions.elementary.integers import floor
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.functions.elementary.trigonometric import cos, sec
from sympy.functions.special.gamma_functions import gamma
from sympy.functions.special.hyper import hyper
from sympy.polys.orthopolys import chebyshevt_poly, chebyshevu_poly, gegenbauer_poly, hermite_poly, hermite_prob_poly, jacobi_poly, laguerre_poly, legendre_poly
_x = Dummy('x')

class OrthogonalPolynomial(Function):
    '''Base class for orthogonal polynomials.
    '''
    _eval_at_order = (lambda cls, n, x: if n.is_integer or n >= 0:
cls._ortho_poly(int(n), _x).subs(_x, x)None)()
    
    def _eval_conjugate(self):
        return self.func(self.args[0], self.args[1].conjugate())



class jacobi(OrthogonalPolynomial):
    '''
    Jacobi polynomial $P_n^{\\left(\\alpha, \\beta\\right)}(x)$.

    Explanation
    ===========

    ``jacobi(n, alpha, beta, x)`` gives the $n$th Jacobi polynomial
    in $x$, $P_n^{\\left(\\alpha, \\beta\\right)}(x)$.

    The Jacobi polynomials are orthogonal on $[-1, 1]$ with respect
    to the weight $\\left(1-x\\right)^\\alpha \\left(1+x\\right)^\\beta$.

    Examples
    ========

    >>> from sympy import jacobi, S, conjugate, diff
    >>> from sympy.abc import a, b, n, x

    >>> jacobi(0, a, b, x)
    1
    >>> jacobi(1, a, b, x)
    a/2 - b/2 + x*(a/2 + b/2 + 1)
    >>> jacobi(2, a, b, x)
    a**2/8 - a*b/4 - a/8 + b**2/8 - b/8 + x**2*(a**2/8 + a*b/4 + 7*a/8 + b**2/8 + 7*b/8 + 3/2) + x*(a**2/4 + 3*a/4 - b**2/4 - 3*b/4) - 1/2

    >>> jacobi(n, a, b, x)
    jacobi(n, a, b, x)

    >>> jacobi(n, a, a, x)
    RisingFactorial(a + 1, n)*gegenbauer(n,
        a + 1/2, x)/RisingFactorial(2*a + 1, n)

    >>> jacobi(n, 0, 0, x)
    legendre(n, x)

    >>> jacobi(n, S(1)/2, S(1)/2, x)
    RisingFactorial(3/2, n)*chebyshevu(n, x)/factorial(n + 1)

    >>> jacobi(n, -S(1)/2, -S(1)/2, x)
    RisingFactorial(1/2, n)*chebyshevt(n, x)/factorial(n)

    >>> jacobi(n, a, b, -x)
    (-1)**n*jacobi(n, b, a, x)

    >>> jacobi(n, a, b, 0)
    gamma(a + n + 1)*hyper((-n, -b - n), (a + 1,), -1)/(2**n*factorial(n)*gamma(a + 1))
    >>> jacobi(n, a, b, 1)
    RisingFactorial(a + 1, n)/factorial(n)

    >>> conjugate(jacobi(n, a, b, x))
    jacobi(n, conjugate(a), conjugate(b), conjugate(x))

    >>> diff(jacobi(n,a,b,x), x)
    (a/2 + b/2 + n/2 + 1/2)*jacobi(n - 1, a + 1, b + 1, x)

    See Also
    ========

    gegenbauer,
    chebyshevt_root, chebyshevu, chebyshevu_root,
    legendre, assoc_legendre,
    hermite, hermite_prob,
    laguerre, assoc_laguerre,
    sympy.polys.orthopolys.jacobi_poly,
    sympy.polys.orthopolys.gegenbauer_poly
    sympy.polys.orthopolys.chebyshevt_poly
    sympy.polys.orthopolys.chebyshevu_poly
    sympy.polys.orthopolys.hermite_poly
    sympy.polys.orthopolys.legendre_poly
    sympy.polys.orthopolys.laguerre_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Jacobi_polynomials
    .. [2] https://mathworld.wolfram.com/JacobiPolynomial.html
    .. [3] https://functions.wolfram.com/Polynomials/JacobiP/

    '''
    eval = (lambda cls, n, a, b, x: if a == b:
if a == Rational(-1, 2):
(RisingFactorial(S.Half, n) / factorial(n)) * chebyshevt(n, x)if None.is_zero:
legendre(n, x)if None == S.Half:
(RisingFactorial(3 * S.Half, n) / factorial(n + 1)) * chebyshevu(n, x)(None(a + 1, n) / RisingFactorial(2 * a + 1, n)) * gegenbauer(n, a + S.Half, x)if None == -a:
((gamma(n + a + 1) / gamma(n + 1)) * (1 + x) ** (a / 2) / (1 - x) ** (a / 2)) * assoc_legendre(n, -a, x)if not None.is_Number:
if x.could_extract_minus_sign():
S.NegativeOne ** n * jacobi(n, b, a, -x)if None.is_zero:
(2 ** (-n) * gamma(a + n + 1) / (gamma(a + 1) * factorial(n))) * hyper([
-b - n,
-n], [
a + 1], -1)if None == S.One:
RisingFactorial(a + 1, n) / factorial(n)if None is S.Infinity or n.is_positive:
if (a + b + 2 * n).is_integer:
raise ValueError('Error. a + b + 2*n should not be an integer.')RisingFactorial(a + b + n + 1, n) * S.InfinityNoneNonejacobi_poly(n, a, b, x))()
    
    def fdiff(self, argindex = (4,)):
        Sum = Sum
        import sympy.concrete.summations
        if argindex == 1:
            raise ArgumentIndexError(self, argindex)
        if argindex == 2:
            (n, a, b, x) = self.args
            k = Dummy('k')
            f1 = 1 / (a + b + n + k + 1)
            f2 = (a + b + 2 * k + 1) * RisingFactorial(b + k + 1, n - k) / ((n - k) * RisingFactorial(a + b + k + 1, n - k))
            return Sum(f1 * (jacobi(n, a, b, x) + f2 * jacobi(k, a, b, x)), (k, 0, n - 1))
        if None == 3:
            (n, a, b, x) = self.args
            k = Dummy('k')
            f1 = 1 / (a + b + n + k + 1)
            f2 = -1 ** (n - k) * ((a + b + 2 * k + 1) * RisingFactorial(a + k + 1, n - k) / ((n - k) * RisingFactorial(a + b + k + 1, n - k)))
            return Sum(f1 * (jacobi(n, a, b, x) + f2 * jacobi(k, a, b, x)), (k, 0, n - 1))
        if None == 4:
            (n, a, b, x) = self.args
            return S.Half * (a + b + n + 1) * jacobi(n - 1, a + 1, b + 1, x)
        raise None(self, argindex)

    
    def _eval_rewrite_as_Sum(self, n, a, b, x, **kwargs):
        Sum = Sum
        import sympy.concrete.summations
        if n.is_negative or n.is_integer is False:
            raise ValueError('Error: n should be a non-negative integer.')
        k = Dummy('k')
        kern = (RisingFactorial(-n, k) * RisingFactorial(a + b + n + 1, k) * RisingFactorial(a + k + 1, n - k) / factorial(k)) * ((1 - x) / 2) ** k
        return (1 / factorial(n)) * Sum(kern, (k, 0, n))

    
    def _eval_rewrite_as_polynomial(self, n, a, b, x, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_conjugate(self):
        (n, a, b, x) = self.args
        return self.func(n, a.conjugate(), b.conjugate(), x.conjugate())



def jacobi_normalized(n, a, b, x):
    '''
    Jacobi polynomial $P_n^{\\left(\\alpha, \\beta\\right)}(x)$.

    Explanation
    ===========

    ``jacobi_normalized(n, alpha, beta, x)`` gives the $n$th
    Jacobi polynomial in $x$, $P_n^{\\left(\\alpha, \\beta\\right)}(x)$.

    The Jacobi polynomials are orthogonal on $[-1, 1]$ with respect
    to the weight $\\left(1-x\\right)^\\alpha \\left(1+x\\right)^\\beta$.

    This functions returns the polynomials normilzed:

    .. math::

        \\int_{-1}^{1}
          P_m^{\\left(\\alpha, \\beta\\right)}(x)
          P_n^{\\left(\\alpha, \\beta\\right)}(x)
          (1-x)^{\\alpha} (1+x)^{\\beta} \\mathrm{d}x
        = \\delta_{m,n}

    Examples
    ========

    >>> from sympy import jacobi_normalized
    >>> from sympy.abc import n,a,b,x

    >>> jacobi_normalized(n, a, b, x)
    jacobi(n, a, b, x)/sqrt(2**(a + b + 1)*gamma(a + n + 1)*gamma(b + n + 1)/((a + b + 2*n + 1)*factorial(n)*gamma(a + b + n + 1)))

    Parameters
    ==========

    n : integer degree of polynomial

    a : alpha value

    b : beta value

    x : symbol

    See Also
    ========

    gegenbauer,
    chebyshevt_root, chebyshevu, chebyshevu_root,
    legendre, assoc_legendre,
    hermite, hermite_prob,
    laguerre, assoc_laguerre,
    sympy.polys.orthopolys.jacobi_poly,
    sympy.polys.orthopolys.gegenbauer_poly
    sympy.polys.orthopolys.chebyshevt_poly
    sympy.polys.orthopolys.chebyshevu_poly
    sympy.polys.orthopolys.hermite_poly
    sympy.polys.orthopolys.legendre_poly
    sympy.polys.orthopolys.laguerre_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Jacobi_polynomials
    .. [2] https://mathworld.wolfram.com/JacobiPolynomial.html
    .. [3] https://functions.wolfram.com/Polynomials/JacobiP/

    '''
    nfactor = S(2) ** (a + b + 1) * gamma(n + a + 1) * gamma(n + b + 1) / (2 * n + a + b + 1) / (factorial(n) * gamma(n + a + b + 1))
    return jacobi(n, a, b, x) / sqrt(nfactor)


class gegenbauer(OrthogonalPolynomial):
    '''
    Gegenbauer polynomial $C_n^{\\left(\\alpha\\right)}(x)$.

    Explanation
    ===========

    ``gegenbauer(n, alpha, x)`` gives the $n$th Gegenbauer polynomial
    in $x$, $C_n^{\\left(\\alpha\\right)}(x)$.

    The Gegenbauer polynomials are orthogonal on $[-1, 1]$ with
    respect to the weight $\\left(1-x^2\\right)^{\\alpha-\\frac{1}{2}}$.

    Examples
    ========

    >>> from sympy import gegenbauer, conjugate, diff
    >>> from sympy.abc import n,a,x
    >>> gegenbauer(0, a, x)
    1
    >>> gegenbauer(1, a, x)
    2*a*x
    >>> gegenbauer(2, a, x)
    -a + x**2*(2*a**2 + 2*a)
    >>> gegenbauer(3, a, x)
    x**3*(4*a**3/3 + 4*a**2 + 8*a/3) + x*(-2*a**2 - 2*a)

    >>> gegenbauer(n, a, x)
    gegenbauer(n, a, x)
    >>> gegenbauer(n, a, -x)
    (-1)**n*gegenbauer(n, a, x)

    >>> gegenbauer(n, a, 0)
    2**n*sqrt(pi)*gamma(a + n/2)/(gamma(a)*gamma(1/2 - n/2)*gamma(n + 1))
    >>> gegenbauer(n, a, 1)
    gamma(2*a + n)/(gamma(2*a)*gamma(n + 1))

    >>> conjugate(gegenbauer(n, a, x))
    gegenbauer(n, conjugate(a), conjugate(x))

    >>> diff(gegenbauer(n, a, x), x)
    2*a*gegenbauer(n - 1, a + 1, x)

    See Also
    ========

    jacobi,
    chebyshevt_root, chebyshevu, chebyshevu_root,
    legendre, assoc_legendre,
    hermite, hermite_prob,
    laguerre, assoc_laguerre,
    sympy.polys.orthopolys.jacobi_poly
    sympy.polys.orthopolys.gegenbauer_poly
    sympy.polys.orthopolys.chebyshevt_poly
    sympy.polys.orthopolys.chebyshevu_poly
    sympy.polys.orthopolys.hermite_poly
    sympy.polys.orthopolys.hermite_prob_poly
    sympy.polys.orthopolys.legendre_poly
    sympy.polys.orthopolys.laguerre_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Gegenbauer_polynomials
    .. [2] https://mathworld.wolfram.com/GegenbauerPolynomial.html
    .. [3] https://functions.wolfram.com/Polynomials/GegenbauerC3/

    '''
    eval = (lambda cls, n, a, x: if n.is_negative:
S.Zeroif None == S.Half:
legendre(n, x)if None == S.One:
chebyshevu(n, x)if None == S.NegativeOne:
S.Zeroif not None.is_Number:
if x == S.NegativeOne:
if (re(a) > S.Half) == True:
S.ComplexInfinityNone(S.Pi * (a + n)) * sec(S.Pi * a) * gamma(2 * a + n) / (gamma(2 * a) * gamma(n + 1))if None.could_extract_minus_sign():
S.NegativeOne ** n * gegenbauer(n, a, -x)if None.is_zero:
2 ** n * sqrt(S.Pi) * gamma(a + S.Half * n) / (gamma((1 - n) / 2) * gamma(n + 1) * gamma(a))if None == S.One:
gamma(2 * a + n) / (gamma(2 * a) * gamma(n + 1))if None is S.Infinity or n.is_positive:
RisingFactorial(a, n) * S.InfinityNoneNonegegenbauer_poly(n, a, x))()
    
    def fdiff(self, argindex = (3,)):
        Sum = Sum
        import sympy.concrete.summations
        if argindex == 1:
            raise ArgumentIndexError(self, argindex)
        if argindex == 2:
            (n, a, x) = self.args
            k = Dummy('k')
            factor1 = 2 * (1 + -1 ** (n - k)) * (k + a) / ((k + n + 2 * a) * (n - k))
            factor2 = 2 * (k + 1) / ((k + 2 * a) * (2 * k + 2 * a + 1)) + 2 / (k + n + 2 * a)
            kern = factor1 * gegenbauer(k, a, x) + factor2 * gegenbauer(n, a, x)
            return Sum(kern, (k, 0, n - 1))
        if None == 3:
            (n, a, x) = self.args
            return 2 * a * gegenbauer(n - 1, a + 1, x)
        raise None(self, argindex)

    
    def _eval_rewrite_as_Sum(self, n, a, x, **kwargs):
        Sum = Sum
        import sympy.concrete.summations
        k = Dummy('k')
        kern = -1 ** k * RisingFactorial(a, n - k) * (2 * x) ** (n - 2 * k) / (factorial(k) * factorial(n - 2 * k))
        return Sum(kern, (k, 0, floor(n / 2)))

    
    def _eval_rewrite_as_polynomial(self, n, a, x, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_conjugate(self):
        (n, a, x) = self.args
        return self.func(n, a.conjugate(), x.conjugate())



class chebyshevt(OrthogonalPolynomial):
    '''
    Chebyshev polynomial of the first kind, $T_n(x)$.

    Explanation
    ===========

    ``chebyshevt(n, x)`` gives the $n$th Chebyshev polynomial (of the first
    kind) in $x$, $T_n(x)$.

    The Chebyshev polynomials of the first kind are orthogonal on
    $[-1, 1]$ with respect to the weight $\\frac{1}{\\sqrt{1-x^2}}$.

    Examples
    ========

    >>> from sympy import chebyshevt, diff
    >>> from sympy.abc import n,x
    >>> chebyshevt(0, x)
    1
    >>> chebyshevt(1, x)
    x
    >>> chebyshevt(2, x)
    2*x**2 - 1

    >>> chebyshevt(n, x)
    chebyshevt(n, x)
    >>> chebyshevt(n, -x)
    (-1)**n*chebyshevt(n, x)
    >>> chebyshevt(-n, x)
    chebyshevt(n, x)

    >>> chebyshevt(n, 0)
    cos(pi*n/2)
    >>> chebyshevt(n, -1)
    (-1)**n

    >>> diff(chebyshevt(n, x), x)
    n*chebyshevu(n - 1, x)

    See Also
    ========

    jacobi, gegenbauer,
    chebyshevt_root, chebyshevu, chebyshevu_root,
    legendre, assoc_legendre,
    hermite, hermite_prob,
    laguerre, assoc_laguerre,
    sympy.polys.orthopolys.jacobi_poly
    sympy.polys.orthopolys.gegenbauer_poly
    sympy.polys.orthopolys.chebyshevt_poly
    sympy.polys.orthopolys.chebyshevu_poly
    sympy.polys.orthopolys.hermite_poly
    sympy.polys.orthopolys.hermite_prob_poly
    sympy.polys.orthopolys.legendre_poly
    sympy.polys.orthopolys.laguerre_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Chebyshev_polynomial
    .. [2] https://mathworld.wolfram.com/ChebyshevPolynomialoftheFirstKind.html
    .. [3] https://mathworld.wolfram.com/ChebyshevPolynomialoftheSecondKind.html
    .. [4] https://functions.wolfram.com/Polynomials/ChebyshevT/
    .. [5] https://functions.wolfram.com/Polynomials/ChebyshevU/

    '''
    _ortho_poly = staticmethod(chebyshevt_poly)
    eval = (lambda cls, n, x: if not n.is_Number:
if x.could_extract_minus_sign():
S.NegativeOne ** n * chebyshevt(n, -x)if None.could_extract_minus_sign():
chebyshevt(-n, x)if None.is_zero:
cos(S.Half * S.Pi * n)if None == S.One:
S.Oneif None is S.Infinity:
S.InfinityNoneif None.is_negative:
cls._eval_at_order(-n, x)None._eval_at_order(n, x))()
    
    def fdiff(self, argindex = (2,)):
        if argindex == 1:
            raise ArgumentIndexError(self, argindex)
        if argindex == 2:
            (n, x) = self.args
            return n * chebyshevu(n - 1, x)
        raise None(self, argindex)

    
    def _eval_rewrite_as_Sum(self, n, x, **kwargs):
        Sum = Sum
        import sympy.concrete.summations
        k = Dummy('k')
        kern = binomial(n, 2 * k) * (x ** 2 - 1) ** k * x ** (n - 2 * k)
        return Sum(kern, (k, 0, floor(n / 2)))

    
    def _eval_rewrite_as_polynomial(self, n, x, **kwargs):
        pass
    # WARNING: Decompyle incomplete



class chebyshevu(OrthogonalPolynomial):
    '''
    Chebyshev polynomial of the second kind, $U_n(x)$.

    Explanation
    ===========

    ``chebyshevu(n, x)`` gives the $n$th Chebyshev polynomial of the second
    kind in x, $U_n(x)$.

    The Chebyshev polynomials of the second kind are orthogonal on
    $[-1, 1]$ with respect to the weight $\\sqrt{1-x^2}$.

    Examples
    ========

    >>> from sympy import chebyshevu, diff
    >>> from sympy.abc import n,x
    >>> chebyshevu(0, x)
    1
    >>> chebyshevu(1, x)
    2*x
    >>> chebyshevu(2, x)
    4*x**2 - 1

    >>> chebyshevu(n, x)
    chebyshevu(n, x)
    >>> chebyshevu(n, -x)
    (-1)**n*chebyshevu(n, x)
    >>> chebyshevu(-n, x)
    -chebyshevu(n - 2, x)

    >>> chebyshevu(n, 0)
    cos(pi*n/2)
    >>> chebyshevu(n, 1)
    n + 1

    >>> diff(chebyshevu(n, x), x)
    (-x*chebyshevu(n, x) + (n + 1)*chebyshevt(n + 1, x))/(x**2 - 1)

    See Also
    ========

    jacobi, gegenbauer,
    chebyshevt, chebyshevt_root, chebyshevu_root,
    legendre, assoc_legendre,
    hermite, hermite_prob,
    laguerre, assoc_laguerre,
    sympy.polys.orthopolys.jacobi_poly
    sympy.polys.orthopolys.gegenbauer_poly
    sympy.polys.orthopolys.chebyshevt_poly
    sympy.polys.orthopolys.chebyshevu_poly
    sympy.polys.orthopolys.hermite_poly
    sympy.polys.orthopolys.hermite_prob_poly
    sympy.polys.orthopolys.legendre_poly
    sympy.polys.orthopolys.laguerre_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Chebyshev_polynomial
    .. [2] https://mathworld.wolfram.com/ChebyshevPolynomialoftheFirstKind.html
    .. [3] https://mathworld.wolfram.com/ChebyshevPolynomialoftheSecondKind.html
    .. [4] https://functions.wolfram.com/Polynomials/ChebyshevT/
    .. [5] https://functions.wolfram.com/Polynomials/ChebyshevU/

    '''
    _ortho_poly = staticmethod(chebyshevu_poly)
    eval = (lambda cls, n, x:
