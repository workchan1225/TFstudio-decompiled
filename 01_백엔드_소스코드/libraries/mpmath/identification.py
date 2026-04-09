# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: identification.pyc (Python 3.11)

'''
Implements the PSLQ algorithm for integer relation detection,
and derivative algorithms for constant recognition.
'''
from libmp.backend import xrange
from libmp import int_types, sqrt_fixed

def round_fixed(x, prec):
    return (x + (1 << prec - 1) >> prec) << prec


class IdentificationMethods(object):
    pass


def pslq(ctx, x, tol, maxcoeff, maxsteps, verbose = (None, 1000, 100, False)):
    '''
    Given a vector of real numbers `x = [x_0, x_1, ..., x_n]`, ``pslq(x)``
    uses the PSLQ algorithm to find a list of integers
    `[c_0, c_1, ..., c_n]` such that

    .. math ::

        |c_1 x_1 + c_2 x_2 + ... + c_n x_n| < \\mathrm{tol}

    and such that `\\max |c_k| < \\mathrm{maxcoeff}`. If no such vector
    exists, :func:`~mpmath.pslq` returns ``None``. The tolerance defaults to
    3/4 of the working precision.

    **Examples**

    Find rational approximations for `\\pi`::

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> pslq([-1, pi], tol=0.01)
        [22, 7]
        >>> pslq([-1, pi], tol=0.001)
        [355, 113]
        >>> mpf(22)/7; mpf(355)/113; +pi
        3.14285714285714
        3.14159292035398
        3.14159265358979

    Pi is not a rational number with denominator less than 1000::

        >>> pslq([-1, pi])
        >>>

    To within the standard precision, it can however be approximated
    by at least one rational number with denominator less than `10^{12}`::

        >>> p, q = pslq([-1, pi], maxcoeff=10**12)
        >>> print(p); print(q)
        238410049439
        75888275702
        >>> mpf(p)/q
        3.14159265358979

    The PSLQ algorithm can be applied to long vectors. For example,
    we can investigate the rational (in)dependence of integer square
    roots::

        >>> mp.dps = 30
        >>> pslq([sqrt(n) for n in range(2, 5+1)])
        >>>
        >>> pslq([sqrt(n) for n in range(2, 6+1)])
        >>>
        >>> pslq([sqrt(n) for n in range(2, 8+1)])
        [2, 0, 0, 0, 0, 0, -1]

    **Machin formulas**

    A famous formula for `\\pi` is Machin\'s,

    .. math ::

        \\frac{\\pi}{4} = 4 \\operatorname{acot} 5 - \\operatorname{acot} 239

    There are actually infinitely many formulas of this type. Two
    others are

    .. math ::

        \\frac{\\pi}{4} = \\operatorname{acot} 1

        \\frac{\\pi}{4} = 12 \\operatorname{acot} 49 + 32 \\operatorname{acot} 57
            + 5 \\operatorname{acot} 239 + 12 \\operatorname{acot} 110443

    We can easily verify the formulas using the PSLQ algorithm::

        >>> mp.dps = 30
        >>> pslq([pi/4, acot(1)])
        [1, -1]
        >>> pslq([pi/4, acot(5), acot(239)])
        [1, -4, 1]
        >>> pslq([pi/4, acot(49), acot(57), acot(239), acot(110443)])
        [1, -12, -32, 5, -12]

    We could try to generate a custom Machin-like formula by running
    the PSLQ algorithm with a few inverse cotangent values, for example
    acot(2), acot(3) ... acot(10). Unfortunately, there is a linear
    dependence among these values, resulting in only that dependence
    being detected, with a zero coefficient for `\\pi`::

        >>> pslq([pi] + [acot(n) for n in range(2,11)])
        [0, 1, -1, 0, 0, 0, -1, 0, 0, 0]

    We get better luck by removing linearly dependent terms::

        >>> pslq([pi] + [acot(n) for n in range(2,11) if n not in (3, 5)])
        [1, -8, 0, 0, 4, 0, 0, 0]

    In other words, we found the following formula::

        >>> 8*acot(2) - 4*acot(7)
        3.14159265358979323846264338328
        >>> +pi
        3.14159265358979323846264338328

    **Algorithm**

    This is a fairly direct translation to Python of the pseudocode given by
    David Bailey, "The PSLQ Integer Relation Algorithm":
    http://www.cecm.sfu.ca/organics/papers/bailey/paper/html/node3.html

    The present implementation uses fixed-point instead of floating-point
    arithmetic, since this is significantly (about 7x) faster.
    '''
    pass
# WARNING: Decompyle incomplete


def findpoly(ctx, x, n = (1,), **kwargs):
    """
    ``findpoly(x, n)`` returns the coefficients of an integer
    polynomial `P` of degree at most `n` such that `P(x) \\approx 0`.
    If no polynomial having `x` as a root can be found,
    :func:`~mpmath.findpoly` returns ``None``.

    :func:`~mpmath.findpoly` works by successively calling :func:`~mpmath.pslq` with
    the vectors `[1, x]`, `[1, x, x^2]`, `[1, x, x^2, x^3]`, ...,
    `[1, x, x^2, .., x^n]` as input. Keyword arguments given to
    :func:`~mpmath.findpoly` are forwarded verbatim to :func:`~mpmath.pslq`. In
    particular, you can specify a tolerance for `P(x)` with ``tol``
    and a maximum permitted coefficient size with ``maxcoeff``.

    For large values of `n`, it is recommended to run :func:`~mpmath.findpoly`
    at high precision; preferably 50 digits or more.

    **Examples**

    By default (degree `n = 1`), :func:`~mpmath.findpoly` simply finds a linear
    polynomial with a rational root::

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> findpoly(0.7)
        [-10, 7]

    The generated coefficient list is valid input to ``polyval`` and
    ``polyroots``::

        >>> nprint(polyval(findpoly(phi, 2), phi), 1)
        -2.0e-16
        >>> for r in polyroots(findpoly(phi, 2)):
        ...     print(r)
        ...
        -0.618033988749895
        1.61803398874989

    Numbers of the form `m + n \\sqrt p` for integers `(m, n, p)` are
    solutions to quadratic equations. As we find here, `1+\\sqrt 2`
    is a root of the polynomial `x^2 - 2x - 1`::

        >>> findpoly(1+sqrt(2), 2)
        [1, -2, -1]
        >>> findroot(lambda x: x**2 - 2*x - 1, 1)
        2.4142135623731

    Despite only containing square roots, the following number results
    in a polynomial of degree 4::

        >>> findpoly(sqrt(2)+sqrt(3), 4)
        [1, 0, -10, 0, 1]

    In fact, `x^4 - 10x^2 + 1` is the *minimal polynomial* of
    `r = \\sqrt 2 + \\sqrt 3`, meaning that a rational polynomial of
    lower degree having `r` as a root does not exist. Given sufficient
    precision, :func:`~mpmath.findpoly` will usually find the correct
    minimal polynomial of a given algebraic number.

    **Non-algebraic numbers**

    If :func:`~mpmath.findpoly` fails to find a polynomial with given
    coefficient size and tolerance constraints, that means no such
    polynomial exists.

    We can verify that `\\pi` is not an algebraic number of degree 3 with
    coefficients less than 1000::

        >>> mp.dps = 15
        >>> findpoly(pi, 3)
        >>>

    It is always possible to find an algebraic approximation of a number
    using one (or several) of the following methods:

        1. Increasing the permitted degree
        2. Allowing larger coefficients
        3. Reducing the tolerance

    One example of each method is shown below::

        >>> mp.dps = 15
        >>> findpoly(pi, 4)
        [95, -545, 863, -183, -298]
        >>> findpoly(pi, 3, maxcoeff=10000)
        [836, -1734, -2658, -457]
        >>> findpoly(pi, 3, tol=1e-7)
        [-4, 22, -29, -2]

    It is unknown whether Euler's constant is transcendental (or even
    irrational). We can use :func:`~mpmath.findpoly` to check that if is
    an algebraic number, its minimal polynomial must have degree
    at least 7 and a coefficient of magnitude at least 1000000::

        >>> mp.dps = 200
        >>> findpoly(euler, 6, maxcoeff=10**6, tol=1e-100, maxsteps=1000)
        >>>

    Note that the high precision and strict tolerance is necessary
    for such high-degree runs, since otherwise unwanted low-accuracy
    approximations will be detected. It may also be necessary to set
    maxsteps high to prevent a premature exit (before the coefficient
    bound has been reached). Running with ``verbose=True`` to get an
    idea what is happening can be useful.
    """
    x = ctx.mpf(x)
    if n < 1:
        raise ValueError('n cannot be less than 1')
    if x == 0:
        return [
            1,
            0]
    xs = [
        None.mpf(1)]
# WARNING: Decompyle incomplete


def fracgcd(p, q):
    y = q
    x = p
# WARNING: Decompyle incomplete


def pslqstring(r, constants):
