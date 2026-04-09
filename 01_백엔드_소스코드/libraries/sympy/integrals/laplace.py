# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: laplace.pyc (Python 3.11)

'''Laplace Transforms'''
import sys
import sympy
from sympy.core import S, pi, I
from sympy.core.add import Add
from sympy.core.cache import cacheit
from sympy.core.expr import Expr
from sympy.core.function import AppliedUndef, Derivative, expand, expand_complex, expand_mul, expand_trig, Lambda, WildFunction, diff, Subs
from sympy.core.mul import Mul, prod
from sympy.core.relational import _canonical, Ge, Gt, Lt, Unequality, Eq, Ne, Relational
from sympy.core.sorting import ordered
from sympy.core.symbol import Dummy, symbols, Wild
from sympy.functions.elementary.complexes import re, im, arg, Abs, polar_lift, periodic_argument
from sympy.functions.elementary.exponential import exp, log
from sympy.functions.elementary.hyperbolic import cosh, coth, sinh, asinh
from sympy.functions.elementary.miscellaneous import Max, Min, sqrt
from sympy.functions.elementary.piecewise import Piecewise, piecewise_exclusive
from sympy.functions.elementary.trigonometric import cos, sin, atan, sinc
from sympy.functions.special.bessel import besseli, besselj, besselk, bessely
from sympy.functions.special.delta_functions import DiracDelta, Heaviside
from sympy.functions.special.error_functions import erf, erfc, Ei
from sympy.functions.special.gamma_functions import digamma, gamma, lowergamma, uppergamma
from sympy.functions.special.singularity_functions import SingularityFunction
from sympy.integrals import integrate, Integral
from sympy.integrals.transforms import _simplify, IntegralTransform, IntegralTransformError
from sympy.logic.boolalg import to_cnf, conjuncts, disjuncts, Or, And
from sympy.matrices.matrixbase import MatrixBase
from sympy.polys.matrices.linsolve import _lin_eq2dict
from sympy.polys.polyerrors import PolynomialError
from sympy.polys.polyroots import roots
from sympy.polys.polytools import Poly
from sympy.polys.rationaltools import together
from sympy.polys.rootoftools import RootSum
from sympy.utilities.exceptions import sympy_deprecation_warning, SymPyDeprecationWarning, ignore_warnings
from sympy.utilities.misc import debugf
_LT_level = 0

def DEBUG_WRAP(func):
    pass
# WARNING: Decompyle incomplete


def _debug(text):
    SYMPY_DEBUG = SYMPY_DEBUG
    import sympy
    if SYMPY_DEBUG:
        print(f'''-LT- {'  ' * _LT_level!s}{text!s}''', file = sys.stderr)
        return None


def _simplifyconds(expr, s, a):
    '''
    Naively simplify some conditions occurring in ``expr``,
    given that `\\operatorname{Re}(s) > a`.

    Examples
    ========

    >>> from sympy.integrals.laplace import _simplifyconds
    >>> from sympy.abc import x
    >>> from sympy import sympify as S
    >>> _simplifyconds(abs(x**2) < 1, x, 1)
    False
    >>> _simplifyconds(abs(x**2) < 1, x, 2)
    False
    >>> _simplifyconds(abs(x**2) < 1, x, 0)
    Abs(x**2) < 1
    >>> _simplifyconds(abs(1/x**2) < 1, x, 1)
    True
    >>> _simplifyconds(S(1) < abs(x), x, 1)
    True
    >>> _simplifyconds(S(1) < abs(1/x), x, 1)
    False

    >>> from sympy import Ne
    >>> _simplifyconds(Ne(1, x**3), x, 1)
    True
    >>> _simplifyconds(Ne(1, x**3), x, 2)
    True
    >>> _simplifyconds(Ne(1, x**3), x, 0)
    Ne(1, x**3)
    '''
    pass
# WARNING: Decompyle incomplete

expand_dirac_delta = (lambda expr: _lin_eq2dict(expr, expr.atoms(DiracDelta)))()
_laplace_transform_integration = (lambda f, t, s_, *, simplify, F = None, cond = None: pass# WARNING: Decompyle incomplete
)()
_laplace_deep_collect = (lambda f, t: pass# WARNING: Decompyle incomplete
)()
_laplace_build_rules = (lambda : pass# WARNING: Decompyle incomplete
)()
_laplace_rule_timescale = (lambda f, t, s:
