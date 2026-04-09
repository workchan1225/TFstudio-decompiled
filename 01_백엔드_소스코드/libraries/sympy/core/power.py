# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: power.pyc (Python 3.11)

from __future__ import annotations
from typing import Callable
from itertools import product
from sympify import _sympify
from cache import cacheit
from singleton import S
from expr import Expr
from evalf import PrecisionExhausted
from function import expand_complex, expand_multinomial, expand_mul, _mexpand, PoleError
from logic import fuzzy_bool, fuzzy_not, fuzzy_and, fuzzy_or
from parameters import global_parameters
from relational import is_gt, is_lt
from kind import NumberKind, UndefinedKind
from sympy.utilities.iterables import sift
from sympy.utilities.exceptions import sympy_deprecation_warning
from sympy.utilities.misc import as_int
from sympy.multipledispatch import Dispatcher

class Pow(Expr):
    pass
# WARNING: Decompyle incomplete

power = Dispatcher('power')
power.add((object, object), Pow)
from add import Add
from numbers import Integer, Rational
from mul import Mul, _keep_coeff
from symbol import Symbol, Dummy, symbols
