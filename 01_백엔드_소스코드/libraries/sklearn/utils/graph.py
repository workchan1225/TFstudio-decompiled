# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: graph.pyc (Python 3.11)

'''Graph utilities and algorithms.'''
import numpy as np
from scipy import sparse
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.utils._param_validation import Integral, Interval, validate_params
single_source_shortest_path_length = (lambda graph = validate_params({
    'graph': [
        'array-like',
        'sparse matrix'],
    'source': [
        Interval(Integral, 0, None, closed = 'left')],
    'cutoff': [
        Interval(Integral, 0, None, closed = 'left'),
        None] }, prefer_skip_nested_validation = True), source = {
    'cutoff': None }, *, cutoff, seen = None: if sparse.issparse(graph):
graph = graph.tolil()else:
graph = sparse.lil_matrix(graph)seen = { }level = 0next_level = [
source]# WARNING: Decompyle incomplete
)()

def _fix_connected_components(X, graph, n_connected_components, component_labels, mode, metric = ('distance', 'euclidean'), **kwargs):
    '''Add connections to sparse graph to connect unconnected components.

    For each pair of unconnected components, compute all pairwise distances
    from one component to the other, and add a connection on the closest pair
    of samples. This is a hacky way to get a graph with a single connected
    component, which is necessary for example to compute a shortest path
    between all pairs of samples in the graph.

    Parameters
    ----------
    X : array of shape (n_samples, n_features) or (n_samples, n_samples)
        Features to compute the pairwise distances. If `metric =
        "precomputed"`, X is the matrix of pairwise distances.

    graph : sparse matrix of shape (n_samples, n_samples)
        Graph of connection between samples.

    n_connected_components : int
        Number of connected components, as computed by
        `scipy.sparse.csgraph.connected_components`.

    component_labels : array of shape (n_samples)
        Labels of connected components, as computed by
        `scipy.sparse.csgraph.connected_components`.

    mode : {\'connectivity\', \'distance\'}, default=\'distance\'
        Type of graph matrix: \'connectivity\' corresponds to the connectivity
        matrix with ones and zeros, and \'distance\' corresponds to the distances
        between neighbors according to the given metric.

    metric : str
        Metric used in `sklearn.metrics.pairwise.pairwise_distances`.

    kwargs : kwargs
        Keyword arguments passed to
        `sklearn.metrics.pairwise.pairwise_distances`.

    Returns
    -------
    graph : sparse matrix of shape (n_samples, n_samples)
        Graph of connection between samples, with a single connected component.
    '''
    if metric == 'precomputed' and sparse.issparse(X):
        raise RuntimeError("_fix_connected_components with metric='precomputed' requires the full distance matrix in X, and does not work with a sparse neighbors graph.")
# WARNING: Decompyle incomplete
