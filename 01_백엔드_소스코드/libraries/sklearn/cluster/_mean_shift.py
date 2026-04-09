# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _mean_shift.pyc (Python 3.11)

'''Mean shift clustering algorithm.

Mean shift clustering aims to discover *blobs* in a smooth density of
samples. It is a centroid based algorithm, which works by updating candidates
for centroids to be the mean of the points within a given region. These
candidates are then filtered in a post-processing stage to eliminate
near-duplicates to form the final set of centroids.

Seeding is performed using a binning technique for scalability.
'''
import warnings
from collections import defaultdict
from numbers import Integral, Real
import numpy as np
from sklearn._config import config_context
from sklearn.base import BaseEstimator, ClusterMixin, _fit_context
from sklearn.metrics.pairwise import pairwise_distances_argmin
from sklearn.neighbors import NearestNeighbors
from sklearn.utils import check_array, check_random_state, gen_batches
from sklearn.utils._param_validation import Interval, validate_params
from sklearn.utils.parallel import Parallel, delayed
from sklearn.utils.validation import check_is_fitted, validate_data
estimate_bandwidth = (lambda X = validate_params({
    'X': [
        'array-like'],
    'quantile': [
        Interval(Real, 0, 1, closed = 'both')],
    'n_samples': [
        Interval(Integral, 1, None, closed = 'left'),
        None],
    'random_state': [
        'random_state'],
    'n_jobs': [
        Integral,
        None] }, prefer_skip_nested_validation = True), *, quantile: X = check_array(X)random_state = check_random_state(random_state)# WARNING: Decompyle incomplete
)()

def _mean_shift_single_seed(my_mean, X, nbrs, max_iter):
    bandwidth = nbrs.get_params()['radius']
    stop_thresh = 0.001 * bandwidth
    completed_iterations = 0
    i_nbrs = nbrs.radius_neighbors([
        my_mean], bandwidth, return_distance = False)[0]
    points_within = X[i_nbrs]
    if len(points_within) == 0:
        pass
    else:
        my_old_mean = my_mean
        my_mean = np.mean(points_within, axis = 0)
        if np.linalg.norm(my_mean - my_old_mean) <= stop_thresh or completed_iterations == max_iter:
            pass
        else:
            completed_iterations += 1
    return (tuple(my_mean), len(points_within), completed_iterations)

mean_shift = (lambda X = validate_params({
    'X': [
        'array-like'] }, prefer_skip_nested_validation = False), *, bandwidth: model = MeanShift(bandwidth = bandwidth, seeds = seeds, min_bin_freq = min_bin_freq, bin_seeding = bin_seeding, cluster_all = cluster_all, n_jobs = n_jobs, max_iter = max_iter).fit(X)(model.cluster_centers_, model.labels_))()

def get_bin_seeds(X, bin_size, min_bin_freq = (1,)):
    """Find seeds for mean_shift.

    Finds seeds by first binning data onto a grid whose lines are
    spaced bin_size apart, and then choosing those bins with at least
    min_bin_freq points.

    Parameters
    ----------

    X : array-like of shape (n_samples, n_features)
        Input points, the same points that will be used in mean_shift.

    bin_size : float
        Controls the coarseness of the binning. Smaller values lead
        to more seeding (which is computationally more expensive). If you're
        not sure how to set this, set it to the value of the bandwidth used
        in clustering.mean_shift.

    min_bin_freq : int, default=1
        Only bins with at least min_bin_freq will be selected as seeds.
        Raising this value decreases the number of seeds found, which
        makes mean_shift computationally cheaper.

    Returns
    -------
    bin_seeds : array-like of shape (n_samples, n_features)
        Points used as initial kernel positions in clustering.mean_shift.
    """
    pass
# WARNING: Decompyle incomplete


class MeanShift(BaseEstimator, ClusterMixin):
    '''Mean shift clustering using a flat kernel.

    Mean shift clustering aims to discover "blobs" in a smooth density of
    samples. It is a centroid-based algorithm, which works by updating
    candidates for centroids to be the mean of the points within a given
    region. These candidates are then filtered in a post-processing stage to
    eliminate near-duplicates to form the final set of centroids.

    Seeding is performed using a binning technique for scalability.

    For an example of how to use MeanShift clustering, refer to:
    :ref:`sphx_glr_auto_examples_cluster_plot_mean_shift.py`.

    Read more in the :ref:`User Guide <mean_shift>`.

    Parameters
    ----------
    bandwidth : float, default=None
        Bandwidth used in the flat kernel.

        If not given, the bandwidth is estimated using
        sklearn.cluster.estimate_bandwidth; see the documentation for that
        function for hints on scalability (see also the Notes, below).

    seeds : array-like of shape (n_samples, n_features), default=None
        Seeds used to initialize kernels. If not set,
        the seeds are calculated by clustering.get_bin_seeds
        with bandwidth as the grid size and default values for
        other parameters.

    bin_seeding : bool, default=False
        If true, initial kernel locations are not locations of all
        points, but rather the location of the discretized version of
        points, where points are binned onto a grid whose coarseness
        corresponds to the bandwidth. Setting this option to True will speed
        up the algorithm because fewer seeds will be initialized.
        The default value is False.
        Ignored if seeds argument is not None.

    min_bin_freq : int, default=1
       To speed up the algorithm, accept only those bins with at least
       min_bin_freq points as seeds.

    cluster_all : bool, default=True
        If true, then all points are clustered, even those orphans that are
        not within any kernel. Orphans are assigned to the nearest kernel.
        If false, then orphans are given cluster label -1.

    n_jobs : int, default=None
        The number of jobs to use for the computation. The following tasks benefit
        from the parallelization:

        - The search of nearest neighbors for bandwidth estimation and label
          assignments. See the details in the docstring of the
          ``NearestNeighbors`` class.
        - Hill-climbing optimization for all seeds.

        See :term:`Glossary <n_jobs>` for more details.

        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    max_iter : int, default=300
        Maximum number of iterations, per seed point before the clustering
        operation terminates (for that seed point), if has not converged yet.

        .. versionadded:: 0.22

    Attributes
    ----------
    cluster_centers_ : ndarray of shape (n_clusters, n_features)
        Coordinates of cluster centers.

    labels_ : ndarray of shape (n_samples,)
        Labels of each point.

    n_iter_ : int
        Maximum number of iterations performed on each seed.

        .. versionadded:: 0.22

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    KMeans : K-Means clustering.

    Notes
    -----

    Scalability:

    Because this implementation uses a flat kernel and
    a Ball Tree to look up members of each kernel, the complexity will tend
    towards O(T*n*log(n)) in lower dimensions, with n the number of samples
    and T the number of points. In higher dimensions the complexity will
    tend towards O(T*n^2).

    Scalability can be boosted by using fewer seeds, for example by using
    a higher value of min_bin_freq in the get_bin_seeds function.

    Note that the estimate_bandwidth function is much less scalable than the
    mean shift algorithm and will be the bottleneck if it is used.

    References
    ----------

    Dorin Comaniciu and Peter Meer, "Mean Shift: A robust approach toward
    feature space analysis". IEEE Transactions on Pattern Analysis and
    Machine Intelligence. 2002. pp. 603-619.

    Examples
    --------
    >>> from sklearn.cluster import MeanShift
    >>> import numpy as np
    >>> X = np.array([[1, 1], [2, 1], [1, 0],
    ...               [4, 7], [3, 5], [3, 6]])
    >>> clustering = MeanShift(bandwidth=2).fit(X)
    >>> clustering.labels_
    array([1, 1, 1, 0, 0, 0])
    >>> clustering.predict([[0, 0], [5, 5]])
    array([1, 0])
    >>> clustering
    MeanShift(bandwidth=2)

    For a comparison of Mean Shift clustering with other clustering algorithms, see
    :ref:`sphx_glr_auto_examples_cluster_plot_cluster_comparison.py`
    '''
    _parameter_constraints: dict = {
        'bandwidth': [
            Interval(Real, 0, None, closed = 'neither'),
            None],
        'seeds': [
            'array-like',
            None],
        'bin_seeding': [
            'boolean'],
        'min_bin_freq': [
            Interval(Integral, 1, None, closed = 'left')],
        'cluster_all': [
            'boolean'],
        'n_jobs': [
            Integral,
            None],
        'max_iter': [
            Interval(Integral, 0, None, closed = 'left')] }
    
    def __init__(self = None, *, bandwidth, seeds, bin_seeding, min_bin_freq, cluster_all, n_jobs, max_iter):
        self.bandwidth = bandwidth
        self.seeds = seeds
        self.bin_seeding = bin_seeding
        self.cluster_all = cluster_all
        self.min_bin_freq = min_bin_freq
        self.n_jobs = n_jobs
        self.max_iter = max_iter

    fit = (lambda self, X, y = (None,): pass# WARNING: Decompyle incomplete
)()
    
    def predict(self, X):
        '''Predict the closest cluster each sample in X belongs to.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            New data to predict.

        Returns
        -------
        labels : ndarray of shape (n_samples,)
            Index of the cluster each sample belongs to.
        '''
        check_is_fitted(self)
        X = validate_data(self, X, reset = False)
        config_context(assume_finite = True)
        None(None, None)
        return 
        with None:
            if not None, pairwise_distances_argmin(X, self.cluster_centers_):
                pass
