# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _bicluster.pyc (Python 3.11)

'''Spectral biclustering algorithms.'''
from abc import ABCMeta, abstractmethod
from numbers import Integral
import numpy as np
from scipy.linalg import norm
from scipy.sparse import dia_matrix, issparse
from scipy.sparse.linalg import eigsh, svds
from sklearn.base import BaseEstimator, BiclusterMixin, _fit_context
from sklearn.cluster._kmeans import KMeans, MiniBatchKMeans
from sklearn.utils import check_random_state, check_scalar
from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.utils.extmath import _randomized_svd, make_nonnegative, safe_sparse_dot
from sklearn.utils.validation import assert_all_finite, validate_data
__all__ = [
    'SpectralBiclustering',
    'SpectralCoclustering']

def _scale_normalize(X):
    '''Normalize ``X`` by scaling rows and columns independently.

    Returns the normalized matrix and the row and column scaling
    factors.
    '''
    X = make_nonnegative(X)
    row_diag = np.asarray(1 / np.sqrt(X.sum(axis = 1))).squeeze()
    col_diag = np.asarray(1 / np.sqrt(X.sum(axis = 0))).squeeze()
    row_diag = np.where(np.isnan(row_diag), 0, row_diag)
    col_diag = np.where(np.isnan(col_diag), 0, col_diag)
    if issparse(X):
        (n_rows, n_cols) = X.shape
        r = dia_matrix((row_diag, [
            0]), shape = (n_rows, n_rows))
        c = dia_matrix((col_diag, [
            0]), shape = (n_cols, n_cols))
        an = r @ X @ c
    else:
        an = row_diag[(:, np.newaxis)] * X * col_diag
    return (an, row_diag, col_diag)


def _bistochastic_normalize(X, max_iter, tol = (1000, 1e-05)):
    '''Normalize rows and columns of ``X`` simultaneously so that all
    rows sum to one constant and all columns sum to a different
    constant.
    '''
    X = make_nonnegative(X)
    X_scaled = X
# WARNING: Decompyle incomplete


def _log_normalize(X):
    """Normalize ``X`` according to Kluger's log-interactions scheme."""
    X = make_nonnegative(X, min_value = 1)
    if issparse(X):
        raise ValueError('Cannot compute log of a sparse matrix, because log(x) diverges to -infinity as x goes to 0.')
    L = np.log(X)
    row_avg = L.mean(axis = 1)[(:, np.newaxis)]
    col_avg = L.mean(axis = 0)
    avg = L.mean()
    return (L - row_avg - col_avg) + avg


def BaseSpectral():
    '''BaseSpectral'''
    pass
# WARNING: Decompyle incomplete

BaseSpectral = <NODE:27>(BaseSpectral, 'BaseSpectral', BiclusterMixin, BaseEstimator, metaclass = ABCMeta)

class SpectralCoclustering(BaseSpectral):
    pass
# WARNING: Decompyle incomplete


class SpectralBiclustering(BaseSpectral):
    pass
# WARNING: Decompyle incomplete
