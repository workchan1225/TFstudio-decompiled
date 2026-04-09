# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sparsefuncs.pyc (Python 3.11)

'''A collection of utilities to work with sparse matrices and arrays.'''
import itertools
import numpy as np
from scipy.sparse import sparse as sp
from scipy.sparse.linalg import LinearOperator
from sklearn.utils.fixes import _sparse_min_max, _sparse_nan_min_max
from sklearn.utils.sparsefuncs_fast import csc_mean_variance_axis0 as _csc_mean_var_axis0
from sklearn.utils.sparsefuncs_fast import csr_matmul_csr_to_dense
from sklearn.utils.sparsefuncs_fast import csr_mean_variance_axis0 as _csr_mean_var_axis0
from sklearn.utils.sparsefuncs_fast import incr_mean_variance_axis0 as _incr_mean_var_axis0
from sklearn.utils.validation import _check_sample_weight

def _raise_typeerror(X):
    '''Raises a TypeError if X is not a CSR or CSC matrix'''
    input_type = X.format if sp.issparse(X) else type(X)
    err = 'Expected a CSR or CSC sparse matrix, got %s.' % input_type
    raise TypeError(err)


def _raise_error_wrong_axis(axis):
    if axis not in (0, 1):
        raise ValueError('Unknown axis value: %d. Use 0 for rows, or 1 for columns' % axis)


def inplace_csr_column_scale(X, scale):
    '''Inplace column scaling of a CSR matrix.

    Scale each feature of the data matrix by multiplying with specific scale
    provided by the caller assuming a (n_samples, n_features) shape.

    Parameters
    ----------
    X : sparse matrix of shape (n_samples, n_features)
        Matrix to normalize using the variance of the features.
        It should be of CSR format.

    scale : ndarray of shape (n_features,), dtype={np.float32, np.float64}
        Array of precomputed feature-wise values to use for scaling.

    Examples
    --------
    >>> from sklearn.utils import sparsefuncs
    >>> from scipy import sparse
    >>> import numpy as np
    >>> indptr = np.array([0, 3, 4, 4, 4])
    >>> indices = np.array([0, 1, 2, 2])
    >>> data = np.array([8, 1, 2, 5])
    >>> scale = np.array([2, 3, 2])
    >>> csr = sparse.csr_matrix((data, indices, indptr))
    >>> csr.todense()
    matrix([[8, 1, 2],
            [0, 0, 5],
            [0, 0, 0],
            [0, 0, 0]])
    >>> sparsefuncs.inplace_csr_column_scale(csr, scale)
    >>> csr.todense()
    matrix([[16,  3,  4],
            [ 0,  0, 10],
            [ 0,  0,  0],
            [ 0,  0,  0]])
    '''
    pass
# WARNING: Decompyle incomplete


def inplace_csr_row_scale(X, scale):
    '''Inplace row scaling of a CSR matrix.

    Scale each sample of the data matrix by multiplying with specific scale
    provided by the caller assuming a (n_samples, n_features) shape.

    Parameters
    ----------
    X : sparse matrix of shape (n_samples, n_features)
        Matrix to be scaled. It should be of CSR format.

    scale : ndarray of float of shape (n_samples,)
        Array of precomputed sample-wise values to use for scaling.
    '''
    pass
# WARNING: Decompyle incomplete


def mean_variance_axis(X, axis, weights, return_sum_weights = (None, False)):
    '''Compute mean and variance along an axis on a CSR or CSC matrix.

    Parameters
    ----------
    X : sparse matrix of shape (n_samples, n_features)
        Input data. It can be of CSR or CSC format.

    axis : {0, 1}
        Axis along which the axis should be computed.

    weights : ndarray of shape (n_samples,) or (n_features,), default=None
        If axis is set to 0 shape is (n_samples,) or
        if axis is set to 1 shape is (n_features,).
        If it is set to None, then samples are equally weighted.

        .. versionadded:: 0.24

    return_sum_weights : bool, default=False
        If True, returns the sum of weights seen for each feature
        if `axis=0` or each sample if `axis=1`.

        .. versionadded:: 0.24

    Returns
    -------

    means : ndarray of shape (n_features,), dtype=floating
        Feature-wise means.

    variances : ndarray of shape (n_features,), dtype=floating
        Feature-wise variances.

    sum_weights : ndarray of shape (n_features,), dtype=floating
        Returned if `return_sum_weights` is `True`.

    Examples
    --------
    >>> from sklearn.utils import sparsefuncs
    >>> from scipy import sparse
    >>> import numpy as np
    >>> indptr = np.array([0, 3, 4, 4, 4])
    >>> indices = np.array([0, 1, 2, 2])
    >>> data = np.array([8, 1, 2, 5])
    >>> scale = np.array([2, 3, 2])
    >>> csr = sparse.csr_matrix((data, indices, indptr))
    >>> csr.todense()
    matrix([[8, 1, 2],
            [0, 0, 5],
            [0, 0, 0],
            [0, 0, 0]])
    >>> sparsefuncs.mean_variance_axis(csr, axis=0)
    (array([2.  , 0.25, 1.75]), array([12.    ,  0.1875,  4.1875]))
    '''
    _raise_error_wrong_axis(axis)
    if sp.issparse(X) and X.format == 'csr':
        if axis == 0:
            return _csr_mean_var_axis0(X, weights = weights, return_sum_weights = return_sum_weights)
        return None(X.T, weights = weights, return_sum_weights = return_sum_weights)
    if None.issparse(X) and X.format == 'csc':
        if axis == 0:
            return _csc_mean_var_axis0(X, weights = weights, return_sum_weights = return_sum_weights)
        return None(X.T, weights = weights, return_sum_weights = return_sum_weights)
    None(X)


def incr_mean_variance_axis(X = None, *, axis, last_mean, last_var, last_n, weights):
    '''Compute incremental mean and variance along an axis on a CSR or CSC matrix.

    last_mean, last_var are the statistics computed at the last step by this
    function. Both must be initialized to 0-arrays of the proper size, i.e.
    the number of features in X. last_n is the number of samples encountered
    until now.

    Parameters
    ----------
    X : CSR or CSC sparse matrix of shape (n_samples, n_features)
        Input data.

    axis : {0, 1}
        Axis along which the axis should be computed.

    last_mean : ndarray of shape (n_features,) or (n_samples,), dtype=floating
        Array of means to update with the new data X.
        Should be of shape (n_features,) if axis=0 or (n_samples,) if axis=1.

    last_var : ndarray of shape (n_features,) or (n_samples,), dtype=floating
        Array of variances to update with the new data X.
        Should be of shape (n_features,) if axis=0 or (n_samples,) if axis=1.

    last_n : float or ndarray of shape (n_features,) or (n_samples,),             dtype=floating
        Sum of the weights seen so far, excluding the current weights
        If not float, it should be of shape (n_features,) if
        axis=0 or (n_samples,) if axis=1. If float it corresponds to
        having same weights for all samples (or features).

    weights : ndarray of shape (n_samples,) or (n_features,), default=None
        If axis is set to 0 shape is (n_samples,) or
        if axis is set to 1 shape is (n_features,).
        If it is set to None, then samples are equally weighted.

        .. versionadded:: 0.24

    Returns
    -------
    means : ndarray of shape (n_features,) or (n_samples,), dtype=floating
        Updated feature-wise means if axis = 0 or
        sample-wise means if axis = 1.

    variances : ndarray of shape (n_features,) or (n_samples,), dtype=floating
        Updated feature-wise variances if axis = 0 or
        sample-wise variances if axis = 1.

    n : ndarray of shape (n_features,) or (n_samples,), dtype=integral
        Updated number of seen samples per feature if axis=0
        or number of seen features per sample if axis=1.

        If weights is not None, n is a sum of the weights of the seen
        samples or features instead of the actual number of seen
        samples or features.

    Notes
    -----
    NaNs are ignored in the algorithm.

    Examples
    --------
    >>> from sklearn.utils import sparsefuncs
    >>> from scipy import sparse
    >>> import numpy as np
    >>> indptr = np.array([0, 3, 4, 4, 4])
    >>> indices = np.array([0, 1, 2, 2])
    >>> data = np.array([8, 1, 2, 5])
    >>> scale = np.array([2, 3, 2])
    >>> csr = sparse.csr_matrix((data, indices, indptr))
    >>> csr.todense()
    matrix([[8, 1, 2],
            [0, 0, 5],
            [0, 0, 0],
            [0, 0, 0]])
    >>> sparsefuncs.incr_mean_variance_axis(
    ...     csr, axis=0, last_mean=np.zeros(3), last_var=np.zeros(3), last_n=2
    ... )
    (array([1.33, 0.167, 1.17]), array([8.88, 0.139, 3.47]),
    array([6., 6., 6.]))
    '''
    _raise_error_wrong_axis(axis)
    if not sp.issparse(X) or X.format in ('csc', 'csr'):
        _raise_typeerror(X)
    if np.size(last_n) == 1:
        last_n = np.full(last_mean.shape, last_n, dtype = last_mean.dtype)
    if not  == np.size(last_mean), np.size(last_var) or np.size(last_mean), np.size(last_var) == np.size(last_n):
        pass
    
    raise ValueError('last_mean, last_var, last_n do not have the same shapes.')
    if axis == 1:
        if np.size(last_mean) != X.shape[0]:
            raise ValueError(f'''If axis=1, then last_mean, last_n, last_var should be of size n_samples {X.shape[0]} (Got {np.size(last_mean)}).''')
    elif np.size(last_mean) != X.shape[1]:
        raise ValueError(f'''If axis=0, then last_mean, last_n, last_var should be of size n_features {X.shape[1]} (Got {np.size(last_mean)}).''')
# WARNING: Decompyle incomplete


def inplace_column_scale(X, scale):
    '''Inplace column scaling of a CSC/CSR matrix.

    Scale each feature of the data matrix by multiplying with specific scale
    provided by the caller assuming a (n_samples, n_features) shape.

    Parameters
    ----------
    X : sparse matrix of shape (n_samples, n_features)
        Matrix to normalize using the variance of the features. It should be
        of CSC or CSR format.

    scale : ndarray of shape (n_features,), dtype={np.float32, np.float64}
        Array of precomputed feature-wise values to use for scaling.

    Examples
    --------
    >>> from sklearn.utils import sparsefuncs
    >>> from scipy import sparse
    >>> import numpy as np
    >>> indptr = np.array([0, 3, 4, 4, 4])
    >>> indices = np.array([0, 1, 2, 2])
    >>> data = np.array([8, 1, 2, 5])
    >>> scale = np.array([2, 3, 2])
    >>> csr = sparse.csr_matrix((data, indices, indptr))
    >>> csr.todense()
    matrix([[8, 1, 2],
            [0, 0, 5],
            [0, 0, 0],
            [0, 0, 0]])
    >>> sparsefuncs.inplace_column_scale(csr, scale)
    >>> csr.todense()
    matrix([[16,  3,  4],
            [ 0,  0, 10],
            [ 0,  0,  0],
            [ 0,  0,  0]])
    '''
    if sp.issparse(X) and X.format == 'csc':
        inplace_csr_row_scale(X.T, scale)
        return None
    if None.issparse(X) and X.format == 'csr':
        inplace_csr_column_scale(X, scale)
        return None
    None(X)


def inplace_row_scale(X, scale):
    '''Inplace row scaling of a CSR or CSC matrix.

    Scale each row of the data matrix by multiplying with specific scale
    provided by the caller assuming a (n_samples, n_features) shape.

    Parameters
    ----------
    X : sparse matrix of shape (n_samples, n_features)
        Matrix to be scaled. It should be of CSR or CSC format.

    scale : ndarray of shape (n_features,), dtype={np.float32, np.float64}
        Array of precomputed sample-wise values to use for scaling.

    Examples
    --------
    >>> from sklearn.utils import sparsefuncs
    >>> from scipy import sparse
    >>> import numpy as np
    >>> indptr = np.array([0, 2, 3, 4, 5])
    >>> indices = np.array([0, 1, 2, 3, 3])
    >>> data = np.array([8, 1, 2, 5, 6])
    >>> scale = np.array([2, 3, 4, 5])
    >>> csr = sparse.csr_matrix((data, indices, indptr))
    >>> csr.todense()
    matrix([[8, 1, 0, 0],
            [0, 0, 2, 0],
            [0, 0, 0, 5],
            [0, 0, 0, 6]])
    >>> sparsefuncs.inplace_row_scale(csr, scale)
    >>> csr.todense()
     matrix([[16,  2,  0,  0],
             [ 0,  0,  6,  0],
             [ 0,  0,  0, 20],
             [ 0,  0,  0, 30]])
    '''
    if sp.issparse(X) and X.format == 'csc':
        inplace_csr_column_scale(X.T, scale)
        return None
    if None.issparse(X) and X.format == 'csr':
        inplace_csr_row_scale(X, scale)
        return None
    None(X)


def inplace_swap_row_csc(X, m, n):
    '''Swap two rows of a CSC matrix in-place.

    Parameters
    ----------
    X : sparse matrix of shape (n_samples, n_features)
        Matrix whose two rows are to be swapped. It should be of
        CSC format.

    m : int
        Index of the row of X to be swapped.

    n : int
        Index of the row of X to be swapped.
    '''
    for t in (m, n):
        if isinstance(t, np.ndarray):
            raise TypeError('m and n should be valid integers')
        if m < 0:
            m += X.shape[0]
    if n < 0:
        n += X.shape[0]
    m_mask = X.indices == m
    X.indices[X.indices == n] = m
    X.indices[m_mask] = n


def inplace_swap_row_csr(X, m, n):
    '''Swap two rows of a CSR matrix in-place.

    Parameters
    ----------
    X : sparse matrix of shape (n_samples, n_features)
        Matrix whose two rows are to be swapped. It should be of
        CSR format.

    m : int
        Index of the row of X to be swapped.

    n : int
        Index of the row of X to be swapped.
    '''
    for t in (m, n):
        if isinstance(t, np.ndarray):
            raise TypeError('m and n should be valid integers')
        if m < 0:
            m += X.shape[0]
    if n < 0:
        n += X.shape[0]
    if m > n:
        n = m
        m = n
    indptr = X.indptr
    m_start = indptr[m]
    m_stop = indptr[m + 1]
    n_start = indptr[n]
    n_stop = indptr[n + 1]
    nz_m = m_stop - m_start
    nz_n = n_stop - n_start
    if nz_m != nz_n:
        m_start + nz_n = None
        X.indptr[n] = n_stop - nz_m
    X.indices = np.concatenate([
        X.indices[:m_start],
        X.indices[n_start:n_stop],
        X.indices[m_stop:n_start],
        X.indices[m_start:m_stop],
        X.indices[n_stop:]])
    X.data = np.concatenate([
        X.data[:m_start],
        X.data[n_start:n_stop],
        X.data[m_stop:n_start],
        X.data[m_start:m_stop],
        X.data[n_stop:]])


def inplace_swap_row(X, m, n):
    '''
    Swap two rows of a CSC/CSR matrix in-place.

    Parameters
    ----------
    X : sparse matrix of shape (n_samples, n_features)
        Matrix whose two rows are to be swapped. It should be of CSR or
        CSC format.

    m : int
        Index of the row of X to be swapped.

    n : int
        Index of the row of X to be swapped.

    Examples
    --------
    >>> from sklearn.utils import sparsefuncs
    >>> from scipy import sparse
    >>> import numpy as np
    >>> indptr = np.array([0, 2, 3, 3, 3])
    >>> indices = np.array([0, 2, 2])
    >>> data = np.array([8, 2, 5])
    >>> csr = sparse.csr_matrix((data, indices, indptr))
    >>> csr.todense()
    matrix([[8, 0, 2],
            [0, 0, 5],
            [0, 0, 0],
            [0, 0, 0]])
    >>> sparsefuncs.inplace_swap_row(csr, 0, 1)
    >>> csr.todense()
    matrix([[0, 0, 5],
            [8, 0, 2],
            [0, 0, 0],
            [0, 0, 0]])
    '''
    if sp.issparse(X) and X.format == 'csc':
        inplace_swap_row_csc(X, m, n)
        return None
    if None.issparse(X) and X.format == 'csr':
        inplace_swap_row_csr(X, m, n)
        return None
    None(X)


def inplace_swap_column(X, m, n):
    '''
    Swap two columns of a CSC/CSR matrix in-place.

    Parameters
    ----------
    X : sparse matrix of shape (n_samples, n_features)
        Matrix whose two columns are to be swapped. It should be of
        CSR or CSC format.

    m : int
        Index of the column of X to be swapped.

    n : int
        Index of the column of X to be swapped.

    Examples
    --------
    >>> from sklearn.utils import sparsefuncs
    >>> from scipy import sparse
    >>> import numpy as np
    >>> indptr = np.array([0, 2, 3, 3, 3])
    >>> indices = np.array([0, 2, 2])
    >>> data = np.array([8, 2, 5])
    >>> csr = sparse.csr_matrix((data, indices, indptr))
    >>> csr.todense()
    matrix([[8, 0, 2],
            [0, 0, 5],
            [0, 0, 0],
            [0, 0, 0]])
    >>> sparsefuncs.inplace_swap_column(csr, 0, 1)
    >>> csr.todense()
    matrix([[0, 8, 2],
            [0, 0, 5],
            [0, 0, 0],
            [0, 0, 0]])
    '''
    if m < 0:
        m += X.shape[1]
    if n < 0:
        n += X.shape[1]
    if sp.issparse(X) and X.format == 'csc':
        inplace_swap_row_csr(X, m, n)
        return None
    if None.issparse(X) and X.format == 'csr':
        inplace_swap_row_csc(X, m, n)
        return None
    None(X)


def min_max_axis(X, axis, ignore_nan = (False,)):
    '''Compute minimum and maximum along an axis on a CSR or CSC matrix.

     Optionally ignore NaN values.

    Parameters
    ----------
    X : sparse matrix of shape (n_samples, n_features)
        Input data. It should be of CSR or CSC format.

    axis : {0, 1}
        Axis along which the axis should be computed.

    ignore_nan : bool, default=False
        Ignore or passing through NaN values.

        .. versionadded:: 0.20

    Returns
    -------

    mins : ndarray of shape (n_features,), dtype={np.float32, np.float64}
        Feature-wise minima.

    maxs : ndarray of shape (n_features,), dtype={np.float32, np.float64}
        Feature-wise maxima.
    '''
    if sp.issparse(X) and X.format in ('csr', 'csc'):
        if ignore_nan:
            return _sparse_nan_min_max(X, axis = axis)
        return None(X, axis = axis)
    None(X)


def count_nonzero(X, axis, sample_weight = (None, None)):
    '''A variant of X.getnnz() with extension to weighting on axis 0.

    Useful in efficiently calculating multilabel metrics.

    Parameters
    ----------
    X : sparse matrix of shape (n_samples, n_labels)
        Input data. It should be of CSR format.

    axis : {0, 1}, default=None
        The axis on which the data is aggregated.

    sample_weight : array-like of shape (n_samples,), default=None
        Weight for each row of X.

    Returns
    -------
    nnz : int, float, ndarray of shape (n_samples,) or ndarray of shape (n_features,)
        Number of non-zero values in the array along a given axis. Otherwise,
        the total number of non-zero values in the array is returned.
    '''
    if axis == -1:
        axis = 1
    elif axis == -2:
        axis = 0
    elif X.format != 'csr':
        raise TypeError('Expected CSR sparse format, got {0}'.format(X.format))
# WARNING: Decompyle incomplete


def _get_median(data, n_zeros):
    '''Compute the median of data with n_zeros additional zeros.

    This function is used to support sparse matrices; it modifies data
    in-place.
    '''
    n_elems = len(data) + n_zeros
    if not n_elems:
        return np.nan
    n_negative = None.count_nonzero(data < 0)
    (middle, is_odd) = divmod(n_elems, 2)
    data.sort()
    if is_odd:
        return _get_elem_at_rank(middle, data, n_negative, n_zeros)
    return (None(middle - 1, data, n_negative, n_zeros) + _get_elem_at_rank(middle, data, n_negative, n_zeros)) / 2


def _get_elem_at_rank(rank, data, n_negative, n_zeros):
    '''Find the value in data augmented with n_zeros for the given rank'''
    if rank < n_negative:
        return data[rank]
    if None - n_negative < n_zeros:
        return 0
    return None[rank - n_zeros]


def csc_median_axis_0(X):
    '''Find the median across axis 0 of a CSC matrix.

    It is equivalent to doing np.median(X, axis=0).

    Parameters
    ----------
    X : sparse matrix of shape (n_samples, n_features)
        Input data. It should be of CSC format.

    Returns
    -------
    median : ndarray of shape (n_features,)
        Median.
    '''
    if not sp.issparse(X) or X.format == 'csc':
        raise TypeError('Expected matrix of CSC format, got %s' % X.format)
    indptr = X.indptr
    (n_samples, n_features) = X.shape
    median = np.zeros(n_features)
    for start, end in enumerate(itertools.pairwise(indptr)):
        data = np.copy(X.data[start:end])
        nz = n_samples - data.size
        median[f_ind] = _get_median(data, nz)
        return median


def _implicit_column_offset(X, offset):
    '''Create an implicitly offset linear operator.

    This is used by PCA on sparse data to avoid densifying the whole data
    matrix.

    Params
    ------
        X : sparse matrix of shape (n_samples, n_features)
        offset : ndarray of shape (n_features,)

    Returns
    -------
    centered : LinearOperator
    '''
    pass
# WARNING: Decompyle incomplete


def sparse_matmul_to_dense(A, B, out = (None,)):
    '''Compute A @ B for sparse and 2-dim A and B while returning an ndarray.

    Parameters
    ----------
    A : sparse matrix of shape (n1, n2) and format CSC or CSR
        Left-side input matrix.
    B : sparse matrix of shape (n2, n3) and format CSC or CSR
        Right-side input matrix.
    out : ndarray of shape (n1, n3) or None
        Optional ndarray into which the result is written.

    Returns
    -------
    out
        An ndarray, new created if out=None.
    '''
    if not sp.issparse(A) and A.format in ('csc', 'csr') or A.ndim == 2:
        raise ValueError("Input 'A' must be a sparse 2-dim CSC or CSR array.")
    if not sp.issparse(B) and B.format in ('csc', 'csr') or B.ndim == 2:
        raise ValueError("Input 'B' must be a sparse 2-dim CSC or CSR array.")
    if A.shape[1] != B.shape[0]:
        msg = f'''Shapes must fulfil A.shape[1] == B.shape[0], got {A.shape[1]} == {B.shape[0]}.'''
        raise ValueError(msg)
    (n1, n2) = A.shape
    n3 = B.shape[1]
    if A.dtype != B.dtype or A.dtype not in (np.float32, np.float64):
        msg = 'Dtype of A and B must be the same, either both float32 or float64.'
        raise ValueError(msg)
# WARNING: Decompyle incomplete
