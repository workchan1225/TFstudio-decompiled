# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: galoisgroups.pyc (Python 3.11)

'''
Compute Galois groups of polynomials.

We use algorithms from [1], with some modifications to use lookup tables for
resolvents.

References
==========

.. [1] Cohen, H. *A Course in Computational Algebraic Number Theory*.

'''
from collections import defaultdict
import random
from sympy.core.symbol import Dummy, symbols
from sympy.ntheory.primetest import is_square
from sympy.polys.domains import ZZ
from sympy.polys.densebasic import dup_random
from sympy.polys.densetools import dup_eval
from sympy.polys.euclidtools import dup_discriminant
from sympy.polys.factortools import dup_factor_list, dup_irreducible_p
from sympy.polys.numberfields.galois_resolvents import GaloisGroupException, get_resolvent_by_lookup, define_resolvents, Resolvent
from sympy.polys.numberfields.utilities import coeff_search
from sympy.polys.polytools import Poly, poly_from_expr, PolificationFailed, ComputationFailed
from sympy.polys.sqfreetools import dup_sqf_p
from sympy.utilities import public

class MaxTriesException(GaloisGroupException):
    pass


def tschirnhausen_transformation(T, max_coeff, max_tries, history, fixed_order = (10, 30, None, True)):
    """
    Given a univariate, monic, irreducible polynomial over the integers, find
    another such polynomial defining the same number field.

    Explanation
    ===========

    See Alg 6.3.4 of [1].

    Parameters
    ==========

    T : Poly
        The given polynomial
    max_coeff : int
        When choosing a transformation as part of the process,
        keep the coeffs between plus and minus this.
    max_tries : int
        Consider at most this many transformations.
    history : set, None, optional (default=None)
        Pass a set of ``Poly.rep``'s in order to prevent any of these
        polynomials from being returned as the polynomial ``U`` i.e. the
        transformation of the given polynomial *T*. The given poly *T* will
        automatically be added to this set, before we try to find a new one.
    fixed_order : bool, default True
        If ``True``, work through candidate transformations A(x) in a fixed
        order, from small coeffs to large, resulting in deterministic behavior.
        If ``False``, the A(x) are chosen randomly, while still working our way
        up from small coefficients to larger ones.

    Returns
    =======

    Pair ``(A, U)``

        ``A`` and ``U`` are ``Poly``, ``A`` is the
        transformation, and ``U`` is the transformed polynomial that defines
        the same number field as *T*. The polynomial ``A`` maps the roots of
        *T* to the roots of ``U``.

    Raises
    ======

    MaxTriesException
        if could not find a polynomial before exceeding *max_tries*.

    """
    pass
# WARNING: Decompyle incomplete


def has_square_disc(T):
    '''Convenience to check if a Poly or dup has square discriminant. '''
    d = T.discriminant() if isinstance(T, Poly) else dup_discriminant(T, ZZ)
    return is_square(d)


def _galois_group_degree_3(T, max_tries, randomize = (30, False)):
    '''
    Compute the Galois group of a polynomial of degree 3.

    Explanation
    ===========

    Uses Prop 6.3.5 of [1].

    '''
    S3TransitiveSubgroups = S3TransitiveSubgroups
    import sympy.combinatorics.galois
    return (S3TransitiveSubgroups.A3, True) if has_square_disc(T) else (S3TransitiveSubgroups.S3, False)


def _galois_group_degree_4_root_approx(T, max_tries, randomize = (30, False)):
    '''
    Compute the Galois group of a polynomial of degree 4.

    Explanation
    ===========

    Follows Alg 6.3.7 of [1], using a pure root approximation approach.

    '''
    pass
# WARNING: Decompyle incomplete


def _galois_group_degree_4_lookup(T, max_tries, randomize = (30, False)):
    '''
    Compute the Galois group of a polynomial of degree 4.

    Explanation
    ===========

    Based on Alg 6.3.6 of [1], but uses resolvent coeff lookup.

    '''
    S4TransitiveSubgroups = S4TransitiveSubgroups
    import sympy.combinatorics.galois
    history = set()
# WARNING: Decompyle incomplete


def _galois_group_degree_5_hybrid(T, max_tries, randomize = (30, False)):
    '''
    Compute the Galois group of a polynomial of degree 5.

    Explanation
    ===========

    Based on Alg 6.3.9 of [1], but uses a hybrid approach, combining resolvent
    coeff lookup, with root approximation.

    '''
    pass
# WARNING: Decompyle incomplete


def _galois_group_degree_5_lookup_ext_factor(T, max_tries, randomize = (30, False)):
    '''
    Compute the Galois group of a polynomial of degree 5.

    Explanation
    ===========

    Based on Alg 6.3.9 of [1], but uses resolvent coeff lookup, plus
    factorization over an algebraic extension.

    '''
    S5TransitiveSubgroups = S5TransitiveSubgroups
    import sympy.combinatorics.galois
    _T = T
    history = set()
    for i in range(max_tries):
        R_dup = get_resolvent_by_lookup(T, 1)
        if dup_sqf_p(R_dup, ZZ):
            pass
        else:
            (_, T) = tschirnhausen_transformation(T, max_tries = max_tries, history = history, fixed_order = not randomize)
        raise MaxTriesException
        sq_disc = has_square_disc(T)
        if dup_irreducible_p(R_dup, ZZ):
            return (S5TransitiveSubgroups.A5, True) if sq_disc else (S5TransitiveSubgroups.S5, False)
        if not None:
            return (S5TransitiveSubgroups.M20, False)
        fl = None(_T, domain = ZZ.alg_field_from_poly(_T)).factor_list()[1]
        if len(fl) == 5:
            return (S5TransitiveSubgroups.C5, True)
        return (None.D5, True)


def _galois_group_degree_6_lookup(T, max_tries, randomize = (30, False)):
    '''
    Compute the Galois group of a polynomial of degree 6.

    Explanation
    ===========

    Based on Alg 6.3.10 of [1], but uses resolvent coeff lookup.

    '''
    S6TransitiveSubgroups = S6TransitiveSubgroups
    import sympy.combinatorics.galois
    history = set()
# WARNING: Decompyle incomplete

galois_group = (lambda f = public, *, by_name: pass# WARNING: Decompyle incomplete
)()
