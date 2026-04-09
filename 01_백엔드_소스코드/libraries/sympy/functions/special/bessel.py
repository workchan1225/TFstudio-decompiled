# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bessel.pyc (Python 3.11)

from functools import wraps
from sympy.core import S
from sympy.core.add import Add
from sympy.core.cache import cacheit
from sympy.core.expr import Expr
from sympy.core.function import Function, ArgumentIndexError, _mexpand
from sympy.core.logic import fuzzy_or, fuzzy_not
from sympy.core.numbers import Rational, pi, I
from sympy.core.power import Pow
from sympy.core.symbol import Dummy, uniquely_named_symbol, Wild
from sympy.core.sympify import sympify
from sympy.functions.combinatorial.factorials import factorial
from sympy.functions.elementary.trigonometric import sin, cos, csc, cot
from sympy.functions.elementary.integers import ceiling
from sympy.functions.elementary.exponential import exp, log
from sympy.functions.elementary.miscellaneous import cbrt, sqrt, root
from sympy.functions.elementary.complexes import Abs, re, im, polar_lift, unpolarify
from sympy.functions.special.gamma_functions import gamma, digamma, uppergamma
from sympy.functions.special.hyper import hyper
from sympy.polys.orthopolys import spherical_bessel_fn
from mpmath import mp, workprec

class BesselBase(Function):
    """
    Abstract base class for Bessel-type functions.

    This class is meant to reduce code duplication.
    All Bessel-type functions can 1) be differentiated, with the derivatives
    expressed in terms of similar functions, and 2) be rewritten in terms
    of other Bessel-type functions.

    Here, Bessel-type functions are assumed to have one complex parameter.

    To use this base class, define class attributes ``_a`` and ``_b`` such that
    ``2*F_n' = -_a*F_{n+1} + b*F_{n-1}``.

    """
    order = (lambda self: self.args[0])()
    argument = (lambda self: self.args[1])()
    eval = (lambda cls, nu, z: pass)()
    
    def fdiff(self, argindex = (2,)):
        if argindex != 2:
            raise ArgumentIndexError(self, argindex)
        return (self._b / 2) * self.__class__(self.order - 1, self.argument) - (self._a / 2) * self.__class__(self.order + 1, self.argument)

    
    def _eval_conjugate(self):
        z = self.argument
        if z.is_extended_negative is False:
            return self.__class__(self.order.conjugate(), z.conjugate())

    
    def _eval_is_meromorphic(self, x, a):
