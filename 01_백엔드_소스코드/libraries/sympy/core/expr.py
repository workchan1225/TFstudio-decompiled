# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: expr.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING
from collections.abc import Iterable
from functools import reduce
import re
from sympify import sympify, _sympify
from basic import Basic, Atom
from singleton import S
from evalf import EvalfMixin, pure_complex, DEFAULT_MAXPREC
from decorators import call_highest_priority, sympify_method_args, sympify_return
from cache import cacheit
from intfunc import mod_inverse
from sorting import default_sort_key
from kind import NumberKind
from sympy.utilities.exceptions import sympy_deprecation_warning
from sympy.utilities.misc import as_int, func_name, filldedent
from sympy.utilities.iterables import has_variety, sift
from mpmath.libmp import mpf_log, prec_to_dps
from mpmath.libmp.libintmath import giant_steps
if TYPE_CHECKING:
    from numbers import Number
from collections import defaultdict

def _corem(eq, c):
    co = []
    non = []
# WARNING: Decompyle incomplete

Expr = <NODE:12>()

class AtomicExpr(Expr, Atom):
    pass
# WARNING: Decompyle incomplete


def _mag(x):
    '''Return integer $i$ such that $0.1 \\le x/10^i < 1$

    Examples
    ========

    >>> from sympy.core.expr import _mag
    >>> from sympy import Float
    >>> _mag(Float(.1))
    0
    >>> _mag(Float(.01))
    -1
    >>> _mag(Float(1234))
    4
    '''
    log10 = log10
    ceil = ceil
    log = log
    import math
    xpos = abs(x.n())
    if not xpos:
        return S.Zero
    
    try:
        mag_first_dig = int(ceil(log10(xpos)))
    except (ValueError, OverflowError):
        mag_first_dig = int(ceil(Float(mpf_log(xpos._mpf_, 53)) / log(10)))

# WARNING: Decompyle incomplete


class UnevaluatedExpr(Expr):
    '''
    Expression that is not evaluated unless released.

    Examples
    ========

    >>> from sympy import UnevaluatedExpr
    >>> from sympy.abc import x
    >>> x*(1/x)
    1
    >>> x*UnevaluatedExpr(1/x)
    x*1/x

    '''
    
    def __new__(cls, arg, **kwargs):
        arg = _sympify(arg)
    # WARNING: Decompyle incomplete

    
    def doit(self, **hints):
        pass
    # WARNING: Decompyle incomplete



def unchanged(func, *args):
    """Return True if `func` applied to the `args` is unchanged.
    Can be used instead of `assert foo == foo`.

    Examples
    ========

    >>> from sympy import Piecewise, cos, pi
    >>> from sympy.core.expr import unchanged
    >>> from sympy.abc import x

    >>> unchanged(cos, 1)  # instead of assert cos(1) == cos(1)
    True

    >>> unchanged(cos, pi)
    False

    Comparison of args uses the builtin capabilities of the object's
    arguments to test for equality so args can be defined loosely. Here,
    the ExprCondPair arguments of Piecewise compare as equal to the
    tuples that can be used to create the Piecewise:

    >>> unchanged(Piecewise, (x, x > 1), (0, True))
    True
    """
    pass
# WARNING: Decompyle incomplete


class ExprBuilder:
    
    def __init__(self, op, args, validator, check = (None, None, True)):
        if not hasattr(op, '__call__'):
            raise TypeError('op {} needs to be callable'.format(op))
        self.op = op
    # WARNING: Decompyle incomplete

    _build_args = (lambda args: args())()
    
    def validate(self):
        pass
    # WARNING: Decompyle incomplete

    
    def build(self, check = (True,)):
        args = self._build_args(self.args)
    # WARNING: Decompyle incomplete

    
    def append_argument(self, arg, check = (True,)):
        self.args.append(arg)
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, item):
        if item == 0:
            return self.op
        return None.args[item - 1]

    
    def __repr__(self):
        return str(self.build())

    
    def search_element(self, elem):
        pass
    # WARNING: Decompyle incomplete


from mul import Mul
from add import Add
from power import Pow
from function import Function, _derivative_dispatch
from mod import Mod
from exprtools import factor_terms
from numbers import Float, Integer, Rational, _illegal, int_valued
