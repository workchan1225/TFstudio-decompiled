# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _scorer.pyc (Python 3.11)

__doc__ = '\nThe :mod:`sklearn.metrics.scorer` submodule implements a flexible\ninterface for model selection and evaluation using\narbitrary score functions.\n\nA scorer object is a callable that can be passed to\n:class:`~sklearn.model_selection.GridSearchCV` or\n:func:`sklearn.model_selection.cross_val_score` as the ``scoring``\nparameter, to specify how a model should be evaluated.\n\nThe signature of the call is ``(estimator, X, y)`` where ``estimator``\nis the model to be evaluated, ``X`` is the test data and ``y`` is the\nground truth labeling (or ``None`` in the case of unsupervised models).\n'
import copy
import warnings
from collections import Counter
from functools import partial
from inspect import signature
from numbers import Integral
from traceback import format_exc
import numpy as np
from sklearn.base import is_regressor
from sklearn.metrics import accuracy_score, average_precision_score, balanced_accuracy_score, brier_score_loss, class_likelihood_ratios, d2_absolute_error_score, d2_brier_score, d2_log_loss_score, explained_variance_score, f1_score, jaccard_score, log_loss, matthews_corrcoef, max_error, mean_absolute_error, mean_absolute_percentage_error, mean_gamma_deviance, mean_poisson_deviance, mean_squared_error, mean_squared_log_error, median_absolute_error, precision_score, r2_score, recall_score, roc_auc_score, root_mean_squared_error, root_mean_squared_log_error, top_k_accuracy_score
from sklearn.metrics.cluster import adjusted_mutual_info_score, adjusted_rand_score, completeness_score, fowlkes_mallows_score, homogeneity_score, mutual_info_score, normalized_mutual_info_score, rand_score, v_measure_score
from sklearn.utils import Bunch
from sklearn.utils._param_validation import HasMethods, StrOptions, validate_params
from sklearn.utils._response import _get_response_values
from sklearn.utils.metadata_routing import MetadataRequest, MetadataRouter, MethodMapping, _MetadataRequester, _raise_for_params, _routing_enabled, get_routing_for_object, process_routing
from sklearn.utils.validation import _check_response_method

def _cached_call(cache, estimator, response_method, *args, **kwargs):
    '''Call estimator with method and args and kwargs.'''
    pass
# WARNING: Decompyle incomplete


def _get_func_repr_or_name(func):
    '''Returns the name of the function or repr of a partial.'''
    if isinstance(func, partial):
        return repr(func)
    return None.__name__


class _MultimetricScorer:
    '''Callable for multimetric scoring used to avoid repeated calls
    to `predict_proba`, `predict`, and `decision_function`.

    `_MultimetricScorer` will return a dictionary of scores corresponding to
    the scorers in the dictionary. Note that `_MultimetricScorer` can be
    created with a dictionary with one key  (i.e. only one actual scorer).

    Parameters
    ----------
    scorers : dict
        Dictionary mapping names to callable scorers.

    raise_exc : bool, default=True
        Whether to raise the exception in `__call__` or not. If set to `False`
        a formatted string of the exception details is passed as result of
        the failing scorer.
    '''
    
    def __init__(self = None, *, scorers, raise_exc):
        self._scorers = scorers
        self._raise_exc = raise_exc

    
    def __call__(self, estimator, *args, **kwargs):
        '''Evaluate predicted target values.'''
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        scorers = (lambda .0: [ f'''"{s}"''' for s in .0 ])(self._scorers())
        return f'''MultiMetricScorer({scorers})'''

    
    def _accept_sample_weight(self):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self._scorers.values()())

    
    def _use_cache(self, estimator):
        '''Return True if using a cache is beneficial, thus when a response method will
        be called several time.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_metadata_routing(self):
        '''Get metadata routing of this object.

        Please check :ref:`User Guide <metadata_routing>` on how the routing
        mechanism works.

        .. versionadded:: 1.3

        Returns
        -------
        routing : MetadataRouter
            A :class:`~utils.metadata_routing.MetadataRouter` encapsulating
            routing information.
        '''
        pass
    # WARNING: Decompyle incomplete



class _BaseScorer(_MetadataRequester):
    '''Base scorer that is used as `scorer(estimator, X, y_true)`.

    Parameters
    ----------
    score_func : callable
        The score function to use. It will be called as
        `score_func(y_true, y_pred, **kwargs)`.

    sign : int
        Either 1 or -1 to returns the score with `sign * score_func(estimator, X, y)`.
        Thus, `sign` defined if higher scores are better or worse.

    kwargs : dict
        Additional parameters to pass to the score function.

    response_method : str
        The method to call on the estimator to get the response values.
    '''
    
    def __init__(self, score_func, sign, kwargs, response_method = ('predict',)):
        self._score_func = score_func
        self._sign = sign
        self._kwargs = kwargs
        self._response_method = response_method

    
    def _get_pos_label(self):
        if 'pos_label' in self._kwargs:
            return self._kwargs['pos_label']
        score_func_params = None(self._score_func).parameters
        if 'pos_label' in score_func_params:
            return score_func_params['pos_label'].default

    
    def _accept_sample_weight(self):
        return 'sample_weight' in signature(self._score_func).parameters

    
    def __repr__(self):
        sign_string = '' if self._sign > 0 else ', greater_is_better=False'
        response_method_string = f''', response_method={self._response_method!r}'''
        kwargs_string = (lambda .0: [ f''', {k}={v}''' for k, v in .0 ])(self._kwargs.items()())
        return f'''make_scorer({_get_func_repr_or_name(self._score_func)}{sign_string}{response_method_string}{kwargs_string})'''

    
    def _routing_repr(self):
        return repr(self)

    
    def __call__(self, estimator, X, y_true, sample_weight = (None,), **kwargs):
        '''Evaluate predicted target values for X relative to y_true.

        Parameters
        ----------
        estimator : object
            Trained estimator to use for scoring. Must have a predict_proba
            method; the output of that is used to compute the score.

        X : {array-like, sparse matrix}
            Test data that will be fed to estimator.predict.

        y_true : array-like
            Gold standard target values for X.

        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights.

        **kwargs : dict
            Other parameters passed to the scorer. Refer to
            :func:`set_score_request` for more details.

            Only available if `enable_metadata_routing=True`. See the
            :ref:`User Guide <metadata_routing>`.

            .. versionadded:: 1.3

        Returns
        -------
        score : float
            Score function applied to prediction of estimator on X.
        '''
        _raise_for_params(kwargs, self, None)
        _kwargs = copy.deepcopy(kwargs)
    # WARNING: Decompyle incomplete

    
    def _warn_overlap(self, message, kwargs):
        '''Warn if there is any overlap between ``self._kwargs`` and ``kwargs``.

        This method is intended to be used to check for overlap between
        ``self._kwargs`` and ``kwargs`` passed as metadata.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def set_score_request(self, **kwargs):
        '''Set requested parameters by the scorer.

        Please see :ref:`User Guide <metadata_routing>` on how the routing
        mechanism works.

        .. versionadded:: 1.3

        Parameters
        ----------
        kwargs : dict
            Arguments should be of the form ``param_name=alias``, and `alias`
            can be one of ``{True, False, None, str}``.
        '''
        if not _routing_enabled():
            raise RuntimeError('This method is only available when metadata routing is enabled. You can enable it using sklearn.set_config(enable_metadata_routing=True).')
        self._warn_overlap(message = 'You are setting metadata request for parameters which are already set as kwargs for this metric. These set values will be overridden by passed metadata if provided. Please pass them either as metadata or kwargs to `make_scorer`.', kwargs = kwargs)
        self._metadata_request = MetadataRequest(owner = self)
        for param, alias in kwargs.items():
            self._metadata_request.score.add_request(param = param, alias = alias)
            return self



class _Scorer(_BaseScorer):
    
    def _score(self, method_caller, estimator, X, y_true, **kwargs):
        '''Evaluate the response method of `estimator` on `X` and `y_true`.

        Parameters
        ----------
        method_caller : callable
            Returns predictions given an estimator, method name, and other
            arguments, potentially caching results.

        estimator : object
            Trained estimator to use for scoring.

        X : {array-like, sparse matrix}
            Test data that will be fed to clf.decision_function or
            clf.predict_proba.

        y_true : array-like
            Gold standard target values for X. These must be class labels,
            not decision function values.

        **kwargs : dict
            Other parameters passed to the scorer. Refer to
            :func:`set_score_request` for more details.

        Returns
        -------
        score : float
            Score function applied to prediction of estimator on X.
        '''
        self._warn_overlap(message = 'There is an overlap between set kwargs of this scorer instance and passed metadata. Please pass them either as kwargs to `make_scorer` or metadata, but not both.', kwargs = kwargs)
        pos_label = None if is_regressor(estimator) else self._get_pos_label()
        response_method = _check_response_method(estimator, self._response_method)
        y_pred = method_caller(estimator, _get_response_method_name(response_method), X, pos_label = pos_label)
    # WARNING: Decompyle incomplete


get_scorer = (lambda scoring: if isinstance(scoring, str):
try:
scorer = copy.deepcopy(_SCORERS[scoring])except KeyError:
raise ValueError('%r is not a valid scoring value. Use sklearn.metrics.get_scorer_names() to get valid options.' % scoring)scorer = scoringscorer)()

class _PassthroughScorer(_MetadataRequester):
    
    def __init__(self, estimator):
        self._estimator = estimator

    
    def __call__(self, estimator, *args, **kwargs):
        '''Method that wraps estimator.score'''
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return f'''{type(self._estimator).__name__}.score'''

    
    def _routing_repr(self):
        return repr(self)

    
    def _accept_sample_weight(self):
        return 'sample_weight' in signature(self._estimator.score).parameters

    
    def get_metadata_routing(self):
        '''Get requested data properties.

        Please check :ref:`User Guide <metadata_routing>` on how the routing
        mechanism works.

        .. versionadded:: 1.3

        Returns
        -------
        routing : MetadataRouter
            A :class:`~utils.metadata_routing.MetadataRouter` encapsulating
            routing information.
        '''
        return get_routing_for_object(self._estimator)



def _check_multimetric_scoring(estimator, scoring):
    '''Check the scoring parameter in cases when multiple metrics are allowed.

    In addition, multimetric scoring leverages a caching mechanism to not call the same
    estimator response method multiple times. Hence, the scorer is modified to only use
    a single response method given a list of response methods and the estimator.

    Parameters
    ----------
    estimator : sklearn estimator instance
        The estimator for which the scoring will be applied.

    scoring : list, tuple or dict
        Strategy to evaluate the performance of the cross-validated model on
        the test set.

        The possibilities are:

        - a list or tuple of unique strings;
        - a callable returning a dictionary where they keys are the metric
          names and the values are the metric scores;
        - a dictionary with metric names as keys and callables a values.

        See :ref:`multimetric_grid_search` for an example.

    Returns
    -------
    scorers_dict : dict
        A dict mapping each scorer name to its validated scorer.
    '''
    pass
# WARNING: Decompyle incomplete


def _get_response_method_name(response_method):
    
    try:
        return response_method.__name__
    except AttributeError:
        return 


make_scorer = (lambda score_func = validate_params({
    'score_func': [
        callable],
    'response_method': [
        list,
        tuple,
        StrOptions({
            'predict',
            'predict_proba',
            'decision_function'})],
    'greater_is_better': [
        'boolean'] }, prefer_skip_nested_validation = True), *, response_method: sign = 1 if greater_is_better else -1_Scorer(score_func, sign, kwargs, response_method))()
explained_variance_scorer = make_scorer(explained_variance_score)
r2_scorer = make_scorer(r2_score)
neg_max_error_scorer = make_scorer(max_error, greater_is_better = False)
neg_mean_squared_error_scorer = make_scorer(mean_squared_error, greater_is_better = False)
neg_mean_squared_log_error_scorer = make_scorer(mean_squared_log_error, greater_is_better = False)
neg_mean_absolute_error_scorer = make_scorer(mean_absolute_error, greater_is_better = False)
neg_mean_absolute_percentage_error_scorer = make_scorer(mean_absolute_percentage_error, greater_is_better = False)
neg_median_absolute_error_scorer = make_scorer(median_absolute_error, greater_is_better = False)
neg_root_mean_squared_error_scorer = make_scorer(root_mean_squared_error, greater_is_better = False)
neg_root_mean_squared_log_error_scorer = make_scorer(root_mean_squared_log_error, greater_is_better = False)
neg_mean_poisson_deviance_scorer = make_scorer(mean_poisson_deviance, greater_is_better = False)
neg_mean_gamma_deviance_scorer = make_scorer(mean_gamma_deviance, greater_is_better = False)
d2_absolute_error_scorer = make_scorer(d2_absolute_error_score)
d2_brier_score_scorer = make_scorer(d2_brier_score, response_method = 'predict_proba')
d2_log_loss_scorer = make_scorer(d2_log_loss_score, response_method = 'predict_proba')
accuracy_scorer = make_scorer(accuracy_score)
balanced_accuracy_scorer = make_scorer(balanced_accuracy_score)
matthews_corrcoef_scorer = make_scorer(matthews_corrcoef)

def positive_likelihood_ratio(y_true, y_pred):
    return class_likelihood_ratios(y_true, y_pred, replace_undefined_by = 1)[0]


def negative_likelihood_ratio(y_true, y_pred):
    return class_likelihood_ratios(y_true, y_pred, replace_undefined_by = 1)[1]

positive_likelihood_ratio_scorer = make_scorer(positive_likelihood_ratio)
neg_negative_likelihood_ratio_scorer = make_scorer(negative_likelihood_ratio, greater_is_better = False)
top_k_accuracy_scorer = make_scorer(top_k_accuracy_score, greater_is_better = True, response_method = ('decision_function', 'predict_proba'))
roc_auc_scorer = make_scorer(roc_auc_score, greater_is_better = True, response_method = ('decision_function', 'predict_proba'))
average_precision_scorer = make_scorer(average_precision_score, response_method = ('decision_function', 'predict_proba'))
roc_auc_ovo_scorer = make_scorer(roc_auc_score, response_method = 'predict_proba', multi_class = 'ovo')
roc_auc_ovo_weighted_scorer = make_scorer(roc_auc_score, response_method = 'predict_proba', multi_class = 'ovo', average = 'weighted')
roc_auc_ovr_scorer = make_scorer(roc_auc_score, response_method = 'predict_proba', multi_class = 'ovr')
roc_auc_ovr_weighted_scorer = make_scorer(roc_auc_score, response_method = 'predict_proba', multi_class = 'ovr', average = 'weighted')
neg_log_loss_scorer = make_scorer(log_loss, greater_is_better = False, response_method = 'predict_proba')
neg_brier_score_scorer = make_scorer(brier_score_loss, greater_is_better = False, response_method = 'predict_proba')
brier_score_loss_scorer = make_scorer(brier_score_loss, greater_is_better = False, response_method = 'predict_proba')
adjusted_rand_scorer = make_scorer(adjusted_rand_score)
rand_scorer = make_scorer(rand_score)
homogeneity_scorer = make_scorer(homogeneity_score)
completeness_scorer = make_scorer(completeness_score)
v_measure_scorer = make_scorer(v_measure_score)
mutual_info_scorer = make_scorer(mutual_info_score)
adjusted_mutual_info_scorer = make_scorer(adjusted_mutual_info_score)
normalized_mutual_info_scorer = make_scorer(normalized_mutual_info_score)
fowlkes_mallows_scorer = make_scorer(fowlkes_mallows_score)
# WARNING: Decompyle incomplete
