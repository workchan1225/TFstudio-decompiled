# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: generators.pyc (Python 3.11)

from sympy.combinatorics.permutations import Permutation
from sympy.core.symbol import symbols
from sympy.matrices import Matrix
from sympy.utilities.iterables import variations, rotate_left

def symmetric(n):
    '''
    Generates the symmetric group of order n, Sn.

    Examples
    ========

    >>> from sympy.combinatorics.generators import symmetric
    >>> list(symmetric(3))
    [(2), (1 2), (2)(0 1), (0 1 2), (0 2 1), (0 2)]
    '''
    pass
# WARNING: Decompyle incomplete


def cyclic(n):
    '''
    Generates the cyclic group of order n, Cn.

    Examples
    ========

    >>> from sympy.combinatorics.generators import cyclic
    >>> list(cyclic(5))
    [(4), (0 1 2 3 4), (0 2 4 1 3),
     (0 3 1 4 2), (0 4 3 2 1)]

    See Also
    ========

    dihedral
    '''
    pass
# WARNING: Decompyle incomplete


def alternating(n):
    '''
    Generates the alternating group of order n, An.

    Examples
    ========

    >>> from sympy.combinatorics.generators import alternating
    >>> list(alternating(3))
    [(2), (0 1 2), (0 2 1)]
    '''
    pass
# WARNING: Decompyle incomplete


def dihedral(n):
    """
    Generates the dihedral group of order 2n, Dn.

    The result is given as a subgroup of Sn, except for the special cases n=1
    (the group S2) and n=2 (the Klein 4-group) where that's not possible
    and embeddings in S2 and S4 respectively are given.

    Examples
    ========

    >>> from sympy.combinatorics.generators import dihedral
    >>> list(dihedral(3))
    [(2), (0 2), (0 1 2), (1 2), (0 2 1), (2)(0 1)]

    See Also
    ========

    cyclic
    """
    pass
# WARNING: Decompyle incomplete


def rubik_cube_generators():
    """Return the permutations of the 3x3 Rubik's cube, see
    https://www.gap-system.org/Doc/Examples/rubik.html
    """
    a = [
        [
            (1, 3, 8, 6),
            (2, 5, 7, 4),
            (9, 33, 25, 17),
            (10, 34, 26, 18),
            (11, 35, 27, 19)],
        [
            (9, 11, 16, 14),
            (10, 13, 15, 12),
            (1, 17, 41, 40),
            (4, 20, 44, 37),
            (6, 22, 46, 35)],
        [
            (17, 19, 24, 22),
            (18, 21, 23, 20),
            (6, 25, 43, 16),
            (7, 28, 42, 13),
            (8, 30, 41, 11)],
        [
            (25, 27, 32, 30),
            (26, 29, 31, 28),
            (3, 38, 43, 19),
            (5, 36, 45, 21),
            (8, 33, 48, 24)],
        [
            (33, 35, 40, 38),
            (34, 37, 39, 36),
            (3, 9, 46, 32),
            (2, 12, 47, 29),
            (1, 14, 48, 27)],
        [
            (41, 43, 48, 46),
            (42, 45, 47, 44),
            (14, 22, 30, 38),
            (15, 23, 31, 39),
            (16, 24, 32, 40)]]
    return a()


def rubik(n):
    """Return permutations for an nxn Rubik's cube.

    Permutations returned are for rotation of each of the slice
    from the face up to the last face for each of the 3 sides (in this order):
    front, right and bottom. Hence, the first n - 1 permutations are for the
    slices from the front.
    """
    pass
# WARNING: Decompyle incomplete
