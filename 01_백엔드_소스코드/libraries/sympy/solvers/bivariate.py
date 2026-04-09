# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bivariate.pyc (Python 3.11)

from sympy.core.add import Add
from sympy.core.exprtools import factor_terms
from sympy.core.function import expand_log, _mexpand
from sympy.core.power import Pow
from sympy.core.singleton import S
from sympy.core.sorting import ordered
from sympy.core.symbol import Dummy
from sympy.functions.elementary.exponential import LambertW, exp, log
from sympy.functions.elementary.miscellaneous import root
from sympy.polys.polyroots import roots
from sympy.polys.polytools import Poly, factor
from sympy.simplify.simplify import separatevars
from sympy.simplify.radsimp import collect
from sympy.simplify.simplify import powsimp
from sympy.solvers.solvers import solve, _invert
from sympy.utilities.iterables import uniq

def _filtered_gens(poly, symbol):
    '''process the generators of ``poly``, returning the set of generators that
    have ``symbol``.  If there are two generators that are inverses of each other,
    prefer the one that has no denominator.

    Examples
    ========

    >>> from sympy.solvers.bivariate import _filtered_gens
    >>> from sympy import Poly, exp
    >>> from sympy.abc import x
    >>> _filtered_gens(Poly(x + 1/x + exp(x)), x)
    {x, exp(x)}

    '''
    pass
# WARNING: Decompyle incomplete


def _mostfunc(lhs, func, X = (None,)):
    '''Returns the term in lhs which contains the most of the
    func-type things e.g. log(log(x)) wins over log(x) if both terms appear.

    ``func`` can be a function (exp, log, etc...) or any other SymPy object,
    like Pow.

    If ``X`` is not ``None``, then the function returns the term composed with the
    most ``func`` having the specified variable.

    Examples
    ========

    >>> from sympy.solvers.bivariate import _mostfunc
    >>> from sympy import exp
    >>> from sympy.abc import x, y
    >>> _mostfunc(exp(x) + exp(exp(x) + 2), exp)
    exp(exp(x) + 2)
    >>> _mostfunc(exp(x) + exp(exp(y) + 2), exp)
    exp(exp(y) + 2)
    >>> _mostfunc(exp(x) + exp(exp(y) + 2), exp, x)
    exp(x)
    >>> _mostfunc(x, exp, x) is None
    True
    >>> _mostfunc(exp(x) + exp(x*y), exp, x)
    exp(x)
    '''
    pass
# WARNING: Decompyle incomplete


def _linab(arg, symbol):
    '''Return ``a, b, X`` assuming ``arg`` can be written as ``a*X + b``
    where ``X`` is a symbol-dependent factor and ``a`` and ``b`` are
    independent of ``symbol``.

    Examples
    ========

    >>> from sympy.solvers.bivariate import _linab
    >>> from sympy.abc import x, y
    >>> from sympy import exp, S
    >>> _linab(S(2), x)
    (2, 0, 1)
    >>> _linab(2*x, x)
    (2, 0, x)
    >>> _linab(y + y*x + 2*x, x)
    (y + 2, y, x)
    >>> _linab(3 + 2*exp(x), x)
    (2, 3, exp(x))
    '''
    arg = factor_terms(arg.expand())
    (ind, dep) = arg.as_independent(symbol)
    if arg.is_Mul and dep.is_Add:
        (a, b, x) = _linab(dep, symbol)
        return (ind * a, ind * b, x)
    if not None.is_Add:
        b = 0
        x = dep
        a = ind
    else:
        b = ind
        (a, x) = separatevars(dep).as_independent(symbol, as_Add = False)
    if x.could_extract_minus_sign():
        a = -a
        x = -x
    return (a, b, x)


def _lambert(eq, x):
    '''
    Given an expression assumed to be in the form
        ``F(X, a..f) = a*log(b*X + c) + d*X + f = 0``
    where X = g(x) and x = g^-1(X), return the Lambert solution,
        ``x = g^-1(-c/b + (a/d)*W(d/(a*b)*exp(c*d/a/b)*exp(-f/a)))``.
    '''
    pass
# WARNING: Decompyle incomplete


def _solve_lambert(f, symbol, gens):
    '''Return solution to ``f`` if it is a Lambert-type expression
    else raise NotImplementedError.

    For ``f(X, a..f) = a*log(b*X + c) + d*X - f = 0`` the solution
    for ``X`` is ``X = -c/b + (a/d)*W(d/(a*b)*exp(c*d/a/b)*exp(f/a))``.
    There are a variety of forms for `f(X, a..f)` as enumerated below:

    1a1)
      if B**B = R for R not in [0, 1] (since those cases would already
      be solved before getting here) then log of both sides gives
      log(B) + log(log(B)) = log(log(R)) and
      X = log(B), a = 1, b = 1, c = 0, d = 1, f = log(log(R))
    1a2)
      if B*(b*log(B) + c)**a = R then log of both sides gives
      log(B) + a*log(b*log(B) + c) = log(R) and
      X = log(B), d=1, f=log(R)
    1b)
      if a*log(b*B + c) + d*B = R and
      X = B, f = R
    2a)
      if (b*B + c)*exp(d*B + g) = R then log of both sides gives
      log(b*B + c) + d*B + g = log(R) and
      X = B, a = 1, f = log(R) - g
    2b)
      if g*exp(d*B + h) - b*B = c then the log form is
      log(g) + d*B + h - log(b*B + c) = 0 and
      X = B, a = -1, f = -h - log(g)
    3)
      if d*p**(a*B + g) - b*B = c then the log form is
      log(d) + (a*B + g)*log(p) - log(b*B + c) = 0 and
      X = B, a = -1, d = a*log(p), f = -log(d) - g*log(p)
    '''
    pass
# WARNING: Decompyle incomplete


def bivariate_type(f, x = None, y = {
    'first': True }, *, first):
    '''Given an expression, f, 3 tests will be done to see what type
    of composite bivariate it might be, options for u(x, y) are::

        x*y
        x+y
        x*y+x
        x*y+y

    If it matches one of these types, ``u(x, y)``, ``P(u)`` and dummy
    variable ``u`` will be returned. Solving ``P(u)`` for ``u`` and
    equating the solutions to ``u(x, y)`` and then solving for ``x`` or
    ``y`` is equivalent to solving the original expression for ``x`` or
    ``y``. If ``x`` and ``y`` represent two functions in the same
    variable, e.g. ``x = g(t)`` and ``y = h(t)``, then if ``u(x, y) - p``
    can be solved for ``t`` then these represent the solutions to
    ``P(u) = 0`` when ``p`` are the solutions of ``P(u) = 0``.

    Only positive values of ``u`` are considered.

    Examples
    ========

    >>> from sympy import solve
    >>> from sympy.solvers.bivariate import bivariate_type
    >>> from sympy.abc import x, y
    >>> eq = (x**2 - 3).subs(x, x + y)
    >>> bivariate_type(eq, x, y)
    (x + y, _u**2 - 3, _u)
    >>> uxy, pu, u = _
    >>> usol = solve(pu, u); usol
    [sqrt(3)]
    >>> [solve(uxy - s) for s in solve(pu, u)]
    [[{x: -y + sqrt(3)}]]
    >>> all(eq.subs(s).equals(0) for sol in _ for s in sol)
    True

    '''
    pass
# WARNING: Decompyle incomplete
