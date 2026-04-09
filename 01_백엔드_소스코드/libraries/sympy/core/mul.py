# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mul.pyc (Python 3.11)

from typing import Tuple as tTuple
from collections import defaultdict
from functools import reduce
from itertools import product
import operator
from sympify import sympify
from basic import Basic, _args_sortkey
from singleton import S
from operations import AssocOp, AssocOpDispatcher
from cache import cacheit
from intfunc import integer_nthroot, trailing
from logic import fuzzy_not, _fuzzy_group
from expr import Expr
from parameters import global_parameters
from kind import KindDispatcher
from traversal import bottom_up
from sympy.utilities.iterables import sift

class NC_Marker:
    is_Order = False
    is_Mul = False
    is_Number = False
    is_Poly = False
    is_commutative = False


def _mulsort(args):
    args.sort(key = _args_sortkey)


def _unevaluated_Mul(*args):
    '''Return a well-formed unevaluated Mul: Numbers are collected and
    put in slot 0, any arguments that are Muls will be flattened, and args
    are sorted. Use this when args have changed but you still want to return
    an unevaluated Mul.

    Examples
    ========

    >>> from sympy.core.mul import _unevaluated_Mul as uMul
    >>> from sympy import S, sqrt, Mul
    >>> from sympy.abc import x
    >>> a = uMul(*[S(3.0), x, S(2)])
    >>> a.args[0]
    6.00000000000000
    >>> a.args[1]
    x

    Two unevaluated Muls with the same arguments will
    always compare as equal during testing:

    >>> m = uMul(sqrt(2), sqrt(3))
    >>> m == uMul(sqrt(3), sqrt(2))
    True
    >>> u = Mul(sqrt(3), sqrt(2), evaluate=False)
    >>> m == uMul(u)
    True
    >>> m == Mul(*m.args)
    False

    '''
    args = list(args)
    newargs = []
    ncargs = []
    co = S.One
# WARNING: Decompyle incomplete


class Mul(AssocOp, Expr):
    pass
# WARNING: Decompyle incomplete

mul = AssocOpDispatcher('mul')

def prod(a, start = (1,)):
    '''Return product of elements of a. Start with int 1 so if only
       ints are included then an int result is returned.

    Examples
    ========

    >>> from sympy import prod, S
    >>> prod(range(3))
    0
    >>> type(_) is int
    True
    >>> prod([S(2), 3])
    6
    >>> _.is_Integer
    True

    You can start the product at something other than 1:

    >>> prod([1, 2], 3)
    6

    '''
    return reduce(operator.mul, a, start)


def _keep_coeff(coeff, factors, clear, sign = (True, False)):
    '''Return ``coeff*factors`` unevaluated if necessary.

    If ``clear`` is False, do not keep the coefficient as a factor
    if it can be distributed on a single factor such that one or
    more terms will still have integer coefficients.

    If ``sign`` is True, allow a coefficient of -1 to remain factored out.

    Examples
    ========

    >>> from sympy.core.mul import _keep_coeff
    >>> from sympy.abc import x, y
    >>> from sympy import S

    >>> _keep_coeff(S.Half, x + 2)
    (x + 2)/2
    >>> _keep_coeff(S.Half, x + 2, clear=False)
    x/2 + 1
    >>> _keep_coeff(S.Half, (x + 2)*y, clear=False)
    y*(x + 2)/2
    >>> _keep_coeff(S(-1), x + y)
    -x - y
    >>> _keep_coeff(S(-1), x + y, sign=True)
    -(x + y)
    '''
    pass
# WARNING: Decompyle incomplete


def expand_2arg(e):
    
    def do(e):
        pass
    # WARNING: Decompyle incomplete

    return bottom_up(e, do)

from numbers import Rational
from power import Pow
from add import Add, _unevaluated_Add
