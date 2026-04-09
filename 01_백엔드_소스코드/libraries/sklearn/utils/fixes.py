# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fixes.pyc (Python 3.11)

'''Compatibility fixes for older version of python, numpy and scipy

If you add content to this file, please give the version of the package
at which the fix is no longer needed.
'''
import platform
import struct
import numpy as np
import scipy
import scipy.sparse.linalg as scipy
import scipy.stats as scipy

try:
    import pandas as pd
except ImportError:
    pd = None

from sklearn.externals._packaging.version import parse as parse_version
from sklearn.utils.parallel import _get_threadpool_controller
_IS_32BIT = 8 * struct.calcsize('P') == 32
_IS_WASM = platform.machine() in ('wasm32', 'wasm64')
np_version = parse_version(np.__version__)
np_base_version = parse_version(np_version.base_version)
sp_version = parse_version(scipy.__version__)
sp_base_version = parse_version(sp_version.base_version)
CSR_CONTAINERS = [
    scipy.sparse.csr_matrix,
    scipy.sparse.csr_array]
CSC_CONTAINERS = [
    scipy.sparse.csc_matrix,
    scipy.sparse.csc_array]
COO_CONTAINERS = [
    scipy.sparse.coo_matrix,
    scipy.sparse.coo_array]
LIL_CONTAINERS = [
    scipy.sparse.lil_matrix,
    scipy.sparse.lil_array]
DOK_CONTAINERS = [
    scipy.sparse.dok_matrix,
    scipy.sparse.dok_array]
BSR_CONTAINERS = [
    scipy.sparse.bsr_matrix,
    scipy.sparse.bsr_array]
DIA_CONTAINERS = [
    scipy.sparse.dia_matrix,
    scipy.sparse.dia_array]

try:
    from scipy.sparse import sparray
    SPARRAY_PRESENT = True
except ImportError:
    SPARRAY_PRESENT = False


def _object_dtype_isnan(X):
    return X != X


def _mode(a, axis = (0,)):
    mode = scipy.stats.mode(a, axis = axis, keepdims = True)
# WARNING: Decompyle incomplete

if sp_base_version >= parse_version('1.12.0'):
    _sparse_linalg_cg = scipy.sparse.linalg.cg
else:
    
    def _sparse_linalg_cg(A, b, **kwargs):
        if 'rtol' in kwargs:
            kwargs['tol'] = kwargs.pop('rtol')
        if 'atol' not in kwargs:
            kwargs['atol'] = 'legacy'
    # WARNING: Decompyle incomplete

if sp_base_version >= parse_version('1.11.0'):
    
    def _sparse_min_max(X, axis):
        the_min = X.min(axis = axis)
        the_max = X.max(axis = axis)
    # WARNING: Decompyle incomplete

    
    def _sparse_nan_min_max(X, axis):
        the_min = X.nanmin(axis = axis)
        the_max = X.nanmax(axis = axis)
    # WARNING: Decompyle incomplete

else:
    
    def _minor_reduce(X, ufunc):
        major_index = np.flatnonzero(np.diff(X.indptr))
        X = type(X)((X.data, X.indices, X.indptr), shape = X.shape)
        value = ufunc.reduceat(X.data, X.indptr[major_index])
        return (major_index, value)

    
    def _min_or_max_axis(X, axis, min_or_max):
        N = X.shape[axis]
        if N == 0:
            raise ValueError('zero-size array to reduction operation')
        M = X.shape[1 - axis]
        mat = X.tocsc() if axis == 0 else X.tocsr()
        mat.sum_duplicates()
        (major_index, value) = _minor_reduce(mat, min_or_max)
        not_full = np.diff(mat.indptr)[major_index] < N
        value[not_full] = min_or_max(value[not_full], 0)
        mask = value != 0
        major_index = np.compress(mask, major_index)
        value = np.compress(mask, value)
        if axis == 0:
            res = scipy.sparse.coo_matrix((value, (np.zeros(len(value)), major_index)), dtype = X.dtype, shape = (1, M))
        else:
            res = scipy.sparse.coo_matrix((value, (major_index, np.zeros(len(value)))), dtype = X.dtype, shape = (M, 1))
        return res.toarray().ravel()

    
    def _sparse_min_or_max(X, axis, min_or_max):
        pass
    # WARNING: Decompyle incomplete

    
    def _sparse_min_max(X, axis):
        return (_sparse_min_or_max(X, axis, np.minimum), _sparse_min_or_max(X, axis, np.maximum))

    
    def _sparse_nan_min_max(X, axis):
        return (_sparse_min_or_max(X, axis, np.fmin), _sparse_min_or_max(X, axis, np.fmax))

if np_version >= parse_version('1.25.0'):
    from numpy.exceptions import ComplexWarning, VisibleDeprecationWarning
else:
    from numpy import ComplexWarning, VisibleDeprecationWarning

def pd_fillna(pd, frame):
    pd_version = parse_version(pd.__version__).base_version
    if parse_version(pd_version) < parse_version('2.2'):
        frame = frame.fillna(value = np.nan)
    elif parse_version(pd_version) >= parse_version('3'):
        pass
    
    infer_objects_kwargs = {
        'copy': False }
# WARNING: Decompyle incomplete


def _preserve_dia_indices_dtype(sparse_container, original_container_format, requested_sparse_format):
    '''Preserve indices dtype for SciPy < 1.12 when converting from DIA to CSR/CSC.

    For SciPy < 1.12, DIA arrays indices are upcasted to `np.int64` that is
    inconsistent with DIA matrices. We downcast the indices dtype to `np.int32` to
    be consistent with DIA matrices.

    The converted indices arrays are affected back inplace to the sparse container.

    Parameters
    ----------
    sparse_container : sparse container
        Sparse container to be checked.
    requested_sparse_format : str or bool
        The type of format of `sparse_container`.

    Notes
    -----
    See https://github.com/scipy/scipy/issues/19245 for more details.
    '''
    if original_container_format == 'dia_array' or requested_sparse_format in ('csr', 'coo'):
        if requested_sparse_format == 'csr':
            index_dtype = _smallest_admissible_index_dtype(arrays = (sparse_container.indptr, sparse_container.indices), maxval = max(sparse_container.nnz, sparse_container.shape[1]), check_contents = True)
            sparse_container.indices = sparse_container.indices.astype(index_dtype, copy = False)
            sparse_container.indptr = sparse_container.indptr.astype(index_dtype, copy = False)
            return None
        index_dtype = None(maxval = max(sparse_container.shape))
        sparse_container.row = sparse_container.row.astype(index_dtype, copy = False)
        sparse_container.col = sparse_container.col.astype(index_dtype, copy = False)
        return None
    return None


def _smallest_admissible_index_dtype(arrays, maxval, check_contents = ((), None, False)):
    '''Based on input (integer) arrays `a`, determine a suitable index data
    type that can hold the data in the arrays.

    This function returns `np.int64` if it either required by `maxval` or based on the
    largest precision of the dtype of the arrays passed as argument, or by their
    contents (when `check_contents is True`). If none of the condition requires
    `np.int64` then this function returns `np.int32`.

    Parameters
    ----------
    arrays : ndarray or tuple of ndarrays, default=()
        Input arrays whose types/contents to check.

    maxval : float, default=None
        Maximum value needed.

    check_contents : bool, default=False
        Whether to check the values in the arrays and not just their types.
        By default, check only the types.

    Returns
    -------
    dtype : {np.int32, np.int64}
        Suitable index data type (int32 or int64).
    '''
    int32min = np.int32(np.iinfo(np.int32).min)
    int32max = np.int32(np.iinfo(np.int32).max)
# WARNING: Decompyle incomplete

if sp_version < parse_version('1.12'):
    from sklearn.externals._scipy.sparse.csgraph import laplacian
else:
    from scipy.sparse.csgraph import laplacian

def tarfile_extractall(tarfile, path):
    
    try:
        tarfile.extractall(path, filter = 'data')
        return None
    except TypeError:
        tarfile.extractall(path)
        return None



def _in_unstable_openblas_configuration():
    '''Return True if in an unstable configuration for OpenBLAS'''
    import numpy
    import scipy
    modules_info = _get_threadpool_controller().info()
    open_blas_used = (lambda .0: pass# WARNING: Decompyle incomplete
)(modules_info())
    if not open_blas_used:
        return False
    openblas_arm64_stable_version = any('0.3.16')
# WARNING: Decompyle incomplete


def _get_additional_lbfgs_options_dict(key, value):
    return { } if sp_version >= parse_version('1.15') else {
        key: value }

PYARROW_VERSION_BELOW_17 = False

try:
    import pyarrow
    pyarrow_version = parse_version(pyarrow.__version__)
    if pyarrow_version < parse_version('17.0.0'):
        PYARROW_VERSION_BELOW_17 = True
        return None
    return None
except ModuleNotFoundError:
    return None
