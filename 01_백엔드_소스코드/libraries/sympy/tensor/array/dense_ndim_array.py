# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dense_ndim_array.pyc (Python 3.11)

import functools
from typing import List
from sympy.core.basic import Basic
from sympy.core.containers import Tuple
from sympy.core.singleton import S
from sympy.core.sympify import _sympify
from sympy.tensor.array.mutable_ndim_array import MutableNDimArray
from sympy.tensor.array.ndim_array import NDimArray, ImmutableNDimArray, ArrayKind
from sympy.utilities.iterables import flatten

class DenseNDimArray(NDimArray):
    _array: List[Basic] = 'DenseNDimArray'
    
    def __new__(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    kind = (lambda self = None: ArrayKind._union(self._array))()
    
    def __getitem__(self, index):
        '''
        Allows to get items from N-dim array.

        Examples
        ========

        >>> from sympy import MutableDenseNDimArray
        >>> a = MutableDenseNDimArray([0, 1, 2, 3], (2, 2))
        >>> a
        [[0, 1], [2, 3]]
        >>> a[0, 0]
        0
        >>> a[1, 1]
        3
        >>> a[0]
        [0, 1]
        >>> a[1]
        [2, 3]


        Symbolic index:

        >>> from sympy.abc import i, j
        >>> a[i, j]
        [[0, 1], [2, 3]][i, j]

        Replace `i` and `j` to get element `(1, 1)`:

        >>> a[i, j].subs({i: 1, j: 1})
        3

        '''
        pass
    # WARNING: Decompyle incomplete

    zeros = (lambda cls: list_length = functools.reduce((lambda x, y: x * y), shape, S.One)
        return cls._new(([
            0] * list_length,), shape)
)()
    
    def tomatrix(self):
        '''
        Converts MutableDenseNDimArray to Matrix. Can convert only 2-dim array, else will raise error.

        Examples
        ========

        >>> from sympy import MutableDenseNDimArray
        >>> a = MutableDenseNDimArray([1 for i in range(9)], (3, 3))
        >>> b = a.tomatrix()
        >>> b
        Matrix([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]])

        '''
        Matrix = Matrix
        import sympy.matrices
        if self.rank() != 2:
            raise ValueError('Dimensions must be of size of 2')
        return Matrix(self.shape[0], self.shape[1], self._array)

    
    def reshape(self, *newshape):
        '''
        Returns MutableDenseNDimArray instance with new shape. Elements number
        must be        suitable to new shape. The only argument of method sets
        new shape.

        Examples
        ========

        >>> from sympy import MutableDenseNDimArray
        >>> a = MutableDenseNDimArray([1, 2, 3, 4, 5, 6], (2, 3))
        >>> a.shape
        (2, 3)
        >>> a
        [[1, 2, 3], [4, 5, 6]]
        >>> b = a.reshape(3, 2)
        >>> b.shape
        (3, 2)
        >>> b
        [[1, 2], [3, 4], [5, 6]]

        '''
        new_total_size = functools.reduce((lambda x, y: x * y), newshape)
        if new_total_size != self._loop_size:
            raise ValueError('Expecting reshape size to %d but got prod(%s) = %d' % (self._loop_size, str(newshape), new_total_size))
        return type(self)(self._array, newshape)



class ImmutableDenseNDimArray(ImmutableNDimArray, DenseNDimArray):
    
    def __new__(cls, iterable, shape = (None,), **kwargs):
        pass
    # WARNING: Decompyle incomplete

    _new = (lambda cls, iterable, shape: pass# WARNING: Decompyle incomplete
)()
    
    def __setitem__(self, index, value):
        raise TypeError('immutable N-dim array')

    
    def as_mutable(self):
        return MutableDenseNDimArray(self)

    
    def _eval_simplify(self, **kwargs):
        simplify = simplify
        import sympy.simplify.simplify
        return self.applyfunc(simplify)



class MutableDenseNDimArray(MutableNDimArray, DenseNDimArray):
    
    def __new__(cls, iterable, shape = (None, None), **kwargs):
        pass
    # WARNING: Decompyle incomplete

    _new = (lambda cls, iterable, shape: pass# WARNING: Decompyle incomplete
)()
    
    def __setitem__(self, index, value):
        '''Allows to set items to MutableDenseNDimArray.

        Examples
        ========

        >>> from sympy import MutableDenseNDimArray
        >>> a = MutableDenseNDimArray.zeros(2,  2)
        >>> a[0,0] = 1
        >>> a[1,1] = 1
        >>> a
        [[1, 0], [0, 1]]

        '''
        if isinstance(index, tuple) and (lambda .0: pass# WARNING: Decompyle incomplete
)(index()):
            (value, eindices, slice_offsets) = self._get_slice_data_for_array_assignment(index, value)
            for i in eindices:
                other_i = zip(i, slice_offsets)()
                self._array[self._parse_index(i)] = value[other_i]
                return None
                index = self._parse_index(index)
                self._setter_iterable_check(value)
                value = _sympify(value)
                self._array[index] = value
                return None

    
    def as_immutable(self):
        return ImmutableDenseNDimArray(self)

    free_symbols = (lambda self: self._array())()
