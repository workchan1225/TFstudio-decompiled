# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fu.pyc (Python 3.11)

from collections import defaultdict
from sympy.core.add import Add
from sympy.core.expr import Expr
from sympy.core.exprtools import Factors, gcd_terms, factor_terms
from sympy.core.function import expand_mul
from sympy.core.mul import Mul
from sympy.core.numbers import pi, I
from sympy.core.power import Pow
from sympy.core.singleton import S
from sympy.core.sorting import ordered
from sympy.core.symbol import Dummy
from sympy.core.sympify import sympify
from sympy.core.traversal import bottom_up
from sympy.functions.combinatorial.factorials import binomial
from sympy.functions.elementary.hyperbolic import cosh, sinh, tanh, coth, sech, csch, HyperbolicFunction
from sympy.functions.elementary.trigonometric import cos, sin, tan, cot, sec, csc, sqrt, TrigonometricFunction
from sympy.ntheory.factor_ import perfect_power
from sympy.polys.polytools import factor
from sympy.strategies.tree import greedy
from sympy.strategies.core import identity, debug
from sympy import SYMPY_DEBUG

def TR0(rv):
    '''Simplification of rational polynomials, trying to simplify
    the expression, e.g. combine things like 3*x + 2*x, etc....
    '''
    return rv.normal().factor().expand()


def TR1(rv):
    '''Replace sec, csc with 1/cos, 1/sin

    Examples
    ========

    >>> from sympy.simplify.fu import TR1, sec, csc
    >>> from sympy.abc import x
    >>> TR1(2*csc(x) + sec(x))
    1/cos(x) + 2/sin(x)
    '''
    
    def f(rv):
        if isinstance(rv, sec):
            a = rv.args[0]
            return S.One / cos(a)
        if None(rv, csc):
            a = rv.args[0]
            return S.One / sin(a)

    return bottom_up(rv, f)


def TR2(rv):
    '''Replace tan and cot with sin/cos and cos/sin

    Examples
    ========

    >>> from sympy.simplify.fu import TR2
    >>> from sympy.abc import x
    >>> from sympy import tan, cot, sin, cos
    >>> TR2(tan(x))
    sin(x)/cos(x)
    >>> TR2(cot(x))
    cos(x)/sin(x)
    >>> TR2(tan(tan(x) - sin(x)/cos(x)))
    0

    '''
    
    def f(rv):
        if isinstance(rv, tan):
            a = rv.args[0]
            return sin(a) / cos(a)
        if None(rv, cot):
            a = rv.args[0]
            return cos(a) / sin(a)

    return bottom_up(rv, f)


def TR2i(rv, half = (False,)):
    '''Converts ratios involving sin and cos as follows::
        sin(x)/cos(x) -> tan(x)
        sin(x)/(cos(x) + 1) -> tan(x/2) if half=True

    Examples
    ========

    >>> from sympy.simplify.fu import TR2i
    >>> from sympy.abc import x, a
    >>> from sympy import sin, cos
    >>> TR2i(sin(x)/cos(x))
    tan(x)

    Powers of the numerator and denominator are also recognized

    >>> TR2i(sin(x)**2/(cos(x) + 1)**2, half=True)
    tan(x/2)**2

    The transformation does not take place unless assumptions allow
    (i.e. the base must be positive or the exponent must be an integer
    for both numerator and denominator)

    >>> TR2i(sin(x)**a/(cos(x) + 1)**a)
    sin(x)**a/(cos(x) + 1)**a

    '''
    pass
# WARNING: Decompyle incomplete


def TR3(rv):
    '''Induced formula: example sin(-a) = -sin(a)

    Examples
    ========

    >>> from sympy.simplify.fu import TR3
    >>> from sympy.abc import x, y
    >>> from sympy import pi
    >>> from sympy import cos
    >>> TR3(cos(y - x*(y - x)))
    cos(x*(x - y) + y)
    >>> cos(pi/2 + x)
    -sin(x)
    >>> cos(30*pi/2 + x)
    -cos(x)

    '''
    pass
# WARNING: Decompyle incomplete


def TR4(rv):
    """Identify values of special angles.

        a=  0   pi/6        pi/4        pi/3        pi/2
    ----------------------------------------------------
    sin(a)  0   1/2         sqrt(2)/2   sqrt(3)/2   1
    cos(a)  1   sqrt(3)/2   sqrt(2)/2   1/2         0
    tan(a)  0   sqt(3)/3    1           sqrt(3)     --

    Examples
    ========

    >>> from sympy import pi
    >>> from sympy import cos, sin, tan, cot
    >>> for s in (0, pi/6, pi/4, pi/3, pi/2):
    ...    print('%s %s %s %s' % (cos(s), sin(s), tan(s), cot(s)))
    ...
    1 0 0 zoo
    sqrt(3)/2 1/2 sqrt(3)/3 sqrt(3)
    sqrt(2)/2 sqrt(2)/2 1 1
    1/2 sqrt(3)/2 sqrt(3) sqrt(3)/3
    0 1 zoo 0
    """
    return rv.replace((lambda x:
