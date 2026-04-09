# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: delta.pyc (Python 3.11)

'''
This module implements sums and products containing the Kronecker Delta function.

References
==========

.. [1] https://mathworld.wolfram.com/KroneckerDelta.html

'''
from products import product
from summations import Sum, summation
from sympy.core import Add, Mul, S, Dummy
from sympy.core.cache import cacheit
from sympy.core.sorting import default_sort_key
from sympy.functions import KroneckerDelta, Piecewise, piecewise_fold
from sympy.polys.polytools import factor
from sympy.sets.sets import Interval
from sympy.solvers.solvers import solve
_expand_delta = (lambda expr, index: pass# WARNING: Decompyle incomplete
)()
_extract_delta = (lambda expr, index: if not _has_simple_delta(expr, index):
(None, expr)if None(expr, KroneckerDelta):
(expr, S.One)if not None.is_Mul:
raise ValueError('Incorrect expr')delta = Noneterms = []# WARNING: Decompyle incomplete
)()
_has_simple_delta = (lambda expr, index: if expr.has(KroneckerDelta):
if _is_simple_delta(expr, index):
Trueif None.is_Add or expr.is_Mul:
for arg in expr.args:
if _has_simple_delta(arg, index):
TrueFalse)()
_is_simple_delta = (lambda delta, index:
