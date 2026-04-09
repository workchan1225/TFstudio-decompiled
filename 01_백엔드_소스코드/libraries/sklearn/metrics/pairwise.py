# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pairwise.pyc (Python 3.11)

'''Metrics for pairwise distances and affinity of sets of samples.'''
import itertools
import math
import warnings
from functools import partial
from numbers import Integral, Real
import numpy as np
from joblib import effective_n_jobs
from scipy.sparse import csr_matrix, issparse
from scipy.spatial import distance
from sklearn import config_context
from sklearn.exceptions import DataConversionWarning
from sklearn.metrics._pairwise_distances_reduction import ArgKmin
from sklearn.metrics._pairwise_fast import _chi2_kernel_fast, _sparse_manhattan
from sklearn.preprocessing import normalize
from sklearn.utils import check_array, gen_batches, gen_even_slices
from sklearn.utils._array_api import _fill_diagonal, _find_matching_floating_dtype, _is_numpy_namespace, _max_precision_float_dtype, _modify_in_place_if_numpy, get_namespace, get_namespace_and_device
from sklearn.utils._chunking import get_chunk_n_rows
from sklearn.utils._mask import _get_mask
from sklearn.utils._missing import is_scalar_nan
from sklearn.utils._param_validation import Hidden, Interval, MissingValues, Options, StrOptions, validate_params
from sklearn.utils.extmath import row_norms, safe_sparse_dot
from sklearn.utils.fixes import parse_version, sp_base_version
from sklearn.utils.parallel import Parallel, delayed
from sklearn.utils.validation import _num_samples, check_non_negative

def _return_float_dtype(X, Y):
    '''
    1. If dtype of X and Y is float32, then dtype float32 is returned.
    2. Else dtype float is returned.
    '''
    if not issparse(X) and isinstance(X, np.ndarray):
        X = np.asarray(X)
# WARNING: Decompyle incomplete


def _find_floating_dtype_allow_sparse(X, Y, xp = (None,)):
    '''Find matching floating type, allowing for sparse input.'''
    if any([
        issparse(X),
        issparse(Y)]) or _is_numpy_namespace(xp):
        (X, Y, dtype_float) = _return_float_dtype(X, Y)
    else:
        dtype_float = _find_matching_floating_dtype(X, Y, xp = xp)
    return (X, Y, dtype_float)


def check_pairwise_arrays(X = None, Y = {
    'precomputed': False,
    'dtype': 'infer_float',
    'accept_sparse': 'csr',
    'ensure_all_finite': True,
    'ensure_2d': True,
    'copy': False }, *, precomputed, dtype, accept_sparse, ensure_all_finite, ensure_2d, copy):
    '''Set X and Y appropriately and checks inputs.

    If Y is None, it is set as a pointer to X (i.e. not a copy).
    If Y is given, this does not happen.
    All distance metrics should use this function first to assert that the
    given parameters are correct and safe to use.

    Specifically, this function first ensures that both X and Y are arrays,
    then checks that they are at least two dimensional while ensuring that
    their elements are floats (or dtype if provided). Finally, the function
    checks that the size of the second dimension of the two arrays is equal, or
    the equivalent check for a precomputed distance matrix.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples_X, n_features)

    Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features)

    precomputed : bool, default=False
        True if X is to be treated as precomputed distances to the samples in
        Y.

    dtype : str, type, list of type or None default="infer_float"
        Data type required for X and Y. If "infer_float", the dtype will be an
        appropriate float type selected by _return_float_dtype. If None, the
        dtype of the input is preserved.

        .. versionadded:: 0.18

    accept_sparse : str, bool or list/tuple of str, default=\'csr\'
        String[s] representing allowed sparse matrix formats, such as \'csc\',
        \'csr\', etc. If the input is sparse but not in the allowed format,
        it will be converted to the first listed format. True allows the input
        to be any format. False means that a sparse matrix input will
        raise an error.

    ensure_all_finite : bool or \'allow-nan\', default=True
        Whether to raise an error on np.inf, np.nan, pd.NA in array. The
        possibilities are:

        - True: Force all values of array to be finite.
        - False: accepts np.inf, np.nan, pd.NA in array.
        - \'allow-nan\': accepts only np.nan and pd.NA values in array. Values
          cannot be infinite.

        .. versionadded:: 1.6
           `force_all_finite` was renamed to `ensure_all_finite`.

    ensure_2d : bool, default=True
        Whether to raise an error when the input arrays are not 2-dimensional. Setting
        this to `False` is necessary when using a custom metric with certain
        non-numerical inputs (e.g. a list of strings).

        .. versionadded:: 1.5

    copy : bool, default=False
        Whether a forced copy will be triggered. If copy=False, a copy might
        be triggered by a conversion.

        .. versionadded:: 0.22

    Returns
    -------
    safe_X : {array-like, sparse matrix} of shape (n_samples_X, n_features)
        An array equal to X, guaranteed to be a numpy array.

    safe_Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features)
        An array equal to Y if Y was not None, guaranteed to be a numpy array.
        If Y was None, safe_Y will be a pointer to X.
    '''
    (xp, _) = get_namespace(X, Y)
    (X, Y, dtype_float) = _find_floating_dtype_allow_sparse(X, Y, xp = xp)
    estimator = 'check_pairwise_arrays'
    if dtype == 'infer_float':
        dtype = dtype_float
# WARNING: Decompyle incomplete


def check_paired_arrays(X, Y):
    '''Set X and Y appropriately and checks inputs for paired distances.

    All paired distance metrics should use this function first to assert that
    the given parameters are correct and safe to use.

    Specifically, this function first ensures that both X and Y are arrays,
    then checks that they are at least two dimensional while ensuring that
    their elements are floats. Finally, the function checks that the size
    of the dimensions of the two arrays are equal.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples_X, n_features)

    Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features)

    Returns
    -------
    safe_X : {array-like, sparse matrix} of shape (n_samples_X, n_features)
        An array equal to X, guaranteed to be a numpy array.

    safe_Y : {array-like, sparse matrix} of shape (n_samples_Y, n_features)
        An array equal to Y if Y was not None, guaranteed to be a numpy array.
        If Y was None, safe_Y will be a pointer to X.
    '''
    (X, Y) = check_pairwise_arrays(X, Y)
    if X.shape != Y.shape:
        raise ValueError(f'''X and Y should be of same shape. They were respectively {X.shape!r} and {Y.shape!r} long.''')
    return (X, Y)

euclidean_distances = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'Y': [
        'array-like',
        'sparse matrix',
        None],
    'Y_norm_squared': [
        'array-like',
        None],
    'squared': [
        'boolean'],
    'X_norm_squared': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), Y = (None,), *, Y_norm_squared, squared: (xp, _) = get_namespace(X, Y)(X, Y) = check_pairwise_arrays(X, Y)# WARNING: Decompyle incomplete
)()

def _euclidean_distances(X, Y, X_norm_squared, Y_norm_squared, squared = (None, None, False)):
    '''Computational part of euclidean_distances

    Assumes inputs are already checked.

    If norms are passed as float32, they are unused. If arrays are passed as
    float32, norms needs to be recomputed on upcast chunks.
    TODO: use a float64 accumulator in row_norms to avoid the latter.
    '''
    (xp, _, device_) = get_namespace_and_device(X, Y)
# WARNING: Decompyle incomplete

nan_euclidean_distances = (lambda X = validate_params({
    'X': [
        'array-like'],
    'Y': [
        'array-like',
        None],
    'squared': [
        'boolean'],
    'missing_values': [
        MissingValues(numeric_only = True)],
    'copy': [
        'boolean'] }, prefer_skip_nested_validation = True), Y = (None,), *, squared, missing_values: ensure_all_finite = 'allow-nan' if is_scalar_nan(missing_values) else True(X, Y) = check_pairwise_arrays(X, Y, accept_sparse = False, ensure_all_finite = ensure_all_finite, copy = copy)missing_X = _get_mask(X, missing_values)missing_Y = missing_X if Y is X else _get_mask(Y, missing_values)X[missing_X] = 0Y[missing_Y] = 0distances = euclidean_distances(X, Y, squared = True)XX = X * XYY = Y * Ydistances -= np.dot(XX, missing_Y.T)distances -= np.dot(missing_X, YY.T)np.clip(distances, 0, None, out = distances)if X is Y:
np.fill_diagonal(distances, 0)present_X = 1 - missing_Xpresent_Y = present_X if Y is X else ~missing_Ypresent_count = np.dot(present_X, present_Y.T)distances[present_count == 0] = np.nannp.maximum(1, present_count, out = present_count)distances /= present_countdistances *= X.shape[1]if not squared:
np.sqrt(distances, out = distances)distances)()

def _euclidean_distances_upcast(X, XX, Y, YY, batch_size = (None, None, None, None)):
    '''Euclidean distances between X and Y.

    Assumes X and Y have float32 dtype.
    Assumes XX and YY have float64 dtype or are None.

    X and Y are upcast to float64 by chunks, which size is chosen to limit
    memory increase by approximately 10% (at least 10MiB).
    '''
    (xp, _, device_) = get_namespace_and_device(X, Y)
    n_samples_X = X.shape[0]
    n_samples_Y = Y.shape[0]
    n_features = X.shape[1]
    distances = xp.empty((n_samples_X, n_samples_Y), dtype = xp.float32, device = device_)
# WARNING: Decompyle incomplete


def _argmin_min_reduce(dist, start):
    indices = dist.argmin(axis = 1)
    values = dist[(np.arange(dist.shape[0]), indices)]
    return (indices, values)


def _argmin_reduce(dist, start):
    return dist.argmin(axis = 1)

_VALID_METRICS = [
    'euclidean',
    'l2',
    'l1',
    'manhattan',
    'cityblock',
    'braycurtis',
    'canberra',
    'chebyshev',
    'correlation',
    'cosine',
    'dice',
    'hamming',
    'jaccard',
    'mahalanobis',
    'matching',
    'minkowski',
    'rogerstanimoto',
    'russellrao',
    'seuclidean',
    'sokalsneath',
    'sqeuclidean',
    'yule',
    'wminkowski',
    'nan_euclidean',
    'haversine']
if sp_base_version < parse_version('1.17'):
    _VALID_METRICS += [
        'sokalmichener']
if sp_base_version < parse_version('1.11'):
    _VALID_METRICS += [
        'kulsinski']
if sp_base_version < parse_version('1.9'):
    _VALID_METRICS += [
        'matching']
_NAN_METRICS = [
    'nan_euclidean']
pairwise_distances_argmin_min = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'Y': [
        'array-like',
        'sparse matrix'],
    'axis': [
        Options(Integral, {
            0,
            1})],
    'metric': [
        StrOptions(set(_VALID_METRICS).union(ArgKmin.valid_metrics())),
        callable],
    'metric_kwargs': [
        dict,
        None] }, prefer_skip_nested_validation = False), Y = {
    'axis': 1,
    'metric': 'euclidean',
    'metric_kwargs': None }, *, axis, metric: ensure_all_finite = 'allow-nan' if metric == 'nan_euclidean' else True(X, Y) = check_pairwise_arrays(X, Y, ensure_all_finite = ensure_all_finite)if axis == 0:
Y = XX = Y# WARNING: Decompyle incomplete
)()
pairwise_distances_argmin = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'Y': [
        'array-like',
        'sparse matrix'],
    'axis': [
        Options(Integral, {
            0,
            1})],
    'metric': [
        StrOptions(set(_VALID_METRICS).union(ArgKmin.valid_metrics())),
        callable],
    'metric_kwargs': [
        dict,
        None] }, prefer_skip_nested_validation = False), Y = {
    'axis': 1,
    'metric': 'euclidean',
    'metric_kwargs': None }, *, axis, metric: ensure_all_finite = 'allow-nan' if metric == 'nan_euclidean' else True(X, Y) = check_pairwise_arrays(X, Y, ensure_all_finite = ensure_all_finite)if axis == 0:
Y = XX = Y# WARNING: Decompyle incomplete
)()
haversine_distances = (lambda X, Y = (None,): DistanceMetric = DistanceMetricimport sklearn.metricsDistanceMetric.get_metric('haversine').pairwise(X, Y))()
manhattan_distances = (lambda X, Y = (None,): (X, Y) = check_pairwise_arrays(X, Y)n_y = Y.shape[0]n_x = X.shape[0]if issparse(X) or issparse(Y):
X = csr_matrix(X, copy = False)Y = csr_matrix(Y, copy = False)X.sum_duplicates()Y.sum_duplicates()D = np.zeros((n_x, n_y))_sparse_manhattan(X.data, X.indices, X.indptr, Y.data, Y.indices, Y.indptr, D)D(xp, _, device_) = None(X, Y)if _is_numpy_namespace(xp):
distance.cdist(X, Y, 'cityblock')float_dtype = None(X, Y, xp = xp)out = xp.empty((n_x, n_y), dtype = float_dtype, device = device_)batch_size = 1024for i in range(0, n_x, batch_size):
i_end = min(i + batch_size, n_x)batch_X = X[(i:i_end, ...)]for j in range(0, n_y, batch_size):
j_end = min(j + batch_size, n_y)batch_Y = Y[(j:j_end, ...)]block_dist = xp.sum(xp.abs(batch_X[(:, None, :)] - batch_Y[(None, :, :)]), axis = 2)out[(i:i_end, j:j_end)] = block_distout)()
cosine_distances = (lambda X, Y = (None,): (xp, _) = get_namespace(X, Y)S = cosine_similarity(X, Y)S *= -1S += 1S = xp.clip(S, 0, 2)# WARNING: Decompyle incomplete
)()
paired_euclidean_distances = (lambda X, Y: (X, Y) = check_paired_arrays(X, Y)row_norms(X - Y))()
paired_manhattan_distances = (lambda X, Y: (X, Y) = check_paired_arrays(X, Y)diff = X - Yif issparse(diff):
diff.data = np.abs(diff.data)np.squeeze(np.array(diff.sum(axis = 1)))None.abs(diff).sum(axis = -1))()
paired_cosine_distances = (lambda X, Y: (X, Y) = check_paired_arrays(X, Y)0.5 * row_norms(normalize(X) - normalize(Y), squared = True))()
PAIRED_DISTANCES = {
    'cosine': paired_cosine_distances,
    'euclidean': paired_euclidean_distances,
    'l2': paired_euclidean_distances,
    'l1': paired_manhattan_distances,
    'manhattan': paired_manhattan_distances,
    'cityblock': paired_manhattan_distances }
paired_distances = (lambda X = validate_params({
    'X': [
        'array-like'],
    'Y': [
        'array-like'],
    'metric': [
        StrOptions(set(PAIRED_DISTANCES)),
        callable] }, prefer_skip_nested_validation = True), Y = {
    'metric': 'euclidean' }, *, metric, kwds = None: if metric in PAIRED_DISTANCES:
func = PAIRED_DISTANCES[metric]func(X, Y)if None(metric):
(X, Y) = check_paired_arrays(X, Y)distances = np.zeros(len(X))for i in range(len(X)):
distances[i] = metric(X[i], Y[i])distancesNone)()
linear_kernel = (lambda X, Y, dense_output = (None, True): (X, Y) = check_pairwise_arrays(X, Y)safe_sparse_dot(X, Y.T, dense_output = dense_output))()
polynomial_kernel = (lambda X, Y, degree, gamma, coef0 = (None, 3, None, 1): (X, Y) = check_pairwise_arrays(X, Y)# WARNING: Decompyle incomplete
)()
sigmoid_kernel = (lambda X, Y, gamma, coef0 = (None, None, 1): (xp, _) = get_namespace(X, Y)(X, Y) = check_pairwise_arrays(X, Y)# WARNING: Decompyle incomplete
)()
rbf_kernel = (lambda X, Y, gamma = (None, None): (xp, _) = get_namespace(X, Y)(X, Y) = check_pairwise_arrays(X, Y)# WARNING: Decompyle incomplete
)()
laplacian_kernel = (lambda X, Y, gamma = (None, None): (X, Y) = check_pairwise_arrays(X, Y)# WARNING: Decompyle incomplete
)()
cosine_similarity = (lambda X, Y, dense_output = (None, True): (X, Y) = check_pairwise_arrays(X, Y)X_normalized = normalize(X, copy = True)if X is Y:
Y_normalized = X_normalizedelse:
Y_normalized = normalize(Y, copy = True)K = safe_sparse_dot(X_normalized, Y_normalized.T, dense_output = dense_output)K)()
additive_chi2_kernel = (lambda X, Y = (None,): (xp, _, device_) = get_namespace_and_device(X, Y)(X, Y) = check_pairwise_arrays(X, Y, accept_sparse = False)if xp.any(X < 0):
raise ValueError('X contains negative values.')if Y is not X and xp.any(Y < 0):
raise ValueError('Y contains negative values.')if _is_numpy_namespace(xp):
result = np.zeros((X.shape[0], Y.shape[0]), dtype = X.dtype)_chi2_kernel_fast(X, Y, result)resultdtype = None(X, Y, xp = xp)xb = X[(:, None, :)]yb = Y[(None, :, :)]nom = -(xb - yb) ** 2denom = xb + ybnom = xp.where(denom == 0, xp.asarray(0, dtype = dtype, device = device_), nom)denom = xp.where(denom == 0, xp.asarray(1, dtype = dtype, device = device_), denom)xp.sum(nom / denom, axis = 2))()
chi2_kernel = (lambda X, Y, gamma = (None, 1): (xp, _) = get_namespace(X, Y)K = additive_chi2_kernel(X, Y)K *= gammaif _is_numpy_namespace(xp):
np.exp(K, out = K)None.exp(K))()
PAIRWISE_DISTANCE_FUNCTIONS = {
    'cityblock': manhattan_distances,
    'cosine': cosine_distances,
    'euclidean': euclidean_distances,
    'haversine': haversine_distances,
    'l2': euclidean_distances,
    'l1': manhattan_distances,
    'manhattan': manhattan_distances,
    'precomputed': None,
    'nan_euclidean': nan_euclidean_distances }

def distance_metrics():
    """Valid metrics for pairwise_distances.

    This function simply returns the valid pairwise distance metrics.
    It exists to allow for a description of the mapping for
    each of the valid strings.

    The valid distance metrics, and the function they map to, are:

    =============== ========================================
    metric          Function
    =============== ========================================
    'cityblock'     metrics.pairwise.manhattan_distances
    'cosine'        metrics.pairwise.cosine_distances
    'euclidean'     metrics.pairwise.euclidean_distances
    'haversine'     metrics.pairwise.haversine_distances
    'l1'            metrics.pairwise.manhattan_distances
    'l2'            metrics.pairwise.euclidean_distances
    'manhattan'     metrics.pairwise.manhattan_distances
    'nan_euclidean' metrics.pairwise.nan_euclidean_distances
    =============== ========================================

    Read more in the :ref:`User Guide <metrics>`.

    Returns
    -------
    distance_metrics : dict
        Returns valid metrics for pairwise_distances.
    """
    return PAIRWISE_DISTANCE_FUNCTIONS


def _transposed_dist_wrapper(dist_func, dist_matrix, slice_, *args, **kwargs):
    '''Write in-place to a slice of a distance matrix.'''
    pass
# WARNING: Decompyle incomplete


def _parallel_pairwise(X, Y, func, n_jobs, **kwds):
    '''Break the pairwise matrix in n_jobs even slices
    and compute them using multithreading.'''
    pass
# WARNING: Decompyle incomplete


def _pairwise_callable(X, Y, metric, ensure_all_finite = (True,), **kwds):
    '''Handle the callable case for pairwise_{distances,kernels}.'''
    (xp, _, device) = get_namespace_and_device(X)
    (X, Y) = check_pairwise_arrays(X, Y, dtype = None, ensure_all_finite = ensure_all_finite, ensure_2d = False)
    (_, _, dtype_float) = _find_floating_dtype_allow_sparse(X, Y, xp = xp)
    
    def _get_slice(array, index):
        if issparse(array):
            return array[([
                index], :)]
        if None.ndim == 1:
            return array[index]
        return None[(index, ...)]

# WARNING: Decompyle incomplete


def _check_chunk_size(reduced, chunk_size):
    '''Checks chunk is a sequence of expected size or a tuple of same.'''
    pass
# WARNING: Decompyle incomplete


def _precompute_metric_params(X, Y, metric = (None,), **kwds):
    '''Precompute data-derived metric parameters if not provided.'''
    if metric == 'seuclidean' and 'V' not in kwds:
        if X is Y:
            V = np.var(X, axis = 0, ddof = 1)
        else:
            raise ValueError("The 'V' parameter is required for the seuclidean metric when Y is passed.")
        return {
            'V': V }
    if None == 'mahalanobis' and 'VI' not in kwds:
        if X is Y:
            VI = np.linalg.inv(np.cov(X.T)).T
        else:
            raise ValueError("The 'VI' parameter is required for the mahalanobis metric when Y is passed.")
        return {
            'VI': VI }

pairwise_distances_chunked = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'Y': [
        'array-like',
        'sparse matrix',
        None],
    'reduce_func': [
        callable,
        None],
    'metric': [
        StrOptions({
            'precomputed'}.union(_VALID_METRICS)),
        callable],
    'n_jobs': [
        Integral,
        None],
    'working_memory': [
        Interval(Real, 0, None, closed = 'left'),
        None] }, prefer_skip_nested_validation = False), Y = (None,), *, reduce_func, metric: pass# WARNING: Decompyle incomplete
)()
pairwise_distances = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'Y': [
        'array-like',
        'sparse matrix',
        None],
    'metric': [
        StrOptions(set(_VALID_METRICS) | {
            'precomputed'}),
        callable],
    'n_jobs': [
        Integral,
        None],
    'ensure_all_finite': [
        'boolean',
        StrOptions({
            'allow-nan'})] }, prefer_skip_nested_validation = True), Y = (None, 'euclidean'), metric = {
    'n_jobs': None,
    'ensure_all_finite': True }, *, n_jobs, ensure_all_finite, kwds = None: if metric == 'precomputed':
(X, _) = check_pairwise_arrays(X, Y, precomputed = True, ensure_all_finite = ensure_all_finite)whom = '`pairwise_distances`. Precomputed distance  need to have non-negative values.'check_non_negative(X, whom = whom)Xif None in PAIRWISE_DISTANCE_FUNCTIONS:
func = PAIRWISE_DISTANCE_FUNCTIONS[metric]# WARNING: Decompyle incomplete
)()
PAIRWISE_BOOLEAN_FUNCTIONS = [
    'dice',
    'jaccard',
    'rogerstanimoto',
    'russellrao',
    'sokalsneath',
    'yule']
if sp_base_version < parse_version('1.17'):
    PAIRWISE_BOOLEAN_FUNCTIONS += [
        'sokalmichener']
if sp_base_version < parse_version('1.11'):
    PAIRWISE_BOOLEAN_FUNCTIONS += [
        'kulsinski']
if sp_base_version < parse_version('1.9'):
    PAIRWISE_BOOLEAN_FUNCTIONS += [
        'matching']
PAIRWISE_KERNEL_FUNCTIONS = {
    'additive_chi2': additive_chi2_kernel,
    'chi2': chi2_kernel,
    'linear': linear_kernel,
    'polynomial': polynomial_kernel,
    'poly': polynomial_kernel,
    'rbf': rbf_kernel,
    'laplacian': laplacian_kernel,
    'sigmoid': sigmoid_kernel,
    'cosine': cosine_similarity }

def kernel_metrics():
    """Valid metrics for pairwise_kernels.

    This function simply returns the valid pairwise distance metrics.
    It exists, however, to allow for a verbose description of the mapping for
    each of the valid strings.

    The valid distance metrics, and the function they map to, are:
      ===============   ========================================
      metric            Function
      ===============   ========================================
      'additive_chi2'   sklearn.pairwise.additive_chi2_kernel
      'chi2'            sklearn.pairwise.chi2_kernel
      'linear'          sklearn.pairwise.linear_kernel
      'poly'            sklearn.pairwise.polynomial_kernel
      'polynomial'      sklearn.pairwise.polynomial_kernel
      'rbf'             sklearn.pairwise.rbf_kernel
      'laplacian'       sklearn.pairwise.laplacian_kernel
      'sigmoid'         sklearn.pairwise.sigmoid_kernel
      'cosine'          sklearn.pairwise.cosine_similarity
      ===============   ========================================

    Read more in the :ref:`User Guide <metrics>`.

    Returns
    -------
    kernel_metrics : dict
        Returns valid metrics for pairwise_kernels.
    """
    return PAIRWISE_KERNEL_FUNCTIONS

KERNEL_PARAMS = {
    'additive_chi2': (),
    'chi2': frozenset([
        'gamma']),
    'cosine': (),
    'linear': (),
    'poly': frozenset([
        'gamma',
        'degree',
        'coef0']),
    'polynomial': frozenset([
        'gamma',
        'degree',
        'coef0']),
    'rbf': frozenset([
        'gamma']),
    'laplacian': frozenset([
        'gamma']),
    'sigmoid': frozenset([
        'gamma',
        'coef0']) }
pairwise_kernels = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'Y': [
        'array-like',
        'sparse matrix',
        None],
    'metric': [
        StrOptions(set(PAIRWISE_KERNEL_FUNCTIONS) | {
            'precomputed'}),
        callable],
    'filter_params': [
        'boolean'],
    'n_jobs': [
        Integral,
        None] }, prefer_skip_nested_validation = True), Y = (None, 'linear'), metric = {
    'filter_params': False,
    'n_jobs': None }, *, filter_params, n_jobs, kwds = None: pass# WARNING: Decompyle incomplete
)()
