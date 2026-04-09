# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: symbol.pyc (Python 3.11)

from __future__ import annotations
from assumptions import StdFactKB, _assume_defined
from basic import Basic, Atom
from cache import cacheit
from containers import Tuple
from expr import Expr, AtomicExpr
from function import AppliedUndef, FunctionClass
from kind import NumberKind, UndefinedKind
from logic import fuzzy_bool
from singleton import S
from sorting import ordered
from sympify import sympify
from sympy.logic.boolalg import Boolean
from sympy.utilities.iterables import sift, is_sequence
from sympy.utilities.misc import filldedent
import string
import re as _re
import random
from itertools import product
from typing import Any

class Str(Atom):
    '''
    Represents string in SymPy.

    Explanation
    ===========

    Previously, ``Symbol`` was used where string is needed in ``args`` of SymPy
    objects, e.g. denoting the name of the instance. However, since ``Symbol``
    represents mathematical scalar, this class should be used instead.

    '''
    __slots__ = ('name',)
    
    def __new__(cls, name, **kwargs):
        if not isinstance(name, str):
            raise TypeError('name should be a string, not %s' % repr(type(name)))
    # WARNING: Decompyle incomplete

    
    def __getnewargs__(self):
        return (self.name,)

    
    def _hashable_content(self):
        return (self.name,)



def _filter_assumptions(kwargs):
    '''Split the given dict into assumptions and non-assumptions.
    Keys are taken as assumptions if they correspond to an
    entry in ``_assume_defined``.
    '''
    (assumptions, nonassumptions) = map(dict, sift(kwargs.items(), (lambda i: i[0] in _assume_defined), binary = True))
    Symbol._sanitize(assumptions)
    return (assumptions, nonassumptions)


def _symbol(s, matching_symbol = (None,), **assumptions):
    """Return s if s is a Symbol, else if s is a string, return either
    the matching_symbol if the names are the same or else a new symbol
    with the same assumptions as the matching symbol (or the
    assumptions as provided).

    Examples
    ========

    >>> from sympy import Symbol
    >>> from sympy.core.symbol import _symbol
    >>> _symbol('y')
    y
    >>> _.is_real is None
    True
    >>> _symbol('y', real=True).is_real
    True

    >>> x = Symbol('x')
    >>> _symbol(x, real=True)
    x
    >>> _.is_real is None  # ignore attribute if s is a Symbol
    True

    Below, the variable sym has the name 'foo':

    >>> sym = Symbol('foo', real=True)

    Since 'x' is not the same as sym's name, a new symbol is created:

    >>> _symbol('x', sym).name
    'x'

    It will acquire any assumptions give:

    >>> _symbol('x', sym, real=False).is_real
    False

    Since 'foo' is the same as sym's name, sym is returned

    >>> _symbol('foo', sym)
    foo

    Any assumptions given are ignored:

    >>> _symbol('foo', sym, real=False).is_real
    True

    NB: the symbol here may not be the same as a symbol with the same
    name defined elsewhere as a result of different assumptions.

    See Also
    ========

    sympy.core.symbol.Symbol

    """
    pass
# WARNING: Decompyle incomplete


def uniquely_named_symbol(xname, exprs, compare, modify = ((), str, None), **assumptions):
    """
    Return a symbol whose name is derivated from *xname* but is unique
    from any other symbols in *exprs*.

    *xname* and symbol names in *exprs* are passed to *compare* to be
    converted to comparable forms. If ``compare(xname)`` is not unique,
    it is recursively passed to *modify* until unique name is acquired.

    Parameters
    ==========

    xname : str or Symbol
        Base name for the new symbol.

    exprs : Expr or iterable of Expr
        Expressions whose symbols are compared to *xname*.

    compare : function
        Unary function which transforms *xname* and symbol names from
        *exprs* to comparable form.

    modify : function
        Unary function which modifies the string. Default is appending
        the number, or increasing the number if exists.

    Examples
    ========

    By default, a number is appended to *xname* to generate unique name.
    If the number already exists, it is recursively increased.

    >>> from sympy.core.symbol import uniquely_named_symbol, Symbol
    >>> uniquely_named_symbol('x', Symbol('x'))
    x0
    >>> uniquely_named_symbol('x', (Symbol('x'), Symbol('x0')))
    x1
    >>> uniquely_named_symbol('x0', (Symbol('x1'), Symbol('x0')))
    x2

    Name generation can be controlled by passing *modify* parameter.

    >>> from sympy.abc import x
    >>> uniquely_named_symbol('x', x, modify=lambda s: 2*s)
    xx

    """
    pass
# WARNING: Decompyle incomplete

_uniquely_named_symbol = uniquely_named_symbol

class Symbol(Boolean, AtomicExpr):
    '''
    Symbol class is used to create symbolic variables.

    Explanation
    ===========

    Symbolic variables are placeholders for mathematical symbols that can represent numbers, constants, or any other mathematical entities and can be used in mathematical expressions and to perform symbolic computations.

    Assumptions:

    commutative = True
    positive = True
    real = True
    imaginary = True
    complex = True
    complete list of more assumptions- :ref:`predicates`

    You can override the default assumptions in the constructor.

    Examples
    ========

    >>> from sympy import Symbol
    >>> x = Symbol("x", positive=True)
    >>> x.is_positive
    True
    >>> x.is_negative
    False

    passing in greek letters:

    >>> from sympy import Symbol
    >>> alpha = Symbol(\'alpha\')
    >>> alpha #doctest: +SKIP
    α

    Trailing digits are automatically treated like subscripts of what precedes them in the name.
    General format to add subscript to a symbol :
    ``<var_name> = Symbol(\'<symbol_name>_<subscript>\')``

    >>> from sympy import Symbol
    >>> alpha_i = Symbol(\'alpha_i\')
    >>> alpha_i #doctest: +SKIP
    αᵢ

    Parameters
    ==========

    AtomicExpr: variable name
    Boolean: Assumption with a boolean value(True or False)
    '''
    is_comparable = False
    name: 'str' = ('name', '_assumptions_orig', '_assumptions0')
    is_Symbol = True
    is_symbol = True
    kind = (lambda self: if self.is_commutative:
NumberKind)()
    _diff_wrt = (lambda self: True)()
    _sanitize = (lambda assumptions, obj = (None,): is_commutative = fuzzy_bool(assumptions.get('commutative', True))# WARNING: Decompyle incomplete
)()
    
    def _merge(self, assumptions):
        base = self.assumptions0
        for k in set(assumptions) & set(base):
            if assumptions[k] != base[k]:
                raise ValueError(filldedent(f'''\n                    non-matching assumptions for {k!s}: existing value\n                    is {base[k]!s} and new value is {assumptions[k]!s}'''))
            base.update(assumptions)
            return base

    
    def __new__(cls, name, **assumptions):
        '''Symbols are identified by name and assumptions::

        >>> from sympy import Symbol
        >>> Symbol("x") == Symbol("x")
        True
        >>> Symbol("x", real=True) == Symbol("x", real=False)
        False

        '''
        cls._sanitize(assumptions, cls)
    # WARNING: Decompyle incomplete

    __xnew__ = (lambda cls, name: if not isinstance(name, str):
raise TypeError('name should be a string, not %s' % repr(type(name)))assumptions_orig = assumptions.copy()assumptions.setdefault('commutative', True)assumptions_kb = StdFactKB(assumptions)assumptions0 = dict(assumptions_kb)obj = Expr.__new__(cls)obj.name = nameobj._assumptions = assumptions_kbobj._assumptions_orig = assumptions_origobj._assumptions0 = assumptions0obj)()
    __xnew_cached_ = (lambda cls, name: pass# WARNING: Decompyle incomplete
)()()
    
    def __getnewargs_ex__(self):
        return ((self.name,), self._assumptions_orig)

    
    def __setstate__(self, state):
        for name, value in state.items():
            setattr(self, name, value)
            return None

    
    def _hashable_content(self):
        return (self.name,) + tuple(sorted(self.assumptions0.items()))

    
    def _eval_subs(self, old, new):
        if old.is_Pow:
            Pow = Pow
            import sympy.core.power
            return Pow(self, S.One, evaluate = False)._eval_subs(old, new)

    
    def _eval_refine(self, assumptions):
        return self

    assumptions0 = (lambda self: self._assumptions0.copy())()
    sort_key = (lambda self, order = (None,): (self.class_key(), (1, (self.name,)), S.One.sort_key(), S.One))()
    
    def as_dummy(self):
        return Dummy(self.name) if self.is_commutative is not False else Dummy(self.name, commutative = self.is_commutative)

    
    def as_real_imag(self, deep = (True,), **hints):
        if hints.get('ignore') == self:
            return None
        im = im
        re = re
        import sympy.functions.elementary.complexes
        return (re(self), im(self))

    
    def is_constant(self, *wrt, **flags):
        if not wrt:
            return False
        return None not in wrt

    free_symbols = (lambda self: {
self})()
    binary_symbols = free_symbols
    
    def as_set(self):
        return S.UniversalSet



class Dummy(Symbol):
    '''Dummy symbols are each unique, even if they have the same name:

    Examples
    ========

    >>> from sympy import Dummy
    >>> Dummy("x") == Dummy("x")
    False

    If a name is not supplied then a string value of an internal count will be
    used. This is useful when a temporary variable is needed and the name
    of the variable used in the expression is not important.

    >>> Dummy() #doctest: +SKIP
    _Dummy_10

    '''
    _count = 0
    _prng = random.Random()
    _base_dummy_index = _prng.randint(1000000, 9000000)
    __slots__ = ('dummy_index',)
    is_Dummy = True
    
    def __new__(cls, name, dummy_index = (None, None), **assumptions):
        pass
    # WARNING: Decompyle incomplete

    
    def __getnewargs_ex__(self):
        return ((self.name, self.dummy_index), self._assumptions_orig)

    sort_key = (lambda self, order = (None,): (self.class_key(), (2, (self.name, self.dummy_index)), S.One.sort_key(), S.One))()
    
    def _hashable_content(self):
        return Symbol._hashable_content(self) + (self.dummy_index,)



class Wild(Symbol):
    pass
# WARNING: Decompyle incomplete

_range = _re.compile('([0-9]*:[0-9]+|[a-zA-Z]?:[a-zA-Z])')

def symbols(names = None, *, cls, **args):
    """
    Transform strings into instances of :class:`Symbol` class.

    :func:`symbols` function returns a sequence of symbols with names taken
    from ``names`` argument, which can be a comma or whitespace delimited
    string, or a sequence of strings::

        >>> from sympy import symbols, Function

        >>> x, y, z = symbols('x,y,z')
        >>> a, b, c = symbols('a b c')

    The type of output is dependent on the properties of input arguments::

        >>> symbols('x')
        x
        >>> symbols('x,')
        (x,)
        >>> symbols('x,y')
        (x, y)
        >>> symbols(('a', 'b', 'c'))
        (a, b, c)
        >>> symbols(['a', 'b', 'c'])
        [a, b, c]
        >>> symbols({'a', 'b', 'c'})
        {a, b, c}

    If an iterable container is needed for a single symbol, set the ``seq``
    argument to ``True`` or terminate the symbol name with a comma::

        >>> symbols('x', seq=True)
        (x,)

    To reduce typing, range syntax is supported to create indexed symbols.
    Ranges are indicated by a colon and the type of range is determined by
    the character to the right of the colon. If the character is a digit
    then all contiguous digits to the left are taken as the nonnegative
    starting value (or 0 if there is no digit left of the colon) and all
    contiguous digits to the right are taken as 1 greater than the ending
    value::

        >>> symbols('x:10')
        (x0, x1, x2, x3, x4, x5, x6, x7, x8, x9)

        >>> symbols('x5:10')
        (x5, x6, x7, x8, x9)
        >>> symbols('x5(:2)')
        (x50, x51)

        >>> symbols('x5:10,y:5')
        (x5, x6, x7, x8, x9, y0, y1, y2, y3, y4)

        >>> symbols(('x5:10', 'y:5'))
        ((x5, x6, x7, x8, x9), (y0, y1, y2, y3, y4))

    If the character to the right of the colon is a letter, then the single
    letter to the left (or 'a' if there is none) is taken as the start
    and all characters in the lexicographic range *through* the letter to
    the right are used as the range::

        >>> symbols('x:z')
        (x, y, z)
        >>> symbols('x:c')  # null range
        ()
        >>> symbols('x(:c)')
        (xa, xb, xc)

        >>> symbols(':c')
        (a, b, c)

        >>> symbols('a:d, x:z')
        (a, b, c, d, x, y, z)

        >>> symbols(('a:d', 'x:z'))
        ((a, b, c, d), (x, y, z))

    Multiple ranges are supported; contiguous numerical ranges should be
    separated by parentheses to disambiguate the ending number of one
    range from the starting number of the next::

        >>> symbols('x:2(1:3)')
        (x01, x02, x11, x12)
        >>> symbols(':3:2')  # parsing is from left to right
        (00, 01, 10, 11, 20, 21)

    Only one pair of parentheses surrounding ranges are removed, so to
    include parentheses around ranges, double them. And to include spaces,
    commas, or colons, escape them with a backslash::

        >>> symbols('x((a:b))')
        (x(a), x(b))
        >>> symbols(r'x(:1\\,:2)')  # or r'x((:1)\\,(:2))'
        (x(0,0), x(0,1))

    All newly created symbols have assumptions set according to ``args``::

        >>> a = symbols('a', integer=True)
        >>> a.is_integer
        True

        >>> x, y, z = symbols('x,y,z', real=True)
        >>> x.is_real and y.is_real and z.is_real
        True

    Despite its name, :func:`symbols` can create symbol-like objects like
    instances of Function or Wild classes. To achieve this, set ``cls``
    keyword argument to the desired type::

        >>> symbols('f,g,h', cls=Function)
        (f, g, h)

        >>> type(_[0])
        <class 'sympy.core.function.UndefinedFunction'>

    """
    pass
# WARNING: Decompyle incomplete


def var(names, **args):
    """
    Create symbols and inject them into the global namespace.

    Explanation
    ===========

    This calls :func:`symbols` with the same arguments and puts the results
    into the *global* namespace. It's recommended not to use :func:`var` in
    library code, where :func:`symbols` has to be used::

    Examples
    ========

    >>> from sympy import var

    >>> var('x')
    x
    >>> x # noqa: F821
    x

    >>> var('a,ab,abc')
    (a, ab, abc)
    >>> abc # noqa: F821
    abc

    >>> var('x,y', real=True)
    (x, y)
    >>> x.is_real and y.is_real # noqa: F821
    True

    See :func:`symbols` documentation for more details on what kinds of
    arguments can be passed to :func:`var`.

    """
    pass
# WARNING: Decompyle incomplete


def disambiguate(*iter):
    """
    Return a Tuple containing the passed expressions with symbols
    that appear the same when printed replaced with numerically
    subscripted symbols, and all Dummy symbols replaced with Symbols.

    Parameters
    ==========

    iter: list of symbols or expressions.

    Examples
    ========

    >>> from sympy.core.symbol import disambiguate
    >>> from sympy import Dummy, Symbol, Tuple
    >>> from sympy.abc import y

    >>> tup = Symbol('_x'), Dummy('x'), Dummy('x')
    >>> disambiguate(*tup)
    (x_2, x, x_1)

    >>> eqs = Tuple(Symbol('x')/y, Dummy('x')/y)
    >>> disambiguate(*eqs)
    (x_1/y, x/y)

    >>> ix = Symbol('x', integer=True)
    >>> vx = Symbol('x')
    >>> disambiguate(vx + ix)
    (x + x_1,)

    To make your own mapping of symbols to use, pass only the free symbols
    of the expressions and create a dictionary:

    >>> free = eqs.free_symbols
    >>> mapping = dict(zip(free, disambiguate(*free)))
    >>> eqs.xreplace(mapping)
    (x_1/y, x/y)

    """
    pass
# WARNING: Decompyle incomplete
