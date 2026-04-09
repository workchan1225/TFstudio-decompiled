# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _validation.pyc (Python 3.11)

__doc__ = '\nThe :mod:`sklearn.model_selection._validation` module includes classes and\nfunctions to validate the model.\n'
import numbers
import time
import warnings
from collections import Counter
from contextlib import suppress
from functools import partial
from numbers import Real
from traceback import format_exc
import numpy as np
from scipy.sparse import sparse as sp
from joblib import logger
from sklearn.base import clone, is_classifier
from sklearn.exceptions import FitFailedWarning, UnsetMetadataPassedError
from sklearn.metrics import check_scoring, get_scorer_names
from sklearn.metrics._scorer import _MultimetricScorer
from sklearn.model_selection._split import check_cv
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import Bunch, _safe_indexing, check_random_state, indexable
from sklearn.utils._array_api import _convert_to_numpy, device, get_namespace, get_namespace_and_device, move_to
from sklearn.utils._param_validation import HasMethods, Integral, Interval, StrOptions, validate_params
from sklearn.utils.metadata_routing import MetadataRouter, MethodMapping, _routing_enabled, process_routing
from sklearn.utils.metaestimators import _safe_split
from sklearn.utils.parallel import Parallel, delayed
from sklearn.utils.validation import _check_method_params, _num_samples
__all__ = [
    'cross_val_predict',
    'cross_val_score',
    'cross_validate',
    'learning_curve',
    'permutation_test_score',
    'validation_curve']

def _check_groups_routing_disabled(groups):
    pass
# WARNING: Decompyle incomplete

cross_validate = (lambda estimator = validate_params({
    'estimator': [
        HasMethods('fit')],
    'X': [
        'array-like',
        'sparse matrix'],
    'y': [
        'array-like',
        None],
    'groups': [
        'array-like',
        None],
    'scoring': [
        StrOptions(set(get_scorer_names())),
        callable,
        list,
        tuple,
        dict,
        None],
    'cv': [
        'cv_object'],
    'n_jobs': [
        Integral,
        None],
    'verbose': [
        'verbose'],
    'params': [
        dict,
        None],
    'pre_dispatch': [
        Integral,
        str],
    'return_train_score': [
        'boolean'],
    'return_estimator': [
        'boolean'],
    'return_indices': [
        'boolean'],
    'error_score': [
        StrOptions({
            'raise'}),
        Real] }, prefer_skip_nested_validation = False), X = (None,), y = {
    'groups': None,
    'scoring': None,
    'cv': None,
    'n_jobs': None,
    'verbose': 0,
    'params': None,
    'pre_dispatch': '2*n_jobs',
    'return_train_score': False,
    'return_estimator': False,
    'return_indices': False,
    'error_score': np.nan }, *, groups, scoring, cv: pass# WARNING: Decompyle incomplete
)()

def _insert_error_scores(results, error_score):
    '''Insert error in `results` by replacing them inplace with `error_score`.

    This only applies to multimetric scores because `_fit_and_score` will
    handle the single metric case.
    '''
    pass
# WARNING: Decompyle incomplete


def _normalize_score_results(scores, scaler_score_key = ('score',)):
    '''Creates a scoring dictionary based on the type of `scores`'''
    if isinstance(scores[0], dict):
        return _aggregate_score_dicts(scores)
    return {
        None: scores }


def _warn_or_raise_about_fit_failures(results, error_score):
    pass
# WARNING: Decompyle incomplete

cross_val_score = (lambda estimator = validate_params({
    'estimator': [
        HasMethods('fit')],
    'X': [
        'array-like',
        'sparse matrix'],
    'y': [
        'array-like',
        None],
    'groups': [
        'array-like',
        None],
    'scoring': [
        StrOptions(set(get_scorer_names())),
        callable,
        None],
    'cv': [
        'cv_object'],
    'n_jobs': [
        Integral,
        None],
    'verbose': [
        'verbose'],
    'params': [
        dict,
        None],
    'pre_dispatch': [
        Integral,
        str,
        None],
    'error_score': [
        StrOptions({
            'raise'}),
        Real] }, prefer_skip_nested_validation = False), X = (None,), y = {
    'groups': None,
    'scoring': None,
    'cv': None,
    'n_jobs': None,
    'verbose': 0,
    'params': None,
    'pre_dispatch': '2*n_jobs',
    'error_score': np.nan }, *, groups, scoring, cv: scorer = check_scoring(estimator, scoring = scoring)cv_results = cross_validate(estimator = estimator, X = X, y = y, groups = groups, scoring = {
'score': scorer }, cv = cv, n_jobs = n_jobs, verbose = verbose, params = params, pre_dispatch = pre_dispatch, error_score = error_score)cv_results['test_score'])()

def _fit_and_score(estimator, X = None, y = {
    'return_train_score': False,
    'return_parameters': False,
    'return_n_test_samples': False,
    'return_times': False,
    'return_estimator': False,
    'split_progress': None,
    'candidate_progress': None,
    'error_score': np.nan }, *, scorer, train, test, verbose, parameters, fit_params, score_params, return_train_score, return_parameters, return_n_test_samples, return_times, return_estimator, split_progress, candidate_progress, error_score):
    """Fit estimator and compute scores for a given dataset split.

    Parameters
    ----------
    estimator : estimator object implementing 'fit'
        The object to use to fit the data.

    X : array-like of shape (n_samples, n_features)
        The data to fit.

    y : array-like of shape (n_samples,) or (n_samples, n_outputs) or None
        The target variable to try to predict in the case of
        supervised learning.

    scorer : A single callable or dict mapping scorer name to the callable
        If it is a single callable, the return value for ``train_scores`` and
        ``test_scores`` is a single float.

        For a dict, it should be one mapping the scorer name to the scorer
        callable object / function.

        The callable object / fn should have signature
        ``scorer(estimator, X, y)``.

    train : array-like of shape (n_train_samples,)
        Indices of training samples.

    test : array-like of shape (n_test_samples,)
        Indices of test samples.

    verbose : int
        The verbosity level.

    error_score : 'raise' or numeric, default=np.nan
        Value to assign to the score if an error occurs in estimator fitting.
        If set to 'raise', the error is raised.
        If a numeric value is given, FitFailedWarning is raised.

    parameters : dict or None
        Parameters to be set on the estimator.

    fit_params : dict or None
        Parameters that will be passed to ``estimator.fit``.

    score_params : dict or None
        Parameters that will be passed to the scorer.

    return_train_score : bool, default=False
        Compute and return score on training set.

    return_parameters : bool, default=False
        Return parameters that has been used for the estimator.

    split_progress : {list, tuple} of int, default=None
        A list or tuple of format (<current_split_id>, <total_num_of_splits>).

    candidate_progress : {list, tuple} of int, default=None
        A list or tuple of format
        (<current_candidate_id>, <total_number_of_candidates>).

    return_n_test_samples : bool, default=False
        Whether to return the ``n_test_samples``.

    return_times : bool, default=False
        Whether to return the fit/score times.

    return_estimator : bool, default=False
        Whether to return the fitted estimator.

    Returns
    -------
    result : dict with the following attributes
        train_scores : dict of scorer name -> float
            Score on training set (for all the scorers),
            returned only if `return_train_score` is `True`.
        test_scores : dict of scorer name -> float
            Score on testing set (for all the scorers).
        n_test_samples : int
            Number of test samples.
        fit_time : float
            Time spent for fitting in seconds.
        score_time : float
            Time spent for scoring in seconds.
        parameters : dict or None
            The parameters that have been evaluated.
        estimator : estimator object
            The fitted estimator.
        fit_error : str or None
            Traceback str if the fit failed, None if the fit succeeded.
    """
    pass
# WARNING: Decompyle incomplete


def _score(estimator, X_test, y_test, scorer, score_params, error_score = ('raise',)):
    '''Compute the score(s) of an estimator on a given test set.

    Will return a dict of floats if `scorer` is a _MultiMetricScorer, otherwise a single
    float is returned.
    '''
    pass
# WARNING: Decompyle incomplete

cross_val_predict = (lambda estimator = validate_params({
    'estimator': [
        HasMethods([
            'fit',
            'predict'])],
    'X': [
        'array-like',
        'sparse matrix'],
    'y': [
        'array-like',
        'sparse matrix',
        None],
    'groups': [
        'array-like',
        None],
    'cv': [
        'cv_object'],
    'n_jobs': [
        Integral,
        None],
    'verbose': [
        'verbose'],
    'params': [
        dict,
        None],
    'pre_dispatch': [
        Integral,
        str,
        None],
    'method': [
        StrOptions({
            'predict',
            'predict_proba',
            'decision_function',
            'predict_log_proba'})] }, prefer_skip_nested_validation = False), X = (None,), y = {
    'groups': None,
    'cv': None,
    'n_jobs': None,
    'verbose': 0,
    'params': None,
    'pre_dispatch': '2*n_jobs',
    'method': 'predict' }, *, groups, cv, n_jobs: pass# WARNING: Decompyle incomplete
)()

def _fit_and_predict(estimator, X, y, train, test, fit_params, method):
    """Fit estimator and predict values for a given dataset split.

    Read more in the :ref:`User Guide <cross_validation>`.

    Parameters
    ----------
    estimator : estimator object implementing 'fit' and 'predict'
        The object to use to fit the data.

    X : array-like of shape (n_samples, n_features)
        The data to fit.

        .. versionchanged:: 0.20
            X is only required to be an object with finite length or shape now

    y : array-like of shape (n_samples,) or (n_samples, n_outputs) or None
        The target variable to try to predict in the case of
        supervised learning.

    train : array-like of shape (n_train_samples,)
        Indices of training samples.

    test : array-like of shape (n_test_samples,)
        Indices of test samples.

    fit_params : dict or None
        Parameters that will be passed to ``estimator.fit``.

    method : str
        Invokes the passed method name of the passed estimator.

    Returns
    -------
    predictions : sequence
        Result of calling 'estimator.method'
    """
    pass
# WARNING: Decompyle incomplete


def _enforce_prediction_order(classes, predictions, n_classes, method):
    '''Ensure that prediction arrays have correct column order

    When doing cross-validation, if one or more classes are
    not present in the subset of data used for training,
    then the output prediction array might not have the same
    columns as other folds. Use the list of class names
    (assumed to be ints) to enforce the correct column order.

    Note that `classes` is the list of classes in this fold
    (a subset of the classes in the full training set)
    and `n_classes` is the number of classes in the full training set.
    '''
    (xp, _) = get_namespace(predictions, classes)
    classes_length = classes.shape[0]
    if n_classes != classes_length:
        recommendation = 'To fix this, use a cross-validation technique resulting in properly stratified folds'
        warnings.warn('Number of classes in training fold ({}) does not match total number of classes ({}). Results may not be appropriate for your use case. {}'.format(classes_length, n_classes, recommendation), RuntimeWarning)
        if method == 'decision_function':
            if predictions.ndim == 2 and predictions.shape[1] != classes_length:
                raise ValueError('Output shape {} of {} does not match number of classes ({}) in fold. Irregular decision_function outputs are not currently supported by cross_val_predict'.format(predictions.shape, method, classes_length))
            if classes_length <= 2:
                raise ValueError('Only {} class/es in training fold, but {} in overall dataset. This is not supported for decision_function with imbalanced folds. {}'.format(classes_length, n_classes, recommendation))
        float_min = xp.finfo(predictions.dtype).min
        default_values = {
            'decision_function': float_min,
            'predict_log_proba': float_min,
            'predict_proba': 0 }
        predictions_for_all_classes = xp.full((_num_samples(predictions), n_classes), default_values[method], dtype = predictions.dtype)
        predictions_for_all_classes[(:, classes)] = predictions
        predictions = predictions_for_all_classes
    return predictions


def _check_is_permutation(indices, n_samples):
    '''Check whether indices is a reordering of the array np.arange(n_samples)

    Parameters
    ----------
    indices : ndarray
        int array to test
    n_samples : int
        number of expected elements

    Returns
    -------
    is_partition : bool
        True iff sorted(indices) is np.arange(n)
    '''
    if len(indices) != n_samples:
        return False
    hit = None.zeros(n_samples, dtype = bool)
    hit[indices] = True
    if not np.all(hit):
        return False

permutation_test_score = (lambda estimator, X = validate_params({
    'estimator': [
        HasMethods('fit')],
    'X': [
        'array-like',
        'sparse matrix'],
    'y': [
        'array-like',
        None],
    'groups': [
        'array-like',
        None],
    'cv': [
        'cv_object'],
    'n_permutations': [
        Interval(Integral, 1, None, closed = 'left')],
    'n_jobs': [
        Integral,
        None],
    'random_state': [
        'random_state'],
    'verbose': [
        'verbose'],
    'scoring': [
        StrOptions(set(get_scorer_names())),
        callable,
        None],
    'params': [
        dict,
        None] }, prefer_skip_nested_validation = False), y = {
    'groups': None,
    'cv': None,
    'n_permutations': 100,
    'n_jobs': None,
    'random_state': 0,
    'verbose': 0,
    'scoring': None,
    'params': None }, *, groups, cv, n_permutations: pass# WARNING: Decompyle incomplete
)()

def _permutation_test_score(estimator, X, y, cv, scorer, split_params, fit_params, score_params):
    '''Auxiliary function for permutation_test_score'''
    pass
# WARNING: Decompyle incomplete


def _shuffle(y, groups, random_state):
    '''Return a shuffled copy of y eventually shuffle among same groups.'''
    pass
# WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete
