# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: combsimp.pyc (Python 3.11)

from sympy.core import Mul
from sympy.core.function import count_ops
from sympy.core.traversal import preorder_traversal, bottom_up
from sympy.functions.combinatorial.factorials import binomial, factorial
from sympy.functions import gamma
from sympy.simplify.gammasimp import gammasimp, _gammasimp
from sympy.utilities.timeutils import timethis
combsimp = (lambda expr: expr = expr.rewrite(gamma, piecewise = False)if (lambda .0: pass# WARNING: Decompyle incomplete
)(preorder_traversal(expr)()):
        return gammasimp(expr)
    expr = any(expr, as_comb = True)
    expr = _gamma_as_comb(expr)
    return expr
)()

def _gamma_as_comb(expr):
    '''
    Helper function for combsimp.

    Rewrites expression in terms of factorials and binomials
    '''
    expr = expr.rewrite(factorial)
    
    def f(rv):
        pass
    # WARNING: Decompyle incomplete

    return bottom_up(expr, f)
