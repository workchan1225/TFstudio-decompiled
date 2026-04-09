# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _regression.pyc (Python 3.11)

'''Metrics to assess performance on regression task.

Functions named as ``*_score`` return a scalar value to maximize: the higher
the better.

Function named as ``*_error`` or ``*_loss`` return a scalar value to minimize:
the lower the better.
'''
import warnings
from numbers import Real
import numpy as np
from sklearn.exceptions import UndefinedMetricWarning
from sklearn.utils._array_api import _average, _find_matching_floating_dtype, _median, get_namespace, get_namespace_and_device, size
from sklearn.utils._array_api import _xlogy as xlogy
from sklearn.utils._param_validation import Interval, StrOptions, validate_params
from sklearn.utils.stats import _weighted_percentile
from sklearn.utils.validation import _check_sample_weight, _num_samples, check_array, check_consistent_length, column_or_1d
__ALL__ = [
    'max_error',
    'mean_absolute_error',
    'mean_squared_error',
    'mean_squared_log_error',
    'median_absolute_error',
    'mean_absolute_percentage_error',
    'mean_pinball_loss',
    'r2_score',
    'root_mean_squared_log_error',
    'root_mean_squared_error',
    'explained_variance_score',
    'mean_tweedie_deviance',
    'mean_poisson_deviance',
    'mean_gamma_deviance',
    'd2_tweedie_score',
    'd2_pinball_score',
    'd2_absolute_error_score']

def _check_reg_targets(y_true, y_pred, sample_weight, multioutput, dtype, xp = ('numeric', None)):
    '''Check that y_true, y_pred and sample_weight belong to the same regression task.

    To reduce redundancy when calling `_find_matching_floating_dtype`,
    please use `_check_reg_targets_with_floating_dtype` instead.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,) or (n_samples, n_outputs)
        Ground truth (correct) target values.

    y_pred : array-like of shape (n_samples,) or (n_samples, n_outputs)
        Estimated target values.

    sample_weight : array-like of shape (n_samples,) or None
        Sample weights.

    multioutput : array-like or string in [\'raw_values\', uniform_average\',
        \'variance_weighted\'] or None
        None is accepted due to backward compatibility of r2_score().

    dtype : str or list, default="numeric"
        the dtype argument passed to check_array.

    xp : module, default=None
        Precomputed array namespace module. When passed, typically from a caller
        that has already performed inspection of its own inputs, skips array
        namespace inspection.

    Returns
    -------
    type_true : one of {\'continuous\', continuous-multioutput\'}
        The type of the true target data, as output by
        \'utils.multiclass.type_of_target\'.

    y_true : array-like of shape (n_samples, n_outputs)
        Ground truth (correct) target values.

    y_pred : array-like of shape (n_samples, n_outputs)
        Estimated target values.

    sample_weight : array-like of shape (n_samples,) or None
        Sample weights.

    multioutput : array-like of shape (n_outputs) or string in [\'raw_values\',
        uniform_average\', \'variance_weighted\'] or None
        Custom output weights if ``multioutput`` is array-like or
        just the corresponding argument if ``multioutput`` is a
        correct keyword.
    '''
    (xp, _) = get_namespace(y_true, y_pred, multioutput, xp = xp)
    check_consistent_length(y_true, y_pred, sample_weight)
    y_true = check_array(y_true, ensure_2d = False, dtype = dtype)
    y_pred = check_array(y_pred, ensure_2d = False, dtype = dtype)
# WARNING: Decompyle incomplete


def _check_reg_targets_with_floating_dtype(y_true, y_pred, sample_weight, multioutput, xp = (None,)):
    """Ensures y_true, y_pred, and sample_weight correspond to same regression task.

    Extends `_check_reg_targets` by automatically selecting a suitable floating-point
    data type for inputs using `_find_matching_floating_dtype`.

    Use this private method only when converting inputs to array API-compatibles.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,) or (n_samples, n_outputs)
        Ground truth (correct) target values.

    y_pred : array-like of shape (n_samples,) or (n_samples, n_outputs)
        Estimated target values.

    sample_weight : array-like of shape (n_samples,)

    multioutput : array-like or string in ['raw_values', 'uniform_average',         'variance_weighted'] or None
        None is accepted due to backward compatibility of r2_score().

    xp : module, default=None
        Precomputed array namespace module. When passed, typically from a caller
        that has already performed inspection of its own inputs, skips array
        namespace inspection.

    Returns
    -------
    type_true : one of {'continuous', 'continuous-multioutput'}
        The type of the true target data, as output by
        'utils.multiclass.type_of_target'.

    y_true : array-like of shape (n_samples, n_outputs)
        Ground truth (correct) target values.

    y_pred : array-like of shape (n_samples, n_outputs)
        Estimated target values.

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    multioutput : array-like of shape (n_outputs) or string in ['raw_values',         'uniform_average', 'variance_weighted'] or None
        Custom output weights if ``multioutput`` is array-like or
        just the corresponding argument if ``multioutput`` is a
        correct keyword.
    """
    dtype_name = _find_matching_floating_dtype(y_true, y_pred, sample_weight, xp = xp)
    (y_type, y_true, y_pred, sample_weight, multioutput) = _check_reg_targets(y_true, y_pred, sample_weight, multioutput, dtype = dtype_name, xp = xp)
    return (y_type, y_true, y_pred, sample_weight, multioutput)

mean_absolute_error = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_pred': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None],
    'multioutput': [
        StrOptions({
            'raw_values',
            'uniform_average'}),
        'array-like'] }, prefer_skip_nested_validation = True), y_pred = {
    'sample_weight': None,
    'multioutput': 'uniform_average' }, *, sample_weight, multioutput: (xp, _) = get_namespace(y_true, y_pred, sample_weight, multioutput)(_, y_true, y_pred, sample_weight, multioutput) = _check_reg_targets_with_floating_dtype(y_true, y_pred, sample_weight, multioutput, xp = xp)output_errors = _average(xp.abs(y_pred - y_true), weights = sample_weight, axis = 0, xp = xp)if isinstance(multioutput, str):
if multioutput == 'raw_values':
output_errorsif None == 'uniform_average':
multioutput = Nonemean_absolute_error = _average(output_errors, weights = multioutput, xp = xp)float(mean_absolute_error))()
mean_pinball_loss = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_pred': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None],
    'alpha': [
        Interval(Real, 0, 1, closed = 'both')],
    'multioutput': [
        StrOptions({
            'raw_values',
            'uniform_average'}),
        'array-like'] }, prefer_skip_nested_validation = True), y_pred = {
    'sample_weight': None,
    'alpha': 0.5,
    'multioutput': 'uniform_average' }, *, sample_weight, alpha: (xp, _) = get_namespace(y_true, y_pred, sample_weight, multioutput)(_, y_true, y_pred, sample_weight, multioutput) = _check_reg_targets_with_floating_dtype(y_true, y_pred, sample_weight, multioutput, xp = xp)diff = y_true - y_predsign = xp.astype(diff >= 0, diff.dtype)loss = alpha * sign * diff - (1 - alpha) * (1 - sign) * diffoutput_errors = _average(loss, weights = sample_weight, axis = 0, xp = xp)if isinstance(multioutput, str) and multioutput == 'raw_values':
output_errorsif None(multioutput, str) and multioutput == 'uniform_average':
multioutput = Nonefloat(_average(output_errors, weights = multioutput, xp = xp)))()
mean_absolute_percentage_error = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_pred': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None],
    'multioutput': [
        StrOptions({
            'raw_values',
            'uniform_average'}),
        'array-like'] }, prefer_skip_nested_validation = True), y_pred = {
    'sample_weight': None,
    'multioutput': 'uniform_average' }, *, sample_weight, multioutput: (xp, _, device_) = get_namespace_and_device(y_true, y_pred, sample_weight, multioutput)(_, y_true, y_pred, sample_weight, multioutput) = _check_reg_targets_with_floating_dtype(y_true, y_pred, sample_weight, multioutput, xp = xp)epsilon = xp.asarray(xp.finfo(xp.float64).eps, dtype = y_true.dtype, device = device_)y_true_abs = xp.abs(y_true)mape = xp.abs(y_pred - y_true) / xp.maximum(y_true_abs, epsilon)output_errors = _average(mape, weights = sample_weight, axis = 0, xp = xp)if isinstance(multioutput, str):
if multioutput == 'raw_values':
output_errorsif None == 'uniform_average':
multioutput = Nonemean_absolute_percentage_error = _average(output_errors, weights = multioutput, xp = xp)float(mean_absolute_percentage_error))()
mean_squared_error = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_pred': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None],
    'multioutput': [
        StrOptions({
            'raw_values',
            'uniform_average'}),
        'array-like'] }, prefer_skip_nested_validation = True), y_pred = {
    'sample_weight': None,
    'multioutput': 'uniform_average' }, *, sample_weight, multioutput: (xp, _) = get_namespace(y_true, y_pred, sample_weight, multioutput)(_, y_true, y_pred, sample_weight, multioutput) = _check_reg_targets_with_floating_dtype(y_true, y_pred, sample_weight, multioutput, xp = xp)output_errors = _average((y_true - y_pred) ** 2, axis = 0, weights = sample_weight, xp = xp)if isinstance(multioutput, str):
if multioutput == 'raw_values':
output_errorsif None == 'uniform_average':
multioutput = Nonemean_squared_error = _average(output_errors, weights = multioutput, xp = xp)float(mean_squared_error))()
root_mean_squared_error = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_pred': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None],
    'multioutput': [
        StrOptions({
            'raw_values',
            'uniform_average'}),
        'array-like'] }, prefer_skip_nested_validation = True), y_pred = {
    'sample_weight': None,
    'multioutput': 'uniform_average' }, *, sample_weight, multioutput: (xp, _) = get_namespace(y_true, y_pred, sample_weight, multioutput)output_errors = xp.sqrt(mean_squared_error(y_true, y_pred, sample_weight = sample_weight, multioutput = 'raw_values'))if isinstance(multioutput, str):
if multioutput == 'raw_values':
output_errorsif None == 'uniform_average':
multioutput = Noneroot_mean_squared_error = _average(output_errors, weights = multioutput, xp = xp)float(root_mean_squared_error))()
mean_squared_log_error = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_pred': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None],
    'multioutput': [
        StrOptions({
            'raw_values',
            'uniform_average'}),
        'array-like'] }, prefer_skip_nested_validation = True), y_pred = {
    'sample_weight': None,
    'multioutput': 'uniform_average' }, *, sample_weight, multioutput: (xp, _) = get_namespace(y_true, y_pred)(_, y_true, y_pred, sample_weight, multioutput) = _check_reg_targets_with_floating_dtype(y_true, y_pred, sample_weight, multioutput, xp = xp)if xp.any(y_true <= -1) or xp.any(y_pred <= -1):
raise ValueError('Mean Squared Logarithmic Error cannot be used when targets contain values less than or equal to -1.')mean_squared_error(xp.log1p(y_true), xp.log1p(y_pred), sample_weight = sample_weight, multioutput = multioutput))()
root_mean_squared_log_error = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_pred': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None],
    'multioutput': [
        StrOptions({
            'raw_values',
            'uniform_average'}),
        'array-like'] }, prefer_skip_nested_validation = True), y_pred = {
    'sample_weight': None,
    'multioutput': 'uniform_average' }, *, sample_weight, multioutput: (xp, _) = get_namespace(y_true, y_pred)(_, y_true, y_pred, sample_weight, multioutput) = _check_reg_targets_with_floating_dtype(y_true, y_pred, sample_weight, multioutput, xp = xp)if xp.any(y_true <= -1) or xp.any(y_pred <= -1):
raise ValueError('Root Mean Squared Logarithmic Error cannot be used when targets contain values less than or equal to -1.')root_mean_squared_error(xp.log1p(y_true), xp.log1p(y_pred), sample_weight = sample_weight, multioutput = multioutput))()
median_absolute_error = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_pred': [
        'array-like'],
    'multioutput': [
        StrOptions({
            'raw_values',
            'uniform_average'}),
        'array-like'],
    'sample_weight': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), y_pred = {
    'multioutput': 'uniform_average',
    'sample_weight': None }, *, multioutput, sample_weight: (xp, _) = get_namespace(y_true, y_pred, multioutput, sample_weight)(_, y_true, y_pred, sample_weight, multioutput) = _check_reg_targets(y_true, y_pred, sample_weight, multioutput)# WARNING: Decompyle incomplete
)()

def _assemble_r2_explained_variance(numerator, denominator, n_outputs, multioutput, force_finite, xp, device):
    '''Common part used by explained variance score and :math:`R^2` score.'''
    dtype = numerator.dtype
    nonzero_denominator = denominator != 0
    if not force_finite:
        output_scores = 1 - numerator / denominator
    else:
        nonzero_numerator = numerator != 0
        output_scores = xp.ones([
            n_outputs], device = device, dtype = dtype)
        valid_score = nonzero_denominator & nonzero_numerator
        output_scores[valid_score] = 1 - numerator[valid_score] / denominator[valid_score]
        output_scores[nonzero_numerator & ~nonzero_denominator] = 0
    if isinstance(multioutput, str):
        if multioutput == 'raw_values':
            return output_scores
        if None == 'uniform_average':
            avg_weights = None
        elif multioutput == 'variance_weighted':
            avg_weights = denominator
            if not xp.any(nonzero_denominator):
                avg_weights = None
            else:
                avg_weights = multioutput
    result = _average(output_scores, weights = avg_weights, xp = xp)
    if size(result) == 1:
        return float(result)

explained_variance_score = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_pred': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None],
    'multioutput': [
        StrOptions({
            'raw_values',
            'uniform_average',
            'variance_weighted'}),
        'array-like'],
    'force_finite': [
        'boolean'] }, prefer_skip_nested_validation = True), y_pred = {
    'sample_weight': None,
    'multioutput': 'uniform_average',
    'force_finite': True }, *, sample_weight, multioutput: (xp, _, device) = get_namespace_and_device(y_true, y_pred, sample_weight, multioutput)(_, y_true, y_pred, sample_weight, multioutput) = _check_reg_targets_with_floating_dtype(y_true, y_pred, sample_weight, multioutput, xp = xp)y_diff_avg = _average(y_true - y_pred, weights = sample_weight, axis = 0, xp = xp)numerator = _average((y_true - y_pred - y_diff_avg) ** 2, weights = sample_weight, axis = 0, xp = xp)y_true_avg = _average(y_true, weights = sample_weight, axis = 0, xp = xp)denominator = _average((y_true - y_true_avg) ** 2, weights = sample_weight, axis = 0, xp = xp)_assemble_r2_explained_variance(numerator = numerator, denominator = denominator, n_outputs = y_true.shape[1], multioutput = multioutput, force_finite = force_finite, xp = xp, device = device))()
r2_score = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_pred': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None],
    'multioutput': [
        StrOptions({
            'raw_values',
            'uniform_average',
            'variance_weighted'}),
        'array-like',
        None],
    'force_finite': [
        'boolean'] }, prefer_skip_nested_validation = True), y_pred = {
    'sample_weight': None,
    'multioutput': 'uniform_average',
    'force_finite': True }, *, sample_weight, multioutput: (xp, _, device_) = get_namespace_and_device(y_true, y_pred, sample_weight, multioutput)(_, y_true, y_pred, sample_weight, multioutput) = _check_reg_targets_with_floating_dtype(y_true, y_pred, sample_weight, multioutput, xp = xp)if _num_samples(y_pred) < 2:
msg = 'R^2 score is not well-defined with less than two samples.'warnings.warn(msg, UndefinedMetricWarning)float('nan')# WARNING: Decompyle incomplete
)()
max_error = (lambda y_true, y_pred: (xp, _) = get_namespace(y_true, y_pred)(y_type, y_true, y_pred, _, _) = _check_reg_targets(y_true, y_pred, sample_weight = None, multioutput = None, xp = xp)if y_type == 'continuous-multioutput':
raise ValueError('Multioutput not supported in max_error')float(xp.max(xp.abs(y_true - y_pred))))()

def _mean_tweedie_deviance(y_true, y_pred, sample_weight, power):
    '''Mean Tweedie deviance regression loss.'''
    (xp, _) = get_namespace(y_true, y_pred)
    p = power
    if p < 0:
        dev = 2 * ((xp.pow(xp.where(y_true > 0, y_true, 0), 2 - p) / ((1 - p) * (2 - p)) - y_true * xp.pow(y_pred, 1 - p) / (1 - p)) + xp.pow(y_pred, 2 - p) / (2 - p))
    elif p == 0:
        dev = (y_true - y_pred) ** 2
    elif p == 1:
        dev = 2 * ((xlogy(y_true, y_true / y_pred) - y_true) + y_pred)
    elif p == 2:
        dev = 2 * (xp.log(y_pred / y_true) + y_true / y_pred - 1)
    else:
        dev = 2 * ((xp.pow(y_true, 2 - p) / ((1 - p) * (2 - p)) - y_true * xp.pow(y_pred, 1 - p) / (1 - p)) + xp.pow(y_pred, 2 - p) / (2 - p))
    return float(_average(dev, weights = sample_weight, xp = xp))

mean_tweedie_deviance = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_pred': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None],
    'power': [
        Interval(Real, None, 0, closed = 'right'),
        Interval(Real, 1, None, closed = 'left')] }, prefer_skip_nested_validation = True), y_pred = {
    'sample_weight': None,
    'power': 0 }, *, sample_weight, power: (xp, _) = get_namespace(y_true, y_pred)(y_type, y_true, y_pred, sample_weight, _) = _check_reg_targets_with_floating_dtype(y_true, y_pred, sample_weight, multioutput = None, xp = xp)if y_type == 'continuous-multioutput':
raise ValueError('Multioutput not supported in mean_tweedie_deviance')# WARNING: Decompyle incomplete
)()
mean_poisson_deviance = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_pred': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), y_pred = {
    'sample_weight': None }, *, sample_weight,
