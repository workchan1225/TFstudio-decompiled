# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exponential.pyc (Python 3.11)

from itertools import product
from typing import Tuple as tTuple
from sympy.core.add import Add
from sympy.core.cache import cacheit
from sympy.core.expr import Expr
from sympy.core.function import Function, ArgumentIndexError, expand_log, expand_mul, FunctionClass, PoleError, expand_multinomial, expand_complex
from sympy.core.logic import fuzzy_and, fuzzy_not, fuzzy_or
from sympy.core.mul import Mul
from sympy.core.numbers import Integer, Rational, pi, I
from sympy.core.parameters import global_parameters
from sympy.core.power import Pow
from sympy.core.relational import Ge
from sympy.core.singleton import S
from sympy.core.symbol import Wild, Dummy
from sympy.core.sympify import sympify
from sympy.functions.combinatorial.factorials import factorial
from sympy.functions.elementary.complexes import arg, unpolarify, im, re, Abs
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.ntheory import multiplicity, perfect_power
from sympy.ntheory.factor_ import factorint

class ExpBase(Function):
    unbranched = True
    _singularities = (S.ComplexInfinity,)
    kind = (lambda self: self.exp.kind)()
    
    def inverse(self, argindex = (1,)):
        '''
        Returns the inverse function of ``exp(x)``.
        '''
        return log

    
    def as_numer_denom(self):
        '''
        Returns this with a positive exponent as a 2-tuple (a fraction).

        Examples
        ========

        >>> from sympy import exp
        >>> from sympy.abc import x
        >>> exp(-x).as_numer_denom()
        (1, exp(x))
        >>> exp(x).as_numer_denom()
        (exp(x), 1)
        '''
        if not self.is_commutative:
            return (self, S.One)
        exp = None.exp
        neg_exp = exp.is_negative
        if not neg_exp and -exp.is_negative:
            neg_exp = exp.could_extract_minus_sign()
        if neg_exp:
            return (S.One, self.func(-exp))
        return (None, S.One)

    exp = (lambda self: self.args[0])()
    
    def as_base_exp(self):
        '''
        Returns the 2-tuple (base, exponent).
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_adjoint(self):
        return self.func(self.exp.adjoint())

    
    def _eval_conjugate(self):
        return self.func(self.exp.conjugate())

    
    def _eval_transpose(self):
        return self.func(self.exp.transpose())

    
    def _eval_is_finite(self):
