# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bsplines.pyc (Python 3.11)

from sympy.core import S, sympify
from sympy.core.symbol import Dummy, symbols
from sympy.functions import Piecewise, piecewise_fold
from sympy.logic.boolalg import And
from sympy.sets.sets import Interval
from functools import lru_cache

def _ivl(cond, x):
    """return the interval corresponding to the condition

    Conditions in spline's Piecewise give the range over
    which an expression is valid like (lo <= x) & (x <= hi).
    This function returns (lo, hi).
    """
    if isinstance(cond, And) and len(cond.args) == 2:
        (a, b) = cond.args
        if a.lts == x:
            b = a
            a = b
        return (a.lts, b.gts)
    raise None('unexpected cond type: %s' % cond)


def _add_splines(c, b1, d, b2, x):
    '''Construct c*b1 + d*b2.'''
    if S.Zero in (b1, c):
        rv = piecewise_fold(d * b2)
    elif S.Zero in (b2, d):
        rv = piecewise_fold(c * b1)
# WARNING: Decompyle incomplete

bspline_basis = (lambda d, knots, n, x: xvar = xx = Dummy()knots = (lambda .0: pass# WARNING: Decompyle incomplete
)(knots())
    d = int(d)
    n = int(n)
    n_knots = len(knots)
    n_intervals = n_knots - 1
    if n + d + 1 > n_intervals:
        raise ValueError('n + d + 1 must not exceed len(knots) - 1')
    if d == 0:
        result = Piecewise((S.One, Interval(knots[n], knots[n + 1]).contains(x)), (0, True))
    elif d > 0:
        denom = knots[n + d + 1] - knots[n + 1]
        denom = knots[n + d] - knots[n]
        result = _add_splines(A, b1, B, b2, x)
    else:
        raise ValueError('degree must be non-negative: %r' % n)
    return result.xreplace({
        x: xvar })
)()

def bspline_basis_set(d, knots, x):
    '''
    Return the ``len(knots)-d-1`` B-splines at *x* of degree *d*
    with *knots*.

    Explanation
    ===========

    This function returns a list of piecewise polynomials that are the
    ``len(knots)-d-1`` B-splines of degree *d* for the given knots.
    This function calls ``bspline_basis(d, knots, n, x)`` for different
    values of *n*.

    Examples
    ========

    >>> from sympy import bspline_basis_set
    >>> from sympy.abc import x
    >>> d = 2
    >>> knots = range(5)
    >>> splines = bspline_basis_set(d, knots, x)
    >>> splines
    [Piecewise((x**2/2, (x >= 0) & (x <= 1)),
               (-x**2 + 3*x - 3/2, (x >= 1) & (x <= 2)),
               (x**2/2 - 3*x + 9/2, (x >= 2) & (x <= 3)),
               (0, True)),
    Piecewise((x**2/2 - x + 1/2, (x >= 1) & (x <= 2)),
              (-x**2 + 5*x - 11/2, (x >= 2) & (x <= 3)),
              (x**2/2 - 4*x + 8, (x >= 3) & (x <= 4)),
              (0, True))]

    Parameters
    ==========

    d : integer
        degree of bspline

    knots : list of integers
        list of knots points of bspline

    x : symbol

    See Also
    ========

    bspline_basis

    '''
    pass
# WARNING: Decompyle incomplete


def interpolating_spline(d, x, X, Y):
    '''
    Return spline of degree *d*, passing through the given *X*
    and *Y* values.

    Explanation
    ===========

    This function returns a piecewise function such that each part is
    a polynomial of degree not greater than *d*. The value of *d*
    must be 1 or greater and the values of *X* must be strictly
    increasing.

    Examples
    ========

    >>> from sympy import interpolating_spline
    >>> from sympy.abc import x
    >>> interpolating_spline(1, x, [1, 2, 4, 7], [3, 6, 5, 7])
    Piecewise((3*x, (x >= 1) & (x <= 2)),
            (7 - x/2, (x >= 2) & (x <= 4)),
            (2*x/3 + 7/3, (x >= 4) & (x <= 7)))
    >>> interpolating_spline(3, x, [-2, 0, 1, 3, 4], [4, 2, 1, 1, 3])
    Piecewise((7*x**3/117 + 7*x**2/117 - 131*x/117 + 2, (x >= -2) & (x <= 1)),
            (10*x**3/117 - 2*x**2/117 - 122*x/117 + 77/39, (x >= 1) & (x <= 4)))

    Parameters
    ==========

    d : integer
        Degree of Bspline strictly greater than equal to one

    x : symbol

    X : list of strictly increasing real values
        list of X coordinates through which the spline passes

    Y : list of real values
        list of corresponding Y coordinates through which the spline passes

    See Also
    ========

    bspline_basis_set, interpolating_poly

    '''
    pass
# WARNING: Decompyle incomplete
