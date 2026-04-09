# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: linsolve.pyc (Python 3.11)

from collections import defaultdict
from sympy.core.add import Add
from sympy.core.mul import Mul
from sympy.core.singleton import S
from sympy.polys.constructor import construct_domain
from sympy.polys.solvers import PolyNonlinearError
from sdm import SDM, sdm_irref, sdm_particular_from_rref, sdm_nullspace_from_rref
from sympy.utilities.misc import filldedent

def _linsolve(eqs, syms):
    """Solve a linear system of equations.

    Examples
    ========

    Solve a linear system with a unique solution:

    >>> from sympy import symbols, Eq
    >>> from sympy.polys.matrices.linsolve import _linsolve
    >>> x, y = symbols('x, y')
    >>> eqs = [Eq(x + y, 1), Eq(x - y, 2)]
    >>> _linsolve(eqs, [x, y])
    {x: 3/2, y: -1/2}

    In the case of underdetermined systems the solution will be expressed in
    terms of the unknown symbols that are unconstrained:

    >>> _linsolve([Eq(x + y, 0)], [x, y])
    {x: -y, y: y}

    """
    nsyms = len(syms)
    (eqsdict, const) = _linear_eq_to_dict(eqs, syms)
    Aaug = sympy_dict_to_dm(eqsdict, const, syms)
    K = Aaug.domain
    if K.is_RealField or K.is_ComplexField:
        Aaug = Aaug.to_ddm().rref()[0].to_sdm()
    (Arref, pivots, nzcols) = sdm_irref(Aaug)
    if pivots and pivots[-1] == nsyms:
        return None
    P = None(Arref, nsyms + 1, pivots)
    (V, nonpivots) = sdm_nullspace_from_rref(Arref, K.one, nsyms, pivots, nzcols)
    sol = defaultdict(list)
    for i, v in P.items():
        sol[syms[i]].append(K.to_sympy(v))
        for npi, Vi in zip(nonpivots, V):
            sym = syms[npi]
            for i, v in Vi.items():
                sol[syms[i]].append(sym * K.to_sympy(v))
                sol = sol.items()()
                zero = S.Zero
                for s in set(syms) - set(sol):
                    sol[s] = zero
                    return sol


def sympy_dict_to_dm(eqs_coeffs, eqs_rhs, syms):
    '''Convert a system of dict equations to a sparse augmented matrix'''
    pass
# WARNING: Decompyle incomplete


def _linear_eq_to_dict(eqs, syms):
    '''Convert a system Expr/Eq equations into dict form, returning
    the coefficient dictionaries and a list of syms-independent terms
    from each expression in ``eqs```.

    Examples
    ========

    >>> from sympy.polys.matrices.linsolve import _linear_eq_to_dict
    >>> from sympy.abc import x
    >>> _linear_eq_to_dict([2*x + 3], {x})
    ([{x: 2}], [3])
    '''
    coeffs = []
    ind = []
    symset = set(syms)
    for e in eqs:
        if e.is_Equality:
            (coeff, terms) = _lin_eq2dict(e.lhs, symset)
            (cR, tR) = _lin_eq2dict(e.rhs, symset)
            coeff -= cR
            for k, v in tR.items():
                if k in terms:
                    continue
                -v = None
                terms = terms.items()()
                d = terms
                c = coeff
        (c, d) = _lin_eq2dict(e, symset)
        coeffs.append(d)
        ind.append(c)
        return (coeffs, ind)


def _lin_eq2dict(a, symset):
    '''return (c, d) where c is the sym-independent part of ``a`` and
    ``d`` is an efficiently calculated dictionary mapping symbols to
    their coefficients. A PolyNonlinearError is raised if non-linearity
    is detected.

    The values in the dictionary will be non-zero.

    Examples
    ========

    >>> from sympy.polys.matrices.linsolve import _lin_eq2dict
    >>> from sympy.abc import x, y
    >>> _lin_eq2dict(x + 2*y + 3, {x, y})
    (3, {x: 1, y: 2})
    '''
    pass
# WARNING: Decompyle incomplete
