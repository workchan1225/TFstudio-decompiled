# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: gammasimp.pyc (Python 3.11)

from sympy.core import Function, S, Mul, Pow, Add
from sympy.core.sorting import ordered, default_sort_key
from sympy.core.function import expand_func
from sympy.core.symbol import Dummy
from sympy.functions import gamma, sqrt, sin
from sympy.polys import factor, cancel
from sympy.utilities.iterables import sift, uniq

def gammasimp(expr):
    """
    Simplify expressions with gamma functions.

    Explanation
    ===========

    This function takes as input an expression containing gamma
    functions or functions that can be rewritten in terms of gamma
    functions and tries to minimize the number of those functions and
    reduce the size of their arguments.

    The algorithm works by rewriting all gamma functions as expressions
    involving rising factorials (Pochhammer symbols) and applies
    recurrence relations and other transformations applicable to rising
    factorials, to reduce their arguments, possibly letting the resulting
    rising factorial to cancel. Rising factorials with the second argument
    being an integer are expanded into polynomial forms and finally all
    other rising factorial are rewritten in terms of gamma functions.

    Then the following two steps are performed.

    1. Reduce the number of gammas by applying the reflection theorem
       gamma(x)*gamma(1-x) == pi/sin(pi*x).
    2. Reduce the number of gammas by applying the multiplication theorem
       gamma(x)*gamma(x+1/n)*...*gamma(x+(n-1)/n) == C*gamma(n*x).

    It then reduces the number of prefactors by absorbing them into gammas
    where possible and expands gammas with rational argument.

    All transformation rules can be found (or were derived from) here:

    .. [1] https://functions.wolfram.com/GammaBetaErf/Pochhammer/17/01/02/
    .. [2] https://functions.wolfram.com/GammaBetaErf/Pochhammer/27/01/0005/

    Examples
    ========

    >>> from sympy.simplify import gammasimp
    >>> from sympy import gamma, Symbol
    >>> from sympy.abc import x
    >>> n = Symbol('n', integer = True)

    >>> gammasimp(gamma(x)/gamma(x - 3))
    (x - 3)*(x - 2)*(x - 1)
    >>> gammasimp(gamma(n + 3))
    gamma(n + 3)

    """
    expr = expr.rewrite(gamma)
    f = expr.atoms(Function)
    gammas = f()
    if not gammas:
        return expr
    (lambda .0: pass# WARNING: Decompyle incomplete
) -= gammas
    f = f & expr.as_dummy().atoms(Function)
# WARNING: Decompyle incomplete


def _gammasimp(expr, as_comb):
    '''
    Helper function for gammasimp and combsimp.

    Explanation
    ===========

    Simplifies expressions written in terms of gamma function. If
    as_comb is True, it tries to preserve integer arguments. See
    docstring of gammasimp for more information. This was part of
    combsimp() in combsimp.py.
    '''
    pass
# WARNING: Decompyle incomplete


class _rf(Function):
    eval = (lambda cls, a, b: pass# WARNING: Decompyle incomplete
)()
