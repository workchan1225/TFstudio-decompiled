# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: accessor.pyc (Python 3.11)

'''Sparse accessor'''
from __future__ import annotations
from typing import TYPE_CHECKING
import numpy as np
from pandas.compat._optional import import_optional_dependency
from pandas.core.dtypes.cast import find_common_type
from pandas.core.dtypes.dtypes import SparseDtype
from pandas.core.accessor import PandasDelegate, delegate_names
from pandas.core.arrays.sparse.array import SparseArray
if TYPE_CHECKING:
    from scipy.sparse import coo_matrix, spmatrix
    from pandas import DataFrame, Series

class BaseAccessor:
    _validation_msg = "Can only use the '.sparse' accessor with Sparse data."
    
    def __init__(self = None, data = None):
        self._parent = data
        self._validate(data)

    
    def _validate(self = None, data = None):
        raise NotImplementedError


SparseAccessor = <NODE:12>()

class SparseFrameAccessor(PandasDelegate, BaseAccessor):
    '''
    DataFrame accessor for sparse data.

    It allows users to interact with a `DataFrame` that contains sparse data types
    (`SparseDtype`). It provides methods and attributes to efficiently work with sparse
    storage, reducing memory usage while maintaining compatibility with standard pandas
    operations.

    Parameters
    ----------
    data : scipy.sparse.spmatrix
        Must be convertible to csc format.

    See Also
    --------
    DataFrame.sparse.density : Ratio of non-sparse points to total (dense) data points.

    Examples
    --------
    >>> df = pd.DataFrame({"a": [1, 2, 0, 0], "b": [3, 0, 0, 4]}, dtype="Sparse[int]")
    >>> df.sparse.density
    np.float64(0.5)
    '''
    
    def _validate(self = None, data = None):
        dtypes = data.dtypes
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(dtypes()):
            raise AttributeError(self._validation_msg)

    from_spmatrix = (lambda cls = None, data = None, index = classmethod, columns = (None, None): IntIndex = IntIndeximport pandas._libs.sparseDataFrame = DataFrameimport pandasdata = data.tocsc()(index, columns) = cls._prep_index(data, index, columns)(n_rows, n_columns) = data.shapedata.sort_indices()indices = data.indicesindptr = data.indptrarray_data = data.datadtype = SparseDtype(array_data.dtype)arrays = []for i in range(n_columns):
sl = slice(indptr[i], indptr[i + 1])idx = IntIndex(n_rows, indices[sl], check_integrity = False)arr = SparseArray._simple_new(array_data[sl], idx, dtype)arrays.append(arr)DataFrame._from_arrays(arrays, columns = columns, index = index, verify_integrity = False))()
    
    def to_dense(self = None):
        '''
        Convert a DataFrame with sparse values to dense.

        Returns
        -------
        DataFrame
            A DataFrame with the same values stored as dense arrays.

        See Also
        --------
        DataFrame.sparse.density : Ratio of non-sparse points to total
            (dense) data points.

        Examples
        --------
        >>> df = pd.DataFrame({"A": pd.arrays.SparseArray([0, 1, 0])})
        >>> df.sparse.to_dense()
           A
        0  0
        1  1
        2  0
        '''
        data = self._parent.items()()
        return self._parent._constructor(data, index = self._parent.index, columns = self._parent.columns)

    
    def to_coo(self = None):
        '''
        Return the contents of the frame as a sparse SciPy COO matrix.

        Returns
        -------
        scipy.sparse.spmatrix
            If the caller is heterogeneous and contains booleans or objects,
            the result will be of dtype=object. See Notes.

        See Also
        --------
        DataFrame.sparse.to_dense : Convert a DataFrame with sparse values to dense.

        Notes
        -----
        The dtype will be the lowest-common-denominator type (implicit
        upcasting); that is to say if the dtypes (even of numeric types)
        are mixed, the one that accommodates all will be chosen.

        e.g. If the dtypes are float16 and float32, dtype will be upcast to
        float32. By numpy.find_common_type convention, mixing int64 and
        and uint64 will result in a float64 dtype.

        Examples
        --------
        >>> df = pd.DataFrame({"A": pd.arrays.SparseArray([0, 1, 0, 1])})
        >>> df.sparse.to_coo()
        <COOrdinate sparse matrix of dtype \'int64\'
            with 2 stored elements and shape (4, 1)>
        '''
        import_optional_dependency('scipy')
        coo_matrix = coo_matrix
        import scipy.sparse
        dtype = find_common_type(self._parent.dtypes.to_list())
        if isinstance(dtype, SparseDtype):
            dtype = dtype.subtype
        data = []
        rows = []
        cols = []
        for _, ser in enumerate(self._parent.items()):
            sp_arr = ser.array
            row = sp_arr.sp_index.indices
            cols.append(np.repeat(col, len(row)))
            rows.append(row)
            data.append(sp_arr.sp_values.astype(dtype, copy = False))
            cols_arr = np.concatenate(cols)
            rows_arr = np.concatenate(rows)
            data_arr = np.concatenate(data)
            return coo_matrix((data_arr, (rows_arr, cols_arr)), shape = self._parent.shape)

    density = (lambda self = None: tmp = (lambda .0: [ column.array.density for _, column in .0 ])(self._parent.items()())
        return tmp
)()
    _prep_index = (lambda data, index, columns: default_index = default_indexensure_index = ensure_indeximport pandas.core.indexes.api(N, K) = data.shape# WARNING: Decompyle incomplete
)()
