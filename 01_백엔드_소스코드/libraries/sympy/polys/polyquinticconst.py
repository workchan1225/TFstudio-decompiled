# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: polyquinticconst.pyc (Python 3.11)

"""
Solving solvable quintics - An implementation of DS Dummit's paper

Paper :
https://www.ams.org/journals/mcom/1991-57-195/S0025-5718-1991-1079014-X/S0025-5718-1991-1079014-X.pdf

Mathematica notebook:
http://www.emba.uvm.edu/~ddummit/quintics/quintics.nb

"""
from sympy.core import Symbol
from sympy.core.evalf import N
from sympy.core.numbers import I, Rational
from sympy.functions import sqrt
from sympy.polys.polytools import Poly
from sympy.utilities import public
x = Symbol('x')
PolyQuintic = <NODE:12>()
