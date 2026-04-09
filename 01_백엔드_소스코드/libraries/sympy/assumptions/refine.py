# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: refine.pyc (Python 3.11)

from __future__ import annotations
from typing import Callable
from sympy.core import S, Add, Expr, Basic, Mul, Pow, Rational
from sympy.core.logic import fuzzy_not
from sympy.logic.boolalg import Boolean
from sympy.assumptions import ask, Q

def refine(expr, assumptions = (True,)):
    '''
    Simplify an expression using assumptions.

    Explanation
    ===========

    Unlike :func:`~.simplify()` which performs structural simplification
    without any assumption, this function transforms the expression into
    the form which is only valid under certain assumptions. Note that
    ``simplify()`` is generally not done in refining process.

    Refining boolean expression involves reducing it to ``S.true`` or
    ``S.false``. Unlike :func:`~.ask()`, the expression will not be reduced
    if the truth value cannot be determined.

    Examples
    ========

    >>> from sympy import refine, sqrt, Q
    >>> from sympy.abc import x
    >>> refine(sqrt(x**2), Q.real(x))
    Abs(x)
    >>> refine(sqrt(x**2), Q.positive(x))
    x

    >>> refine(Q.real(x), Q.positive(x))
    True
    >>> refine(Q.positive(x), Q.real(x))
    Q.positive(x)

    See Also
    ========

    sympy.simplify.simplify.simplify : Structural simplification without assumptions.
    sympy.assumptions.ask.ask : Query for boolean expressions using assumptions.
    '''
    pass
# WARNING: Decompyle incomplete


def refine_abs(expr, assumptions):
    '''
    Handler for the absolute value.

    Examples
    ========

    >>> from sympy import Q, Abs
    >>> from sympy.assumptions.refine import refine_abs
    >>> from sympy.abc import x
    >>> refine_abs(Abs(x), Q.real(x))
    >>> refine_abs(Abs(x), Q.positive(x))
    x
    >>> refine_abs(Abs(x), Q.negative(x))
    -x

    '''
    pass
# WARNING: Decompyle incomplete


def refine_Pow(expr, assumptions):
    '''
    Handler for instances of Pow.

    Examples
    ========

    >>> from sympy import Q
    >>> from sympy.assumptions.refine import refine_Pow
    >>> from sympy.abc import x,y,z
    >>> refine_Pow((-1)**x, Q.real(x))
    >>> refine_Pow((-1)**x, Q.even(x))
    1
    >>> refine_Pow((-1)**x, Q.odd(x))
    -1

    For powers of -1, even parts of the exponent can be simplified:

    >>> refine_Pow((-1)**(x+y), Q.even(x))
    (-1)**y
    >>> refine_Pow((-1)**(x+y+z), Q.odd(x) & Q.odd(z))
    (-1)**y
    >>> refine_Pow((-1)**(x+y+2), Q.odd(x))
    (-1)**(y + 1)
    >>> refine_Pow((-1)**(x+3), True)
    (-1)**(x + 1)

    '''
    Abs = Abs
    import sympy.functions.elementary.complexes
    sign = sign
    import sympy.functions
    if isinstance(expr.base, Abs) and ask(Q.real(expr.base.args[0]), assumptions) and ask(Q.even(expr.exp), assumptions):
        return expr.base.args[0] ** expr.exp
# WARNING: Decompyle incomplete


def refine_atan2(expr, assumptions):
    '''
    Handler for the atan2 function.

    Examples
    ========

    >>> from sympy import Q, atan2
    >>> from sympy.assumptions.refine import refine_atan2
    >>> from sympy.abc import x, y
    >>> refine_atan2(atan2(y,x), Q.real(y) & Q.positive(x))
    atan(y/x)
    >>> refine_atan2(atan2(y,x), Q.negative(y) & Q.negative(x))
    atan(y/x) - pi
    >>> refine_atan2(atan2(y,x), Q.positive(y) & Q.negative(x))
    atan(y/x) + pi
    >>> refine_atan2(atan2(y,x), Q.zero(y) & Q.negative(x))
    pi
    >>> refine_atan2(atan2(y,x), Q.positive(y) & Q.zero(x))
    pi/2
    >>> refine_atan2(atan2(y,x), Q.negative(y) & Q.zero(x))
    -pi/2
    >>> refine_atan2(atan2(y,x), Q.zero(y) & Q.zero(x))
    nan
    '''
    atan = atan
    import sympy.functions.elementary.trigonometric
    (y, x) = expr.args
    if ask(Q.real(y) & Q.positive(x), assumptions):
        return atan(y / x)
    if None(Q.negative(y) & Q.negative(x), assumptions):
        return atan(y / x) - S.Pi
    if None(Q.positive(y) & Q.negative(x), assumptions):
        return atan(y / x) + S.Pi
    if None(Q.zero(y) & Q.negative(x), assumptions):
        return S.Pi
    if None(Q.positive(y) & Q.zero(x), assumptions):
        return S.Pi / 2
    if None(Q.negative(y) & Q.zero(x), assumptions):
        return -(S.Pi) / 2
    if None(Q.zero(y) & Q.zero(x), assumptions):
        return S.NaN


def refine_re(expr, assumptions):
    '''
    Handler for real part.

    Examples
    ========

    >>> from sympy.assumptions.refine import refine_re
    >>> from sympy import Q, re
    >>> from sympy.abc import x
    >>> refine_re(re(x), Q.real(x))
    x
    >>> refine_re(re(x), Q.imaginary(x))
    0
    '''
    arg = expr.args[0]
    if ask(Q.real(arg), assumptions):
        return arg
    if None(Q.imaginary(arg), assumptions):
        return S.Zero
    return None(expr, assumptions)


def refine_im(expr, assumptions):
    '''
    Handler for imaginary part.

    Explanation
    ===========

    >>> from sympy.assumptions.refine import refine_im
    >>> from sympy import Q, im
    >>> from sympy.abc import x
    >>> refine_im(im(x), Q.real(x))
    0
    >>> refine_im(im(x), Q.imaginary(x))
    -I*x
    '''
    arg = expr.args[0]
    if ask(Q.real(arg), assumptions):
        return S.Zero
    if None(Q.imaginary(arg), assumptions):
        return -(S.ImaginaryUnit) * arg
    return None(expr, assumptions)


def refine_arg(expr, assumptions):
    '''
    Handler for complex argument

    Explanation
    ===========

    >>> from sympy.assumptions.refine import refine_arg
    >>> from sympy import Q, arg
    >>> from sympy.abc import x
    >>> refine_arg(arg(x), Q.positive(x))
    0
    >>> refine_arg(arg(x), Q.negative(x))
    pi
    '''
    rg = expr.args[0]
    if ask(Q.positive(rg), assumptions):
        return S.Zero
    if None(Q.negative(rg), assumptions):
        return S.Pi


def _refine_reim(expr, assumptions):
