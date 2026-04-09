# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _spectral_embedding.pyc (Python 3.11)

'''Spectral Embedding.'''
import warnings
from numbers import Integral, Real
import numpy as np
from scipy import sparse
from scipy.linalg import eigh
from scipy.sparse.csgraph import connected_components
from scipy.sparse.linalg import eigsh, lobpcg
from sklearn.base import BaseEstimator, _fit_context
from sklearn.metrics.pairwise import rbf_kernel
from sklearn.neighbors import NearestNeighbors, kneighbors_graph
from sklearn.utils import check_array, check_random_state, check_symmetric
from sklearn.utils._arpack import _init_arpack_v0
from sklearn.utils._param_validation import Interval, StrOptions, validate_params
from sklearn.utils.extmath import _deterministic_vector_sign_flip
from sklearn.utils.fixes import laplacian as csgraph_laplacian
from sklearn.utils.fixes import parse_version, sp_version
from sklearn.utils.validation import validate_data

def _graph_connected_component(graph, node_id):
    '''Find the largest graph connected components that contains one
    given node.

    Parameters
    ----------
    graph : array-like of shape (n_samples, n_samples)
        Adjacency matrix of the graph, non-zero weight means an edge
        between the nodes.

    node_id : int
        The index of the query node of the graph.

    Returns
    -------
    connected_components_matrix : array-like of shape (n_samples,)
        An array of bool value indicating the indexes of the nodes
        belonging to the largest connected components of the given query
        node.
    '''
    n_node = graph.shape[0]
    if sparse.issparse(graph):
        graph = graph.tocsr()
    connected_nodes = np.zeros(n_node, dtype = bool)
    nodes_to_explore = np.zeros(n_node, dtype = bool)
    nodes_to_explore[node_id] = True
    for _ in range(n_node):
        last_num_component = connected_nodes.sum()
        np.logical_or(connected_nodes, nodes_to_explore, out = connected_nodes)
        if last_num_component >= connected_nodes.sum():
            pass
        else:
            indices = np.where(nodes_to_explore)[0]
            nodes_to_explore.fill(False)
            for i in indices:
                if sparse.issparse(graph):
                    neighbors = graph[([
                        i], :)].toarray().ravel()
                else:
                    neighbors = graph[i]
                np.logical_or(nodes_to_explore, neighbors, out = nodes_to_explore)
                return connected_nodes


def _graph_is_connected(graph):
    '''Return whether the graph is connected (True) or Not (False).

    Parameters
    ----------
    graph : {array-like, sparse matrix} of shape (n_samples, n_samples)
        Adjacency matrix of the graph, non-zero weight means an edge
        between the nodes.

    Returns
    -------
    is_connected : bool
        True means the graph is fully connected and False means not.
    '''
    if sparse.issparse(graph):
        accept_large_sparse = sp_version >= parse_version('1.11.3')
        graph = check_array(graph, accept_sparse = True, accept_large_sparse = accept_large_sparse)
        (n_connected_components, _) = connected_components(graph)
        return n_connected_components == 1
    return None(graph, 0).sum() == graph.shape[0]


def _set_diag(laplacian, value, norm_laplacian):
    '''Set the diagonal of the laplacian matrix and convert it to a
    sparse format well suited for eigenvalue decomposition.

    Parameters
    ----------
    laplacian : {ndarray, sparse matrix}
        The graph laplacian.

    value : float
        The value of the diagonal.

    norm_laplacian : bool
        Whether the value of the diagonal should be changed or not.

    Returns
    -------
    laplacian : {array, sparse matrix}
        An array of matrix in a form that is well suited to fast
        eigenvalue decomposition, depending on the band width of the
        matrix.
    '''
    n_nodes = laplacian.shape[0]
    if not sparse.issparse(laplacian):
        if norm_laplacian:
            laplacian.flat[::n_nodes + 1] = value
        else:
            laplacian = laplacian.tocoo()
            if norm_laplacian:
                diag_idx = laplacian.row == laplacian.col
                laplacian.data[diag_idx] = value
            n_diags = np.unique(laplacian.row - laplacian.col).size
            if n_diags <= 7:
                laplacian = laplacian.todia()
            else:
                laplacian = laplacian.tocsr()
    return laplacian

spectral_embedding = (lambda adjacency = validate_params({
    'adjacency': [
        'array-like',
        'sparse matrix'],
    'n_components': [
        Interval(Integral, 1, None, closed = 'left')],
    'eigen_solver': [
        StrOptions({
            'amg',
            'arpack',
            'lobpcg'}),
        None],
    'random_state': [
        'random_state'],
    'eigen_tol': [
        Interval(Real, 0, None, closed = 'left'),
        StrOptions({
            'auto'})],
    'norm_laplacian': [
        'boolean'],
    'drop_first': [
        'boolean'] }, prefer_skip_nested_validation = True), *, n_components: random_state = check_random_state(random_state)_spectral_embedding(adjacency, n_components = n_components, eigen_solver = eigen_solver, random_state = random_state, eigen_tol = eigen_tol, norm_laplacian = norm_laplacian, drop_first = drop_first))()

def _spectral_embedding(adjacency = None, *, n_components, eigen_solver, random_state, eigen_tol, norm_laplacian, drop_first):
    adjacency = check_symmetric(adjacency)
# WARNING: Decompyle incomplete


class SpectralEmbedding(BaseEstimator):
    pass
# WARNING: Decompyle incomplete
