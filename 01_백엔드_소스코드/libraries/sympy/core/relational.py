# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: relational.pyc (Python 3.11)

from __future__ import annotations
from basic import Atom, Basic
from sorting import ordered
from evalf import EvalfMixin
from function import AppliedUndef
from numbers import int_valued
from singleton import S
from sympify import _sympify, SympifyError
from parameters import global_parameters
from logic import fuzzy_bool, fuzzy_xor, fuzzy_and, fuzzy_not
from sympy.logic.boolalg import Boolean, BooleanAtom
from sympy.utilities.iterables import sift
from sympy.utilities.misc import filldedent
from sympy.utilities.exceptions import sympy_deprecation_warning
__all__ = ('Rel', 'Eq', 'Ne', 'Lt', 'Le', 'Gt', 'Ge', 'Relational', 'Equality', 'Unequality', 'StrictLessThan', 'LessThan', 'StrictGreaterThan', 'GreaterThan')
from expr import Expr
from sympy.multipledispatch import dispatch
from containers import Tuple
from symbol import Symbol

def _nontrivBool(side):
