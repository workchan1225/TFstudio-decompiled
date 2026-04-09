# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _optics.pyc (Python 3.11)

'''Ordering Points To Identify the Clustering Structure (OPTICS)

These routines execute the OPTICS algorithm, and implement various
cluster extraction methods of the ordered list.
'''
import warnings
from numbers import Integral, Real
import numpy as np
from scipy.sparse import SparseEfficiencyWarning, issparse
from sklearn.base import BaseEstimator, ClusterMixin, _fit_context
from sklearn.exceptions import DataConversionWarning
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import _VALID_METRICS, PAIRWISE_BOOLEAN_FUNCTIONS
from sklearn.neighbors import NearestNeighbors
from sklearn.utils import gen_batches
from sklearn.utils._chunking import get_chunk_n_rows
from sklearn.utils._param_validation import HasMethods, Interval, RealNotInt, StrOptions, validate_params
from sklearn.utils.validation import check_memory, validate_data

class OPTICS(BaseEstimator, ClusterMixin):
    '''Estimate clustering structure from vector array.

    OPTICS (Ordering Points To Identify the Clustering Structure), closely
    related to DBSCAN, finds core samples of high density and expands clusters
    from them [1]_. Unlike DBSCAN, it keeps cluster hierarchy for a variable
    neighborhood radius. Better suited for usage on large datasets than the
    current scikit-learn implementation of DBSCAN.

    Clusters are then extracted from the cluster-order using a
    DBSCAN-like method (cluster_method = \'dbscan\') or an automatic
    technique proposed in [1]_ (cluster_method = \'xi\').

    This implementation deviates from the original OPTICS by first performing
    k-nearest-neighborhood searches on all points to identify core sizes of
    all points (instead of computing neighbors while looping through points).
    Reachability distances to only unprocessed points are then computed, to
    construct the cluster order, similar to the original OPTICS.
    Note that we do not employ a heap to manage the expansion
    candidates, so the time complexity will be O(n^2).

    Read more in the :ref:`User Guide <optics>`.

    Parameters
    ----------
    min_samples : int > 1 or float between 0 and 1, default=5
        The number of samples in a neighborhood for a point to be considered as
        a core point. Also, up and down steep regions can\'t have more than
        ``min_samples`` consecutive non-steep points. Expressed as an absolute
        number or a fraction of the number of samples (rounded to be at least
        2).

    max_eps : float, default=np.inf
        The maximum distance between two samples for one to be considered as
        in the neighborhood of the other. Default value of ``np.inf`` will
        identify clusters across all scales; reducing ``max_eps`` will result
        in shorter run times.

    metric : str or callable, default=\'minkowski\'
        Metric to use for distance computation. Any metric from scikit-learn
        or :mod:`scipy.spatial.distance` can be used.

        If `metric` is a callable function, it is called on each
        pair of instances (rows) and the resulting value recorded. The callable
        should take two arrays as input and return one value indicating the
        distance between them. This works for Scipy\'s metrics, but is less
        efficient than passing the metric name as a string. If metric is
        "precomputed", `X` is assumed to be a distance matrix and must be
        square.

        Valid values for metric are:

        - from scikit-learn: [\'cityblock\', \'cosine\', \'euclidean\', \'l1\', \'l2\',
          \'manhattan\']

        - from scipy.spatial.distance: [\'braycurtis\', \'canberra\', \'chebyshev\',
          \'correlation\', \'dice\', \'hamming\', \'jaccard\', \'kulsinski\',
          \'mahalanobis\', \'minkowski\', \'rogerstanimoto\', \'russellrao\',
          \'seuclidean\', \'sokalmichener\', \'sokalsneath\', \'sqeuclidean\',
          \'yule\']

        Sparse matrices are only supported by scikit-learn metrics.
        See :mod:`scipy.spatial.distance` for details on these metrics.

        .. note::
           `\'kulsinski\'` is deprecated from SciPy 1.9 and will be removed in SciPy 1.11.

    p : float, default=2
        Parameter for the Minkowski metric from
        :class:`~sklearn.metrics.pairwise_distances`. When p = 1, this is
        equivalent to using manhattan_distance (l1), and euclidean_distance
        (l2) for p = 2. For arbitrary p, minkowski_distance (l_p) is used.

    metric_params : dict, default=None
        Additional keyword arguments for the metric function.

    cluster_method : {\'xi\', \'dbscan\'}, default=\'xi\'
        The extraction method used to extract clusters using the calculated
        reachability and ordering.

    eps : float, default=None
        The maximum distance between two samples for one to be considered as
        in the neighborhood of the other. By default it assumes the same value
        as ``max_eps``.
        Used only when ``cluster_method=\'dbscan\'``.

    xi : float between 0 and 1, default=0.05
        Determines the minimum steepness on the reachability plot that
        constitutes a cluster boundary. For example, an upwards point in the
        reachability plot is defined by the ratio from one point to its
        successor being at most 1-xi.
        Used only when ``cluster_method=\'xi\'``.

    predecessor_correction : bool, default=True
        Correct clusters according to the predecessors calculated by OPTICS
        [2]_. This parameter has minimal effect on most datasets.
        Used only when ``cluster_method=\'xi\'``.

    min_cluster_size : int > 1 or float between 0 and 1, default=None
        Minimum number of samples in an OPTICS cluster, expressed as an
        absolute number or a fraction of the number of samples (rounded to be
        at least 2). If ``None``, the value of ``min_samples`` is used instead.
        Used only when ``cluster_method=\'xi\'``.

    algorithm : {\'auto\', \'ball_tree\', \'kd_tree\', \'brute\'}, default=\'auto\'
        Algorithm used to compute the nearest neighbors:

        - \'ball_tree\' will use :class:`~sklearn.neighbors.BallTree`.
        - \'kd_tree\' will use :class:`~sklearn.neighbors.KDTree`.
        - \'brute\' will use a brute-force search.
        - \'auto\' (default) will attempt to decide the most appropriate
          algorithm based on the values passed to :meth:`fit` method.

        Note: fitting on sparse input will override the setting of
        this parameter, using brute force.

    leaf_size : int, default=30
        Leaf size passed to :class:`~sklearn.neighbors.BallTree` or
        :class:`~sklearn.neighbors.KDTree`. This can affect the speed of the
        construction and query, as well as the memory required to store the
        tree. The optimal value depends on the nature of the problem.

    memory : str or object with the joblib.Memory interface, default=None
        Used to cache the output of the computation of the tree.
        By default, no caching is done. If a string is given, it is the
        path to the caching directory.

    n_jobs : int, default=None
        The number of parallel jobs to run for neighbors search.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    Attributes
    ----------
    labels_ : ndarray of shape (n_samples,)
        Cluster labels for each point in the dataset given to fit().
        Noisy samples and points which are not included in a leaf cluster
        of ``cluster_hierarchy_`` are labeled as -1.

    reachability_ : ndarray of shape (n_samples,)
        Reachability distances per sample, indexed by object order. Use
        ``clust.reachability_[clust.ordering_]`` to access in cluster order.

    ordering_ : ndarray of shape (n_samples,)
        The cluster ordered list of sample indices.

    core_distances_ : ndarray of shape (n_samples,)
        Distance at which each sample becomes a core point, indexed by object
        order. Points which will never be core have a distance of inf. Use
        ``clust.core_distances_[clust.ordering_]`` to access in cluster order.

    predecessor_ : ndarray of shape (n_samples,)
        Point that a sample was reached from, indexed by object order.
        Seed points have a predecessor of -1.

    cluster_hierarchy_ : ndarray of shape (n_clusters, 2)
        The list of clusters in the form of ``[start, end]`` in each row, with
        all indices inclusive. The clusters are ordered according to
        ``(end, -start)`` (ascending) so that larger clusters encompassing
        smaller clusters come after those smaller ones. Since ``labels_`` does
        not reflect the hierarchy, usually
        ``len(cluster_hierarchy_) > np.unique(optics.labels_)``. Please also
        note that these indices are of the ``ordering_``, i.e.
        ``X[ordering_][start:end + 1]`` form a cluster.
        Only available when ``cluster_method=\'xi\'``.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    DBSCAN : A similar clustering for a specified neighborhood radius (eps).
        Our implementation is optimized for runtime.

    References
    ----------
    .. [1] Ankerst, Mihael, Markus M. Breunig, Hans-Peter Kriegel,
       and Jörg Sander. "OPTICS: ordering points to identify the clustering
       structure." ACM SIGMOD Record 28, no. 2 (1999): 49-60.

    .. [2] Schubert, Erich, Michael Gertz.
       "Improving the Cluster Structure Extracted from OPTICS Plots." Proc. of
       the Conference "Lernen, Wissen, Daten, Analysen" (LWDA) (2018): 318-329.

    Examples
    --------
    >>> from sklearn.cluster import OPTICS
    >>> import numpy as np
    >>> X = np.array([[1, 2], [2, 5], [3, 6],
    ...               [8, 7], [8, 8], [7, 3]])
    >>> clustering = OPTICS(min_samples=2).fit(X)
    >>> clustering.labels_
    array([0, 0, 0, 1, 1, 1])

    For a more detailed example see
    :ref:`sphx_glr_auto_examples_cluster_plot_optics.py`.

    For a comparison of OPTICS with other clustering algorithms, see
    :ref:`sphx_glr_auto_examples_cluster_plot_cluster_comparison.py`
    '''
    _parameter_constraints: dict = {
        'min_samples': [
            Interval(Integral, 2, None, closed = 'left'),
            Interval(RealNotInt, 0, 1, closed = 'both')],
        'max_eps': [
            Interval(Real, 0, None, closed = 'both')],
        'metric': [
            StrOptions(set(_VALID_METRICS) | {
                'precomputed'}),
            callable],
        'p': [
            Interval(Real, 1, None, closed = 'left')],
        'metric_params': [
            dict,
            None],
        'cluster_method': [
            StrOptions({
                'dbscan',
                'xi'})],
        'eps': [
            Interval(Real, 0, None, closed = 'both'),
            None],
        'xi': [
            Interval(Real, 0, 1, closed = 'both')],
        'predecessor_correction': [
            'boolean'],
        'min_cluster_size': [
            Interval(Integral, 2, None, closed = 'left'),
            Interval(RealNotInt, 0, 1, closed = 'right'),
            None],
        'algorithm': [
            StrOptions({
                'auto',
                'brute',
                'kd_tree',
                'ball_tree'})],
        'leaf_size': [
            Interval(Integral, 1, None, closed = 'left')],
        'memory': [
            str,
            HasMethods('cache'),
            None],
        'n_jobs': [
            Integral,
            None] }
    
    def __init__(self = None, *, min_samples, max_eps, metric, p, metric_params, cluster_method, eps, xi, predecessor_correction, min_cluster_size, algorithm, leaf_size, memory, n_jobs):
        self.max_eps = max_eps
        self.min_samples = min_samples
        self.min_cluster_size = min_cluster_size
        self.algorithm = algorithm
        self.metric = metric
        self.metric_params = metric_params
        self.p = p
        self.leaf_size = leaf_size
        self.cluster_method = cluster_method
        self.eps = eps
        self.xi = xi
        self.predecessor_correction = predecessor_correction
        self.memory = memory
        self.n_jobs = n_jobs

    fit = (lambda self, X, y = (None,): dtype = bool if self.metric in PAIRWISE_BOOLEAN_FUNCTIONS else floatif dtype is bool and X.dtype != bool:
msg = f'''Data will be converted to boolean for metric {self.metric}, to avoid this warning, you may convert the data prior to calling fit.'''warnings.warn(msg, DataConversionWarning)X = validate_data(self, X, dtype = dtype, accept_sparse = 'csr')if self.metric == 'precomputed' and issparse(X):
X = X.copy()warnings.catch_warnings()warnings.simplefilter('ignore', SparseEfficiencyWarning)X.setdiag(X.diagonal())None(None, None)else:
with None:
if not None:
passmemory = check_memory(self.memory)(self.ordering_, self.core_distances_, self.reachability_, self.predecessor_) = memory.cache(compute_optics_graph)(X = X, min_samples = self.min_samples, algorithm = self.algorithm, leaf_size = self.leaf_size, metric = self.metric, metric_params = self.metric_params, p = self.p, n_jobs = self.n_jobs, max_eps = self.max_eps)if self.cluster_method == 'xi':
(labels_, clusters_) = cluster_optics_xi(reachability = self.reachability_, predecessor = self.predecessor_, ordering = self.ordering_, min_samples = self.min_samples, min_cluster_size = self.min_cluster_size, xi = self.xi, predecessor_correction = self.predecessor_correction)self.cluster_hierarchy_ = clusters_# WARNING: Decompyle incomplete
)()


def _validate_size(size, n_samples, param_name):
    if size > n_samples:
        raise ValueError('%s must be no greater than the number of samples (%d). Got %d' % (param_name, n_samples, size))


def _compute_core_distances_(X, neighbors, min_samples, working_memory):
    """Compute the k-th nearest neighbor of each sample.

    Equivalent to neighbors.kneighbors(X, self.min_samples)[0][:, -1]
    but with more memory efficiency.

    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        The data.
    neighbors : NearestNeighbors instance
        The fitted nearest neighbors estimator.
    working_memory : int, default=None
        The sought maximum memory for temporary distance matrix chunks.
        When None (default), the value of
        ``sklearn.get_config()['working_memory']`` is used.

    Returns
    -------
    core_distances : ndarray of shape (n_samples,)
        Distance at which each sample becomes a core point.
        Points which will never be core have a distance of inf.
    """
    n_samples = X.shape[0]
    core_distances = np.empty(n_samples)
    core_distances.fill(np.nan)
    chunk_n_rows = get_chunk_n_rows(row_bytes = 16 * min_samples, max_n_rows = n_samples, working_memory = working_memory)
    slices = gen_batches(n_samples, chunk_n_rows)
    for sl in slices:
        core_distances[sl] = neighbors.kneighbors(X[sl], min_samples)[0][(:, -1)]
        return core_distances

compute_optics_graph = (lambda X, *, min_samples: n_samples = X.shape[0]_validate_size(min_samples, n_samples, 'min_samples')if min_samples <= 1:
min_samples = max(2, int(min_samples * n_samples))reachability_ = np.empty(n_samples)reachability_.fill(np.inf)predecessor_ = np.empty(n_samples, dtype = int)predecessor_.fill(-1)nbrs = NearestNeighbors(n_neighbors = min_samples, algorithm = algorithm, leaf_size = leaf_size, metric = metric, metric_params = metric_params, p = p, n_jobs = n_jobs)nbrs.fit(X)core_distances_ = _compute_core_distances_(X = X, neighbors = nbrs, min_samples = min_samples, working_memory = None)core_distances_[core_distances_ > max_eps] = np.infnp.around(core_distances_, decimals = np.finfo(core_distances_.dtype).precision, out = core_distances_)processed = np.zeros(X.shape[0], dtype = bool)ordering = np.zeros(X.shape[0], dtype = int)for ordering_idx in range(X.shape[0]):
index = np.where(processed == 0)[0]point = index[np.argmin(reachability_[index])]processed[point] = Trueordering[ordering_idx] = pointif core_distances_[point] != np.inf:
_set_reach_dist(core_distances_ = core_distances_, reachability_ = reachability_, predecessor_ = predecessor_, point_index = point, processed = processed, X = X, nbrs = nbrs, metric = metric, metric_params = metric_params, p = p, max_eps = max_eps)if np.all(np.isinf(reachability_)):
warnings.warn('All reachability values are inf. Set a larger max_eps or all data will be considered outliers.', UserWarning)(ordering, core_distances_, reachability_, predecessor_))()

def _set_reach_dist(core_distances_, reachability_, predecessor_, point_index, processed, X, nbrs, metric, metric_params, p, max_eps):
    P = X[point_index:point_index + 1]
    indices = nbrs.radius_neighbors(P, radius = max_eps, return_distance = False)[0]
    unproc = np.compress(~np.take(processed, indices), indices)
    if not unproc.size:
        return None
    if None == 'precomputed':
        dists = X[([
            point_index], unproc)]
        if isinstance(dists, np.matrix):
            dists = np.asarray(dists)
        dists = dists.ravel()
# WARNING: Decompyle incomplete

cluster_optics_dbscan = (lambda *: n_samples = len(core_distances)labels = np.zeros(n_samples, dtype = int)far_reach = reachability > epsnear_core = core_distances <= epslabels[ordering] = np.cumsum(far_reach[ordering] & near_core[ordering]) - 1labels[far_reach & ~near_core] = -1labels)()
cluster_optics_xi = (lambda *: n_samples = len(reachability)_validate_size(min_samples, n_samples, 'min_samples')if min_samples <= 1:
min_samples = max(2, int(min_samples * n_samples))# WARNING: Decompyle incomplete
)()

def _extend_region(steep_point, xward_point, start, min_samples):
    """Extend the area until it's maximal.

    It's the same function for both upward and downward reagions, depending on
    the given input parameters. Assuming:

        - steep_{upward/downward}: bool array indicating whether a point is a
          steep {upward/downward};
        - upward/downward: bool array indicating whether a point is
          upward/downward;

    To extend an upward reagion, ``steep_point=steep_upward`` and
    ``xward_point=downward`` are expected, and to extend a downward region,
    ``steep_point=steep_downward`` and ``xward_point=upward``.

    Parameters
    ----------
    steep_point : ndarray of shape (n_samples,), dtype=bool
        True if the point is steep downward (upward).

    xward_point : ndarray of shape (n_samples,), dtype=bool
        True if the point is an upward (respectively downward) point.

    start : int
        The start of the xward region.

    min_samples : int
       The same as the min_samples given to OPTICS. Up and down steep
       regions can't have more then ``min_samples`` consecutive non-steep
       points.

    Returns
    -------
    index : int
        The current index iterating over all the samples, i.e. where we are up
        to in our search.

    end : int
        The end of the region, which can be behind the index. The region
        includes the ``end`` index.
    """
    n_samples = len(steep_point)
    non_xward_points = 0
    index = start
    end = start
# WARNING: Decompyle incomplete


def _update_filter_sdas(sdas, mib, xi_complement, reachability_plot):
    '''Update steep down areas (SDAs) using the new maximum in between (mib)
    value, and the given complement of xi, i.e. ``1 - xi``.
    '''
    pass
# WARNING: Decompyle incomplete


def _correct_predecessor(reachability_plot, predecessor_plot, ordering, s, e):
    '''Correct for predecessors.

    Applies Algorithm 2 of [1]_.

    Input parameters are ordered by the computer OPTICS ordering.

    .. [1] Schubert, Erich, Michael Gertz.
       "Improving the Cluster Structure Extracted from OPTICS Plots." Proc. of
       the Conference "Lernen, Wissen, Daten, Analysen" (LWDA) (2018): 318-329.
    '''
    pass
# WARNING: Decompyle incomplete


def _xi_cluster(reachability_plot, predecessor_plot, ordering, xi, min_samples, min_cluster_size, predecessor_correction):
    """Automatically extract clusters according to the Xi-steep method.

    This is rouphly an implementation of Figure 19 of the OPTICS paper.

    Parameters
    ----------
    reachability_plot : array-like of shape (n_samples,)
        The reachability plot, i.e. reachability ordered according to
        the calculated ordering, all computed by OPTICS.

    predecessor_plot : array-like of shape (n_samples,)
        Predecessors ordered according to the calculated ordering.

    xi : float, between 0 and 1
        Determines the minimum steepness on the reachability plot that
        constitutes a cluster boundary. For example, an upwards point in the
        reachability plot is defined by the ratio from one point to its
        successor being at most 1-xi.

    min_samples : int > 1
        The same as the min_samples given to OPTICS. Up and down steep regions
        can't have more then ``min_samples`` consecutive non-steep points.

    min_cluster_size : int > 1
        Minimum number of samples in an OPTICS cluster.

    predecessor_correction : bool
        Correct clusters based on the calculated predecessors.

    Returns
    -------
    clusters : ndarray of shape (n_clusters, 2)
        The list of clusters in the form of [start, end] in each row, with all
        indices inclusive. The clusters are ordered in a way that larger
        clusters encompassing smaller clusters come after those smaller
        clusters.
    """
    reachability_plot = np.hstack((reachability_plot, np.inf))
    xi_complement = 1 - xi
    sdas = []
    clusters = []
    index = 0
    mib = 0
    np.errstate(invalid = 'ignore')
    ratio = reachability_plot[:-1] / reachability_plot[1:]
    steep_upward = ratio <= xi_complement
    steep_downward = ratio >= 1 / xi_complement
    downward = ratio > 1
    upward = ratio < 1
    None(None, None)
# WARNING: Decompyle incomplete


def _extract_xi_labels(ordering, clusters):
    '''Extracts the labels from the clusters returned by `_xi_cluster`.
    We rely on the fact that clusters are stored
    with the smaller clusters coming before the larger ones.

    Parameters
    ----------
    ordering : array-like of shape (n_samples,)
        The ordering of points calculated by OPTICS

    clusters : array-like of shape (n_clusters, 2)
        List of clusters i.e. (start, end) tuples,
        as returned by `_xi_cluster`.

    Returns
    -------
    labels : ndarray of shape (n_samples,)
    '''
    labels = np.full(len(ordering), -1, dtype = int)
    label = 0
    for c in clusters:
        if not np.any(labels[c[0]:c[1] + 1] != -1):
            labels[c[0]:c[1] + 1] = label
            label += 1
        labels[ordering] = labels.copy()
        return labels
