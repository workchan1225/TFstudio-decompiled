# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _trigonometric_special.pyc (Python 3.11)

'''A module for special angle formulas for trigonometric functions

TODO
====

This module should be developed in the future to contain direct square root
representation of

.. math
    F(\\frac{n}{m} \\pi)

for every

- $m \\in \\{ 3, 5, 17, 257, 65537 \\}$
- $n \\in \\mathbb{N}$, $0 \\le n < m$
- $F \\in \\{\\sin, \\cos, \\tan, \\csc, \\sec, \\cot\\}$

Without multi-step rewrites
(e.g. $\\tan \\to \\cos/\\sin \\to \\cos/\\sqrt \\to \\ sqrt$)
or using chebyshev identities
(e.g. $\\cos \\to \\cos + \\cos^2 + \\cdots \\to \\sqrt{} + \\sqrt{}^2 + \\cdots $),
which are trivial to implement in sympy,
and had used to give overly complicated expressions.

The reference can be found below, if anyone may need help implementing them.

References
==========

.. [*] Gottlieb, Christian. (1999). The Simple and straightforward construction
   of the regular 257-gon. The Mathematical Intelligencer. 21. 31-37.
   10.1007/BF03024829.
.. [*] https://resources.wolframcloud.com/FunctionRepository/resources/Cos2PiOverFermatPrime
'''
from __future__ import annotations
from typing import Callable
from functools import reduce
from sympy.core.expr import Expr
from sympy.core.singleton import S
from sympy.core.intfunc import igcdex
from sympy.core.numbers import Integer
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.core.cache import cacheit

def migcdex(*x):
    '''Compute extended gcd for multiple integers.

    Explanation
    ===========

    Given the integers $x_1, \\cdots, x_n$ and
    an extended gcd for multiple arguments are defined as a solution
    $(y_1, \\cdots, y_n), g$ for the diophantine equation
    $x_1 y_1 + \\cdots + x_n y_n = g$ such that
    $g = \\gcd(x_1, \\cdots, x_n)$.

    Examples
    ========

    >>> from sympy.functions.elementary._trigonometric_special import migcdex
    >>> migcdex()
    ((), 0)
    >>> migcdex(4)
    ((1,), 4)
    >>> migcdex(4, 6)
    ((-1, 1), 2)
    >>> migcdex(6, 10, 15)
    ((1, 1, -1), 1)
    '''
    pass
# WARNING: Decompyle incomplete


def ipartfrac(*denoms):
    '''Compute the partial fraction decomposition.

    Explanation
    ===========

    Given a rational number $\\frac{1}{q_1 \\cdots q_n}$ where all
    $q_1, \\cdots, q_n$ are pairwise coprime,

    A partial fraction decomposition is defined as

    .. math::
        \\frac{1}{q_1 \\cdots q_n} = \\frac{p_1}{q_1} + \\cdots + \\frac{p_n}{q_n}

    And it can be derived from solving the following diophantine equation for
    the $p_1, \\cdots, p_n$

    .. math::
        1 = p_1 \\prod_{i \\ne 1}q_i + \\cdots + p_n \\prod_{i \\ne n}q_i

    Where $q_1, \\cdots, q_n$ being pairwise coprime implies
    $\\gcd(\\prod_{i \\ne 1}q_i, \\cdots, \\prod_{i \\ne n}q_i) = 1$,
    which guarantees the existence of the solution.

    It is sufficient to compute partial fraction decomposition only
    for numerator $1$ because partial fraction decomposition for any
    $\\frac{n}{q_1 \\cdots q_n}$ can be easily computed by multiplying
    the result by $n$ afterwards.

    Parameters
    ==========

    denoms : int
        The pairwise coprime integer denominators $q_i$ which defines the
        rational number $\\frac{1}{q_1 \\cdots q_n}$

    Returns
    =======

    tuple[int, ...]
        The list of numerators which semantically corresponds to $p_i$ of the
        partial fraction decomposition
        $\\frac{1}{q_1 \\cdots q_n} = \\frac{p_1}{q_1} + \\cdots + \\frac{p_n}{q_n}$

    Examples
    ========

    >>> from sympy import Rational, Mul
    >>> from sympy.functions.elementary._trigonometric_special import ipartfrac

    >>> denoms = 2, 3, 5
    >>> numers = ipartfrac(2, 3, 5)
    >>> numers
    (1, 7, -14)

    >>> Rational(1, Mul(*denoms))
    1/30
    >>> out = 0
    >>> for n, d in zip(numers, denoms):
    ...    out += Rational(n, d)
    >>> out
    1/30
    '''
    pass
# WARNING: Decompyle incomplete


def fermat_coords(n = None):
