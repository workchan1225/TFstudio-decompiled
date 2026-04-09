# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_functions.pyc (Python 3.11)

from sympy.core import S
from sympy.core.function import Function, ArgumentIndexError
from sympy.core.symbol import Dummy, uniquely_named_symbol
from sympy.functions.special.gamma_functions import gamma, digamma
from sympy.functions.combinatorial.numbers import catalan
from sympy.functions.elementary.complexes import conjugate

def betainc_mpmath_fix(a, b, x1, x2, reg = (0,)):
    betainc = betainc
    mpf = mpf
    import mpmath
    if x1 == x2:
        return mpf(0)
    return betainc(a, b, x1, x2, reg)


class beta(Function):
    """
    The beta integral is called the Eulerian integral of the first kind by
    Legendre:

    .. math::
        \\mathrm{B}(x,y)  \\int^{1}_{0} t^{x-1} (1-t)^{y-1} \\mathrm{d}t.

    Explanation
    ===========

    The Beta function or Euler's first integral is closely associated
    with the gamma function. The Beta function is often used in probability
    theory and mathematical statistics. It satisfies properties like:

    .. math::
        \\mathrm{B}(a,1) = \\frac{1}{a} \\\\
        \\mathrm{B}(a,b) = \\mathrm{B}(b,a)  \\\\
        \\mathrm{B}(a,b) = \\frac{\\Gamma(a) \\Gamma(b)}{\\Gamma(a+b)}

    Therefore for integral values of $a$ and $b$:

    .. math::
        \\mathrm{B} = \\frac{(a-1)! (b-1)!}{(a+b-1)!}

    A special case of the Beta function when `x = y` is the
    Central Beta function. It satisfies properties like:

    .. math::
        \\mathrm{B}(x) = 2^{1 - 2x}\\mathrm{B}(x, \\frac{1}{2})
        \\mathrm{B}(x) = 2^{1 - 2x} cos(\\pi x) \\mathrm{B}(\\frac{1}{2} - x, x)
        \\mathrm{B}(x) = \\int_{0}^{1} \\frac{t^x}{(1 + t)^{2x}} dt
        \\mathrm{B}(x) = \\frac{2}{x} \\prod_{n = 1}^{\\infty} \\frac{n(n + 2x)}{(n + x)^2}

    Examples
    ========

    >>> from sympy import I, pi
    >>> from sympy.abc import x, y

    The Beta function obeys the mirror symmetry:

    >>> from sympy import beta, conjugate
    >>> conjugate(beta(x, y))
    beta(conjugate(x), conjugate(y))

    Differentiation with respect to both $x$ and $y$ is supported:

    >>> from sympy import beta, diff
    >>> diff(beta(x, y), x)
    (polygamma(0, x) - polygamma(0, x + y))*beta(x, y)

    >>> diff(beta(x, y), y)
    (polygamma(0, y) - polygamma(0, x + y))*beta(x, y)

    >>> diff(beta(x), x)
    2*(polygamma(0, x) - polygamma(0, 2*x))*beta(x, x)

    We can numerically evaluate the Beta function to
    arbitrary precision for any complex numbers x and y:

    >>> from sympy import beta
    >>> beta(pi).evalf(40)
    0.02671848900111377452242355235388489324562

    >>> beta(1 + I).evalf(20)
    -0.2112723729365330143 - 0.7655283165378005676*I

    See Also
    ========

    gamma: Gamma function.
    uppergamma: Upper incomplete gamma function.
    lowergamma: Lower incomplete gamma function.
    polygamma: Polygamma function.
    loggamma: Log Gamma function.
    digamma: Digamma function.
    trigamma: Trigamma function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Beta_function
    .. [2] https://mathworld.wolfram.com/BetaFunction.html
    .. [3] https://dlmf.nist.gov/5.12

    """
    unbranched = True
    
    def fdiff(self, argindex):
        (x, y) = self.args
        if argindex == 1:
            return beta(x, y) * (digamma(x) - digamma(x + y))
        if None == 2:
            return beta(x, y) * (digamma(y) - digamma(x + y))
        raise None(self, argindex)

    eval = (lambda cls, x, y = (None,): pass# WARNING: Decompyle incomplete
)()
    
    def doit(self, **hints):
        x = self.args[0]
        xold = self.args[0]
        single_argument = len(self.args) == 1
        y = self.args[0] if single_argument else self.args[1]
        yold = self.args[0] if single_argument else self.args[1]
    # WARNING: Decompyle incomplete

    
    def _eval_expand_func(self, **hints):
        (x, y) = self.args
        return gamma(x) * gamma(y) / gamma(x + y)

    
    def _eval_is_real(self):
