# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: basis.pyc (Python 3.11)

'''Computing integral bases for number fields. '''
from sympy.polys.polytools import Poly
from sympy.polys.domains.algebraicfield import AlgebraicField
from sympy.polys.domains.integerring import ZZ
from sympy.polys.domains.rationalfield import QQ
from sympy.utilities.decorator import public
from modules import ModuleEndomorphism, ModuleHomomorphism, PowerBasis
from utilities import extract_fundamental_discriminant

def _apply_Dedekind_criterion(T, p):
    '''
    Apply the "Dedekind criterion" to test whether the order needs to be
    enlarged relative to a given prime *p*.
    '''
    x = T.gen
    T_bar = Poly(T, modulus = p)
    (lc, fl) = T_bar.factor_list()
# WARNING: Decompyle incomplete


def nilradical_mod_p(H, p, q = (None,)):
    '''
    Compute the nilradical mod *p* for a given order *H*, and prime *p*.

    Explanation
    ===========

    This is the ideal $I$ in $H/pH$ consisting of all elements some positive
    power of which is zero in this quotient ring, i.e. is a multiple of *p*.

    Parameters
    ==========

    H : :py:class:`~.Submodule`
        The given order.
    p : int
        The rational prime.
    q : int, optional
        If known, the smallest power of *p* that is $>=$ the dimension of *H*.
        If not provided, we compute it here.

    Returns
    =======

    :py:class:`~.Module` representing the nilradical mod *p* in *H*.

    References
    ==========

    .. [1] Cohen, H. *A Course in Computational Algebraic Number Theory*.
    (See Lemma 6.1.6.)

    '''
    pass
# WARNING: Decompyle incomplete


def _second_enlargement(H, p, q):
    '''
    Perform the second enlargement in the Round Two algorithm.
    '''
    pass
# WARNING: Decompyle incomplete

round_two = (lambda T, radicals = (None,): K = Noneif isinstance(T, AlgebraicField):
T = T.ext.minpoly_of_element()K = Tif T.is_univariate and T.is_irreducible or T.domain not in (ZZ, QQ):
raise ValueError('Round 2 requires an irreducible univariate polynomial over ZZ or QQ.')(T, _) = T.make_monic_over_integers_by_scaling_roots()n = T.degree()D = T.discriminant()D_modulus = ZZ.from_sympy(abs(D))(_, F) = extract_fundamental_discriminant(D)# WARNING: Decompyle incomplete
)()
