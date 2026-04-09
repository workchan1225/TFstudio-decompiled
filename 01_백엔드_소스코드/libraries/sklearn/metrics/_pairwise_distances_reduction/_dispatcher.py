# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _dispatcher.pyc (Python 3.11)

from abc import abstractmethod
from typing import List
import numpy as np
from scipy.sparse import issparse
from sklearn import get_config
from sklearn.metrics._dist_metrics import BOOL_METRICS, METRIC_MAPPING64, DistanceMetric
from sklearn.metrics._pairwise_distances_reduction._argkmin import ArgKmin32, ArgKmin64
from sklearn.metrics._pairwise_distances_reduction._argkmin_classmode import ArgKminClassMode32, ArgKminClassMode64
from sklearn.metrics._pairwise_distances_reduction._base import _sqeuclidean_row_norms32, _sqeuclidean_row_norms64
from sklearn.metrics._pairwise_distances_reduction._radius_neighbors import RadiusNeighbors32, RadiusNeighbors64
from sklearn.metrics._pairwise_distances_reduction._radius_neighbors_classmode import RadiusNeighborsClassMode32, RadiusNeighborsClassMode64

def sqeuclidean_row_norms(X, num_threads):
    '''Compute the squared euclidean norm of the rows of X in parallel.

    Parameters
    ----------
    X : ndarray or CSR matrix of shape (n_samples, n_features)
        Input data. Must be c-contiguous.

    num_threads : int
        The number of OpenMP threads to use.

    Returns
    -------
    sqeuclidean_row_norms : ndarray of shape (n_samples,)
        Arrays containing the squared euclidean norm of each row of X.
    '''
    if X.dtype == np.float64:
        return np.asarray(_sqeuclidean_row_norms64(X, num_threads))
    if None.dtype == np.float32:
        return np.asarray(_sqeuclidean_row_norms32(X, num_threads))
    raise None(f'''Only float64 or float32 datasets are supported at this time, got: X.dtype={X.dtype}.''')


class BaseDistancesReductionDispatcher:
    '''Abstract base dispatcher for pairwise distance computation & reduction.

    Each dispatcher extending the base :class:`BaseDistancesReductionDispatcher`
    dispatcher must implement the :meth:`compute` classmethod.
    '''
    valid_metrics = (lambda cls = None: excluded = Nonesorted(({
'sqeuclidean'} | set(METRIC_MAPPING64.keys())) - excluded))()
    is_usable_for = (lambda cls = None, X = None, Y = classmethod, metric = ('return', bool):
