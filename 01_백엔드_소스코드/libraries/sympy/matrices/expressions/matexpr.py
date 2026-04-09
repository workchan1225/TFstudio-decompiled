# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: matexpr.pyc (Python 3.11)

from __future__ import annotations
from functools import wraps
from sympy.core import S, Integer, Basic, Mul, Add
from sympy.core.assumptions import check_assumptions
from sympy.core.decorators import call_highest_priority
from sympy.core.expr import Expr, ExprBuilder
from sympy.core.logic import FuzzyBool
from sympy.core.symbol import Str, Dummy, symbols, Symbol
from sympy.core.sympify import SympifyError, _sympify
from sympy.external.gmpy import SYMPY_INTS
from sympy.functions import conjugate, adjoint
from sympy.functions.special.tensor_functions import KroneckerDelta
from sympy.matrices.exceptions import NonSquareMatrixError
from sympy.matrices.kind import MatrixKind
from sympy.matrices.matrixbase import MatrixBase
from sympy.multipledispatch import dispatch
from sympy.utilities.misc import filldedent

def _sympifyit(arg, retval = (None,)):
    pass
# WARNING: Decompyle incomplete


class MatrixExpr(Expr):
    pass
# WARNING: Decompyle incomplete

_eval_is_eq = (lambda lhs, rhs: False)()
_eval_is_eq = (lambda lhs, rhs: if lhs.shape != rhs.shape:
Falseif (None - rhs).is_ZeroMatrix:
True)()

def get_postprocessor(cls):
    pass
# WARNING: Decompyle incomplete

Basic._constructor_postprocessor_mapping[MatrixExpr] = {
    'Mul': [
        get_postprocessor(Mul)],
    'Add': [
        get_postprocessor(Add)] }

def _matrix_derivative(expr, x, old_algorithm = (False,)):
    if isinstance(expr, MatrixBase) or isinstance(x, MatrixBase):
        old_algorithm = True
    if old_algorithm:
        return _matrix_derivative_old_algorithm(expr, x)
    convert_matrix_to_array = convert_matrix_to_array
    import sympy.tensor.array.expressions.from_matrix_to_array
    array_derive = array_derive
    import sympy.tensor.array.expressions.arrayexpr_derivatives
    convert_array_to_matrix = convert_array_to_matrix
    import sympy.tensor.array.expressions.from_array_to_matrix
    array_expr = convert_matrix_to_array(expr)
    diff_array_expr = array_derive(array_expr, x)
    diff_matrix_expr = convert_array_to_matrix(diff_array_expr)
    return diff_matrix_expr


def _matrix_derivative_old_algorithm(expr, x):
    pass
# WARNING: Decompyle incomplete


class MatrixElement(Expr):
    parent = property((lambda self: self.args[0]))
    i = property((lambda self: self.args[1]))
    j = property((lambda self: self.args[2]))
    _diff_wrt = True
    is_symbol = True
    is_commutative = True
    
    def __new__(cls, name, n, m):
        (n, m) = map(_sympify, (n, m))
        if isinstance(name, str):
            name = Symbol(name)
        elif isinstance(name, MatrixBase):
            if n.is_Integer and m.is_Integer:
                return name[(n, m)]
            name = None(name)
        else:
            name = _sympify(name)
            if not isinstance(name.kind, MatrixKind):
                raise TypeError('First argument of MatrixElement should be a matrix')
        if not getattr(name, 'valid_index', (lambda n, m: True))(n, m):
            raise IndexError('indices out of range')
        obj = Expr.__new__(cls, name, n, m)
        return obj

    symbol = (lambda self: self.args[0])()
    
    def doit(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    indices = (lambda self: self.args[1:])()
    
    def _eval_derivative(self, v):
        if not isinstance(v, MatrixElement):
            return self.parent.diff(v)[(self.i, self.j)]
        M = None.args[0]
        (m, n) = self.parent.shape
        if M == v.args[0]:
            return KroneckerDelta(self.args[1], v.args[1], (0, m - 1)) * KroneckerDelta(self.args[2], v.args[2], (0, n - 1))
        if None(M, Inverse):
            Sum = Sum
            import sympy.concrete.summations
            (i, j) = self.args[1:]
            (i1, i2) = symbols('z1, z2', cls = Dummy)
            Y = M.args[0]
            (r1, r2) = Y.shape
            return -Sum(M[(i, i1)] * Y[(i1, i2)].diff(v) * M[(i2, j)], (i1, 0, r1 - 1), (i2, 0, r2 - 1))
        if None.has(v.args[0]):
            return None
        return None.Zero



class MatrixSymbol(MatrixExpr):
    """Symbolic representation of a Matrix object

    Creates a SymPy Symbol to represent a Matrix. This matrix has a shape and
    can be included in Matrix Expressions

    Examples
    ========

    >>> from sympy import MatrixSymbol, Identity
    >>> A = MatrixSymbol('A', 3, 4) # A 3 by 4 Matrix
    >>> B = MatrixSymbol('B', 4, 3) # A 4 by 3 Matrix
    >>> A.shape
    (3, 4)
    >>> 2*A*B + Identity(3)
    I + 2*A*B
    """
    is_commutative = False
    is_symbol = True
    _diff_wrt = True
    
    def __new__(cls, name, n, m):
        m = _sympify(m)
        n = _sympify(n)
        cls._check_dim(m)
        cls._check_dim(n)
        if isinstance(name, str):
            name = Str(name)
        obj = Basic.__new__(cls, name, n, m)
        return obj

    shape = (lambda self: (self.args[1], self.args[2]))()
    name = (lambda self: self.args[0].name)()
    
    def _entry(self, i, j, **kwargs):
        return MatrixElement(self, i, j)

    free_symbols = (lambda self: {
self})()
    
    def _eval_simplify(self, **kwargs):
        return self

    
    def _eval_derivative(self, x):
        return ZeroMatrix(self.shape[0], self.shape[1])

    
    def _eval_derivative_matrix_lines(self, x):
        if self != x:
            first = ZeroMatrix(x.shape[0], self.shape[0]) if self.shape[0] != 1 else S.Zero
            second = ZeroMatrix(x.shape[1], self.shape[1]) if self.shape[1] != 1 else S.Zero
            return [
                _LeftRightArgs([
                    first,
                    second])]
        first = Identity(self.shape[0]) if None.shape[0] != 1 else S.One
        second = Identity(self.shape[1]) if self.shape[1] != 1 else S.One
        return [
            _LeftRightArgs([
                first,
                second])]



def matrix_symbols(expr):
    return expr.free_symbols()


class _LeftRightArgs:
    '''
    Helper class to compute matrix derivatives.

    The logic: when an expression is derived by a matrix `X_{mn}`, two lines of
    matrix multiplications are created: the one contracted to `m` (first line),
    and the one contracted to `n` (second line).

    Transposition flips the side by which new matrices are connected to the
    lines.

    The trace connects the end of the two lines.
    '''
    
    def __init__(self, lines, higher = (S.One,)):
        self._lines = list(lines)
        self._first_pointer_parent = self._lines
        self._first_pointer_index = 0
        self._first_line_index = 0
        self._second_pointer_parent = self._lines
        self._second_pointer_index = 1
        self._second_line_index = 1
        self.higher = higher

    first_pointer = (lambda self: self._first_pointer_parent[self._first_pointer_index])()
    first_pointer = (lambda self, value: self._first_pointer_parent[self._first_pointer_index] = value)()
    second_pointer = (lambda self: self._second_pointer_parent[self._second_pointer_index])()
    second_pointer = (lambda self, value: self._second_pointer_parent[self._second_pointer_index] = value)()
    
    def __repr__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def transpose(self):
        self._first_pointer_parent, self._second_pointer_parent = self._second_pointer_parent, self._first_pointer_parent
        self._first_pointer_index, self._second_pointer_index = self._second_pointer_index, self._first_pointer_index
        self._first_line_index, self._second_line_index = self._second_line_index, self._first_line_index
        return self

    _build = (lambda expr: if isinstance(expr, ExprBuilder):
expr.build()# WARNING: Decompyle incomplete
)()
    
    def build(self):
        pass
    # WARNING: Decompyle incomplete

    
    def matrix_form(self):
        if self.first != 1 and self.higher != 1:
            raise ValueError('higher dimensional array cannot be represented')
        
        def _get_shape(elem):
            if isinstance(elem, MatrixExpr):
                return elem.shape

        if _get_shape(self.first)[1] != _get_shape(self.second)[1]:
            if _get_shape(self.second) == (1, 1):
                return self.first * self.second[(0, 0)]
            if _get_shape(self.first) == (1, 1):
                return self.first[(1, 1)] * self.second.T
            raise None('incompatible shapes')
        if self.first != 1:
            return self.first * self.second.T
        return None.higher

    
    def rank(self):
        '''
        Number of dimensions different from trivial (warning: not related to
        matrix rank).
        '''
        rank = 0
        if self.first != 1:
            sum += (lambda .0: pass# WARNING: Decompyle incomplete
)(self.first.shape())
        if self.second != 1:
            sum += (lambda .0: pass# WARNING: Decompyle incomplete
)(self.second.shape())
        if self.higher != 1:
            rank += 2
        return rank

    
    def _multiply_pointer(self, pointer, other):
        ArrayTensorProduct = ArrayTensorProduct
        import tensor.array.expressions.array_expressions
        ArrayContraction = ArrayContraction
        import tensor.array.expressions.array_expressions
        subexpr = ExprBuilder(ArrayContraction, [
            ExprBuilder(ArrayTensorProduct, [
                pointer,
                other]),
            (1, 2)], validator = ArrayContraction._validate)
        return subexpr

    
    def append_first(self, other):
        pass

    
    def append_second(self, other):
        pass



def _make_matrix(x):
    ImmutableDenseMatrix = ImmutableDenseMatrix
    import sympy.matrices.immutable
    if isinstance(x, MatrixExpr):
        return x
    return ImmutableDenseMatrix([
        [
            x]])

from matmul import MatMul
from matadd import MatAdd
from matpow import MatPow
from transpose import Transpose
from inverse import Inverse
from special import ZeroMatrix, Identity
from determinant import Determinant
