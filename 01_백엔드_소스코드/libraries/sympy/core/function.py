# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: function.pyc (Python 3.11)

'''
There are three types of functions implemented in SymPy:

    1) defined functions (in the sense that they can be evaluated) like
       exp or sin; they have a name and a body:
           f = exp
    2) undefined function which have a name but no body. Undefined
       functions can be defined using a Function class as follows:
           f = Function(\'f\')
       (the result will be a Function instance)
    3) anonymous function (or lambda function) which have a body (defined
       with dummy variables) but have no name:
           f = Lambda(x, exp(x)*x)
           f = Lambda((x, y), exp(x)*y)
    The fourth type of functions are composites, like (sin + cos)(x); these work in
    SymPy core, but are not yet part of SymPy.

    Examples
    ========

    >>> import sympy
    >>> f = sympy.Function("f")
    >>> from sympy.abc import x
    >>> f(x)
    f(x)
    >>> print(sympy.srepr(f(x).func))
    Function(\'f\')
    >>> f(x).args
    (x,)

'''
from __future__ import annotations
from typing import Any
from collections.abc import Iterable
from add import Add
from basic import Basic, _atomic
from cache import cacheit
from containers import Tuple, Dict
from decorators import _sympifyit
from evalf import pure_complex
from expr import Expr, AtomicExpr
from logic import fuzzy_and, fuzzy_or, fuzzy_not, FuzzyBool
from mul import Mul
from numbers import Rational, Float, Integer
from operations import LatticeOp
from parameters import global_parameters
from rules import Transform
from singleton import S
from sympify import sympify, _sympify
from sorting import default_sort_key, ordered
from sympy.utilities.exceptions import sympy_deprecation_warning, SymPyDeprecationWarning, ignore_warnings
from sympy.utilities.iterables import has_dups, sift, iterable, is_sequence, uniq, topological_sort
from sympy.utilities.lambdify import MPMATH_TRANSLATIONS
from sympy.utilities.misc import as_int, filldedent, func_name
import mpmath
from mpmath.libmp.libmpf import prec_to_dps
import inspect
from collections import Counter

def _coeff_isneg(a):
