# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _supervised.pyc (Python 3.11)

'''Utilities to evaluate the clustering performance of models.

Functions named as *_score return a scalar value to maximize: the higher the
better.
'''
import warnings
from math import log
from numbers import Real
import numpy as np
from scipy import sparse as sp
from sklearn.metrics.cluster._expected_mutual_info_fast import expected_mutual_information
from sklearn.utils import deprecated
from sklearn.utils._array_api import _max_precision_float_dtype, get_namespace_and_device
from sklearn.utils._param_validation import Hidden, Interval, StrOptions, validate_params
from sklearn.utils.multiclass import type_of_target
from sklearn.utils.validation import check_array, check_consistent_length

def check_clusterings(labels_true, labels_pred):
    '''Check that the labels arrays are 1D and of same dimension.

    Parameters
    ----------
    labels_true : array-like of shape (n_samples,)
        The true labels.

    labels_pred : array-like of shape (n_samples,)
        The predicted labels.
    '''
    labels_true = check_array(labels_true, ensure_2d = False, ensure_min_samples = 0, dtype = None)
    labels_pred = check_array(labels_pred, ensure_2d = False, ensure_min_samples = 0, dtype = None)
    type_label = type_of_target(labels_true)
    type_pred = type_of_target(labels_pred)
    if 'continuous' in (type_pred, type_label):
        msg = f'''Clustering metrics expects discrete values but received {type_label} values for label, and {type_pred} values for target'''
        warnings.warn(msg, UserWarning)
    if labels_true.ndim != 1:
        raise ValueError(f'''labels_true must be 1D: shape is {labels_true.shape!r}''')
    if labels_pred.ndim != 1:
        raise ValueError(f'''labels_pred must be 1D: shape is {labels_pred.shape!r}''')
    check_consistent_length(labels_true, labels_pred)
    return (labels_true, labels_pred)


def _generalized_average(U, V, average_method):
    '''Return a particular mean of two numbers.'''
    if average_method == 'min':
        return min(U, V)
    if None == 'geometric':
        return np.sqrt(U * V)
    if None == 'arithmetic':
        return np.mean([
            U,
            V])
    if None == 'max':
        return max(U, V)
    raise None("'average_method' must be 'min', 'geometric', 'arithmetic', or 'max'")

contingency_matrix = (lambda labels_true = validate_params({
    'labels_true': [
        'array-like',
        None],
    'labels_pred': [
        'array-like',
        None],
    'eps': [
        Interval(Real, 0, None, closed = 'left'),
        None],
    'sparse': [
        'boolean'],
    'dtype': 'no_validation' }, prefer_skip_nested_validation = True), labels_pred = {
    'eps': None,
    'sparse': False,
    'dtype': np.int64 }, *, eps, sparse: pass# WARNING: Decompyle incomplete
)()
pair_confusion_matrix = (lambda labels_true, labels_pred: (labels_true, labels_pred) = check_clusterings(labels_true, labels_pred)n_samples = np.int64(labels_true.shape[0])contingency = contingency_matrix(labels_true, labels_pred, sparse = True, dtype = np.int64)n_c = np.ravel(contingency.sum(axis = 1))n_k = np.ravel(contingency.sum(axis = 0))sum_squares = (contingency.data ** 2).sum()C = np.empty((2, 2), dtype = np.int64)C[(1, 1)] = sum_squares - n_samplesC[(0, 1)] = contingency.dot(n_k).sum() - sum_squaresC[(1, 0)] = contingency.transpose().dot(n_c).sum() - sum_squaresC[(0, 0)] = n_samples ** 2 - C[(0, 1)] - C[(1, 0)] - sum_squaresC)()
rand_score = (lambda labels_true, labels_pred: contingency = pair_confusion_matrix(labels_true, labels_pred)numerator = contingency.diagonal().sum()denominator = contingency.sum()if numerator == denominator or denominator == 0:
1None(numerator / denominator))()
adjusted_rand_score = (lambda labels_true, labels_pred: (tn, fp) = ()(fn, tp) = pair_confusion_matrix(labels_true, labels_pred)(tn, fp, fn, tp) = (int(tn), int(fp), int(fn), int(tp))if fn == 0 and fp == 0:
1None * (tp * tn - fn * fp) / ((tp + fn) * (fn + tn) + (tp + fp) * (fp + tn)))()
homogeneity_completeness_v_measure = (lambda labels_true = validate_params({
    'labels_true': [
        'array-like'],
    'labels_pred': [
        'array-like'],
    'beta': [
        Interval(Real, 0, None, closed = 'left')] }, prefer_skip_nested_validation = True), labels_pred = {
    'beta': 1 }, *, beta, entropy_C = None: (labels_true, labels_pred) = check_clusterings(labels_true, labels_pred)if len(labels_true) == 0:
(1, 1, 1)entropy_C = None(labels_true)entropy_K = _entropy(labels_pred)contingency = contingency_matrix(labels_true, labels_pred, sparse = True)MI = mutual_info_score(None, None, contingency = contingency)homogeneity = MI / entropy_C if entropy_C else 1completeness = MI / entropy_K if entropy_K else 1if homogeneity + completeness == 0:
v_measure_score = 0else:
v_measure_score = (1 + beta) * homogeneity * completeness / (beta * homogeneity + completeness)(float(homogeneity), float(completeness), float(v_measure_score)))()
homogeneity_score = (lambda labels_true, labels_pred: homogeneity_completeness_v_measure(labels_true, labels_pred)[0])()
completeness_score = (lambda labels_true, labels_pred: homogeneity_completeness_v_measure(labels_true, labels_pred)[1])()
v_measure_score = (lambda labels_true = validate_params({
    'labels_true': [
        'array-like'],
    'labels_pred': [
        'array-like'],
    'beta': [
        Interval(Real, 0, None, closed = 'left')] }, prefer_skip_nested_validation = True), labels_pred = {
    'beta': 1 }, *, beta,
