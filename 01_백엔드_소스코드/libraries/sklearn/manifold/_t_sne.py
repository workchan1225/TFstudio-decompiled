# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _t_sne.pyc (Python 3.11)

from numbers import Integral, Real
from time import time
import numpy as np
from scipy import linalg
from scipy.sparse import csr_matrix, issparse
from scipy.spatial.distance import pdist, squareform
from sklearn.base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin, _fit_context
from sklearn.decomposition import PCA
from sklearn.manifold import _barnes_hut_tsne, _utils
from sklearn.metrics.pairwise import _VALID_METRICS, pairwise_distances
from sklearn.neighbors import NearestNeighbors
from sklearn.utils import check_random_state
from sklearn.utils._openmp_helpers import _openmp_effective_n_threads
from sklearn.utils._param_validation import Interval, StrOptions, validate_params
from sklearn.utils.validation import _num_samples, check_non_negative, validate_data
MACHINE_EPSILON = np.finfo(np.double).eps

def _joint_probabilities(distances, desired_perplexity, verbose):
    '''Compute joint probabilities p_ij from distances.

    Parameters
    ----------
    distances : ndarray of shape (n_samples * (n_samples-1) / 2,)
        Distances of samples are stored as condensed matrices, i.e.
        we omit the diagonal and duplicate entries and store everything
        in a one-dimensional array.

    desired_perplexity : float
        Desired perplexity of the joint probability distributions.

    verbose : int
        Verbosity level.

    Returns
    -------
    P : ndarray of shape (n_samples * (n_samples-1) / 2,)
        Condensed joint probability matrix.
    '''
    distances = distances.astype(np.float32, copy = False)
    conditional_P = _utils._binary_search_perplexity(distances, desired_perplexity, verbose)
    P = conditional_P + conditional_P.T
    sum_P = np.maximum(np.sum(P), MACHINE_EPSILON)
    P = np.maximum(squareform(P) / sum_P, MACHINE_EPSILON)
    return P


def _joint_probabilities_nn(distances, desired_perplexity, verbose):
    '''Compute joint probabilities p_ij from distances using just nearest
    neighbors.

    This method is approximately equal to _joint_probabilities. The latter
    is O(N), but limiting the joint probability to nearest neighbors improves
    this substantially to O(uN).

    Parameters
    ----------
    distances : sparse matrix of shape (n_samples, n_samples)
        Distances of samples to its n_neighbors nearest neighbors. All other
        distances are left to zero (and are not materialized in memory).
        Matrix should be of CSR format.

    desired_perplexity : float
        Desired perplexity of the joint probability distributions.

    verbose : int
        Verbosity level.

    Returns
    -------
    P : sparse matrix of shape (n_samples, n_samples)
        Condensed joint probability matrix with only nearest neighbors. Matrix
        will be of CSR format.
    '''
    t0 = time()
    distances.sort_indices()
    n_samples = distances.shape[0]
    distances_data = distances.data.reshape(n_samples, -1)
    distances_data = distances_data.astype(np.float32, copy = False)
    conditional_P = _utils._binary_search_perplexity(distances_data, desired_perplexity, verbose)
# WARNING: Decompyle incomplete


def _kl_divergence(params, P, degrees_of_freedom, n_samples, n_components, skip_num_points, compute_error = (0, True)):
    """t-SNE objective function: gradient of the KL divergence
    of p_ijs and q_ijs and the absolute error.

    Parameters
    ----------
    params : ndarray of shape (n_params,)
        Unraveled embedding.

    P : ndarray of shape (n_samples * (n_samples-1) / 2,)
        Condensed joint probability matrix.

    degrees_of_freedom : int
        Degrees of freedom of the Student's-t distribution.

    n_samples : int
        Number of samples.

    n_components : int
        Dimension of the embedded space.

    skip_num_points : int, default=0
        This does not compute the gradient for points with indices below
        `skip_num_points`. This is useful when computing transforms of new
        data where you'd like to keep the old data fixed.

    compute_error: bool, default=True
        If False, the kl_divergence is not computed and returns NaN.

    Returns
    -------
    kl_divergence : float
        Kullback-Leibler divergence of p_ij and q_ij.

    grad : ndarray of shape (n_params,)
        Unraveled gradient of the Kullback-Leibler divergence with respect to
        the embedding.
    """
    X_embedded = params.reshape(n_samples, n_components)
    dist = pdist(X_embedded, 'sqeuclidean')
    dist /= degrees_of_freedom
    dist += 1
    dist **= (degrees_of_freedom + 1) / -2
    Q = np.maximum(dist / (2 * np.sum(dist)), MACHINE_EPSILON)
    if compute_error:
        kl_divergence = 2 * np.dot(P, np.log(np.maximum(P, MACHINE_EPSILON) / Q))
    else:
        kl_divergence = np.nan
    grad = np.ndarray((n_samples, n_components), dtype = params.dtype)
    PQd = squareform((P - Q) * dist)
    for i in range(skip_num_points, n_samples):
        grad[i] = np.dot(np.ravel(PQd[i], order = 'K'), X_embedded[i] - X_embedded)
        grad = grad.ravel()
        c = 2 * (degrees_of_freedom + 1) / degrees_of_freedom
        grad *= c
        return (kl_divergence, grad)


def _kl_divergence_bh(params, P, degrees_of_freedom, n_samples, n_components, angle, skip_num_points, verbose, compute_error, num_threads = (0.5, 0, False, True, 1)):
    """t-SNE objective function: KL divergence of p_ijs and q_ijs.

    Uses Barnes-Hut tree methods to calculate the gradient that
    runs in O(NlogN) instead of O(N^2).

    Parameters
    ----------
    params : ndarray of shape (n_params,)
        Unraveled embedding.

    P : sparse matrix of shape (n_samples, n_sample)
        Sparse approximate joint probability matrix, computed only for the
        k nearest-neighbors and symmetrized. Matrix should be of CSR format.

    degrees_of_freedom : int
        Degrees of freedom of the Student's-t distribution.

    n_samples : int
        Number of samples.

    n_components : int
        Dimension of the embedded space.

    angle : float, default=0.5
        This is the trade-off between speed and accuracy for Barnes-Hut T-SNE.
        'angle' is the angular size (referred to as theta in [3]) of a distant
        node as measured from a point. If this size is below 'angle' then it is
        used as a summary node of all points contained within it.
        This method is not very sensitive to changes in this parameter
        in the range of 0.2 - 0.8. Angle less than 0.2 has quickly increasing
        computation time and angle greater 0.8 has quickly increasing error.

    skip_num_points : int, default=0
        This does not compute the gradient for points with indices below
        `skip_num_points`. This is useful when computing transforms of new
        data where you'd like to keep the old data fixed.

    verbose : int, default=False
        Verbosity level.

    compute_error: bool, default=True
        If False, the kl_divergence is not computed and returns NaN.

    num_threads : int, default=1
        Number of threads used to compute the gradient. This is set here to
        avoid calling _openmp_effective_n_threads for each gradient step.

    Returns
    -------
    kl_divergence : float
        Kullback-Leibler divergence of p_ij and q_ij.

    grad : ndarray of shape (n_params,)
        Unraveled gradient of the Kullback-Leibler divergence with respect to
        the embedding.
    """
    params = params.astype(np.float32, copy = False)
    X_embedded = params.reshape(n_samples, n_components)
    val_P = P.data.astype(np.float32, copy = False)
    neighbors = P.indices.astype(np.int64, copy = False)
    indptr = P.indptr.astype(np.int64, copy = False)
    grad = np.zeros(X_embedded.shape, dtype = np.float32)
    error = _barnes_hut_tsne.gradient(val_P, X_embedded, neighbors, indptr, grad, angle, n_components, verbose, dof = degrees_of_freedom, compute_error = compute_error, num_threads = num_threads)
    c = 2 * (degrees_of_freedom + 1) / degrees_of_freedom
    grad = grad.ravel()
    grad *= c
    return (error, grad)


def _gradient_descent(objective, p0, it, max_iter, n_iter_check, n_iter_without_progress, momentum, learning_rate, min_gain, min_grad_norm, verbose, args, kwargs = (1, 300, 0.8, 200, 0.01, 1e-07, 0, None, None)):
    """Batch gradient descent with momentum and individual gains.

    Parameters
    ----------
    objective : callable
        Should return a tuple of cost and gradient for a given parameter
        vector. When expensive to compute, the cost can optionally
        be None and can be computed every n_iter_check steps using
        the objective_error function.

    p0 : array-like of shape (n_params,)
        Initial parameter vector.

    it : int
        Current number of iterations (this function will be called more than
        once during the optimization).

    max_iter : int
        Maximum number of gradient descent iterations.

    n_iter_check : int, default=1
        Number of iterations before evaluating the global error. If the error
        is sufficiently low, we abort the optimization.

    n_iter_without_progress : int, default=300
        Maximum number of iterations without progress before we abort the
        optimization.

    momentum : float within (0.0, 1.0), default=0.8
        The momentum generates a weight for previous gradients that decays
        exponentially.

    learning_rate : float, default=200.0
        The learning rate for t-SNE is usually in the range [10.0, 1000.0]. If
        the learning rate is too high, the data may look like a 'ball' with any
        point approximately equidistant from its nearest neighbours. If the
        learning rate is too low, most points may look compressed in a dense
        cloud with few outliers.

    min_gain : float, default=0.01
        Minimum individual gain for each parameter.

    min_grad_norm : float, default=1e-7
        If the gradient norm is below this threshold, the optimization will
        be aborted.

    verbose : int, default=0
        Verbosity level.

    args : sequence, default=None
        Arguments to pass to objective function.

    kwargs : dict, default=None
        Keyword arguments to pass to objective function.

    Returns
    -------
    p : ndarray of shape (n_params,)
        Optimum parameters.

    error : float
        Optimum.

    i : int
        Last iteration.
    """
    pass
# WARNING: Decompyle incomplete

trustworthiness = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'X_embedded': [
        'array-like',
        'sparse matrix'],
    'n_neighbors': [
        Interval(Integral, 1, None, closed = 'left')],
    'metric': [
        StrOptions(set(_VALID_METRICS) | {
            'precomputed'}),
        callable] }, prefer_skip_nested_validation = True), X_embedded = {
    'n_neighbors': 5,
    'metric': 'euclidean' }, *, n_neighbors, metric: n_samples = _num_samples(X)if n_neighbors >= n_samples / 2:
raise ValueError(f'''n_neighbors ({n_neighbors}) should be less than n_samples / 2 ({n_samples / 2})''')dist_X = pairwise_distances(X, metric = metric)if metric == 'precomputed':
dist_X = dist_X.copy()np.fill_diagonal(dist_X, np.inf)ind_X = np.argsort(dist_X, axis = 1)ind_X_embedded = NearestNeighbors(n_neighbors = n_neighbors).fit(X_embedded).kneighbors(return_distance = False)inverted_index = np.zeros((n_samples, n_samples), dtype = int)ordered_indices = np.arange(n_samples + 1)inverted_index[(ordered_indices[(:-1, np.newaxis)], ind_X)] = ordered_indices[1:]ranks = inverted_index[(ordered_indices[(:-1, np.newaxis)], ind_X_embedded)] - n_neighborst = np.sum(ranks[ranks > 0])t = 1 - t * (2 / (n_samples * n_neighbors * (2 * n_samples - 3 * n_neighbors - 1)))t)()

class TSNE(BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin):
    pass
# WARNING: Decompyle incomplete
