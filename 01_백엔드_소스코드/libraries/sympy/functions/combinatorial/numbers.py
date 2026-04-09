# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: numbers.pyc (Python 3.11)

"""
This module implements some special functions that commonly appear in
combinatorial contexts (e.g. in power series); in particular,
sequences of rational numbers such as Bernoulli and Fibonacci numbers.

Factorials, binomial coefficients and related functions are located in
the separate 'factorials' module.
"""
from math import prod
from collections import defaultdict
from typing import Tuple as tTuple
from sympy.core import S, Symbol, Add, Dummy
from sympy.core.cache import cacheit
from sympy.core.containers import Dict
from sympy.core.expr import Expr
from sympy.core.function import ArgumentIndexError, Function, expand_mul
from sympy.core.logic import fuzzy_not
from sympy.core.mul import Mul
from sympy.core.numbers import E, I, pi, oo, Rational, Integer
from sympy.core.relational import Eq, is_le, is_gt, is_lt
from sympy.external.gmpy import SYMPY_INTS, remove, lcm, legendre, jacobi, kronecker
from sympy.functions.combinatorial.factorials import binomial, factorial, subfactorial
from sympy.functions.elementary.exponential import log
from sympy.functions.elementary.piecewise import Piecewise
from sympy.ntheory.factor_ import factorint, _divisor_sigma, is_carmichael, find_carmichael_numbers_in_range, find_first_n_carmichaels
from sympy.ntheory.generate import _primepi
from sympy.ntheory.partitions_ import _partition, _partition_rec
from sympy.ntheory.primetest import isprime, is_square
from sympy.polys.appellseqs import bernoulli_poly, euler_poly, genocchi_poly
from sympy.polys.polytools import cancel
from sympy.utilities.enumerative import MultisetPartitionTraverser
from sympy.utilities.exceptions import sympy_deprecation_warning
from sympy.utilities.iterables import multiset, multiset_derangements, iterable
from sympy.utilities.memoization import recurrence_memo
from sympy.utilities.misc import as_int
from mpmath import mp, workprec
from mpmath.libmp import ifib as _ifib

def _product(a, b):
    return prod(range(a, b + 1))

_sym = Symbol('x')

class carmichael(Function):
    """
    Carmichael Numbers:

    Certain cryptographic algorithms make use of big prime numbers.
    However, checking whether a big number is prime is not so easy.
    Randomized prime number checking tests exist that offer a high degree of
    confidence of accurate determination at low cost, such as the Fermat test.

    Let 'a' be a random number between $2$ and $n - 1$, where $n$ is the
    number whose primality we are testing. Then, $n$ is probably prime if it
    satisfies the modular arithmetic congruence relation:

    .. math :: a^{n-1} = 1 \\pmod{n}

    (where mod refers to the modulo operation)

    If a number passes the Fermat test several times, then it is prime with a
    high probability.

    Unfortunately, certain composite numbers (non-primes) still pass the Fermat
    test with every number smaller than themselves.
    These numbers are called Carmichael numbers.

    A Carmichael number will pass a Fermat primality test to every base $b$
    relatively prime to the number, even though it is not actually prime.
    This makes tests based on Fermat's Little Theorem less effective than
    strong probable prime tests such as the Baillie-PSW primality test and
    the Miller-Rabin primality test.

    Examples
    ========

    >>> from sympy.ntheory.factor_ import find_first_n_carmichaels, find_carmichael_numbers_in_range
    >>> find_first_n_carmichaels(5)
    [561, 1105, 1729, 2465, 2821]
    >>> find_carmichael_numbers_in_range(0, 562)
    [561]
    >>> find_carmichael_numbers_in_range(0,1000)
    [561]
    >>> find_carmichael_numbers_in_range(0,2000)
    [561, 1105, 1729]

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Carmichael_number
    .. [2] https://en.wikipedia.org/wiki/Fermat_primality_test
    .. [3] https://www.jstor.org/stable/23248683?seq=1#metadata_info_tab_contents
    """
    is_perfect_square = (lambda n: sympy_deprecation_warning('\nis_perfect_square is just a wrapper around sympy.ntheory.primetest.is_square\nso use that directly instead.\n        ', deprecated_since_version = '1.11', active_deprecations_target = 'deprecated-carmichael-static-methods')is_square(n))()
    divides = (lambda p, n: sympy_deprecation_warning('\n        divides can be replaced by directly testing n % p == 0.\n        ', deprecated_since_version = '1.11', active_deprecations_target = 'deprecated-carmichael-static-methods')n % p == 0)()
    is_prime = (lambda n: sympy_deprecation_warning('\nis_prime is just a wrapper around sympy.ntheory.primetest.isprime so use that\ndirectly instead.\n        ', deprecated_since_version = '1.11', active_deprecations_target = 'deprecated-carmichael-static-methods')isprime(n))()
    is_carmichael = (lambda n: sympy_deprecation_warning('\nis_carmichael is just a wrapper around sympy.ntheory.factor_.is_carmichael so use that\ndirectly instead.\n        ', deprecated_since_version = '1.13', active_deprecations_target = 'deprecated-ntheory-symbolic-functions')is_carmichael(n))()
    find_carmichael_numbers_in_range = (lambda x, y: sympy_deprecation_warning('\nfind_carmichael_numbers_in_range is just a wrapper around sympy.ntheory.factor_.find_carmichael_numbers_in_range so use that\ndirectly instead.\n        ', deprecated_since_version = '1.13', active_deprecations_target = 'deprecated-ntheory-symbolic-functions')find_carmichael_numbers_in_range(x, y))()
    find_first_n_carmichaels = (lambda n: sympy_deprecation_warning('\nfind_first_n_carmichaels is just a wrapper around sympy.ntheory.factor_.find_first_n_carmichaels so use that\ndirectly instead.\n        ', deprecated_since_version = '1.13', active_deprecations_target = 'deprecated-ntheory-symbolic-functions')find_first_n_carmichaels(n))()


class fibonacci(Function):
    """
    Fibonacci numbers / Fibonacci polynomials

    The Fibonacci numbers are the integer sequence defined by the
    initial terms `F_0 = 0`, `F_1 = 1` and the two-term recurrence
    relation `F_n = F_{n-1} + F_{n-2}`.  This definition
    extended to arbitrary real and complex arguments using
    the formula

    .. math :: F_z = \\frac{\\phi^z - \\cos(\\pi z) \\phi^{-z}}{\\sqrt 5}

    The Fibonacci polynomials are defined by `F_1(x) = 1`,
    `F_2(x) = x`, and `F_n(x) = x*F_{n-1}(x) + F_{n-2}(x)` for `n > 2`.
    For all positive integers `n`, `F_n(1) = F_n`.

    * ``fibonacci(n)`` gives the `n^{th}` Fibonacci number, `F_n`
    * ``fibonacci(n, x)`` gives the `n^{th}` Fibonacci polynomial in `x`, `F_n(x)`

    Examples
    ========

    >>> from sympy import fibonacci, Symbol

    >>> [fibonacci(x) for x in range(11)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    >>> fibonacci(5, Symbol('t'))
    t**4 + 3*t**2 + 1

    See Also
    ========

    bell, bernoulli, catalan, euler, harmonic, lucas, genocchi, partition, tribonacci

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Fibonacci_number
    .. [2] https://mathworld.wolfram.com/FibonacciNumber.html

    """
    _fib = (lambda n: _ifib(n))()
    _fibpoly = (lambda n, prev: (prev[-2] + _sym * prev[-1]).expand())()()
    eval = (lambda cls, n, sym = (None,): if n is S.Infinity:
S.Infinity# WARNING: Decompyle incomplete
)()
    
    def _eval_rewrite_as_tractable(self, n, **kwargs):
        sqrt = sqrt
        cos = cos
        import sympy.functions
        return (S.GoldenRatio ** n - cos(S.Pi * n) / S.GoldenRatio ** n) / sqrt(5)

    
    def _eval_rewrite_as_sqrt(self, n, **kwargs):
        sqrt = sqrt
        import sympy.functions.elementary.miscellaneous
        return 2 ** (-n) * sqrt(5) * ((1 + sqrt(5)) ** n - (-sqrt(5) + 1) ** n) / 5

    
    def _eval_rewrite_as_GoldenRatio(self, n, **kwargs):
        return (S.GoldenRatio ** n - 1 / (-(S.GoldenRatio)) ** n) / (2 * S.GoldenRatio - 1)



class lucas(Function):
    '''
    Lucas numbers

    Lucas numbers satisfy a recurrence relation similar to that of
    the Fibonacci sequence, in which each term is the sum of the
    preceding two. They are generated by choosing the initial
    values `L_0 = 2` and `L_1 = 1`.

    * ``lucas(n)`` gives the `n^{th}` Lucas number

    Examples
    ========

    >>> from sympy import lucas

    >>> [lucas(x) for x in range(11)]
    [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123]

    See Also
    ========

    bell, bernoulli, catalan, euler, fibonacci, harmonic, genocchi, partition, tribonacci

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Lucas_number
    .. [2] https://mathworld.wolfram.com/LucasNumber.html

    '''
    eval = (lambda cls, n: if n is S.Infinity:
S.Infinityif None.is_Integer:
fibonacci(n + 1) + fibonacci(n - 1))()
    
    def _eval_rewrite_as_sqrt(self, n, **kwargs):
        sqrt = sqrt
        import sympy.functions.elementary.miscellaneous
        return 2 ** (-n) * ((1 + sqrt(5)) ** n + (-sqrt(5) + 1) ** n)



class tribonacci(Function):
    """
    Tribonacci numbers / Tribonacci polynomials

    The Tribonacci numbers are the integer sequence defined by the
    initial terms `T_0 = 0`, `T_1 = 1`, `T_2 = 1` and the three-term
    recurrence relation `T_n = T_{n-1} + T_{n-2} + T_{n-3}`.

    The Tribonacci polynomials are defined by `T_0(x) = 0`, `T_1(x) = 1`,
    `T_2(x) = x^2`, and `T_n(x) = x^2 T_{n-1}(x) + x T_{n-2}(x) + T_{n-3}(x)`
    for `n > 2`.  For all positive integers `n`, `T_n(1) = T_n`.

    * ``tribonacci(n)`` gives the `n^{th}` Tribonacci number, `T_n`
    * ``tribonacci(n, x)`` gives the `n^{th}` Tribonacci polynomial in `x`, `T_n(x)`

    Examples
    ========

    >>> from sympy import tribonacci, Symbol

    >>> [tribonacci(x) for x in range(11)]
    [0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149]
    >>> tribonacci(5, Symbol('t'))
    t**8 + 3*t**5 + 3*t**2

    See Also
    ========

    bell, bernoulli, catalan, euler, fibonacci, harmonic, lucas, genocchi, partition

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Generalizations_of_Fibonacci_numbers#Tribonacci_numbers
    .. [2] https://mathworld.wolfram.com/TribonacciNumber.html
    .. [3] https://oeis.org/A000073

    """
    _trib = (lambda n, prev: prev[-3] + prev[-2] + prev[-1])()()
    _tribpoly = (lambda n, prev: (prev[-3] + _sym * prev[-2] + _sym ** 2 * prev[-1]).expand())()()
    eval = (lambda cls, n, sym = (None,): if n is S.Infinity:
S.Infinity# WARNING: Decompyle incomplete
)()
    
    def _eval_rewrite_as_sqrt(self, n, **kwargs):
        cbrt = cbrt
        sqrt = sqrt
        import sympy.functions.elementary.miscellaneous
        w = (-1 + S.ImaginaryUnit * sqrt(3)) / 2
        a = (1 + cbrt(19 + 3 * sqrt(33)) + cbrt(19 - 3 * sqrt(33))) / 3
        b = (1 + w * cbrt(19 + 3 * sqrt(33)) + w ** 2 * cbrt(19 - 3 * sqrt(33))) / 3
        c = (1 + w ** 2 * cbrt(19 + 3 * sqrt(33)) + w * cbrt(19 - 3 * sqrt(33))) / 3
        Tn = a ** (n + 1) / ((a - b) * (a - c)) + b ** (n + 1) / ((b - a) * (b - c)) + c ** (n + 1) / ((c - a) * (c - b))
        return Tn

    
    def _eval_rewrite_as_TribonacciConstant(self, n, **kwargs):
        floor = floor
        import sympy.functions.elementary.integers
        cbrt = cbrt
        sqrt = sqrt
        import sympy.functions.elementary.miscellaneous
        b = cbrt(586 + 102 * sqrt(33))
        Tn = 3 * b * S.TribonacciConstant ** n / ((b ** 2 - 2 * b) + 4)
        return floor(Tn + S.Half)



class bernoulli(Function):
    args: tTuple[Integer] = '\n    Bernoulli numbers / Bernoulli polynomials / Bernoulli function\n\n    The Bernoulli numbers are a sequence of rational numbers\n    defined by `B_0 = 1` and the recursive relation (`n > 0`):\n\n    .. math :: n+1 = \\sum_{k=0}^n \\binom{n+1}{k} B_k\n\n    They are also commonly defined by their exponential generating\n    function, which is `\\frac{x}{1 - e^{-x}}`. For odd indices > 1,\n    the Bernoulli numbers are zero.\n\n    The Bernoulli polynomials satisfy the analogous formula:\n\n    .. math :: B_n(x) = \\sum_{k=0}^n (-1)^k \\binom{n}{k} B_k x^{n-k}\n\n    Bernoulli numbers and Bernoulli polynomials are related as\n    `B_n(1) = B_n`.\n\n    The generalized Bernoulli function `\\operatorname{B}(s, a)`\n    is defined for any complex `s` and `a`, except where `a` is a\n    nonpositive integer and `s` is not a nonnegative integer. It is\n    an entire function of `s` for fixed `a`, related to the Hurwitz\n    zeta function by\n\n    .. math:: \\operatorname{B}(s, a) = \\begin{cases}\n              -s \\zeta(1-s, a) & s \\ne 0 \\\\ 1 & s = 0 \\end{cases}\n\n    When `s` is a nonnegative integer this function reduces to the\n    Bernoulli polynomials: `\\operatorname{B}(n, x) = B_n(x)`. When\n    `a` is omitted it is assumed to be 1, yielding the (ordinary)\n    Bernoulli function which interpolates the Bernoulli numbers and is\n    related to the Riemann zeta function.\n\n    We compute Bernoulli numbers using Ramanujan\'s formula:\n\n    .. math :: B_n = \\frac{A(n) - S(n)}{\\binom{n+3}{n}}\n\n    where:\n\n    .. math :: A(n) = \\begin{cases} \\frac{n+3}{3} &\n        n \\equiv 0\\ \\text{or}\\ 2 \\pmod{6} \\\\\n        -\\frac{n+3}{6} & n \\equiv 4 \\pmod{6} \\end{cases}\n\n    and:\n\n    .. math :: S(n) = \\sum_{k=1}^{[n/6]} \\binom{n+3}{n-6k} B_{n-6k}\n\n    This formula is similar to the sum given in the definition, but\n    cuts `\\frac{2}{3}` of the terms. For Bernoulli polynomials, we use\n    Appell sequences.\n\n    For `n` a nonnegative integer and `s`, `a`, `x` arbitrary complex numbers,\n\n    * ``bernoulli(n)`` gives the nth Bernoulli number, `B_n`\n    * ``bernoulli(s)`` gives the Bernoulli function `\\operatorname{B}(s)`\n    * ``bernoulli(n, x)`` gives the nth Bernoulli polynomial in `x`, `B_n(x)`\n    * ``bernoulli(s, a)`` gives the generalized Bernoulli function\n      `\\operatorname{B}(s, a)`\n\n    .. versionchanged:: 1.12\n        ``bernoulli(1)`` gives `+\\frac{1}{2}` instead of `-\\frac{1}{2}`.\n        This choice of value confers several theoretical advantages [5]_,\n        including the extension to complex parameters described above\n        which this function now implements. The previous behavior, defined\n        only for nonnegative integers `n`, can be obtained with\n        ``(-1)**n*bernoulli(n)``.\n\n    Examples\n    ========\n\n    >>> from sympy import bernoulli\n    >>> from sympy.abc import x\n    >>> [bernoulli(n) for n in range(11)]\n    [1, 1/2, 1/6, 0, -1/30, 0, 1/42, 0, -1/30, 0, 5/66]\n    >>> bernoulli(1000001)\n    0\n    >>> bernoulli(3, x)\n    x**3 - 3*x**2/2 + x/2\n\n    See Also\n    ========\n\n    andre, bell, catalan, euler, fibonacci, harmonic, lucas, genocchi,\n    partition, tribonacci, sympy.polys.appellseqs.bernoulli_poly\n\n    References\n    ==========\n\n    .. [1] https://en.wikipedia.org/wiki/Bernoulli_number\n    .. [2] https://en.wikipedia.org/wiki/Bernoulli_polynomial\n    .. [3] https://mathworld.wolfram.com/BernoulliNumber.html\n    .. [4] https://mathworld.wolfram.com/BernoulliPolynomial.html\n    .. [5] Peter Luschny, "The Bernoulli Manifesto",\n           https://luschny.de/math/zeta/The-Bernoulli-Manifesto.html\n    .. [6] Peter Luschny, "An introduction to the Bernoulli function",\n           https://arxiv.org/abs/2009.06743\n\n    '
    _calc_bernoulli = (lambda n: s = 0a = int(binomial(n + 3, n - 6))for j in range(1, n // 6 + 1):
s += a * bernoulli(n - 6 * j)a *= _product((n - 6 - 6 * j) + 1, n - 6 * j)a //= _product(6 * j + 4, 6 * j + 9)if n % 6 == 4:
s = -Rational(n + 3, 6) - selse:
s = Rational(n + 3, 3) - ss / binomial(n + 3, n))()
    _cache = {
        0: S.One,
        1: Rational(1, 2),
        2: Rational(1, 6),
        4: Rational(-1, 30) }
    _highest = {
        0: 0,
        1: 1,
        2: 2,
        4: 4 }
    eval = (lambda cls, n, x = (None,): if x is S.One:
cls(n)if None.is_zero:
S.One# WARNING: Decompyle incomplete
)()
    
    def _eval_rewrite_as_zeta(self, n, x = (1,), **kwargs):
        zeta = zeta
        import sympy.functions.special.zeta_functions
        return Piecewise((1, Eq(n, 0)), (-n * zeta(1 - n, x), True))

    
    def _eval_evalf(self, prec):
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args()):
            return None
        n = all.args[0]._to_mpmath(prec)
        x = self.args[1] if len(self.args) > 1 else S.One._to_mpmath(prec)
        workprec(prec)
        if n == 0:
            res = mp.mpf(1)
        elif n == 1:
            res = x - mp.mpf(0.5)
        elif mp.isint(n) and n >= 0:
            res = mp.bernoulli(n) if x == 1 else mp.bernpoly(n, x)
        else:
            res = -n * mp.zeta(1 - n, x)
        None(None, None)



class bell(Function):
    '''
    Bell numbers / Bell polynomials

    The Bell numbers satisfy `B_0 = 1` and

    .. math:: B_n = \\sum_{k=0}^{n-1} \\binom{n-1}{k} B_k.

    They are also given by:

    .. math:: B_n = \\frac{1}{e} \\sum_{k=0}^{\\infty} \\frac{k^n}{k!}.

    The Bell polynomials are given by `B_0(x) = 1` and

    .. math:: B_n(x) = x \\sum_{k=1}^{n-1} \\binom{n-1}{k-1} B_{k-1}(x).

    The second kind of Bell polynomials (are sometimes called "partial" Bell
    polynomials or incomplete Bell polynomials) are defined as

    .. math:: B_{n,k}(x_1, x_2,\\dotsc x_{n-k+1}) =
            \\sum_{j_1+j_2+j_2+\\dotsb=k \\atop j_1+2j_2+3j_2+\\dotsb=n}
                \\frac{n!}{j_1!j_2!\\dotsb j_{n-k+1}!}
                \\left(\\frac{x_1}{1!} \\right)^{j_1}
                \\left(\\frac{x_2}{2!} \\right)^{j_2} \\dotsb
                \\left(\\frac{x_{n-k+1}}{(n-k+1)!} \\right) ^{j_{n-k+1}}.

    * ``bell(n)`` gives the `n^{th}` Bell number, `B_n`.
    * ``bell(n, x)`` gives the `n^{th}` Bell polynomial, `B_n(x)`.
    * ``bell(n, k, (x1, x2, ...))`` gives Bell polynomials of the second kind,
      `B_{n,k}(x_1, x_2, \\dotsc, x_{n-k+1})`.

    Notes
    =====

    Not to be confused with Bernoulli numbers and Bernoulli polynomials,
    which use the same notation.

    Examples
    ========

    >>> from sympy import bell, Symbol, symbols

    >>> [bell(n) for n in range(11)]
    [1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147, 115975]
    >>> bell(30)
    846749014511809332450147
    >>> bell(4, Symbol(\'t\'))
    t**4 + 6*t**3 + 7*t**2 + t
    >>> bell(6, 2, symbols(\'x:6\')[1:])
    6*x1*x5 + 15*x2*x4 + 10*x3**2

    See Also
    ========

    bernoulli, catalan, euler, fibonacci, harmonic, lucas, genocchi, partition, tribonacci

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Bell_number
    .. [2] https://mathworld.wolfram.com/BellNumber.html
    .. [3] https://mathworld.wolfram.com/BellPolynomial.html

    '''
    _bell = (lambda n, prev: s = 1a = 1for k in range(1, n):
a = a * (n - k) // ks += a * prev[k]s)()()
    _bell_poly = (lambda n, prev: s = 1a = 1for k in range(2, n + 1):
a = a * ((n - k) + 1) // (k - 1)s += a * prev[k - 1]expand_mul(_sym * s))()()
    _bell_incomplete_poly = (lambda n, k, symbols: if n == 0 and k == 0:
S.Oneif None == 0 or k == 0:
S.Zeros = None.Zeroa = S.Onefor m in range(1, (n - k) + 2):
s += a * bell._bell_incomplete_poly(n - m, k - 1, symbols) * symbols[m - 1]a = a * (n - m) / mexpand_mul(s))()
    eval = (lambda cls, n, k_sym, symbols = (None, None): pass# WARNING: Decompyle incomplete
)()
    
    def _eval_rewrite_as_Sum(self, n, k_sym, symbols = (None, None), **kwargs):
        Sum = Sum
        import sympy.concrete.summations
    # WARNING: Decompyle incomplete



class harmonic(Function):
    '''
    Harmonic numbers

    The nth harmonic number is given by `\\operatorname{H}_{n} =
    1 + \\frac{1}{2} + \\frac{1}{3} + \\ldots + \\frac{1}{n}`.

    More generally:

    .. math:: \\operatorname{H}_{n,m} = \\sum_{k=1}^{n} \\frac{1}{k^m}

    As `n \\rightarrow \\infty`, `\\operatorname{H}_{n,m} \\rightarrow \\zeta(m)`,
    the Riemann zeta function.

    * ``harmonic(n)`` gives the nth harmonic number, `\\operatorname{H}_n`

    * ``harmonic(n, m)`` gives the nth generalized harmonic number
      of order `m`, `\\operatorname{H}_{n,m}`, where
      ``harmonic(n) == harmonic(n, 1)``

    This function can be extended to complex `n` and `m` where `n` is not a
    negative integer or `m` is a nonpositive integer as

    .. math:: \\operatorname{H}_{n,m} = \\begin{cases} \\zeta(m) - \\zeta(m, n+1)
            & m \\ne 1 \\\\ \\psi(n+1) + \\gamma & m = 1 \\end{cases}

    Examples
    ========

    >>> from sympy import harmonic, oo

    >>> [harmonic(n) for n in range(6)]
    [0, 1, 3/2, 11/6, 25/12, 137/60]
    >>> [harmonic(n, 2) for n in range(6)]
    [0, 1, 5/4, 49/36, 205/144, 5269/3600]
    >>> harmonic(oo, 2)
    pi**2/6

    >>> from sympy import Symbol, Sum
    >>> n = Symbol("n")

    >>> harmonic(n).rewrite(Sum)
    Sum(1/_k, (_k, 1, n))

    We can evaluate harmonic numbers for all integral and positive
    rational arguments:

    >>> from sympy import S, expand_func, simplify
    >>> harmonic(8)
    761/280
    >>> harmonic(11)
    83711/27720

    >>> H = harmonic(1/S(3))
    >>> H
    harmonic(1/3)
    >>> He = expand_func(H)
    >>> He
    -log(6) - sqrt(3)*pi/6 + 2*Sum(log(sin(_k*pi/3))*cos(2*_k*pi/3), (_k, 1, 1))
                           + 3*Sum(1/(3*_k + 1), (_k, 0, 0))
    >>> He.doit()
    -log(6) - sqrt(3)*pi/6 - log(sqrt(3)/2) + 3
    >>> H = harmonic(25/S(7))
    >>> He = simplify(expand_func(H).doit())
    >>> He
    log(sin(2*pi/7)**(2*cos(16*pi/7))/(14*sin(pi/7)**(2*cos(pi/7))*cos(pi/14)**(2*sin(pi/14)))) + pi*tan(pi/14)/2 + 30247/9900
    >>> He.n(40)
    1.983697455232980674869851942390639915940
    >>> harmonic(25/S(7)).n(40)
    1.983697455232980674869851942390639915940

    We can rewrite harmonic numbers in terms of polygamma functions:

    >>> from sympy import digamma, polygamma
    >>> m = Symbol("m", integer=True, positive=True)

    >>> harmonic(n).rewrite(digamma)
    polygamma(0, n + 1) + EulerGamma

    >>> harmonic(n).rewrite(polygamma)
    polygamma(0, n + 1) + EulerGamma

    >>> harmonic(n,3).rewrite(polygamma)
    polygamma(2, n + 1)/2 + zeta(3)

    >>> simplify(harmonic(n,m).rewrite(polygamma))
    Piecewise((polygamma(0, n + 1) + EulerGamma, Eq(m, 1)),
    (-(-1)**m*polygamma(m - 1, n + 1)/factorial(m - 1) + zeta(m), True))

    Integer offsets in the argument can be pulled out:

    >>> from sympy import expand_func

    >>> expand_func(harmonic(n+4))
    harmonic(n) + 1/(n + 4) + 1/(n + 3) + 1/(n + 2) + 1/(n + 1)

    >>> expand_func(harmonic(n-4))
    harmonic(n) - 1/(n - 1) - 1/(n - 2) - 1/(n - 3) - 1/n

    Some limits can be computed as well:

    >>> from sympy import limit, oo

    >>> limit(harmonic(n), n, oo)
    oo

    >>> limit(harmonic(n, 2), n, oo)
    pi**2/6

    >>> limit(harmonic(n, 3), n, oo)
    zeta(3)

    For `m > 1`, `H_{n,m}` tends to `\\zeta(m)` in the limit of infinite `n`:

    >>> m = Symbol("m", positive=True)
    >>> limit(harmonic(n, m+1), n, oo)
    zeta(m + 1)

    See Also
    ========

    bell, bernoulli, catalan, euler, fibonacci, lucas, genocchi, partition, tribonacci

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Harmonic_number
    .. [2] https://functions.wolfram.com/GammaBetaErf/HarmonicNumber/
    .. [3] https://functions.wolfram.com/GammaBetaErf/HarmonicNumber2/

    '''
    eval = (lambda cls, n, m = (None,): pass# WARNING: Decompyle incomplete
)()
    
    def _eval_rewrite_as_polygamma(self, n, m = (S.One,), **kwargs):
        gamma = gamma
        polygamma = polygamma
        import sympy.functions.special.gamma_functions
        if m.is_integer or m.is_positive:
            return Piecewise((polygamma(0, n + 1) + S.EulerGamma, Eq(m, 1)), (S.NegativeOne ** m * (polygamma(m - 1, 1) - polygamma(m - 1, n + 1)) / gamma(m), True))
        return None

    
    def _eval_rewrite_as_digamma(self, n, m = (1,), **kwargs):
        polygamma = polygamma
        import sympy.functions.special.gamma_functions
        return self.rewrite(polygamma)

    
    def _eval_rewrite_as_trigamma(self, n, m = (1,), **kwargs):
        polygamma = polygamma
        import sympy.functions.special.gamma_functions
        return self.rewrite(polygamma)

    
    def _eval_rewrite_as_Sum(self, n, m = (None,), **kwargs):
        Sum = Sum
        import sympy.concrete.summations
        k = Dummy('k', integer = True)
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_zeta(self, n, m = (S.One,), **kwargs):
        zeta = zeta
        import sympy.functions.special.zeta_functions
        digamma = digamma
        import sympy.functions.special.gamma_functions
        return Piecewise((digamma(n + 1) + S.EulerGamma, Eq(m, 1)), (zeta(m) - zeta(m, n + 1), True))

    
    def _eval_expand_func(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_tractable(self, n, m, limitvar = (1, None), **kwargs):
        zeta = zeta
        import sympy.functions.special.zeta_functions
        polygamma = polygamma
        import sympy.functions.special.gamma_functions
        pg = self.rewrite(polygamma)
        if not isinstance(pg, harmonic):
            return pg.rewrite('tractable', deep = True)
        arg = None - S.One
        if arg.is_nonzero:
            return (zeta(m) - zeta(m, n + 1)).rewrite('tractable', deep = True)

    
    def _eval_evalf(self, prec):
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args()):
            return None
        n = all.args[0]._to_mpmath(prec)
        m = self.args[1] if len(self.args) > 1 else S.One._to_mpmath(prec)
        if mp.isint(n) and n < 0:
            return S.NaN
        None(prec)
        if m == 1:
            res = mp.harmonic(n)
        else:
            res = mp.zeta(m) - mp.zeta(m, n + 1)
        None(None, None)

    
    def fdiff(self, argindex = (1,)):
        zeta = zeta
        import sympy.functions.special.zeta_functions
        if len(self.args) == 2:
            (n, m) = self.args
        else:
            (n, m) = self.args + (1,)
        if argindex == 1:
            return m * zeta(m + 1, n + 1)
        raise None



class euler(Function):
    '''
    Euler numbers / Euler polynomials / Euler function

    The Euler numbers are given by:

    .. math:: E_{2n} = I \\sum_{k=1}^{2n+1} \\sum_{j=0}^k \\binom{k}{j}
        \\frac{(-1)^j (k-2j)^{2n+1}}{2^k I^k k}

    .. math:: E_{2n+1} = 0

    Euler numbers and Euler polynomials are related by

    .. math:: E_n = 2^n E_n\\left(\\frac{1}{2}\\right).

    We compute symbolic Euler polynomials using Appell sequences,
    but numerical evaluation of the Euler polynomial is computed
    more efficiently (and more accurately) using the mpmath library.

    The Euler polynomials are special cases of the generalized Euler function,
    related to the Genocchi function as

    .. math:: \\operatorname{E}(s, a) = -\\frac{\\operatorname{G}(s+1, a)}{s+1}

    with the limit of `\\psi\\left(\\frac{a+1}{2}\\right) - \\psi\\left(\\frac{a}{2}\\right)`
    being taken when `s = -1`. The (ordinary) Euler function interpolating
    the Euler numbers is then obtained as
    `\\operatorname{E}(s) = 2^s \\operatorname{E}\\left(s, \\frac{1}{2}\\right)`.

    * ``euler(n)`` gives the nth Euler number `E_n`.
    * ``euler(s)`` gives the Euler function `\\operatorname{E}(s)`.
    * ``euler(n, x)`` gives the nth Euler polynomial `E_n(x)`.
    * ``euler(s, a)`` gives the generalized Euler function `\\operatorname{E}(s, a)`.

    Examples
    ========

    >>> from sympy import euler, Symbol, S
    >>> [euler(n) for n in range(10)]
    [1, 0, -1, 0, 5, 0, -61, 0, 1385, 0]
    >>> [2**n*euler(n,1) for n in range(10)]
    [1, 1, 0, -2, 0, 16, 0, -272, 0, 7936]
    >>> n = Symbol("n")
    >>> euler(n + 2*n)
    euler(3*n)

    >>> x = Symbol("x")
    >>> euler(n, x)
    euler(n, x)

    >>> euler(0, x)
    1
    >>> euler(1, x)
    x - 1/2
    >>> euler(2, x)
    x**2 - x
    >>> euler(3, x)
    x**3 - 3*x**2/2 + 1/4
    >>> euler(4, x)
    x**4 - 2*x**3 + x

    >>> euler(12, S.Half)
    2702765/4096
    >>> euler(12)
    2702765

    See Also
    ========

    andre, bell, bernoulli, catalan, fibonacci, harmonic, lucas, genocchi,
    partition, tribonacci, sympy.polys.appellseqs.euler_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Euler_numbers
    .. [2] https://mathworld.wolfram.com/EulerNumber.html
    .. [3] https://en.wikipedia.org/wiki/Alternating_permutation
    .. [4] https://mathworld.wolfram.com/AlternatingPermutation.html

    '''
    eval = (lambda cls, n, x = (None,): if n.is_zero:
S.One# WARNING: Decompyle incomplete
)()
    
    def _eval_rewrite_as_Sum(self, n, x = (None,), **kwargs):
        Sum = Sum
        import sympy.concrete.summations
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_genocchi(self, n, x = (None,), **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_evalf(self, prec):
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args()):
            return None
        mp = mp
        import mpmath
        (m, x) = (self.args[0], None) if len(self.args) == 1 else self.args
        m = m._to_mpmath(prec)
    # WARNING: Decompyle incomplete



class catalan(Function):
    '''
    Catalan numbers

    The `n^{th}` catalan number is given by:

    .. math :: C_n = \\frac{1}{n+1} \\binom{2n}{n}

    * ``catalan(n)`` gives the `n^{th}` Catalan number, `C_n`

    Examples
    ========

    >>> from sympy import (Symbol, binomial, gamma, hyper,
    ...     catalan, diff, combsimp, Rational, I)

    >>> [catalan(i) for i in range(1,10)]
    [1, 2, 5, 14, 42, 132, 429, 1430, 4862]

    >>> n = Symbol("n", integer=True)

    >>> catalan(n)
    catalan(n)

    Catalan numbers can be transformed into several other, identical
    expressions involving other mathematical functions

    >>> catalan(n).rewrite(binomial)
    binomial(2*n, n)/(n + 1)

    >>> catalan(n).rewrite(gamma)
    4**n*gamma(n + 1/2)/(sqrt(pi)*gamma(n + 2))

    >>> catalan(n).rewrite(hyper)
    hyper((-n, 1 - n), (2,), 1)

    For some non-integer values of n we can get closed form
    expressions by rewriting in terms of gamma functions:

    >>> catalan(Rational(1, 2)).rewrite(gamma)
    8/(3*pi)

    We can differentiate the Catalan numbers C(n) interpreted as a
    continuous real function in n:

    >>> diff(catalan(n), n)
    (polygamma(0, n + 1/2) - polygamma(0, n + 2) + log(4))*catalan(n)

    As a more advanced example consider the following ratio
    between consecutive numbers:

    >>> combsimp((catalan(n + 1)/catalan(n)).rewrite(binomial))
    2*(2*n + 1)/(n + 2)

    The Catalan numbers can be generalized to complex numbers:

    >>> catalan(I).rewrite(gamma)
    4**I*gamma(1/2 + I)/(sqrt(pi)*gamma(2 + I))

    and evaluated with arbitrary precision:

    >>> catalan(I).evalf(20)
    0.39764993382373624267 - 0.020884341620842555705*I

    See Also
    ========

    andre, bell, bernoulli, euler, fibonacci, harmonic, lucas, genocchi,
    partition, tribonacci, sympy.functions.combinatorial.factorials.binomial

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Catalan_number
    .. [2] https://mathworld.wolfram.com/CatalanNumber.html
    .. [3] https://functions.wolfram.com/GammaBetaErf/CatalanNumber/
    .. [4] http://geometer.org/mathcircles/catalan.pdf

    '''
    eval = (lambda cls, n: gamma = gammaimport sympy.functions.special.gamma_functionsif (n.is_Integer or n.is_nonnegative or n.is_noninteger) and n.is_negative:
4 ** n * gamma(n + S.Half) / (gamma(S.Half) * gamma(n + 2))if None.is_integer or n.is_negative:
if (n + 1).is_negative:
S.Zeroif (None + 1).is_zero:
Rational(-1, 2)NoneNone)()
    
    def fdiff(self, argindex = (1,)):
        log = log
        import sympy.functions.elementary.exponential
        polygamma = polygamma
        import sympy.functions.special.gamma_functions
        n = self.args[0]
        return catalan(n) * ((polygamma(0, n + S.Half) - polygamma(0, n + 2)) + log(4))

    
    def _eval_rewrite_as_binomial(self, n, **kwargs):
        return binomial(2 * n, n) / (n + 1)

    
    def _eval_rewrite_as_factorial(self, n, **kwargs):
        return factorial(2 * n) / (factorial(n + 1) * factorial(n))

    
    def _eval_rewrite_as_gamma(self, n, piecewise = (True,), **kwargs):
        gamma = gamma
        import sympy.functions.special.gamma_functions
        return 4 ** n * gamma(n + S.Half) / (gamma(S.Half) * gamma(n + 2))

    
    def _eval_rewrite_as_hyper(self, n, **kwargs):
        hyper = hyper
        import sympy.functions.special.hyper
        return hyper([
            1 - n,
            -n], [
            2], 1)

    
    def _eval_rewrite_as_Product(self, n, **kwargs):
        Product = Product
        import sympy.concrete.products
        if not n.is_integer or n.is_nonnegative:
            return self
        k = None('k', integer = True, positive = True)
        return Product((n + k) / k, (k, 2, n))

    
    def _eval_is_integer(self):
        if self.args[0].is_integer or self.args[0].is_nonnegative:
            return True
        return None

    
    def _eval_is_positive(self):
        if self.args[0].is_nonnegative:
            return True

    
    def _eval_is_composite(self):
        if self.args[0].is_integer or (self.args[0] - 3).is_positive:
            return True
        return None

    
    def _eval_evalf(self, prec):
        gamma = gamma
        import sympy.functions.special.gamma_functions
        if self.args[0].is_number:
            return self.rewrite(gamma)._eval_evalf(prec)



class genocchi(Function):
    '''
    Genocchi numbers / Genocchi polynomials / Genocchi function

    The Genocchi numbers are a sequence of integers `G_n` that satisfy the
    relation:

    .. math:: \\frac{-2t}{1 + e^{-t}} = \\sum_{n=0}^\\infty \\frac{G_n t^n}{n!}

    They are related to the Bernoulli numbers by

    .. math:: G_n = 2 (1 - 2^n) B_n

    and generalize like the Bernoulli numbers to the Genocchi polynomials and
    function as

    .. math:: \\operatorname{G}(s, a) = 2 \\left(\\operatorname{B}(s, a) -
              2^s \\operatorname{B}\\left(s, \\frac{a+1}{2}\\right)\\right)

    .. versionchanged:: 1.12
        ``genocchi(1)`` gives `-1` instead of `1`.

    Examples
    ========

    >>> from sympy import genocchi, Symbol
    >>> [genocchi(n) for n in range(9)]
    [0, -1, -1, 0, 1, 0, -3, 0, 17]
    >>> n = Symbol(\'n\', integer=True, positive=True)
    >>> genocchi(2*n + 1)
    0
    >>> x = Symbol(\'x\')
    >>> genocchi(4, x)
    -4*x**3 + 6*x**2 - 1

    See Also
    ========

    bell, bernoulli, catalan, euler, fibonacci, harmonic, lucas, partition, tribonacci
    sympy.polys.appellseqs.genocchi_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Genocchi_number
    .. [2] https://mathworld.wolfram.com/GenocchiNumber.html
    .. [3] Peter Luschny, "An introduction to the Bernoulli function",
           https://arxiv.org/abs/2009.06743

    '''
    eval = (lambda cls, n, x = (None,): if x is S.One:
cls(n)if None.is_integer is False or n.is_nonnegative is False:
None# WARNING: Decompyle incomplete
)()
    
    def _eval_rewrite_as_bernoulli(self, n, x = (1,), **kwargs):
        if x == 1 and n.is_integer and n.is_nonnegative:
            return 2 * (1 - S(2) ** n) * bernoulli(n)
        return None * (bernoulli(n, x) - 2 ** n * bernoulli(n, (x + 1) / 2))

    
    def _eval_rewrite_as_dirichlet_eta(self, n, x = (1,), **kwargs):
        dirichlet_eta = dirichlet_eta
        import sympy.functions.special.zeta_functions
        return -2 * n * dirichlet_eta(1 - n, x)

    
    def _eval_is_integer(self):
        if len(self.args) > 1 and self.args[1] != 1:
            return None
        n = None.args[0]
        if n.is_integer or n.is_nonnegative:
            return True
        return None

    
    def _eval_is_negative(self):
        if len(self.args) > 1 and self.args[1] != 1:
            return None
        n = None.args[0]
        if n.is_integer or n.is_nonnegative:
            if n.is_odd:
                return fuzzy_not((n - 1).is_positive)
            return (None / 2).is_odd
        return None

    
    def _eval_is_positive(self):
        if len(self.args) > 1 and self.args[1] != 1:
            return None
        n = None.args[0]
        if n.is_integer or n.is_nonnegative:
            if n.is_zero or n.is_odd:
                return False
            return (None / 2).is_even
        return None

    
    def _eval_is_even(self):
        if len(self.args) > 1 and self.args[1] != 1:
            return None
        n = None.args[0]
        if n.is_integer or n.is_nonnegative:
            if n.is_even:
                return n.is_zero
            return (None - 1).is_positive
        return None

    
    def _eval_is_odd(self):
        if len(self.args) > 1 and self.args[1] != 1:
            return None
        n = None.args[0]
        if n.is_integer or n.is_nonnegative:
            if n.is_even:
                return fuzzy_not(n.is_zero)
            return None((n - 1).is_positive)
        return None

    
    def _eval_is_prime(self):
        if len(self.args) > 1 and self.args[1] != 1:
            return None
        n = None.args[0]
        return (n - 8).is_zero

    
    def _eval_evalf(self, prec):
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args()):
            return self.rewrite(bernoulli)._eval_evalf(prec)
        return all



class andre(Function):
    '''
    Andre numbers / Andre function

    The Andre number `\\mathcal{A}_n` is Luschny\'s name for half the number of
    *alternating permutations* on `n` elements, where a permutation is alternating
    if adjacent elements alternately compare "greater" and "smaller" going from
    left to right. For example, `2 < 3 > 1 < 4` is an alternating permutation.

    This sequence is A000111 in the OEIS, which assigns the names *up/down numbers*
    and *Euler zigzag numbers*. It satisfies a recurrence relation similar to that
    for the Catalan numbers, with `\\mathcal{A}_0 = 1` and

    .. math:: 2 \\mathcal{A}_{n+1} = \\sum_{k=0}^n \\binom{n}{k} \\mathcal{A}_k \\mathcal{A}_{n-k}

    The Bernoulli and Euler numbers are signed transformations of the odd- and
    even-indexed elements of this sequence respectively:

    .. math :: \\operatorname{B}_{2k} = \\frac{2k \\mathcal{A}_{2k-1}}{(-4)^k - (-16)^k}

    .. math :: \\operatorname{E}_{2k} = (-1)^k \\mathcal{A}_{2k}

    Like the Bernoulli and Euler numbers, the Andre numbers are interpolated by the
    entire Andre function:

    .. math :: \\mathcal{A}(s) = (-i)^{s+1} \\operatorname{Li}_{-s}(i) +
            i^{s+1} \\operatorname{Li}_{-s}(-i) = \\\\ \\frac{2 \\Gamma(s+1)}{(2\\pi)^{s+1}}
            (\\zeta(s+1, 1/4) - \\zeta(s+1, 3/4) \\cos{\\pi s})

    Examples
    ========

    >>> from sympy import andre, euler, bernoulli
    >>> [andre(n) for n in range(11)]
    [1, 1, 1, 2, 5, 16, 61, 272, 1385, 7936, 50521]
    >>> [(-1)**k * andre(2*k) for k in range(7)]
    [1, -1, 5, -61, 1385, -50521, 2702765]
    >>> [euler(2*k) for k in range(7)]
    [1, -1, 5, -61, 1385, -50521, 2702765]
    >>> [andre(2*k-1) * (2*k) / ((-4)**k - (-16)**k) for k in range(1, 8)]
    [1/6, -1/30, 1/42, -1/30, 5/66, -691/2730, 7/6]
    >>> [bernoulli(2*k) for k in range(1, 8)]
    [1/6, -1/30, 1/42, -1/30, 5/66, -691/2730, 7/6]

    See Also
    ========

    bernoulli, catalan, euler, sympy.polys.appellseqs.andre_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Alternating_permutation
    .. [2] https://mathworld.wolfram.com/EulerZigzagNumber.html
    .. [3] Peter Luschny, "An introduction to the Bernoulli function",
           https://arxiv.org/abs/2009.06743
    '''
    eval = (lambda cls, n: if n is S.NaN:
S.NaNif None is S.Infinity:
S.Infinityif None.is_zero:
S.Oneif None == -1:
-log(2)if None == -2:
-2 * S.Catalanif None.is_Integer:
if n.is_nonnegative and n.is_even:
abs(euler(n))if None.is_odd:
zeta = zetaimport sympy.functions.special.zeta_functionsm = -n - 1I ** m * Rational(1 - 2 ** m, 4 ** m) * zeta(-n)None)()
    
    def _eval_rewrite_as_zeta(self, s, **kwargs):
        cos = cos
        import sympy.functions.elementary.trigonometric
        gamma = gamma
        import sympy.functions.special.gamma_functions
        zeta = zeta
        import sympy.functions.special.zeta_functions
        return (2 * gamma(s + 1) / (2 * pi) ** (s + 1)) * (zeta(s + 1, S.One / 4) - cos(pi * s) * zeta(s + 1, S(3) / 4))

    
    def _eval_rewrite_as_polylog(self, s, **kwargs):
        polylog = polylog
        import sympy.functions.special.zeta_functions
        return (-I) ** (s + 1) * polylog(-s, I) + I ** (s + 1) * polylog(-s, -I)

    
    def _eval_is_integer(self):
        n = self.args[0]
        if n.is_integer or n.is_nonnegative:
            return True
        return None

    
    def _eval_is_positive(self):
        if self.args[0].is_nonnegative:
            return True

    
    def _eval_evalf(self, prec):
        if not self.args[0].is_number:
            return None
        s = None.args[0]._to_mpmath(prec + 12)
        workprec(prec + 12)
        cp = mp.cospi(s / 2)
        sp = mp.sinpi(s / 2)
        res = 2 * mp.dirichlet(-s, (-sp, cp, sp, -cp))
        None(None, None)



class partition(Function):
    """
    Partition numbers

    The Partition numbers are a sequence of integers `p_n` that represent the
    number of distinct ways of representing `n` as a sum of natural numbers
    (with order irrelevant). The generating function for `p_n` is given by:

    .. math:: \\sum_{n=0}^\\infty p_n x^n = \\prod_{k=1}^\\infty (1 - x^k)^{-1}

    Examples
    ========

    >>> from sympy import partition, Symbol
    >>> [partition(n) for n in range(9)]
    [1, 1, 2, 3, 5, 7, 11, 15, 22]
    >>> n = Symbol('n', integer=True, negative=True)
    >>> partition(n)
    0

    See Also
    ========

    bell, bernoulli, catalan, euler, fibonacci, harmonic, lucas, genocchi, tribonacci

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Partition_(number_theory%29
    .. [2] https://en.wikipedia.org/wiki/Pentagonal_number_theorem

    """
    is_integer = True
    is_nonnegative = True
    eval = (lambda cls, n: if n.is_integer is False:
raise TypeError('n should be an integer')if n.is_negative is True:
S.Zeroif None.is_zero is True or n is S.One:
S.Oneif None.is_Integer is True:
S(_partition(as_int(n))))()
    
    def _eval_is_positive(self):
        if self.args[0].is_nonnegative is True:
            return True



class divisor_sigma(Function):
    """
    Calculate the divisor function `\\sigma_k(n)` for positive integer n

    ``divisor_sigma(n, k)`` is equal to ``sum([x**k for x in divisors(n)])``

    If n's prime factorization is:

    .. math ::
        n = \\prod_{i=1}^\\omega p_i^{m_i},

    then

    .. math ::
        \\sigma_k(n) = \\prod_{i=1}^\\omega (1+p_i^k+p_i^{2k}+\\cdots
        + p_i^{m_ik}).

    Examples
    ========

    >>> from sympy.functions.combinatorial.numbers import divisor_sigma
    >>> divisor_sigma(18, 0)
    6
    >>> divisor_sigma(39, 1)
    56
    >>> divisor_sigma(12, 2)
    210
    >>> divisor_sigma(37)
    38

    See Also
    ========

    sympy.ntheory.factor_.divisor_count, totient, sympy.ntheory.factor_.divisors, sympy.ntheory.factor_.factorint

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Divisor_function

    """
    is_integer = True
    is_positive = True
    eval = (lambda cls, n, k = (S.One,): pass# WARNING: Decompyle incomplete
)()


class udivisor_sigma(Function):
    """
    Calculate the unitary divisor function `\\sigma_k^*(n)` for positive integer n

    ``udivisor_sigma(n, k)`` is equal to ``sum([x**k for x in udivisors(n)])``

    If n's prime factorization is:

    .. math ::
        n = \\prod_{i=1}^\\omega p_i^{m_i},

    then

    .. math ::
        \\sigma_k^*(n) = \\prod_{i=1}^\\omega (1+ p_i^{m_ik}).

    Parameters
    ==========

    k : power of divisors in the sum

        for k = 0, 1:
        ``udivisor_sigma(n, 0)`` is equal to ``udivisor_count(n)``
        ``udivisor_sigma(n, 1)`` is equal to ``sum(udivisors(n))``

        Default for k is 1.

    Examples
    ========

    >>> from sympy.functions.combinatorial.numbers import udivisor_sigma
    >>> udivisor_sigma(18, 0)
    4
    >>> udivisor_sigma(74, 1)
    114
    >>> udivisor_sigma(36, 3)
    47450
    >>> udivisor_sigma(111)
    152

    See Also
    ========

    sympy.ntheory.factor_.divisor_count, totient, sympy.ntheory.factor_.divisors,
    sympy.ntheory.factor_.udivisors, sympy.ntheory.factor_.udivisor_count, divisor_sigma,
    sympy.ntheory.factor_.factorint

    References
    ==========

    .. [1] https://mathworld.wolfram.com/UnitaryDivisorFunction.html

    """
    is_integer = True
    is_positive = True
    eval = (lambda cls, n, k = (S.One,): pass# WARNING: Decompyle incomplete
)()


class legendre_symbol(Function):
    '''
    Returns the Legendre symbol `(a / p)`.

    For an integer ``a`` and an odd prime ``p``, the Legendre symbol is
    defined as

    .. math ::
        \\genfrac(){}{}{a}{p} = \\begin{cases}
             0 & \\text{if } p \\text{ divides } a\\\\
             1 & \\text{if } a \\text{ is a quadratic residue modulo } p\\\\
            -1 & \\text{if } a \\text{ is a quadratic nonresidue modulo } p
        \\end{cases}

    Examples
    ========

    >>> from sympy.functions.combinatorial.numbers import legendre_symbol
    >>> [legendre_symbol(i, 7) for i in range(7)]
    [0, 1, 1, -1, 1, -1, -1]
    >>> sorted(set([i**2 % 7 for i in range(7)]))
    [0, 1, 2, 4]

    See Also
    ========

    sympy.ntheory.residue_ntheory.is_quad_residue, jacobi_symbol

    '''
    is_integer = True
    is_prime = False
    eval = (lambda cls, a, p: if a.is_integer is False:
raise TypeError('a should be an integer')if p.is_integer is False:
raise TypeError('p should be an integer')if p.is_prime is False or p.is_odd is False:
raise ValueError('p should be an odd prime integer')if (a % p).is_zero is True:
S.Zeroif None is S.One:
S.Oneif None.is_Integer is True or p.is_Integer is True:
S(legendre(as_int(a), as_int(p)))None)()


class jacobi_symbol(Function):
    '''
    Returns the Jacobi symbol `(m / n)`.

    For any integer ``m`` and any positive odd integer ``n`` the Jacobi symbol
    is defined as the product of the Legendre symbols corresponding to the
    prime factors of ``n``:

    .. math ::
        \\genfrac(){}{}{m}{n} =
            \\genfrac(){}{}{m}{p^{1}}^{\\alpha_1}
            \\genfrac(){}{}{m}{p^{2}}^{\\alpha_2}
            ...
            \\genfrac(){}{}{m}{p^{k}}^{\\alpha_k}
            \\text{ where } n =
                p_1^{\\alpha_1}
                p_2^{\\alpha_2}
                ...
                p_k^{\\alpha_k}

    Like the Legendre symbol, if the Jacobi symbol `\\genfrac(){}{}{m}{n} = -1`
    then ``m`` is a quadratic nonresidue modulo ``n``.

    But, unlike the Legendre symbol, if the Jacobi symbol
    `\\genfrac(){}{}{m}{n} = 1` then ``m`` may or may not be a quadratic residue
    modulo ``n``.

    Examples
    ========

    >>> from sympy.functions.combinatorial.numbers import jacobi_symbol, legendre_symbol
    >>> from sympy import S
    >>> jacobi_symbol(45, 77)
    -1
    >>> jacobi_symbol(60, 121)
    1

    The relationship between the ``jacobi_symbol`` and ``legendre_symbol`` can
    be demonstrated as follows:

    >>> L = legendre_symbol
    >>> S(45).factors()
    {3: 2, 5: 1}
    >>> jacobi_symbol(7, 45) == L(7, 3)**2 * L(7, 5)**1
    True

    See Also
    ========

    sympy.ntheory.residue_ntheory.is_quad_residue, legendre_symbol

    '''
    is_integer = True
    is_prime = False
    eval = (lambda cls, m, n: if m.is_integer is False:
raise TypeError('m should be an integer')if n.is_integer is False:
raise TypeError('n should be an integer')if n.is_positive is False or n.is_odd is False:
raise ValueError('n should be an odd positive integer')if m is S.One or n is S.One:
S.Oneif (None % n).is_zero is True:
S.Zeroif None.is_Integer is True or n.is_Integer is True:
S(jacobi(as_int(m), as_int(n)))None)()


class kronecker_symbol(Function):
    '''
    Returns the Kronecker symbol `(a / n)`.

    Examples
    ========

    >>> from sympy.functions.combinatorial.numbers import kronecker_symbol
    >>> kronecker_symbol(45, 77)
    -1
    >>> kronecker_symbol(13, -120)
    1

    See Also
    ========

    jacobi_symbol, legendre_symbol

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Kronecker_symbol

    '''
    is_integer = True
    is_prime = False
    eval = (lambda cls, a, n: if a.is_integer is False:
raise TypeError('a should be an integer')if n.is_integer is False:
raise TypeError('n should be an integer')if a is S.One or n is S.One:
S.Oneif None.is_Integer is True or n.is_Integer is True:
S(kronecker(as_int(a), as_int(n)))None)()


class mobius(Function):
    '''
    Mobius function maps natural number to {-1, 0, 1}

    It is defined as follows:
        1) `1` if `n = 1`.
        2) `0` if `n` has a squared prime factor.
        3) `(-1)^k` if `n` is a square-free positive integer with `k`
           number of prime factors.

    It is an important multiplicative function in number theory
    and combinatorics.  It has applications in mathematical series,
    algebraic number theory and also physics (Fermion operator has very
    concrete realization with Mobius Function model).

    Examples
    ========

    >>> from sympy.functions.combinatorial.numbers import mobius
    >>> mobius(13*7)
    1
    >>> mobius(1)
    1
    >>> mobius(13*7*5)
    -1
    >>> mobius(13**2)
    0

    Even in the case of a symbol, if it clearly contains a squared prime factor, it will be zero.

    >>> from sympy import Symbol
    >>> n = Symbol("n", integer=True, positive=True)
    >>> mobius(4*n)
    0
    >>> mobius(n**2)
    0

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/M%C3%B6bius_function
    .. [2] Thomas Koshy "Elementary Number Theory with Applications"
    .. [3] https://oeis.org/A008683

    '''
    is_integer = True
    is_prime = False
    eval = (lambda cls, n: if n.is_integer is False:
raise TypeError('n should be an integer')if n.is_positive is False:
raise ValueError('n should be a positive integer')if n.is_prime is True:
S.NegativeOneif None is S.One:
S.Oneresult = None# WARNING: Decompyle incomplete
)()


class primenu(Function):
    """
    Calculate the number of distinct prime factors for a positive integer n.

    If n's prime factorization is:

    .. math ::
        n = \\prod_{i=1}^k p_i^{m_i},

    then ``primenu(n)`` or `\\nu(n)` is:

    .. math ::
        \\nu(n) = k.

    Examples
    ========

    >>> from sympy.functions.combinatorial.numbers import primenu
    >>> primenu(1)
    0
    >>> primenu(30)
    3

    See Also
    ========

    sympy.ntheory.factor_.factorint

    References
    ==========

    .. [1] https://mathworld.wolfram.com/PrimeFactor.html
    .. [2] https://oeis.org/A001221

    """
    is_integer = True
    is_nonnegative = True
    eval = (lambda cls, n: if n.is_integer is False:
raise TypeError('n should be an integer')if n.is_positive is False:
raise ValueError('n should be a positive integer')if n.is_prime is True:
S.Oneif None is S.One:
S.Zeroif None.is_Integer is True:
S(len(factorint(n))))()


class primeomega(Function):
    """
    Calculate the number of prime factors counting multiplicities for a
    positive integer n.

    If n's prime factorization is:

    .. math ::
        n = \\prod_{i=1}^k p_i^{m_i},

    then ``primeomega(n)``  or `\\Omega(n)` is:

    .. math ::
        \\Omega(n) = \\sum_{i=1}^k m_i.

    Examples
    ========

    >>> from sympy.functions.combinatorial.numbers import primeomega
    >>> primeomega(1)
    0
    >>> primeomega(20)
    3

    See Also
    ========

    sympy.ntheory.factor_.factorint

    References
    ==========

    .. [1] https://mathworld.wolfram.com/PrimeFactor.html
    .. [2] https://oeis.org/A001222

    """
    is_integer = True
    is_nonnegative = True
    eval = (lambda cls, n: if n.is_integer is False:
raise TypeError('n should be an integer')if n.is_positive is False:
raise ValueError('n should be a positive integer')if n.is_prime is True:
S.Oneif None is S.One:
S.Zeroif None.is_Integer is True:
S(sum(factorint(n).values())))()


class totient(Function):
    '''
    Calculate the Euler totient function phi(n)

    ``totient(n)`` or `\\phi(n)` is the number of positive integers `\\leq` n
    that are relatively prime to n.

    Examples
    ========

    >>> from sympy.functions.combinatorial.numbers import totient
    >>> totient(1)
    1
    >>> totient(25)
    20
    >>> totient(45) == totient(5)*totient(9)
    True

    See Also
    ========

    sympy.ntheory.factor_.divisor_count

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Euler%27s_totient_function
    .. [2] https://mathworld.wolfram.com/TotientFunction.html
    .. [3] https://oeis.org/A000010

    '''
    is_integer = True
    is_positive = True
    eval = (lambda cls, n: if n.is_integer is False:
raise TypeError('n should be an integer')if n.is_positive is False:
raise ValueError('n should be a positive integer')if n is S.One:
S.Oneif None.is_prime is True:
n - 1if None(n, Dict):
prod((lambda .0: pass# WARNING: Decompyle incomplete
)(n.items()()))
        if None.is_Integer is True:
            return prod((lambda .0: pass# WARNING: Decompyle incomplete
)(factorint(n).items()()))
)()


class reduced_totient(Function):
    '''
    Calculate the Carmichael reduced totient function lambda(n)

    ``reduced_totient(n)`` or `\\lambda(n)` is the smallest m > 0 such that
    `k^m \\equiv 1 \\mod n` for all k relatively prime to n.

    Examples
    ========

    >>> from sympy.functions.combinatorial.numbers import reduced_totient
    >>> reduced_totient(1)
    1
    >>> reduced_totient(8)
    2
    >>> reduced_totient(30)
    4

    See Also
    ========

    totient

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Carmichael_function
    .. [2] https://mathworld.wolfram.com/CarmichaelFunction.html
    .. [3] https://oeis.org/A002322

    '''
    is_integer = True
    is_positive = True
    eval = (lambda cls, n:
