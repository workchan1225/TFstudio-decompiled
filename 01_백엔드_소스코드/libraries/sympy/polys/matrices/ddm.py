# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ddm.pyc (Python 3.11)

"""

Module for the DDM class.

The DDM class is an internal representation used by DomainMatrix. The letters
DDM stand for Dense Domain Matrix. A DDM instance represents a matrix using
elements from a polynomial Domain (e.g. ZZ, QQ, ...) in a dense-matrix
representation.

Basic usage:

    >>> from sympy import ZZ, QQ
    >>> from sympy.polys.matrices.ddm import DDM
    >>> A = DDM([[ZZ(0), ZZ(1)], [ZZ(-1), ZZ(0)]], (2, 2), ZZ)
    >>> A.shape
    (2, 2)
    >>> A
    [[0, 1], [-1, 0]]
    >>> type(A)
    <class 'sympy.polys.matrices.ddm.DDM'>
    >>> A @ A
    [[-1, 0], [0, -1]]

The ddm_* functions are designed to operate on DDM as well as on an ordinary
list of lists:

    >>> from sympy.polys.matrices.dense import ddm_idet
    >>> ddm_idet(A, QQ)
    1
    >>> ddm_idet([[0, 1], [-1, 0]], QQ)
    1
    >>> A
    [[-1, 0], [0, -1]]

Note that ddm_idet modifies the input matrix in-place. It is recommended to
use the DDM.det method as a friendlier interface to this instead which takes
care of copying the matrix:

    >>> B = DDM([[ZZ(0), ZZ(1)], [ZZ(-1), ZZ(0)]], (2, 2), ZZ)
    >>> B.det()
    1

Normally DDM would not be used directly and is just part of the internal
representation of DomainMatrix which adds further functionality including e.g.
unifying domains.

The dense format used by DDM is a list of lists of elements e.g. the 2x2
identity matrix is like [[1, 0], [0, 1]]. The DDM class itself is a subclass
of list and its list items are plain lists. Elements are accessed as e.g.
ddm[i][j] where ddm[i] gives the ith row and ddm[i][j] gets the element in the
jth column of that row. Subclassing list makes e.g. iteration and indexing
very efficient. We do not override __getitem__ because it would lose that
benefit.

The core routines are implemented by the ddm_* functions defined in dense.py.
Those functions are intended to be able to operate on a raw list-of-lists
representation of matrices with most functions operating in-place. The DDM
class takes care of copying etc and also stores a Domain object associated
with its elements. This makes it possible to implement things like A + B with
domain checking and also shape checking so that the list of lists
representation is friendlier.

"""
from itertools import chain
from sympy.external.gmpy import GROUND_TYPES
from sympy.utilities.decorator import doctest_depends_on
from exceptions import DMBadInputError, DMDomainError, DMNonSquareMatrixError, DMShapeError
from sympy.polys.domains import QQ
from dense import ddm_transpose, ddm_iadd, ddm_isub, ddm_ineg, ddm_imul, ddm_irmul, ddm_imatmul, ddm_irref, ddm_irref_den, ddm_idet, ddm_iinv, ddm_ilu_split, ddm_ilu_solve, ddm_berk
from lll import ddm_lll, ddm_lll_transform
if GROUND_TYPES != 'flint':
    __doctest_skip__ = [
        'DDM.to_dfm',
        'DDM.to_dfm_or_ddm']

class DDM(list):
    pass
# WARNING: Decompyle incomplete

from sdm import SDM
from dfm import DFM
