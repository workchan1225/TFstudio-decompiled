# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: zeta_functions.pyc (Python 3.11)

''' Riemann zeta and related function. '''
from sympy.core.add import Add
from sympy.core.cache import cacheit
from sympy.core.function import ArgumentIndexError, expand_mul, Function
from sympy.core.numbers import pi, I, Integer
from sympy.core.relational import Eq
from sympy.core.singleton import S
from sympy.core.symbol import Dummy
from sympy.core.sympify import sympify
from sympy.functions.combinatorial.numbers import bernoulli, factorial, genocchi, harmonic
from sympy.functions.elementary.complexes import re, unpolarify, Abs, polar_lift
from sympy.functions.elementary.exponential import log, exp_polar, exp
from sympy.functions.elementary.integers import ceiling, floor
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.functions.elementary.piecewise import Piecewise
from sympy.polys.polytools import Poly

class lerchphi(Function):
    '''
    Lerch transcendent (Lerch phi function).

    Explanation
    ===========

    For $\\operatorname{Re}(a) > 0$, $|z| < 1$ and $s \\in \\mathbb{C}$, the
    Lerch transcendent is defined as

    .. math :: \\Phi(z, s, a) = \\sum_{n=0}^\\infty \\frac{z^n}{(n + a)^s},

    where the standard branch of the argument is used for $n + a$,
    and by analytic continuation for other values of the parameters.

    A commonly used related function is the Lerch zeta function, defined by

    .. math:: L(q, s, a) = \\Phi(e^{2\\pi i q}, s, a).

    **Analytic Continuation and Branching Behavior**

    It can be shown that

    .. math:: \\Phi(z, s, a) = z\\Phi(z, s, a+1) + a^{-s}.

    This provides the analytic continuation to $\\operatorname{Re}(a) \\le 0$.

    Assume now $\\operatorname{Re}(a) > 0$. The integral representation

    .. math:: \\Phi_0(z, s, a) = \\int_0^\\infty \\frac{t^{s-1} e^{-at}}{1 - ze^{-t}}
                                \\frac{\\mathrm{d}t}{\\Gamma(s)}

    provides an analytic continuation to $\\mathbb{C} - [1, \\infty)$.
    Finally, for $x \\in (1, \\infty)$ we find

    .. math:: \\lim_{\\epsilon \\to 0^+} \\Phi_0(x + i\\epsilon, s, a)
             -\\lim_{\\epsilon \\to 0^+} \\Phi_0(x - i\\epsilon, s, a)
             = \\frac{2\\pi i \\log^{s-1}{x}}{x^a \\Gamma(s)},

    using the standard branch for both $\\log{x}$ and
    $\\log{\\log{x}}$ (a branch of $\\log{\\log{x}}$ is needed to
    evaluate $\\log{x}^{s-1}$).
    This concludes the analytic continuation. The Lerch transcendent is thus
    branched at $z \\in \\{0, 1, \\infty\\}$ and
    $a \\in \\mathbb{Z}_{\\le 0}$. For fixed $z, a$ outside these
    branch points, it is an entire function of $s$.

    Examples
    ========

    The Lerch transcendent is a fairly general function, for this reason it does
    not automatically evaluate to simpler functions. Use ``expand_func()`` to
    achieve this.

    If $z=1$, the Lerch transcendent reduces to the Hurwitz zeta function:

    >>> from sympy import lerchphi, expand_func
    >>> from sympy.abc import z, s, a
    >>> expand_func(lerchphi(1, s, a))
    zeta(s, a)

    More generally, if $z$ is a root of unity, the Lerch transcendent
    reduces to a sum of Hurwitz zeta functions:

    >>> expand_func(lerchphi(-1, s, a))
    zeta(s, a/2)/2**s - zeta(s, a/2 + 1/2)/2**s

    If $a=1$, the Lerch transcendent reduces to the polylogarithm:

    >>> expand_func(lerchphi(z, s, 1))
    polylog(s, z)/z

    More generally, if $a$ is rational, the Lerch transcendent reduces
    to a sum of polylogarithms:

    >>> from sympy import S
    >>> expand_func(lerchphi(z, s, S(1)/2))
    2**(s - 1)*(polylog(s, sqrt(z))/sqrt(z) -
                polylog(s, sqrt(z)*exp_polar(I*pi))/sqrt(z))
    >>> expand_func(lerchphi(z, s, S(3)/2))
    -2**s/z + 2**(s - 1)*(polylog(s, sqrt(z))/sqrt(z) -
                          polylog(s, sqrt(z)*exp_polar(I*pi))/sqrt(z))/z

    The derivatives with respect to $z$ and $a$ can be computed in
    closed form:

    >>> lerchphi(z, s, a).diff(z)
    (-a*lerchphi(z, s, a) + lerchphi(z, s - 1, a))/z
    >>> lerchphi(z, s, a).diff(a)
    -s*lerchphi(z, s + 1, a)

    See Also
    ========

    polylog, zeta

    References
    ==========

    .. [1] Bateman, H.; Erdelyi, A. (1953), Higher Transcendental Functions,
           Vol. I, New York: McGraw-Hill. Section 1.11.
    .. [2] https://dlmf.nist.gov/25.14
    .. [3] https://en.wikipedia.org/wiki/Lerch_transcendent

    '''
    
    def _eval_expand_func(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def fdiff(self, argindex = (1,)):
        (z, s, a) = self.args
        if argindex == 3:
            return -s * lerchphi(z, s + 1, a)
        if None == 1:
            return (lerchphi(z, s - 1, a) - a * lerchphi(z, s, a)) / z
        raise None

    
    def _eval_rewrite_helper(self, target):
        res = self._eval_expand_func()
        if res.has(target):
            return res

    
    def _eval_rewrite_as_zeta(self, z, s, a, **kwargs):
        return self._eval_rewrite_helper(zeta)

    
    def _eval_rewrite_as_polylog(self, z, s, a, **kwargs):
        return self._eval_rewrite_helper(polylog)



class polylog(Function):
    pass
# WARNING: Decompyle incomplete


class zeta(Function):
    pass
# WARNING: Decompyle incomplete


class dirichlet_eta(Function):
    '''
    Dirichlet eta function.

    Explanation
    ===========

    For $\\operatorname{Re}(s) > 0$ and $0 < x \\le 1$, this function is defined as

    .. math:: \\eta(s, a) = \\sum_{n=0}^\\infty \\frac{(-1)^n}{(n+a)^s}.

    It admits a unique analytic continuation to all of $\\mathbb{C}$ for any
    fixed $a$ not a nonpositive integer. It is an entire, unbranched function.

    It can be expressed using the Hurwitz zeta function as

    .. math:: \\eta(s, a) = \\zeta(s,a) - 2^{1-s} \\zeta\\left(s, \\frac{a+1}{2}\\right)

    and using the generalized Genocchi function as

    .. math:: \\eta(s, a) = \\frac{G(1-s, a)}{2(s-1)}.

    In both cases the limiting value of $\\log2 - \\psi(a) + \\psi\\left(\\frac{a+1}{2}\\right)$
    is used when $s = 1$.

    Examples
    ========

    >>> from sympy import dirichlet_eta, zeta
    >>> from sympy.abc import s
    >>> dirichlet_eta(s).rewrite(zeta)
    Piecewise((log(2), Eq(s, 1)), ((1 - 2**(1 - s))*zeta(s), True))

    See Also
    ========

    zeta

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Dirichlet_eta_function
    .. [2] Peter Luschny, "An introduction to the Bernoulli function",
           https://arxiv.org/abs/2009.06743

    '''
    eval = (lambda cls, s, a = (None,): if a is S.One:
cls(s)# WARNING: Decompyle incomplete
)()
    
    def _eval_rewrite_as_zeta(self, s, a = (1,), **kwargs):
        digamma = digamma
        import sympy.functions.special.gamma_functions
        if a == 1:
            return Piecewise((log(2), Eq(s, 1)), ((1 - 2 ** (1 - s)) * zeta(s), True))
        return None(((log(2) - digamma(a)) + digamma((a + 1) / 2), Eq(s, 1)), (zeta(s, a) - 2 ** (1 - s) * zeta(s, (a + 1) / 2), True))

    
    def _eval_rewrite_as_genocchi(self, s, a = (S.One,), **kwargs):
        digamma = digamma
        import sympy.functions.special.gamma_functions
        return Piecewise(((log(2) - digamma(a)) + digamma((a + 1) / 2), Eq(s, 1)), (genocchi(1 - s, a) / (2 * (s - 1)), True))

    
    def _eval_evalf(self, prec):
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args()):
            return self.rewrite(zeta)._eval_evalf(prec)
        return all



class riemann_xi(Function):
    '''
    Riemann Xi function.

    Examples
    ========

    The Riemann Xi function is closely related to the Riemann zeta function.
    The zeros of Riemann Xi function are precisely the non-trivial zeros
    of the zeta function.

    >>> from sympy import riemann_xi, zeta
    >>> from sympy.abc import s
    >>> riemann_xi(s).rewrite(zeta)
    s*(s - 1)*gamma(s/2)*zeta(s)/(2*pi**(s/2))

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Riemann_Xi_function

    '''
    eval = (lambda cls, s: gamma = gammaimport sympy.functions.special.gamma_functionsz = zeta(s)if s in (S.Zero, S.One):
S.Halfif not None(z, zeta):
s * (s - 1) * gamma(s / 2) * z / (2 * pi ** (s / 2)))()
    
    def _eval_rewrite_as_zeta(self, s, **kwargs):
        gamma = gamma
        import sympy.functions.special.gamma_functions
        return s * (s - 1) * gamma(s / 2) * zeta(s) / (2 * pi ** (s / 2))



class stieltjes(Function):
    """
    Represents Stieltjes constants, $\\gamma_{k}$ that occur in
    Laurent Series expansion of the Riemann zeta function.

    Examples
    ========

    >>> from sympy import stieltjes
    >>> from sympy.abc import n, m
    >>> stieltjes(n)
    stieltjes(n)

    The zero'th stieltjes constant:

    >>> stieltjes(0)
    EulerGamma
    >>> stieltjes(0, 1)
    EulerGamma

    For generalized stieltjes constants:

    >>> stieltjes(n, m)
    stieltjes(n, m)

    Constants are only defined for integers >= 0:

    >>> stieltjes(-1)
    zoo

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Stieltjes_constants

    """
    eval = (lambda cls, n, a = (None,): pass# WARNING: Decompyle incomplete
)()

_dilogtable = (lambda : {
(1 - I) / 2: -log(2) ** 2 / 8 + pi * I * log(2) / 8 + 5 * pi ** 2 / 96 - I * S.Catalan,
1 + I: pi ** 2 / 16 + I * S.Catalan + (pi * I / 4) * log(2),
1 - I: pi ** 2 / 16 - I * S.Catalan - (pi * I / 4) * log(2),
-I: -I * S.Catalan - pi ** 2 / 48,
I: I * S.Catalan - pi ** 2 / 48,
(sqrt(5) - 1) / 2: pi ** 2 / 10 - log((sqrt(5) - 1) / 2) ** 2,
(3 - sqrt(5)) / 2: pi ** 2 / 15 - log((sqrt(5) - 1) / 2) ** 2,
-(sqrt(5) + 1) / 2: -pi ** 2 / 10 - log((sqrt(5) + 1) / 2) ** 2,
-(sqrt(5) - 1) / 2: -pi ** 2 / 15 + log((sqrt(5) - 1) / 2) ** 2 / 2,
Integer(2): pi ** 2 / 4 - I * pi * log(2),
S.Half: pi ** 2 / 12 - log(2) ** 2 / 2 })()
