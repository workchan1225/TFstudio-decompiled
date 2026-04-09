# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: issubset.pyc (Python 3.11)

from sympy.core.singleton import S
from sympy.core.symbol import Symbol
from sympy.core.logic import fuzzy_and, fuzzy_bool, fuzzy_not, fuzzy_or
from sympy.core.relational import Eq
from sympy.sets.sets import FiniteSet, Interval, Set, Union, ProductSet
from sympy.sets.fancysets import Complexes, Reals, Range, Rationals
from sympy.multipledispatch import Dispatcher
_inf_sets = [
    S.Naturals,
    S.Naturals0,
    S.Integers,
    S.Rationals,
    S.Reals,
    S.Complexes]
is_subset_sets = Dispatcher('is_subset_sets')
_ = (lambda a, b: pass)()
_ = (lambda a, b: if fuzzy_bool(a.start < b.start):
Falseif None(a.end > b.end):
Falseif None.left_open and a.left_open and fuzzy_bool(Eq(a.start, b.start)):
Falseif None.right_open or a.right_open or fuzzy_bool(Eq(a.end, b.end)):
FalseNoneNone)()
_ = (lambda a_interval, b_fs: if fuzzy_not(a_interval.measure.is_zero):
False)()
_ = (lambda a_interval, b_u: pass# WARNING: Decompyle incomplete
)()
_ = (lambda a, b: if  == a.step, b.step or a.step, b.step == 1:
passelse:
NoneNone([
fuzzy_bool(a.start >= b.start),
fuzzy_bool(a.stop <= b.stop)]))()
_ = (lambda a_range, b_interval: if a_range.step.is_positive:
if b_interval.left_open and a_range.inf.is_finite:
cond_left = a_range.inf > b_interval.leftelse:
cond_left = a_range.inf >= b_interval.leftif b_interval.right_open and a_range.sup.is_finite:
cond_right = a_range.sup < b_interval.rightelse:
cond_right = a_range.sup <= b_interval.rightfuzzy_and([
cond_left,
cond_right]))()
_ = (lambda a_range, b_finiteset: pass# WARNING: Decompyle incomplete
)()
_ = (lambda a_interval, b_range: if a_interval.measure.is_extended_nonzero:
False)()
_ = (lambda a_interval, b_rationals: if a_interval.measure.is_extended_nonzero:
False)()
_ = (lambda a, b: True)()
_ = (lambda a, b: False)()
_ = (lambda a, b: False)()
_ = (lambda a, b: False)()
_ = (lambda a, b: True)()
_ = (lambda a, b: False)()
_ = (lambda a_ps, b_fs: pass# WARNING: Decompyle incomplete
)()
