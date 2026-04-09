# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _affinity_propagation.pyc (Python 3.11)

'''Affinity Propagation clustering algorithm.'''
import warnings
from numbers import Integral, Real
import numpy as np
from sklearn._config import config_context
from sklearn.base import BaseEstimator, ClusterMixin, _fit_context
from sklearn.exceptions import ConvergenceWarning
from sklearn.metrics import euclidean_distances, pairwise_distances_argmin
from sklearn.utils import check_random_state
from sklearn.utils._param_validation import Interval, StrOptions, validate_params
from sklearn.utils.validation import check_is_fitted, validate_data

def _equal_similarities_and_preferences(S, preference):
    pass
# WARNING: Decompyle incomplete


def _affinity_propagation(S, *, preference, convergence_iter, max_iter, damping, verbose, return_n_iter, random_state):
    '''Main affinity propagation algorithm.'''
    n_samples = S.shape[0]
    if n_samples == 1 or _equal_similarities_and_preferences(S, preference):
        warnings.warn('All samples have mutually equal similarities. Returning arbitrary cluster center(s).')
        if preference.flat[0] > S.flat[n_samples - 1]:
            return (np.arange(n_samples), np.arange(n_samples), 0) if return_n_iter else (np.arange(n_samples), np.arange(n_samples))
        return (np.array([
            0]), np.array([
            0] * n_samples), 0) if None else (np.array([
            0]), np.array([
            0] * n_samples))
    S.flat[::n_samples + 1] = None
    A = np.zeros((n_samples, n_samples))
    R = np.zeros((n_samples, n_samples))
    tmp = np.zeros((n_samples, n_samples))
    S += (np.finfo(S.dtype).eps * S + np.finfo(S.dtype).tiny * 100) * random_state.standard_normal(size = (n_samples, n_samples))
    e = np.zeros((n_samples, convergence_iter))
    ind = np.arange(n_samples)
    for it in range(max_iter):
        np.add(A, S, tmp)
        I = np.argmax(tmp, axis = 1)
        Y = tmp[(ind, I)]
        tmp[(ind, I)] = -(np.inf)
        Y2 = np.max(tmp, axis = 1)
        np.subtract(S, Y[(:, None)], tmp)
        tmp[(ind, I)] = S[(ind, I)] - Y2
        tmp *= 1 - damping
        R *= damping
        R += tmp
        np.maximum(R, 0, out = tmp)
        tmp.flat[::n_samples + 1] = R.flat[::n_samples + 1]
        tmp -= np.sum(tmp, axis = 0)
        dA = np.diag(tmp).copy()
        tmp.clip(0, np.inf, tmp)
        tmp.flat[::n_samples + 1] = dA
        tmp *= 1 - damping
        A *= damping
        A -= tmp
        E = np.diag(A) + np.diag(R) > 0
        e[(:, it % convergence_iter)] = E
        K = np.sum(E, axis = 0)
        if it >= convergence_iter:
            se = np.sum(e, axis = 1)
            unconverged = np.sum((se == convergence_iter) + (se == 0)) != n_samples
            if unconverged or K > 0 or it == max_iter:
                never_converged = False
                if verbose:
                    print('Converged after %d iterations.' % it)
            
            never_converged = True
            if verbose:
                print('Did not converge')
    I = np.flatnonzero(E)
    K = I.size
    if K > 0:
        if never_converged:
            warnings.warn('Affinity propagation did not converge, this model may return degenerate cluster centers and labels.', ConvergenceWarning)
        c = np.argmax(S[(:, I)], axis = 1)
        c[I] = np.arange(K)
        for k in range(K):
            ii = np.asarray(c == k).nonzero()[0]
            j = np.argmax(np.sum(S[(ii[(:, np.newaxis)], ii)], axis = 0))
            I[k] = ii[j]
            c = np.argmax(S[(:, I)], axis = 1)
            c[I] = np.arange(K)
            labels = I[c]
            cluster_centers_indices = np.unique(labels)
            labels = np.searchsorted(cluster_centers_indices, labels)
    warnings.warn('Affinity propagation did not converge and this model will not have any cluster centers.', ConvergenceWarning)
    labels = np.array([
        -1] * n_samples)
    cluster_centers_indices = []
    if return_n_iter:
        return (cluster_centers_indices, labels, it + 1)
    return (None, labels)

affinity_propagation = (lambda S = validate_params({
    'S': [
        'array-like'],
    'return_n_iter': [
        'boolean'] }, prefer_skip_nested_validation = False), *, preference: estimator = AffinityPropagation(damping = damping, max_iter = max_iter, convergence_iter = convergence_iter, copy = copy, preference = preference, affinity = 'precomputed', verbose = verbose, random_state = random_state).fit(S)if return_n_iter:
(estimator.cluster_centers_indices_, estimator.labels_, estimator.n_iter_)(None.cluster_centers_indices_, estimator.labels_))()

class AffinityPropagation(BaseEstimator, ClusterMixin):
    pass
# WARNING: Decompyle incomplete
