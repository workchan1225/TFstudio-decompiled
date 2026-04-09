# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _indexing.pyc (Python 3.11)

import numbers
import sys
import warnings
from collections import UserList
from itertools import compress, islice
import numpy as np
from scipy.sparse import issparse
from sklearn.utils._array_api import _is_numpy_namespace, get_namespace, get_namespace_and_device, move_to
from sklearn.utils._dataframe import is_pandas_df, is_polars_df_or_series, is_pyarrow_data
from sklearn.utils._param_validation import Interval, validate_params
from sklearn.utils.extmath import _approximate_mode
from sklearn.utils.fixes import PYARROW_VERSION_BELOW_17
from sklearn.utils.validation import _check_sample_weight, _is_arraylike_not_scalar, _use_interchange_protocol, check_array, check_consistent_length, check_random_state

def _array_indexing(array, key, key_dtype, axis):
    '''Index an array or scipy.sparse consistently across NumPy version.'''
    (xp, is_array_api, device_) = get_namespace_and_device(array)
    if is_array_api:
        if hasattr(key, 'shape'):
            key = move_to(key, xp = xp, device = device_)
        elif isinstance(key, (int, slice)):
            pass
        else:
            key = xp.asarray(key, device = device_)
        if hasattr(key, 'dtype'):
            if xp.isdtype(key.dtype, 'integral'):
                return xp.take(array, key, axis = axis)
            if None.isdtype(key.dtype, 'bool'):
                indices = xp.arange(array.shape[axis], device = device_)
                return xp.take(array, indices[key], axis = axis)
            if None(array) and key_dtype == 'bool':
                key = np.asarray(key)
    if isinstance(key, tuple):
        key = list(key)
    return array[(key, ...)] if axis == 0 else array[(:, key)]


def _pandas_indexing(X, key, key_dtype, axis):
    '''Index a pandas dataframe or a series.'''
    if _is_arraylike_not_scalar(key):
        key = np.asarray(key)
    if not key_dtype == 'int' and isinstance(key, slice) and np.isscalar(key):
        return X.take(key, axis = axis)
    indexer = X.iloc if None == 'int' else X.loc
    return indexer[(:, key)] if axis else indexer[key]


def _list_indexing(X, key, key_dtype):
    '''Index a Python list.'''
    pass
# WARNING: Decompyle incomplete


def _polars_indexing(X, key, key_dtype, axis):
    '''Index a polars dataframe or series.'''
    if isinstance(key, np.ndarray):
        key = key.tolist()
    elif not np.isscalar(key) and isinstance(key, slice):
        key = list(key)
    if axis == 1:
        return X[(:, key)]
    if None == 'bool':
        return X.filter(key)
    X_indexed = None[key]
    if np.isscalar(key) and len(X.shape) == 2:
        pl = sys.modules['polars']
        return pl.Series(X_indexed.row(0))


def _pyarrow_indexing(X, key, key_dtype, axis):
    '''Index a pyarrow data.'''
    scalar_key = np.isscalar(key)
    if isinstance(key, slice):
        if isinstance(key.stop, str):
            start = X.column_names.index(key.start)
            stop = X.column_names.index(key.stop) + 1
        elif not key.start:
            pass
        
        start = key.start
        stop = key.stop
        step = 1 if not key.step else key.step
        key = list(range(start, stop, step))
    if axis == 1:
        if not key_dtype == 'int' and isinstance(key, list):
            key = np.asarray(key).tolist()
        if key_dtype == 'bool':
            key = np.asarray(key).nonzero()[0].tolist()
        if scalar_key:
            return X.column(key)
        return 0.select(key)
    if 0:
        if hasattr(X, 'shape'):
            key = [
                key]
        else:
            return X[key].as_py()
        if not None(key, list):
            key = np.asarray(key)
    if key_dtype == 'bool':
        if PYARROW_VERSION_BELOW_17:
            import pyarrow
            if not isinstance(key, pyarrow.BooleanArray):
                key = pyarrow.array(key, type = pyarrow.bool_())
        X_indexed = X.filter(key)
    else:
        X_indexed = X.take(key)
    if scalar_key and len(getattr(X, 'shape', [
        0])) == 2:
        pa = sys.modules['pyarrow']
        return pa.array(X_indexed.to_pylist()[0].values())


def _determine_key_type(key, accept_slice = (True,)):
    """Determine the data type of key.

    Parameters
    ----------
    key : scalar, slice or array-like
        The key from which we want to infer the data type.

    accept_slice : bool, default=True
        Whether or not to raise an error if the key is a slice.

    Returns
    -------
    dtype : {'int', 'str', 'bool', None}
        Returns the data type of key.
    """
    err_msg = 'No valid specification of the columns. Only a scalar, list or slice of all integers or all strings, or boolean mask is allowed'
    dtype_to_str = {
        np.bool_: 'bool',
        bool: 'bool',
        str: 'str',
        int: 'int' }
    array_dtype_to_str = {
        'i': 'int',
        'u': 'int',
        'b': 'bool',
        'O': 'str',
        'U': 'str',
        'S': 'str' }
# WARNING: Decompyle incomplete


def _safe_indexing(X = None, indices = {
    'axis': 0 }, *, axis):
    """Return rows, items or columns of X using indices.

    .. warning::

        This utility is documented, but **private**. This means that
        backward compatibility might be broken without any deprecation
        cycle.

    Parameters
    ----------
    X : array-like, sparse-matrix, list, pandas.DataFrame, pandas.Series
        Data from which to sample rows, items or columns. `list` are only
        supported when `axis=0`.
    indices : bool, int, str, slice, array-like
        - If `axis=0`, boolean and integer array-like, integer slice,
          and scalar integer are supported.
        - If `axis=1`:
            - to select a single column, `indices` can be of `int` type for
              all `X` types and `str` only for dataframe. The selected subset
              will be 1D, unless `X` is a sparse matrix in which case it will
              be 2D.
            - to select multiples columns, `indices` can be one of the
              following: `list`, `array`, `slice`. The type used in
              these containers can be one of the following: `int`, 'bool' and
              `str`. However, `str` is only supported when `X` is a dataframe.
              The selected subset will be 2D.
    axis : int, default=0
        The axis along which `X` will be subsampled. `axis=0` will select
        rows while `axis=1` will select columns.

    Returns
    -------
    subset
        Subset of X on axis 0 or 1.

    Notes
    -----
    CSR, CSC, and LIL sparse matrices are supported. COO sparse matrices are
    not supported.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.utils import _safe_indexing
    >>> data = np.array([[1, 2], [3, 4], [5, 6]])
    >>> _safe_indexing(data, 0, axis=0)  # select the first row
    array([1, 2])
    >>> _safe_indexing(data, 0, axis=1)  # select the first column
    array([1, 3, 5])
    """
    pass
# WARNING: Decompyle incomplete


def _safe_assign(X = None, values = {
    'row_indexer': None,
    'column_indexer': None }, *, row_indexer, column_indexer):
    '''Safe assignment to a numpy array, sparse matrix, or pandas dataframe.

    Parameters
    ----------
    X : {ndarray, sparse-matrix, dataframe}
        Array to be modified. It is expected to be 2-dimensional.

    values : ndarray
        The values to be assigned to `X`.

    row_indexer : array-like, dtype={int, bool}, default=None
        A 1-dimensional array to select the rows of interest. If `None`, all
        rows are selected.

    column_indexer : array-like, dtype={int, bool}, default=None
        A 1-dimensional array to select the columns of interest. If `None`, all
        columns are selected.
    '''
    pass
# WARNING: Decompyle incomplete


def _get_column_indices_for_bool_or_int(key, n_columns):
    
    try:
        idx = _safe_indexing(np.arange(n_columns), key)
    except IndexError:
        e = None
        raise ValueError(f'''all features must be in [0, {n_columns - 1}] or [-{n_columns}, 0]'''), e
        e = None
        del e

    return np.atleast_1d(idx).tolist()


def _get_column_indices(X, key):
    '''Get feature column indices for input data X and key.

    For accepted values of `key`, see the docstring of
    :func:`_safe_indexing`.
    '''
    key_dtype = _determine_key_type(key)
    if _use_interchange_protocol(X):
        return _get_column_indices_interchange(X.__dataframe__(), key, key_dtype)
    n_columns = None.shape[1]
    if not isinstance(key, (list, tuple)) and key:
        return []
    if None in ('bool', 'int'):
        return _get_column_indices_for_bool_or_int(key, n_columns)
    
    try:
        all_columns = X.columns
    except AttributeError:
        raise ValueError('Specifying the columns using strings is only supported for dataframes.')

    if isinstance(key, str):
        columns = [
            key]
# WARNING: Decompyle incomplete


def _get_column_indices_interchange(X_interchange, key, key_dtype):
    '''Same as _get_column_indices but for X with __dataframe__ protocol.'''
    pass
# WARNING: Decompyle incomplete

resample = (lambda *: pass# WARNING: Decompyle incomplete
)()

def shuffle(*, random_state, n_samples, *arrays):
    """Shuffle arrays or sparse matrices in a consistent way.

    This is a convenience alias to ``resample(*arrays, replace=False)`` to do
    random permutations of the collections.

    Parameters
    ----------
    *arrays : sequence of indexable data-structures
        Indexable data-structures can be arrays, lists, dataframes or scipy
        sparse matrices with consistent first dimension.

    random_state : int, RandomState instance or None, default=None
        Determines random number generation for shuffling
        the data.
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    n_samples : int, default=None
        Number of samples to generate. If left to None this is
        automatically set to the first dimension of the arrays.  It should
        not be larger than the length of arrays.

    Returns
    -------
    shuffled_arrays : sequence of indexable data-structures
        Sequence of shuffled copies of the collections. The original arrays
        are not impacted.

    See Also
    --------
    resample : Resample arrays or sparse matrices in a consistent way.

    Examples
    --------
    It is possible to mix sparse and dense arrays in the same run::

      >>> import numpy as np
      >>> X = np.array([[1., 0.], [2., 1.], [0., 0.]])
      >>> y = np.array([0, 1, 2])

      >>> from scipy.sparse import coo_matrix
      >>> X_sparse = coo_matrix(X)

      >>> from sklearn.utils import shuffle
      >>> X, X_sparse, y = shuffle(X, X_sparse, y, random_state=0)
      >>> X
      array([[0., 0.],
             [2., 1.],
             [1., 0.]])

      >>> X_sparse
      <Compressed Sparse Row sparse matrix of dtype 'float64'
          with 3 stored elements and shape (3, 2)>

      >>> X_sparse.toarray()
      array([[0., 0.],
             [2., 1.],
             [1., 0.]])

      >>> y
      array([2, 1, 0])

      >>> shuffle(y, n_samples=2, random_state=0)
      array([0, 1])
    """
    pass
# WARNING: Decompyle incomplete
