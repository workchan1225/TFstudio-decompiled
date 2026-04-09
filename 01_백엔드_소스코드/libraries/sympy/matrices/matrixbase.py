# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: matrixbase.pyc (Python 3.11)

from collections import defaultdict
from collections.abc import Iterable
from inspect import isfunction
from functools import reduce
from sympy.assumptions.refine import refine
from sympy.core import SympifyError, Add
from sympy.core.basic import Atom, Basic
from sympy.core.kind import UndefinedKind
from sympy.core.numbers import Integer
from sympy.core.mod import Mod
from sympy.core.symbol import Symbol, Dummy
from sympy.core.sympify import sympify, _sympify
from sympy.core.function import diff
from sympy.polys import cancel
from sympy.functions.elementary.complexes import Abs, re, im
from sympy.printing import sstr
from sympy.functions.elementary.miscellaneous import Max, Min, sqrt
from sympy.functions.special.tensor_functions import KroneckerDelta, LeviCivita
from sympy.core.singleton import S
from sympy.printing.defaults import Printable
from sympy.printing.str import StrPrinter
from sympy.functions.elementary.exponential import exp, log
from sympy.functions.combinatorial.factorials import binomial, factorial
import mpmath as mp
from collections.abc import Callable
from sympy.utilities.iterables import reshape
from sympy.core.expr import Expr
from sympy.core.power import Pow
from sympy.core.symbol import uniquely_named_symbol
from utilities import _dotprodsimp, _simplify as _utilities_simplify
from sympy.polys.polytools import Poly
from sympy.utilities.iterables import flatten, is_sequence
from sympy.utilities.misc import as_int, filldedent
from sympy.core.decorators import call_highest_priority
from sympy.core.logic import fuzzy_and, FuzzyBool
from sympy.tensor.array import NDimArray
from sympy.utilities.iterables import NotIterable
from utilities import _get_intermediate_simp_bool
from kind import MatrixKind
from exceptions import MatrixError, ShapeError, NonSquareMatrixError, NonInvertibleMatrixError
from utilities import _iszero, _is_zero_after_expand_mul
from determinant import _find_reasonable_pivot, _find_reasonable_pivot_naive, _adjugate, _charpoly, _cofactor, _cofactor_matrix, _per, _det, _det_bareiss, _det_berkowitz, _det_bird, _det_laplace, _det_LU, _minor, _minor_submatrix
from reductions import _is_echelon, _echelon_form, _rank, _rref
from solvers import _diagonal_solve, _lower_triangular_solve, _upper_triangular_solve, _cholesky_solve, _LDLsolve, _LUsolve, _QRsolve, _gauss_jordan_solve, _pinv_solve, _cramer_solve, _solve, _solve_least_squares
from inverse import _pinv, _inv_ADJ, _inv_GE, _inv_LU, _inv_CH, _inv_LDL, _inv_QR, _inv, _inv_block
from subspaces import _columnspace, _nullspace, _rowspace, _orthogonalize
from eigen import _eigenvals, _eigenvects, _bidiagonalize, _bidiagonal_decomposition, _is_diagonalizable, _diagonalize, _is_positive_definite, _is_positive_semidefinite, _is_negative_definite, _is_negative_semidefinite, _is_indefinite, _jordan_form, _left_eigenvects, _singular_values
from decompositions import _rank_decomposition, _cholesky, _LDLdecomposition, _LUdecomposition, _LUdecomposition_Simple, _LUdecompositionFF, _singular_value_decomposition, _QRdecomposition, _upper_hessenberg_decomposition
from graph import _connected_components, _connected_components_decomposition, _strongly_connected_components, _strongly_connected_components_decomposition
__doctest_requires__ = {
    ('MatrixBase.is_indefinite', 'MatrixBase.is_positive_definite', 'MatrixBase.is_positive_semidefinite', 'MatrixBase.is_negative_definite', 'MatrixBase.is_negative_semidefinite'): [
        'matplotlib'] }

class MatrixBase(Printable):
    '''All common matrix operations including basic arithmetic, shaping,
    and special matrices like `zeros`, and `eye`.'''
    _op_priority = 10.01
    __array_priority__ = 11
    is_Matrix = True
    _class_priority = 3
    _sympify = staticmethod(sympify)
    zero = S.Zero
    one = S.One
    _diff_wrt = True
    rows = None
    cols = None
    _simplify = None
    _new = (lambda cls: raise NotImplementedError('Subclasses must implement this.'))()
    
    def __eq__(self, other):
        raise NotImplementedError('Subclasses must implement this.')

    
    def __getitem__(self, key):
        '''Implementations of __getitem__ should accept ints, in which
        case the matrix is indexed as a flat list, tuples (i,j) in which
        case the (i,j) entry is returned, slices, or mixed tuples (a,b)
        where a and b are any combination of slices and integers.'''
        raise NotImplementedError('Subclasses must implement this.')

    shape = (lambda self: (self.rows, self.cols))()
    
    def _eval_col_del(self, col):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_col_insert(self, pos, other):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_col_join(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_extract(self, rowsList, colsList):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_get_diag_blocks(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_row_del(self, row):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_row_insert(self, pos, other):
        entries = list(self)
        insert_pos = pos * self.cols
        entries[insert_pos:insert_pos] = list(other)
        return self._new(self.rows + other.rows, self.cols, entries)

    
    def _eval_row_join(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_tolist(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_todok(self):
        dok = { }
        (rows, cols) = self.shape
        for i in range(rows):
            for j in range(cols):
                val = self[(i, j)]
                if val != self.zero:
                    dok[(i, j)] = val
                return dok

    _eval_from_dok = (lambda cls, rows, cols, dok: out_flat = [
cls.zero] * rows * colsfor i, j in dok.items():
val = Noneout_flat[i * cols + j] = valcls._new(rows, cols, out_flat))()
    
    def _eval_vec(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_vech(self, diagonal):
        c = self.cols
        v = []
        if diagonal:
            for j in range(c):
                for i in range(j, c):
                    v.append(self[(i, j)])
                for j in range(c):
                    for i in range(j + 1, c):
                        v.append(self[(i, j)])
                        return self._new(len(v), 1, v)

    
    def col_del(self, col):
        '''Delete the specified column.'''
        if col < 0:
            col += self.cols
        if not  <= 0, col or 0, col < self.cols:
            pass
        
        raise IndexError('Column {} is out of range.'.format(col))
        return self._eval_col_del(col)

    
    def col_insert(self, pos, other):
        '''Insert one or more columns at the given column position.

        Examples
        ========

        >>> from sympy import zeros, ones
        >>> M = zeros(3)
        >>> V = ones(3, 1)
        >>> M.col_insert(1, V)
        Matrix([
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]])

        See Also
        ========

        col
        row_insert
        '''
        if not self:
            return type(self)(other)
        pos = None(pos)
        if pos < 0:
            pos = self.cols + pos
        if pos < 0:
            pos = 0
        elif pos > self.cols:
            pos = self.cols
        if self.rows != other.rows:
            raise ShapeError('The matrices have incompatible number of rows ({} and {})'.format(self.rows, other.rows))
        return self._eval_col_insert(pos, other)

    
    def col_join(self, other):
        """Concatenates two matrices along self's last and other's first row.

        Examples
        ========

        >>> from sympy import zeros, ones
        >>> M = zeros(3)
        >>> V = ones(1, 3)
        >>> M.col_join(V)
        Matrix([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [1, 1, 1]])

        See Also
        ========

        col
        row_join
        """
        if self.rows == 0 and self.cols != other.cols:
            return self._new(0, other.cols, []).col_join(other)
        if None.cols != other.cols:
            raise ShapeError('The matrices have incompatible number of columns ({} and {})'.format(self.cols, other.cols))
        return self._eval_col_join(other)

    
    def col(self, j):
        '''Elementary column selector.

        Examples
        ========

        >>> from sympy import eye
        >>> eye(2).col(0)
        Matrix([
        [1],
        [0]])

        See Also
        ========

        row
        col_del
        col_join
        col_insert
        '''
        return self[(:, j)]

    
    def extract(self, rowsList, colsList):
        '''Return a submatrix by specifying a list of rows and columns.
        Negative indices can be given. All indices must be in the range
        $-n \\le i < n$ where $n$ is the number of rows or columns.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(4, 3, range(12))
        >>> m
        Matrix([
        [0,  1,  2],
        [3,  4,  5],
        [6,  7,  8],
        [9, 10, 11]])
        >>> m.extract([0, 1, 3], [0, 1])
        Matrix([
        [0,  1],
        [3,  4],
        [9, 10]])

        Rows or columns can be repeated:

        >>> m.extract([0, 0, 1], [-1])
        Matrix([
        [2],
        [2],
        [5]])

        Every other row can be taken by using range to provide the indices:

        >>> m.extract(range(0, m.rows, 2), [-1])
        Matrix([
        [2],
        [8]])

        RowsList or colsList can also be a list of booleans, in which case
        the rows or columns corresponding to the True values will be selected:

        >>> m.extract([0, 1, 2, 3], [True, False, True])
        Matrix([
        [0,  2],
        [3,  5],
        [6,  8],
        [9, 11]])
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_diag_blocks(self):
        '''Obtains the square sub-matrices on the main diagonal of a square matrix.

        Useful for inverting symbolic matrices or solving systems of
        linear equations which may be decoupled by having a block diagonal
        structure.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.abc import x, y, z
        >>> A = Matrix([[1, 3, 0, 0], [y, z*z, 0, 0], [0, 0, x, 0], [0, 0, 0, 0]])
        >>> a1, a2, a3 = A.get_diag_blocks()
        >>> a1
        Matrix([
        [1,    3],
        [y, z**2]])
        >>> a2
        Matrix([[x]])
        >>> a3
        Matrix([[0]])

        '''
        return self._eval_get_diag_blocks()

    hstack = (lambda cls: if len(args) == 0:
cls._new()kls = None(args[0])reduce(kls.row_join, args))()
    
    def reshape(self, rows, cols):
        '''Reshape the matrix. Total number of elements must remain the same.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(2, 3, lambda i, j: 1)
        >>> m
        Matrix([
        [1, 1, 1],
        [1, 1, 1]])
        >>> m.reshape(1, 6)
        Matrix([[1, 1, 1, 1, 1, 1]])
        >>> m.reshape(3, 2)
        Matrix([
        [1, 1],
        [1, 1],
        [1, 1]])

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def row_del(self, row):
        '''Delete the specified row.'''
        if row < 0:
            row += self.rows
        if not  <= 0, row or 0, row < self.rows:
            pass
        
        raise IndexError('Row {} is out of range.'.format(row))
        return self._eval_row_del(row)

    
    def row_insert(self, pos, other):
        '''Insert one or more rows at the given row position.

        Examples
        ========

        >>> from sympy import zeros, ones
        >>> M = zeros(3)
        >>> V = ones(1, 3)
        >>> M.row_insert(1, V)
        Matrix([
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0]])

        See Also
        ========

        row
        col_insert
        '''
        if not self:
            return self._new(other)
        pos = None(pos)
        if pos < 0:
            pos = self.rows + pos
        if pos < 0:
            pos = 0
        elif pos > self.rows:
            pos = self.rows
        if self.cols != other.cols:
            raise ShapeError('The matrices have incompatible number of columns ({} and {})'.format(self.cols, other.cols))
        return self._eval_row_insert(pos, other)

    
    def row_join(self, other):
        """Concatenates two matrices along self's last and rhs's first column

        Examples
        ========

        >>> from sympy import zeros, ones
        >>> M = zeros(3)
        >>> V = ones(3, 1)
        >>> M.row_join(V)
        Matrix([
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1]])

        See Also
        ========

        row
        col_join
        """
        if self.cols == 0 and self.rows != other.rows:
            return self._new(other.rows, 0, []).row_join(other)
        if None.rows != other.rows:
            raise ShapeError('The matrices have incompatible number of rows ({} and {})'.format(self.rows, other.rows))
        return self._eval_row_join(other)

    
    def diagonal(self, k = (0,)):
        '''Returns the kth diagonal of self. The main diagonal
        corresponds to `k=0`; diagonals above and below correspond to
        `k > 0` and `k < 0`, respectively. The values of `self[i, j]`
        for which `j - i = k`, are returned in order of increasing
        `i + j`, starting with `i + j = |k|`.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(3, 3, lambda i, j: j - i); m
        Matrix([
        [ 0,  1, 2],
        [-1,  0, 1],
        [-2, -1, 0]])
        >>> _.diagonal()
        Matrix([[0, 0, 0]])
        >>> m.diagonal(1)
        Matrix([[1, 1]])
        >>> m.diagonal(-2)
        Matrix([[-2]])

        Even though the diagonal is returned as a Matrix, the element
        retrieval can be done with a single index:

        >>> Matrix.diag(1, 2, 3).diagonal()[1]  # instead of [0, 1]
        2

        See Also
        ========

        diag
        '''
        rv = []
        k = as_int(k)
        r = 0 if k > 0 else -k
        c = 0 if r else k
        if r == self.rows or c == self.cols:
            pass
        else:
            rv.append(self[(r, c)])
            r += 1
            c += 1
        if not rv:
            raise ValueError(filldedent(f'''\n            The {k!s} diagonal is out of range [{1 - self.rows!s}, {self.cols - 1!s}]'''))
        return self._new(1, len(rv), rv)

    
    def row(self, i):
        '''Elementary row selector.

        Examples
        ========

        >>> from sympy import eye
        >>> eye(2).row(0)
        Matrix([[1, 0]])

        See Also
        ========

        col
        row_del
        row_join
        row_insert
        '''
        return self[(i, :)]

    
    def todok(self):
        '''Return the matrix as dictionary of keys.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix.eye(3)
        >>> M.todok()
        {(0, 0): 1, (1, 1): 1, (2, 2): 1}
        '''
        return self._eval_todok()

    from_dok = (lambda cls, rows, cols, dok: pass# WARNING: Decompyle incomplete
)()
    
    def tolist(self):
        '''Return the Matrix as a nested Python list.

        Examples
        ========

        >>> from sympy import Matrix, ones
        >>> m = Matrix(3, 3, range(9))
        >>> m
        Matrix([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]])
        >>> m.tolist()
        [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        >>> ones(3, 0).tolist()
        [[], [], []]

        When there are no rows then it will not be possible to tell how
        many columns were in the original matrix:

        >>> ones(0, 3).tolist()
        []

        '''
        if not self.rows:
            return []
        if not None.cols:
            return range(self.rows)()
        return None._eval_tolist()

    
    def todod(M):
        '''Returns matrix as dict of dicts containing non-zero elements of the Matrix

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix([[0, 1],[0, 3]])
        >>> A
        Matrix([
        [0, 1],
        [0, 3]])
        >>> A.todod()
        {0: {1: 1}, 1: {1: 3}}


        '''
        rowsdict = { }
        Mlol = M.tolist()
        for i, Mi in enumerate(Mlol):
            row = enumerate(Mi)()
            if row:
                rowsdict[i] = row
        return rowsdict

    
    def vec(self):
        '''Return the Matrix converted into a one column matrix by stacking columns

        Examples
        ========

        >>> from sympy import Matrix
        >>> m=Matrix([[1, 3], [2, 4]])
        >>> m
        Matrix([
        [1, 3],
        [2, 4]])
        >>> m.vec()
        Matrix([
        [1],
        [2],
        [3],
        [4]])

        See Also
        ========

        vech
        '''
        return self._eval_vec()

    
    def vech(self, diagonal, check_symmetry = (True, True)):
        '''Reshapes the matrix into a column vector by stacking the
        elements in the lower triangle.

        Parameters
        ==========

        diagonal : bool, optional
            If ``True``, it includes the diagonal elements.

        check_symmetry : bool, optional
            If ``True``, it checks whether the matrix is symmetric.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m=Matrix([[1, 2], [2, 3]])
        >>> m
        Matrix([
        [1, 2],
        [2, 3]])
        >>> m.vech()
        Matrix([
        [1],
        [2],
        [3]])
        >>> m.vech(diagonal=False)
        Matrix([[2]])

        Notes
        =====

        This should work for symmetric matrices and ``vech`` can
        represent symmetric matrices in vector form with less size than
        ``vec``.

        See Also
        ========

        vec
        '''
        if not self.is_square:
            raise NonSquareMatrixError
        if not check_symmetry and self.is_symmetric():
            raise ValueError('The matrix is not symmetric.')
        return self._eval_vech(diagonal)

    vstack = (lambda cls: if len(args) == 0:
cls._new()kls = None(args[0])reduce(kls.col_join, args))()
    _eval_diag = (lambda cls, rows, cols, diag_dict: pass# WARNING: Decompyle incomplete
)()
    _eval_eye = (lambda cls, rows, cols: vals = [
cls.zero] * rows * colsvals[::cols + 1] = [
cls.one] * min(rows, cols)cls._new(rows, cols, vals, copy = False))()
    _eval_jordan_block = (lambda cls = classmethod, size = classmethod, eigenvalue = classmethod, band = ('upper',): pass# WARNING: Decompyle incomplete
)()
    _eval_ones = (lambda cls, rows, cols: pass# WARNING: Decompyle incomplete
)()
    _eval_zeros = (lambda cls, rows, cols: cls._new(rows, cols, [
cls.zero] * rows * cols, copy = False))()
    _eval_wilkinson = (lambda cls, n: pass# WARNING: Decompyle incomplete
)()
    diag = (lambda kls = classmethod, *, strict: MatrixBase = MatrixBaseimport sympy.matrices.matrixbaseMatrix = Matriximport sympy.matrices.denseSparseMatrix = SparseMatriximport sympy.matricesklass = kwargs.get('cls', kls)if not unpack and len(args) == 1 and is_sequence(args[0]) and isinstance(args[0], MatrixBase):
args = args[0]diag_entries = defaultdict(int)rmax = 0cmax = 0# WARNING: Decompyle incomplete
)()
    eye = (lambda kls, rows, cols = (None,): pass# WARNING: Decompyle incomplete
)()
    jordan_block = (lambda kls = classmethod, size = (None, None), eigenvalue = {
        'band': 'upper' }, *, band, kwargs = None, klass = None: klass = kwargs.pop('cls', kls)eigenval = kwargs.get('eigenval', None)# WARNING: Decompyle incomplete
)()
    ones = (lambda kls, rows, cols = (None,): pass# WARNING: Decompyle incomplete
)()
    zeros = (lambda kls, rows, cols = (None,): pass# WARNING: Decompyle incomplete
)()
    companion = (lambda kls, poly: pass# WARNING: Decompyle incomplete
)()
    wilkinson = (lambda kls, n: klass = kwargs.get('cls', kls)n = as_int(n)klass._eval_wilkinson(n))()
    
    def _eval_iter_values(self):
        return self()

    
    def _eval_values(self):
        return list(self.iter_values())

    
    def _eval_iter_items(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_atoms(self, *types):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_free_symbols(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_has(self, *patterns):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_is_symbolic(self):
        return self.has(Symbol)

    
    def _eval_is_matrix_hermitian(self, simpfunc):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_is_zero_matrix(self):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.iter_values()())

    
    def _eval_is_Identity(self = classmethod):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_is_diagonal(self):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.iter_items()())

    
    def _eval_is_lower(self):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.iter_items()())

    
    def _eval_is_upper(self):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.iter_items()())

    
    def _eval_is_lower_hessenberg(self):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.iter_items()())

    
    def _eval_is_upper_hessenberg(self):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.iter_items()())

    
    def _eval_is_symmetric(self, simpfunc):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_is_anti_symmetric(self, simpfunc):
        pass
    # WARNING: Decompyle incomplete

    
    def _has_positive_diagonals(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _has_nonnegative_diagonals(self):
        pass
    # WARNING: Decompyle incomplete

    
    def atoms(self, *types):
        '''Returns the atoms that form the current object.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import Matrix
        >>> Matrix([[x]])
        Matrix([[x]])
        >>> _.atoms()
        {x}
        >>> Matrix([[x, y], [y, x]])
        Matrix([
        [x, y],
        [y, x]])
        >>> _.atoms()
        {x, y}
        '''
        types = (lambda .0: pass# WARNING: Decompyle incomplete
)(types())
        if not types:
            types = (Atom,)
    # WARNING: Decompyle incomplete

    free_symbols = (lambda self: self._eval_free_symbols())()
    
    def has(self, *patterns):
        '''Test whether any subexpression matches any of the patterns.

        Examples
        ========

        >>> from sympy import Matrix, SparseMatrix, Float
        >>> from sympy.abc import x, y
        >>> A = Matrix(((1, x), (0.2, 3)))
        >>> B = SparseMatrix(((1, x), (0.2, 3)))
        >>> A.has(x)
        True
        >>> A.has(y)
        False
        >>> A.has(Float)
        True
        >>> B.has(x)
        True
        >>> B.has(y)
        False
        >>> B.has(Float)
        True
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def is_anti_symmetric(self, simplify = (True,)):
        """Check if matrix M is an antisymmetric matrix,
        that is, M is a square matrix with all M[i, j] == -M[j, i].

        When ``simplify=True`` (default), the sum M[i, j] + M[j, i] is
        simplified before testing to see if it is zero. By default,
        the SymPy simplify function is used. To use a custom function
        set simplify to a function that accepts a single argument which
        returns a simplified expression. To skip simplification, set
        simplify to False but note that although this will be faster,
        it may induce false negatives.

        Examples
        ========

        >>> from sympy import Matrix, symbols
        >>> m = Matrix(2, 2, [0, 1, -1, 0])
        >>> m
        Matrix([
        [ 0, 1],
        [-1, 0]])
        >>> m.is_anti_symmetric()
        True
        >>> x, y = symbols('x y')
        >>> m = Matrix(2, 3, [0, 0, x, -y, 0, 0])
        >>> m
        Matrix([
        [ 0, 0, x],
        [-y, 0, 0]])
        >>> m.is_anti_symmetric()
        False

        >>> from sympy.abc import x, y
        >>> m = Matrix(3, 3, [0, x**2 + 2*x + 1, y,
        ...                   -(x + 1)**2, 0, x*y,
        ...                   -y, -x*y, 0])

        Simplification of matrix elements is done by default so even
        though two elements which should be equal and opposite would not
        pass an equality test, the matrix is still reported as
        anti-symmetric:

        >>> m[0, 1] == -m[1, 0]
        False
        >>> m.is_anti_symmetric()
        True

        If ``simplify=False`` is used for the case when a Matrix is already
        simplified, this will speed things up. Here, we see that without
        simplification the matrix does not appear anti-symmetric:

        >>> print(m.is_anti_symmetric(simplify=False))
        None

        But if the matrix were already expanded, then it would appear
        anti-symmetric and simplification in the is_anti_symmetric routine
        is not needed:

        >>> m = m.expand()
        >>> m.is_anti_symmetric(simplify=False)
        True
        """
        simpfunc = simplify
        if not isfunction(simplify):
            simpfunc = _utilities_simplify if simplify else (lambda x: x)
        if not self.is_square:
            return False
        return None._eval_is_anti_symmetric(simpfunc)

    
    def is_diagonal(self):
        '''Check if matrix is diagonal,
        that is matrix in which the entries outside the main diagonal are all zero.

        Examples
        ========

        >>> from sympy import Matrix, diag
        >>> m = Matrix(2, 2, [1, 0, 0, 2])
        >>> m
        Matrix([
        [1, 0],
        [0, 2]])
        >>> m.is_diagonal()
        True

        >>> m = Matrix(2, 2, [1, 1, 0, 2])
        >>> m
        Matrix([
        [1, 1],
        [0, 2]])
        >>> m.is_diagonal()
        False

        >>> m = diag(1, 2, 3)
        >>> m
        Matrix([
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 3]])
        >>> m.is_diagonal()
        True

        See Also
        ========

        is_lower
        is_upper
        sympy.matrices.matrixbase.MatrixBase.is_diagonalizable
        diagonalize
        '''
        return self._eval_is_diagonal()

    is_weakly_diagonally_dominant = (lambda self: pass# WARNING: Decompyle incomplete
)()
    is_strongly_diagonally_dominant = (lambda self: pass# WARNING: Decompyle incomplete
)()
    is_hermitian = (lambda self: if not self.is_square:
FalseNone._eval_is_matrix_hermitian(_utilities_simplify))()
    is_Identity = (lambda self = property: if not self.is_square:
FalseNone._eval_is_Identity())()
    is_lower_hessenberg = (lambda self: self._eval_is_lower_hessenberg())()
    is_lower = (lambda self: self._eval_is_lower())()
    is_square = (lambda self: self.rows == self.cols)()
    
    def is_symbolic(self):
        '''Checks if any elements contain Symbols.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.abc import x, y
        >>> M = Matrix([[x, y], [1, 0]])
        >>> M.is_symbolic()
        True

        '''
        return self._eval_is_symbolic()

    
    def is_symmetric(self, simplify = (True,)):
        """Check if matrix is symmetric matrix,
        that is square matrix and is equal to its transpose.

        By default, simplifications occur before testing symmetry.
        They can be skipped using 'simplify=False'; while speeding things a bit,
        this may however induce false negatives.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(2, 2, [0, 1, 1, 2])
        >>> m
        Matrix([
        [0, 1],
        [1, 2]])
        >>> m.is_symmetric()
        True

        >>> m = Matrix(2, 2, [0, 1, 2, 0])
        >>> m
        Matrix([
        [0, 1],
        [2, 0]])
        >>> m.is_symmetric()
        False

        >>> m = Matrix(2, 3, [0, 0, 0, 0, 0, 0])
        >>> m
        Matrix([
        [0, 0, 0],
        [0, 0, 0]])
        >>> m.is_symmetric()
        False

        >>> from sympy.abc import x, y
        >>> m = Matrix(3, 3, [1, x**2 + 2*x + 1, y, (x + 1)**2, 2, 0, y, 0, 3])
        >>> m
        Matrix([
        [         1, x**2 + 2*x + 1, y],
        [(x + 1)**2,              2, 0],
        [         y,              0, 3]])
        >>> m.is_symmetric()
        True

        If the matrix is already simplified, you may speed-up is_symmetric()
        test by using 'simplify=False'.

        >>> bool(m.is_symmetric(simplify=False))
        False
        >>> m1 = m.expand()
        >>> m1.is_symmetric(simplify=False)
        True
        """
        simpfunc = simplify
        if not isfunction(simplify):
            simpfunc = _utilities_simplify if simplify else (lambda x: x)
        if not self.is_square:
            return False
        return None._eval_is_symmetric(simpfunc)

    is_upper_hessenberg = (lambda self: self._eval_is_upper_hessenberg())()
    is_upper = (lambda self: self._eval_is_upper())()
    is_zero_matrix = (lambda self: self._eval_is_zero_matrix())()
    
    def values(self):
        '''Return non-zero values of self.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix([[0, 1], [2, 3]])
        >>> m.values()
        [1, 2, 3]

        See Also
        ========

        iter_values
        tolist
        flat
        '''
        return self._eval_values()

    
    def iter_values(self):
        '''
        Iterate over non-zero values of self.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix([[0, 1], [2, 3]])
        >>> list(m.iter_values())
        [1, 2, 3]

        See Also
        ========

        values
        '''
        return self._eval_iter_values()

    
    def iter_items(self):
        '''Iterate over indices and values of nonzero items.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix([[0, 1], [2, 3]])
        >>> list(m.iter_items())
        [((0, 1), 1), ((1, 0), 2), ((1, 1), 3)]

        See Also
        ========

        iter_values
        todok
        '''
        return self._eval_iter_items()

    
    def _eval_adjoint(self):
        return self.transpose().conjugate()

    
    def _eval_applyfunc(self, f):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_as_real_imag(self):
        return (self.applyfunc(re), self.applyfunc(im))

    
    def _eval_conjugate(self):
        return self.applyfunc((lambda x: x.conjugate()))

    
    def _eval_permute_cols(self, perm):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_permute_rows(self, perm):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_trace(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_transpose(self):
        pass
    # WARNING: Decompyle incomplete

    
    def adjoint(self):
        '''Conjugate transpose or Hermitian conjugation.'''
        return self._eval_adjoint()

    
    def applyfunc(self, f):
        '''Apply a function to each element of the matrix.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(2, 2, lambda i, j: i*2+j)
        >>> m
        Matrix([
        [0, 1],
        [2, 3]])
        >>> m.applyfunc(lambda i: 2*i)
        Matrix([
        [0, 2],
        [4, 6]])

        '''
        if not callable(f):
            raise TypeError('`f` must be callable.')
        return self._eval_applyfunc(f)

    
    def as_real_imag(self, deep = (True,), **hints):
        '''Returns a tuple containing the (real, imaginary) part of matrix.'''
        return self._eval_as_real_imag()

    
    def conjugate(self):
        '''Return the by-element conjugation.

        Examples
        ========

        >>> from sympy import SparseMatrix, I
        >>> a = SparseMatrix(((1, 2 + I), (3, 4), (I, -I)))
        >>> a
        Matrix([
        [1, 2 + I],
        [3,     4],
        [I,    -I]])
        >>> a.C
        Matrix([
        [ 1, 2 - I],
        [ 3,     4],
        [-I,     I]])

        See Also
        ========

        transpose: Matrix transposition
        H: Hermite conjugation
        sympy.matrices.matrixbase.MatrixBase.D: Dirac conjugation
        '''
        return self._eval_conjugate()

    
    def doit(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def evalf(self, n, subs, maxn, chop, strict, quad, verbose = (15, None, 100, False, False, None, False)):
        '''Apply evalf() to each element of self.'''
        pass
    # WARNING: Decompyle incomplete

    
    def expand(self, deep, modulus, power_base, power_exp, mul, log, multinomial, basic = (True, None, True, True, True, True, True, True), **hints):
        '''Apply core.function.expand to each entry of the matrix.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import Matrix
        >>> Matrix(1, 1, [x*(x+1)])
        Matrix([[x*(x + 1)]])
        >>> _.expand()
        Matrix([[x**2 + x]])

        '''
        pass
    # WARNING: Decompyle incomplete

    H = (lambda self: self.T.C)()
    
    def permute(self, perm, orientation, direction = ('rows', 'forward')):
        """Permute the rows or columns of a matrix by the given list of
        swaps.

        Parameters
        ==========

        perm : Permutation, list, or list of lists
            A representation for the permutation.

            If it is ``Permutation``, it is used directly with some
            resizing with respect to the matrix size.

            If it is specified as list of lists,
            (e.g., ``[[0, 1], [0, 2]]``), then the permutation is formed
            from applying the product of cycles. The direction how the
            cyclic product is applied is described in below.

            If it is specified as a list, the list should represent
            an array form of a permutation. (e.g., ``[1, 2, 0]``) which
            would would form the swapping function
            `0 \\mapsto 1, 1 \\mapsto 2, 2\\mapsto 0`.

        orientation : 'rows', 'cols'
            A flag to control whether to permute the rows or the columns

        direction : 'forward', 'backward'
            A flag to control whether to apply the permutations from
            the start of the list first, or from the back of the list
            first.

            For example, if the permutation specification is
            ``[[0, 1], [0, 2]]``,

            If the flag is set to ``'forward'``, the cycle would be
            formed as `0 \\mapsto 2, 2 \\mapsto 1, 1 \\mapsto 0`.

            If the flag is set to ``'backward'``, the cycle would be
            formed as `0 \\mapsto 1, 1 \\mapsto 2, 2 \\mapsto 0`.

            If the argument ``perm`` is not in a form of list of lists,
            this flag takes no effect.

        Examples
        ========

        >>> from sympy import eye
        >>> M = eye(3)
        >>> M.permute([[0, 1], [0, 2]], orientation='rows', direction='forward')
        Matrix([
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0]])

        >>> from sympy import eye
        >>> M = eye(3)
        >>> M.permute([[0, 1], [0, 2]], orientation='rows', direction='backward')
        Matrix([
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0]])

        Notes
        =====

        If a bijective function
        `\\sigma : \\mathbb{N}_0 \\rightarrow \\mathbb{N}_0` denotes the
        permutation.

        If the matrix `A` is the matrix to permute, represented as
        a horizontal or a vertical stack of vectors:

        .. math::
            A =
            \\begin{bmatrix}
            a_0 \\\\ a_1 \\\\ \\vdots \\\\ a_{n-1}
            \\end{bmatrix} =
            \\begin{bmatrix}
            \\alpha_0 & \\alpha_1 & \\cdots & \\alpha_{n-1}
            \\end{bmatrix}

        If the matrix `B` is the result, the permutation of matrix rows
        is defined as:

        .. math::
            B := \\begin{bmatrix}
            a_{\\sigma(0)} \\\\ a_{\\sigma(1)} \\\\ \\vdots \\\\ a_{\\sigma(n-1)}
            \\end{bmatrix}

        And the permutation of matrix columns is defined as:

        .. math::
            B := \\begin{bmatrix}
            \\alpha_{\\sigma(0)} & \\alpha_{\\sigma(1)} &
            \\cdots & \\alpha_{\\sigma(n-1)}
            \\end{bmatrix}
        """
        pass
    # WARNING: Decompyle incomplete

    
    def permute_cols(self, swaps, direction = ('forward',)):
        """Alias for
        ``self.permute(swaps, orientation='cols', direction=direction)``

        See Also
        ========

        permute
        """
        return self.permute(swaps, orientation = 'cols', direction = direction)

    
    def permute_rows(self, swaps, direction = ('forward',)):
        """Alias for
        ``self.permute(swaps, orientation='rows', direction=direction)``

        See Also
        ========

        permute
        """
        return self.permute(swaps, orientation = 'rows', direction = direction)

    
    def refine(self, assumptions = (True,)):
        """Apply refine to each element of the matrix.

        Examples
        ========

        >>> from sympy import Symbol, Matrix, Abs, sqrt, Q
        >>> x = Symbol('x')
        >>> Matrix([[Abs(x)**2, sqrt(x**2)],[sqrt(x**2), Abs(x)**2]])
        Matrix([
        [ Abs(x)**2, sqrt(x**2)],
        [sqrt(x**2),  Abs(x)**2]])
        >>> _.refine(Q.real(x))
        Matrix([
        [  x**2, Abs(x)],
        [Abs(x),   x**2]])

        """
        pass
    # WARNING: Decompyle incomplete

    
    def replace(self, F, G, map, simultaneous, exact = (False, True, None)):
        """Replaces Function F in Matrix entries with Function G.

        Examples
        ========

        >>> from sympy import symbols, Function, Matrix
        >>> F, G = symbols('F, G', cls=Function)
        >>> M = Matrix(2, 2, lambda i, j: F(i+j)) ; M
        Matrix([
        [F(0), F(1)],
        [F(1), F(2)]])
        >>> N = M.replace(F,G)
        >>> N
        Matrix([
        [G(0), G(1)],
        [G(1), G(2)]])
        """
        pass
    # WARNING: Decompyle incomplete

    
    def rot90(self, k = (1,)):
        """Rotates Matrix by 90 degrees

        Parameters
        ==========

        k : int
            Specifies how many times the matrix is rotated by 90 degrees
            (clockwise when positive, counter-clockwise when negative).

        Examples
        ========

        >>> from sympy import Matrix, symbols
        >>> A = Matrix(2, 2, symbols('a:d'))
        >>> A
        Matrix([
        [a, b],
        [c, d]])

        Rotating the matrix clockwise one time:

        >>> A.rot90(1)
        Matrix([
        [c, a],
        [d, b]])

        Rotating the matrix anticlockwise two times:

        >>> A.rot90(-2)
        Matrix([
        [d, c],
        [b, a]])
        """
        mod = k % 4
        if mod == 0:
            return self
        if None == 1:
            return self[(::-1, :)].T
        if None == 2:
            return self[(::-1, ::-1)]
        if None == 3:
            return self[(:, ::-1)].T

    
    def simplify(self, **kwargs):
        '''Apply simplify to each element of the matrix.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import SparseMatrix, sin, cos
        >>> SparseMatrix(1, 1, [x*sin(y)**2 + x*cos(y)**2])
        Matrix([[x*sin(y)**2 + x*cos(y)**2]])
        >>> _.simplify()
        Matrix([[x]])
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def subs(self, *args, **kwargs):
        '''Return a new matrix with subs applied to each entry.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import SparseMatrix, Matrix
        >>> SparseMatrix(1, 1, [x])
        Matrix([[x]])
        >>> _.subs(x, y)
        Matrix([[y]])
        >>> Matrix(_).subs(y, x)
        Matrix([[x]])
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def trace(self):
        '''
        Returns the trace of a square matrix i.e. the sum of the
        diagonal elements.

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix(2, 2, [1, 2, 3, 4])
        >>> A.trace()
        5

        '''
        if self.rows != self.cols:
            raise NonSquareMatrixError()
        return self._eval_trace()

    
    def transpose(self):
        '''
        Returns the transpose of the matrix.

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix(2, 2, [1, 2, 3, 4])
        >>> A.transpose()
        Matrix([
        [1, 3],
        [2, 4]])

        >>> from sympy import Matrix, I
        >>> m=Matrix(((1, 2+I), (3, 4)))
        >>> m
        Matrix([
        [1, 2 + I],
        [3,     4]])
        >>> m.transpose()
        Matrix([
        [    1, 3],
        [2 + I, 4]])
        >>> m.T == m.transpose()
        True

        See Also
        ========

        conjugate: By-element conjugation

        '''
        return self._eval_transpose()

    T = (lambda self: self.transpose())()
    C = (lambda self: self.conjugate())()
    
    def n(self, *args, **kwargs):
        '''Apply evalf() to each element of self.'''
        pass
    # WARNING: Decompyle incomplete

    
    def xreplace(self, rule):
        '''Return a new matrix with xreplace applied to each entry.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import SparseMatrix, Matrix
        >>> SparseMatrix(1, 1, [x])
        Matrix([[x]])
        >>> _.xreplace({x: y})
        Matrix([[y]])
        >>> Matrix(_).xreplace({y: x})
        Matrix([[x]])
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_simplify(self, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_trigsimp(self, **opts):
        pass
    # WARNING: Decompyle incomplete

    
    def upper_triangular(self, k = (0,)):
        '''Return the elements on and above the kth diagonal of a matrix.
        If k is not specified then simply returns upper-triangular portion
        of a matrix

        Examples
        ========

        >>> from sympy import ones
        >>> A = ones(4)
        >>> A.upper_triangular()
        Matrix([
        [1, 1, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 1, 1],
        [0, 0, 0, 1]])

        >>> A.upper_triangular(2)
        Matrix([
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]])

        >>> A.upper_triangular(-1)
        Matrix([
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 1, 1]])

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def lower_triangular(self, k = (0,)):
        '''Return the elements on and below the kth diagonal of a matrix.
        If k is not specified then simply returns lower-triangular portion
        of a matrix

        Examples
        ========

        >>> from sympy import ones
        >>> A = ones(4)
        >>> A.lower_triangular()
        Matrix([
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]])

        >>> A.lower_triangular(-2)
        Matrix([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 1, 0, 0]])

        >>> A.lower_triangular(1)
        Matrix([
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1]])

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_Abs(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_add(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_matrix_mul(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_matrix_mul_elementwise(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_matrix_rmul(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_pow_by_recursion(self, num):
        if num == 1:
            return self
        if None % 2 == 1:
            b = self._eval_pow_by_recursion(num - 1)
            a = self
        else:
            a = self._eval_pow_by_recursion(num // 2)
            b = self._eval_pow_by_recursion(num // 2)
        return a.multiply(b)

    
    def _eval_pow_by_cayley(self, exp):
        linrec_coeffs = linrec_coeffs
        import sympy.discrete.recurrences
        row = self.shape[0]
        p = self.charpoly()
        coeffs = -p.all_coeffs()[1:]
        coeffs = linrec_coeffs(coeffs, exp)
        new_mat = self.eye(row)
        ans = self.zeros(row)
        for i in range(row):
            ans += coeffs[i] * new_mat
            new_mat *= self
            return ans

    
    def _eval_pow_by_recursion_dotprodsimp(self, num, prevsimp = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_scalar_mul(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_scalar_rmul(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_Mod(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def __abs__(self):
        '''Returns a new matrix with entry-wise absolute values.'''
        return self._eval_Abs()

    __add__ = (lambda self, other: (other, T) = _coerce_operand(self, other)if T != 'is_matrix':
NotImplementedif None.shape != other.shape:
raise ShapeError(f'''Matrix size mismatch: {self.shape} + {other.shape}.''')b = othera = selfif a.__class__ != classof(a, b):
a = bb = aa._eval_add(b))()
    __truediv__ = (lambda self, other: self * (self.one / other))()
    __matmul__ = (lambda self, other: (self, other, T) = _unify_with_other(self, other)if T != 'is_matrix':
NotImplementedNone.__mul__(other))()
    
    def __mod__(self, other):
        pass
    # WARNING: Decompyle incomplete

    __mul__ = (lambda self, other: self.multiply(other))()
    
    def multiply(self, other, dotprodsimp = (None,)):
        '''Same as __mul__() but with optional simplification.

        Parameters
        ==========

        dotprodsimp : bool, optional
            Specifies whether intermediate term algebraic simplification is used
            during matrix multiplications to control expression blowup and thus
            speed up calculation. Default is off.
        '''
        isimpbool = _get_intermediate_simp_bool(False, dotprodsimp)
        (self, other, T) = _unify_with_other(self, other)
        if T == 'possible_scalar':
            
            try:
                return self._eval_scalar_mul(other)
            except TypeError:
                return 
                if T == 'is_matrix':
                    if self.shape[1] != other.shape[0]:
                        raise ShapeError(f'''Matrix size mismatch: {self.shape} * {other.shape}.''')
                    if isimpbool:
                        
                        def <listcomp>(.0):
                            return [ _dotprodsimp(e) for e in .0 ]

                        m.rows(m.cols, <listcomp>, m()) = m._new
                    return m
                return None


    
    def multiply_elementwise(self, other):
        '''Return the Hadamard product (elementwise product) of A and B

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix([[0, 1, 2], [3, 4, 5]])
        >>> B = Matrix([[1, 10, 100], [100, 10, 1]])
        >>> A.multiply_elementwise(B)
        Matrix([
        [  0, 10, 200],
        [300, 40,   5]])

        See Also
        ========

        sympy.matrices.matrixbase.MatrixBase.cross
        sympy.matrices.matrixbase.MatrixBase.dot
        multiply
        '''
        if self.shape != other.shape:
            raise ShapeError('Matrix shapes must agree {} != {}'.format(self.shape, other.shape))
        return self._eval_matrix_mul_elementwise(other)

    
    def __neg__(self):
        return self._eval_scalar_mul(-1)

    __pow__ = (lambda self, exp: self.pow(exp))()
    
    def pow(self, exp, method = (None,)):
        '''Return self**exp a scalar or symbol.

        Parameters
        ==========

        method : multiply, mulsimp, jordan, cayley
            If multiply then it returns exponentiation using recursion.
            If jordan then Jordan form exponentiation will be used.
            If cayley then the exponentiation is done using Cayley-Hamilton
            theorem.
            If mulsimp then the exponentiation is done using recursion
            with dotprodsimp. This specifies whether intermediate term
            algebraic simplification is used during naive matrix power to
            control expression blowup and thus speed up calculation.
            If None, then it heuristically decides which method to use.

        '''
        pass
    # WARNING: Decompyle incomplete

    __radd__ = (lambda self, other: self + other)()
    __rmatmul__ = (lambda self, other: (self, other, T) = _unify_with_other(self, other)if T != 'is_matrix':
NotImplementedNone.__rmul__(other))()
    __rmul__ = (lambda self, other: self.rmultiply(other))()
    
    def rmultiply(self, other, dotprodsimp = (None,)):
        '''Same as __rmul__() but with optional simplification.

        Parameters
        ==========

        dotprodsimp : bool, optional
            Specifies whether intermediate term algebraic simplification is used
            during matrix multiplications to control expression blowup and thus
            speed up calculation. Default is off.
        '''
        isimpbool = _get_intermediate_simp_bool(False, dotprodsimp)
        (self, other, T) = _unify_with_other(self, other)
        if T == 'possible_scalar':
            
            try:
                return self._eval_scalar_rmul(other)
            except TypeError:
                return 
                if T == 'is_matrix':
                    if self.shape[0] != other.shape[1]:
                        raise ShapeError('Matrix size mismatch.')
                    if isimpbool:
                        
                        def <listcomp>(.0):
                            return [ _dotprodsimp(e) for e in .0 ]

                        return m.rows(m.cols, <listcomp>, m())
                    return self._eval_matrix_rmul(other)
                return None


    __rsub__ = (lambda self, a: -self + a)()
    __sub__ = (lambda self, a: self + -a)()
    
    def _eval_det_bareiss(self, iszerofunc = (_is_zero_after_expand_mul,)):
        return _det_bareiss(self, iszerofunc = iszerofunc)

    
    def _eval_det_berkowitz(self):
        return _det_berkowitz(self)

    
    def _eval_det_lu(self, iszerofunc, simpfunc = (_iszero, None)):
        return _det_LU(self, iszerofunc = iszerofunc, simpfunc = simpfunc)

    
    def _eval_det_bird(self):
        return _det_bird(self)

    
    def _eval_det_laplace(self):
        return _det_laplace(self)

    
    def _eval_determinant(self):
        return _det(self)

    
    def adjugate(self, method = ('berkowitz',)):
        return _adjugate(self, method = method)

    
    def charpoly(self, x, simplify = ('lambda', _utilities_simplify)):
        return _charpoly(self, x = x, simplify = simplify)

    
    def cofactor(self, i, j, method = ('berkowitz',)):
        return _cofactor(self, i, j, method = method)

    
    def cofactor_matrix(self, method = ('berkowitz',)):
        return _cofactor_matrix(self, method = method)

    
    def det(self, method, iszerofunc = ('bareiss', None)):
        return _det(self, method = method, iszerofunc = iszerofunc)

    
    def per(self):
        return _per(self)

    
    def minor(self, i, j, method = ('berkowitz',)):
        return _minor(self, i, j, method = method)

    
    def minor_submatrix(self, i, j):
        return _minor_submatrix(self, i, j)

    _find_reasonable_pivot.__doc__ = _find_reasonable_pivot.__doc__
    _find_reasonable_pivot_naive.__doc__ = _find_reasonable_pivot_naive.__doc__
    _eval_det_bareiss.__doc__ = _det_bareiss.__doc__
    _eval_det_berkowitz.__doc__ = _det_berkowitz.__doc__
    _eval_det_bird.__doc__ = _det_bird.__doc__
    _eval_det_laplace.__doc__ = _det_laplace.__doc__
    _eval_det_lu.__doc__ = _det_LU.__doc__
    _eval_determinant.__doc__ = _det.__doc__
    adjugate.__doc__ = _adjugate.__doc__
    charpoly.__doc__ = _charpoly.__doc__
    cofactor.__doc__ = _cofactor.__doc__
    cofactor_matrix.__doc__ = _cofactor_matrix.__doc__
    det.__doc__ = _det.__doc__
    per.__doc__ = _per.__doc__
    minor.__doc__ = _minor.__doc__
    minor_submatrix.__doc__ = _minor_submatrix.__doc__
    
    def echelon_form(self, iszerofunc, simplify, with_pivots = (_iszero, False, False)):
        return _echelon_form(self, iszerofunc = iszerofunc, simplify = simplify, with_pivots = with_pivots)

    is_echelon = (lambda self: _is_echelon(self))()
    
    def rank(self, iszerofunc, simplify = (_iszero, False)):
        return _rank(self, iszerofunc = iszerofunc, simplify = simplify)

    
    def rref_rhs(self, rhs):
        """Return reduced row-echelon form of matrix, matrix showing
        rhs after reduction steps. ``rhs`` must have the same number
        of rows as ``self``.

        Examples
        ========

        >>> from sympy import Matrix, symbols
        >>> r1, r2 = symbols('r1 r2')
        >>> Matrix([[1, 1], [2, 1]]).rref_rhs(Matrix([r1, r2]))
        (Matrix([
        [1, 0],
        [0, 1]]), Matrix([
        [ -r1 + r2],
        [2*r1 - r2]]))
        """
        (r, _) = _rref(self.hstack(self, self.eye(self.rows), rhs))
        return (r[(:, :self.cols)], r[(:, -(rhs.cols):)])

    
    def rref(self, iszerofunc, simplify, pivots, normalize_last = (_iszero, False, True, True)):
        return _rref(self, iszerofunc = iszerofunc, simplify = simplify, pivots = pivots, normalize_last = normalize_last)

    echelon_form.__doc__ = _echelon_form.__doc__
    is_echelon.__doc__ = _is_echelon.__doc__
    rank.__doc__ = _rank.__doc__
    rref.__doc__ = _rref.__doc__
    
    def _normalize_op_args(self, op, col, k, col1, col2, error_str = ('col',)):
        '''Validate the arguments for a row/column operation.  ``error_str``
        can be one of "row" or "col" depending on the arguments being parsed.'''
        if op not in ('n->kn', 'n<->m', 'n->n+km'):
            raise ValueError("Unknown {} operation '{}'. Valid col operations are 'n->kn', 'n<->m', 'n->n+km'".format(error_str, op))
        self_cols = self.cols if error_str == 'col' else self.rows
    # WARNING: Decompyle incomplete

    
    def _eval_col_op_multiply_col_by_const(self, col, k):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_col_op_swap(self, col1, col2):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_col_op_add_multiple_to_other_col(self, col, k, col2):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_row_op_swap(self, row1, row2):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_row_op_multiply_row_by_const(self, row, k):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_row_op_add_multiple_to_other_row(self, row, k, row2):
        pass
    # WARNING: Decompyle incomplete

    
    def elementary_col_op(self, op, col, k, col1, col2 = ('n->kn', None, None, None, None)):
        '''Performs the elementary column operation `op`.

        `op` may be one of

            * ``"n->kn"`` (column n goes to k*n)
            * ``"n<->m"`` (swap column n and column m)
            * ``"n->n+km"`` (column n goes to column n + k*column m)

        Parameters
        ==========

        op : string; the elementary row operation
        col : the column to apply the column operation
        k : the multiple to apply in the column operation
        col1 : one column of a column swap
        col2 : second column of a column swap or column "m" in the column operation
               "n->n+km"
        '''
        (op, col, k, col1, col2) = self._normalize_op_args(op, col, k, col1, col2, 'col')
        if op == 'n->kn':
            return self._eval_col_op_multiply_col_by_const(col, k)
        if None == 'n<->m':
            return self._eval_col_op_swap(col1, col2)
        if None == 'n->n+km':
            return self._eval_col_op_add_multiple_to_other_col(col, k, col2)

    
    def elementary_row_op(self, op, row, k, row1, row2 = ('n->kn', None, None, None, None)):
        '''Performs the elementary row operation `op`.

        `op` may be one of

            * ``"n->kn"`` (row n goes to k*n)
            * ``"n<->m"`` (swap row n and row m)
            * ``"n->n+km"`` (row n goes to row n + k*row m)

        Parameters
        ==========

        op : string; the elementary row operation
        row : the row to apply the row operation
        k : the multiple to apply in the row operation
        row1 : one row of a row swap
        row2 : second row of a row swap or row "m" in the row operation
               "n->n+km"
        '''
        (op, row, k, row1, row2) = self._normalize_op_args(op, row, k, row1, row2, 'row')
        if op == 'n->kn':
            return self._eval_row_op_multiply_row_by_const(row, k)
        if None == 'n<->m':
            return self._eval_row_op_swap(row1, row2)
        if None == 'n->n+km':
            return self._eval_row_op_add_multiple_to_other_row(row, k, row2)

    
    def columnspace(self, simplify = (False,)):
        return _columnspace(self, simplify = simplify)

    
    def nullspace(self, simplify, iszerofunc = (False, _iszero)):
        return _nullspace(self, simplify = simplify, iszerofunc = iszerofunc)

    
    def rowspace(self, simplify = (False,)):
        return _rowspace(self, simplify = simplify)

    
    def orthogonalize(cls, *vecs, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    columnspace.__doc__ = _columnspace.__doc__
    nullspace.__doc__ = _nullspace.__doc__
    rowspace.__doc__ = _rowspace.__doc__
    orthogonalize.__doc__ = _orthogonalize.__doc__
    orthogonalize = classmethod(orthogonalize)
    
    def eigenvals(self, error_when_incomplete = (True,), **flags):
        pass
    # WARNING: Decompyle incomplete

    
    def eigenvects(self, error_when_incomplete, iszerofunc = (True, _iszero), **flags):
        pass
    # WARNING: Decompyle incomplete

    
    def is_diagonalizable(self, reals_only = (False,), **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def diagonalize(self, reals_only, sort, normalize = (False, False, False)):
        return _diagonalize(self, reals_only = reals_only, sort = sort, normalize = normalize)

    
    def bidiagonalize(self, upper = (True,)):
        return _bidiagonalize(self, upper = upper)

    
    def bidiagonal_decomposition(self, upper = (True,)):
        return _bidiagonal_decomposition(self, upper = upper)

    is_positive_definite = (lambda self: _is_positive_definite(self))()
    is_positive_semidefinite = (lambda self: _is_positive_semidefinite(self))()
    is_negative_definite = (lambda self: _is_negative_definite(self))()
    is_negative_semidefinite = (lambda self: _is_negative_semidefinite(self))()
    is_indefinite = (lambda self: _is_indefinite(self))()
    
    def jordan_form(self, calc_transform = (True,), **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def left_eigenvects(self, **flags):
        pass
    # WARNING: Decompyle incomplete

    
    def singular_values(self):
        return _singular_values(self)

    eigenvals.__doc__ = _eigenvals.__doc__
    eigenvects.__doc__ = _eigenvects.__doc__
    is_diagonalizable.__doc__ = _is_diagonalizable.__doc__
    diagonalize.__doc__ = _diagonalize.__doc__
    is_positive_definite.__doc__ = _is_positive_definite.__doc__
    is_positive_semidefinite.__doc__ = _is_positive_semidefinite.__doc__
    is_negative_definite.__doc__ = _is_negative_definite.__doc__
    is_negative_semidefinite.__doc__ = _is_negative_semidefinite.__doc__
    is_indefinite.__doc__ = _is_indefinite.__doc__
    jordan_form.__doc__ = _jordan_form.__doc__
    left_eigenvects.__doc__ = _left_eigenvects.__doc__
    singular_values.__doc__ = _singular_values.__doc__
    bidiagonalize.__doc__ = _bidiagonalize.__doc__
    bidiagonal_decomposition.__doc__ = _bidiagonal_decomposition.__doc__
    
    def diff(self = property, *, evaluate, *args, **kwargs):
        '''Calculate the derivative of each element in the matrix.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.abc import x, y
        >>> M = Matrix([[x, y], [1, 0]])
        >>> M.diff(x)
        Matrix([
        [1, 0],
        [0, 0]])

        See Also
        ========

        integrate
        limit
        '''
        ArrayDerivative = ArrayDerivative
        import sympy.tensor.array.array_derivatives
    # WARNING: Decompyle incomplete

    
    def _eval_derivative(self, arg):
        pass
    # WARNING: Decompyle incomplete

    
    def integrate(self, *args, **kwargs):
        '''Integrate each element of the matrix.  ``args`` will
        be passed to the ``integrate`` function.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.abc import x, y
        >>> M = Matrix([[x, y], [1, 0]])
        >>> M.integrate((x, ))
        Matrix([
        [x**2/2, x*y],
        [     x,   0]])
        >>> M.integrate((x, 0, 2))
        Matrix([
        [2, 2*y],
        [2,   0]])

        See Also
        ========

        limit
        diff
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def jacobian(self, X):
        """Calculates the Jacobian matrix (derivative of a vector-valued function).

        Parameters
        ==========

        ``self`` : vector of expressions representing functions f_i(x_1, ..., x_n).
        X : set of x_i's in order, it can be a list or a Matrix

        Both ``self`` and X can be a row or a column matrix in any order
        (i.e., jacobian() should always work).

        Examples
        ========

        >>> from sympy import sin, cos, Matrix
        >>> from sympy.abc import rho, phi
        >>> X = Matrix([rho*cos(phi), rho*sin(phi), rho**2])
        >>> Y = Matrix([rho, phi])
        >>> X.jacobian(Y)
        Matrix([
        [cos(phi), -rho*sin(phi)],
        [sin(phi),  rho*cos(phi)],
        [   2*rho,             0]])
        >>> X = Matrix([rho*cos(phi), rho*sin(phi)])
        >>> X.jacobian(Y)
        Matrix([
        [cos(phi), -rho*sin(phi)],
        [sin(phi),  rho*cos(phi)]])

        See Also
        ========

        hessian
        wronskian
        """
        pass
    # WARNING: Decompyle incomplete

    
    def limit(self, *args):
        '''Calculate the limit of each element in the matrix.
        ``args`` will be passed to the ``limit`` function.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.abc import x, y
        >>> M = Matrix([[x, y], [1, 0]])
        >>> M.limit(x, 2)
        Matrix([
        [2, y],
        [1, 0]])

        See Also
        ========

        integrate
        diff
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def berkowitz_charpoly(self, x, simplify = (Dummy('lambda'), _utilities_simplify)):
        return self.charpoly(x = x)

    
    def berkowitz_det(self):
        '''Computes determinant using Berkowitz method.

        See Also
        ========

        det
        '''
        return self.det(method = 'berkowitz')

    
    def berkowitz_eigenvals(self, **flags):
        '''Computes eigenvalues of a Matrix using Berkowitz method.'''
        pass
    # WARNING: Decompyle incomplete

    
    def berkowitz_minors(self):
        '''Computes principal minors using Berkowitz method.'''
        minors = []
        sign = self.one
        for poly in self.berkowitz():
            minors.append(sign * poly[-1])
            sign = -sign
            return tuple(minors)

    
    def berkowitz(self):
        zeros = zeros
        import sympy.matrices
        berk = ((1,),)
        if not self:
            return berk
        if not None.is_square:
            raise NonSquareMatrixError()
        N = self.rows
        A = self
        transforms = [
            0] * (N - 1)
        for n in range(N, 1, -1):
            k = n - 1
            T = zeros(n + 1, n)
            C = A[(:k, k)]
            R = -A[(k, :k)]
            a = -A[(k, k)]
            A = A[(:k, :k)]
            items = [
                C]
            for i in range(0, n - 2):
                items.append(A * items[i])
                for i, B in enumerate(items):
                    items[i] = R * B[(0, 0)]
                    items = [
                        self.one,
                        a] + items
                    for i in range(n):
                        T[(i:, i)] = items[:(n - i) + 1]
                        transforms[k - 1] = T
                        polys = [
                            self._new([
                                self.one,
                                -A[(0, 0)]])]
                        for i, T in enumerate(transforms):
                            polys.append(T * polys[i])
                            return berk + tuple(map(tuple, polys))

    
    def cofactorMatrix(self, method = ('berkowitz',)):
        return self.cofactor_matrix(method = method)

    
    def det_bareis(self):
        return _det_bareiss(self)

    
    def det_LU_decomposition(self):
        '''Compute matrix determinant using LU decomposition.


        Note that this method fails if the LU decomposition itself
        fails. In particular, if the matrix has no inverse this method
        will fail.

        TODO: Implement algorithm for sparse matrices (SFF),
        http://www.eecis.udel.edu/~saunders/papers/sffge/it5.ps.

        See Also
        ========


        det
        berkowitz_det
        '''
        return self.det(method = 'lu')

    
    def jordan_cell(self, eigenval, n):
        return self.jordan_block(size = n, eigenvalue = eigenval)

    
    def jordan_cells(self, calc_transformation = (True,)):
        (P, J) = self.jordan_form()
        return (P, J.get_diag_blocks())

    
    def minorEntry(self, i, j, method = ('berkowitz',)):
        return self.minor(i, j, method = method)

    
    def minorMatrix(self, i, j):
        return self.minor_submatrix(i, j)

    
    def permuteBkwd(self, perm):
        '''Permute the rows of the matrix with the given permutation in reverse.'''
        return self.permute_rows(perm, direction = 'backward')

    
    def permuteFwd(self, perm):
        '''Permute the rows of the matrix with the given permutation.'''
        return self.permute_rows(perm, direction = 'forward')

    kind = (lambda self = property: elem_kinds = self.flat()()MatrixKind(elemkind))()
    
    def flat(self):
        '''
        Returns a flat list of all elements in the matrix.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix([[0, 2], [3, 4]])
        >>> m.flat()
        [0, 2, 3, 4]

        See Also
        ========

        tolist
        values
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __array__(self, dtype, copy = (object, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def __len__(self):
        '''Return the number of elements of ``self``.

        Implemented mainly so bool(Matrix()) == False.
        '''
        return self.rows * self.cols

    
    def _matrix_pow_by_jordan_blocks(self, num):
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        if S.Zero in self.shape:
            return f'''Matrix({self.rows!s}, {self.cols!s}, [])'''
        return None % str(self.tolist())

    
    def _format_str(self, printer = (None,)):
        if not printer:
            printer = StrPrinter()
        if S.Zero in self.shape:
            return f'''Matrix({self.rows!s}, {self.cols!s}, [])'''
        if None.rows == 1:
            return 'Matrix([%s])' % self.table(printer, rowsep = ',\n')
        return None % self.table(printer, rowsep = ',\n')

    irregular = (lambda cls, ntop: pass# WARNING: Decompyle incomplete
)()
    _handle_ndarray = (lambda cls, arg: pass# WARNING: Decompyle incomplete
)()
    _handle_creation_inputs = (lambda cls: pass# WARNING: Decompyle incomplete
)()
    
    def _setitem(self, key, value):
        '''Helper to set value at location given by key.

        Examples
        ========

        >>> from sympy import Matrix, I, zeros, ones
        >>> m = Matrix(((1, 2+I), (3, 4)))
        >>> m
        Matrix([
        [1, 2 + I],
        [3,     4]])
        >>> m[1, 0] = 9
        >>> m
        Matrix([
        [1, 2 + I],
        [9,     4]])
        >>> m[1, 0] = [[0, 1]]

        To replace row r you assign to position r*m where m
        is the number of columns:

        >>> M = zeros(4)
        >>> m = M.cols
        >>> M[3*m] = ones(1, m)*2; M
        Matrix([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [2, 2, 2, 2]])

        And to replace column c you can assign to position c:

        >>> M[2] = ones(m, 1)*4; M
        Matrix([
        [0, 0, 4, 0],
        [0, 0, 4, 0],
        [0, 0, 4, 0],
        [2, 2, 4, 2]])
        '''
        Matrix = Matrix
        import dense
        is_slice = isinstance(key, slice)
        (i, j) = self.key2ij(key)
        key = self.key2ij(key)
        is_mat = isinstance(value, MatrixBase)
        if isinstance(i, slice) or isinstance(j, slice):
            if is_mat:
                self.copyin_matrix(key, value)
                return None
            if None(value, Expr) and is_sequence(value):
                self.copyin_list(key, value)
                return None
            raise None('unexpected value: %s' % value)
        if is_mat and isinstance(value, Basic) and is_sequence(value):
            value = Matrix(value)
            is_mat = True
    # WARNING: Decompyle incomplete

    
    def add(self, b):
        '''Return self + b.'''
        return self + b

    
    def condition_number(self):
        '''Returns the condition number of a matrix.

        This is the maximum singular value divided by the minimum singular value

        Examples
        ========

        >>> from sympy import Matrix, S
        >>> A = Matrix([[1, 0, 0], [0, 10, 0], [0, 0, S.One/10]])
        >>> A.condition_number()
        100

        See Also
        ========

        singular_values
        '''
        if not self:
            return self.zero
        singularvalues = None.singular_values()
    # WARNING: Decompyle incomplete

    
    def copy(self):
        '''
        Returns the copy of a matrix.

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix(2, 2, [1, 2, 3, 4])
        >>> A.copy()
        Matrix([
        [1, 2],
        [3, 4]])

        '''
        return self._new(self.rows, self.cols, self.flat())

    
    def cross(self, b):
        '''
        Return the cross product of ``self`` and ``b`` relaxing the condition
        of compatible dimensions: if each has 3 elements, a matrix of the
        same type and shape as ``self`` will be returned. If ``b`` has the same
        shape as ``self`` then common identities for the cross product (like
        `a \\times b = - b \\times a`) will hold.

        Parameters
        ==========
            b : 3x1 or 1x3 Matrix

        See Also
        ========

        dot
        hat
        vee
        multiply
        multiply_elementwise
        '''
        MatrixExpr = MatrixExpr
        import sympy.matrices.expressions.matexpr
        if not isinstance(b, (MatrixBase, MatrixExpr)):
            raise TypeError('{} must be a Matrix, not {}.'.format(b, type(b)))
        if not  == self.rows * self.cols, b.rows * b.cols or self.rows * self.cols, b.rows * b.cols == 3:
            pass
        
        raise ShapeError(f'''Dimensions incorrect for cross product: {(self.rows, self.cols)!s} x {(b.rows, b.cols)!s}''')
        return self._new(self.rows, self.cols, (self[1] * b[2] - self[2] * b[1], self[2] * b[0] - self[0] * b[2], self[0] * b[1] - self[1] * b[0]))

    
    def hat(self):
        '''
        Return the skew-symmetric matrix representing the cross product,
        so that ``self.hat() * b`` is equivalent to  ``self.cross(b)``.

        Examples
        ========

        Calling ``hat`` creates a skew-symmetric 3x3 Matrix from a 3x1 Matrix:

        >>> from sympy import Matrix
        >>> a = Matrix([1, 2, 3])
        >>> a.hat()
        Matrix([
        [ 0, -3,  2],
        [ 3,  0, -1],
        [-2,  1,  0]])

        Multiplying it with another 3x1 Matrix calculates the cross product:

        >>> b = Matrix([3, 2, 1])
        >>> a.hat() * b
        Matrix([
        [-4],
        [ 8],
        [-4]])

        Which is equivalent to calling the ``cross`` method:

        >>> a.cross(b)
        Matrix([
        [-4],
        [ 8],
        [-4]])

        See Also
        ========

        dot
        cross
        vee
        multiply
        multiply_elementwise
        '''
        if self.shape != (3, 1):
            raise ShapeError('Dimensions incorrect, expected (3, 1), got ' + str(self.shape))
        (x, y, z) = self
        return self._new(3, 3, (0, -z, y, z, 0, -x, -y, x, 0))

    
    def vee(self):
        """
        Return a 3x1 vector from a skew-symmetric matrix representing the cross product,
        so that ``self * b`` is equivalent to  ``self.vee().cross(b)``.

        Examples
        ========

        Calling ``vee`` creates a vector from a skew-symmetric Matrix:

        >>> from sympy import Matrix
        >>> A = Matrix([[0, -3, 2], [3, 0, -1], [-2, 1, 0]])
        >>> a = A.vee()
        >>> a
        Matrix([
        [1],
        [2],
        [3]])

        Calculating the matrix product of the original matrix with a vector
        is equivalent to a cross product:

        >>> b = Matrix([3, 2, 1])
        >>> A * b
        Matrix([
        [-4],
        [ 8],
        [-4]])

        >>> a.cross(b)
        Matrix([
        [-4],
        [ 8],
        [-4]])

        ``vee`` can also be used to retrieve angular velocity expressions.
        Defining a rotation matrix:

        >>> from sympy import rot_ccw_axis3, trigsimp
        >>> from sympy.physics.mechanics import dynamicsymbols
        >>> theta = dynamicsymbols('theta')
        >>> R = rot_ccw_axis3(theta)
        >>> R
        Matrix([
        [cos(theta(t)), -sin(theta(t)), 0],
        [sin(theta(t)),  cos(theta(t)), 0],
        [            0,              0, 1]])

        We can retrive the angular velocity:

        >>> Omega = R.T * R.diff()
        >>> Omega = trigsimp(Omega)
        >>> Omega.vee()
        Matrix([
        [                      0],
        [                      0],
        [Derivative(theta(t), t)]])

        See Also
        ========

        dot
        cross
        hat
        multiply
        multiply_elementwise
        """
        if self.shape != (3, 3):
            raise ShapeError('Dimensions incorrect, expected (3, 3), got ' + str(self.shape))
        if not self.is_anti_symmetric():
            raise ValueError('Matrix is not skew-symmetric')
        return self._new(3, 1, (self[(2, 1)], self[(0, 2)], self[(1, 0)]))

    D = (lambda self: mgamma = mgammaimport sympy.physics.matricesif self.rows != 4:
raise AttributeErrorself.H * mgamma(0))()
    
    def dot(self, b, hermitian, conjugate_convention = (None, None)):
        '''Return the dot or inner product of two vectors of equal length.
        Here ``self`` must be a ``Matrix`` of size 1 x n or n x 1, and ``b``
        must be either a matrix of size 1 x n, n x 1, or a list/tuple of length n.
        A scalar is returned.

        By default, ``dot`` does not conjugate ``self`` or ``b``, even if there are
        complex entries. Set ``hermitian=True`` (and optionally a ``conjugate_convention``)
        to compute the hermitian inner product.

        Possible kwargs are ``hermitian`` and ``conjugate_convention``.

        If ``conjugate_convention`` is ``"left"``, ``"math"`` or ``"maths"``,
        the conjugate of the first vector (``self``) is used.  If ``"right"``
        or ``"physics"`` is specified, the conjugate of the second vector ``b`` is used.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> v = Matrix([1, 1, 1])
        >>> M.row(0).dot(v)
        6
        >>> M.col(0).dot(v)
        12
        >>> v = [3, 2, 1]
        >>> M.row(0).dot(v)
        10

        >>> from sympy import I
        >>> q = Matrix([1*I, 1*I, 1*I])
        >>> q.dot(q, hermitian=False)
        -3

        >>> q.dot(q, hermitian=True)
        3

        >>> q1 = Matrix([1, 1, 1*I])
        >>> q.dot(q1, hermitian=True, conjugate_convention="maths")
        1 - 2*I
        >>> q.dot(q1, hermitian=True, conjugate_convention="physics")
        1 + 2*I


        See Also
        ========

        cross
        multiply
        multiply_elementwise
        '''
        Matrix = Matrix
        import dense
        if not isinstance(b, MatrixBase):
            if is_sequence(b):
                if len(b) != self.cols and len(b) != self.rows:
                    raise ShapeError(f'''Dimensions incorrect for dot product: {self.shape!s}, {len(b)!s}''')
                return self.dot(Matrix(b))
            raise None('`b` must be an ordered iterable or Matrix, not %s.' % type(b))
        if 1 not in self.shape or 1 not in b.shape:
            raise ShapeError
        if len(self) != len(b):
            raise ShapeError(f'''Dimensions incorrect for dot product: {self.shape!s}, {b.shape!s}''')
        mat = self
        n = len(mat)
        if mat.shape != (1, n):
            mat = mat.reshape(1, n)
        if b.shape != (n, 1):
            b = b.reshape(n, 1)
    # WARNING: Decompyle incomplete

    
    def dual(self):
        """Returns the dual of a matrix.

        A dual of a matrix is:

        ``(1/2)*levicivita(i, j, k, l)*M(k, l)`` summed over indices `k` and `l`

        Since the levicivita method is anti_symmetric for any pairwise
        exchange of indices, the dual of a symmetric matrix is the zero
        matrix. Strictly speaking the dual defined here assumes that the
        'matrix' `M` is a contravariant anti_symmetric second rank tensor,
        so that the dual is a covariant second rank tensor.

        """
        zeros = zeros
        import sympy.matrices
        n = self.rows
        M = self[(:, :)]
        work = zeros(n)
        if self.is_symmetric():
            return work
        for i in None(1, n):
            for j in range(1, n):
                acum = 0
                for k in range(1, n):
                    acum += LeviCivita(i, j, 0, k) * M[(0, k)]
                    work[(i, j)] = acum
                    work[(j, i)] = -acum
                    for l in range(1, n):
                        acum = 0
                        for a in range(1, n):
                            for b in range(1, n):
                                acum += LeviCivita(0, l, a, b) * M[(a, b)]
                                acum /= 2
                                work[(0, l)] = -acum
                                work[(l, 0)] = acum
                                return work

    
    def _eval_matrix_exp_jblock(self):
        """A helper function to compute an exponential of a Jordan block
        matrix

        Examples
        ========

        >>> from sympy import Symbol, Matrix
        >>> l = Symbol('lamda')

        A trivial example of 1*1 Jordan block:

        >>> m = Matrix.jordan_block(1, l)
        >>> m._eval_matrix_exp_jblock()
        Matrix([[exp(lamda)]])

        An example of 3*3 Jordan block:

        >>> m = Matrix.jordan_block(3, l)
        >>> m._eval_matrix_exp_jblock()
        Matrix([
        [exp(lamda), exp(lamda), exp(lamda)/2],
        [         0, exp(lamda),   exp(lamda)],
        [         0,          0,   exp(lamda)]])

        References
        ==========

        .. [1] https://en.wikipedia.org/wiki/Matrix_function#Jordan_decomposition
        """
        pass
    # WARNING: Decompyle incomplete

    
    def analytic_func(self, f, x):
        """
        Computes f(A) where A is a Square Matrix
        and f is an analytic function.

        Examples
        ========

        >>> from sympy import Symbol, Matrix, S, log

        >>> x = Symbol('x')
        >>> m = Matrix([[S(5)/4, S(3)/4], [S(3)/4, S(5)/4]])
        >>> f = log(x)
        >>> m.analytic_func(f, x)
        Matrix([
        [     0, log(2)],
        [log(2),      0]])

        Parameters
        ==========

        f : Expr
            Analytic Function
        x : Symbol
            parameter of f

        """
        x = _sympify(x)
        f = _sympify(f)
        if not self.is_square:
            raise NonSquareMatrixError
        if not x.is_symbol:
            raise ValueError('{} must be a symbol.'.format(x))
        if x not in f.free_symbols:
            raise ValueError('{} must be a parameter of {}.'.format(x, f))
        if x in self.free_symbols:
            raise ValueError('{} must not be a parameter of {}.'.format(x, self))
        eigen = self.eigenvals()
        max_mul = max(eigen.values())
        derivative = { }
        dd = f
    # WARNING: Decompyle incomplete

    
    def exp(self):
        """Return the exponential of a square matrix.

        Examples
        ========

        >>> from sympy import Symbol, Matrix

        >>> t = Symbol('t')
        >>> m = Matrix([[0, 1], [-1, 0]]) * t
        >>> m.exp()
        Matrix([
        [    exp(I*t)/2 + exp(-I*t)/2, -I*exp(I*t)/2 + I*exp(-I*t)/2],
        [I*exp(I*t)/2 - I*exp(-I*t)/2,      exp(I*t)/2 + exp(-I*t)/2]])
        """
        if not self.is_square:
            raise NonSquareMatrixError('Exponentiation is valid only for square matrices')
        
        try:
            (P, J) = self.jordan_form()
            cells = J.get_diag_blocks()
        except MatrixError:
            raise NotImplementedError('Exponentiation is implemented only for matrices for which the Jordan normal form can be computed')

        blocks = cells()
        diag = diag
        import sympy.matrices
    # WARNING: Decompyle incomplete

    
    def _eval_matrix_log_jblock(self):
        """Helper function to compute logarithm of a jordan block.

        Examples
        ========

        >>> from sympy import Symbol, Matrix
        >>> l = Symbol('lamda')

        A trivial example of 1*1 Jordan block:

        >>> m = Matrix.jordan_block(1, l)
        >>> m._eval_matrix_log_jblock()
        Matrix([[log(lamda)]])

        An example of 3*3 Jordan block:

        >>> m = Matrix.jordan_block(3, l)
        >>> m._eval_matrix_log_jblock()
        Matrix([
        [log(lamda),    1/lamda, -1/(2*lamda**2)],
        [         0, log(lamda),         1/lamda],
        [         0,          0,      log(lamda)]])
        """
        size = self.rows
        l = self[(0, 0)]
        if l.is_zero:
            raise MatrixError('Could not take logarithm or reciprocal for the given eigenvalue {}'.format(l))
        bands = {
            0: log(l) }
        for i in range(1, size):
            bands[i] = -(-l) ** (-i) / i
            banded = banded
            import sparsetools
            return self.__class__(banded(size, bands))

    
    def log(self, simplify = (cancel,)):
        '''Return the logarithm of a square matrix.

        Parameters
        ==========

        simplify : function, bool
            The function to simplify the result with.

            Default is ``cancel``, which is effective to reduce the
            expression growing for taking reciprocals and inverses for
            symbolic matrices.

        Examples
        ========

        >>> from sympy import S, Matrix

        Examples for positive-definite matrices:

        >>> m = Matrix([[1, 1], [0, 1]])
        >>> m.log()
        Matrix([
        [0, 1],
        [0, 0]])

        >>> m = Matrix([[S(5)/4, S(3)/4], [S(3)/4, S(5)/4]])
        >>> m.log()
        Matrix([
        [     0, log(2)],
        [log(2),      0]])

        Examples for non positive-definite matrices:

        >>> m = Matrix([[S(3)/4, S(5)/4], [S(5)/4, S(3)/4]])
        >>> m.log()
        Matrix([
        [         I*pi/2, log(2) - I*pi/2],
        [log(2) - I*pi/2,          I*pi/2]])

        >>> m = Matrix(
        ...     [[0, 0, 0, 1],
        ...      [0, 0, 1, 0],
        ...      [0, 1, 0, 0],
        ...      [1, 0, 0, 0]])
        >>> m.log()
        Matrix([
        [ I*pi/2,       0,       0, -I*pi/2],
        [      0,  I*pi/2, -I*pi/2,       0],
        [      0, -I*pi/2,  I*pi/2,       0],
        [-I*pi/2,       0,       0,  I*pi/2]])
        '''
        if not self.is_square:
            raise NonSquareMatrixError('Logarithm is valid only for square matrices')
        
        try:
            if simplify:
                (P, J) = simplify(self).jordan_form()
            else:
                (P, J) = self.jordan_form()
            cells = J.get_diag_blocks()
        except MatrixError:
            raise NotImplementedError('Logarithm is implemented only for matrices for which the Jordan normal form can be computed')

        blocks = cells()
        diag = diag
        import sympy.matrices
    # WARNING: Decompyle incomplete

    
    def is_nilpotent(self):
        '''Checks if a matrix is nilpotent.

        A matrix B is nilpotent if for some integer k, B**k is
        a zero matrix.

        Examples
        ========

        >>> from sympy import Matrix
        >>> a = Matrix([[0, 0, 0], [1, 0, 0], [1, 1, 0]])
        >>> a.is_nilpotent()
        True

        >>> a = Matrix([[1, 0, 1], [1, 0, 0], [1, 1, 0]])
        >>> a.is_nilpotent()
        False
        '''
        if not self:
            return True
        if not None.is_square:
            raise NonSquareMatrixError('Nilpotency is valid only for square matrices')
        x = uniquely_named_symbol('x', self, modify = (lambda s: '_' + s))
        p = self.charpoly(x)
        if p.args[0] == x ** self.rows:
            return True

    
    def key2bounds(self, keys):
        """Converts a key with potentially mixed types of keys (integer and slice)
        into a tuple of ranges and raises an error if any index is out of ``self``'s
        range.

        See Also
        ========

        key2ij
        """
        (islice, jslice) = keys()
        return (rlo, rhi, clo, chi)

    
    def key2ij(self, key):
        """Converts key into canonical form, converting integers or indexable
        items into valid integers for ``self``'s range or returning slices
        unchanged.

        See Also
        ========

        key2bounds
        """
        if is_sequence(key):
            if not len(key) == 2:
                raise TypeError('key must be a sequence of length 2')
            return zip(key, self.shape)()
        if None(key, slice):
            return key.indices(len(self))[:2]
        return None(a2idx(key, len(self)), self.cols)

    
    def normalized(self, iszerofunc = (_iszero,)):
        '''Return the normalized version of ``self``.

        Parameters
        ==========

        iszerofunc : Function, optional
            A function to determine whether ``self`` is a zero vector.
            The default ``_iszero`` tests to see if each element is
            exactly zero.

        Returns
        =======

        Matrix
            Normalized vector form of ``self``.
            It has the same length as a unit vector. However, a zero vector
            will be returned for a vector with norm 0.

        Raises
        ======

        ShapeError
            If the matrix is not in a vector form.

        See Also
        ========

        norm
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def norm(self, ord = (None,)):
        """Return the Norm of a Matrix or Vector.

        In the simplest case this is the geometric size of the vector
        Other norms can be specified by the ord parameter


        =====  ============================  ==========================
        ord    norm for matrices             norm for vectors
        =====  ============================  ==========================
        None   Frobenius norm                2-norm
        'fro'  Frobenius norm                - does not exist
        inf    maximum row sum               max(abs(x))
        -inf   --                            min(abs(x))
        1      maximum column sum            as below
        -1     --                            as below
        2      2-norm (largest sing. value)  as below
        -2     smallest singular value       as below
        other  - does not exist              sum(abs(x)**ord)**(1./ord)
        =====  ============================  ==========================

        Examples
        ========

        >>> from sympy import Matrix, Symbol, trigsimp, cos, sin, oo
        >>> x = Symbol('x', real=True)
        >>> v = Matrix([cos(x), sin(x)])
        >>> trigsimp( v.norm() )
        1
        >>> v.norm(10)
        (sin(x)**10 + cos(x)**10)**(1/10)
        >>> A = Matrix([[1, 1], [1, 1]])
        >>> A.norm(1) # maximum sum of absolute values of A is 2
        2
        >>> A.norm(2) # Spectral norm (max of |Ax|/|x| under 2-vector-norm)
        2
        >>> A.norm(-2) # Inverse spectral norm (smallest singular value)
        0
        >>> A.norm() # Frobenius Norm
        2
        >>> A.norm(oo) # Infinity Norm
        2
        >>> Matrix([1, -2]).norm(oo)
        2
        >>> Matrix([-1, 2]).norm(-oo)
        1

        See Also
        ========

        normalized
        """
        pass
    # WARNING: Decompyle incomplete

    
    def print_nonzero(self, symb = ('X',)):
        '''Shows location of non-zero entries for fast shape lookup.

        Examples
        ========

        >>> from sympy import Matrix, eye
        >>> m = Matrix(2, 3, lambda i, j: i*3+j)
        >>> m
        Matrix([
        [0, 1, 2],
        [3, 4, 5]])
        >>> m.print_nonzero()
        [ XX]
        [XXX]
        >>> m = eye(4)
        >>> m.print_nonzero("x")
        [x   ]
        [ x  ]
        [  x ]
        [   x]

        '''
        s = []
        for i in range(self.rows):
            line = []
            for j in range(self.cols):
                if self[(i, j)] == 0:
                    line.append(' ')
                    continue
                line.append(str(symb))
                s.append('[%s]' % ''.join(line))
                print('\n'.join(s))
                return None

    
    def project(self, v):
        '''Return the projection of ``self`` onto the line containing ``v``.

        Examples
        ========

        >>> from sympy import Matrix, S, sqrt
        >>> V = Matrix([sqrt(3)/2, S.Half])
        >>> x = Matrix([[1, 0]])
        >>> V.project(x)
        Matrix([[sqrt(3)/2, 0]])
        >>> V.project(-x)
        Matrix([[sqrt(3)/2, 0]])
        '''
        return v * (self.dot(v) / v.dot(v))

    
    def table(self, printer, rowstart, rowend, rowsep, colsep, align = ('[', ']', '\n', ', ', 'right')):
        """
        String form of Matrix as a table.

        ``printer`` is the printer to use for on the elements (generally
        something like StrPrinter())

        ``rowstart`` is the string used to start each row (by default '[').

        ``rowend`` is the string used to end each row (by default ']').

        ``rowsep`` is the string used to separate rows (by default a newline).

        ``colsep`` is the string used to separate columns (by default ', ').

        ``align`` defines how the elements are aligned. Must be one of 'left',
        'right', or 'center'.  You can also use '<', '>', and '^' to mean the
        same thing, respectively.

        This is used by the string printer for Matrix.

        Examples
        ========

        >>> from sympy import Matrix, StrPrinter
        >>> M = Matrix([[1, 2], [-33, 4]])
        >>> printer = StrPrinter()
        >>> M.table(printer)
        '[  1, 2]\\n[-33, 4]'
        >>> print(M.table(printer))
        [  1, 2]
        [-33, 4]
        >>> print(M.table(printer, rowsep=',\\n'))
        [  1, 2],
        [-33, 4]
        >>> print('[%s]' % M.table(printer, rowsep=',\\n'))
        [[  1, 2],
        [-33, 4]]
        >>> print(M.table(printer, colsep=' '))
        [  1 2]
        [-33 4]
        >>> print(M.table(printer, align='center'))
        [ 1 , 2]
        [-33, 4]
        >>> print(M.table(printer, rowstart='{', rowend='}'))
        {  1, 2}
        {-33, 4}
        """
        if S.Zero in self.shape:
            return '[]'
        res = None
        maxlen = [
            0] * self.cols
        for i in range(self.rows):
            res.append([])
            for j in range(self.cols):
                s = printer._print(self[(i, j)])
                res[-1].append(s)
                maxlen[j] = max(len(s), maxlen[j])
                align = {
                    'left': 'ljust',
                    'right': 'rjust',
                    'center': 'center',
                    '<': 'ljust',
                    '>': 'rjust',
                    '^': 'center' }[align]
                for i, row in enumerate(res):
                    for j, elem in enumerate(row):
                        row[j] = getattr(elem, align)(maxlen[j])
                        res[i] = rowstart + colsep.join(row) + rowend
                        return rowsep.join(res)

    
    def rank_decomposition(self, iszerofunc, simplify = (_iszero, False)):
        return _rank_decomposition(self, iszerofunc = iszerofunc, simplify = simplify)

    
    def cholesky(self, hermitian = (True,)):
        raise NotImplementedError('This function is implemented in DenseMatrix or SparseMatrix')

    
    def LDLdecomposition(self, hermitian = (True,)):
        raise NotImplementedError('This function is implemented in DenseMatrix or SparseMatrix')

    
    def LUdecomposition(self, iszerofunc, simpfunc, rankcheck = (_iszero, None, False)):
        return _LUdecomposition(self, iszerofunc = iszerofunc, simpfunc = simpfunc, rankcheck = rankcheck)

    
    def LUdecomposition_Simple(self, iszerofunc, simpfunc, rankcheck = (_iszero, None, False)):
        return _LUdecomposition_Simple(self, iszerofunc = iszerofunc, simpfunc = simpfunc, rankcheck = rankcheck)

    
    def LUdecompositionFF(self):
        return _LUdecompositionFF(self)

    
    def singular_value_decomposition(self):
        return _singular_value_decomposition(self)

    
    def QRdecomposition(self):
        return _QRdecomposition(self)

    
    def upper_hessenberg_decomposition(self):
        return _upper_hessenberg_decomposition(self)

    
    def diagonal_solve(self, rhs):
        return _diagonal_solve(self, rhs)

    
    def lower_triangular_solve(self, rhs):
        raise NotImplementedError('This function is implemented in DenseMatrix or SparseMatrix')

    
    def upper_triangular_solve(self, rhs):
        raise NotImplementedError('This function is implemented in DenseMatrix or SparseMatrix')

    
    def cholesky_solve(self, rhs):
        return _cholesky_solve(self, rhs)

    
    def LDLsolve(self, rhs):
        return _LDLsolve(self, rhs)

    
    def LUsolve(self, rhs, iszerofunc = (_iszero,)):
        return _LUsolve(self, rhs, iszerofunc = iszerofunc)

    
    def QRsolve(self, b):
        return _QRsolve(self, b)

    
    def gauss_jordan_solve(self, B, freevar = (False,)):
        return _gauss_jordan_solve(self, B, freevar = freevar)

    
    def pinv_solve(self, B, arbitrary_matrix = (None,)):
        return _pinv_solve(self, B, arbitrary_matrix = arbitrary_matrix)

    
    def cramer_solve(self, rhs, det_method = ('laplace',)):
        return _cramer_solve(self, rhs, det_method = det_method)

    
    def solve(self, rhs, method = ('GJ',)):
        return _solve(self, rhs, method = method)

    
    def solve_least_squares(self, rhs, method = ('CH',)):
        return _solve_least_squares(self, rhs, method = method)

    
    def pinv(self, method = ('RD',)):
        return _pinv(self, method = method)

    
    def inverse_ADJ(self, iszerofunc = (_iszero,)):
        return _inv_ADJ(self, iszerofunc = iszerofunc)

    
    def inverse_BLOCK(self, iszerofunc = (_iszero,)):
        return _inv_block(self, iszerofunc = iszerofunc)

    
    def inverse_GE(self, iszerofunc = (_iszero,)):
        return _inv_GE(self, iszerofunc = iszerofunc)

    
    def inverse_LU(self, iszerofunc = (_iszero,)):
        return _inv_LU(self, iszerofunc = iszerofunc)

    
    def inverse_CH(self, iszerofunc = (_iszero,)):
        return _inv_CH(self, iszerofunc = iszerofunc)

    
    def inverse_LDL(self, iszerofunc = (_iszero,)):
        return _inv_LDL(self, iszerofunc = iszerofunc)

    
    def inverse_QR(self, iszerofunc = (_iszero,)):
        return _inv_QR(self, iszerofunc = iszerofunc)

    
    def inv(self, method, iszerofunc, try_block_diag = (None, _iszero, False)):
        return _inv(self, method = method, iszerofunc = iszerofunc, try_block_diag = try_block_diag)

    
    def connected_components(self):
        return _connected_components(self)

    
    def connected_components_decomposition(self):
        return _connected_components_decomposition(self)

    
    def strongly_connected_components(self):
        return _strongly_connected_components(self)

    
    def strongly_connected_components_decomposition(self, lower = (True,)):
        return _strongly_connected_components_decomposition(self, lower = lower)

    _sage_ = Basic._sage_
    rank_decomposition.__doc__ = _rank_decomposition.__doc__
    cholesky.__doc__ = _cholesky.__doc__
    LDLdecomposition.__doc__ = _LDLdecomposition.__doc__
    LUdecomposition.__doc__ = _LUdecomposition.__doc__
    LUdecomposition_Simple.__doc__ = _LUdecomposition_Simple.__doc__
    LUdecompositionFF.__doc__ = _LUdecompositionFF.__doc__
    singular_value_decomposition.__doc__ = _singular_value_decomposition.__doc__
    QRdecomposition.__doc__ = _QRdecomposition.__doc__
    upper_hessenberg_decomposition.__doc__ = _upper_hessenberg_decomposition.__doc__
    diagonal_solve.__doc__ = _diagonal_solve.__doc__
    lower_triangular_solve.__doc__ = _lower_triangular_solve.__doc__
    upper_triangular_solve.__doc__ = _upper_triangular_solve.__doc__
    cholesky_solve.__doc__ = _cholesky_solve.__doc__
    LDLsolve.__doc__ = _LDLsolve.__doc__
    LUsolve.__doc__ = _LUsolve.__doc__
    QRsolve.__doc__ = _QRsolve.__doc__
    gauss_jordan_solve.__doc__ = _gauss_jordan_solve.__doc__
    pinv_solve.__doc__ = _pinv_solve.__doc__
    cramer_solve.__doc__ = _cramer_solve.__doc__
    solve.__doc__ = _solve.__doc__
    solve_least_squares.__doc__ = _solve_least_squares.__doc__
    pinv.__doc__ = _pinv.__doc__
    inverse_ADJ.__doc__ = _inv_ADJ.__doc__
    inverse_GE.__doc__ = _inv_GE.__doc__
    inverse_LU.__doc__ = _inv_LU.__doc__
    inverse_CH.__doc__ = _inv_CH.__doc__
    inverse_LDL.__doc__ = _inv_LDL.__doc__
    inverse_QR.__doc__ = _inv_QR.__doc__
    inverse_BLOCK.__doc__ = _inv_block.__doc__
    inv.__doc__ = _inv.__doc__
    connected_components.__doc__ = _connected_components.__doc__
    connected_components_decomposition.__doc__ = _connected_components_decomposition.__doc__
    strongly_connected_components.__doc__ = _strongly_connected_components.__doc__
    strongly_connected_components_decomposition.__doc__ = _strongly_connected_components_decomposition.__doc__


def _convert_matrix(typ, mat):
    '''Convert mat to a Matrix of type typ.'''
    MatrixBase = MatrixBase
    import sympy.matrices.matrixbase
# WARNING: Decompyle incomplete


def _has_matrix_shape(other):
    shape = getattr(other, 'shape', None)
# WARNING: Decompyle incomplete


def _has_rows_cols(other):
