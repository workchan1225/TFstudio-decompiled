# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: partfrac.pyc (Python 3.11)

'''Algorithms for partial fraction decomposition of rational functions. '''
from sympy.core import S, Add, sympify, Function, Lambda, Dummy
from sympy.core.traversal import preorder_traversal
from sympy.polys import Poly, RootSum, cancel, factor
from sympy.polys.polyerrors import PolynomialError
from sympy.polys.polyoptions import allowed_flags, set_defaults
from sympy.polys.polytools import parallel_poly_from_expr
from sympy.utilities import numbered_symbols, take, xthreaded, public
apart = (lambda f, x, full = (None, False): allowed_flags(options, [])f = sympify(f)if f.is_Atom:
f(P, Q) = None.as_numer_denom()_options = options.copy()options = set_defaults(options, extension = True)# WARNING: Decompyle incomplete
)()()

def apart_undetermined_coeffs(P, Q):
    '''Partial fractions via method of undetermined coefficients. '''
    X = numbered_symbols(cls = Dummy)
    symbols = []
    partial = []
    (_, factors) = Q.factor_list()
# WARNING: Decompyle incomplete


def apart_full_decomposition(P, Q):
    """
    Bronstein's full partial fraction decomposition algorithm.

    Given a univariate rational function ``f``, performing only GCD
    operations over the algebraic closure of the initial ground domain
    of definition, compute full partial fraction decomposition with
    fractions having linear denominators.

    Note that no factorization of the initial denominator of ``f`` is
    performed. The final decomposition is formed in terms of a sum of
    :class:`RootSum` instances.

    References
    ==========

    .. [1] [Bronstein93]_

    """
    return assemble_partfrac_list(apart_list(P / Q, P.gens[0]))

apart_list = (lambda f, x, dummies = (None, None): allowed_flags(options, [])f = sympify(f)if f.is_Atom:
f(P, Q) = None.as_numer_denom()options = set_defaults(options, extension = True)# WARNING: Decompyle incomplete
)()

def apart_list_full_decomposition(P, Q, dummygen):
    """
    Bronstein's full partial fraction decomposition algorithm.

    Given a univariate rational function ``f``, performing only GCD
    operations over the algebraic closure of the initial ground domain
    of definition, compute full partial fraction decomposition with
    fractions having linear denominators.

    Note that no factorization of the initial denominator of ``f`` is
    performed. The final decomposition is formed in terms of a sum of
    :class:`RootSum` instances.

    References
    ==========

    .. [1] [Bronstein93]_

    """
    (P_orig, Q_orig, x, U) = (P, Q, P.gen, [])
    u = Function('u')(x)
    a = Dummy('a')
    partial = []
# WARNING: Decompyle incomplete

assemble_partfrac_list = (lambda partial_list: common = partial_list[0]polypart = partial_list[1]pfd = polypart.as_expr()for r, nf, df, ex in partial_list[2]:
if isinstance(r, Poly):
nu = nf.expran = nf.variablesde = df.exprad = df.variablesde = de.subs(ad[0], an[0])func = Lambda(tuple(an), nu / de ** ex)pfd += RootSum(r, func, auto = False, quadratic = False)continuefor root in r:
pfd += nf(root) / df(root) ** excommon * pfd)()
