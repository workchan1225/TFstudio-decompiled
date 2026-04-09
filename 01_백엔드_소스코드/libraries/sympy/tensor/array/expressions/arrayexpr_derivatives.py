# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: arrayexpr_derivatives.pyc (Python 3.11)

import operator
from functools import reduce, singledispatch
from sympy.core.expr import Expr
from sympy.core.singleton import S
from sympy.matrices.expressions.hadamard import HadamardProduct
from sympy.matrices.expressions.inverse import Inverse
from sympy.matrices.expressions.matexpr import MatrixExpr, MatrixSymbol
from sympy.matrices.expressions.special import Identity, OneMatrix
from sympy.matrices.expressions.transpose import Transpose
from sympy.combinatorics.permutations import _af_invert
from sympy.matrices.expressions.applyfunc import ElementwiseApplyFunction
from sympy.tensor.array.expressions.array_expressions import _ArrayExpr, ZeroArray, ArraySymbol, ArrayTensorProduct, ArrayAdd, PermuteDims, ArrayDiagonal, ArrayElementwiseApplyFunc, get_rank, get_shape, ArrayContraction, _array_tensor_product, _array_contraction, _array_diagonal, _array_add, _permute_dims, Reshape
from sympy.tensor.array.expressions.from_matrix_to_array import convert_matrix_to_array
array_derive = (lambda expr, x: raise NotImplementedError(f'''not implemented for type {type(expr)}'''))()
_ = (lambda expr = None, x = singledispatch: pass# WARNING: Decompyle incomplete
)()
_ = (lambda expr = None, x = None:
