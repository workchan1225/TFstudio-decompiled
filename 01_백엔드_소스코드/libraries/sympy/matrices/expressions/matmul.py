# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: matmul.pyc (Python 3.11)

from sympy.assumptions.ask import ask, Q
from sympy.assumptions.refine import handlers_dict
from sympy.core import Basic, sympify, S
from sympy.core.mul import mul, Mul
from sympy.core.numbers import Number, Integer
from sympy.core.symbol import Dummy
from sympy.functions import adjoint
from sympy.strategies import rm_id, unpack, typed, flatten, exhaust, do_one, new
from sympy.matrices.exceptions import NonInvertibleMatrixError
from sympy.matrices.matrixbase import MatrixBase
from sympy.utilities.exceptions import sympy_deprecation_warning
from sympy.matrices.expressions._shape import validate_matmul_integer as validate
from inverse import Inverse
from matexpr import MatrixExpr
from matpow import MatPow
from transpose import transpose
from permutation import PermutationMatrix
from special import ZeroMatrix, Identity, GenericIdentity, OneMatrix

class MatMul(Mul, MatrixExpr):
    pass
# WARNING: Decompyle incomplete

mul.register_handlerclass((Mul, MatMul), MatMul)

def newmul(*args):
    if args[0] == 1:
        args = args[1:]
# WARNING: Decompyle incomplete


def any_zeros(mul):
    if (lambda .0: pass# WARNING: Decompyle incomplete
)(mul.args()):
        matrices = mul.args()
        return ZeroMatrix(matrices[0].rows, matrices[-1].cols)
    return any


def merge_explicit(matmul):
    """ Merge explicit MatrixBase arguments

    >>> from sympy import MatrixSymbol, Matrix, MatMul, pprint
    >>> from sympy.matrices.expressions.matmul import merge_explicit
    >>> A = MatrixSymbol('A', 2, 2)
    >>> B = Matrix([[1, 1], [1, 1]])
    >>> C = Matrix([[1, 2], [3, 4]])
    >>> X = MatMul(A, B, C)
    >>> pprint(X)
      [1  1] [1  2]
    A*[    ]*[    ]
      [1  1] [3  4]
    >>> pprint(merge_explicit(X))
      [4  6]
    A*[    ]
      [4  6]

    >>> X = MatMul(B, A, C)
    >>> pprint(X)
    [1  1]   [1  2]
    [    ]*A*[    ]
    [1  1]   [3  4]
    >>> pprint(merge_explicit(X))
    [1  1]   [1  2]
    [    ]*A*[    ]
    [1  1]   [3  4]
    """
    if not (lambda .0: pass# WARNING: Decompyle incomplete
)(matmul.args()):
        return matmul
    newargs = any
    last = matmul.args[0]
# WARNING: Decompyle incomplete


def remove_ids(mul):
    ''' Remove Identities from a MatMul

    This is a modified version of sympy.strategies.rm_id.
    This is necesssary because MatMul may contain both MatrixExprs and Exprs
    as args.

    See Also
    ========

    sympy.strategies.rm_id
    '''
    (factor, mmul) = mul.as_coeff_mmul()
    result = rm_id((lambda x: x.is_Identity is True))(mmul)
# WARNING: Decompyle incomplete


def factor_in_front(mul):
    (factor, matrices) = mul.as_coeff_matrices()
# WARNING: Decompyle incomplete


def combine_powers(mul):
    '''Combine consecutive powers with the same base into one, e.g.
    $$A \\times A^2 \\Rightarrow A^3$$

    This also cancels out the possible matrix inverses using the
    knowledgebase of :class:`~.Inverse`, e.g.,
    $$ Y \\times X \\times X^{-1} \\Rightarrow Y $$
    '''
    (factor, args) = mul.as_coeff_matrices()
    new_args = [
        args[0]]
# WARNING: Decompyle incomplete


def combine_permutations(mul):
    '''Refine products of permutation matrices as the products of cycles.
    '''
    args = mul.args
    l = len(args)
    if l < 2:
        return mul
    result = [
        None[0]]
# WARNING: Decompyle incomplete


def combine_one_matrices(mul):
    '''
    Combine products of OneMatrix

    e.g. OneMatrix(2, 3) * OneMatrix(3, 4) -> 3 * OneMatrix(2, 4)
    '''
    (factor, args) = mul.as_coeff_matrices()
    new_args = [
        args[0]]
# WARNING: Decompyle incomplete


def distribute_monom(mul):
    '''
    Simplify MatMul expressions but distributing
    rational term to MatMul.

    e.g. 2*(A+B) -> 2*A + 2*B
    '''
    pass
# WARNING: Decompyle incomplete

rules = (distribute_monom, any_zeros, remove_ids, combine_one_matrices, combine_powers, unpack, rm_id((lambda x: x == 1)), merge_explicit, factor_in_front, flatten, combine_permutations)
# WARNING: Decompyle incomplete
