# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _classification_threshold.pyc (Python 3.11)

from collections.abc import MutableMapping
from numbers import Integral, Real
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin, MetaEstimatorMixin, _fit_context, clone
from sklearn.exceptions import NotFittedError
from sklearn.metrics import check_scoring, get_scorer_names
from sklearn.metrics._scorer import _CurveScorer, _threshold_scores_to_class_labels
from sklearn.model_selection._split import StratifiedShuffleSplit, check_cv
from sklearn.utils import _safe_indexing, get_tags
from sklearn.utils._param_validation import HasMethods, Interval, RealNotInt, StrOptions
from sklearn.utils._response import _get_response_values_binary
from sklearn.utils.metadata_routing import MetadataRouter, MethodMapping, _raise_for_params, process_routing
from sklearn.utils.metaestimators import available_if
from sklearn.utils.multiclass import type_of_target
from sklearn.utils.parallel import Parallel, delayed
from sklearn.utils.validation import _check_method_params, _estimator_has, _num_samples, check_is_fitted, indexable

def _check_is_fitted(estimator):
    
    try:
        check_is_fitted(estimator.estimator)
        return None
    except NotFittedError:
        check_is_fitted(estimator, 'estimator_')
        return None



class BaseThresholdClassifier(BaseEstimator, MetaEstimatorMixin, ClassifierMixin):
    pass
# WARNING: Decompyle incomplete


class FixedThresholdClassifier(BaseThresholdClassifier):
    pass
# WARNING: Decompyle incomplete


def _fit_and_score_over_thresholds(classifier, X, y, *, fit_params, train_idx, val_idx, curve_scorer, score_params):
    '''Fit a classifier and compute the scores for different decision thresholds.

    Parameters
    ----------
    classifier : estimator instance
        The classifier to fit and use for scoring. If `classifier` is already fitted,
        it will be used as is.

    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        The entire dataset.

    y : array-like of shape (n_samples,)
        The entire target vector.

    fit_params : dict
        Parameters to pass to the `fit` method of the underlying classifier.

    train_idx : ndarray of shape (n_train_samples,) or None
        The indices of the training set. If `None`, `classifier` is expected to be
        already fitted.

    val_idx : ndarray of shape (n_val_samples,)
        The indices of the validation set used to score `classifier`. If `train_idx`,
        the entire set will be used.

    curve_scorer : scorer instance
        The scorer taking `classifier` and the validation set as input and outputting
        decision thresholds and scores as a curve. Note that this is different from
        the usual scorer that outputs a single score value as `curve_scorer`
        outputs a single score value for each threshold.

    score_params : dict
        Parameters to pass to the `score` method of the underlying scorer.

    Returns
    -------
    scores : ndarray of shape (thresholds,) or tuple of such arrays
        The scores computed for each decision threshold. When TPR/TNR or precision/
        recall are computed, `scores` is a tuple of two arrays.

    potential_thresholds : ndarray of shape (thresholds,)
        The decision thresholds used to compute the scores. They are returned in
        ascending order.
    '''
    pass
# WARNING: Decompyle incomplete


def _mean_interpolated_score(target_thresholds, cv_thresholds, cv_scores):
    '''Compute the mean interpolated score across folds by defining common thresholds.

    Parameters
    ----------
    target_thresholds : ndarray of shape (thresholds,)
        The thresholds to use to compute the mean score.

    cv_thresholds : ndarray of shape (n_folds, thresholds_fold)
        The thresholds used to compute the scores for each fold.

    cv_scores : ndarray of shape (n_folds, thresholds_fold)
        The scores computed for each threshold for each fold.

    Returns
    -------
    mean_score : ndarray of shape (thresholds,)
        The mean score across all folds for each target threshold.
    '''
    pass
# WARNING: Decompyle incomplete


class TunedThresholdClassifierCV(BaseThresholdClassifier):
    pass
# WARNING: Decompyle incomplete
