# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ndim_array.pyc (Python 3.11)

from sympy.core.basic import Basic
from sympy.core.containers import Dict, Tuple
from sympy.core.expr import Expr
from sympy.core.kind import Kind, NumberKind, UndefinedKind
from sympy.core.numbers import Integer
from sympy.core.singleton import S
from sympy.core.sympify import sympify
from sympy.external.gmpy import SYMPY_INTS
from sympy.printing.defaults import Printable
import itertools
from collections.abc import Iterable

class ArrayKind(Kind):
    pass
# WARNING: Decompyle incomplete


class NDimArray(Printable):
    '''N-dimensional array.

    Examples
    ========

    Create an N-dim array of zeros:

    >>> from sympy import MutableDenseNDimArray
    >>> a = MutableDenseNDimArray.zeros(2, 3, 4)
    >>> a
    [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

    Create an N-dim array from a list;

    >>> a = MutableDenseNDimArray([[2, 3], [4, 5]])
    >>> a
    [[2, 3], [4, 5]]

    >>> b = MutableDenseNDimArray([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]])
    >>> b
    [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]

    Create an N-dim array from a flat list with dimension shape:

    >>> a = MutableDenseNDimArray([1, 2, 3, 4, 5, 6], (2, 3))
    >>> a
    [[1, 2, 3], [4, 5, 6]]

    Create an N-dim array from a matrix:

    >>> from sympy import Matrix
    >>> a = Matrix([[1,2],[3,4]])
    >>> a
    Matrix([
    [1, 2],
    [3, 4]])
    >>> b = MutableDenseNDimArray(a)
    >>> b
    [[1, 2], [3, 4]]

    Arithmetic operations on N-dim arrays

    >>> a = MutableDenseNDimArray([1, 1, 1, 1], (2, 2))
    >>> b = MutableDenseNDimArray([4, 4, 4, 4], (2, 2))
    >>> c = a + b
    >>> c
    [[5, 5], [5, 5]]
    >>> a - b
    [[-3, -3], [-3, -3]]

    '''
    _diff_wrt = True
    is_scalar = False
    
    def __new__(cls, iterable, shape = (None,), **kwargs):
        ImmutableDenseNDimArray = ImmutableDenseNDimArray
        import sympy.tensor.array
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, index):
        raise NotImplementedError('A subclass of NDimArray should implement __getitem__')

    
    def _parse_index(self, index):
        if isinstance(index, (SYMPY_INTS, Integer)):
            if index >= self._loop_size:
                raise ValueError('Only a tuple index is accepted')
            return index
        if None._loop_size == 0:
            raise ValueError('Index not valid with an empty array')
        if len(index) != self._rank:
            raise ValueError('Wrong number of array axes')
        real_index = 0
        for i in range(self._rank):
            if index[i] >= self.shape[i] or index[i] < -self.shape[i]:
                raise ValueError('Index ' + str(index) + ' out of border')
            if index[i] < 0:
                real_index += 1
            real_index = real_index * self.shape[i] + index[i]
            return real_index

    
    def _get_tuple_index(self, integer_index):
        index = []
        for sh in reversed(self.shape):
            index.append(integer_index % sh)
            integer_index //= sh
            index.reverse()
            return tuple(index)

    
    def _check_symbolic_index(self, index):
        tuple_index = index if isinstance(index, tuple) else (index,)
    # WARNING: Decompyle incomplete

    
    def _setter_iterable_check(self, value):
        MatrixBase = MatrixBase
        import sympy.matrices.matrixbase
        if isinstance(value, (Iterable, MatrixBase, NDimArray)):
            raise NotImplementedError

    _scan_iterable_shape = (lambda cls, iterable: pass# WARNING: Decompyle incomplete
)()
    _handle_ndarray_creation_inputs = (lambda cls, iterable, shape = (None, None): MatrixBase = MatrixBaseimport sympy.matrices.matrixbaseSparseNDimArray = SparseNDimArrayimport sympy.tensor.array# WARNING: Decompyle incomplete
)()
    
    def __len__(self):
        '''Overload common function len(). Returns number of elements in array.

        Examples
        ========

        >>> from sympy import MutableDenseNDimArray
        >>> a = MutableDenseNDimArray.zeros(3, 3)
        >>> a
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        >>> len(a)
        9

        '''
        return self._loop_size

    shape = (lambda self: self._shape)()
    
    def rank(self):
        '''
        Returns rank of array.

        Examples
        ========

        >>> from sympy import MutableDenseNDimArray
        >>> a = MutableDenseNDimArray.zeros(3,4,5,6,3)
        >>> a.rank()
        5

        '''
        return self._rank

    
    def diff(self, *args, **kwargs):
        '''
        Calculate the derivative of each element in the array.

        Examples
        ========

        >>> from sympy import ImmutableDenseNDimArray
        >>> from sympy.abc import x, y
        >>> M = ImmutableDenseNDimArray([[x, y], [1, x*y]])
        >>> M.diff(x)
        [[1, 0], [0, y]]

        '''
        ArrayDerivative = ArrayDerivative
        import sympy.tensor.array.array_derivatives
        kwargs.setdefault('evaluate', True)
    # WARNING: Decompyle incomplete

    
    def _eval_derivative(self, base):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_derivative_n_times(self, s, n):
        return Basic._eval_derivative_n_times(self, s, n)

    
    def applyfunc(self, f):
        '''Apply a function to each element of the N-dim array.

        Examples
        ========

        >>> from sympy import ImmutableDenseNDimArray
        >>> m = ImmutableDenseNDimArray([i*2+j for i in range(2) for j in range(2)], (2, 2))
        >>> m
        [[0, 1], [2, 3]]
        >>> m.applyfunc(lambda i: 2*i)
        [[0, 2], [4, 6]]
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _sympystr(self, printer):
        pass
    # WARNING: Decompyle incomplete

    
    def tolist(self):
        '''
        Converting MutableDenseNDimArray to one-dim list

        Examples
        ========

        >>> from sympy import MutableDenseNDimArray
        >>> a = MutableDenseNDimArray([1, 2, 3, 4], (2, 2))
        >>> a
        [[1, 2], [3, 4]]
        >>> b = a.tolist()
        >>> b
        [[1, 2], [3, 4]]
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __add__(self, other):
        Flatten = Flatten
        import sympy.tensor.array.arrayop
        if not isinstance(other, NDimArray):
            return NotImplemented
        if None.shape != other.shape:
            raise ValueError('array shape mismatch')
        result_list = zip(Flatten(self), Flatten(other))()
        return type(self)(result_list, self.shape)

    
    def __sub__(self, other):
        Flatten = Flatten
        import sympy.tensor.array.arrayop
        if not isinstance(other, NDimArray):
            return NotImplemented
        if None.shape != other.shape:
            raise ValueError('array shape mismatch')
        result_list = zip(Flatten(self), Flatten(other))()
        return type(self)(result_list, self.shape)

    
    def __mul__(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def __rmul__(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def __truediv__(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def __rtruediv__(self, other):
        raise NotImplementedError('unsupported operation on NDimArray')

    
    def __neg__(self):
