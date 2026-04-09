# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: limits.pyc (Python 3.11)

from sympy.calculus.accumulationbounds import AccumBounds
from sympy.core import S, Symbol, Add, sympify, Expr, PoleError, Mul
from sympy.core.exprtools import factor_terms
from sympy.core.numbers import Float, _illegal
from sympy.functions.combinatorial.factorials import factorial
from sympy.functions.elementary.complexes import Abs, sign, arg, re
from sympy.functions.elementary.exponential import exp, log
from sympy.functions.special.gamma_functions import gamma
from sympy.polys import PolynomialError, factor
from sympy.series.order import Order
from gruntz import gruntz

def limit(e, z, z0, dir = ('+',)):
    '''Computes the limit of ``e(z)`` at the point ``z0``.

    Parameters
    ==========

    e : expression, the limit of which is to be taken

    z : symbol representing the variable in the limit.
        Other symbols are treated as constants. Multivariate limits
        are not supported.

    z0 : the value toward which ``z`` tends. Can be any expression,
        including ``oo`` and ``-oo``.

    dir : string, optional (default: "+")
        The limit is bi-directional if ``dir="+-"``, from the right
        (z->z0+) if ``dir="+"``, and from the left (z->z0-) if
        ``dir="-"``. For infinite ``z0`` (``oo`` or ``-oo``), the ``dir``
        argument is determined from the direction of the infinity
        (i.e., ``dir="-"`` for ``oo``).

    Examples
    ========

    >>> from sympy import limit, sin, oo
    >>> from sympy.abc import x
    >>> limit(sin(x)/x, x, 0)
    1
    >>> limit(1/x, x, 0) # default dir=\'+\'
    oo
    >>> limit(1/x, x, 0, dir="-")
    -oo
    >>> limit(1/x, x, 0, dir=\'+-\')
    zoo
    >>> limit(1/x, x, oo)
    0

    Notes
    =====

    First we try some heuristics for easy and frequent cases like "x", "1/x",
    "x**2" and similar, so that it\'s fast. For all other cases, we use the
    Gruntz algorithm (see the gruntz() function).

    See Also
    ========

     limit_seq : returns the limit of a sequence.
    '''
    return Limit(e, z, z0, dir).doit(deep = False)


def heuristics(e, z, z0, dir):
    '''Computes the limit of an expression term-wise.
    Parameters are the same as for the ``limit`` function.
    Works with the arguments of expression ``e`` one by one, computing
    the limit of each and then combining the results. This approach
    works only for simple limits, but it is fast.
    '''
    rv = None
    if z0 is S.Infinity:
        rv = limit(e.subs(z, 1 / z), z, S.Zero, '+')
        if isinstance(rv, Limit):
            return None
# WARNING: Decompyle incomplete


class Limit(Expr):
    '''Represents an unevaluated limit.

    Examples
    ========

    >>> from sympy import Limit, sin
    >>> from sympy.abc import x
    >>> Limit(sin(x)/x, x, 0)
    Limit(sin(x)/x, x, 0, dir=\'+\')
    >>> Limit(1/x, x, 0, dir="-")
    Limit(1/x, x, 0, dir=\'-\')

    '''
    
    def __new__(cls, e, z, z0, dir = ('+',)):
        e = sympify(e)
        z = sympify(z)
        z0 = sympify(z0)
        if z0 in (S.Infinity, S.ImaginaryUnit * S.Infinity):
            dir = '-'
        elif z0 in (S.NegativeInfinity, S.ImaginaryUnit * S.NegativeInfinity):
            dir = '+'
        if z0.has(z):
            raise NotImplementedError(f'''Limits approaching a variable point are not supported ({z!s} -> {z0!s})''')
        if isinstance(dir, str):
            dir = Symbol(dir)
        elif not isinstance(dir, Symbol):
            raise TypeError('direction must be of type basestring or Symbol, not %s' % type(dir))
        if str(dir) not in ('+', '-', '+-'):
            raise ValueError("direction must be one of '+', '-' or '+-', not %s" % dir)
        obj = Expr.__new__(cls)
        obj._args = (e, z, z0, dir)
        return obj

    free_symbols = (lambda self: e = self.args[0]isyms = e.free_symbolsisyms.difference_update(self.args[1].free_symbols)isyms.update(self.args[2].free_symbols)isyms)()
    
    def pow_heuristics(self, e):
        (_, z, z0, _) = self.args
        e1 = e.exp
        b1 = e.base
        if not b1.has(z):
            res = limit(e1 * log(b1), z, z0)
            return exp(res)
        ex_lim = None(e1, z, z0)
        base_lim = limit(b1, z, z0)
        if base_lim is S.One and ex_lim in (S.Infinity, S.NegativeInfinity):
            res = limit(e1 * (b1 - 1), z, z0)
            return exp(res)
        if None is S.NegativeInfinity or ex_lim is S.Infinity:
            return S.ComplexInfinity
        return None

    
    def doit(self, **hints):
        '''Evaluates the limit.

        Parameters
        ==========

        deep : bool, optional (default: True)
            Invoke the ``doit`` method of the expressions involved before
            taking the limit.

        hints : optional keyword arguments
            To be passed to ``doit`` methods; only used if deep is True.
        '''
        pass
    # WARNING: Decompyle incomplete
