# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hdbscan.pyc (Python 3.11)

'''
HDBSCAN: Hierarchical Density-Based Spatial Clustering
         of Applications with Noise
'''
from numbers import Integral, Real
from warnings import warn
import numpy as np
from scipy.sparse import csgraph, issparse
from sklearn.base import BaseEstimator, ClusterMixin, _fit_context
from sklearn.cluster._hdbscan._linkage import MST_edge_dtype, make_single_linkage, mst_from_data_matrix, mst_from_mutual_reachability
from sklearn.cluster._hdbscan._reachability import mutual_reachability_graph
from sklearn.cluster._hdbscan._tree import HIERARCHY_dtype, labelling_at_cut, tree_to_labels
from sklearn.metrics import pairwise_distances
from sklearn.metrics._dist_metrics import DistanceMetric
from sklearn.metrics.pairwise import _VALID_METRICS
from sklearn.neighbors import BallTree, KDTree, NearestNeighbors
from sklearn.utils._param_validation import Hidden, Interval, StrOptions
from sklearn.utils.validation import _allclose_dense_sparse, _assert_all_finite, validate_data
FAST_METRICS = set(KDTree.valid_metrics + BallTree.valid_metrics)
_OUTLIER_ENCODING: dict = {
    'infinite': {
        'label': -2,
        'prob': 0 },
    'missing': {
        'label': -3,
        'prob': np.nan } }

def _brute_mst(mutual_reachability, min_samples):
    '''
    Builds a minimum spanning tree (MST) from the provided mutual-reachability
    values. This function dispatches to a custom Cython implementation for
    dense arrays, and `scipy.sparse.csgraph.minimum_spanning_tree` for sparse
    arrays/matrices.

    Parameters
    ----------
    mututal_reachability_graph: {ndarray, sparse matrix} of shape             (n_samples, n_samples)
        Weighted adjacency matrix of the mutual reachability graph.

    min_samples : int, default=None
        The number of samples in a neighborhood for a point
        to be considered as a core point. This includes the point itself.

    Returns
    -------
    mst : ndarray of shape (n_samples - 1,), dtype=MST_edge_dtype
        The MST representation of the mutual-reachability graph. The MST is
        represented as a collection of edges.
    '''
    pass
# WARNING: Decompyle incomplete


def _process_mst(min_spanning_tree):
    '''
    Builds a single-linkage tree (SLT) from the provided minimum spanning tree
    (MST). The MST is first sorted then processed by a custom Cython routine.

    Parameters
    ----------
    min_spanning_tree : ndarray of shape (n_samples - 1,), dtype=MST_edge_dtype
        The MST representation of the mutual-reachability graph. The MST is
        represented as a collection of edges.

    Returns
    -------
    single_linkage : ndarray of shape (n_samples - 1,), dtype=HIERARCHY_dtype
        The single-linkage tree tree (dendrogram) built from the MST.
    '''
    row_order = np.argsort(min_spanning_tree['distance'])
    min_spanning_tree = min_spanning_tree[row_order]
    return make_single_linkage(min_spanning_tree)


def _hdbscan_brute(X, min_samples, alpha, metric, n_jobs, copy = (5, None, 'euclidean', None, False), **metric_params):
    '''
    Builds a single-linkage tree (SLT) from the input data `X`. If
    `metric="precomputed"` then `X` must be a symmetric array of distances.
    Otherwise, the pairwise distances are calculated directly and passed to
    `mutual_reachability_graph`.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features) or (n_samples, n_samples)
        Either the raw data from which to compute the pairwise distances,
        or the precomputed distances.

    min_samples : int, default=None
        The number of samples in a neighborhood for a point
        to be considered as a core point. This includes the point itself.

    alpha : float, default=1.0
        A distance scaling parameter as used in robust single linkage.

    metric : str or callable, default=\'euclidean\'
        The metric to use when calculating distance between instances in a
        feature array.

        - If metric is a string or callable, it must be one of
          the options allowed by :func:`~sklearn.metrics.pairwise_distances`
          for its metric parameter.

        - If metric is "precomputed", X is assumed to be a distance matrix and
          must be square.

    n_jobs : int, default=None
        The number of jobs to use for computing the pairwise distances. This
        works by breaking down the pairwise matrix into n_jobs even slices and
        computing them in parallel. This parameter is passed directly to
        :func:`~sklearn.metrics.pairwise_distances`.

        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    copy : bool, default=False
        If `copy=True` then any time an in-place modifications would be made
        that would overwrite `X`, a copy will first be made, guaranteeing that
        the original data will be unchanged. Currently, it only applies when
        `metric="precomputed"`, when passing a dense array or a CSR sparse
        array/matrix.

    metric_params : dict, default=None
        Arguments passed to the distance metric.

    Returns
    -------
    single_linkage : ndarray of shape (n_samples - 1,), dtype=HIERARCHY_dtype
        The single-linkage tree tree (dendrogram) built from the MST.
    '''
    if metric == 'precomputed':
        if X.shape[0] != X.shape[1]:
            raise ValueError(f'''The precomputed distance matrix is expected to be symmetric, however it has shape {X.shape}. Please verify that the distance matrix was constructed correctly.''')
        if not _allclose_dense_sparse(X, X.T):
            raise ValueError('The precomputed distance matrix is expected to be symmetric, however its values appear to be asymmetric. Please verify that the distance matrix was constructed correctly.')
        distance_matrix = X.copy() if copy else X
# WARNING: Decompyle incomplete


def _hdbscan_prims(X, algo, min_samples, alpha, metric, leaf_size, n_jobs = (5, 1, 'euclidean', 40, None), **metric_params):
    '''
    Builds a single-linkage tree (SLT) from the input data `X`. If
    `metric="precomputed"` then `X` must be a symmetric array of distances.
    Otherwise, the pairwise distances are calculated directly and passed to
    `mutual_reachability_graph`.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        The raw data.

    min_samples : int, default=None
        The number of samples in a neighborhood for a point
        to be considered as a core point. This includes the point itself.

    alpha : float, default=1.0
        A distance scaling parameter as used in robust single linkage.

    metric : str or callable, default=\'euclidean\'
        The metric to use when calculating distance between instances in a
        feature array. `metric` must be one of the options allowed by
        :func:`~sklearn.metrics.pairwise_distances` for its metric
        parameter.

    n_jobs : int, default=None
        The number of jobs to use for computing the pairwise distances. This
        works by breaking down the pairwise matrix into n_jobs even slices and
        computing them in parallel. This parameter is passed directly to
        :func:`~sklearn.metrics.pairwise_distances`.

        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    copy : bool, default=False
        If `copy=True` then any time an in-place modifications would be made
        that would overwrite `X`, a copy will first be made, guaranteeing that
        the original data will be unchanged. Currently, it only applies when
        `metric="precomputed"`, when passing a dense array or a CSR sparse
        array/matrix.

    metric_params : dict, default=None
        Arguments passed to the distance metric.

    Returns
    -------
    single_linkage : ndarray of shape (n_samples - 1,), dtype=HIERARCHY_dtype
        The single-linkage tree tree (dendrogram) built from the MST.
    '''
    X = np.asarray(X, order = 'C')
    nbrs = NearestNeighbors(n_neighbors = min_samples, algorithm = algo, leaf_size = leaf_size, metric = metric, metric_params = metric_params, n_jobs = n_jobs, p = None).fit(X)
    (neighbors_distances, _) = nbrs.kneighbors(X, min_samples, return_distance = True)
    core_distances = np.ascontiguousarray(neighbors_distances[(:, -1)])
# WARNING: Decompyle incomplete


def remap_single_linkage_tree(tree, internal_to_raw, non_finite):
    '''
    Takes an internal single_linkage_tree structure and adds back in a set of points
    that were initially detected as non-finite and returns that new tree.
    These points will all be merged into the final node at np.inf distance and
    considered noise points.

    Parameters
    ----------
    tree : ndarray of shape (n_samples - 1,), dtype=HIERARCHY_dtype
        The single-linkage tree tree (dendrogram) built from the MST.
    internal_to_raw: dict
        A mapping from internal integer index to the raw integer index
    non_finite : ndarray
        Boolean array of which entries in the raw data are non-finite
    '''
    finite_count = len(internal_to_raw)
    outlier_count = len(non_finite)
    for i, _ in enumerate(tree):
        left = tree[i]['left_node']
        right = tree[i]['right_node']
        if left < finite_count:
            tree[i]['left_node'] = internal_to_raw[left]
        else:
            tree[i]['left_node'] = left + outlier_count
        if right < finite_count:
            tree[i]['right_node'] = internal_to_raw[right]
            continue
        tree[i]['right_node'] = right + outlier_count
        outlier_tree = np.zeros(len(non_finite), dtype = HIERARCHY_dtype)
        last_cluster_id = max(tree[tree.shape[0] - 1]['left_node'], tree[tree.shape[0] - 1]['right_node'])
        last_cluster_size = tree[tree.shape[0] - 1]['cluster_size']
        for i, outlier in enumerate(non_finite):
            outlier_tree[i] = (outlier, last_cluster_id + 1, np.inf, last_cluster_size + 1)
            last_cluster_id += 1
            last_cluster_size += 1
            tree = np.concatenate([
                tree,
                outlier_tree])
            return tree


def _get_finite_row_indices(matrix):
    '''
    Returns the indices of the purely finite rows of a
    sparse matrix or dense ndarray
    '''
    return row_indices


class HDBSCAN(BaseEstimator, ClusterMixin):
    pass
# WARNING: Decompyle incomplete
