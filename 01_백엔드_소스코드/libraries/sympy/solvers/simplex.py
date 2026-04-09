# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: simplex.pyc (Python 3.11)

'''Tools for optimizing a linear function for a given simplex.

For the linear objective function ``f`` with linear constraints
expressed using `Le`, `Ge` or `Eq` can be found with ``lpmin`` or
``lpmax``. The symbols are **unbounded** unless specifically
constrained.

As an alternative, the matrices describing the objective and the
constraints, and an optional list of bounds can be passed to
``linprog`` which will solve for the minimization of ``C*x``
under constraints ``A*x <= b`` and/or ``Aeq*x = beq``, and
individual bounds for variables given as ``(lo, hi)``. The values
returned are **nonnegative** unless bounds are provided that
indicate otherwise.

Errors that might be raised are UnboundedLPError when there is no
finite solution for the system or InfeasibleLPError when the
constraints represent impossible conditions (i.e. a non-existant
 simplex).

Here is a simple 1-D system: minimize `x` given that ``x >= 1``.

    >>> from sympy.solvers.simplex import lpmin, linprog
    >>> from sympy.abc import x

    The function and a list with the constraint is passed directly
    to `lpmin`:

    >>> lpmin(x, [x >= 1])
    (1, {x: 1})

    For `linprog` the matrix for the objective is `[1]` and the
    uivariate constraint can be passed as a bound with None acting
    as infinity:

    >>> linprog([1], bounds=(1, None))
    (1, [1])

    Or the matrices, corresponding to ``x >= 1`` expressed as
    ``-x <= -1`` as required by the routine, can be passed:

    >>> linprog([1], [-1], [-1])
    (1, [1])

    If there is no limit for the objective, an error is raised.
    In this case there is a valid region of interest (simplex)
    but no limit to how small ``x`` can be:

    >>> lpmin(x, [])
    Traceback (most recent call last):
    ...
    sympy.solvers.simplex.UnboundedLPError:
    Objective function can assume arbitrarily large values!

    An error is raised if there is no possible solution:

    >>> lpmin(x,[x<=1,x>=2])
    Traceback (most recent call last):
    ...
    sympy.solvers.simplex.InfeasibleLPError:
    Inconsistent/False constraint
'''
from sympy.core import sympify
from sympy.core.exprtools import factor_terms
from sympy.core.relational import Le, Ge, Eq
from sympy.core.singleton import S
from sympy.core.symbol import Dummy
from sympy.core.sorting import ordered
from sympy.functions.elementary.complexes import sign
from sympy.matrices.dense import Matrix, zeros
from sympy.solvers.solveset import linear_eq_to_matrix
from sympy.utilities.iterables import numbered_symbols
from sympy.utilities.misc import filldedent

class UnboundedLPError(Exception):
    """
    A linear programing problem is said to be unbounded if its objective
    function can assume arbitrarily large values.

    Example
    =======

    Suppose you want to maximize
        2x
    subject to
        x >= 0

    There's no upper limit that 2x can take.
    """
    pass


class InfeasibleLPError(Exception):
    '''
    A linear programing problem is considered infeasible if its
    constraint set is empty. That is, if the set of all vectors
    satisfying the contraints is empty, then the problem is infeasible.

    Example
    =======

    Suppose you want to maximize
        x
    subject to
        x >= 10
        x <= 9

    No x can satisfy those constraints.
    '''
    pass


def _pivot(M, i, j):
    """
    The pivot element `M[i, j]` is inverted and the rest of the matrix
    modified and returned as a new matrix; original is left unmodified.

    Example
    =======

    >>> from sympy.matrices.dense import Matrix
    >>> from sympy.solvers.simplex import _pivot
    >>> from sympy import var
    >>> Matrix(3, 3, var('a:i'))
    Matrix([
    [a, b, c],
    [d, e, f],
    [g, h, i]])
    >>> _pivot(_, 1, 0)
    Matrix([
    [-a/d, -a*e/d + b, -a*f/d + c],
    [ 1/d,        e/d,        f/d],
    [-g/d,  h - e*g/d,  i - f*g/d]])
    """
    Mij = M[(i, j)]
    Mj = M[(:, j)]
    Mi = M[(i, :)]
    if Mij == 0:
        raise ZeroDivisionError('Tried to pivot about zero-valued entry.')
    A = M - Mj * (Mi / Mij)
    A[(i, :)] = Mi / Mij
    A[(:, j)] = -Mj / Mij
    A[(i, j)] = 1 / Mij
    return A


def _choose_pivot_row(A, B, candidate_rows, pivot_col, Y):
    pass
# WARNING: Decompyle incomplete


def _simplex(A, B, C, D, dual = (None, False)):
    '''Return ``(o, x, y)`` obtained from the two-phase simplex method
    using Bland\'s rule: ``o`` is the minimum value of primal,
    ``Cx - D``, under constraints ``Ax <= B`` (with ``x >= 0``) and
    the maximum of the dual, ``y^{T}B - D``, under constraints
    ``A^{T}*y >= C^{T}`` (with ``y >= 0``). To compute the dual of
    the system, pass `dual=True` and ``(o, y, x)`` will be returned.

    Note: the nonnegative constraints for ``x`` and ``y`` supercede
    any values of ``A`` and ``B`` that are inconsistent with that
    assumption, so if a constraint of ``x >= -1`` is represented
    in ``A`` and ``B``, no value will be obtained that is negative; if
    a constraint of ``x <= -1`` is represented, an error will be
    raised since no solution is possible.

    This routine relies on the ability of determining whether an
    expression is 0 or not. This is guaranteed if the input contains
    only Float or Rational entries. It will raise a TypeError if
    a relationship does not evaluate to True or False.

    Examples
    ========

    >>> from sympy.solvers.simplex import _simplex
    >>> from sympy import Matrix

    Consider the simple minimization of ``f = x + y + 1`` under the
    constraint that ``y + 2*x >= 4``. This is the "standard form" of
    a minimization.

    In the nonnegative quadrant, this inequality describes a area above
    a triangle with vertices at (0, 4), (0, 0) and (2, 0). The minimum
    of ``f`` occurs at (2, 0). Define A, B, C, D for the standard
    minimization:

    >>> A = Matrix([[2, 1]])
    >>> B = Matrix([4])
    >>> C = Matrix([[1, 1]])
    >>> D = Matrix([-1])

    Confirm that this is the system of interest:

    >>> from sympy.abc import x, y
    >>> X = Matrix([x, y])
    >>> (C*X - D)[0]
    x + y + 1
    >>> [i >= j for i, j in zip(A*X, B)]
    [2*x + y >= 4]

    Since `_simplex` will do a minimization for constraints given as
    ``A*x <= B``, the signs of ``A`` and ``B`` must be negated since
    the currently correspond to a greater-than inequality:

    >>> _simplex(-A, -B, C, D)
    (3, [2, 0], [1/2])

    The dual of minimizing ``f`` is maximizing ``F = c*y - d`` for
    ``a*y <= b`` where ``a``, ``b``, ``c``, ``d`` are derived from the
    transpose of the matrix representation of the standard minimization:

    >>> tr = lambda a, b, c, d: [i.T for i in (a, c, b, d)]
    >>> a, b, c, d = tr(A, B, C, D)

    This time ``a*x <= b`` is the expected inequality for the `_simplex`
    method, but to maximize ``F``, the sign of ``c`` and ``d`` must be
    changed (so that minimizing the negative will give the negative of
    the maximum of ``F``):

    >>> _simplex(a, b, -c, -d)
    (-3, [1/2], [2, 0])

    The negative of ``F`` and the min of ``f`` are the same. The dual
    point `[1/2]` is the value of ``y`` that minimized ``F = c*y - d``
    under constraints a*x <= b``:

    >>> y = Matrix([\'y\'])
    >>> (c*y - d)[0]
    4*y + 1
    >>> [i <= j for i, j in zip(a*y,b)]
    [2*y <= 1, y <= 1]

    In this 1-dimensional dual system, the more restrictive contraint is
    the first which limits ``y`` between 0 and 1/2 and the maximum of
    ``F`` is attained at the nonzero value, hence is ``4*(1/2) + 1 = 3``.

    In this case the values for ``x`` and ``y`` were the same when the
    dual representation was solved. This is not always the case (though
    the value of the function will be the same).

    >>> l = [[1, 1], [-1, 1], [0, 1], [-1, 0]], [5, 1, 2, -1], [[1, 1]], [-1]
    >>> A, B, C, D = [Matrix(i) for i in l]
    >>> _simplex(A, B, -C, -D)
    (-6, [3, 2], [1, 0, 0, 0])
    >>> _simplex(A, B, -C, -D, dual=True)  # [5, 0] != [3, 2]
    (-6, [1, 0, 0, 0], [5, 0])

    In both cases the function has the same value:

    >>> Matrix(C)*Matrix([3, 2]) == Matrix(C)*Matrix([5, 0])
    True

    See Also
    ========
    _lp - poses min/max problem in form compatible with _simplex
    lpmin - minimization which calls _lp
    lpmax - maximimzation which calls _lp

    References
    ==========

    .. [1] Thomas S. Ferguson, LINEAR PROGRAMMING: A Concise Introduction
           web.tecnico.ulisboa.pt/mcasquilho/acad/or/ftp/FergusonUCLA_lp.pdf

    '''
    pass
# WARNING: Decompyle incomplete


def _abcd(M, list = (False,)):
    '''return parts of M as matrices or lists

    Examples
    ========

    >>> from sympy import Matrix
    >>> from sympy.solvers.simplex import _abcd

    >>> m = Matrix(3, 3, range(9)); m
    Matrix([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]])
    >>> a, b, c, d = _abcd(m)
    >>> a
    Matrix([
    [0, 1],
    [3, 4]])
    >>> b
    Matrix([
    [2],
    [5]])
    >>> c
    Matrix([[6, 7]])
    >>> d
    Matrix([[8]])

    The matrices can be returned as compact lists, too:

    >>> L = a, b, c, d = _abcd(m, list=True); L
    ([[0, 1], [3, 4]], [2, 5], [[6, 7]], [8])
    '''
    pass
# WARNING: Decompyle incomplete


def _m(a, b, c, d = (None,)):
