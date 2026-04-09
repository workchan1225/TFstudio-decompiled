# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: domainmatrix.pyc (Python 3.11)

'''

Module for the DomainMatrix class.

A DomainMatrix represents a matrix with elements that are in a particular
Domain. Each DomainMatrix internally wraps a DDM which is used for the
lower-level operations. The idea is that the DomainMatrix class provides the
convenience routines for converting between Expr and the poly domains as well
as unifying matrices with different domains.

'''
from collections import Counter
from functools import reduce
from typing import Union as tUnion, Tuple as tTuple
from sympy.external.gmpy import GROUND_TYPES
from sympy.utilities.decorator import doctest_depends_on
from sympy.core.sympify import _sympify
from domains import Domain
from constructor import construct_domain
from exceptions import DMFormatError, DMBadInputError, DMShapeError, DMDomainError, DMNotAField, DMNonSquareMatrixError, DMNonInvertibleMatrixError
from domainscalar import DomainScalar
from sympy.polys.domains import ZZ, EXRAW, QQ
from sympy.polys.densearith import dup_mul
from sympy.polys.densebasic import dup_convert
from sympy.polys.densetools import dup_mul_ground, dup_quo_ground, dup_content, dup_clear_denoms, dup_primitive, dup_transform
from sympy.polys.factortools import dup_factor_list
from sympy.polys.polyutils import _sort_factors
from ddm import DDM
from sdm import SDM
from dfm import DFM
from rref import _dm_rref, _dm_rref_den
if GROUND_TYPES != 'flint':
    __doctest_skip__ = [
        'DomainMatrix.to_dfm',
        'DomainMatrix.to_dfm_or_ddm']
else:
    __doctest_skip__ = [
        'DomainMatrix.from_list']

def DM(rows, domain):
    '''Convenient alias for DomainMatrix.from_list

    Examples
    ========

    >>> from sympy import ZZ
    >>> from sympy.polys.matrices import DM
    >>> DM([[1, 2], [3, 4]], ZZ)
    DomainMatrix([[1, 2], [3, 4]], (2, 2), ZZ)

    See Also
    ========

    DomainMatrix.from_list
    '''
    return DomainMatrix.from_list(rows, domain)


class DomainMatrix:
    pass
# WARNING: Decompyle incomplete


def _collect_factors(factors_list):
    '''
    Collect repeating factors and sort.

    >>> from sympy.polys.matrices.domainmatrix import _collect_factors
    >>> _collect_factors([([1, 2], 2), ([1, 4], 3), ([1, 2], 5)])
    [([1, 4], 3), ([1, 2], 7)]
    '''
    factors = Counter()
    for factor, exponent in factors_list:
        
        def factors.items()()(.0):
            return [ (list(f), e) for f, e in .0 ]

        return _sort_factors(factors_list)
