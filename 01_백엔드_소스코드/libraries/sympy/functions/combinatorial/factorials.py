# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: factorials.pyc (Python 3.11)

from __future__ import annotations
from functools import reduce
from sympy.core import S, sympify, Dummy, Mod
from sympy.core.cache import cacheit
from sympy.core.function import Function, ArgumentIndexError, PoleError
from sympy.core.logic import fuzzy_and
from sympy.core.numbers import Integer, pi, I
from sympy.core.relational import Eq
from sympy.external.gmpy import gmpy as _gmpy
from sympy.ntheory import sieve
from sympy.ntheory.residue_ntheory import binomial_mod
from sympy.polys.polytools import Poly
from math import factorial as _factorial, prod, sqrt as _sqrt

class CombinatorialFunction(Function):
    '''Base class for combinatorial functions. '''
    
    def _eval_simplify(self, **kwargs):
        combsimp = combsimp
        import sympy.simplify.combsimp
        expr = combsimp(self)
        measure = kwargs['measure']
        if measure(expr) <= kwargs['ratio'] * measure(self):
            return expr



class factorial(CombinatorialFunction):
    """Implementation of factorial function over nonnegative integers.
       By convention (consistent with the gamma function and the binomial
       coefficients), factorial of a negative integer is complex infinity.

       The factorial is very important in combinatorics where it gives
       the number of ways in which `n` objects can be permuted. It also
       arises in calculus, probability, number theory, etc.

       There is strict relation of factorial with gamma function. In
       fact `n! = gamma(n+1)` for nonnegative integers. Rewrite of this
       kind is very useful in case of combinatorial simplification.

       Computation of the factorial is done using two algorithms. For
       small arguments a precomputed look up table is used. However for bigger
       input algorithm Prime-Swing is used. It is the fastest algorithm
       known and computes `n!` via prime factorization of special class
       of numbers, called here the 'Swing Numbers'.

       Examples
       ========

       >>> from sympy import Symbol, factorial, S
       >>> n = Symbol('n', integer=True)

       >>> factorial(0)
       1

       >>> factorial(7)
       5040

       >>> factorial(-2)
       zoo

       >>> factorial(n)
       factorial(n)

       >>> factorial(2*n)
       factorial(2*n)

       >>> factorial(S(1)/2)
       factorial(1/2)

       See Also
       ========

       factorial2, RisingFactorial, FallingFactorial
    """
    
    def fdiff(self, argindex = (1,)):
        gamma = gamma
        polygamma = polygamma
        import sympy.functions.special.gamma_functions
        if argindex == 1:
            return gamma(self.args[0] + 1) * polygamma(0, self.args[0] + 1)
        raise None(self, argindex)

    _small_swing = [
        1,
        1,
        1,
        3,
        3,
        15,
        5,
        35,
        35,
        315,
        63,
        693,
        231,
        3003,
        429,
        6435,
        6435,
        109395,
        12155,
        230945,
        46189,
        969969,
        88179,
        2028117,
        676039,
        16900975,
        1300075,
        35102025,
        5014575,
        145422675,
        9694845,
        300540195,
        300540195]
    _small_factorials: 'list[int]' = []
    _swing = (lambda cls, n: if n < 33:
cls._small_swing[n]primes = []N = None(_sqrt(n))for prime in sieve.primerange(3, N + 1):
q = np = 1q //= primeif q > 0:
if q & 1 == 1:
p *= primeif p > 1:
primes.append(p)for prime in sieve.primerange(N + 1, n // 3 + 1):
if n // prime & 1 == 1:
primes.append(prime)L_product = prod(sieve.primerange(n // 2 + 1, n + 1))R_product = prod(primes)L_product * R_product)()
    _recursive = (lambda cls, n: if n < 2:
1None._recursive(n // 2) ** 2 * cls._swing(n))()
    eval = (lambda cls, n: n = sympify(n)# WARNING: Decompyle incomplete
)()
    
    def _facmod(self, n, q):
        N = int(_sqrt(n))
        res = 1
        pw = [
            1] * N
        m = 2
    # WARNING: Decompyle incomplete

    
    def _eval_Mod(self, q):
        n = self.args[0]
        if n.is_integer or n.is_nonnegative or q.is_integer:
            aq = abs(q)
            d = aq - n
            if d.is_nonpositive:
                return S.Zero
            isprime = None.is_prime
            if d == 1:
                if isprime:
                    return -1 % q
                if None is False or (aq - 6).is_nonnegative:
                    return S.Zero
                return None
            return None
        if None.is_Integer or q.is_Integer:
            (n, d, aq) = map(int, (n, d, aq))
            if isprime and d - 1 < n:
                fc = self._facmod(d - 1, aq)
                fc = pow(fc, aq - 2, aq)
                if d % 2:
                    fc = -fc
                else:
                    fc = self._facmod(n, aq)
            return fc % q
        return None
        return None
        return None
        return None

    
    def _eval_rewrite_as_gamma(self, n, piecewise = (True,), **kwargs):
        gamma = gamma
        import sympy.functions.special.gamma_functions
        return gamma(n + 1)

    
    def _eval_rewrite_as_Product(self, n, **kwargs):
        Product = Product
        import sympy.concrete.products
        if n.is_nonnegative or n.is_integer:
            i = Dummy('i', integer = True)
            return Product(i, (i, 1, n))
        return None

    
    def _eval_is_integer(self):
        if self.args[0].is_integer or self.args[0].is_nonnegative:
            return True
        return None

    
    def _eval_is_positive(self):
        if self.args[0].is_integer or self.args[0].is_nonnegative:
            return True
        return None

    
    def _eval_is_even(self):
        x = self.args[0]
        if x.is_integer or x.is_nonnegative:
            return (x - 2).is_nonnegative
        return None

    
    def _eval_is_composite(self):
        x = self.args[0]
        if x.is_integer or x.is_nonnegative:
            return (x - 3).is_nonnegative
        return None

    
    def _eval_is_real(self):
        x = self.args[0]
        if x.is_nonnegative or x.is_noninteger:
            return True

    
    def _eval_as_leading_term(self, x, logx, cdir = (None, 0)):
        arg = self.args[0].as_leading_term(x)
        arg0 = arg.subs(x, 0)
        if arg0.is_zero:
            return S.One
        if not None.is_infinite:
            return self.func(arg)
        raise None('Cannot expand %s around 0' % self)



class MultiFactorial(CombinatorialFunction):
    pass


class subfactorial(CombinatorialFunction):
    '''The subfactorial counts the derangements of $n$ items and is
    defined for non-negative integers as:

    .. math:: !n = \\begin{cases} 1 & n = 0 \\\\ 0 & n = 1 \\\\
                    (n-1)(!(n-1) + !(n-2)) & n > 1 \\end{cases}

    It can also be written as ``int(round(n!/exp(1)))`` but the
    recursive definition with caching is implemented for this function.

    An interesting analytic expression is the following [2]_

    .. math:: !x = \\Gamma(x + 1, -1)/e

    which is valid for non-negative integers `x`. The above formula
    is not very useful in case of non-integers. `\\Gamma(x + 1, -1)` is
    single-valued only for integral arguments `x`, elsewhere on the positive
    real axis it has an infinite number of branches none of which are real.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Subfactorial
    .. [2] https://mathworld.wolfram.com/Subfactorial.html

    Examples
    ========

    >>> from sympy import subfactorial
    >>> from sympy.abc import n
    >>> subfactorial(n + 1)
    subfactorial(n + 1)
    >>> subfactorial(5)
    44

    See Also
    ========

    factorial, uppergamma,
    sympy.utilities.iterables.generate_derangements
    '''
    _eval = (lambda self, n: if not n:
S.Oneif None == 1:
S.Zero(z1, z2) = Nonefor i in range(2, n + 1):
z2 = (i - 1) * (z2 + z1)z1 = z2z2)()()
    eval = (lambda cls, arg: if arg.is_Number:
if arg.is_Integer and arg.is_nonnegative:
cls._eval(arg)if None is S.NaN:
S.NaNif None is S.Infinity:
S.InfinityNone)()
    
    def _eval_is_even(self):
        if self.args[0].is_odd or self.args[0].is_nonnegative:
            return True
        return None

    
    def _eval_is_integer(self):
        if self.args[0].is_integer or self.args[0].is_nonnegative:
            return True
        return None

    
    def _eval_rewrite_as_factorial(self, arg, **kwargs):
        summation = summation
        import sympy.concrete.summations
        i = Dummy('i')
        f = S.NegativeOne ** i / factorial(i)
        return factorial(arg) * summation(f, (i, 0, arg))

    
    def _eval_rewrite_as_gamma(self, arg, piecewise = (True,), **kwargs):
        exp = exp
        import sympy.functions.elementary.exponential
        gamma = gamma
        lowergamma = lowergamma
        import sympy.functions.special.gamma_functions
        return (S.NegativeOne ** (arg + 1) * exp(-I * pi * arg) * lowergamma(arg + 1, -1) + gamma(arg + 1)) * exp(-1)

    
    def _eval_rewrite_as_uppergamma(self, arg, **kwargs):
        uppergamma = uppergamma
        import sympy.functions.special.gamma_functions
        return uppergamma(arg + 1, -1) / S.Exp1

    
    def _eval_is_nonnegative(self):
        if self.args[0].is_integer or self.args[0].is_nonnegative:
            return True
        return None

    
    def _eval_is_odd(self):
        if self.args[0].is_even or self.args[0].is_nonnegative:
            return True
        return None



class factorial2(CombinatorialFunction):
    """The double factorial `n!!`, not to be confused with `(n!)!`

    The double factorial is defined for nonnegative integers and for odd
    negative integers as:

    .. math:: n!! = \\begin{cases} 1 & n = 0 \\\\
                    n(n-2)(n-4) \\cdots 1 & n\\ \\text{positive odd} \\\\
                    n(n-2)(n-4) \\cdots 2 & n\\ \\text{positive even} \\\\
                    (n+2)!!/(n+2) & n\\ \\text{negative odd} \\end{cases}

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Double_factorial

    Examples
    ========

    >>> from sympy import factorial2, var
    >>> n = var('n')
    >>> n
    n
    >>> factorial2(n + 1)
    factorial2(n + 1)
    >>> factorial2(5)
    15
    >>> factorial2(-1)
    1
    >>> factorial2(-5)
    1/3

    See Also
    ========

    factorial, RisingFactorial, FallingFactorial
    """
    eval = (lambda cls, arg: if arg.is_Number:
if not arg.is_Integer:
raise ValueError('argument must be nonnegative integer or negative odd integer')if arg.is_nonnegative:
if arg.is_even:
k = arg / 22 ** k * factorial(k)None(arg) / factorial2(arg - 1)if None.is_odd:
arg * S.NegativeOne ** ((1 - arg) / 2) / factorial2(-arg)raise None('argument must be nonnegative integer or negative odd integer'))()
    
    def _eval_is_even(self):
        n = self.args[0]
        if n.is_integer:
            if n.is_odd:
                return False
            if None.is_even:
                if n.is_positive:
                    return True
                if None.is_zero:
                    return False
                return None
            return None

    
    def _eval_is_integer(self):
        n = self.args[0]
        if n.is_integer:
            if (n + 1).is_nonnegative:
                return True
            if None.is_odd:
                return (n + 3).is_nonnegative
            return None

    
    def _eval_is_odd(self):
        n = self.args[0]
        if n.is_odd:
            return (n + 3).is_nonnegative
        if None.is_even:
            if n.is_positive:
                return False
            if None.is_zero:
                return True
            return None

    
    def _eval_is_positive(self):
        n = self.args[0]
        if n.is_integer:
            if (n + 1).is_nonnegative:
                return True
            if None.is_odd:
                return ((n + 1) / 2).is_even
            return None

    
    def _eval_rewrite_as_gamma(self, n, piecewise = (True,), **kwargs):
        sqrt = sqrt
        import sympy.functions.elementary.miscellaneous
        Piecewise = Piecewise
        import sympy.functions.elementary.piecewise
        gamma = gamma
        import sympy.functions.special.gamma_functions
        return 2 ** (n / 2) * gamma(n / 2 + 1) * Piecewise((1, Eq(Mod(n, 2), 0)), (sqrt(2 / pi), Eq(Mod(n, 2), 1)))



class RisingFactorial(CombinatorialFunction):
    '''
    Rising factorial (also called Pochhammer symbol [1]_) is a double valued
    function arising in concrete mathematics, hypergeometric functions
    and series expansions. It is defined by:

    .. math:: \\texttt{rf(y, k)} = (x)^k = x \\cdot (x+1) \\cdots (x+k-1)

    where `x` can be arbitrary expression and `k` is an integer. For
    more information check "Concrete mathematics" by Graham, pp. 66
    or visit https://mathworld.wolfram.com/RisingFactorial.html page.

    When `x` is a `~.Poly` instance of degree $\\ge 1$ with a single variable,
    `(x)^k = x(y) \\cdot x(y+1) \\cdots x(y+k-1)`, where `y` is the
    variable of `x`. This is as described in [2]_.

    Examples
    ========

    >>> from sympy import rf, Poly
    >>> from sympy.abc import x
    >>> rf(x, 0)
    1
    >>> rf(1, 5)
    120
    >>> rf(x, 5) == x*(1 + x)*(2 + x)*(3 + x)*(4 + x)
    True
    >>> rf(Poly(x**3, x), 2)
    Poly(x**6 + 3*x**5 + 3*x**4 + x**3, x, domain=\'ZZ\')

    Rewriting is complicated unless the relationship between
    the arguments is known, but rising factorial can
    be rewritten in terms of gamma, factorial, binomial,
    and falling factorial.

    >>> from sympy import Symbol, factorial, ff, binomial, gamma
    >>> n = Symbol(\'n\', integer=True, positive=True)
    >>> R = rf(n, n + 2)
    >>> for i in (rf, ff, factorial, binomial, gamma):
    ...  R.rewrite(i)
    ...
    RisingFactorial(n, n + 2)
    FallingFactorial(2*n + 1, n + 2)
    factorial(2*n + 1)/factorial(n - 1)
    binomial(2*n + 1, n + 2)*factorial(n + 2)
    gamma(2*n + 2)/gamma(n)

    See Also
    ========

    factorial, factorial2, FallingFactorial

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Pochhammer_symbol
    .. [2] Peter Paule, "Greatest Factorial Factorization and Symbolic
           Summation", Journal of Symbolic Computation, vol. 20, pp. 235-268,
           1995.

    '''
    eval = (lambda cls, x, k: pass# WARNING: Decompyle incomplete
)()
    
    def _eval_rewrite_as_gamma(self, x, k, piecewise = (True,), **kwargs):
        Piecewise = Piecewise
        import sympy.functions.elementary.piecewise
        gamma = gamma
        import sympy.functions.special.gamma_functions
        if not piecewise:
            if x <= 0 == True:
                return S.NegativeOne ** k * gamma(1 - x) / gamma((-k - x) + 1)
            return gamma(x + k) / gamma(x)
        return Piecewise((gamma(x + k) / gamma(x), x > 0), (S.NegativeOne ** k * gamma(1 - x) / gamma((-k - x) + 1), True))

    
    def _eval_rewrite_as_FallingFactorial(self, x, k, **kwargs):
        return FallingFactorial(x + k - 1, k)

    
    def _eval_rewrite_as_factorial(self, x, k, **kwargs):
        Piecewise = Piecewise
        import sympy.functions.elementary.piecewise
        if x.is_integer or k.is_integer:
            return Piecewise((factorial(k + x - 1) / factorial(x - 1), x > 0), (S.NegativeOne ** k * factorial(-x) / factorial(-k - x), True))
        return None

    
    def _eval_rewrite_as_binomial(self, x, k, **kwargs):
        if k.is_integer:
            return factorial(k) * binomial(x + k - 1, k)

    
    def _eval_rewrite_as_tractable(self, x, k, limitvar = (None,), **kwargs):
