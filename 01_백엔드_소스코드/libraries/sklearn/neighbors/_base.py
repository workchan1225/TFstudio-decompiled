# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _base.pyc (Python 3.11)

'''Base and mixin classes for nearest neighbors.'''
import itertools
import numbers
import warnings
from abc import ABCMeta, abstractmethod
from functools import partial
from numbers import Integral, Real
import numpy as np
from joblib import effective_n_jobs
from scipy.sparse import csr_matrix, issparse
from sklearn.base import BaseEstimator, MultiOutputMixin, is_classifier
from sklearn.exceptions import DataConversionWarning, EfficiencyWarning
from sklearn.metrics import DistanceMetric, pairwise_distances_chunked
from sklearn.metrics._pairwise_distances_reduction import ArgKmin, RadiusNeighbors
from sklearn.metrics.pairwise import PAIRWISE_DISTANCE_FUNCTIONS
from sklearn.neighbors._ball_tree import BallTree
from sklearn.neighbors._kd_tree import KDTree
from sklearn.utils import check_array, gen_even_slices, get_tags
from sklearn.utils._param_validation import Interval, StrOptions, validate_params
from sklearn.utils.fixes import parse_version, sp_base_version
from sklearn.utils.multiclass import check_classification_targets
from sklearn.utils.parallel import Parallel, delayed
from sklearn.utils.validation import _to_object_array, check_is_fitted, validate_data
SCIPY_METRICS = [
    'braycurtis',
    'canberra',
    'chebyshev',
    'correlation',
    'cosine',
    'dice',
    'hamming',
    'jaccard',
    'mahalanobis',
    'minkowski',
    'rogerstanimoto',
    'russellrao',
    'seuclidean',
    'sokalsneath',
    'sqeuclidean',
    'yule']
if sp_base_version < parse_version('1.17'):
    SCIPY_METRICS += [
        'sokalmichener']
if sp_base_version < parse_version('1.11'):
    SCIPY_METRICS += [
        'kulsinski']
if sp_base_version < parse_version('1.9'):
    SCIPY_METRICS += [
        'matching']
VALID_METRICS = dict(ball_tree = BallTree.valid_metrics, kd_tree = KDTree.valid_metrics, brute = sorted(set(PAIRWISE_DISTANCE_FUNCTIONS).union(SCIPY_METRICS)))
VALID_METRICS_SPARSE = dict(ball_tree = [], kd_tree = [], brute = PAIRWISE_DISTANCE_FUNCTIONS.keys() - {
    'haversine',
    'nan_euclidean'})

def _get_weights(dist, weights):
    """Get the weights from an array of distances and a parameter ``weights``.

    Assume weights have already been validated.

    Parameters
    ----------
    dist : ndarray
        The input distances.

    weights : {'uniform', 'distance'}, callable or None
        The kind of weighting used.

    Returns
    -------
    weights_arr : array of the same shape as ``dist``
        If ``weights == 'uniform'``, then returns None.
    """
    if weights in (None, 'uniform'):
        return None
    if None == 'distance':
        if dist.dtype is np.dtype(object):
            for point_dist_i, point_dist in enumerate(dist):
                if hasattr(point_dist, '__contains__') and 0 in point_dist:
                    dist[point_dist_i] = point_dist == 0
                    continue
                dist[point_dist_i] = 1 / point_dist
        np.errstate(divide = 'ignore')
        dist = 1 / dist
        None(None, None)
    else:
        with None:
            if not None:
                pass
    inf_mask = np.isinf(dist)
    inf_row = np.any(inf_mask, axis = 1)
    dist[inf_row] = inf_mask[inf_row]
    return dist
    if callable(weights):
        return weights(dist)


def _is_sorted_by_data(graph):
    """Return whether the graph's non-zero entries are sorted by data.

    The non-zero entries are stored in graph.data and graph.indices.
    For each row (or sample), the non-zero entries can be either:
        - sorted by indices, as after graph.sort_indices();
        - sorted by data, as after _check_precomputed(graph);
        - not sorted.

    Parameters
    ----------
    graph : sparse matrix of shape (n_samples, n_samples)
        Neighbors graph as given by `kneighbors_graph` or
        `radius_neighbors_graph`. Matrix should be of format CSR format.

    Returns
    -------
    res : bool
        Whether input graph is sorted by data.
    """
    pass
# WARNING: Decompyle incomplete


def _check_precomputed(X):
    '''Check precomputed distance matrix.

    If the precomputed distance matrix is sparse, it checks that the non-zero
    entries are sorted by distances. If not, the matrix is copied and sorted.

    Parameters
    ----------
    X : {sparse matrix, array-like}, (n_samples, n_samples)
        Distance matrix to other samples. X may be a sparse matrix, in which
        case only non-zero elements may be considered neighbors.

    Returns
    -------
    X : {sparse matrix, array-like}, (n_samples, n_samples)
        Distance matrix to other samples. X may be a sparse matrix, in which
        case only non-zero elements may be considered neighbors.
    '''
    if not issparse(X):
        X = check_array(X, ensure_non_negative = True, input_name = 'X')
        return X
    graph = None
    if graph.format not in ('csr', 'csc', 'coo', 'lil'):
        raise TypeError('Sparse matrix in {!r} format is not supported due to its handling of explicit zeros'.format(graph.format))
    copied = graph.format != 'csr'
    graph = check_array(graph, accept_sparse = 'csr', ensure_non_negative = True, input_name = 'precomputed distance matrix')
    graph = sort_graph_by_row_values(graph, copy = not copied, warn_when_not_sorted = True)
    return graph

sort_graph_by_row_values = (lambda graph, copy, warn_when_not_sorted = (False, True): if graph.format == 'csr' and _is_sorted_by_data(graph):
graphif None:
warnings.warn('Precomputed sparse input was not sorted by row values. Use the function sklearn.neighbors.sort_graph_by_row_values to sort the input by row values, with warn_when_not_sorted=False to remove this warning.', EfficiencyWarning)if graph.format not in ('csr', 'csc', 'coo', 'lil'):
raise TypeError(f'''Sparse matrix in {graph.format!r} format is not supported due to its handling of explicit zeros''')if graph.format != 'csr':
if not copy:
raise ValueError('The input graph is not in CSR format. Use copy=True to allow the conversion to CSR format.')graph = graph.asformat('csr')elif copy:
graph = graph.copy()row_nnz = np.diff(graph.indptr)if row_nnz.max() == row_nnz.min():
n_samples = graph.shape[0]distances = graph.data.reshape(n_samples, -1)order = np.argsort(distances, kind = 'mergesort')order += np.arange(n_samples)[(:, None)] * row_nnz[0]order = order.ravel()graph.data = graph.data[order]graph.indices = graph.indices[order]else:
for start, stop in zip(graph.indptr, graph.indptr[1:]):
order = np.argsort(graph.data[start:stop], kind = 'mergesort')graph.data[start:stop] = graph.data[start:stop][order]graph.indices[start:stop] = graph.indices[start:stop][order]graph)()

def _kneighbors_from_graph(graph, n_neighbors, return_distance):
    '''Decompose a nearest neighbors sparse graph into distances and indices.

    Parameters
    ----------
    graph : sparse matrix of shape (n_samples, n_samples)
        Neighbors graph as given by `kneighbors_graph` or
        `radius_neighbors_graph`. Matrix should be of format CSR format.

    n_neighbors : int
        Number of neighbors required for each sample.

    return_distance : bool
        Whether or not to return the distances.

    Returns
    -------
    neigh_dist : ndarray of shape (n_samples, n_neighbors)
        Distances to nearest neighbors. Only present if `return_distance=True`.

    neigh_ind : ndarray of shape (n_samples, n_neighbors)
        Indices of nearest neighbors.
    '''
    pass
# WARNING: Decompyle incomplete


def _radius_neighbors_from_graph(graph, radius, return_distance):
    '''Decompose a nearest neighbors sparse graph into distances and indices.

    Parameters
    ----------
    graph : sparse matrix of shape (n_samples, n_samples)
        Neighbors graph as given by `kneighbors_graph` or
        `radius_neighbors_graph`. Matrix should be of format CSR format.

    radius : float
        Radius of neighborhoods which should be strictly positive.

    return_distance : bool
        Whether or not to return the distances.

    Returns
    -------
    neigh_dist : ndarray of shape (n_samples,) of arrays
        Distances to nearest neighbors. Only present if `return_distance=True`.

    neigh_ind : ndarray of shape (n_samples,) of arrays
        Indices of nearest neighbors.
    '''
    pass
# WARNING: Decompyle incomplete


def NeighborsBase():
    '''NeighborsBase'''
    pass
# WARNING: Decompyle incomplete

NeighborsBase = <NODE:27>(NeighborsBase, 'NeighborsBase', MultiOutputMixin, BaseEstimator, metaclass = ABCMeta)

class KNeighborsMixin:
    '''Mixin for k-neighbors searches.'''
    
    def _kneighbors_reduce_func(self, dist, start, n_neighbors, return_distance):
        '''Reduce a chunk of distances to the nearest neighbors.

        Callback to :func:`sklearn.metrics.pairwise.pairwise_distances_chunked`

        Parameters
        ----------
        dist : ndarray of shape (n_samples_chunk, n_samples)
            The distance matrix.

        start : int
            The index in X which the first row of dist corresponds to.

        n_neighbors : int
            Number of neighbors required for each sample.

        return_distance : bool
            Whether or not to return the distances.

        Returns
        -------
        dist : array of shape (n_samples_chunk, n_neighbors)
            Returned only if `return_distance=True`.

        neigh : array of shape (n_samples_chunk, n_neighbors)
            The neighbors indices.
        '''
        sample_range = np.arange(dist.shape[0])[(:, None)]
        neigh_ind = np.argpartition(dist, n_neighbors - 1, axis = 1)
        neigh_ind = neigh_ind[(:, :n_neighbors)]
        neigh_ind = neigh_ind[(sample_range, np.argsort(dist[(sample_range, neigh_ind)]))]
        if return_distance:
            if self.effective_metric_ == 'euclidean':
                result = (np.sqrt(dist[(sample_range, neigh_ind)]), neigh_ind)
            else:
                result = (dist[(sample_range, neigh_ind)], neigh_ind)
        else:
            result = neigh_ind
        return result

    
    def kneighbors(self, X, n_neighbors, return_distance = (None, None, True)):
        """Find the K-neighbors of a point.

        Returns indices of and distances to the neighbors of each point.

        Parameters
        ----------
        X : {array-like, sparse matrix}, shape (n_queries, n_features),             or (n_queries, n_indexed) if metric == 'precomputed', default=None
            The query point or points.
            If not provided, neighbors of each indexed point are returned.
            In this case, the query point is not considered its own neighbor.

        n_neighbors : int, default=None
            Number of neighbors required for each sample. The default is the
            value passed to the constructor.

        return_distance : bool, default=True
            Whether or not to return the distances.

        Returns
        -------
        neigh_dist : ndarray of shape (n_queries, n_neighbors)
            Array representing the lengths to points, only present if
            return_distance=True.

        neigh_ind : ndarray of shape (n_queries, n_neighbors)
            Indices of the nearest points in the population matrix.

        Examples
        --------
        In the following example, we construct a NearestNeighbors
        class from an array representing our data set and ask who's
        the closest point to [1,1,1]

        >>> samples = [[0., 0., 0.], [0., .5, 0.], [1., 1., .5]]
        >>> from sklearn.neighbors import NearestNeighbors
        >>> neigh = NearestNeighbors(n_neighbors=1)
        >>> neigh.fit(samples)
        NearestNeighbors(n_neighbors=1)
        >>> print(neigh.kneighbors([[1., 1., 1.]]))
        (array([[0.5]]), array([[2]]))

        As you can see, it returns [[0.5]], and [[2]], which means that the
        element is at distance 0.5 and is the third element of samples
        (indexes start at 0). You can also query for multiple points:

        >>> X = [[0., 1., 0.], [1., 0., 1.]]
        >>> neigh.kneighbors(X, return_distance=False)
        array([[1],
               [2]]...)
        """
        pass
    # WARNING: Decompyle incomplete

    
    def kneighbors_graph(self, X, n_neighbors, mode = (None, None, 'connectivity')):
        """Compute the (weighted) graph of k-Neighbors for points in X.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_queries, n_features),             or (n_queries, n_indexed) if metric == 'precomputed', default=None
            The query point or points.
            If not provided, neighbors of each indexed point are returned.
            In this case, the query point is not considered its own neighbor.
            For ``metric='precomputed'`` the shape should be
            (n_queries, n_indexed). Otherwise the shape should be
            (n_queries, n_features).

        n_neighbors : int, default=None
            Number of neighbors for each sample. The default is the value
            passed to the constructor.

        mode : {'connectivity', 'distance'}, default='connectivity'
            Type of returned matrix: 'connectivity' will return the
            connectivity matrix with ones and zeros, in 'distance' the
            edges are distances between points, type of distance
            depends on the selected metric parameter in
            NearestNeighbors class.

        Returns
        -------
        A : sparse-matrix of shape (n_queries, n_samples_fit)
            `n_samples_fit` is the number of samples in the fitted data.
            `A[i, j]` gives the weight of the edge connecting `i` to `j`.
            The matrix is of CSR format.

        See Also
        --------
        NearestNeighbors.radius_neighbors_graph : Compute the (weighted) graph
            of Neighbors for points in X.

        Examples
        --------
        >>> X = [[0], [3], [1]]
        >>> from sklearn.neighbors import NearestNeighbors
        >>> neigh = NearestNeighbors(n_neighbors=2)
        >>> neigh.fit(X)
        NearestNeighbors(n_neighbors=2)
        >>> A = neigh.kneighbors_graph(X)
        >>> A.toarray()
        array([[1., 0., 1.],
               [0., 1., 1.],
               [1., 0., 1.]])
        """
        check_is_fitted(self)
    # WARNING: Decompyle incomplete



class RadiusNeighborsMixin:
    pass
# WARNING: Decompyle incomplete
