# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _kmeans.pyc (Python 3.11)

'''K-means clustering.'''
import warnings
from abc import ABC, abstractmethod
from numbers import Integral, Real
import numpy as np
from scipy.sparse import sparse as sp
from sklearn.base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, ClusterMixin, TransformerMixin, _fit_context
from sklearn.cluster._k_means_common import CHUNK_SIZE, _inertia_dense, _inertia_sparse, _is_same_clustering
from sklearn.cluster._k_means_elkan import elkan_iter_chunked_dense, elkan_iter_chunked_sparse, init_bounds_dense, init_bounds_sparse
from sklearn.cluster._k_means_lloyd import lloyd_iter_chunked_dense, lloyd_iter_chunked_sparse
from sklearn.cluster._k_means_minibatch import _minibatch_update_dense, _minibatch_update_sparse
from sklearn.exceptions import ConvergenceWarning
from sklearn.metrics.pairwise import _euclidean_distances, euclidean_distances
from sklearn.utils import check_array, check_random_state
from sklearn.utils._openmp_helpers import _openmp_effective_n_threads
from sklearn.utils._param_validation import Interval, StrOptions, validate_params
from sklearn.utils.extmath import row_norms
from sklearn.utils.parallel import _get_threadpool_controller, _threadpool_controller_decorator
from sklearn.utils.sparsefuncs import mean_variance_axis
from sklearn.utils.sparsefuncs_fast import assign_rows_csr
from sklearn.utils.validation import _check_sample_weight, _is_arraylike_not_scalar, check_is_fitted, validate_data
kmeans_plusplus = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'n_clusters': [
        Interval(Integral, 1, None, closed = 'left')],
    'sample_weight': [
        'array-like',
        None],
    'x_squared_norms': [
        'array-like',
        None],
    'random_state': [
        'random_state'],
    'n_local_trials': [
        Interval(Integral, 1, None, closed = 'left'),
        None] }, prefer_skip_nested_validation = True), n_clusters = {
    'sample_weight': None,
    'x_squared_norms': None,
    'random_state': None,
    'n_local_trials': None }, *, sample_weight, x_squared_norms: check_array(X, accept_sparse = 'csr', dtype = [
np.float64,
np.float32])sample_weight = _check_sample_weight(sample_weight, X, dtype = X.dtype)if X.shape[0] < n_clusters:
raise ValueError(f'''n_samples={X.shape[0]} should be >= n_clusters={n_clusters}.''')# WARNING: Decompyle incomplete
)()

def _kmeans_plusplus(X, n_clusters, x_squared_norms, sample_weight, random_state, n_local_trials = (None,)):
    '''Computational component for initialization of n_clusters by
    k-means++. Prior validation of data is assumed.

    Parameters
    ----------
    X : {ndarray, sparse matrix} of shape (n_samples, n_features)
        The data to pick seeds for.

    n_clusters : int
        The number of seeds to choose.

    sample_weight : ndarray of shape (n_samples,)
        The weights for each observation in `X`.

    x_squared_norms : ndarray of shape (n_samples,)
        Squared Euclidean norm of each data point.

    random_state : RandomState instance
        The generator used to initialize the centers.
        See :term:`Glossary <random_state>`.

    n_local_trials : int, default=None
        The number of seeding trials for each center (except the first),
        of which the one reducing inertia the most is greedily chosen.
        Set to None to make the number of trials depend logarithmically
        on the number of seeds (2+log(k)); this is the default.

    Returns
    -------
    centers : ndarray of shape (n_clusters, n_features)
        The initial centers for k-means.

    indices : ndarray of shape (n_clusters,)
        The index location of the chosen centers in the data array X. For a
        given index and center, X[index] = center.
    '''
    (n_samples, n_features) = X.shape
    centers = np.empty((n_clusters, n_features), dtype = X.dtype)
# WARNING: Decompyle incomplete


def _tolerance(X, tol):
    '''Return a tolerance which is dependent on the dataset.'''
    if tol == 0:
        return 0
    if None.issparse(X):
        variances = mean_variance_axis(X, axis = 0)[1]
    else:
        variances = np.var(X, axis = 0)
    return np.mean(variances) * tol

k_means = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'sample_weight': [
        'array-like',
        None],
    'return_n_iter': [
        bool] }, prefer_skip_nested_validation = False), n_clusters = {
    'sample_weight': None,
    'init': 'k-means++',
    'n_init': 'auto',
    'max_iter': 300,
    'verbose': False,
    'tol': 0.0001,
    'random_state': None,
    'copy_x': True,
    'algorithm': 'lloyd',
    'return_n_iter': False }, *, sample_weight, init: est = KMeans(n_clusters = n_clusters, init = init, n_init = n_init, max_iter = max_iter, verbose = verbose, tol = tol, random_state = random_state, copy_x = copy_x, algorithm = algorithm).fit(X, sample_weight = sample_weight)if return_n_iter:
(est.cluster_centers_, est.labels_, est.inertia_, est.n_iter_)(None.cluster_centers_, est.labels_, est.inertia_))()

def _kmeans_single_elkan(X, sample_weight, centers_init, max_iter, verbose, tol, n_threads = (300, False, 0.0001, 1)):
    """A single run of k-means elkan, assumes preparation completed prior.

    Parameters
    ----------
    X : {ndarray, sparse matrix} of shape (n_samples, n_features)
        The observations to cluster. If sparse matrix, must be in CSR format.

    sample_weight : array-like of shape (n_samples,)
        The weights for each observation in X.

    centers_init : ndarray of shape (n_clusters, n_features)
        The initial centers.

    max_iter : int, default=300
        Maximum number of iterations of the k-means algorithm to run.

    verbose : bool, default=False
        Verbosity mode.

    tol : float, default=1e-4
        Relative tolerance with regards to Frobenius norm of the difference
        in the cluster centers of two consecutive iterations to declare
        convergence.
        It's not advised to set `tol=0` since convergence might never be
        declared due to rounding errors. Use a very small number instead.

    n_threads : int, default=1
        The number of OpenMP threads to use for the computation. Parallelism is
        sample-wise on the main cython loop which assigns each sample to its
        closest center.

    Returns
    -------
    centroid : ndarray of shape (n_clusters, n_features)
        Centroids found at the last iteration of k-means.

    label : ndarray of shape (n_samples,)
        label[i] is the code or index of the centroid the
        i'th observation is closest to.

    inertia : float
        The final value of the inertia criterion (sum of squared distances to
        the closest centroid for all observations in the training set).

    n_iter : int
        Number of iterations run.
    """
    n_samples = X.shape[0]
    n_clusters = centers_init.shape[0]
    centers = centers_init
    centers_new = np.zeros_like(centers)
    weight_in_clusters = np.zeros(n_clusters, dtype = X.dtype)
    labels = np.full(n_samples, -1, dtype = np.int32)
    labels_old = labels.copy()
    center_half_distances = euclidean_distances(centers) / 2
    distance_next_center = np.partition(np.asarray(center_half_distances), kth = 1, axis = 0)[1]
    upper_bounds = np.zeros(n_samples, dtype = X.dtype)
    lower_bounds = np.zeros((n_samples, n_clusters), dtype = X.dtype)
    center_shift = np.zeros(n_clusters, dtype = X.dtype)
    if sp.issparse(X):
        init_bounds = init_bounds_sparse
        elkan_iter = elkan_iter_chunked_sparse
        _inertia = _inertia_sparse
    else:
        init_bounds = init_bounds_dense
        elkan_iter = elkan_iter_chunked_dense
        _inertia = _inertia_dense
    init_bounds(X, centers, center_half_distances, labels, upper_bounds, lower_bounds, n_threads = n_threads)
    strict_convergence = False
    for i in range(max_iter):
        elkan_iter(X, sample_weight, centers, centers_new, weight_in_clusters, center_half_distances, distance_next_center, upper_bounds, lower_bounds, labels, center_shift, n_threads)
        center_half_distances = euclidean_distances(centers_new) / 2
        distance_next_center = np.partition(np.asarray(center_half_distances), kth = 1, axis = 0)[1]
        if verbose:
            inertia = _inertia(X, sample_weight, centers, labels, n_threads)
            print(f'''Iteration {i}, inertia {inertia}''')
        centers_new = centers
        centers = centers_new
        if np.array_equal(labels, labels_old):
            if verbose:
                print(f'''Converged at iteration {i}: strict convergence.''')
            strict_convergence = True
        else:
            center_shift_tot = (center_shift ** 2).sum()
            if center_shift_tot <= tol:
                if verbose:
                    print(f'''Converged at iteration {i}: center shift {center_shift_tot} within tolerance {tol}.''')
            else:
                labels_old[:] = labels
    if not strict_convergence:
        elkan_iter(X, sample_weight, centers, centers, weight_in_clusters, center_half_distances, distance_next_center, upper_bounds, lower_bounds, labels, center_shift, n_threads, update_centers = False)
    inertia = _inertia(X, sample_weight, centers, labels, n_threads)
    return (labels, inertia, centers, i + 1)

_kmeans_single_lloyd = (lambda X, sample_weight, centers_init, max_iter, verbose, tol, n_threads = (300, False, 0.0001, 1): n_clusters = centers_init.shape[0]centers = centers_initcenters_new = np.zeros_like(centers)labels = np.full(X.shape[0], -1, dtype = np.int32)labels_old = labels.copy()weight_in_clusters = np.zeros(n_clusters, dtype = X.dtype)center_shift = np.zeros(n_clusters, dtype = X.dtype)if sp.issparse(X):
lloyd_iter = lloyd_iter_chunked_sparse_inertia = _inertia_sparseelse:
lloyd_iter = lloyd_iter_chunked_dense_inertia = _inertia_densestrict_convergence = Falsefor i in range(max_iter):
lloyd_iter(X, sample_weight, centers, centers_new, weight_in_clusters, labels, center_shift, n_threads)if verbose:
inertia = _inertia(X, sample_weight, centers, labels, n_threads)print(f'''Iteration {i}, inertia {inertia}.''')centers_new = centerscenters = centers_newif np.array_equal(labels, labels_old):
if verbose:
print(f'''Converged at iteration {i}: strict convergence.''')strict_convergence = Trueelse:
center_shift_tot = (center_shift ** 2).sum()if center_shift_tot <= tol:
if verbose:
print(f'''Converged at iteration {i}: center shift {center_shift_tot} within tolerance {tol}.''')else:
labels_old[:] = labelsif not strict_convergence:
lloyd_iter(X, sample_weight, centers, centers, weight_in_clusters, labels, center_shift, n_threads, update_centers = False)inertia = _inertia(X, sample_weight, centers, labels, n_threads)(labels, inertia, centers, i + 1))()

def _labels_inertia(X, sample_weight, centers, n_threads, return_inertia = (1, True)):
    '''E step of the K-means EM algorithm.

    Compute the labels and the inertia of the given samples and centers.

    Parameters
    ----------
    X : {ndarray, sparse matrix} of shape (n_samples, n_features)
        The input samples to assign to the labels. If sparse matrix, must
        be in CSR format.

    sample_weight : ndarray of shape (n_samples,)
        The weights for each observation in X.

    x_squared_norms : ndarray of shape (n_samples,)
        Precomputed squared euclidean norm of each data point, to speed up
        computations.

    centers : ndarray of shape (n_clusters, n_features)
        The cluster centers.

    n_threads : int, default=1
        The number of OpenMP threads to use for the computation. Parallelism is
        sample-wise on the main cython loop which assigns each sample to its
        closest center.

    return_inertia : bool, default=True
        Whether to compute and return the inertia.

    Returns
    -------
    labels : ndarray of shape (n_samples,)
        The resulting assignment.

    inertia : float
        Sum of squared distances of samples to their closest cluster center.
        Inertia is only returned if return_inertia is True.
    '''
    n_samples = X.shape[0]
    n_clusters = centers.shape[0]
    labels = np.full(n_samples, -1, dtype = np.int32)
    center_shift = np.zeros(n_clusters, dtype = centers.dtype)
    if sp.issparse(X):
        _labels = lloyd_iter_chunked_sparse
        _inertia = _inertia_sparse
    else:
        _labels = lloyd_iter_chunked_dense
        _inertia = _inertia_dense
    _labels(X, sample_weight, centers, centers_new = None, weight_in_clusters = None, labels = labels, center_shift = center_shift, n_threads = n_threads, update_centers = False)
    if return_inertia:
        inertia = _inertia(X, sample_weight, centers, labels, n_threads)
        return (labels, inertia)

_labels_inertia_threadpool_limit = _threadpool_controller_decorator(limits = 1, user_api = 'blas')(_labels_inertia)

class _BaseKMeans(ABC, BaseEstimator, ClusterMixin, TransformerMixin, ClassNamePrefixFeaturesOutMixin):
    pass
# WARNING: Decompyle incomplete


class KMeans(_BaseKMeans):
    pass
# WARNING: Decompyle incomplete


def _mini_batch_step(X, sample_weight, centers, centers_new, weight_sums, random_state, random_reassign, reassignment_ratio, verbose, n_threads = (False, 0.01, False, 1)):
    '''Incremental update of the centers for the Minibatch K-Means algorithm.

    Parameters
    ----------

    X : {ndarray, sparse matrix} of shape (n_samples, n_features)
        The original data array. If sparse, must be in CSR format.

    x_squared_norms : ndarray of shape (n_samples,)
        Squared euclidean norm of each data point.

    sample_weight : ndarray of shape (n_samples,)
        The weights for each observation in `X`.

    centers : ndarray of shape (n_clusters, n_features)
        The cluster centers before the current iteration

    centers_new : ndarray of shape (n_clusters, n_features)
        The cluster centers after the current iteration. Modified in-place.

    weight_sums : ndarray of shape (n_clusters,)
        The vector in which we keep track of the numbers of points in a
        cluster. This array is modified in place.

    random_state : RandomState instance
        Determines random number generation for low count centers reassignment.
        See :term:`Glossary <random_state>`.

    random_reassign : boolean, default=False
        If True, centers with very low counts are randomly reassigned
        to observations.

    reassignment_ratio : float, default=0.01
        Control the fraction of the maximum number of counts for a
        center to be reassigned. A higher value means that low count
        centers are more likely to be reassigned, which means that the
        model will take longer to converge, but should converge in a
        better clustering.

    verbose : bool, default=False
        Controls the verbosity.

    n_threads : int, default=1
        The number of OpenMP threads to use for the computation.

    Returns
    -------
    inertia : float
        Sum of squared distances of samples to their closest cluster center.
        The inertia is computed after finding the labels and before updating
        the centers.
    '''
    (labels, inertia) = _labels_inertia(X, sample_weight, centers, n_threads = n_threads)
    if sp.issparse(X):
        _minibatch_update_sparse(X, sample_weight, centers, centers_new, weight_sums, labels, n_threads)
    else:
        _minibatch_update_dense(X, sample_weight, centers, centers_new, weight_sums, labels, n_threads)
    if random_reassign and reassignment_ratio > 0:
        to_reassign = weight_sums < reassignment_ratio * weight_sums.max()
        if to_reassign.sum() > 0.5 * X.shape[0]:
            indices_dont_reassign = np.argsort(weight_sums)[int(0.5 * X.shape[0]):]
            to_reassign[indices_dont_reassign] = False
        n_reassigns = to_reassign.sum()
        if n_reassigns:
            new_centers = random_state.choice(X.shape[0], replace = False, size = n_reassigns)
            if verbose:
                print(f'''[MiniBatchKMeans] Reassigning {n_reassigns} cluster centers.''')
            if sp.issparse(X):
                assign_rows_csr(X, new_centers.astype(np.intp, copy = False), np.where(to_reassign)[0].astype(np.intp, copy = False), centers_new)
            else:
                centers_new[to_reassign] = X[new_centers]
        weight_sums[to_reassign] = np.min(weight_sums[~to_reassign])
    return inertia


class MiniBatchKMeans(_BaseKMeans):
    pass
# WARNING: Decompyle incomplete
