# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sparse.pyc (Python 3.11)

from collections.abc import Callable
from sympy.core.containers import Dict
from sympy.utilities.exceptions import sympy_deprecation_warning
from sympy.utilities.iterables import is_sequence
from sympy.utilities.misc import as_int
from matrixbase import MatrixBase
from repmatrix import MutableRepMatrix, RepMatrix
from utilities import _iszero
from decompositions import _liupc, _row_structure_symbolic_cholesky, _cholesky_sparse, _LDLdecomposition_sparse
from solvers import _lower_triangular_solve_sparse, _upper_triangular_solve_sparse

class SparseRepMatrix(RepMatrix):
    pass
# WARNING: Decompyle incomplete


class MutableSparseMatrix(MutableRepMatrix, SparseRepMatrix):
    _new = (lambda cls: pass# WARNING: Decompyle incomplete
)()

SparseMatrix = MutableSparseMatrix
