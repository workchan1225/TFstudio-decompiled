# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: multiclass.pyc (Python 3.11)

'''Multiclass learning algorithms.

- one-vs-the-rest / one-vs-all
- one-vs-one
- error correcting output codes

The estimators provided in this module are meta-estimators: they require a base
estimator to be provided in their constructor. For example, it is possible to
use these estimators to turn a binary classifier or a regressor into a
multiclass classifier. It is also possible to use these estimators with
multiclass estimators in the hope that their accuracy or runtime performance
improves.

All classifiers in scikit-learn implement multiclass classification; you
only need to use this module if you want to experiment with custom multiclass
strategies.

The one-vs-the-rest meta-classifier also implements a `predict_proba` method,
so long as such a method is implemented by the base classifier. This method
returns probabilities of class membership in both the single label and
multilabel case.  Note that in the multilabel case, probabilities are the
marginal probability that a given sample falls in the given class. As such, in
the multilabel case the sum of these probabilities over all possible labels
for a given sample *will not* sum to unity, as they do in the single label
case.
'''
import array
import itertools
import warnings
from numbers import Integral, Real
import numpy as np
from scipy.sparse import sparse as sp
from sklearn.base import BaseEstimator, ClassifierMixin, MetaEstimatorMixin, MultiOutputMixin, _fit_context, clone, is_classifier, is_regressor
from sklearn.metrics.pairwise import pairwise_distances_argmin
from sklearn.preprocessing import LabelBinarizer
from sklearn.utils import check_random_state
from sklearn.utils._param_validation import HasMethods, Interval
from sklearn.utils._tags import get_tags
from sklearn.utils.metadata_routing import MetadataRouter, MethodMapping, _raise_for_params, process_routing
from sklearn.utils.metaestimators import _safe_split, available_if
from sklearn.utils.multiclass import _check_partial_fit_first_call, _ovr_decision_function, check_classification_targets
from sklearn.utils.parallel import Parallel, delayed
from sklearn.utils.validation import _check_method_params, _num_samples, check_is_fitted, validate_data
__all__ = [
    'OneVsOneClassifier',
    'OneVsRestClassifier',
    'OutputCodeClassifier']

def _fit_binary(estimator, X, y, fit_params, classes = (None,)):
    '''Fit a single binary estimator.'''
    unique_y = np.unique(y)
# WARNING: Decompyle incomplete


def _partial_fit_binary(estimator, X, y, partial_fit_params):
    '''Partially fit a single binary estimator.'''
    pass
# WARNING: Decompyle incomplete


def _predict_binary(estimator, X):
    '''Make predictions using a single binary estimator.'''
    if is_regressor(estimator):
        return estimator.predict(X)
    
    try:
        score = np.ravel(estimator.decision_function(X))
    except (AttributeError, NotImplementedError):
        score = estimator.predict_proba(X)[(:, 1)]

    return score


def _threshold_for_binary_predict(estimator):
    '''Threshold for predictions from binary estimator.'''
    if hasattr(estimator, 'decision_function') and is_classifier(estimator):
        return 0


class _ConstantPredictor(BaseEstimator):
    '''Helper predictor to be used when only one class is present.'''
    
    def fit(self, X, y):
        check_params = dict(ensure_all_finite = False, dtype = None, ensure_2d = False, accept_sparse = True)
        validate_data(self, X, y, reset = True, validate_separately = (check_params, check_params))
        self.y_ = y
        return self

    
    def predict(self, X):
        check_is_fitted(self)
        validate_data(self, X, ensure_all_finite = False, dtype = None, accept_sparse = True, ensure_2d = False, reset = False)
        return np.repeat(self.y_, _num_samples(X))

    
    def decision_function(self, X):
        check_is_fitted(self)
        validate_data(self, X, ensure_all_finite = False, dtype = None, accept_sparse = True, ensure_2d = False, reset = False)
        return np.repeat(self.y_, _num_samples(X))

    
    def predict_proba(self, X):
        check_is_fitted(self)
        validate_data(self, X, ensure_all_finite = False, dtype = None, accept_sparse = True, ensure_2d = False, reset = False)
        y_ = self.y_.astype(np.float64)
        return np.repeat([
            np.hstack([
                1 - y_,
                y_])], _num_samples(X), axis = 0)



def _estimators_has(attr):
    '''Check if self.estimator or self.estimators_[0] has attr.

    If `self.estimators_[0]` has the attr, then its safe to assume that other
    estimators have it too. We raise the original `AttributeError` if `attr`
    does not exist. This function is used together with `available_if`.
    '''
    pass
# WARNING: Decompyle incomplete


class OneVsRestClassifier(BaseEstimator, MetaEstimatorMixin, ClassifierMixin, MultiOutputMixin):
    pass
# WARNING: Decompyle incomplete


def _fit_ovo_binary(estimator, X, y, i, j, fit_params):
    '''Fit a single binary estimator (one-vs-one).'''
    cond = np.logical_or(y == i, y == j)
    y = y[cond]
    y_binary = np.empty(y.shape, int)
    y_binary[y == i] = 0
    y_binary[y == j] = 1
    indcond = np.arange(_num_samples(X))[cond]
    fit_params_subset = _check_method_params(X, params = fit_params, indices = indcond)
    return (_fit_binary(estimator, _safe_split(estimator, X, None, indices = indcond)[0], y_binary, fit_params = fit_params_subset, classes = [
        i,
        j]), indcond)


def _partial_fit_ovo_binary(estimator, X, y, i, j, partial_fit_params):
    '''Partially fit a single binary estimator(one-vs-one).'''
    cond = np.logical_or(y == i, y == j)
    y = y[cond]
    if len(y) != 0:
        y_binary = np.zeros_like(y)
        y_binary[y == j] = 1
        partial_fit_params_subset = _check_method_params(X, params = partial_fit_params, indices = cond)
        return _partial_fit_binary(estimator, X[cond], y_binary, partial_fit_params = partial_fit_params_subset)


class OneVsOneClassifier(BaseEstimator, ClassifierMixin, MetaEstimatorMixin):
    pass
# WARNING: Decompyle incomplete


class OutputCodeClassifier(BaseEstimator, ClassifierMixin, MetaEstimatorMixin):
    pass
# WARNING: Decompyle incomplete
