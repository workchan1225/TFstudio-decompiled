# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _dfm.pyc (Python 3.11)

from sympy.external.gmpy import GROUND_TYPES
from sympy.external.importtools import import_module
from sympy.utilities.decorator import doctest_depends_on
from sympy.polys.domains import ZZ, QQ
from exceptions import DMBadInputError, DMDomainError, DMNonSquareMatrixError, DMNonInvertibleMatrixError, DMRankError, DMShapeError, DMValueError
if GROUND_TYPES != 'flint':
    __doctest_skip__ = [
        '*']
flint = import_module('flint')
__all__ = [
    'DFM']
DFM = <NODE:12>()
from sympy.polys.matrices.ddm import DDM
from sympy.polys.matrices.ddm import SDM
