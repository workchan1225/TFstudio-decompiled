# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: from_array_to_matrix.pyc (Python 3.11)

import itertools
from collections import defaultdict
from typing import Tuple as tTuple, Union as tUnion, FrozenSet, Dict as tDict, List, Optional
from functools import singledispatch
from itertools import accumulate
from sympy import MatMul, Basic, Wild, KroneckerProduct
from sympy.assumptions.ask import Q, ask
from sympy.core.mul import Mul
from sympy.core.singleton import S
from sympy.matrices.expressions.diagonal import DiagMatrix
from sympy.matrices.expressions.hadamard import hadamard_product, HadamardPower
from sympy.matrices.expressions.matexpr import MatrixExpr
from sympy.matrices.expressions.special import Identity, ZeroMatrix, OneMatrix
from sympy.matrices.expressions.trace import Trace
from sympy.matrices.expressions.transpose import Transpose
from sympy.combinatorics.permutations import _af_invert, Permutation
from sympy.matrices.matrixbase import MatrixBase
from sympy.matrices.expressions.applyfunc import ElementwiseApplyFunction
from sympy.matrices.expressions.matexpr import MatrixElement
from sympy.tensor.array.expressions.array_expressions import PermuteDims, ArrayDiagonal, ArrayTensorProduct, OneArray, get_rank, _get_subrank, ZeroArray, ArrayContraction, ArrayAdd, _CodegenArrayAbstract, get_shape, ArrayElementwiseApplyFunc, _ArrayExpr, _EditArrayContraction, _ArgE, ArrayElement, _array_tensor_product, _array_contraction, _array_diagonal, _array_add, _permute_dims
from sympy.tensor.array.expressions.utils import _get_mapping_from_subranks

def _get_candidate_for_matmul_from_contraction(scan_indices = None, remaining_args = None):
    scan_indices_int = scan_indices()
    if len(scan_indices_int) == 0:
        return (None, False, -1)
    
    def transpose(.0):
        pass
    # WARNING: Decompyle incomplete

    candidate = None
    candidate_index = -1
# WARNING: Decompyle incomplete


def _insert_candidate_into_editor(editor, arg_with_ind = None, candidate = None, transpose1 = None, transpose2 = ('editor', _EditArrayContraction, 'arg_with_ind', _ArgE, 'candidate', _ArgE, 'transpose1', bool, 'transpose2', bool)):
    other = candidate.element
    if transpose2:
        other = Transpose(other)
        other_index = candidate.indices[0]
    else:
        other_index = candidate.indices[1]
    new_element = Transpose(arg_with_ind.element) if transpose1 else arg_with_ind.element * other
    editor.args_with_ind.remove(candidate)
    new_arge = _ArgE(new_element)
    return (new_arge, other_index)


def _support_function_tp1_recognize(contraction_indices, args):
    pass
# WARNING: Decompyle incomplete


def _find_trivial_matrices_rewrite(expr = None):
    trivial_matrices = []
    pos = None
    first = None
    second = None
    removed = []
    counter = 0
    args = list(expr.args)
# WARNING: Decompyle incomplete


def _find_trivial_kronecker_products_broadcast(expr = None):
    pass
# WARNING: Decompyle incomplete

_array2matrix = (lambda expr: expr)()
_ = (lambda expr = None: pass# WARNING: Decompyle incomplete
)()
_ = (lambda expr = None: pass# WARNING: Decompyle incomplete
)()
_ = (lambda expr = None: expr = expr.flatten_contraction_of_diagonal()expr = identify_removable_identity_matrices(expr)expr = expr.split_multiple_contractions()expr = identify_hadamard_products(expr)if not isinstance(expr, ArrayContraction):
_array2matrix(expr)subexpr = None.exprcontraction_indices = expr.contraction_indices# WARNING: Decompyle incomplete
)()
_ = (lambda expr = None: pass# WARNING: Decompyle incomplete
)()
_ = (lambda expr = None: pass# WARNING: Decompyle incomplete
)()
_ = (lambda expr = None: addends = expr.args()# WARNING: Decompyle incomplete
)()
_ = (lambda expr = None: subexpr = _array2matrix(expr.expr)# WARNING: Decompyle incomplete
)()
_ = (lambda expr = None: ret = _array2matrix(expr.name)# WARNING: Decompyle incomplete
)()
_remove_trivial_dims = (lambda expr: (expr, []))()
_ = (lambda expr = None: removed = []newargs = []cumul = accumulate([
0]((lambda .0: [ get_rank(arg) for arg in .0 ]) + expr.args()))
    pending = None
    prev_i = None
# WARNING: Decompyle incomplete
)()
_ = (lambda expr = None: rec = expr.args()# WARNING: Decompyle incomplete
)()
_ = (lambda expr = None: pass# WARNING: Decompyle incomplete
)()
_ = (lambda expr = None: pass# WARNING: Decompyle incomplete
)()

def _remove_diagonalized_identity_matrices(expr = None):
    pass
# WARNING: Decompyle incomplete

_ = (lambda expr = None: pass# WARNING: Decompyle incomplete
)()
_ = (lambda expr = None: (subexpr, removed) = _remove_trivial_dims(expr.expr)if subexpr.shape == (1, 1):
(expr.function(subexpr), removed + [
0,
1])(None(expr.function, subexpr), []))()
_ = (lambda expr = None: (subexpr, removed) = _remove_trivial_dims(expr.expr)(ArrayElementwiseApplyFunc(expr.function, subexpr), removed))()

def convert_array_to_matrix(expr):
    '''
    Recognize matrix expressions in codegen objects.

    If more than one matrix multiplication line have been detected, return a
    list with the matrix expressions.

    Examples
    ========

    >>> from sympy.tensor.array.expressions.from_indexed_to_array import convert_indexed_to_array
    >>> from sympy.tensor.array import tensorcontraction, tensorproduct
    >>> from sympy import MatrixSymbol, Sum
    >>> from sympy.abc import i, j, k, l, N
    >>> from sympy.tensor.array.expressions.from_matrix_to_array import convert_matrix_to_array
    >>> from sympy.tensor.array.expressions.from_array_to_matrix import convert_array_to_matrix
    >>> A = MatrixSymbol("A", N, N)
    >>> B = MatrixSymbol("B", N, N)
    >>> C = MatrixSymbol("C", N, N)
    >>> D = MatrixSymbol("D", N, N)

    >>> expr = Sum(A[i, j]*B[j, k], (j, 0, N-1))
    >>> cg = convert_indexed_to_array(expr)
    >>> convert_array_to_matrix(cg)
    A*B
    >>> cg = convert_indexed_to_array(expr, first_indices=[k])
    >>> convert_array_to_matrix(cg)
    B.T*A.T

    Transposition is detected:

    >>> expr = Sum(A[j, i]*B[j, k], (j, 0, N-1))
    >>> cg = convert_indexed_to_array(expr)
    >>> convert_array_to_matrix(cg)
    A.T*B
    >>> cg = convert_indexed_to_array(expr, first_indices=[k])
    >>> convert_array_to_matrix(cg)
    B.T*A

    Detect the trace:

    >>> expr = Sum(A[i, i], (i, 0, N-1))
    >>> cg = convert_indexed_to_array(expr)
    >>> convert_array_to_matrix(cg)
    Trace(A)

    Recognize some more complex traces:

    >>> expr = Sum(A[i, j]*B[j, i], (i, 0, N-1), (j, 0, N-1))
    >>> cg = convert_indexed_to_array(expr)
    >>> convert_array_to_matrix(cg)
    Trace(A*B)

    More complicated expressions:

    >>> expr = Sum(A[i, j]*B[k, j]*A[l, k], (j, 0, N-1), (k, 0, N-1))
    >>> cg = convert_indexed_to_array(expr)
    >>> convert_array_to_matrix(cg)
    A*B.T*A.T

    Expressions constructed from matrix expressions do not contain literal
    indices, the positions of free indices are returned instead:

    >>> expr = A*B
    >>> cg = convert_matrix_to_array(expr)
    >>> convert_array_to_matrix(cg)
    A*B

    If more than one line of matrix multiplications is detected, return
    separate matrix multiplication factors embedded in a tensor product object:

    >>> cg = tensorcontraction(tensorproduct(A, B, C, D), (1, 2), (5, 6))
    >>> convert_array_to_matrix(cg)
    ArrayTensorProduct(A*B, C*D)

    The two lines have free indices at axes 0, 3 and 4, 7, respectively.
    '''
    rec = _array2matrix(expr)
    (rec, removed) = _remove_trivial_dims(rec)
    return rec


def _array_diag2contr_diagmatrix(expr = None):
    pass
# WARNING: Decompyle incomplete


def _a2m_mul(*args):
    pass
# WARNING: Decompyle incomplete


def _a2m_tensor_product(*args):
    scalars = []
    arrays = []
    for arg in args:
        if isinstance(arg, (MatrixExpr, _ArrayExpr, _CodegenArrayAbstract)):
            arrays.append(arg)
            continue
        scalars.append(arg)
        scalar = Mul.fromiter(scalars)
        if len(arrays) == 0:
            return scalar
        if None != 1:
            if isinstance(arrays[0], _CodegenArrayAbstract):
                arrays = [
                    scalar] + arrays
            
# WARNING: Decompyle incomplete


def _a2m_add(*args):
    pass
# WARNING: Decompyle incomplete


def _a2m_trace(arg):
    if isinstance(arg, _CodegenArrayAbstract):
        return _array_contraction(arg, (0, 1))
    Trace = Trace
    import sympy.matrices.expressions.trace
    return Trace(arg)


def _a2m_transpose(arg):
    if isinstance(arg, _CodegenArrayAbstract):
        return _permute_dims(arg, [
            1,
            0])
    Transpose = Transpose
    import sympy.matrices.expressions.transpose
    return Transpose(arg).doit()


def identify_hadamard_products(expr = None):
    pass
# WARNING: Decompyle incomplete


def identify_removable_identity_matrices(expr):
    pass
# WARNING: Decompyle incomplete


def remove_identity_matrices(expr = None):
    pass
# WARNING: Decompyle incomplete


def _combine_removed(dim = None, removed1 = None, removed2 = None):
    removed1 = sorted(removed1)
    removed2 = sorted(removed2)
    i = 0
    j = 0
    removed = []
# WARNING: Decompyle incomplete


def _array_contraction_to_diagonal_multiple_identity(expr = None):
    pass
# WARNING: Decompyle incomplete
