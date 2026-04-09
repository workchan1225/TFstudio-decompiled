# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: basic.pyc (Python 3.11)

'''Base class for all the objects in SymPy'''
from __future__ import annotations
from collections import defaultdict
from collections.abc import Mapping
from itertools import chain, zip_longest
from functools import cmp_to_key
from assumptions import _prepare_class_assumptions
from cache import cacheit
from sympify import _sympify, sympify, SympifyError, _external_converter
from sorting import ordered
from kind import Kind, UndefinedKind
from _print_helpers import Printable
from sympy.utilities.decorator import deprecated
from sympy.utilities.exceptions import sympy_deprecation_warning
from sympy.utilities.iterables import iterable, numbered_symbols
from sympy.utilities.misc import filldedent, func_name
from inspect import getmro

def as_Basic(expr):
    '''Return expr as a Basic instance using strict sympify
    or raise a TypeError; this is just a wrapper to _sympify,
    raising a TypeError instead of a SympifyError.'''
    
    try:
        return _sympify(expr)
    except SympifyError:
        raise TypeError('Argument must be a Basic object, not `%s`' % func_name(expr))


ordering_of_classes = [
    'Zero',
    'One',
    'Half',
    'Infinity',
    'NaN',
    'NegativeOne',
    'NegativeInfinity',
    'Integer',
    'Rational',
    'Float',
    'Exp1',
    'Pi',
    'ImaginaryUnit',
    'Symbol',
    'Wild',
    'Pow',
    'Mul',
    'Add',
    'Derivative',
    'Integral',
    'Abs',
    'Sign',
    'Sqrt',
    'Floor',
    'Ceiling',
    'Re',
    'Im',
    'Arg',
    'Conjugate',
    'Exp',
    'Log',
    'Sin',
    'Cos',
    'Tan',
    'Cot',
    'ASin',
    'ACos',
    'ATan',
    'ACot',
    'Sinh',
    'Cosh',
    'Tanh',
    'Coth',
    'ASinh',
    'ACosh',
    'ATanh',
    'ACoth',
    'RisingFactorial',
    'FallingFactorial',
    'factorial',
    'binomial',
    'Gamma',
    'LowerGamma',
    'UpperGamma',
    'PolyGamma',
    'Erf',
    'Chebyshev',
    'Chebyshev2',
    'Function',
    'WildFunction',
    'Lambda',
    'Order',
    'Equality',
    'Unequality',
    'StrictGreaterThan',
    'StrictLessThan',
    'GreaterThan',
    'LessThan']

def _cmp_name(x = None, y = None):
    '''return -1, 0, 1 if the name of x is before that of y.
    A string comparison is done if either name does not appear
    in `ordering_of_classes`. This is the helper for
    ``Basic.compare``

    Examples
    ========

    >>> from sympy import cos, tan, sin
    >>> from sympy.core import basic
    >>> save = basic.ordering_of_classes
    >>> basic.ordering_of_classes = ()
    >>> basic._cmp_name(cos, tan)
    -1
    >>> basic.ordering_of_classes = ["tan", "sin", "cos"]
    >>> basic._cmp_name(cos, tan)
    1
    >>> basic._cmp_name(sin, cos)
    -1
    >>> basic.ordering_of_classes = save

    '''
    if not issubclass(y, Basic):
        return -1
    n1 = None.__name__
    n2 = y.__name__
    if n1 == n2:
        return 0
    UNKNOWN = None(ordering_of_classes) + 1
    
    try:
        i1 = ordering_of_classes.index(n1)
    except ValueError:
        i1 = UNKNOWN

    
    try:
        i2 = ordering_of_classes.index(n2)
    except ValueError:
        i2 = UNKNOWN

    if i1 == UNKNOWN and i2 == UNKNOWN:
        return (n1 > n2) - (n1 < n2)
    return (None > i2) - (i1 < i2)


class Basic(Printable):
    pass
# WARNING: Decompyle incomplete

_aresame = Basic.is_same
_args_sortkey = cmp_to_key(Basic.compare)
_prepare_class_assumptions(Basic)

class Atom(Basic):
    '''
    A parent class for atomic things. An atom is an expression with no subexpressions.

    Examples
    ========

    Symbol, Number, Rational, Integer, ...
    But not: Add, Mul, Pow, ...
    '''
    is_Atom = True
    __slots__ = ()
    
    def matches(self, expr, repl_dict, old = (None, False)):
        pass
    # WARNING: Decompyle incomplete

    
    def xreplace(self, rule, hack2 = (False,)):
        return rule.get(self, self)

    
    def doit(self, **hints):
        return self

    class_key = (lambda cls: (2, 0, cls.__name__))()
    sort_key = (lambda self, order = (None,): (self.class_key(), (1, (str(self),)), S.One.sort_key(), S.One))()
    
    def _eval_simplify(self, **kwargs):
        return self

    _sorted_args = (lambda self: raise AttributeError('Atoms have no args. It might be necessary to make a check for Atoms in the calling code.'))()


def _atomic(e, recursive = (False,)):
    """Return atom-like quantities as far as substitution is
    concerned: Derivatives, Functions and Symbols. Do not
    return any 'atoms' that are inside such quantities unless
    they also appear outside, too, unless `recursive` is True.

    Examples
    ========

    >>> from sympy import Derivative, Function, cos
    >>> from sympy.abc import x, y
    >>> from sympy.core.basic import _atomic
    >>> f = Function('f')
    >>> _atomic(x + y)
    {x, y}
    >>> _atomic(x + f(y))
    {x, f(y)}
    >>> _atomic(Derivative(f(x), x) + cos(x) + y)
    {y, cos(x), Derivative(f(x), x)}

    """
    pot = _preorder_traversal(e)
    seen = set()
# WARNING: Decompyle incomplete


def _make_find_query(query):
    '''Convert the argument of Basic.find() into a callable'''
    pass
# WARNING: Decompyle incomplete

from singleton import S
from traversal import preorder_traversal as _preorder_traversal, iterargs, iterfreeargs
preorder_traversal = deprecated('\n    Using preorder_traversal from the sympy.core.basic submodule is\n    deprecated.\n\n    Instead, use preorder_traversal from the top-level sympy namespace, like\n\n        sympy.preorder_traversal\n    ', deprecated_since_version = '1.10', active_deprecations_target = 'deprecated-traversal-functions-moved')(_preorder_traversal)
