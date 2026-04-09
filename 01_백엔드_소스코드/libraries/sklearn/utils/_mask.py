# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _mask.pyc (Python 3.11)

from contextlib import suppress
import numpy as np
from scipy import sparse as sp
from sklearn.utils._missing import is_scalar_nan
from sklearn.utils._param_validation import validate_params
from sklearn.utils.fixes import _object_dtype_isnan

def _get_dense_mask(X, value_to_mask):
    suppress(ImportError, AttributeError)
    import pandas
    if value_to_mask is pandas.NA:
        None(None, None)
        return 
    None(None, None)


def _get_mask(X, value_to_mask):
    '''Compute the boolean mask X == value_to_mask.

    Parameters
    ----------
    X : {ndarray, sparse matrix} of shape (n_samples, n_features)
        Input data, where ``n_samples`` is the number of samples and
        ``n_features`` is the number of features.

    value_to_mask : {int, float}
        The value which is to be masked in X.

    Returns
    -------
    X_mask : {ndarray, sparse matrix} of shape (n_samples, n_features)
        Missing mask.
    '''
    if not sp.issparse(X):
        return _get_dense_mask(X, value_to_mask)
    Xt = None(X.data, value_to_mask)
    sparse_constructor = sp.csr_matrix if X.format == 'csr' else sp.csc_matrix
    Xt_sparse = sparse_constructor((Xt, X.indices.copy(), X.indptr.copy()), shape = X.shape, dtype = bool)
    return Xt_sparse

safe_mask = (lambda X, mask: mask = np.asarray(mask)if np.issubdtype(mask.dtype, np.signedinteger):
maskif None(X, 'toarray'):
ind = np.arange(mask.shape[0])mask = ind[mask]mask)()

def axis0_safe_slice(X, mask, len_mask):
    '''Return a mask which is safer to use on X than safe_mask.

    This mask is safer than safe_mask since it returns an
    empty array, when a sparse matrix is sliced with a boolean mask
    with all False, instead of raising an unhelpful error in older
    versions of SciPy.

    See: https://github.com/scipy/scipy/issues/5361

    Also note that we can avoid doing the dot product by checking if
    the len_mask is not zero in _huber_loss_and_gradient but this
    is not going to be the bottleneck, since the number of outliers
    and non_outliers are typically non-zero and it makes the code
    tougher to follow.

    Parameters
    ----------
    X : {array-like, sparse matrix}
        Data on which to apply mask.

    mask : ndarray
        Mask to be used on X.

    len_mask : int
        The length of the mask.

    Returns
    -------
    mask : ndarray
        Array that is safe to use on X.
    '''
    if len_mask != 0:
        return X[(safe_mask(X, mask), :)]
    return None.zeros(shape = (0, X.shape[1]))


def indices_to_mask(indices, mask_length):
    '''Convert list of indices to boolean mask.

    Parameters
    ----------
    indices : list-like
        List of integers treated as indices.
    mask_length : int
        Length of boolean mask to be generated.
        This parameter must be greater than max(indices).

    Returns
    -------
    mask : 1d boolean nd-array
        Boolean array that is True where indices are present, else False.

    Examples
    --------
    >>> from sklearn.utils._mask import indices_to_mask
    >>> indices = [1, 2 , 3, 4]
    >>> indices_to_mask(indices, 5)
    array([False,  True,  True,  True,  True])
    '''
    if mask_length <= np.max(indices):
        raise ValueError('mask_length must be greater than max(indices)')
    mask = np.zeros(mask_length, dtype = bool)
    mask[indices] = True
    return mask
