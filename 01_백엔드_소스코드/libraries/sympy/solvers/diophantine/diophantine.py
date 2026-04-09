# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: diophantine.pyc (Python 3.11)

from __future__ import annotations
from sympy.core.add import Add
from sympy.core.assumptions import check_assumptions
from sympy.core.containers import Tuple
from sympy.core.exprtools import factor_terms
from sympy.core.function import _mexpand
from sympy.core.mul import Mul
from sympy.core.numbers import Rational, int_valued
from sympy.core.intfunc import igcdex, ilcm, igcd, integer_nthroot, isqrt
from sympy.core.relational import Eq
from sympy.core.singleton import S
from sympy.core.sorting import default_sort_key, ordered
from sympy.core.symbol import Symbol, symbols
from sympy.core.sympify import _sympify
from sympy.external.gmpy import jacobi, remove, invert, iroot
from sympy.functions.elementary.complexes import sign
from sympy.functions.elementary.integers import floor
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.matrices.dense import MutableDenseMatrix as Matrix
from sympy.ntheory.factor_ import divisors, factorint, perfect_power
from sympy.ntheory.generate import nextprime
from sympy.ntheory.primetest import is_square, isprime
from sympy.ntheory.modular import symmetric_residue
from sympy.ntheory.residue_ntheory import sqrt_mod, sqrt_mod_iter
from sympy.polys.polyerrors import GeneratorsNeeded
from sympy.polys.polytools import Poly, factor_list
from sympy.simplify.simplify import signsimp
from sympy.solvers.solveset import solveset_real
from sympy.utilities import numbered_symbols
from sympy.utilities.misc import as_int, filldedent
from sympy.utilities.iterables import is_sequence, subsets, permute_signs, signed_permutations, ordered_partitions
__all__ = [
    'diophantine',
    'classify_diop']

class DiophantineSolutionSet(set):
    pass
# WARNING: Decompyle incomplete


class DiophantineEquationType:
    '''
    Internal representation of a particular diophantine equation type.

    Parameters
    ==========

    equation :
        The diophantine equation that is being solved.
    free_symbols : list (optional)
        The symbols being solved for.

    Attributes
    ==========

    total_degree :
        The maximum of the degrees of all terms in the equation
    homogeneous :
        Does the equation contain a term of degree 0
    homogeneous_order :
        Does the equation contain any coefficient that is in the symbols being solved for
    dimension :
        The number of symbols being solved for
    '''
    name = None
    
    def __init__(self, equation, free_symbols = (None,)):
        self.equation = _sympify(equation).expand(force = True)
    # WARNING: Decompyle incomplete

    
    def matches(self):
        '''
        Determine whether the given equation can be matched to the particular equation type.
        '''
        return False

    n_parameters = (lambda self: self.dimension)()
    parameters = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def solve(self = None, parameters = property, limit = property):
        raise NotImplementedError('No solver has been written for %s.' % self.name)

    
    def pre_solve(self, parameters = (None,)):
        if not self.matches():
            raise ValueError('This equation does not match the %s equation type.' % self.name)
    # WARNING: Decompyle incomplete



class Univariate(DiophantineEquationType):
    '''
    Representation of a univariate diophantine equation.

    A univariate diophantine equation is an equation of the form
    `a_{0} + a_{1}x + a_{2}x^2 + .. + a_{n}x^n = 0` where `a_{1}, a_{2}, ..a_{n}` are
    integer constants and `x` is an integer variable.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import Univariate
    >>> from sympy.abc import x
    >>> Univariate((x - 2)*(x - 3)**2).solve() # solves equation (x - 2)*(x - 3)**2 == 0
    {(2,), (3,)}

    '''
    name = 'univariate'
    
    def matches(self):
        return self.dimension == 1

    
    def solve(self, parameters, limit = (None, None)):
        self.pre_solve(parameters)
        result = DiophantineSolutionSet(self.free_symbols, parameters = self.parameters)
        for i in solveset_real(self.equation, self.free_symbols[0]).intersect(S.Integers):
            result.add((i,))
            return result



class Linear(DiophantineEquationType):
    '''
    Representation of a linear diophantine equation.

    A linear diophantine equation is an equation of the form `a_{1}x_{1} +
    a_{2}x_{2} + .. + a_{n}x_{n} = 0` where `a_{1}, a_{2}, ..a_{n}` are
    integer constants and `x_{1}, x_{2}, ..x_{n}` are integer variables.

    Examples
    ========

    >>> from sympy.solvers.diophantine.diophantine import Linear
    >>> from sympy.abc import x, y, z
    >>> l1 = Linear(2*x - 3*y - 5)
    >>> l1.matches() # is this equation linear
    True
    >>> l1.solve() # solves equation 2*x - 3*y - 5 == 0
    {(3*t_0 - 5, 2*t_0 - 5)}

    Here x = -3*t_0 - 5 and y = -2*t_0 - 5

    >>> Linear(2*x - 3*y - 4*z -3).solve()
    {(t_0, 2*t_0 + 4*t_1 + 3, -t_0 - 3*t_1 - 3)}

    '''
    name = 'linear'
    
    def matches(self):
        return self.total_degree == 1

    
    def solve(self, parameters, limit = (None, None)):
        pass
    # WARNING: Decompyle incomplete



class BinaryQuadratic(DiophantineEquationType):
    '''
    Representation of a binary quadratic diophantine equation.

    A binary quadratic diophantine equation is an equation of the
    form `Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0`, where `A, B, C, D, E,
    F` are integer constants and `x` and `y` are integer variables.

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy.solvers.diophantine.diophantine import BinaryQuadratic
    >>> b1 = BinaryQuadratic(x**3 + y**2 + 1)
    >>> b1.matches()
    False
    >>> b2 = BinaryQuadratic(x**2 + y**2 + 2*x + 2*y + 2)
    >>> b2.matches()
    True
    >>> b2.solve()
    {(-1, -1)}

    References
    ==========

    .. [1] Methods to solve Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0, [online],
          Available: https://www.alpertron.com.ar/METHODS.HTM
    .. [2] Solving the equation ax^2+ bxy + cy^2 + dx + ey + f= 0, [online],
          Available: https://web.archive.org/web/20160323033111/http://www.jpr2718.org/ax2p.pdf

    '''
    name = 'binary_quadratic'
    
    def matches(self):
