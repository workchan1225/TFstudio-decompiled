# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: basisdependent.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING
from sympy.simplify import simplify as simp, trigsimp as tsimp
from sympy.core.decorators import call_highest_priority, _sympifyit
from sympy.core.assumptions import StdFactKB
from sympy.core.function import diff as df
from sympy.integrals.integrals import Integral
from sympy.polys.polytools import factor as fctr
from sympy.core import S, Add, Mul
from sympy.core.expr import Expr
if TYPE_CHECKING:
    from sympy.vector.vector import BaseVector

class BasisDependent(Expr):
    zero: 'BasisDependentZero' = '\n    Super class containing functionality common to vectors and\n    dyadics.\n    Named so because the representation of these quantities in\n    sympy.vector is dependent on the basis they are expressed in.\n    '
    __add__ = (lambda self, other: self._add_func(self, other))()
    __radd__ = (lambda self, other: self._add_func(other, self))()
    __sub__ = (lambda self, other: self._add_func(self, -other))()
    __rsub__ = (lambda self, other: self._add_func(other, -self))()
    __mul__ = (lambda self, other: self._mul_func(self, other))()()
    __rmul__ = (lambda self, other: self._mul_func(other, self))()()
    
    def __neg__(self):
        return self._mul_func(S.NegativeOne, self)

    __truediv__ = (lambda self, other: self._div_helper(other))()()
    __rtruediv__ = (lambda self, other: TypeError('Invalid divisor for division'))()
    
    def evalf(self, n, subs, maxn, chop, strict, quad, verbose = (15, None, 100, False, False, None, False)):
        """
        Implements the SymPy evalf routine for this quantity.

        evalf's documentation
        =====================

        """
        options = {
            'subs': subs,
            'maxn': maxn,
            'chop': chop,
            'strict': strict,
            'quad': quad,
            'verbose': verbose }
        vec = self.zero
    # WARNING: Decompyle incomplete

    evalf = evalf, evalf.__doc__ += Expr.evalf.__doc__, .__doc__
    
    def simplify(self, **kwargs):
        """
        Implements the SymPy simplify routine for this quantity.

        simplify's documentation
        ========================

        """
        pass
    # WARNING: Decompyle incomplete

    (lambda self: pass# WARNING: Decompyle incomplete
) = simplify, simplify.__doc__ += simp.__doc__, .__doc__
    (lambda self: pass# WARNING: Decompyle incomplete
) = trigsimp, trigsimp.__doc__ += tsimp.__doc__, .__doc__
    
    def _eval_trigsimp(self, **opts):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_derivative(self, wrt):
        return self.diff(wrt)

    
    def _eval_Integral(self, *symbols, **assumptions):
        pass
    # WARNING: Decompyle incomplete

    
    def as_numer_denom(self):
        '''
        Returns the expression as a tuple wrt the following
        transformation -

        expression -> a/b -> a, b

        '''
        return (self, S.One)

    
    def factor(self, *args, **kwargs):
        """
        Implements the SymPy factor routine, on the scalar parts
        of a basis-dependent expression.

        factor's documentation
        ========================

        """
        pass
    # WARNING: Decompyle incomplete

    (lambda self, rational = (False,): (S.One, self)) = factor, factor.__doc__ += fctr.__doc__, .__doc__
    
    def as_coeff_add(self, *deps):
        '''Efficiently extract the coefficient of a summation.'''
        pass
    # WARNING: Decompyle incomplete

    
    def diff(self, *args, **kwargs):
        """
        Implements the SymPy diff routine, for vectors.

        diff's documentation
        ========================

        """
        pass
    # WARNING: Decompyle incomplete

    (lambda self: pass# WARNING: Decompyle incomplete
) = diff, diff.__doc__ += df.__doc__, .__doc__


class BasisDependentAdd(Add, BasisDependent):
    pass
# WARNING: Decompyle incomplete


class BasisDependentMul(Mul, BasisDependent):
    pass
# WARNING: Decompyle incomplete


class BasisDependentZero(BasisDependent):
    pass
# WARNING: Decompyle incomplete
