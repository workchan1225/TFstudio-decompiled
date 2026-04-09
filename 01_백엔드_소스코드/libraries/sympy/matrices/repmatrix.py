# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: repmatrix.pyc (Python 3.11)

from collections import defaultdict
from operator import index as index_
from sympy.core.expr import Expr
from sympy.core.kind import Kind, NumberKind, UndefinedKind
from sympy.core.numbers import Integer, Rational
from sympy.core.sympify import _sympify, SympifyError
from sympy.core.singleton import S
from sympy.polys.domains import ZZ, QQ, GF, EXRAW
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.exceptions import DMNonInvertibleMatrixError
from sympy.polys.polyerrors import CoercionFailed
from sympy.utilities.exceptions import sympy_deprecation_warning
from sympy.utilities.iterables import is_sequence
from sympy.utilities.misc import filldedent, as_int
from exceptions import ShapeError, NonSquareMatrixError, NonInvertibleMatrixError
from matrixbase import classof, MatrixBase
from kind import MatrixKind

class RepMatrix(MatrixBase):
    _rep: DomainMatrix = 'Matrix implementation based on DomainMatrix as an internal representation.\n\n    The RepMatrix class is a superclass for Matrix, ImmutableMatrix,\n    SparseMatrix and ImmutableSparseMatrix which are the main usable matrix\n    classes in SymPy. Most methods on this class are simply forwarded to\n    DomainMatrix.\n    '
    
    def __eq__(self, other):
        if not isinstance(other, RepMatrix):
            
            try:
                other = _sympify(other)
            except SympifyError:
                return 

            if not isinstance(other, RepMatrix):
                return NotImplemented
            return None._rep.unify_eq(other._rep)

    
    def to_DM(self, domain = (None,), **kwargs):
        """Convert to a :class:`~.DomainMatrix`.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix([[1, 2], [3, 4]])
        >>> M.to_DM()
        DomainMatrix({0: {0: 1, 1: 2}, 1: {0: 3, 1: 4}}, (2, 2), ZZ)

        The :meth:`DomainMatrix.to_Matrix` method can be used to convert back:

        >>> M.to_DM().to_Matrix() == M
        True

        The domain can be given explicitly or otherwise it will be chosen by
        :func:`construct_domain`. Any keyword arguments (besides ``domain``)
        are passed to :func:`construct_domain`:

        >>> from sympy import QQ, symbols
        >>> x = symbols('x')
        >>> M = Matrix([[x, 1], [1, x]])
        >>> M
        Matrix([
        [x, 1],
        [1, x]])
        >>> M.to_DM().domain
        ZZ[x]
        >>> M.to_DM(field=True).domain
        ZZ(x)
        >>> M.to_DM(domain=QQ[x]).domain
        QQ[x]

        See Also
        ========

        DomainMatrix
        DomainMatrix.to_Matrix
        DomainMatrix.convert_to
        DomainMatrix.choose_domain
        construct_domain
        """
        pass
    # WARNING: Decompyle incomplete

    _unify_element_sympy = (lambda cls, rep, element: domain = rep.domainelement = _sympify(element)if domain != EXRAW:
if element.is_Integer:
new_domain = domainelif element.is_Rational:
new_domain = QQelse:
new_domain = EXRAWif new_domain != domain:
rep = rep.convert_to(new_domain)domain = new_domainif domain != EXRAW:
element = new_domain.from_sympy(element)if not domain == EXRAW and isinstance(element, Expr):
sympy_deprecation_warning('\n                non-Expr objects in a Matrix is deprecated. Matrix represents\n                a mathematical matrix. To represent a container of non-numeric\n                entities, Use a list of lists, TableForm, NumPy array, or some\n                other data structure instead.\n                ', deprecated_since_version = '1.9', active_deprecations_target = 'deprecated-non-expr-in-matrix', stacklevel = 4)(rep, element))()
    _dod_to_DomainMatrix = (lambda cls, rows, cols, dod, types: if not (lambda .0: pass# WARNING: Decompyle incomplete
)(types()):
            sympy_deprecation_warning('\n                non-Expr objects in a Matrix is deprecated. Matrix represents\n                a mathematical matrix. To represent a container of non-numeric\n                entities, Use a list of lists, TableForm, NumPy array, or some\n                other data structure instead.\n                ', deprecated_since_version = '1.9', active_deprecations_target = 'deprecated-non-expr-in-matrix', stacklevel = 6)
        rep = DomainMatrix(dod, (rows, cols), EXRAW)
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(types()):
            pass
        return rep
)()
    _flat_list_to_DomainMatrix = (lambda cls, rows, cols, flat_list: elements_dod = defaultdict(dict)for n, element in enumerate(flat_list):
if element != 0:
(i, j) = divmod(n, cols)elements_dod[i][j] = elementtypes = set(map(type, flat_list))rep = cls._dod_to_DomainMatrix(rows, cols, elements_dod, types)rep)()
    _smat_to_DomainMatrix = (lambda cls, rows, cols, smat: elements_dod = defaultdict(dict)for i, j in smat.items():
element = Noneif element != 0:
elements_dod[i][j] = elementtypes = set(map(type, smat.values()))rep = cls._dod_to_DomainMatrix(rows, cols, elements_dod, types)rep)()
    
    def flat(self):
        return self._rep.to_sympy().to_list_flat()

    
    def _eval_tolist(self):
        return self._rep.to_sympy().to_list()

    
    def _eval_todok(self):
        return self._rep.to_sympy().to_dok()

    _eval_from_dok = (lambda cls, rows, cols, dok: cls._fromrep(cls._smat_to_DomainMatrix(rows, cols, dok)))()
    
    def _eval_values(self):
        return list(self._eval_iter_values())

    
    def _eval_iter_values(self):
        rep = self._rep
        K = rep.domain
        values = rep.iter_values()
        if not K.is_EXRAW:
            values = map(K.to_sympy, values)
        return values

    
    def _eval_iter_items(self):
        pass
    # WARNING: Decompyle incomplete

    
    def copy(self):
        return self._fromrep(self._rep.copy())

    kind = (lambda self = classmethod: domain = self._rep.domainif domain in (ZZ, QQ):
element_kind = NumberKindelif domain == EXRAW:
kinds = self.values()()if len(kinds) == 1:
(element_kind,) = kindselse:
element_kind = UndefinedKindelse:
raise RuntimeError('Domain should only be ZZ, QQ or EXRAW')MatrixKind(element_kind))()
    
    def _eval_has(self, *patterns):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_is_Identity(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_is_symmetric(self, simpfunc):
        diff = (self - self.T).applyfunc(simpfunc)
        return len(diff.values()) == 0

    
    def _eval_transpose(self):
        '''Returns the transposed SparseMatrix of this SparseMatrix.

        Examples
        ========

        >>> from sympy import SparseMatrix
        >>> a = SparseMatrix(((1, 2), (3, 4)))
        >>> a
        Matrix([
        [1, 2],
        [3, 4]])
        >>> a.T
        Matrix([
        [1, 3],
        [2, 4]])
        '''
        return self._fromrep(self._rep.transpose())

    
    def _eval_col_join(self, other):
        return self._fromrep(self._rep.vstack(other._rep))

    
    def _eval_row_join(self, other):
        return self._fromrep(self._rep.hstack(other._rep))

    
    def _eval_extract(self, rowsList, colsList):
        return self._fromrep(self._rep.extract(rowsList, colsList))

    
    def __getitem__(self, key):
        return _getitem_RepMatrix(self, key)

    _eval_zeros = (lambda cls, rows, cols: rep = DomainMatrix.zeros((rows, cols), ZZ)cls._fromrep(rep))()
    _eval_eye = (lambda cls, rows, cols: rep = DomainMatrix.eye((rows, cols), ZZ)cls._fromrep(rep))()
    
    def _eval_add(self, other):
        return classof(self, other)._fromrep(self._rep + other._rep)

    
    def _eval_matrix_mul(self, other):
        return classof(self, other)._fromrep(self._rep * other._rep)

    
    def _eval_matrix_mul_elementwise(self, other):
        (selfrep, otherrep) = self._rep.unify(other._rep)
        newrep = selfrep.mul_elementwise(otherrep)
        return classof(self, other)._fromrep(newrep)

    
    def _eval_scalar_mul(self, other):
        (rep, other) = self._unify_element_sympy(self._rep, other)
        return self._fromrep(rep.scalarmul(other))

    
    def _eval_scalar_rmul(self, other):
        (rep, other) = self._unify_element_sympy(self._rep, other)
        return self._fromrep(rep.rscalarmul(other))

    
    def _eval_Abs(self):
        return self._fromrep(self._rep.applyfunc(abs))

    
    def _eval_conjugate(self):
        rep = self._rep
        domain = rep.domain
        if domain in (ZZ, QQ):
            return self.copy()
        return None._fromrep(rep.applyfunc((lambda e: e.conjugate())))

    
    def equals(self, other, failing_expression = (False,)):
        '''Applies ``equals`` to corresponding elements of the matrices,
        trying to prove that the elements are equivalent, returning True
        if they are, False if any pair is not, and None (or the first
        failing expression if failing_expression is True) if it cannot
        be decided if the expressions are equivalent or not. This is, in
        general, an expensive operation.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.abc import x
        >>> A = Matrix([x*(x - 1), 0])
        >>> B = Matrix([x**2 - x, 0])
        >>> A == B
        False
        >>> A.simplify() == B.simplify()
        True
        >>> A.equals(B)
        True
        >>> A.equals(2)
        False

        See Also
        ========
        sympy.core.expr.Expr.equals
        '''
        if self.shape != getattr(other, 'shape', None):
            return False
        rv = None
        for i in range(self.rows):
            for j in range(self.cols):
                ans = self[(i, j)].equals(other[(i, j)], failing_expression)
                if ans is False:
                    return False
                if None is not True and rv is True:
                    rv = ans
                return rv

    
    def inv_mod(M, m):
        '''
        Returns the inverse of the integer matrix ``M`` modulo ``m``.

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix(2, 2, [1, 2, 3, 4])
        >>> A.inv_mod(5)
        Matrix([
        [3, 1],
        [4, 2]])
        >>> A.inv_mod(3)
        Matrix([
        [1, 1],
        [0, 1]])

        '''
        if not M.is_square:
            raise NonSquareMatrixError()
        
        try:
            m = as_int(m)
        except ValueError:
            raise TypeError('inv_mod: modulus m must be an integer')

        K = GF(m, symmetric = False)
        
        try:
            dM = M.to_DM(K)
        except CoercionFailed:
            raise ValueError('inv_mod: matrix entries must be integers')

        
        try:
            dMi = dM.inv()
        except DMNonInvertibleMatrixError:
            exc = None
            msg = f'''Matrix is not invertible (mod {m})'''
            raise NonInvertibleMatrixError(msg), exc
            exc = None
            del exc

        return dMi.to_Matrix()

    
    def lll(self, delta = (0.75,)):
        '''LLL-reduced basis for the rowspace of a matrix of integers.

        Performs the Lenstra–Lenstra–Lovász (LLL) basis reduction algorithm.

        The implementation is provided by :class:`~DomainMatrix`. See
        :meth:`~DomainMatrix.lll` for more details.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix([[1, 0, 0, 0, -20160],
        ...             [0, 1, 0, 0, 33768],
        ...             [0, 0, 1, 0, 39578],
        ...             [0, 0, 0, 1, 47757]])
        >>> M.lll()
        Matrix([
        [ 10, -3,  -2,  8,  -4],
        [  3, -9,   8,  1, -11],
        [ -3, 13,  -9, -3,  -9],
        [-12, -7, -11,  9,  -1]])

        See Also
        ========

        lll_transform
        sympy.polys.matrices.domainmatrix.DomainMatrix.lll
        '''
        delta = QQ.from_sympy(_sympify(delta))
        dM = self._rep.convert_to(ZZ)
        basis = dM.lll(delta = delta)
        return self._fromrep(basis)

    
    def lll_transform(self, delta = (0.75,)):
        '''LLL-reduced basis and transformation matrix.

        Performs the Lenstra–Lenstra–Lovász (LLL) basis reduction algorithm.

        The implementation is provided by :class:`~DomainMatrix`. See
        :meth:`~DomainMatrix.lll_transform` for more details.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix([[1, 0, 0, 0, -20160],
        ...             [0, 1, 0, 0, 33768],
        ...             [0, 0, 1, 0, 39578],
        ...             [0, 0, 0, 1, 47757]])
        >>> B, T = M.lll_transform()
        >>> B
        Matrix([
        [ 10, -3,  -2,  8,  -4],
        [  3, -9,   8,  1, -11],
        [ -3, 13,  -9, -3,  -9],
        [-12, -7, -11,  9,  -1]])
        >>> T
        Matrix([
        [ 10, -3,  -2,  8],
        [  3, -9,   8,  1],
        [ -3, 13,  -9, -3],
        [-12, -7, -11,  9]])

        The transformation matrix maps the original basis to the LLL-reduced
        basis:

        >>> T * M == B
        True

        See Also
        ========

        lll
        sympy.polys.matrices.domainmatrix.DomainMatrix.lll_transform
        '''
        delta = QQ.from_sympy(_sympify(delta))
        dM = self._rep.convert_to(ZZ)
        (basis, transform) = dM.lll_transform(delta = delta)
        B = self._fromrep(basis)
        T = self._fromrep(transform)
        return (B, T)



class MutableRepMatrix(RepMatrix):
    pass
# WARNING: Decompyle incomplete


def _getitem_RepMatrix(self, key):
    '''Return portion of self defined by key. If the key involves a slice
    then a list will be returned (if key is a single slice) or a matrix
    (if key was a tuple involving a slice).

    Examples
    ========

    >>> from sympy import Matrix, I
    >>> m = Matrix([
    ... [1, 2 + I],
    ... [3, 4    ]])

    If the key is a tuple that does not involve a slice then that element
    is returned:

    >>> m[1, 0]
    3

    When a tuple key involves a slice, a matrix is returned. Here, the
    first column is selected (all rows, column 0):

    >>> m[:, 0]
    Matrix([
    [1],
    [3]])

    If the slice is not a tuple then it selects from the underlying
    list of elements that are arranged in row order and a list is
    returned if a slice is involved:

    >>> m[0]
    1
    >>> m[::2]
    [1, 3]
    '''
    pass
# WARNING: Decompyle incomplete
