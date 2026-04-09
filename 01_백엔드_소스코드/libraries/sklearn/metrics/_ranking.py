# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _ranking.pyc (Python 3.11)

'''Metrics to assess performance on classification task given scores.

Functions named as ``*_score`` return a scalar value to maximize: the higher
the better.

Function named as ``*_error`` or ``*_loss`` return a scalar value to minimize:
the lower the better.
'''
import warnings
from functools import partial
from numbers import Integral, Real
import numpy as np
from scipy.integrate import trapezoid
from scipy.sparse import csr_matrix, issparse
from scipy.stats import rankdata
from sklearn.exceptions import UndefinedMetricWarning
from sklearn.metrics._base import _average_binary_score, _average_multiclass_ovo_score
from sklearn.preprocessing import label_binarize
from sklearn.utils import assert_all_finite, check_array, check_consistent_length, column_or_1d
from sklearn.utils._array_api import _max_precision_float_dtype, get_namespace_and_device, size
from sklearn.utils._encode import _encode, _unique
from sklearn.utils._param_validation import Interval, StrOptions, validate_params
from sklearn.utils.multiclass import type_of_target
from sklearn.utils.sparsefuncs import count_nonzero
from sklearn.utils.validation import _check_pos_label_consistency, _check_sample_weight
auc = (lambda x, y: check_consistent_length(x, y)x = column_or_1d(x)y = column_or_1d(y)if x.shape[0] < 2:
raise ValueError('At least 2 points are needed to compute area under curve, but x.shape = %s' % x.shape)direction = 1dx = np.diff(x)if np.any(dx < 0):
if np.all(dx <= 0):
direction = -1else:
raise ValueError('x is neither increasing nor decreasing : {}.'.format(x))area = direction * trapezoid(y, x)if isinstance(area, np.memmap):
area = area.dtype.type(area)float(area))()
average_precision_score = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_score': [
        'array-like'],
    'average': [
        StrOptions({
            'macro',
            'micro',
            'samples',
            'weighted'}),
        None],
    'pos_label': [
        Real,
        str,
        'boolean'],
    'sample_weight': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), y_score = {
    'average': 'macro',
    'pos_label': 1,
    'sample_weight': None }, *, average, pos_label: 
def _binary_uninterpolated_average_precision(y_true, y_score, pos_label, sample_weight = (1, None)):
(precision, recall, _) = precision_recall_curve(y_true, y_score, pos_label = pos_label, sample_weight = sample_weight)float(max(0, -np.sum(np.diff(recall) * np.array(precision)[:-1])))y_type = type_of_target(y_true, input_name = 'y_true')present_labels = np.unique(y_true).tolist()if y_type == 'binary':
if len(present_labels) == 2 and pos_label not in present_labels:
raise ValueError(f'''pos_label={pos_label} is not a valid label. It should be one of {present_labels}''')elif y_type == 'multilabel-indicator' and pos_label != 1:
raise ValueError('Parameter pos_label is fixed to 1 for multilabel-indicator y_true. Do not set pos_label or set pos_label to 1.')if y_type == 'multiclass':
if pos_label != 1:
raise ValueError('Parameter pos_label is fixed to 1 for multiclass y_true. Do not set pos_label or set pos_label to 1.')y_true = label_binarize(y_true, classes = present_labels)average_precision = partial(_binary_uninterpolated_average_precision, pos_label = pos_label)_average_binary_score(average_precision, y_true, y_score, average, sample_weight = sample_weight))()
det_curve = (lambda y_true, y_score, pos_label, sample_weight, drop_intermediate = (None, None, False): (xp, _, device) = get_namespace_and_device(y_true, y_score)(_, fps, _, tps, thresholds) = confusion_matrix_at_thresholds(y_true, y_score, pos_label = pos_label, sample_weight = sample_weight)tps = xp.concat((xp.asarray([
0], device = device), tps))fps = xp.concat((xp.asarray([
0], device = device), fps))thresholds = xp.astype(thresholds, _max_precision_float_dtype(xp, device))thresholds = xp.concat((xp.asarray([
xp.inf], device = device), thresholds))if drop_intermediate and len(fps) > 2:
optimal_idxs = xp.where(xp.concat([
xp.asarray([
True], device = device),
xp.logical_or(xp.diff(tps[:-1]), xp.diff(tps[1:])),
xp.asarray([
True], device = device)]))[0]fps = fps[optimal_idxs]tps = tps[optimal_idxs]thresholds = thresholds[optimal_idxs]if xp.unique_values(y_true).shape[0] != 2:
raise ValueError('Only one class is present in y_true. Detection error tradeoff curve is not defined in that case.')fns = tps[-1] - tpsp_count = tps[-1]n_count = fps[-1]first_ind = xp.searchsorted(fps, fps[0], side = 'right') - 1 if xp.searchsorted(fps, fps[0], side = 'right') > 0 else Nonelast_ind = xp.searchsorted(tps, tps[-1]) + 1sl = slice(first_ind, last_ind)(xp.flip(fps[sl]) / n_count, xp.flip(fns[sl]) / p_count, xp.flip(thresholds[sl])))()

def _binary_roc_auc_score(y_true, y_score, sample_weight, max_fpr = (None, None)):
    '''Binary roc auc score.'''
    if len(np.unique(y_true)) != 2:
        warnings.warn('Only one class is present in y_true. ROC AUC score is not defined in that case.', UndefinedMetricWarning)
        return np.nan
    (fpr, tpr, _) = None(y_true, y_score, sample_weight = sample_weight)
# WARNING: Decompyle incomplete

roc_auc_score = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_score': [
        'array-like'],
    'average': [
        StrOptions({
            'macro',
            'micro',
            'samples',
            'weighted'}),
        None],
    'sample_weight': [
        'array-like',
        None],
    'max_fpr': [
        Interval(Real, 0, 1, closed = 'right'),
        None],
    'multi_class': [
        StrOptions({
            'ovo',
            'ovr',
            'raise'})],
    'labels': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), y_score = {
    'average': 'macro',
    'sample_weight': None,
    'max_fpr': None,
    'multi_class': 'raise',
    'labels': None }, *, average, sample_weight: y_type = type_of_target(y_true, input_name = 'y_true')y_true = check_array(y_true, ensure_2d = False, dtype = None)y_score = check_array(y_score, ensure_2d = False)# WARNING: Decompyle incomplete
)()

def _multiclass_roc_auc_score(y_true, y_score, labels, multi_class, average, sample_weight):
    """Multiclass roc auc score.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True multiclass labels.

    y_score : array-like of shape (n_samples, n_classes)
        Target scores corresponding to probability estimates of a sample
        belonging to a particular class

    labels : array-like of shape (n_classes,) or None
        List of labels to index ``y_score`` used for multiclass. If ``None``,
        the lexical order of ``y_true`` is used to index ``y_score``.

    multi_class : {'ovr', 'ovo'}
        Determines the type of multiclass configuration to use.
        ``'ovr'``:
            Calculate metrics for the multiclass case using the one-vs-rest
            approach.
        ``'ovo'``:
            Calculate metrics for the multiclass case using the one-vs-one
            approach.

    average : {'micro', 'macro', 'weighted'}
        Determines the type of averaging performed on the pairwise binary
        metric scores
        ``'micro'``:
            Calculate metrics for the binarized-raveled classes. Only supported
            for `multi_class='ovr'`.

        .. versionadded:: 1.2

        ``'macro'``:
            Calculate metrics for each label, and find their unweighted
            mean. This does not take label imbalance into account. Classes
            are assumed to be uniformly distributed.
        ``'weighted'``:
            Calculate metrics for each label, taking into account the
            prevalence of the classes.

    sample_weight : array-like of shape (n_samples,) or None
        Sample weights.

    """
    if not np.allclose(1, y_score.sum(axis = 1)):
        raise ValueError('Target scores need to be probabilities for multiclass roc_auc, i.e. they should sum up to 1.0 over classes')
    average_options = ('macro', 'weighted', None)
    if multi_class == 'ovr':
        average_options = ('micro',) + average_options
    if average not in average_options:
        raise ValueError('average must be one of {0} for multiclass problems'.format(average_options))
    multiclass_options = ('ovo', 'ovr')
    if multi_class not in multiclass_options:
        raise ValueError("multi_class='{0}' is not supported for multiclass ROC AUC, multi_class must be in {1}".format(multi_class, multiclass_options))
# WARNING: Decompyle incomplete

confusion_matrix_at_thresholds = (lambda y_true, y_score, pos_label, sample_weight = (None, None): y_type = type_of_target(y_true, input_name = 'y_true')# WARNING: Decompyle incomplete
)()
precision_recall_curve = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_score': [
        'array-like'],
    'pos_label': [
        Real,
        str,
        'boolean',
        None],
    'sample_weight': [
        'array-like',
        None],
    'drop_intermediate': [
        'boolean'] }, prefer_skip_nested_validation = True), y_score = {
    'pos_label': None,
    'sample_weight': None,
    'drop_intermediate': False }, *, pos_label, sample_weight: (xp, _, device) = get_namespace_and_device(y_true, y_score)(_, fps, _, tps, thresholds) = confusion_matrix_at_thresholds(y_true, y_score, pos_label = pos_label, sample_weight = sample_weight)if drop_intermediate and fps.shape[0] > 2:
optimal_idxs = xp.where(xp.concat([
xp.asarray([
True], device = device),
xp.logical_or(xp.diff(tps[:-1]), xp.diff(tps[1:])),
xp.asarray([
True], device = device)]))[0]fps = fps[optimal_idxs]tps = tps[optimal_idxs]thresholds = thresholds[optimal_idxs]ps = tps + fpsprecision = xp.where(ps != 0, xp.divide(tps, ps), 0)if tps[-1] == 0:
warnings.warn('No positive class found in y_true, recall is set to one for all thresholds.')recall = xp.full(tps.shape, 1)else:
recall = tps / tps[-1](xp.concat((xp.flip(precision), xp.asarray([
1], device = device))), xp.concat((xp.flip(recall), xp.asarray([
0], device = device))), xp.flip(thresholds)))()
roc_curve = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_score': [
        'array-like'],
    'pos_label': [
        Real,
        str,
        'boolean',
        None],
    'sample_weight': [
        'array-like',
        None],
    'drop_intermediate': [
        'boolean'] }, prefer_skip_nested_validation = True), y_score = {
    'pos_label': None,
    'sample_weight': None,
    'drop_intermediate': True }, *, pos_label, sample_weight: (xp, _, device) = get_namespace_and_device(y_true, y_score)(_, fps, _, tps, thresholds) = confusion_matrix_at_thresholds(y_true, y_score, pos_label = pos_label, sample_weight = sample_weight)if drop_intermediate and fps.shape[0] > 2:
optimal_idxs = xp.where(xp.concat([
xp.asarray([
True], device = device),
xp.logical_or(xp.diff(fps, 2), xp.diff(tps, 2)),
xp.asarray([
True], device = device)]))[0]fps = fps[optimal_idxs]tps = tps[optimal_idxs]thresholds = thresholds[optimal_idxs]tps = xp.concat([
xp.asarray([
0], device = device),
tps])fps = xp.concat([
xp.asarray([
0], device = device),
fps])thresholds = xp.astype(thresholds, _max_precision_float_dtype(xp, device))thresholds = xp.concat([
xp.asarray([
xp.inf], device = device),
thresholds])if fps[-1] <= 0:
warnings.warn('No negative samples in y_true, false positive value should be meaningless', UndefinedMetricWarning)fpr = xp.full(fps.shape, xp.nan)else:
fpr = fps / fps[-1]if tps[-1] <= 0:
warnings.warn('No positive samples in y_true, true positive value should be meaningless', UndefinedMetricWarning)tpr = xp.full(tps.shape, xp.nan)else:
tpr = tps / tps[-1](fpr, tpr, thresholds))()
label_ranking_average_precision_score = (lambda y_true = validate_params({
    'y_true': [
        'array-like',
        'sparse matrix'],
    'y_score': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), y_score = {
    'sample_weight': None }, *, sample_weight, y_type = None: check_consistent_length(y_true, y_score, sample_weight)y_true = check_array(y_true, ensure_2d = False, accept_sparse = 'csr')y_score = check_array(y_score, ensure_2d = False)if y_true.shape != y_score.shape:
raise ValueError('y_true and y_score have different shape')y_type = type_of_target(y_true, input_name = 'y_true')if y_type != 'multilabel-indicator':
if not y_type == 'binary' or y_true.ndim == 2:
raise ValueError('{0} format is not supported'.format(y_type))if not issparse(y_true):
y_true = csr_matrix(y_true)y_score = -y_score(n_samples, n_labels) = y_true.shapeout = 0# WARNING: Decompyle incomplete
)()
coverage_error = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_score': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), y_score = {
    'sample_weight': None }, *, sample_weight, y_type = None: y_true = check_array(y_true, ensure_2d = True)y_score = check_array(y_score, ensure_2d = True)check_consistent_length(y_true, y_score, sample_weight)y_type = type_of_target(y_true, input_name = 'y_true')if y_type != 'multilabel-indicator':
raise ValueError('{0} format is not supported'.format(y_type))if y_true.shape != y_score.shape:
raise ValueError('y_true and y_score have different shape')y_score_mask = np.ma.masked_array(y_score, mask = np.logical_not(y_true))y_min_relevant = y_score_mask.min(axis = 1).reshape((-1, 1))coverage = (y_score >= y_min_relevant).sum(axis = 1)coverage = coverage.filled(0)float(np.average(coverage, weights = sample_weight)))()
label_ranking_loss = (lambda y_true = validate_params({
    'y_true': [
        'array-like',
        'sparse matrix'],
    'y_score': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), y_score = {
    'sample_weight': None }, *, sample_weight, y_type = None: y_true = check_array(y_true, ensure_2d = False, accept_sparse = 'csr')y_score = check_array(y_score, ensure_2d = False)check_consistent_length(y_true, y_score, sample_weight)y_type = type_of_target(y_true, input_name = 'y_true')if y_type not in ('multilabel-indicator',):
raise ValueError('{0} format is not supported'.format(y_type))if y_true.shape != y_score.shape:
raise ValueError('y_true and y_score have different shape')(n_samples, n_labels) = y_true.shapey_true = csr_matrix(y_true)loss = np.zeros(n_samples)for start, stop in enumerate(zip(y_true.indptr, y_true.indptr[1:])):
(unique_scores, unique_inverse) = np.unique(y_score[i], return_inverse = True)true_at_reversed_rank = np.bincount(unique_inverse[y_true.indices[start:stop]], minlength = len(unique_scores))all_at_reversed_rank = np.bincount(unique_inverse, minlength = len(unique_scores))false_at_reversed_rank = all_at_reversed_rank - true_at_reversed_rankloss[i] = np.dot(true_at_reversed_rank.cumsum(), false_at_reversed_rank)n_positives = count_nonzero(y_true, axis = 1)np.errstate(divide = 'ignore', invalid = 'ignore')loss /= (n_labels - n_positives) * n_positivesNone(None, None)with None:
if not None:
passloss[np.logical_or(n_positives == 0, n_positives == n_labels)] = 0float(np.average(loss, weights = sample_weight)))()

def _dcg_sample_scores(y_true, y_score, k, log_base, ignore_ties = (None, 2, False)):
    '''Compute Discounted Cumulative Gain.

    Sum the true scores ranked in the order induced by the predicted scores,
    after applying a logarithmic discount.

    This ranking metric yields a high value if true labels are ranked high by
    ``y_score``.

    Parameters
    ----------
    y_true : ndarray of shape (n_samples, n_labels)
        True targets of multilabel classification, or true scores of entities
        to be ranked.

    y_score : ndarray of shape (n_samples, n_labels)
        Target scores, can either be probability estimates, confidence values,
        or non-thresholded measure of decisions (as returned by
        "decision_function" on some classifiers).

    k : int, default=None
        Only consider the highest k scores in the ranking. If `None`, use all
        outputs.

    log_base : float, default=2
        Base of the logarithm used for the discount. A low value means a
        sharper discount (top results are more important).

    ignore_ties : bool, default=False
        Assume that there are no ties in y_score (which is likely to be the
        case if y_score is continuous) for efficiency gains.

    Returns
    -------
    discounted_cumulative_gain : ndarray of shape (n_samples,)
        The DCG score for each sample.

    See Also
    --------
    ndcg_score : The Discounted Cumulative Gain divided by the Ideal Discounted
        Cumulative Gain (the DCG obtained for a perfect ranking), in order to
        have a score between 0 and 1.
    '''
    pass
# WARNING: Decompyle incomplete


def _tie_averaged_dcg(y_true, y_score, discount_cumsum):
    '''
    Compute DCG by averaging over possible permutations of ties.

    The gain (`y_true`) of an index falling inside a tied group (in the order
    induced by `y_score`) is replaced by the average gain within this group.
    The discounted gain for a tied group is then the average `y_true` within
    this group times the sum of discounts of the corresponding ranks.

    This amounts to averaging scores for all possible orderings of the tied
    groups.

    (note in the case of dcg@k the discount is 0 after index k)

    Parameters
    ----------
    y_true : ndarray
        The true relevance scores.

    y_score : ndarray
        Predicted scores.

    discount_cumsum : ndarray
        Precomputed cumulative sum of the discounts.

    Returns
    -------
    discounted_cumulative_gain : float
        The discounted cumulative gain.

    References
    ----------
    McSherry, F., & Najork, M. (2008, March). Computing information retrieval
    performance measures efficiently in the presence of tied scores. In
    European conference on information retrieval (pp. 414-421). Springer,
    Berlin, Heidelberg.
    '''
    (_, inv, counts) = np.unique(-y_score, return_inverse = True, return_counts = True)
    ranked = np.zeros(len(counts))
    np.add.at(ranked, inv, y_true)
    ranked /= counts
    groups = np.cumsum(counts) - 1
    discount_sums = np.empty(len(counts))
    discount_sums[0] = discount_cumsum[groups[0]]
    discount_sums[1:] = np.diff(discount_cumsum[groups])
    return (ranked * discount_sums).sum()


def _check_dcg_target_type(y_true):
    y_type = type_of_target(y_true, input_name = 'y_true')
    supported_fmt = ('multilabel-indicator', 'continuous-multioutput', 'multiclass-multioutput')
    if y_type not in supported_fmt:
        raise ValueError('Only {} formats are supported. Got {} instead'.format(supported_fmt, y_type))

dcg_score = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_score': [
        'array-like'],
    'k': [
        Interval(Integral, 1, None, closed = 'left'),
        None],
    'log_base': [
        Interval(Real, 0, None, closed = 'neither')],
    'sample_weight': [
        'array-like',
        None],
    'ignore_ties': [
        'boolean'] }, prefer_skip_nested_validation = True), y_score = {
    'k': None,
    'log_base': 2,
    'sample_weight': None,
    'ignore_ties': False }, *, k, log_base: y_true = check_array(y_true, ensure_2d = False)y_score = check_array(y_score, ensure_2d = False)check_consistent_length(y_true, y_score, sample_weight)_check_dcg_target_type(y_true)float(np.average(_dcg_sample_scores(y_true, y_score, k = k, log_base = log_base, ignore_ties = ignore_ties), weights = sample_weight)))()

def _ndcg_sample_scores(y_true, y_score, k, ignore_ties = (None, False)):
    '''Compute Normalized Discounted Cumulative Gain.

    Sum the true scores ranked in the order induced by the predicted scores,
    after applying a logarithmic discount. Then divide by the best possible
    score (Ideal DCG, obtained for a perfect ranking) to obtain a score between
    0 and 1.

    This ranking metric yields a high value if true labels are ranked high by
    ``y_score``.

    Parameters
    ----------
    y_true : ndarray of shape (n_samples, n_labels)
        True targets of multilabel classification, or true scores of entities
        to be ranked.

    y_score : ndarray of shape (n_samples, n_labels)
        Target scores, can either be probability estimates, confidence values,
        or non-thresholded measure of decisions (as returned by
        "decision_function" on some classifiers).

    k : int, default=None
        Only consider the highest k scores in the ranking. If None, use all
        outputs.

    ignore_ties : bool, default=False
        Assume that there are no ties in y_score (which is likely to be the
        case if y_score is continuous) for efficiency gains.

    Returns
    -------
    normalized_discounted_cumulative_gain : ndarray of shape (n_samples,)
        The NDCG score for each sample (float in [0., 1.]).

    See Also
    --------
    dcg_score : Discounted Cumulative Gain (not normalized).

    '''
    gain = _dcg_sample_scores(y_true, y_score, k, ignore_ties = ignore_ties)
    normalizing_gain = _dcg_sample_scores(y_true, y_true, k, ignore_ties = True)
    all_irrelevant = normalizing_gain == 0
    gain[all_irrelevant] = 0
    return gain

ndcg_score = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_score': [
        'array-like'],
    'k': [
        Interval(Integral, 1, None, closed = 'left'),
        None],
    'sample_weight': [
        'array-like',
        None],
    'ignore_ties': [
        'boolean'] }, prefer_skip_nested_validation = True), y_score = {
    'k': None,
    'sample_weight': None,
    'ignore_ties': False }, *, k, sample_weight: y_true = check_array(y_true, ensure_2d = False)y_score = check_array(y_score, ensure_2d = False)check_consistent_length(y_true, y_score, sample_weight)if y_true.min() < 0:
raise ValueError('ndcg_score should not be used on negative y_true values.')if y_true.ndim > 1 and y_true.shape[1] <= 1:
raise ValueError(f'''Computing NDCG is only meaningful when there is more than 1 document. Got {y_true.shape[1]} instead.''')_check_dcg_target_type(y_true)gain = _ndcg_sample_scores(y_true, y_score, k = k, ignore_ties = ignore_ties)float(np.average(gain, weights = sample_weight)))()
top_k_accuracy_score = (lambda y_true = validate_params({
    'y_true': [
        'array-like'],
    'y_score': [
        'array-like'],
    'k': [
        Interval(Integral, 1, None, closed = 'left')],
    'normalize': [
        'boolean'],
    'sample_weight': [
        'array-like',
        None],
    'labels': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), y_score = {
    'k': 2,
    'normalize': True,
    'sample_weight': None,
    'labels': None }, *, k, normalize: y_true = check_array(y_true, ensure_2d = False, dtype = None)y_true = column_or_1d(y_true)y_type = type_of_target(y_true, input_name = 'y_true')# WARNING: Decompyle incomplete
)()
