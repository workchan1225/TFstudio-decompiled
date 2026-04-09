# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: residues.pyc (Python 3.11)

'''
This module implements the Residue function and related tools for working
with residues.
'''
from sympy.core.mul import Mul
from sympy.core.singleton import S
from sympy.core.sympify import sympify
from sympy.utilities.timeutils import timethis
residue = (lambda expr, x, x0: Order = Orderimport sympy.series.ordercollect = collectimport sympy.simplify.radsimpexpr = sympify(expr)if x0 != 0:
expr = expr.subs(x, x + x0)for n in (0, 1, 2, 4, 8, 16, 32):
s = expr.nseries(x, n = n)if s.has(Order) or s.getn() >= 0:
passs = collect(s.removeO(), x)if s.is_Add:
args = s.argselse:
args = [
s]res = S.Zero# WARNING: Decompyle incomplete
)()
