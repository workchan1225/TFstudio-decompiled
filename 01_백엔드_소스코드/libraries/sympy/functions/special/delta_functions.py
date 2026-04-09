# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: delta_functions.pyc (Python 3.11)

from sympy.core import S, diff
from sympy.core.function import Function, ArgumentIndexError
from sympy.core.logic import fuzzy_not
from sympy.core.relational import Eq, Ne
from sympy.functions.elementary.complexes import im, sign
from sympy.functions.elementary.piecewise import Piecewise
from sympy.polys.polyerrors import PolynomialError
from sympy.polys.polyroots import roots
from sympy.utilities.misc import filldedent

class DiracDelta(Function):
    """
    The DiracDelta function and its derivatives.

    Explanation
    ===========

    DiracDelta is not an ordinary function. It can be rigorously defined either
    as a distribution or as a measure.

    DiracDelta only makes sense in definite integrals, and in particular,
    integrals of the form ``Integral(f(x)*DiracDelta(x - x0), (x, a, b))``,
    where it equals ``f(x0)`` if ``a <= x0 <= b`` and ``0`` otherwise. Formally,
    DiracDelta acts in some ways like a function that is ``0`` everywhere except
    at ``0``, but in many ways it also does not. It can often be useful to treat
    DiracDelta in formal ways, building up and manipulating expressions with
    delta functions (which may eventually be integrated), but care must be taken
    to not treat it as a real function. SymPy's ``oo`` is similar. It only
    truly makes sense formally in certain contexts (such as integration limits),
    but SymPy allows its use everywhere, and it tries to be consistent with
    operations on it (like ``1/oo``), but it is easy to get into trouble and get
    wrong results if ``oo`` is treated too much like a number. Similarly, if
    DiracDelta is treated too much like a function, it is easy to get wrong or
    nonsensical results.

    DiracDelta function has the following properties:

    1) $\\frac{d}{d x} \\theta(x) = \\delta(x)$
    2) $\\int_{-\\infty}^\\infty \\delta(x - a)f(x)\\, dx = f(a)$ and $\\int_{a-
       \\epsilon}^{a+\\epsilon} \\delta(x - a)f(x)\\, dx = f(a)$
    3) $\\delta(x) = 0$ for all $x \\neq 0$
    4) $\\delta(g(x)) = \\sum_i \\frac{\\delta(x - x_i)}{\\|g'(x_i)\\|}$ where $x_i$
       are the roots of $g$
    5) $\\delta(-x) = \\delta(x)$

    Derivatives of ``k``-th order of DiracDelta have the following properties:

    6) $\\delta(x, k) = 0$ for all $x \\neq 0$
    7) $\\delta(-x, k) = -\\delta(x, k)$ for odd $k$
    8) $\\delta(-x, k) = \\delta(x, k)$ for even $k$

    Examples
    ========

    >>> from sympy import DiracDelta, diff, pi
    >>> from sympy.abc import x, y

    >>> DiracDelta(x)
    DiracDelta(x)
    >>> DiracDelta(1)
    0
    >>> DiracDelta(-1)
    0
    >>> DiracDelta(pi)
    0
    >>> DiracDelta(x - 4).subs(x, 4)
    DiracDelta(0)
    >>> diff(DiracDelta(x))
    DiracDelta(x, 1)
    >>> diff(DiracDelta(x - 1), x, 2)
    DiracDelta(x - 1, 2)
    >>> diff(DiracDelta(x**2 - 1), x, 2)
    2*(2*x**2*DiracDelta(x**2 - 1, 2) + DiracDelta(x**2 - 1, 1))
    >>> DiracDelta(3*x).is_simple(x)
    True
    >>> DiracDelta(x**2).is_simple(x)
    False
    >>> DiracDelta((x**2 - 1)*y).expand(diracdelta=True, wrt=x)
    DiracDelta(x - 1)/(2*Abs(y)) + DiracDelta(x + 1)/(2*Abs(y))

    See Also
    ========

    Heaviside
    sympy.simplify.simplify.simplify, is_simple
    sympy.functions.special.tensor_functions.KroneckerDelta

    References
    ==========

    .. [1] https://mathworld.wolfram.com/DeltaFunction.html

    """
    is_real = True
    
    def fdiff(self, argindex = (1,)):
        '''
        Returns the first derivative of a DiracDelta Function.

        Explanation
        ===========

        The difference between ``diff()`` and ``fdiff()`` is: ``diff()`` is the
        user-level function and ``fdiff()`` is an object method. ``fdiff()`` is
        a convenience method available in the ``Function`` class. It returns
        the derivative of the function without considering the chain rule.
        ``diff(function, x)`` calls ``Function._eval_derivative`` which in turn
        calls ``fdiff()`` internally to compute the derivative of the function.

        Examples
        ========

        >>> from sympy import DiracDelta, diff
        >>> from sympy.abc import x

        >>> DiracDelta(x).fdiff()
        DiracDelta(x, 1)

        >>> DiracDelta(x, 1).fdiff()
        DiracDelta(x, 2)

        >>> DiracDelta(x**2 - 1).fdiff()
        DiracDelta(x**2 - 1, 1)

        >>> diff(DiracDelta(x, 1)).fdiff()
        DiracDelta(x, 3)

        Parameters
        ==========

        argindex : integer
            degree of derivative

        '''
        if argindex == 1:
            k = 0
            if len(self.args) > 1:
                k = self.args[1]
            return self.func(self.args[0], k + 1)
        raise None(self, argindex)

    eval = (lambda cls, arg, k = (S.Zero,): if k.is_Integer or k.is_negative:
raise ValueError(f'''Error: the second argument of DiracDelta must be             a non-negative integer, {k!s} given instead.''')if arg is S.NaN:
S.NaNif None.is_nonzero:
S.Zeroif None(im(arg).is_zero):
raise ValueError(filldedent(f'''\n                Function defined only for Real Values.\n                Complex part: {repr(im(arg))!s}  found in {repr(arg)!s} .'''))(c, nc) = arg.args_cnc()if c and c[0] is S.NegativeOne:
if k.is_odd:
-cls(-arg, k)if None.is_even:
cls(-arg, k) if k else cls(-arg)Noneif None.is_zero:
cls(arg, evaluate = False))()
    
    def _eval_expand_diracdelta(self, **hints):
        '''
        Compute a simplified representation of the function using
        property number 4. Pass ``wrt`` as a hint to expand the expression
        with respect to a particular variable.

        Explanation
        ===========

        ``wrt`` is:

        - a variable with respect to which a DiracDelta expression will
        get expanded.

        Examples
        ========

        >>> from sympy import DiracDelta
        >>> from sympy.abc import x, y

        >>> DiracDelta(x*y).expand(diracdelta=True, wrt=x)
        DiracDelta(x)/Abs(y)
        >>> DiracDelta(x*y).expand(diracdelta=True, wrt=y)
        DiracDelta(y)/Abs(x)

        >>> DiracDelta(x**2 + x - 2).expand(diracdelta=True, wrt=x)
        DiracDelta(x - 1)/3 + DiracDelta(x + 2)/3

        See Also
        ========

        is_simple, Diracdelta

        '''
        wrt = hints.get('wrt', None)
    # WARNING: Decompyle incomplete

    
    def is_simple(self, x):
        '''
        Tells whether the argument(args[0]) of DiracDelta is a linear
        expression in *x*.

        Examples
        ========

        >>> from sympy import DiracDelta, cos
        >>> from sympy.abc import x, y

        >>> DiracDelta(x*y).is_simple(x)
        True
        >>> DiracDelta(x*y).is_simple(y)
        True

        >>> DiracDelta(x**2 + x - 2).is_simple(x)
        False

        >>> DiracDelta(cos(x)).is_simple(x)
        False

        Parameters
        ==========

        x : can be a symbol

        See Also
        ========

        sympy.simplify.simplify.simplify, DiracDelta

        '''
        p = self.args[0].as_poly(x)
        if p:
            return p.degree() == 1

    
    def _eval_rewrite_as_Piecewise(self, *args, **kwargs):
        """
        Represents DiracDelta in a piecewise form.

        Examples
        ========

        >>> from sympy import DiracDelta, Piecewise, Symbol
        >>> x = Symbol('x')

        >>> DiracDelta(x).rewrite(Piecewise)
        Piecewise((DiracDelta(0), Eq(x, 0)), (0, True))

        >>> DiracDelta(x - 5).rewrite(Piecewise)
        Piecewise((DiracDelta(0), Eq(x, 5)), (0, True))

        >>> DiracDelta(x**2 - 5).rewrite(Piecewise)
           Piecewise((DiracDelta(0), Eq(x**2, 5)), (0, True))

        >>> DiracDelta(x - 5, 4).rewrite(Piecewise)
        DiracDelta(x - 5, 4)

        """
        if len(args) == 1:
            return Piecewise((DiracDelta(0), Eq(args[0], 0)), (0, True))

    
    def _eval_rewrite_as_SingularityFunction(self, *args, **kwargs):
        '''
        Returns the DiracDelta expression written in the form of Singularity
        Functions.

        '''
        solve = solve
        import sympy.solvers
        SingularityFunction = SingularityFunction
        import sympy.functions.special.singularity_functions
        if self == DiracDelta(0):
            return SingularityFunction(0, 0, -1)
        if None == DiracDelta(0, 1):
            return SingularityFunction(0, 0, -2)
        free = None.free_symbols
        if len(free) == 1:
            x = free.pop()
            if len(args) == 1:
                return SingularityFunction(x, solve(args[0], x)[0], -1)
            return SingularityFunction(x, solve(args[0], x)[0], -args[1] - 1)
        raise None(filldedent('\n                rewrite(SingularityFunction) does not support\n                arguments with more that one variable.'))



class Heaviside(Function):
    pass
# WARNING: Decompyle incomplete
