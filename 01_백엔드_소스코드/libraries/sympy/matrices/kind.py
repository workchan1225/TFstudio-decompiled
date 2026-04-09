# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: kind.pyc (Python 3.11)

from sympy.core.kind import Kind, _NumberKind, NumberKind
from sympy.core.mul import Mul

class MatrixKind(Kind):
    pass
# WARNING: Decompyle incomplete

num_mat_mul = (lambda k1, k2: if not isinstance(k2, MatrixKind):
k2 = k1k1 = k2elemk = Mul._kind_dispatcher(k1, k2.element_kind)MatrixKind(elemk))()
mat_mat_mul = (lambda k1, k2: elemk = Mul._kind_dispatcher(k1.element_kind, k2.element_kind)MatrixKind(elemk))()
