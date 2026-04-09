# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _mds.pyc (Python 3.11)

'''
Multi-dimensional Scaling (MDS).
'''
import warnings
from numbers import Integral, Real
import numpy as np
from joblib import effective_n_jobs
from sklearn.base import BaseEstimator, _fit_context
from sklearn.isotonic import IsotonicRegression
from sklearn.manifold import ClassicalMDS
from sklearn.metrics import euclidean_distances, pairwise_distances
from sklearn.utils import check_array, check_random_state, check_symmetric
from sklearn.utils._param_validation import Hidden, Interval, StrOptions, validate_params
from sklearn.utils.parallel import Parallel, delayed
from sklearn.utils.validation import validate_data

def _smacof_single(dissimilarities, metric, n_components, init, max_iter, verbose, eps, random_state, normalized_stress = (True, 2, None, 300, 0, 1e-06, None, False)):
    '''Computes multidimensional scaling using SMACOF algorithm.

    Parameters
    ----------
    dissimilarities : ndarray of shape (n_samples, n_samples)
        Pairwise dissimilarities between the points. Must be symmetric.

    metric : bool, default=True
        Compute metric or nonmetric SMACOF algorithm.
        When ``False`` (i.e. non-metric MDS), dissimilarities with 0 are considered as
        missing values.

    n_components : int, default=2
        Number of dimensions in which to immerse the dissimilarities. If an
        ``init`` array is provided, this option is overridden and the shape of
        ``init`` is used to determine the dimensionality of the embedding
        space.

    init : ndarray of shape (n_samples, n_components), default=None
        Starting configuration of the embedding to initialize the algorithm. By
        default, the algorithm is initialized with a randomly chosen array.

    max_iter : int, default=300
        Maximum number of iterations of the SMACOF algorithm for a single run.

    verbose : int, default=0
        Level of verbosity.

    eps : float, default=1e-6
        The tolerance with respect to stress (normalized by the sum of squared
        embedding distances) at which to declare convergence.

        .. versionchanged:: 1.7
           The default value for `eps` has changed from 1e-3 to 1e-6, as a result
           of a bugfix in the computation of the convergence criterion.

    random_state : int, RandomState instance or None, default=None
        Determines the random number generator used to initialize the centers.
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    normalized_stress : bool, default=False
        Whether to return normalized stress value (Stress-1) instead of raw
        stress.

        .. versionadded:: 1.2

        .. versionchanged:: 1.7
           Normalized stress is now supported for metric MDS as well.

    Returns
    -------
    X : ndarray of shape (n_samples, n_components)
        Coordinates of the points in a ``n_components``-space.

    stress : float
        The final value of the stress (sum of squared distance of the
        disparities and the distances for all constrained points).
        If `normalized_stress=True`, returns Stress-1.
        A value of 0 indicates "perfect" fit, 0.025 excellent, 0.05 good,
        0.1 fair, and 0.2 poor [1]_.

    n_iter : int
        The number of iterations corresponding to the best stress.

    References
    ----------
    .. [1] "Nonmetric multidimensional scaling: a numerical method" Kruskal, J.
           Psychometrika, 29 (1964)

    .. [2] "Multidimensional scaling by optimizing goodness of fit to a nonmetric
           hypothesis" Kruskal, J. Psychometrika, 29, (1964)

    .. [3] "Modern Multidimensional Scaling - Theory and Applications" Borg, I.;
           Groenen P. Springer Series in Statistics (1997)
    '''
    dissimilarities = check_symmetric(dissimilarities, raise_exception = True)
    n_samples = dissimilarities.shape[0]
    random_state = check_random_state(random_state)
    dissimilarities_flat = ((1 - np.tri(n_samples)) * dissimilarities).ravel()
    dissimilarities_flat_w = dissimilarities_flat[dissimilarities_flat != 0]
# WARNING: Decompyle incomplete

smacof = (lambda dissimilarities = validate_params({
    'dissimilarities': [
        'array-like'],
    'metric': [
        'boolean'],
    'n_components': [
        Interval(Integral, 1, None, closed = 'left')],
    'init': [
        'array-like',
        None],
    'n_init': [
        Interval(Integral, 1, None, closed = 'left'),
        StrOptions({
            'warn'})],
    'n_jobs': [
        Integral,
        None],
    'max_iter': [
        Interval(Integral, 1, None, closed = 'left')],
    'verbose': [
        'verbose'],
    'eps': [
        Interval(Real, 0, None, closed = 'left')],
    'random_state': [
        'random_state'],
    'return_n_iter': [
        'boolean'],
    'normalized_stress': [
        'boolean',
        StrOptions({
            'auto'})] }, prefer_skip_nested_validation = True), *, metric: pass# WARNING: Decompyle incomplete
)()

class MDS(BaseEstimator):
    pass
# WARNING: Decompyle incomplete
