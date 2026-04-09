# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sqrtdenest.pyc (Python 3.11)

from sympy.core import Add, Expr, Mul, S, sympify
from sympy.core.function import _mexpand, count_ops, expand_mul
from sympy.core.sorting import default_sort_key
from sympy.core.symbol import Dummy
from sympy.functions import root, sign, sqrt
from sympy.polys import Poly, PolynomialError

def is_sqrt(expr):
    '''Return True if expr is a sqrt, otherwise False.'''
    if expr.is_Pow:
        if expr.exp.is_Rational:
            pass
    return abs(expr.exp) is S.Half


def sqrt_depth(p = None):
    '''Return the maximum depth of any square root argument of p.

    >>> from sympy.functions.elementary.miscellaneous import sqrt
    >>> from sympy.simplify.sqrtdenest import sqrt_depth

    Neither of these square roots contains any other square roots
    so the depth is 1:

    >>> sqrt_depth(1 + sqrt(2)*(1 + sqrt(3)))
    1

    The sqrt(3) is contained within a square root so the depth is
    2:

    >>> sqrt_depth(1 + sqrt(2)*sqrt(1 + sqrt(3)))
    2
    '''
    if p is S.ImaginaryUnit:
        return 1
    if None.is_Atom:
        return 0
    if None.is_Add or p.is_Mul:
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(p.args())
    if None(p):
        return sqrt_depth(p.base) + 1


def is_algebraic(p):
    '''Return True if p is comprised of only Rationals or square roots
    of Rationals and algebraic operations.

    Examples
    ========

    >>> from sympy.functions.elementary.miscellaneous import sqrt
    >>> from sympy.simplify.sqrtdenest import is_algebraic
    >>> from sympy import cos
    >>> is_algebraic(sqrt(2)*(3/(sqrt(7) + sqrt(5)*sqrt(2))))
    True
    >>> is_algebraic(sqrt(2)*(3/(sqrt(7) + sqrt(5)*cos(2))))
    False
    '''
    if p.is_Rational:
        return True
    if None.is_Atom:
        return False
    if (None(p) or p.is_Pow) and p.exp.is_Integer:
        return is_algebraic(p.base)
    if None.is_Add or p.is_Mul:
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(p.args())


def _subsets(n):
    '''
    Returns all possible subsets of the set (0, 1, ..., n-1) except the
    empty set, listed in reversed lexicographical order according to binary
    representation, so that the case of the fourth root is treated last.

    Examples
    ========

    >>> from sympy.simplify.sqrtdenest import _subsets
    >>> _subsets(2)
    [[1, 0], [0, 1], [1, 1]]

    '''
    if n == 1:
        a = [
            [
                1]]
    elif n == 2:
        a = [
            [
                1,
                0],
            [
                0,
                1],
            [
                1,
                1]]
    elif n == 3:
        a = [
            [
                1,
                0,
                0],
            [
                0,
                1,
                0],
            [
                1,
                1,
                0],
            [
                0,
                0,
                1],
            [
                1,
                0,
                1],
            [
                0,
                1,
                1],
            [
                1,
                1,
                1]]
    else:
        b = _subsets(n - 1)
        a0 = b()
        a1 = b()
        a = a0 + [
            [
                0] * (n - 1) + [
                1]] + a1
    return a


def sqrtdenest(expr, max_iter = (3,)):
    """Denests sqrts in an expression that contain other square roots
    if possible, otherwise returns the expr unchanged. This is based on the
    algorithms of [1].

    Examples
    ========

    >>> from sympy.simplify.sqrtdenest import sqrtdenest
    >>> from sympy import sqrt
    >>> sqrtdenest(sqrt(5 + 2 * sqrt(6)))
    sqrt(2) + sqrt(3)

    See Also
    ========

    sympy.solvers.solvers.unrad

    References
    ==========

    .. [1] https://web.archive.org/web/20210806201615/https://researcher.watson.ibm.com/researcher/files/us-fagin/symb85.pdf

    .. [2] D. J. Jeffrey and A. D. Rich, 'Symplifying Square Roots of Square Roots
           by Denesting' (available at https://www.cybertester.com/data/denest.pdf)

    """
    expr = expand_mul(expr)
    for i in range(max_iter):
        z = _sqrtdenest0(expr)
        if expr == z:
            
            return None, expr
        return expr


def _sqrt_match(p):
