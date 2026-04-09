# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sparse_ndim_array.pyc (Python 3.11)

from sympy.core.basic import Basic
from sympy.core.containers import Dict, Tuple
from sympy.core.singleton import S
from sympy.core.sympify import _sympify
from sympy.tensor.array.mutable_ndim_array import MutableNDimArray
from sympy.tensor.array.ndim_array import NDimArray, ImmutableNDimArray
from sympy.utilities.iterables import flatten
import functools

class SparseNDimArray(NDimArray):
    
    def __new__(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, index):
        '''
        Get an element from a sparse N-dim array.

        Examples
        ========

        >>> from sympy import MutableSparseNDimArray
        >>> a = MutableSparseNDimArray(range(4), (2, 2))
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

        Symbolic indexing:

        >>> from sympy.abc import i, j
        >>> a[i, j]
        [[0, 1], [2, 3]][i, j]

        Replace `i` and `j` to get element `(0, 0)`:

        >>> a[i, j].subs({i: 0, j: 0})
        0

        '''
        pass
    # WARNING: Decompyle incomplete

    zeros = (lambda cls: cls({ }, shape))()
    
    def tomatrix(self):
        '''
        Converts MutableDenseNDimArray to Matrix. Can convert only 2-dim array, else will raise error.

        Examples
        ========

        >>> from sympy import MutableSparseNDimArray
        >>> a = MutableSparseNDimArray([1 for i in range(9)], (3, 3))
        >>> b = a.tomatrix()
        >>> b
        Matrix([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]])
        '''
        SparseMatrix = SparseMatrix
        import sympy.matrices
        if self.rank() != 2:
            raise ValueError('Dimensions must be of size of 2')
        mat_sparse = { }
        for key, value in self._sparse_array.items():
            mat_sparse[self._get_tuple_index(key)] = value
            return SparseMatrix(self.shape[0], self.shape[1], mat_sparse)

    
    def reshape(self, *newshape):
        new_total_size = functools.reduce((lambda x, y: x * y), newshape)
        if new_total_size != self._loop_size:
            raise ValueError('Invalid reshape parameters ' + newshape)
        return type(self)(self._sparse_array, newshape)



class ImmutableSparseNDimArray(ImmutableNDimArray, SparseNDimArray):
    
    def __new__(cls, iterable, shape = (None, None), **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def __setitem__(self, index, value):
        raise TypeError('immutable N-dim array')

    
    def as_mutable(self):
        return MutableSparseNDimArray(self)



class MutableSparseNDimArray(SparseNDimArray, MutableNDimArray):
    
    def __new__(cls, iterable, shape = (None, None), **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def __setitem__(self, index, value):
        '''Allows to set items to MutableDenseNDimArray.

        Examples
        ========

        >>> from sympy import MutableSparseNDimArray
        >>> a = MutableSparseNDimArray.zeros(2, 2)
        >>> a[0, 0] = 1
        >>> a[1, 1] = 1
        >>> a
        [[1, 0], [0, 1]]
        '''
        if isinstance(index, tuple) and (lambda .0: pass# WARNING: Decompyle incomplete
)(index()):
            (value, eindices, slice_offsets) = self._get_slice_data_for_array_assignment(index, value)
            for i in eindices:
                other_i = zip(i, slice_offsets)()
                other_value = value[other_i]
                complete_index = self._parse_index(i)
                if other_value != 0:
                    self._sparse_array[complete_index] = other_value
                    continue
                if complete_index in self._sparse_array:
                    self._sparse_array.pop(complete_index)
                return None
                index = self._parse_index(index)
                value = _sympify(value)
                if value == 0 and index in self._sparse_array:
                    self._sparse_array.pop(index)
                    return None
                
                def self._sparse_array[index](.0):
                    pass
                # WARNING: Decompyle incomplete

                return None

    
    def as_immutable(self):
        return ImmutableSparseNDimArray(self)

    free_symbols = (lambda self: self._sparse_array.values()())()
