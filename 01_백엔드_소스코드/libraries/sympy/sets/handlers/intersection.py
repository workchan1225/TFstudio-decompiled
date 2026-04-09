# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: intersection.pyc (Python 3.11)

from sympy.core.basic import _aresame
from sympy.core.function import Lambda, expand_complex
from sympy.core.mul import Mul
from sympy.core.numbers import ilcm, Float
from sympy.core.relational import Eq
from sympy.core.singleton import S
from sympy.core.symbol import Dummy, symbols
from sympy.core.sorting import ordered
from sympy.functions.elementary.complexes import sign
from sympy.functions.elementary.integers import floor, ceiling
from sympy.sets.fancysets import ComplexRegion
from sympy.sets.sets import FiniteSet, Intersection, Interval, Set, Union
from sympy.multipledispatch import Dispatcher
from sympy.sets.conditionset import ConditionSet
from sympy.sets.fancysets import Integers, Naturals, Reals, Range, ImageSet, Rationals
from sympy.sets.sets import EmptySet, UniversalSet, imageset, ProductSet
from sympy.simplify.radsimp import numer
intersection_sets = Dispatcher('intersection_sets')
_ = (lambda a, b: pass)()
_ = (lambda a, b: ConditionSet(a.sym, a.condition, Intersection(a.base_set, b)))()
_ = (lambda a, b: a)()
_ = (lambda a, b: a if a is S.Naturals else b)()
_ = (lambda a, b: intersection_sets(b, a))()
_ = (lambda self, other: pass# WARNING: Decompyle incomplete
)()
_ = (lambda a, b: a)()
_ = (lambda a, b: if not (lambda .0: pass# WARNING: Decompyle incomplete
)(a.args + b.args[:2]()):
        return None
    if all.size == 0:
        return S.EmptySet
    start = None(max(b.inf, a.inf))
    if start not in b:
        start += 1
    end = floor(min(b.sup, a.sup))
    if end not in b:
        end -= 1
    return intersection_sets(a, Range(start, end + 1))
)()
_ = (lambda a, b: intersection_sets(a, Interval(b.inf, S.Infinity)))()
_ = (lambda a, b: pass# WARNING: Decompyle incomplete
)()
_ = (lambda a, b: a)()
_ = (lambda a, b: a)()
_ = (lambda self, other: pass# WARNING: Decompyle incomplete
)()
_ = (lambda a, b: if len(b.args) != len(a.args):
S.EmptySet# WARNING: Decompyle incomplete
)()
_ = (lambda a, b: infty = (S.NegativeInfinity, S.Infinity)# WARNING: Decompyle incomplete
)()
_ = (lambda a, b: S.EmptySet)()
_ = (lambda a, b: b)()
_ = (lambda a, b: pass# WARNING: Decompyle incomplete
)()
_ = (lambda a, b: pass# WARNING: Decompyle incomplete
)()
_ = (lambda a, b: pass)()
_ = (lambda a, b: a)()
_ = (lambda a, b: a)()
_ = (lambda a, b: a)()

def _intlike_interval(a, b):
    
    try:
        if b._inf is S.NegativeInfinity and b._sup is S.Infinity:
            return a
        s = None(max(a.inf, ceiling(b.left)), floor(b.right) + 1)
        return intersection_sets(s, b)
    except ValueError:
        return None


_ = (lambda a, b: _intlike_interval(a, b))()
_ = (lambda a, b: _intlike_interval(a, b))()
