# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: wrapper.pyc (Python 3.11)

"""
Functions and wrapper object to call assumption property and predicate
query with same syntax.

In SymPy, there are two assumption systems. Old assumption system is
defined in sympy/core/assumptions, and it can be accessed by attribute
such as ``x.is_even``. New assumption system is defined in
sympy/assumptions, and it can be accessed by predicates such as
``Q.even(x)``.

Old assumption is fast, while new assumptions can freely take local facts.
In general, old assumption is used in evaluation method and new assumption
is used in refinement method.

In most cases, both evaluation and refinement follow the same process, and
the only difference is which assumption system is used. This module provides
``is_[...]()`` functions and ``AssumptionsWrapper()`` class which allows
using two systems with same syntax so that parallel code implementation can be
avoided.

Examples
========

For multiple use, use ``AssumptionsWrapper()``.

>>> from sympy import Q, Symbol
>>> from sympy.assumptions.wrapper import AssumptionsWrapper
>>> x = Symbol('x')
>>> _x = AssumptionsWrapper(x, Q.even(x))
>>> _x.is_integer
True
>>> _x.is_odd
False

For single use, use ``is_[...]()`` functions.

>>> from sympy.assumptions.wrapper import is_infinite
>>> a = Symbol('a')
>>> print(is_infinite(a))
None
>>> is_infinite(a, Q.finite(a))
False

"""
from sympy.assumptions import ask, Q
from sympy.core.basic import Basic
from sympy.core.sympify import _sympify

def make_eval_method(fact):
    pass
# WARNING: Decompyle incomplete


class AssumptionsWrapper(Basic):
    pass
# WARNING: Decompyle incomplete


def is_infinite(obj, assumptions = (None,)):
    pass
# WARNING: Decompyle incomplete


def is_extended_real(obj, assumptions = (None,)):
    pass
# WARNING: Decompyle incomplete


def is_extended_nonnegative(obj, assumptions = (None,)):
    pass
# WARNING: Decompyle incomplete
