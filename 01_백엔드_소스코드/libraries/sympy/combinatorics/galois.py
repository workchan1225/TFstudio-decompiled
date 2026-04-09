# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: galois.pyc (Python 3.11)

"""
Construct transitive subgroups of symmetric groups, useful in Galois theory.

Besides constructing instances of the :py:class:`~.PermutationGroup` class to
represent the transitive subgroups of $S_n$ for small $n$, this module provides
*names* for these groups.

In some applications, it may be preferable to know the name of a group,
rather than receive an instance of the :py:class:`~.PermutationGroup`
class, and then have to do extra work to determine which group it is, by
checking various properties.

Names are instances of ``Enum`` classes defined in this module. With a name in
hand, the name's ``get_perm_group`` method can then be used to retrieve a
:py:class:`~.PermutationGroup`.

The names used for groups in this module are taken from [1].

References
==========

.. [1] Cohen, H. *A Course in Computational Algebraic Number Theory*.

"""
from collections import defaultdict
from enum import Enum
import itertools
from sympy.combinatorics.named_groups import SymmetricGroup, AlternatingGroup, CyclicGroup, DihedralGroup, set_symmetric_group_properties, set_alternating_group_properties
from sympy.combinatorics.perm_groups import PermutationGroup
from sympy.combinatorics.permutations import Permutation

class S1TransitiveSubgroups(Enum):
    '''
    Names for the transitive subgroups of S1.
    '''
    S1 = 'S1'
    
    def get_perm_group(self):
        return SymmetricGroup(1)



class S2TransitiveSubgroups(Enum):
    '''
    Names for the transitive subgroups of S2.
    '''
    S2 = 'S2'
    
    def get_perm_group(self):
        return SymmetricGroup(2)



class S3TransitiveSubgroups(Enum):
    '''
    Names for the transitive subgroups of S3.
    '''
    A3 = 'A3'
    S3 = 'S3'
    
    def get_perm_group(self):
        if self == S3TransitiveSubgroups.A3:
            return AlternatingGroup(3)
        if None == S3TransitiveSubgroups.S3:
            return SymmetricGroup(3)



class S4TransitiveSubgroups(Enum):
    '''
    Names for the transitive subgroups of S4.
    '''
    C4 = 'C4'
    V = 'V'
    D4 = 'D4'
    A4 = 'A4'
    S4 = 'S4'
    
    def get_perm_group(self):
        if self == S4TransitiveSubgroups.C4:
            return CyclicGroup(4)
        if None == S4TransitiveSubgroups.V:
            return four_group()
        if None == S4TransitiveSubgroups.D4:
            return DihedralGroup(4)
        if None == S4TransitiveSubgroups.A4:
            return AlternatingGroup(4)
        if None == S4TransitiveSubgroups.S4:
            return SymmetricGroup(4)



class S5TransitiveSubgroups(Enum):
    '''
    Names for the transitive subgroups of S5.
    '''
    C5 = 'C5'
    D5 = 'D5'
    M20 = 'M20'
    A5 = 'A5'
    S5 = 'S5'
    
    def get_perm_group(self):
        if self == S5TransitiveSubgroups.C5:
            return CyclicGroup(5)
        if None == S5TransitiveSubgroups.D5:
            return DihedralGroup(5)
        if None == S5TransitiveSubgroups.M20:
            return M20()
        if None == S5TransitiveSubgroups.A5:
            return AlternatingGroup(5)
        if None == S5TransitiveSubgroups.S5:
            return SymmetricGroup(5)



class S6TransitiveSubgroups(Enum):
    '''
    Names for the transitive subgroups of S6.
    '''
    C6 = 'C6'
    S3 = 'S3'
    D6 = 'D6'
    A4 = 'A4'
    G18 = 'G18'
    A4xC2 = 'A4 x C2'
    S4m = 'S4-'
    S4p = 'S4+'
    G36m = 'G36-'
    G36p = 'G36+'
    S4xC2 = 'S4 x C2'
    PSL2F5 = 'PSL2(F5)'
    G72 = 'G72'
    PGL2F5 = 'PGL2(F5)'
    A6 = 'A6'
    S6 = 'S6'
    
    def get_perm_group(self):
        if self == S6TransitiveSubgroups.C6:
            return CyclicGroup(6)
        if None == S6TransitiveSubgroups.S3:
            return S3_in_S6()
        if None == S6TransitiveSubgroups.D6:
            return DihedralGroup(6)
        if None == S6TransitiveSubgroups.A4:
            return A4_in_S6()
        if None == S6TransitiveSubgroups.G18:
            return G18()
        if None == S6TransitiveSubgroups.A4xC2:
            return A4xC2()
        if None == S6TransitiveSubgroups.S4m:
            return S4m()
        if None == S6TransitiveSubgroups.S4p:
            return S4p()
        if None == S6TransitiveSubgroups.G36m:
            return G36m()
        if None == S6TransitiveSubgroups.G36p:
            return G36p()
        if None == S6TransitiveSubgroups.S4xC2:
            return S4xC2()
        if None == S6TransitiveSubgroups.PSL2F5:
            return PSL2F5()
        if None == S6TransitiveSubgroups.G72:
            return G72()
        if None == S6TransitiveSubgroups.PGL2F5:
            return PGL2F5()
        if None == S6TransitiveSubgroups.A6:
            return AlternatingGroup(6)
        if None == S6TransitiveSubgroups.S6:
            return SymmetricGroup(6)



def four_group():
    '''
    Return a representation of the Klein four-group as a transitive subgroup
    of S4.
    '''
    return PermutationGroup(Permutation(0, 1)(2, 3), Permutation(0, 2)(1, 3))


def M20():
    '''
    Return a representation of the metacyclic group M20, a transitive subgroup
    of S5 that is one of the possible Galois groups for polys of degree 5.

    Notes
    =====

    See [1], Page 323.

    '''
    G = PermutationGroup(Permutation(0, 1, 2, 3, 4), Permutation(1, 2, 4, 3))
    G._degree = 5
    G._order = 20
    G._is_transitive = True
    G._is_sym = False
    G._is_alt = False
    G._is_cyclic = False
    G._is_dihedral = False
    return G


def S3_in_S6():
    '''
    Return a representation of S3 as a transitive subgroup of S6.

    Notes
    =====

    The representation is found by viewing the group as the symmetries of a
    triangular prism.

    '''
    G = PermutationGroup(Permutation(0, 1, 2)(3, 4, 5), Permutation(0, 3)(2, 4)(1, 5))
    set_symmetric_group_properties(G, 3, 6)
    return G


def A4_in_S6():
    '''
    Return a representation of A4 as a transitive subgroup of S6.

    Notes
    =====

    This was computed using :py:func:`~.find_transitive_subgroups_of_S6`.

    '''
    G = PermutationGroup(Permutation(0, 4, 5)(1, 3, 2), Permutation(0, 1, 2)(3, 5, 4))
    set_alternating_group_properties(G, 4, 6)
    return G


def S4m():
    '''
    Return a representation of the S4- transitive subgroup of S6.

    Notes
    =====

    This was computed using :py:func:`~.find_transitive_subgroups_of_S6`.

    '''
    G = PermutationGroup(Permutation(1, 4, 5, 3), Permutation(0, 4)(1, 5)(2, 3))
    set_symmetric_group_properties(G, 4, 6)
    return G


def S4p():
    '''
    Return a representation of the S4+ transitive subgroup of S6.

    Notes
    =====

    This was computed using :py:func:`~.find_transitive_subgroups_of_S6`.

    '''
    G = PermutationGroup(Permutation(0, 2, 4, 1)(3, 5), Permutation(0, 3)(4, 5))
    set_symmetric_group_properties(G, 4, 6)
    return G


def A4xC2():
    '''
    Return a representation of the (A4 x C2) transitive subgroup of S6.

    Notes
    =====

    This was computed using :py:func:`~.find_transitive_subgroups_of_S6`.

    '''
    return PermutationGroup(Permutation(0, 4, 5)(1, 3, 2), Permutation(0, 1, 2)(3, 5, 4), Permutation(5)(2, 4))


def S4xC2():
    '''
    Return a representation of the (S4 x C2) transitive subgroup of S6.

    Notes
    =====

    This was computed using :py:func:`~.find_transitive_subgroups_of_S6`.

    '''
    return PermutationGroup(Permutation(1, 4, 5, 3), Permutation(0, 4)(1, 5)(2, 3), Permutation(1, 4)(3, 5))


def G18():
    '''
    Return a representation of the group G18, a transitive subgroup of S6
    isomorphic to the semidirect product of C3^2 with C2.

    Notes
    =====

    This was computed using :py:func:`~.find_transitive_subgroups_of_S6`.

    '''
    return PermutationGroup(Permutation(5)(0, 1, 2), Permutation(3, 4, 5), Permutation(0, 4)(1, 5)(2, 3))


def G36m():
    '''
    Return a representation of the group G36-, a transitive subgroup of S6
    isomorphic to the semidirect product of C3^2 with C2^2.

    Notes
    =====

    This was computed using :py:func:`~.find_transitive_subgroups_of_S6`.

    '''
    return PermutationGroup(Permutation(5)(0, 1, 2), Permutation(3, 4, 5), Permutation(1, 2)(3, 5), Permutation(0, 4)(1, 5)(2, 3))


def G36p():
    '''
    Return a representation of the group G36+, a transitive subgroup of S6
    isomorphic to the semidirect product of C3^2 with C4.

    Notes
    =====

    This was computed using :py:func:`~.find_transitive_subgroups_of_S6`.

    '''
    return PermutationGroup(Permutation(5)(0, 1, 2), Permutation(3, 4, 5), Permutation(0, 5, 2, 3)(1, 4))


def G72():
    '''
    Return a representation of the group G72, a transitive subgroup of S6
    isomorphic to the semidirect product of C3^2 with D4.

    Notes
    =====

    See [1], Page 325.

    '''
    return PermutationGroup(Permutation(5)(0, 1, 2), Permutation(0, 4, 1, 3)(2, 5), Permutation(0, 3)(1, 4)(2, 5))


def PSL2F5():
    '''
    Return a representation of the group $PSL_2(\\mathbb{F}_5)$, as a transitive
    subgroup of S6, isomorphic to $A_5$.

    Notes
    =====

    This was computed using :py:func:`~.find_transitive_subgroups_of_S6`.

    '''
    G = PermutationGroup(Permutation(0, 4, 5)(1, 3, 2), Permutation(0, 4, 3, 1, 5))
    set_alternating_group_properties(G, 5, 6)
    return G


def PGL2F5():
    '''
    Return a representation of the group $PGL_2(\\mathbb{F}_5)$, as a transitive
    subgroup of S6, isomorphic to $S_5$.

    Notes
    =====

    See [1], Page 325.

    '''
    G = PermutationGroup(Permutation(0, 1, 2, 3, 4), Permutation(0, 5)(1, 2)(3, 4))
    set_symmetric_group_properties(G, 5, 6)
    return G


def find_transitive_subgroups_of_S6(*, print_report, *targets):
    '''
    Search for certain transitive subgroups of $S_6$.

    The symmetric group $S_6$ has 16 different transitive subgroups, up to
    conjugacy. Some are more easily constructed than others. For example, the
    dihedral group $D_6$ is immediately found, but it is not at all obvious how
    to realize $S_4$ or $S_5$ *transitively* within $S_6$.

    In some cases there are well-known constructions that can be used. For
    example, $S_5$ is isomorphic to $PGL_2(\\mathbb{F}_5)$, which acts in a
    natural way on the projective line $P^1(\\mathbb{F}_5)$, a set of order 6.

    In absence of such special constructions however, we can simply search for
    generators. For example, transitive instances of $A_4$ and $S_4$ can be
    found within $S_6$ in this way.

    Once we are engaged in such searches, it may then be easier (if less
    elegant) to find even those groups like $S_5$ that do have special
    constructions, by mere search.

    This function locates generators for transitive instances in $S_6$ of the
    following subgroups:

    * $A_4$
    * $S_4^-$ ($S_4$ not contained within $A_6$)
    * $S_4^+$ ($S_4$ contained within $A_6$)
    * $A_4 \\times C_2$
    * $S_4 \\times C_2$
    * $G_{18}   = C_3^2 \\rtimes C_2$
    * $G_{36}^- = C_3^2 \\rtimes C_2^2$
    * $G_{36}^+ = C_3^2 \\rtimes C_4$
    * $G_{72}   = C_3^2 \\rtimes D_4$
    * $A_5$
    * $S_5$

    Note: Each of these groups also has a dedicated function in this module
    that returns the group immediately, using generators that were found by
    this search procedure.

    The search procedure serves as a record of how these generators were
    found. Also, due to randomness in the generation of the elements of
    permutation groups, it can be called again, in order to (probably) get
    different generators for the same groups.

    Parameters
    ==========

    targets : list of :py:class:`~.S6TransitiveSubgroups` values
        The groups you want to find.

    print_report : bool (default False)
        If True, print to stdout the generators found for each group.

    Returns
    =======

    dict
        mapping each name in *targets* to the :py:class:`~.PermutationGroup`
        that was found

    References
    ==========

    .. [2] https://en.wikipedia.org/wiki/Projective_linear_group#Exceptional_isomorphisms
    .. [3] https://en.wikipedia.org/wiki/Automorphisms_of_the_symmetric_and_alternating_groups#PGL%282,5%29

    '''
    pass
# WARNING: Decompyle incomplete
