# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utilities.pyc (Python 3.11)

'''Utilities for algebraic number theory. '''
from sympy.core.sympify import sympify
from sympy.ntheory.factor_ import factorint
from sympy.polys.domains.rationalfield import QQ
from sympy.polys.domains.integerring import ZZ
from sympy.polys.matrices.exceptions import DMRankError
from sympy.polys.numberfields.minpoly import minpoly
from sympy.printing.lambdarepr import IntervalPrinter
from sympy.utilities.decorator import public
from sympy.utilities.lambdify import lambdify
from mpmath import mp

def is_rat(c):
