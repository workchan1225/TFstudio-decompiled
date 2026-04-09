# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: miscellaneous.pyc (Python 3.11)

from sympy.core import Function, S, sympify, NumberKind
from sympy.utilities.iterables import sift
from sympy.core.add import Add
from sympy.core.containers import Tuple
from sympy.core.operations import LatticeOp, ShortCircuit
from sympy.core.function import Application, Lambda, ArgumentIndexError
from sympy.core.expr import Expr
from sympy.core.exprtools import factor_terms
from sympy.core.mod import Mod
from sympy.core.mul import Mul
from sympy.core.numbers import Rational
from sympy.core.power import Pow
from sympy.core.relational import Eq, Relational
from sympy.core.singleton import Singleton
from sympy.core.sorting import ordered
from sympy.core.symbol import Dummy
from sympy.core.rules import Transform
from sympy.core.logic import fuzzy_and, fuzzy_or, _torf
from sympy.core.traversal import walk
from sympy.core.numbers import Integer
from sympy.logic.boolalg import And, Or

def _minmax_as_Piecewise(op, *args):
    pass
# WARNING: Decompyle incomplete


def IdentityFunction():
    '''IdentityFunction'''
    __doc__ = "\n    The identity function\n\n    Examples\n    ========\n\n    >>> from sympy import Id, Symbol\n    >>> x = Symbol('x')\n    >>> Id(x)\n    x\n\n    "
    _symbol = Dummy('x')
    signature = (lambda self: Tuple(self._symbol))()
    expr = (lambda self: self._symbol)()

IdentityFunction = <NODE:27>(IdentityFunction, 'IdentityFunction', Lambda, metaclass = Singleton)
Id = S.IdentityFunction

def sqrt(arg, evaluate = (None,)):
    """Returns the principal square root.

    Parameters
    ==========

    evaluate : bool, optional
        The parameter determines if the expression should be evaluated.
        If ``None``, its value is taken from
        ``global_parameters.evaluate``.

    Examples
    ========

    >>> from sympy import sqrt, Symbol, S
    >>> x = Symbol('x')

    >>> sqrt(x)
    sqrt(x)

    >>> sqrt(x)**2
    x

    Note that sqrt(x**2) does not simplify to x.

    >>> sqrt(x**2)
    sqrt(x**2)

    This is because the two are not equal to each other in general.
    For example, consider x == -1:

    >>> from sympy import Eq
    >>> Eq(sqrt(x**2), x).subs(x, -1)
    False

    This is because sqrt computes the principal square root, so the square may
    put the argument in a different branch.  This identity does hold if x is
    positive:

    >>> y = Symbol('y', positive=True)
    >>> sqrt(y**2)
    y

    You can force this simplification by using the powdenest() function with
    the force option set to True:

    >>> from sympy import powdenest
    >>> sqrt(x**2)
    sqrt(x**2)
    >>> powdenest(sqrt(x**2), force=True)
    x

    To get both branches of the square root you can use the rootof function:

    >>> from sympy import rootof

    >>> [rootof(x**2-3,i) for i in (0,1)]
    [-sqrt(3), sqrt(3)]

    Although ``sqrt`` is printed, there is no ``sqrt`` function so looking for
    ``sqrt`` in an expression will fail:

    >>> from sympy.utilities.misc import func_name
    >>> func_name(sqrt(x))
    'Pow'
    >>> sqrt(x).has(sqrt)
    False

    To find ``sqrt`` look for ``Pow`` with an exponent of ``1/2``:

    >>> (x + 1/sqrt(x)).find(lambda i: i.is_Pow and abs(i.exp) is S.Half)
    {1/sqrt(x)}

    See Also
    ========

    sympy.polys.rootoftools.rootof, root, real_root

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Square_root
    .. [2] https://en.wikipedia.org/wiki/Principal_value
    """
    return Pow(arg, S.Half, evaluate = evaluate)


def cbrt(arg, evaluate = (None,)):
    """Returns the principal cube root.

    Parameters
    ==========

    evaluate : bool, optional
        The parameter determines if the expression should be evaluated.
        If ``None``, its value is taken from
        ``global_parameters.evaluate``.

    Examples
    ========

    >>> from sympy import cbrt, Symbol
    >>> x = Symbol('x')

    >>> cbrt(x)
    x**(1/3)

    >>> cbrt(x)**3
    x

    Note that cbrt(x**3) does not simplify to x.

    >>> cbrt(x**3)
    (x**3)**(1/3)

    This is because the two are not equal to each other in general.
    For example, consider `x == -1`:

    >>> from sympy import Eq
    >>> Eq(cbrt(x**3), x).subs(x, -1)
    False

    This is because cbrt computes the principal cube root, this
    identity does hold if `x` is positive:

    >>> y = Symbol('y', positive=True)
    >>> cbrt(y**3)
    y

    See Also
    ========

    sympy.polys.rootoftools.rootof, root, real_root

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Cube_root
    .. [2] https://en.wikipedia.org/wiki/Principal_value

    """
    return Pow(arg, Rational(1, 3), evaluate = evaluate)


def root(arg, n, k, evaluate = (0, None)):
    '''Returns the *k*-th *n*-th root of ``arg``.

    Parameters
    ==========

    k : int, optional
        Should be an integer in $\\{0, 1, ..., n-1\\}$.
        Defaults to the principal root if $0$.

    evaluate : bool, optional
        The parameter determines if the expression should be evaluated.
        If ``None``, its value is taken from
        ``global_parameters.evaluate``.

    Examples
    ========

    >>> from sympy import root, Rational
    >>> from sympy.abc import x, n

    >>> root(x, 2)
    sqrt(x)

    >>> root(x, 3)
    x**(1/3)

    >>> root(x, n)
    x**(1/n)

    >>> root(x, -Rational(2, 3))
    x**(-3/2)

    To get the k-th n-th root, specify k:

    >>> root(-2, 3, 2)
    -(-1)**(2/3)*2**(1/3)

    To get all n n-th roots you can use the rootof function.
    The following examples show the roots of unity for n
    equal 2, 3 and 4:

    >>> from sympy import rootof

    >>> [rootof(x**2 - 1, i) for i in range(2)]
    [-1, 1]

    >>> [rootof(x**3 - 1,i) for i in range(3)]
    [1, -1/2 - sqrt(3)*I/2, -1/2 + sqrt(3)*I/2]

    >>> [rootof(x**4 - 1,i) for i in range(4)]
    [-1, 1, -I, I]

    SymPy, like other symbolic algebra systems, returns the
    complex root of negative numbers. This is the principal
    root and differs from the text-book result that one might
    be expecting. For example, the cube root of -8 does not
    come back as -2:

    >>> root(-8, 3)
    2*(-1)**(1/3)

    The real_root function can be used to either make the principal
    result real (or simply to return the real root directly):

    >>> from sympy import real_root
    >>> real_root(_)
    -2
    >>> real_root(-32, 5)
    -2

    Alternatively, the n//2-th n-th root of a negative number can be
    computed with root:

    >>> root(-32, 5, 5//2)
    -2

    See Also
    ========

    sympy.polys.rootoftools.rootof
    sympy.core.intfunc.integer_nthroot
    sqrt, real_root

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Square_root
    .. [2] https://en.wikipedia.org/wiki/Real_root
    .. [3] https://en.wikipedia.org/wiki/Root_of_unity
    .. [4] https://en.wikipedia.org/wiki/Principal_value
    .. [5] https://mathworld.wolfram.com/CubeRoot.html

    '''
    n = sympify(n)
    if k:
        return Mul(Pow(arg, S.One / n, evaluate = evaluate), S.NegativeOne ** (2 * k / n), evaluate = evaluate)
    return None(arg, 1 / n, evaluate = evaluate)


def real_root(arg, n, evaluate = (None, None)):
    """Return the real *n*'th-root of *arg* if possible.

    Parameters
    ==========

    n : int or None, optional
        If *n* is ``None``, then all instances of
        $(-n)^{1/\\text{odd}}$ will be changed to $-n^{1/\\text{odd}}$.
        This will only create a real root of a principal root.
        The presence of other factors may cause the result to not be
        real.

    evaluate : bool, optional
        The parameter determines if the expression should be evaluated.
        If ``None``, its value is taken from
        ``global_parameters.evaluate``.

    Examples
    ========

    >>> from sympy import root, real_root

    >>> real_root(-8, 3)
    -2
    >>> root(-8, 3)
    2*(-1)**(1/3)
    >>> real_root(_)
    -2

    If one creates a non-principal root and applies real_root, the
    result will not be real (so use with caution):

    >>> root(-8, 3, 2)
    -2*(-1)**(2/3)
    >>> real_root(_)
    -2*(-1)**(2/3)

    See Also
    ========

    sympy.polys.rootoftools.rootof
    sympy.core.intfunc.integer_nthroot
    root, sqrt
    """
    Abs = Abs
    im = im
    sign = sign
    import sympy.functions.elementary.complexes
    Piecewise = Piecewise
    import sympy.functions.elementary.piecewise
# WARNING: Decompyle incomplete


class MinMaxBase(LatticeOp, Expr):
    
    def __new__(cls, *args, **assumptions):
        global_parameters = global_parameters
        import sympy.core.parameters
        evaluate = assumptions.pop('evaluate', global_parameters.evaluate)
        args = args()
    # WARNING: Decompyle incomplete

    _collapse_arguments = (lambda cls, args: pass# WARNING: Decompyle incomplete
)()
    _new_args_filter = (lambda cls, arg_sequence: pass# WARNING: Decompyle incomplete
)()
    _find_localzeros = (lambda cls, values: localzeros = set()for v in values:
is_newzero = Truelocalzeros_ = list(localzeros)for z in localzeros_:
if id(v) == id(z):
is_newzero = Falsecontinuecon = cls._is_connected(v, z)if con:
is_newzero = Falseif con is True or con == cls:
localzeros.remove(z)localzeros.update([
v])if is_newzero:
localzeros.update([
v])localzeros)()
    _is_connected = (lambda cls, x, y: for i in range(2):
if x == y:
Truef = Mint = Nonefor op in '><':
for j in range(2):
if op == '>':
v = x >= yelse:
v = x <= yexcept TypeError:
Falseif not v.is_Relational:
None, None, None, t if v else ft = Noney = xx = yy = xx = yx = factor_terms(x - y)y = S.ZeroFalse)()
    
    def _eval_derivative(self, s):
        i = 0
        l = []
        for a in self.args:
            i += 1
            da = a.diff(s)
            if da.is_zero:
                continue
            df = self.fdiff(i)
        except ArgumentIndexError:
            df = Function.fdiff(self, i)
        l.append(df * da)
        continue
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_Abs(self, *args, **kwargs):
        Abs = Abs
        import sympy.functions.elementary.complexes
    # WARNING: Decompyle incomplete

    
    def evalf(self, n = (15,), **options):
        pass
    # WARNING: Decompyle incomplete

    
    def n(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    _eval_is_algebraic = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_antihermitian = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_commutative = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_complex = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_composite = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_even = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_finite = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_hermitian = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_imaginary = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_infinite = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_integer = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_irrational = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_negative = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_noninteger = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_nonnegative = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_nonpositive = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_nonzero = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_odd = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_polar = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_positive = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_prime = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_rational = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_real = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_extended_real = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_transcendental = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())

    
    _eval_is_zero = lambda s: (lambda .0: pass# WARNING: Decompyle incomplete
)(s.args())



class Max(Application, MinMaxBase):
    '''
    Return, if possible, the maximum value of the list.

    When number of arguments is equal one, then
    return this argument.

    When number of arguments is equal two, then
    return, if possible, the value from (a, b) that is $\\ge$ the other.

    In common case, when the length of list greater than 2, the task
    is more complicated. Return only the arguments, which are greater
    than others, if it is possible to determine directional relation.

    If is not possible to determine such a relation, return a partially
    evaluated result.

    Assumptions are used to make the decision too.

    Also, only comparable arguments are permitted.

    It is named ``Max`` and not ``max`` to avoid conflicts
    with the built-in function ``max``.


    Examples
    ========

    >>> from sympy import Max, Symbol, oo
    >>> from sympy.abc import x, y, z
    >>> p = Symbol(\'p\', positive=True)
    >>> n = Symbol(\'n\', negative=True)

    >>> Max(x, -2)
    Max(-2, x)
    >>> Max(x, -2).subs(x, 3)
    3
    >>> Max(p, -2)
    p
    >>> Max(x, y)
    Max(x, y)
    >>> Max(x, y) == Max(y, x)
    True
    >>> Max(x, Max(y, z))
    Max(x, y, z)
    >>> Max(n, 8, p, 7, -oo)
    Max(8, p)
    >>> Max (1, x, oo)
    oo

    * Algorithm

    The task can be considered as searching of supremums in the
    directed complete partial orders [1]_.

    The source values are sequentially allocated by the isolated subsets
    in which supremums are searched and result as Max arguments.

    If the resulted supremum is single, then it is returned.

    The isolated subsets are the sets of values which are only the comparable
    with each other in the current set. E.g. natural numbers are comparable with
    each other, but not comparable with the `x` symbol. Another example: the
    symbol `x` with negative assumption is comparable with a natural number.

    Also there are "least" elements, which are comparable with all others,
    and have a zero property (maximum or minimum for all elements).
    For example, in case of $\\infty$, the allocation operation is terminated
    and only this value is returned.

    Assumption:
       - if $A > B > C$ then $A > C$
       - if $A = B$ then $B$ can be removed

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Directed_complete_partial_order
    .. [2] https://en.wikipedia.org/wiki/Lattice_%28order%29

    See Also
    ========

    Min : find minimum values
    '''
    zero = S.Infinity
    identity = S.NegativeInfinity
    
    def fdiff(self, argindex):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_Heaviside(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_Piecewise(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_is_positive(self):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args())

    
    def _eval_is_nonnegative(self):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args())

    
    def _eval_is_negative(self):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args())



class Min(Application, MinMaxBase):
    """
    Return, if possible, the minimum value of the list.
    It is named ``Min`` and not ``min`` to avoid conflicts
    with the built-in function ``min``.

    Examples
    ========

    >>> from sympy import Min, Symbol, oo
    >>> from sympy.abc import x, y
    >>> p = Symbol('p', positive=True)
    >>> n = Symbol('n', negative=True)

    >>> Min(x, -2)
    Min(-2, x)
    >>> Min(x, -2).subs(x, 3)
    -2
    >>> Min(p, -3)
    -3
    >>> Min(x, y)
    Min(x, y)
    >>> Min(n, 8, p, -7, p, oo)
    Min(-7, n)

    See Also
    ========

    Max : find maximum values
    """
    zero = S.NegativeInfinity
    identity = S.Infinity
    
    def fdiff(self, argindex):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_Heaviside(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_Piecewise(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_is_positive(self):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args())

    
    def _eval_is_nonnegative(self):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args())

    
    def _eval_is_negative(self):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args())



class Rem(Function):
    '''Returns the remainder when ``p`` is divided by ``q`` where ``p`` is finite
    and ``q`` is not equal to zero. The result, ``p - int(p/q)*q``, has the same sign
    as the divisor.

    Parameters
    ==========

    p : Expr
        Dividend.

    q : Expr
        Divisor.

    Notes
    =====

    ``Rem`` corresponds to the ``%`` operator in C.

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy import Rem
    >>> Rem(x**3, y)
    Rem(x**3, y)
    >>> Rem(x**3, y).subs({x: -5, y: 3})
    -2

    See Also
    ========

    Mod
    '''
    kind = NumberKind
    eval = (lambda cls, p, q: if q.is_zero:
raise ZeroDivisionError('Division by zero')if p is S.NaN and q is S.NaN and p.is_finite is False or q.is_finite is False:
S.NaNif (None is S.Zero and p in (q, -q) or p.is_integer) and q == 1:
S.Zeroif None.is_Number or p.is_Number:
p - Integer(p / q) * qNone)()
