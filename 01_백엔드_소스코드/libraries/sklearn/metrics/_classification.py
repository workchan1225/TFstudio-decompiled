# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _classification.pyc (Python 3.11)

'''Metrics to assess performance on classification task given class prediction.

Functions named as ``*_score`` return a scalar value to maximize: the higher
the better.

Function named as ``*_error`` or ``*_loss`` return a scalar value to minimize:
the lower the better.
'''
import warnings
from contextlib import nullcontext
from math import sqrt
from numbers import Integral, Real
import numpy as np
from scipy.sparse import coo_matrix, csr_matrix, issparse
from scipy.special import xlogy
from sklearn.exceptions import UndefinedMetricWarning
from sklearn.preprocessing import LabelBinarizer, LabelEncoder
from sklearn.utils import assert_all_finite, check_array, check_consistent_length, check_scalar, column_or_1d
from sklearn.utils._array_api import _average, _bincount, _convert_to_numpy, _count_nonzero, _fill_diagonal, _find_matching_floating_dtype, _is_numpy_namespace, _is_xp_namespace, _isin, _max_precision_float_dtype, _tolist, _union1d, get_namespace, get_namespace_and_device, move_to, supported_float_dtypes, xpx
from sklearn.utils._param_validation import Hidden, Interval, Options, StrOptions, validate_params
from sklearn.utils._unique import attach_unique
from sklearn.utils.extmath import _nanaverage
from sklearn.utils.multiclass import type_of_target, unique_labels
from sklearn.utils.validation import _check_pos_label_consistency, _check_sample_weight, _num_samples

def _check_zero_division(zero_division):
    if isinstance(zero_division, str) and zero_division == 'warn':
        return np.float64(0)
    if None(zero_division, (int, float)) and zero_division in (0, 1):
        return np.float64(zero_division)
    return None.nan


def _check_targets(y_true, y_pred, sample_weight = (None,)):
    """Check that y_true and y_pred belong to the same classification task.

    This converts multiclass or binary types to a common shape, and raises a
    ValueError for a mix of multilabel and multiclass targets, a mix of
    multilabel formats, for the presence of continuous-valued or multioutput
    targets, or for targets of different lengths.

    Column vectors are squeezed to 1d, while multilabel formats are returned
    as CSR sparse label indicators.

    Parameters
    ----------
    y_true : array-like

    y_pred : array-like

    sample_weight : array-like, default=None

    Returns
    -------
    type_true : one of {'multilabel-indicator', 'multiclass', 'binary'}
        The type of the true target data, as output by
        ``utils.multiclass.type_of_target``.

    y_true : array or indicator matrix

    y_pred : array or indicator matrix

    sample_weight : array or None
    """
    (xp, _) = get_namespace(y_true, y_pred, sample_weight)
    check_consistent_length(y_true, y_pred, sample_weight)
    type_true = type_of_target(y_true, input_name = 'y_true')
    type_pred = type_of_target(y_pred, input_name = 'y_pred')
# WARNING: Decompyle incomplete


def _one_hot_encoding_multiclass_target(y_true, labels, target_xp, target_device):
    '''Convert multi-class `y_true` into a one-hot encoded array and also ensure
    that the encoded array is placed on the target API namespace and device.
    Also return the classes provided by `LabelBinarizer` in additional to the
    integer encoded array.
    '''
    (xp, _) = get_namespace(y_true)
    lb = LabelBinarizer()
# WARNING: Decompyle incomplete


def _validate_multiclass_probabilistic_prediction(y_true, y_prob, sample_weight, labels):
    """Convert y_true and y_prob to shape (n_samples, n_classes)

    1. Verify that y_true, y_prob, and sample_weights have the same first dim
    2. Ensure 2 or more classes in y_true i.e. valid classification task. The
       classes are provided by the labels argument, or inferred using y_true.
       When inferring y_true is assumed binary if it has shape (n_samples, ).
    3. Validate y_true, and y_prob have the same number of classes. Convert to
       shape (n_samples, n_classes)

    Parameters
    ----------
    y_true : array-like or label indicator matrix
        Ground truth (correct) labels for n_samples samples.

    y_prob : array of floats, shape=(n_samples, n_classes) or (n_samples,)
        Predicted probabilities, as returned by a classifier's
        predict_proba method. If `y_prob.shape = (n_samples,)`
        the probabilities provided are assumed to be that of the
        positive class. The labels in `y_prob` are assumed to be
        ordered lexicographically, as done by
        :class:`preprocessing.LabelBinarizer`.

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    labels : array-like, default=None
        If not provided, labels will be inferred from y_true. If `labels`
        is `None` and `y_prob` has shape `(n_samples,)` the labels are
        assumed to be binary and are inferred from `y_true`.

    Returns
    -------
    transformed_labels : array of shape (n_samples, n_classes)

    y_prob : array of shape (n_samples, n_classes)
    """
    (xp, _, device_) = get_namespace_and_device(y_prob)
    if xp.max(y_prob) > 1:
        raise ValueError(f'''y_prob contains values greater than 1: {xp.max(y_prob)}''')
    if xp.min(y_prob) < 0:
        raise ValueError(f'''y_prob contains values lower than 0: {xp.min(y_prob)}''')
    check_consistent_length(y_prob, y_true, sample_weight)
# WARNING: Decompyle incomplete

accuracy_score = (lambda y_true = validate_params({
    'y_true': [
        'array-like',
        'sparse matrix'],
    'y_pred': [
        'array-like',
        'sparse matrix'],
    'normalize': [
        'boolean'],
    'sample_weight': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), y_pred = {
    'normalize': True,
    'sample_weight': None }, *, normalize, sample_weight: (xp, _, device) = get_namespace_and_device(y_pred)(y_true, sample_weight) = move_to(y_true, sample_weight, xp = xp, device = device)(y_true, y_pred) = attach_unique(y_true, y_pred)(y_type, y_true, y_pred, sample_weight) = _check_targets(y_true, y_pred, sample_weight)if y_type.startswith('multilabel'):
differing_labels = _count_nonzero(y_true - y_pred, xp = xp, device = device, axis = 1)score = xp.asarray(differing_labels == 0, device = device)else:
score = y_true == y_predfloat(_average(score, weights = sample_weight, normalize = normalize, xp = xp)))()
confusion_matrix = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_pred': [
        'array-like'],
    'labels': [
        'array-like',
        None],
    'sample_weight': [
        'array-like',
        None],
    'normalize': [
        StrOptions({
            'all',
            'pred',
            'true'}),
        None] }, prefer_skip_nested_validation = True), y_pred = {
    'labels': None,
    'sample_weight': None,
    'normalize': None }, *, labels, sample_weight: pass# WARNING: Decompyle incomplete
)()
multilabel_confusion_matrix = (lambda y_true = validate_params({
    'y_true': [
        'array-like',
        'sparse matrix'],
    'y_pred': [
        'array-like',
        'sparse matrix'],
    'sample_weight': [
        'array-like',
        None],
    'labels': [
        'array-like',
        None],
    'samplewise': [
        'boolean'] }, prefer_skip_nested_validation = True), y_pred = {
    'sample_weight': None,
    'labels': None,
    'samplewise': False }, *, sample_weight, labels: (y_true, y_pred) = attach_unique(y_true, y_pred)(xp, _, device_) = get_namespace_and_device(y_true, y_pred, sample_weight)(y_type, y_true, y_pred, sample_weight) = _check_targets(y_true, y_pred, sample_weight)if y_type not in ('binary', 'multiclass', 'multilabel-indicator'):
raise ValueError('%s is not supported' % y_type)present_labels = unique_labels(y_true, y_pred)# WARNING: Decompyle incomplete
)()
cohen_kappa_score = (lambda y1 = validate_params({
    'y1': [
        'array-like'],
    'y2': [
        'array-like'],
    'labels': [
        'array-like',
        None],
    'weights': [
        StrOptions({
            'linear',
            'quadratic'}),
        None],
    'sample_weight': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), y2 = {
    'labels': None,
    'weights': None,
    'sample_weight': None }, *, labels, weights: try:
confusion = confusion_matrix(y1, y2, labels = labels, sample_weight = sample_weight)except ValueError:
e = Noneif 'At least one label specified must be in y_true' in str(e):
msg = 'At least one label in `labels` must be present in `y1` (even though `cohen_kappa_score` is otherwise agnostic to the order of `y1` and `y2`).'raise ValueError(msg), eraise e = Nonedel e(xp, _, device_) = get_namespace_and_device(y1, y2)n_classes = confusion.shape[0]max_float_dtype = _max_precision_float_dtype(xp, device = device_)confusion = xp.astype(confusion, max_float_dtype, copy = False)sum0 = xp.sum(confusion, axis = 0)sum1 = xp.sum(confusion, axis = 1)expected = xp.linalg.outer(sum0, sum1) / xp.sum(sum0)# WARNING: Decompyle incomplete
)()
jaccard_score = (lambda y_true = validate_params({
    'y_true': [
        'array-like',
        'sparse matrix'],
    'y_pred': [
        'array-like',
        'sparse matrix'],
    'labels': [
        'array-like',
        None],
    'pos_label': [
        Real,
        str,
        'boolean',
        None],
    'average': [
        StrOptions({
            'macro',
            'micro',
            'binary',
            'samples',
            'weighted'}),
        None],
    'sample_weight': [
        'array-like',
        None],
    'zero_division': [
        Options(Real, {
            0,
            1}),
        StrOptions({
            'warn'})] }, prefer_skip_nested_validation = True), y_pred = {
    'labels': None,
    'pos_label': 1,
    'average': 'binary',
    'sample_weight': None,
    'zero_division': 'warn' }, *, labels, pos_label: labels = _check_set_wise_labels(y_true, y_pred, average, labels, pos_label)samplewise = average == 'samples'MCM = multilabel_confusion_matrix(y_true, y_pred, sample_weight = sample_weight, labels = labels, samplewise = samplewise)numerator = MCM[(:, 1, 1)]denominator = MCM[(:, 1, 1)] + MCM[(:, 0, 1)] + MCM[(:, 1, 0)](xp, _, device_) = get_namespace_and_device(y_true, y_pred)if average == 'micro':
numerator = xp.asarray(xp.sum(numerator, keepdims = True), device = device_)denominator = xp.asarray(xp.sum(denominator, keepdims = True), device = device_)jaccard = _prf_divide(numerator, denominator, 'jaccard', 'true or predicted', average, ('jaccard',), zero_division = zero_division)# WARNING: Decompyle incomplete
)()
matthews_corrcoef = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_pred': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), y_pred = {
    'sample_weight': None }, *, sample_weight, y_type = None: (y_true, y_pred) = attach_unique(y_true, y_pred)(y_type, y_true, y_pred, sample_weight) = _check_targets(y_true, y_pred, sample_weight)if y_type not in frozenset({'binary', 'multiclass'}):
raise ValueError('%s is not supported' % y_type)lb = LabelEncoder()lb.fit(np.hstack([
y_true,
y_pred]))y_true = lb.transform(y_true)y_pred = lb.transform(y_pred)C = confusion_matrix(y_true, y_pred, sample_weight = sample_weight)t_sum = C.sum(axis = 1, dtype = np.float64)p_sum = C.sum(axis = 0, dtype = np.float64)n_correct = np.trace(C, dtype = np.float64)n_samples = p_sum.sum()cov_ytyp = n_correct * n_samples - np.dot(t_sum, p_sum)cov_ypyp = n_samples ** 2 - np.dot(p_sum, p_sum)cov_ytyt = n_samples ** 2 - np.dot(t_sum, t_sum)cov_ypyp_ytyt = cov_ypyp * cov_ytytif cov_ypyp_ytyt == 0:
0None(cov_ytyp / np.sqrt(cov_ypyp_ytyt)))()
zero_one_loss = (lambda y_true = validate_params({
    'y_true': [
        'array-like',
        'sparse matrix'],
    'y_pred': [
        'array-like',
        'sparse matrix'],
    'normalize': [
        'boolean'],
    'sample_weight': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), y_pred = {
    'normalize': True,
    'sample_weight': None }, *, normalize, sample_weight: (xp, _) = get_namespace(y_true, y_pred)score = accuracy_score(y_true, y_pred, normalize = normalize, sample_weight = sample_weight)if normalize:
1 - score# WARNING: Decompyle incomplete
)()
f1_score = (lambda y_true = validate_params({
    'y_true': [
        'array-like',
        'sparse matrix'],
    'y_pred': [
        'array-like',
        'sparse matrix'],
    'labels': [
        'array-like',
        None],
    'pos_label': [
        Real,
        str,
        'boolean',
        None],
    'average': [
        StrOptions({
            'macro',
            'micro',
            'binary',
            'samples',
            'weighted'}),
        None],
    'sample_weight': [
        'array-like',
        None],
    'zero_division': [
        Options(Real, {
            0,
            1}),
        'nan',
        StrOptions({
            'warn'})] }, prefer_skip_nested_validation = True), y_pred = {
    'labels': None,
    'pos_label': 1,
    'average': 'binary',
    'sample_weight': None,
    'zero_division': 'warn' }, *, labels, pos_label: fbeta_score(y_true, y_pred, beta = 1, labels = labels, pos_label = pos_label, average = average, sample_weight = sample_weight, zero_division = zero_division))()
fbeta_score = (lambda y_true = validate_params({
    'y_true': [
        'array-like',
        'sparse matrix'],
    'y_pred': [
        'array-like',
        'sparse matrix'],
    'beta': [
        Interval(Real, 0, None, closed = 'both')],
    'labels': [
        'array-like',
        None],
    'pos_label': [
        Real,
        str,
        'boolean',
        None],
    'average': [
        StrOptions({
            'macro',
            'micro',
            'binary',
            'samples',
            'weighted'}),
        None],
    'sample_weight': [
        'array-like',
        None],
    'zero_division': [
        Options(Real, {
            0,
            1}),
        'nan',
        StrOptions({
            'warn'})] }, prefer_skip_nested_validation = True), y_pred = {
    'labels': None,
    'pos_label': 1,
    'average': 'binary',
    'sample_weight': None,
    'zero_division': 'warn' }, *, beta, labels: (_, _, f, _) = precision_recall_fscore_support(y_true, y_pred, beta = beta, labels = labels, pos_label = pos_label, average = average, warn_for = ('f-score',), sample_weight = sample_weight, zero_division = zero_division)f)()

def _prf_divide(numerator, denominator, metric, modifier, average, warn_for, zero_division = ('warn',)):
    '''Performs division and handles divide-by-zero.

    On zero-division, sets the corresponding result elements equal to
    0, 1 or np.nan (according to ``zero_division``). Plus, if
    ``zero_division != "warn"`` raises a warning.

    The metric, modifier and average arguments are used only for determining
    an appropriate warning.
    '''
    (xp, _) = get_namespace(numerator, denominator)
    dtype_float = _find_matching_floating_dtype(numerator, denominator, xp = xp)
    mask = denominator == 0
    denominator = xp.asarray(denominator, copy = True, dtype = dtype_float)
    denominator[mask] = 1
    result = xp.asarray(numerator, dtype = dtype_float) / denominator
    if not xp.any(mask):
        return result
    zero_division_value = None(zero_division)
    result[mask] = zero_division_value
    if zero_division != 'warn' or metric not in warn_for:
        return result
    if None in warn_for:
        _warn_prf(average, modifier, f'''{metric.capitalize()} is''', result.shape[0])
    return result


def _warn_prf(average, modifier, msg_start, result_size):
    (axis0, axis1) = ('sample', 'label')
    if average == 'samples':
        axis1 = axis0
        axis0 = axis1
    msg = '{0} ill-defined and being set to 0.0 {{0}} no {1} {2}s. Use `zero_division` parameter to control this behavior.'.format(msg_start, modifier, axis0)
    if result_size == 1:
        msg = msg.format('due to')
    else:
        msg = msg.format('in {0}s with'.format(axis1))
    warnings.warn(msg, UndefinedMetricWarning, stacklevel = 2)


def _check_set_wise_labels(y_true, y_pred, average, labels, pos_label):
    '''Validation associated with set-wise metrics.

    Returns identified labels.
    '''
    average_options = (None, 'micro', 'macro', 'weighted', 'samples')
    if average not in average_options and average != 'binary':
        raise ValueError('average has to be one of ' + str(average_options))
    (y_true, y_pred) = attach_unique(y_true, y_pred)
    (y_type, y_true, y_pred, _) = _check_targets(y_true, y_pred)
    present_labels = _tolist(unique_labels(y_true, y_pred))
    if average == 'binary':
        if y_type == 'binary':
            if pos_label not in present_labels and len(present_labels) >= 2:
                raise ValueError(f'''pos_label={pos_label} is not a valid label. It should be one of {present_labels}''')
            labels = [
                pos_label]
        else:
            average_options = list(average_options)
            if y_type == 'multiclass':
                average_options.remove('samples')
            raise ValueError(f'''Target is {y_type!s} but average=\'binary\'. Please choose another average setting, one of {average_options!r}.''')
    if pos_label not in (None, 1):
        warnings.warn(f'''Note that pos_label (set to {pos_label!r}) is ignored when average != \'binary\' (got {average!r}). You may use labels=[pos_label] to specify a single positive class.''', UserWarning)
    return labels

precision_recall_fscore_support = (lambda y_true = validate_params({
    'y_true': [
        'array-like',
        'sparse matrix'],
    'y_pred': [
        'array-like',
        'sparse matrix'],
    'beta': [
        Interval(Real, 0, None, closed = 'both')],
    'labels': [
        'array-like',
        None],
    'pos_label': [
        Real,
        str,
        'boolean',
        None],
    'average': [
        StrOptions({
            'macro',
            'micro',
            'binary',
            'samples',
            'weighted'}),
        None],
    'warn_for': [
        list,
        tuple,
        set],
    'sample_weight': [
        'array-like',
        None],
    'zero_division': [
        Options(Real, {
            0,
            1}),
        'nan',
        StrOptions({
            'warn'})] }, prefer_skip_nested_validation = True), y_pred = {
    'beta': 1,
    'labels': None,
    'pos_label': 1,
    'average': None,
    'warn_for': ('precision', 'recall', 'f-score'),
    'sample_weight': None,
    'zero_division': 'warn' }, *, beta, labels: _check_zero_division(zero_division)labels = _check_set_wise_labels(y_true, y_pred, average, labels, pos_label)samplewise = average == 'samples'MCM = multilabel_confusion_matrix(y_true, y_pred, sample_weight = sample_weight, labels = labels, samplewise = samplewise)tp_sum = MCM[(:, 1, 1)]pred_sum = tp_sum + MCM[(:, 0, 1)]true_sum = tp_sum + MCM[(:, 1, 0)](xp, _, device_) = get_namespace_and_device(y_true, y_pred)if average == 'micro':
tp_sum = xp.reshape(xp.sum(tp_sum), (1,))pred_sum = xp.reshape(xp.sum(pred_sum), (1,))true_sum = xp.reshape(xp.sum(true_sum), (1,))beta2 = beta ** 2precision = _prf_divide(tp_sum, pred_sum, 'precision', 'predicted', average, warn_for, zero_division)recall = _prf_divide(tp_sum, true_sum, 'recall', 'true', average, warn_for, zero_division)if np.isposinf(beta):
f_score = recallelif beta == 0:
f_score = precisionelse:
max_float_type = _max_precision_float_dtype(xp = xp, device = device_)denom = beta2 * xp.astype(true_sum, max_float_type) + xp.astype(pred_sum, max_float_type)f_score = _prf_divide((1 + beta2) * xp.astype(tp_sum, max_float_type), denom, 'f-score', 'true nor predicted', average, warn_for, zero_division)if average == 'weighted':
weights = true_sumelif average == 'samples':
weights = sample_weightelse:
weights = None# WARNING: Decompyle incomplete
)()
class_likelihood_ratios = (lambda y_true = validate_params({
    'y_true': [
        'array-like',
        'sparse matrix'],
    'y_pred': [
        'array-like',
        'sparse matrix'],
    'labels': [
        'array-like',
        None],
    'sample_weight': [
        'array-like',
        None],
    'raise_warning': [
        'boolean',
        Hidden(StrOptions({
            'deprecated'}))],
    'replace_undefined_by': [
        Options(Real, {
            1,
            np.nan}),
        dict] }, prefer_skip_nested_validation = True), y_pred = {
    'labels': None,
    'sample_weight': None,
    'raise_warning': 'deprecated',
    'replace_undefined_by': np.nan }, *, labels, sample_weight: (y_true, y_pred) = attach_unique(y_true, y_pred)(y_type, y_true, y_pred, sample_weight) = _check_targets(y_true, y_pred, sample_weight)if y_type != 'binary':
raise ValueError(f'''class_likelihood_ratios only supports binary classification problems, got targets of type: {y_type}''')msg_deprecated_param = '`raise_warning` was deprecated in version 1.7 and will be removed in 1.9. An `UndefinedMetricWarning` will always be raised in case of a division by zero and the value set with the `replace_undefined_by` param will be returned.'if raise_warning != 'deprecated':
warnings.warn(msg_deprecated_param, FutureWarning)else:
raise_warning = Trueif replace_undefined_by == 1:
replace_undefined_by = {
'LR+': 1,
'LR-': 1 }if isinstance(replace_undefined_by, dict):
msg = f'''The dictionary passed as `replace_undefined_by` needs to be in the form `{{\'LR+\': `value_1`, \'LR-\': `value_2`}}` where the value for `LR+` ranges from `1.0` to `np.inf` or is `np.nan` and the value for `LR-` ranges from `0.0` to `1.0` or is `np.nan`; got `{replace_undefined_by}`.'''if 'LR+' in replace_undefined_by and 'LR-' in replace_undefined_by:
try:
desired_lr_pos = replace_undefined_by.get('LR+', None)check_scalar(desired_lr_pos, 'positive_likelihood_ratio', target_type = Real, min_val = 1, include_boundaries = 'left')desired_lr_neg = replace_undefined_by.get('LR-', None)check_scalar(desired_lr_neg, 'negative_likelihood_ratio', target_type = Real, min_val = 0, max_val = 1, include_boundaries = 'both')except Exception:
e = Noneraise ValueError(msg), ee = Nonedel eraise ValueError(msg)cm = confusion_matrix(y_true, y_pred, sample_weight = sample_weight, labels = labels)(tn, fp, fn, tp) = cm.ravel()support_pos = tp + fnsupport_neg = tn + fppos_num = tp * support_negpos_denom = fp * support_posneg_num = fn * support_negneg_denom = tn * support_posif support_pos == 0:
msg = "No samples of the positive class are present in `y_true`. `positive_likelihood_ratio` and `negative_likelihood_ratio` are both set to `np.nan`. Use the `replace_undefined_by` param to control this behavior. To suppress this warning or turn it into an error, see Python's `warnings` module and `warnings.catch_warnings()`."warnings.warn(msg, UndefinedMetricWarning, stacklevel = 2)positive_likelihood_ratio = np.nannegative_likelihood_ratio = np.nanif fp == 0:
if raise_warning:
if tp == 0:
msg_beginning = 'No samples were predicted for the positive class and `positive_likelihood_ratio` is 'else:
msg_beginning = '`positive_likelihood_ratio` is ill-defined and 'msg_end = 'set to `np.nan`. Use the `replace_undefined_by` param to 'warnings.warn(msg_beginning + msg_end, UndefinedMetricWarning, stacklevel = 2)if isinstance(replace_undefined_by, float) and np.isnan(replace_undefined_by):
positive_likelihood_ratio = replace_undefined_byelse:
positive_likelihood_ratio = desired_lr_poselse:
positive_likelihood_ratio = pos_num / pos_denomif tn == 0:
if raise_warning:
msg = "`negative_likelihood_ratio` is ill-defined and set to `np.nan`. Use the `replace_undefined_by` param to control this behavior. To suppress this warning or turn it into an error, see Python's `warnings` module and `warnings.catch_warnings()`."warnings.warn(msg, UndefinedMetricWarning, stacklevel = 2)if isinstance(replace_undefined_by, float) and np.isnan(replace_undefined_by):
negative_likelihood_ratio = replace_undefined_byelse:
negative_likelihood_ratio = desired_lr_negelse:
negative_likelihood_ratio = neg_num / neg_denom(float(positive_likelihood_ratio), float(negative_likelihood_ratio)))()
precision_score = (lambda y_true = validate_params({
    'y_true': [
        'array-like',
        'sparse matrix'],
    'y_pred': [
        'array-like',
        'sparse matrix'],
    'labels': [
        'array-like',
        None],
    'pos_label': [
        Real,
        str,
        'boolean',
        None],
    'average': [
        StrOptions({
            'macro',
            'micro',
            'binary',
            'samples',
            'weighted'}),
        None],
    'sample_weight': [
        'array-like',
        None],
    'zero_division': [
        Options(Real, {
            0,
            1}),
        'nan',
        StrOptions({
            'warn'})] }, prefer_skip_nested_validation = True), y_pred = {
    'labels': None,
    'pos_label': 1,
    'average': 'binary',
    'sample_weight': None,
    'zero_division': 'warn' }, *, labels, pos_label: (p, _, _, _) = precision_recall_fscore_support(y_true, y_pred, labels = labels, pos_label = pos_label, average = average, warn_for = ('precision',), sample_weight = sample_weight, zero_division = zero_division)p)()
recall_score = (lambda y_true = validate_params({
    'y_true': [
        'array-like',
        'sparse matrix'],
    'y_pred': [
        'array-like',
        'sparse matrix'],
    'labels': [
        'array-like',
        None],
    'pos_label': [
        Real,
        str,
        'boolean',
        None],
    'average': [
        StrOptions({
            'macro',
            'micro',
            'binary',
            'samples',
            'weighted'}),
        None],
    'sample_weight': [
        'array-like',
        None],
    'zero_division': [
        Options(Real, {
            0,
            1}),
        'nan',
        StrOptions({
            'warn'})] }, prefer_skip_nested_validation = True), y_pred = {
    'labels': None,
    'pos_label': 1,
    'average': 'binary',
    'sample_weight': None,
    'zero_division': 'warn' }, *, labels, pos_label: (_, r, _, _) = precision_recall_fscore_support(y_true, y_pred, labels = labels, pos_label = pos_label, average = average, warn_for = ('recall',), sample_weight = sample_weight, zero_division = zero_division)r)()
balanced_accuracy_score = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_pred': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None],
    'adjusted': [
        'boolean'] }, prefer_skip_nested_validation = True), y_pred = {
    'sample_weight': None,
    'adjusted': False }, *, sample_weight, adjusted: C = confusion_matrix(y_true, y_pred, sample_weight = sample_weight)(xp, _, device_) = get_namespace_and_device(y_pred, y_true)if _is_xp_namespace(xp, 'array_api_strict'):
C = xp.astype(C, _max_precision_float_dtype(xp, device = device_), copy = False)context_manager = np.errstate(divide = 'ignore', invalid = 'ignore') if _is_numpy_namespace(xp) else nullcontext()context_managerper_class = xp.linalg.diagonal(C) / xp.sum(C, axis = 1)None(None, None))()
classification_report = (lambda y_true = validate_params({
    'y_true': [
        'array-like',
        'sparse matrix'],
    'y_pred': [
        'array-like',
        'sparse matrix'],
    'labels': [
        'array-like',
        None],
    'target_names': [
        'array-like',
        None],
    'sample_weight': [
        'array-like',
        None],
    'digits': [
        Interval(Integral, 0, None, closed = 'left')],
    'output_dict': [
        'boolean'],
    'zero_division': [
        Options(Real, {
            0,
            1}),
        'nan',
        StrOptions({
            'warn'})] }, prefer_skip_nested_validation = True), y_pred = {
    'labels': None,
    'target_names': None,
    'sample_weight': None,
    'digits': 2,
    'output_dict': False,
    'zero_division': 'warn' }, *, labels, target_names: (y_true, y_pred) = attach_unique(y_true, y_pred)(y_type, y_true, y_pred, sample_weight) = _check_targets(y_true, y_pred, sample_weight)# WARNING: Decompyle incomplete
)()
hamming_loss = (lambda y_true = validate_params({
    'y_true': [
        'array-like',
        'sparse matrix'],
    'y_pred': [
        'array-like',
        'sparse matrix'],
    'sample_weight': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), y_pred = {
    'sample_weight': None }, *, sample_weight, y_type = None: (y_true, y_pred) = attach_unique(y_true, y_pred)(y_type, y_true, y_pred, sample_weight) = _check_targets(y_true, y_pred, sample_weight)(xp, _, device) = get_namespace_and_device(y_true, y_pred, sample_weight)# WARNING: Decompyle incomplete
)()
log_loss = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_pred': [
        'array-like'],
    'normalize': [
        'boolean'],
    'sample_weight': [
        'array-like',
        None],
    'labels': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), y_pred = {
    'normalize': True,
    'sample_weight': None,
    'labels': None }, *, normalize, sample_weight: (xp, _, device_) = get_namespace_and_device(y_pred)y_pred = check_array(y_pred, ensure_2d = False, dtype = supported_float_dtypes(xp, device = device_))# WARNING: Decompyle incomplete
)()

def _log_loss(transformed_labels = None, y_pred = {
    'normalize': True,
    'sample_weight': None }, *, normalize, sample_weight):
    '''Log loss for transformed labels and validated probabilistic predictions.'''
    (xp, _, device_) = get_namespace_and_device(y_pred)
# WARNING: Decompyle incomplete

hinge_loss = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'pred_decision': [
        'array-like'],
    'labels': [
        'array-like',
        None],
    'sample_weight': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), pred_decision = {
    'labels': None,
    'sample_weight': None }, *, labels, sample_weight: check_consistent_length(y_true, pred_decision, sample_weight)pred_decision = check_array(pred_decision, ensure_2d = False)y_true = column_or_1d(y_true)# WARNING: Decompyle incomplete
)()

def _one_hot_encoding_binary_target(y_true, pos_label, target_xp, target_device):
    '''Convert binary `y_true` into a one-hot encoded array and also ensure that
    the encoded array is placed on the target API namespace and device.
    '''
    (xp_y_true, _) = get_namespace(y_true)
    y_true_pos = xp_y_true.asarray(y_true == pos_label, dtype = xp_y_true.int64)
    y_true_pos = target_xp.asarray(y_true_pos, device = target_device)
    return target_xp.stack((1 - y_true_pos, y_true_pos), axis = 1)


def _validate_binary_probabilistic_prediction(y_true, y_prob, sample_weight, pos_label):
    '''Convert y_true and y_prob in binary classification to shape (n_samples, 2)

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True labels.

    y_prob : array-like of shape (n_samples,)
        Probabilities of the positive class.

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    pos_label : int, float, bool or str, default=None
        Label of the positive class. If None, `pos_label` will be inferred
        in the following manner:

        * if `y_true` in {-1, 1} or {0, 1}, `pos_label` defaults to 1;
        * else if `y_true` contains string, an error will be raised and
          `pos_label` should be explicitly specified;
        * otherwise, `pos_label` defaults to the greater label,
          i.e. `np.unique(y_true)[-1]`.

    Returns
    -------
    transformed_labels : array of shape (n_samples, 2)

    y_prob : array of shape (n_samples, 2)
    '''
    y_true = column_or_1d(y_true)
    y_prob = column_or_1d(y_prob)
    assert_all_finite(y_true)
    assert_all_finite(y_prob)
    check_consistent_length(y_prob, y_true, sample_weight)
# WARNING: Decompyle incomplete

brier_score_loss = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_proba': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None],
    'pos_label': [
        Real,
        str,
        'boolean',
        None],
    'labels': [
        'array-like',
        None],
    'scale_by_half': [
        'boolean',
        StrOptions({
            'auto'})] }, prefer_skip_nested_validation = True), y_proba = {
    'sample_weight': None,
    'pos_label': None,
    'labels': None,
    'scale_by_half': 'auto' }, *, sample_weight, pos_label: (xp, _, device_) = get_namespace_and_device(y_proba)y_proba = check_array(y_proba, ensure_2d = False, dtype = supported_float_dtypes(xp, device = device_))# WARNING: Decompyle incomplete
)()
d2_log_loss_score = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_pred': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None],
    'labels': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), y_pred = {
    'sample_weight': None,
    'labels': None }, *, sample_weight, labels: check_consistent_length(y_pred, y_true, sample_weight)if _num_samples(y_pred) < 2:
msg = 'D^2 score is not well-defined with less than two samples.'warnings.warn(msg, UndefinedMetricWarning)float('nan')(xp, _, device_) = None(y_pred)y_pred = check_array(y_pred, ensure_2d = False, dtype = supported_float_dtypes(xp, device = device_))# WARNING: Decompyle incomplete
)()
d2_brier_score = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_proba': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None],
    'pos_label': [
        Real,
        str,
        'boolean',
        None],
    'labels': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), y_proba = {
    'sample_weight': None,
    'pos_label': None,
    'labels': None }, *, sample_weight, pos_label: check_consistent_length(y_proba, y_true, sample_weight)if _num_samples(y_proba) < 2:
msg = 'D^2 score is not well-defined with less than two samples.'warnings.warn(msg, UndefinedMetricWarning)float('nan')(xp, _, device_) = None(y_proba)y_proba = check_array(y_proba, ensure_2d = False, dtype = supported_float_dtypes(xp, device = device_))# WARNING: Decompyle incomplete
)()
