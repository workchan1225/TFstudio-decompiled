# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: intfunc.pyc (Python 3.11)

"""
The routines here were removed from numbers.py, power.py,
digits.py and factor_.py so they could be imported into core
without raising circular import errors.

Although the name 'intfunc' was chosen to represent functions that
work with integers, it can also be thought of as containing
internal/core functions that are needed by the classes of the core.
"""
import math
import sys
from functools import lru_cache
from sympify import sympify
from singleton import S
from sympy.external.gmpy import gcd as number_gcd, lcm as number_lcm, sqrt, iroot, bit_scan1, gcdext
from sympy.utilities.misc import as_int, filldedent

def num_digits(n, base = (10,)):
    '''Return the number of digits needed to express n in give base.

    Examples
    ========

    >>> from sympy.core.intfunc import num_digits
    >>> num_digits(10)
    2
    >>> num_digits(10, 2)  # 1010 -> 4 digits
    4
    >>> num_digits(-100, 16)  # -64 -> 2 digits
    2


    Parameters
    ==========

    n: integer
        The number whose digits are counted.

    b: integer
        The base in which digits are computed.

    See Also
    ========
    sympy.ntheory.digits.digits, sympy.ntheory.digits.count_digits
    '''
    if base < 0:
        raise ValueError('base must be int greater than 1')
    if not n:
        return 1
    (e, t) = None(abs(n), base)
    return 1 + e


def integer_log(n, b):
    '''
    Returns ``(e, bool)`` where e is the largest nonnegative integer
    such that :math:`|n| \\geq |b^e|` and ``bool`` is True if $n = b^e$.

    Examples
    ========

    >>> from sympy import integer_log
    >>> integer_log(125, 5)
    (3, True)
    >>> integer_log(17, 9)
    (1, False)

    If the base is positive and the number negative the
    return value will always be the same except for 2:

    >>> integer_log(-4, 2)
    (2, False)
    >>> integer_log(-16, 4)
    (0, False)

    When the base is negative, the returned value
    will only be True if the parity of the exponent is
    correct for the sign of the base:

    >>> integer_log(4, -2)
    (2, True)
    >>> integer_log(8, -2)
    (3, False)
    >>> integer_log(-8, -2)
    (3, True)
    >>> integer_log(-4, -2)
    (2, False)

    See Also
    ========
    integer_nthroot
    sympy.ntheory.primetest.is_square
    sympy.ntheory.factor_.multiplicity
    sympy.ntheory.factor_.perfect_power
    '''
    n = as_int(n)
    b = as_int(b)
# WARNING: Decompyle incomplete


def trailing(n):
    '''Count the number of trailing zero digits in the binary
    representation of n, i.e. determine the largest power of 2
    that divides n.

    Examples
    ========

    >>> from sympy import trailing
    >>> trailing(128)
    7
    >>> trailing(63)
    0

    See Also
    ========
    sympy.ntheory.factor_.multiplicity

    '''
    if not n:
        return 0
    return None(int(n))

igcd = (lambda : if len(args) < 2:
raise TypeError('igcd() takes at least 2 arguments (%s given)' % len(args))# WARNING: Decompyle incomplete
)()
igcd2 = math.gcd

def igcd_lehmer(a, b):
    """Computes greatest common divisor of two integers.

    Explanation
    ===========

    Euclid's algorithm for the computation of the greatest
    common divisor ``gcd(a, b)``  of two (positive) integers
    $a$ and $b$ is based on the division identity
    $$ a = q \\times b + r$$,
    where the quotient  $q$  and the remainder  $r$  are integers
    and  $0 \\le r < b$. Then each common divisor of  $a$  and  $b$
    divides  $r$, and it follows that  ``gcd(a, b) == gcd(b, r)``.
    The algorithm works by constructing the sequence
    r0, r1, r2, ..., where  r0 = a, r1 = b,  and each  rn
    is the remainder from the division of the two preceding
    elements.

    In Python, ``q = a // b``  and  ``r = a % b``  are obtained by the
    floor division and the remainder operations, respectively.
    These are the most expensive arithmetic operations, especially
    for large  a  and  b.

    Lehmer's algorithm [1]_ is based on the observation that the quotients
    ``qn = r(n-1) // rn``  are in general small integers even
    when  a  and  b  are very large. Hence the quotients can be
    usually determined from a relatively small number of most
    significant bits.

    The efficiency of the algorithm is further enhanced by not
    computing each long remainder in Euclid's sequence. The remainders
    are linear combinations of  a  and  b  with integer coefficients
    derived from the quotients. The coefficients can be computed
    as far as the quotients can be determined from the chosen
    most significant parts of  a  and  b. Only then a new pair of
    consecutive remainders is computed and the algorithm starts
    anew with this pair.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Lehmer%27s_GCD_algorithm

    """
    b = abs(as_int(b))
    a = abs(as_int(a))
    if a < b:
        b = a
        a = b
    nbits = 2 * sys.int_info.bits_per_digit
# WARNING: Decompyle incomplete


def ilcm(*args):
    '''Computes integer least common multiple.

    Examples
    ========

    >>> from sympy import ilcm
    >>> ilcm(5, 10)
    10
    >>> ilcm(7, 3)
    21
    >>> ilcm(5, 10, 15)
    30

    '''
    if len(args) < 2:
        raise TypeError('ilcm() takes at least 2 arguments (%s given)' % len(args))
# WARNING: Decompyle incomplete


def igcdex(a, b):
    '''Returns x, y, g such that g = x*a + y*b = gcd(a, b).

    Examples
    ========

    >>> from sympy.core.intfunc import igcdex
    >>> igcdex(2, 3)
    (-1, 1, 1)
    >>> igcdex(10, 12)
    (-1, 1, 2)

    >>> x, y, g = igcdex(100, 2004)
    >>> x, y, g
    (-20, 1, 4)
    >>> x*100 + y*2004
    4

    '''
    if not a and b:
        return (0, 1, 0)
    (g, x, y) = None(int(a), int(b))
    return (x, y, g)


def mod_inverse(a, m):
    '''
    Return the number $c$ such that, $a \\times c = 1 \\pmod{m}$
    where $c$ has the same sign as $m$. If no such value exists,
    a ValueError is raised.

    Examples
    ========

    >>> from sympy import mod_inverse, S

    Suppose we wish to find multiplicative inverse $x$ of
    3 modulo 11. This is the same as finding $x$ such
    that $3x = 1 \\pmod{11}$. One value of x that satisfies
    this congruence is 4. Because $3 \\times 4 = 12$ and $12 = 1 \\pmod{11}$.
    This is the value returned by ``mod_inverse``:

    >>> mod_inverse(3, 11)
    4
    >>> mod_inverse(-3, 11)
    7

    When there is a common factor between the numerators of
    `a` and `m` the inverse does not exist:

    >>> mod_inverse(2, 4)
    Traceback (most recent call last):
    ...
    ValueError: inverse of 2 mod 4 does not exist

    >>> mod_inverse(S(2)/7, S(5)/2)
    7/2

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
    .. [2] https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    '''
    c = None
# WARNING: Decompyle incomplete


def isqrt(n):
    ''' Return the largest integer less than or equal to `\\sqrt{n}`.

    Parameters
    ==========

    n : non-negative integer

    Returns
    =======

    int : `\\left\\lfloor\\sqrt{n}\\right\\rfloor`

    Raises
    ======

    ValueError
        If n is negative.
    TypeError
        If n is of a type that cannot be compared to ``int``.
        Therefore, a TypeError is raised for ``str``, but not for ``float``.

    Examples
    ========

    >>> from sympy.core.intfunc import isqrt
    >>> isqrt(0)
    0
    >>> isqrt(9)
    3
    >>> isqrt(10)
    3
    >>> isqrt("30")
    Traceback (most recent call last):
        ...
    TypeError: \'<\' not supported between instances of \'str\' and \'int\'
    >>> from sympy.core.numbers import Rational
    >>> isqrt(Rational(-1, 2))
    Traceback (most recent call last):
        ...
    ValueError: n must be nonnegative

    '''
    if n < 0:
        raise ValueError('n must be nonnegative')
    return int(sqrt(int(n)))


def integer_nthroot(y, n):
    '''
    Return a tuple containing x = floor(y**(1/n))
    and a boolean indicating whether the result is exact (that is,
    whether x**n == y).

    Examples
    ========

    >>> from sympy import integer_nthroot
    >>> integer_nthroot(16, 2)
    (4, True)
    >>> integer_nthroot(26, 2)
    (5, False)

    To simply determine if a number is a perfect square, the is_square
    function should be used:

    >>> from sympy.ntheory.primetest import is_square
    >>> is_square(26)
    False

    See Also
    ========
    sympy.ntheory.primetest.is_square
    integer_log
    '''
    (x, b) = iroot(as_int(y), as_int(n))
    return (int(x), b)
