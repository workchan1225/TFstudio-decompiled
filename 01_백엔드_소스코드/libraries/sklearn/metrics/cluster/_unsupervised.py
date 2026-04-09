# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _unsupervised.pyc (Python 3.11)

'''Unsupervised evaluation metrics.'''
import functools
from numbers import Integral
import numpy as np
from scipy.sparse import issparse
from sklearn.externals.array_api_compat import is_numpy_array
from sklearn.metrics.pairwise import _VALID_METRICS, pairwise_distances, pairwise_distances_chunked
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import _safe_indexing, check_random_state, check_X_y
from sklearn.utils._array_api import _average, _convert_to_numpy, _is_numpy_namespace, _max_precision_float_dtype, get_namespace_and_device, xpx
from sklearn.utils._param_validation import Interval, StrOptions, validate_params

def check_number_of_labels(n_labels, n_samples):
    '''Check that number of labels are valid.

    Parameters
    ----------
    n_labels : int
        Number of labels.

    n_samples : int
        Number of samples.
    '''
    if not  < 1, n_labels or 1, n_labels < n_samples:
        pass
    
    raise ValueError('Number of labels is %d. Valid values are 2 to n_samples - 1 (inclusive)' % n_labels)

silhouette_score = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'labels': [
        'array-like'],
    'metric': [
        StrOptions(set(_VALID_METRICS) | {
            'precomputed'}),
        callable],
    'sample_size': [
        Interval(Integral, 1, None, closed = 'left'),
        None],
    'random_state': [
        'random_state'] }, prefer_skip_nested_validation = True), labels = {
    'metric': 'euclidean',
    'sample_size': None,
    'random_state': None }, *, metric, sample_size: pass# WARNING: Decompyle incomplete
)()

def _silhouette_reduce(D_chunk, start, labels, label_freqs):
    '''Accumulate silhouette statistics for vertical chunk of X.

    Parameters
    ----------
    D_chunk : {array-like, sparse matrix} of shape (n_chunk_samples, n_samples)
        Precomputed distances for a chunk. If a sparse matrix is provided,
        only CSR format is accepted.
    start : int
        First index in the chunk.
    labels : array-like of shape (n_samples,)
        Corresponding cluster labels, encoded as {0, ..., n_clusters-1}.
    label_freqs : array-like
        Distribution of cluster labels in ``labels``.
    '''
    n_chunk_samples = D_chunk.shape[0]
    cluster_distances = np.zeros((n_chunk_samples, len(label_freqs)), dtype = D_chunk.dtype)
    if issparse(D_chunk):
        if D_chunk.format != 'csr':
            raise TypeError('Expected CSR matrix. Please pass sparse matrix in CSR format.')
        for i in range(n_chunk_samples):
            indptr = D_chunk.indptr
            indices = D_chunk.indices[indptr[i]:indptr[i + 1]]
            sample_weights = D_chunk.data[indptr[i]:indptr[i + 1]]
            sample_labels = np.take(labels, indices)
    for None in range(n_chunk_samples):
        sample_weights = D_chunk[i]
        sample_labels = labels
        start + n_chunk_samples = None
        intra_index = (np.arange(n_chunk_samples), labels[start:end])
        intra_cluster_distances = cluster_distances[intra_index]
        cluster_distances[intra_index] = np.inf
        cluster_distances /= label_freqs
        inter_cluster_distances = cluster_distances.min(axis = 1)
        return (intra_cluster_distances, inter_cluster_distances)

silhouette_samples = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'labels': [
        'array-like'],
    'metric': [
        StrOptions(set(_VALID_METRICS) | {
            'precomputed'}),
        callable] }, prefer_skip_nested_validation = True), labels = {
    'metric': 'euclidean' }, *, metric, kwds = None: (X, labels) = check_X_y(X, labels, accept_sparse = [
'csr'])if metric == 'precomputed':
error_msg = ValueError('The precomputed distance matrix contains non-zero elements on the diagonal. Use np.fill_diagonal(X, 0).')if X.dtype.kind == 'f':
atol = np.finfo(X.dtype).eps * 100if np.any(np.abs(X.diagonal()) > atol):
raise error_msgelif np.any(X.diagonal() != 0):
raise error_msgle = LabelEncoder()labels = le.fit_transform(labels)n_samples = len(labels)label_freqs = np.bincount(labels)check_number_of_labels(len(le.classes_), n_samples)kwds['metric'] = metricreduce_func = functools.partial(_silhouette_reduce, labels = labels, label_freqs = label_freqs)# WARNING: Decompyle incomplete
)()
calinski_harabasz_score = (lambda X, labels: (xp, _, device_) = get_namespace_and_device(X, labels)if not _is_numpy_namespace(xp) and is_numpy_array(X):
X = _convert_to_numpy(X, xp = xp)else:
X = xp.astype(X, _max_precision_float_dtype(xp, device_), copy = False)(X, labels) = check_X_y(X, labels)le = LabelEncoder()labels = le.fit_transform(labels)(n_samples, _) = X.shapen_labels = le.classes_.shape[0]check_number_of_labels(n_labels, n_samples)(extra_disp, intra_disp) = (0, 0)mean = xp.mean(X, axis = 0)for k in range(n_labels):
cluster_k = X[labels == k]mean_k = xp.mean(cluster_k, axis = 0)extra_disp += cluster_k.shape[0] * xp.sum((mean_k - mean) ** 2)intra_disp += xp.sum((cluster_k - mean_k) ** 2)float(1 if intra_disp == 0 else extra_disp * (n_samples - n_labels) / (intra_disp * (n_labels - 1))))()
davies_bouldin_score = (lambda X, labels: (xp, _, device_) = get_namespace_and_device(X, labels)(X, labels) = check_X_y(X, labels)le = LabelEncoder()labels = le.fit_transform(labels)(n_samples, _) = X.shapen_labels = le.classes_.shape[0]check_number_of_labels(n_labels, n_samples)dtype = _max_precision_float_dtype(xp, device_)intra_dists = xp.zeros(n_labels, dtype = dtype, device = device_)centroids = xp.zeros((n_labels, X.shape[1]), dtype = dtype, device = device_)for k in range(n_labels):
cluster_k = _safe_indexing(X, xp.nonzero(labels == k)[0])centroid = _average(cluster_k, axis = 0, xp = xp)centroids[(k, ...)] = centroidintra_dists[k] = _average(pairwise_distances(cluster_k, xp.stack([
centroid])), xp = xp)centroid_distances = pairwise_distances(centroids)zero = xp.asarray(0, device = device_, dtype = dtype)if xp.all(xpx.isclose(intra_dists, zero)) or xp.all(xpx.isclose(centroid_distances, zero)):
0centroid_distances[centroid_distances == 0] = None.infcombined_intra_dists = intra_dists[(:, None)] + intra_distsscores = xp.max(combined_intra_dists / centroid_distances, axis = 1)float(_average(scores, xp = xp)))()
