# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: add.pyc (Python 3.11)

from typing import Tuple as tTuple
from collections import defaultdict
from functools import reduce
from operator import attrgetter
from basic import _args_sortkey
from parameters import global_parameters
from logic import _fuzzy_group, fuzzy_or, fuzzy_not
from singleton import S
from operations import AssocOp, AssocOpDispatcher
from cache import cacheit
from numbers import equal_valued
from intfunc import ilcm, igcd
from expr import Expr
from kind import UndefinedKind
from sympy.utilities.iterables import is_sequence, sift

def _could_extract_minus_sign(expr):
    negative_args = (lambda .0: pass# WARNING: Decompyle incomplete
)(expr.args())
    positive_args = len(expr.args) - negative_args
    if positive_args > negative_args:
        return False
    if sum < negative_args:
        return True
    return None(expr.sort_key() < -expr.sort_key())


def _addsort(args):
    args.sort(key = _args_sortkey)


def _unevaluated_Add(*args):
    '''Return a well-formed unevaluated Add: Numbers are collected and
    put in slot 0 and args are sorted. Use this when args have changed
    but you still want to return an unevaluated Add.

    Examples
    ========

    >>> from sympy.core.add import _unevaluated_Add as uAdd
    >>> from sympy import S, Add
    >>> from sympy.abc import x, y
    >>> a = uAdd(*[S(1.0), x, S(2)])
    >>> a.args[0]
    3.00000000000000
    >>> a.args[1]
    x

    Beyond the Number being in slot 0, there is no other assurance of
    order for the arguments since they are hash sorted. So, for testing
    purposes, output produced by this in some other function can only
    be tested against the output of this function or as one of several
    options:

    >>> opts = (Add(x, y, evaluate=False), Add(y, x, evaluate=False))
    >>> a = uAdd(x, y)
    >>> assert a in opts and a == uAdd(x, y)
    >>> uAdd(x + 1, x + 2)
    x + x + 3
    '''
    args = list(args)
    newargs = []
    co = S.Zero
# WARNING: Decompyle incomplete


class Add(AssocOp, Expr):
    pass
# WARNING: Decompyle incomplete

add = AssocOpDispatcher('add')
from mul import Mul, _keep_coeff, _unevaluated_Mul
from numbers import Rational
