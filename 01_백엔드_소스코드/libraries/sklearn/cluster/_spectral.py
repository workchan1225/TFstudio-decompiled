# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _spectral.pyc (Python 3.11)

'''Algorithms for spectral clustering'''
import warnings
from numbers import Integral, Real
import numpy as np
from scipy.linalg import LinAlgError, qr, svd
from scipy.sparse import csc_matrix
from sklearn.base import BaseEstimator, ClusterMixin, _fit_context
from sklearn.cluster._kmeans import k_means
from sklearn.manifold._spectral_embedding import _spectral_embedding
from sklearn.metrics.pairwise import KERNEL_PARAMS, pairwise_kernels
from sklearn.neighbors import NearestNeighbors, kneighbors_graph
from sklearn.utils import as_float_array, check_random_state
from sklearn.utils._param_validation import Interval, StrOptions, validate_params
from sklearn.utils.validation import validate_data

def cluster_qr(vectors):
    '''Find the discrete partition closest to the eigenvector embedding.

        This implementation was proposed in [1]_.

    .. versionadded:: 1.1

        Parameters
        ----------
        vectors : array-like, shape: (n_samples, n_clusters)
            The embedding space of the samples.

        Returns
        -------
        labels : array of integers, shape: n_samples
            The cluster labels of vectors.

        References
        ----------
        .. [1] :doi:`Simple, direct, and efficient multi-way spectral clustering, 2019
            Anil Damle, Victor Minden, Lexing Ying
            <10.1093/imaiai/iay008>`

    '''
    k = vectors.shape[1]
    (_, _, piv) = qr(vectors.T, pivoting = True)
    (ut, _, v) = svd(vectors[(piv[:k], :)].T)
    vectors = abs(np.dot(vectors, np.dot(ut, v.conj())))
    return vectors.argmax(axis = 1)


def discretize(vectors = None, *, copy, max_svd_restarts, n_iter_max, random_state):
    '''Search for a partition matrix which is closest to the eigenvector embedding.

    This implementation was proposed in [1]_.

    Parameters
    ----------
    vectors : array-like of shape (n_samples, n_clusters)
        The embedding space of the samples.

    copy : bool, default=True
        Whether to copy vectors, or perform in-place normalization.

    max_svd_restarts : int, default=30
        Maximum number of attempts to restart SVD if convergence fails

    n_iter_max : int, default=30
        Maximum number of iterations to attempt in rotation and partition
        matrix search if machine precision convergence is not reached

    random_state : int, RandomState instance, default=None
        Determines random number generation for rotation matrix initialization.
        Use an int to make the randomness deterministic.
        See :term:`Glossary <random_state>`.

    Returns
    -------
    labels : array of integers, shape: n_samples
        The labels of the clusters.

    References
    ----------

    .. [1] `Multiclass spectral clustering, 2003
           Stella X. Yu, Jianbo Shi
           <https://people.eecs.berkeley.edu/~jordan/courses/281B-spring04/readings/yu-shi.pdf>`_

    Notes
    -----

    The eigenvector embedding is used to iteratively search for the
    closest discrete partition.  First, the eigenvector embedding is
    normalized to the space of partition matrices. An optimal discrete
    partition matrix closest to this normalized embedding multiplied by
    an initial rotation is calculated.  Fixing this discrete partition
    matrix, an optimal rotation matrix is calculated.  These two
    calculations are performed until convergence.  The discrete partition
    matrix is returned as the clustering solution.  Used in spectral
    clustering, this method tends to be faster and more robust to random
    initialization than k-means.

    '''
    random_state = check_random_state(random_state)
    vectors = as_float_array(vectors, copy = copy)
    eps = np.finfo(float).eps
    (n_samples, n_components) = vectors.shape
    norm_ones = np.sqrt(n_samples)
# WARNING: Decompyle incomplete

spectral_clustering = (lambda affinity = validate_params({
    'affinity': [
        'array-like',
        'sparse matrix'] }, prefer_skip_nested_validation = False), *, n_clusters: clusterer = SpectralClustering(n_clusters = n_clusters, n_components = n_components, eigen_solver = eigen_solver, random_state = random_state, n_init = n_init, affinity = 'precomputed', eigen_tol = eigen_tol, assign_labels = assign_labels, verbose = verbose).fit(affinity)clusterer.labels_)()

class SpectralClustering(BaseEstimator, ClusterMixin):
    pass
# WARNING: Decompyle incomplete
