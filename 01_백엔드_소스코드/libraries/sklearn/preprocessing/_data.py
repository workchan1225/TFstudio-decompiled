# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _data.pyc (Python 3.11)

import warnings
from numbers import Integral, Real
import numpy as np
from scipy import sparse, stats
from scipy.special import boxcox, inv_boxcox
from sklearn.base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, OneToOneFeatureMixin, TransformerMixin, _fit_context
from sklearn.preprocessing._encoders import OneHotEncoder
from sklearn.utils import _array_api, check_array, metadata_routing, resample
from sklearn.utils._array_api import _find_matching_floating_dtype, _max_precision_float_dtype, _modify_in_place_if_numpy, device, get_namespace, get_namespace_and_device, size, supported_float_dtypes
from sklearn.utils._param_validation import Interval, Options, StrOptions, validate_params
from sklearn.utils.extmath import _incremental_mean_and_var, row_norms
from sklearn.utils.sparsefuncs import incr_mean_variance_axis, inplace_column_scale, mean_variance_axis, min_max_axis
from sklearn.utils.sparsefuncs_fast import inplace_csr_row_normalize_l1, inplace_csr_row_normalize_l2
from sklearn.utils.validation import FLOAT_DTYPES, _check_sample_weight, check_is_fitted, check_random_state, validate_data
BOUNDS_THRESHOLD = 1e-07
__all__ = [
    'Binarizer',
    'KernelCenterer',
    'MaxAbsScaler',
    'MinMaxScaler',
    'Normalizer',
    'OneHotEncoder',
    'PowerTransformer',
    'QuantileTransformer',
    'RobustScaler',
    'StandardScaler',
    'add_dummy_feature',
    'binarize',
    'maxabs_scale',
    'minmax_scale',
    'normalize',
    'power_transform',
    'quantile_transform',
    'robust_scale',
    'scale']

def _is_constant_feature(var, mean, n_samples):
    '''Detect if a feature is indistinguishable from a constant feature.

    The detection is based on its computed variance and on the theoretical
    error bounds of the \'2 pass algorithm\' for variance computation.

    See "Algorithms for computing the sample variance: analysis and
    recommendations", by Chan, Golub, and LeVeque.
    '''
    (xp, _, device_) = get_namespace_and_device(var, mean)
    max_float_dtype = _max_precision_float_dtype(xp = xp, device = device_)
    eps = xp.finfo(max_float_dtype).eps
    upper_bound = n_samples * eps * var + (n_samples * mean * eps) ** 2
    return var <= upper_bound


def _handle_zeros_in_scale(scale, copy, constant_mask = (True, None)):
    '''Set scales of near constant features to 1.

    The goal is to avoid division by very small or zero values.

    Near constant features are detected automatically by identifying
    scales close to machine precision unless they are precomputed by
    the caller and passed with the `constant_mask` kwarg.

    Typically for standard scaling, the scales are the standard
    deviation while near constant features are better detected on the
    computed variances which are closer to machine precision by
    construction.
    '''
    if np.isscalar(scale):
        if scale == 0:
            scale = 1
        return scale
    (xp, _) = None(scale)
# WARNING: Decompyle incomplete

scale = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'axis': [
        Options(Integral, {
            0,
            1})],
    'with_mean': [
        'boolean'],
    'with_std': [
        'boolean'],
    'copy': [
        'boolean'] }, prefer_skip_nested_validation = True), *, axis: X = check_array(X, accept_sparse = 'csc', copy = copy, ensure_2d = False, estimator = 'the scale function', dtype = FLOAT_DTYPES, ensure_all_finite = 'allow-nan', input_name = 'X')if sparse.issparse(X):
if with_mean:
raise ValueError('Cannot center sparse matrices: pass `with_mean=False` instead See docstring for motivation and alternatives.')if axis != 0:
raise ValueError('Can only scale sparse matrix on axis=0,  got axis=%d' % axis)if with_std:
(_, var) = mean_variance_axis(X, axis = 0)var = _handle_zeros_in_scale(var, copy = False)inplace_column_scale(X, 1 / np.sqrt(var))else:
X = np.asarray(X)if with_mean:
mean_ = np.nanmean(X, axis)if with_std:
scale_ = np.nanstd(X, axis)Xr = np.rollaxis(X, axis)if with_mean:
Xr -= mean_mean_1 = np.nanmean(Xr, axis = 0)if not np.allclose(mean_1, 0):
warnings.warn('Numerical issues were encountered when centering the data and might not be solved. Dataset may contain too large values. You may need to prescale your features.')Xr -= mean_1if with_std:
scale_ = _handle_zeros_in_scale(scale_, copy = False)Xr /= scale_if with_mean:
mean_2 = np.nanmean(Xr, axis = 0)if not np.allclose(mean_2, 0):
warnings.warn('Numerical issues were encountered when scaling the data and might not be solved. The standard deviation of the data is probably very close to 0. ')Xr -= mean_2X)()

class MinMaxScaler(BaseEstimator, TransformerMixin, OneToOneFeatureMixin):
    pass
# WARNING: Decompyle incomplete

minmax_scale = (lambda X = validate_params({
    'X': [
        'array-like'],
    'axis': [
        Options(Integral, {
            0,
            1})] }, prefer_skip_nested_validation = False), feature_range = ((0, 1),), *, axis, copy: X = check_array(X, copy = False, ensure_2d = False, dtype = FLOAT_DTYPES, ensure_all_finite = 'allow-nan')original_ndim = X.ndimif original_ndim == 1:
X = X.reshape(X.shape[0], 1)s = MinMaxScaler(feature_range = feature_range, copy = copy)if axis == 0:
X = s.fit_transform(X)else:
X = s.fit_transform(X.T).Tif original_ndim == 1:
X = X.ravel()X)()

class StandardScaler(BaseEstimator, TransformerMixin, OneToOneFeatureMixin):
    pass
# WARNING: Decompyle incomplete


class MaxAbsScaler(BaseEstimator, TransformerMixin, OneToOneFeatureMixin):
    pass
# WARNING: Decompyle incomplete

maxabs_scale = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'axis': [
        Options(Integral, {
            0,
            1})] }, prefer_skip_nested_validation = False), *, axis: X = check_array(X, accept_sparse = ('csr', 'csc'), copy = False, ensure_2d = False, dtype = FLOAT_DTYPES, ensure_all_finite = 'allow-nan')original_ndim = X.ndimif original_ndim == 1:
X = X.reshape(X.shape[0], 1)s = MaxAbsScaler(copy = copy)if axis == 0:
X = s.fit_transform(X)else:
X = s.fit_transform(X.T).Tif original_ndim == 1:
X = X.ravel()X)()

class RobustScaler(BaseEstimator, TransformerMixin, OneToOneFeatureMixin):
    pass
# WARNING: Decompyle incomplete

robust_scale = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'axis': [
        Options(Integral, {
            0,
            1})] }, prefer_skip_nested_validation = False), *, axis: X = check_array(X, accept_sparse = ('csr', 'csc'), copy = False, ensure_2d = False, dtype = FLOAT_DTYPES, ensure_all_finite = 'allow-nan')original_ndim = X.ndimif original_ndim == 1:
X = X.reshape(X.shape[0], 1)s = RobustScaler(with_centering = with_centering, with_scaling = with_scaling, quantile_range = quantile_range, unit_variance = unit_variance, copy = copy)if axis == 0:
X = s.fit_transform(X)else:
X = s.fit_transform(X.T).Tif original_ndim == 1:
X = X.ravel()X)()
normalize = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'norm': [
        StrOptions({
            'l1',
            'l2',
            'max'})],
    'axis': [
        Options(Integral, {
            0,
            1})],
    'copy': [
        'boolean'],
    'return_norm': [
        'boolean'] }, prefer_skip_nested_validation = True), norm = ('l2',), *, axis, copy: if axis == 0:
sparse_format = 'csc'else:
sparse_format = 'csr'(xp, _) = get_namespace(X)X = check_array(X, accept_sparse = sparse_format, copy = copy, estimator = 'the normalize function', dtype = _array_api.supported_float_dtypes(xp), force_writeable = True)if axis == 0:
X = X.Tif sparse.issparse(X):
if return_norm and norm in ('l1', 'l2'):
raise NotImplementedError("return_norm=True is not implemented for sparse matrices with norm 'l1' or norm 'l2'")if norm == 'l1':
inplace_csr_row_normalize_l1(X)elif norm == 'l2':
inplace_csr_row_normalize_l2(X)elif norm == 'max':
(mins, maxes) = min_max_axis(X, 1)norms = np.maximum(abs(mins), maxes)norms_elementwise = norms.repeat(np.diff(X.indptr))mask = norms_elementwise != 0elif norm == 'l1':
xp.sum(xp.abs(X), axis = 1) = Noneelif norm == 'l2':
norms = row_norms(X)elif norm == 'max':
norms = xp.max(xp.abs(X), axis = 1)norms = _handle_zeros_in_scale(norms, copy = False)X /= norms[(:, None)]if axis == 0:
X = X.Tif return_norm:
(X, norms))()

class Normalizer(BaseEstimator, TransformerMixin, OneToOneFeatureMixin):
    pass
# WARNING: Decompyle incomplete

binarize = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'threshold': [
        Interval(Real, None, None, closed = 'neither')],
    'copy': [
        'boolean'] }, prefer_skip_nested_validation = True), *, threshold: X = check_array(X, accept_sparse = [
'csr',
'csc'], force_writeable = True, copy = copy)if sparse.issparse(X):
if threshold < 0:
raise ValueError('Cannot binarize a sparse matrix with threshold < 0')cond = X.data > thresholdnot_cond = np.logical_not(cond)X.data[cond] = 1X.data[not_cond] = 0X.eliminate_zeros()else:
(xp, _, device) = get_namespace_and_device(X)float_dtype = _find_matching_floating_dtype(X, threshold, xp = xp)cond = xp.astype(X, float_dtype, copy = False) > thresholdnot_cond = xp.logical_not(cond)X[cond] = 1X[not_cond] = 0X)()

class Binarizer(BaseEstimator, TransformerMixin, OneToOneFeatureMixin):
    pass
# WARNING: Decompyle incomplete


class KernelCenterer(BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin):
    pass
# WARNING: Decompyle incomplete

add_dummy_feature = (lambda X, value = (1,): X = check_array(X, accept_sparse = [
'csc',
'csr',
'coo'], dtype = FLOAT_DTYPES)(n_samples, n_features) = X.shapeshape = (n_samples, n_features + 1)if sparse.issparse(X):
if X.format == 'coo':
col = X.col + 1col = np.concatenate((np.zeros(n_samples), col))row = np.concatenate((np.arange(n_samples), X.row))data = np.concatenate((np.full(n_samples, value), X.data))sparse.coo_matrix((data, (row, col)), shape)if None.format == 'csc':
indptr = X.indptr + n_samplesindptr = np.concatenate((np.array([
0]), indptr))indices = np.concatenate((np.arange(n_samples), X.indices))data = np.concatenate((np.full(n_samples, value), X.data))sparse.csc_matrix((data, indices, indptr), shape)klass = None.__class__klass(add_dummy_feature(X.tocoo(), value))None.hstack((np.full((n_samples, 1), value), X)))()

class QuantileTransformer(BaseEstimator, TransformerMixin, OneToOneFeatureMixin):
    pass
# WARNING: Decompyle incomplete

quantile_transform = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'axis': [
        Options(Integral, {
            0,
            1})] }, prefer_skip_nested_validation = False), *, axis: n = QuantileTransformer(n_quantiles = n_quantiles, output_distribution = output_distribution, subsample = subsample, ignore_implicit_zeros = ignore_implicit_zeros, random_state = random_state, copy = copy)if axis == 0:
X = n.fit_transform(X)else:
X = n.fit_transform(X.T).TX)()

class PowerTransformer(BaseEstimator, TransformerMixin, OneToOneFeatureMixin):
    pass
# WARNING: Decompyle incomplete

power_transform = (lambda X = validate_params({
    'X': [
        'array-like'] }, prefer_skip_nested_validation = False), method = ('yeo-johnson',), *, standardize, copy: pt = PowerTransformer(method = method, standardize = standardize, copy = copy)pt.fit_transform(X))()
