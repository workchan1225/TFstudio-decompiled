# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: discriminant_analysis.pyc (Python 3.11)

'''Linear and quadratic discriminant analysis.'''
import warnings
from numbers import Integral, Real
import numpy as np
import scipy.linalg as scipy
from scipy import linalg
from sklearn.base import BaseEstimator, ClassifierMixin, ClassNamePrefixFeaturesOutMixin, TransformerMixin, _fit_context
from sklearn.covariance import empirical_covariance, ledoit_wolf, shrunk_covariance
from sklearn.linear_model._base import LinearClassifierMixin
from sklearn.preprocessing import StandardScaler
from sklearn.utils._array_api import _expit, device, get_namespace, size
from sklearn.utils._param_validation import HasMethods, Interval, StrOptions
from sklearn.utils.extmath import softmax
from sklearn.utils.multiclass import check_classification_targets, unique_labels
from sklearn.utils.validation import check_is_fitted, validate_data
__all__ = [
    'LinearDiscriminantAnalysis',
    'QuadraticDiscriminantAnalysis']

def _cov(X, shrinkage, covariance_estimator = (None, None)):
    """Estimate covariance matrix (using optional covariance_estimator).
    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        Input data.

    shrinkage : {'empirical', 'auto'} or float, default=None
        Shrinkage parameter, possible values:
          - None or 'empirical': no shrinkage (default).
          - 'auto': automatic shrinkage using the Ledoit-Wolf lemma.
          - float between 0 and 1: fixed shrinkage parameter.

        Shrinkage parameter is ignored if  `covariance_estimator`
        is not None.

    covariance_estimator : estimator, default=None
        If not None, `covariance_estimator` is used to estimate
        the covariance matrices instead of relying on the empirical
        covariance estimator (with potential shrinkage).
        The object should have a fit method and a ``covariance_`` attribute
        like the estimators in :mod:`sklearn.covariance``.
        If None the shrinkage parameter drives the estimate.

        .. versionadded:: 0.24

    Returns
    -------
    s : ndarray of shape (n_features, n_features)
        Estimated covariance matrix.
    """
    pass
# WARNING: Decompyle incomplete


def _class_means(X, y):
    '''Compute class means.

    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        Input data.

    y : array-like of shape (n_samples,) or (n_samples, n_targets)
        Target values.

    Returns
    -------
    means : array-like of shape (n_classes, n_features)
        Class means.
    '''
    (xp, is_array_api_compliant) = get_namespace(X)
    (classes, y) = xp.unique_inverse(y)
    means = xp.zeros((classes.shape[0], X.shape[1]), device = device(X), dtype = X.dtype)
    if is_array_api_compliant:
        for i in range(classes.shape[0]):
            means[(i, :)] = xp.mean(X[y == i], axis = 0)
    cnt = np.bincount(y)
    np.add.at(means, y, X)
    means /= cnt[(:, None)]
    return means


def _class_cov(X, y, priors, shrinkage, covariance_estimator = (None, None)):
    """Compute weighted within-class covariance matrix.

    The per-class covariance are weighted by the class priors.

    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        Input data.

    y : array-like of shape (n_samples,) or (n_samples, n_targets)
        Target values.

    priors : array-like of shape (n_classes,)
        Class priors.

    shrinkage : 'auto' or float, default=None
        Shrinkage parameter, possible values:
          - None: no shrinkage (default).
          - 'auto': automatic shrinkage using the Ledoit-Wolf lemma.
          - float between 0 and 1: fixed shrinkage parameter.

        Shrinkage parameter is ignored if `covariance_estimator` is not None.

    covariance_estimator : estimator, default=None
        If not None, `covariance_estimator` is used to estimate
        the covariance matrices instead of relying the empirical
        covariance estimator (with potential shrinkage).
        The object should have a fit method and a ``covariance_`` attribute
        like the estimators in sklearn.covariance.
        If None, the shrinkage parameter drives the estimate.

        .. versionadded:: 0.24

    Returns
    -------
    cov : array-like of shape (n_features, n_features)
        Weighted within-class covariance matrix
    """
    classes = np.unique(y)
    cov = np.zeros(shape = (X.shape[1], X.shape[1]))
    for idx, group in enumerate(classes):
        Xg = X[(y == group, :)]
        cov += priors[idx] * np.atleast_2d(_cov(Xg, shrinkage, covariance_estimator))
        return cov


class DiscriminantAnalysisPredictionMixin:
    '''Mixin class for QuadraticDiscriminantAnalysis and NearestCentroid.'''
    
    def decision_function(self, X):
        '''Apply decision function to an array of samples.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Array of samples (test vectors).

        Returns
        -------
        y_scores : ndarray of shape (n_samples,) or (n_samples, n_classes)
            Decision function values related to each class, per sample.
            In the two-class case, the shape is `(n_samples,)`, giving the
            log likelihood ratio of the positive class.
        '''
        y_scores = self._decision_function(X)
        if len(self.classes_) == 2:
            return y_scores[(:, 1)] - y_scores[(:, 0)]

    
    def predict(self, X):
        '''Perform classification on an array of vectors `X`.

        Returns the class label for each sample.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Input vectors, where `n_samples` is the number of samples and
            `n_features` is the number of features.

        Returns
        -------
        y_pred : ndarray of shape (n_samples,)
            Class label for each sample.
        '''
        scores = self._decision_function(X)
        return self.classes_.take(scores.argmax(axis = 1))

    
    def predict_proba(self, X):
        '''Estimate class probabilities.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Input data.

        Returns
        -------
        y_proba : ndarray of shape (n_samples, n_classes)
            Probability estimate of the sample for each class in the
            model, where classes are ordered as they are in `self.classes_`.
        '''
        return np.exp(self.predict_log_proba(X))

    
    def predict_log_proba(self, X):
        '''Estimate log class probabilities.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Input data.

        Returns
        -------
        y_log_proba : ndarray of shape (n_samples, n_classes)
            Estimated log probabilities.
        '''
        scores = self._decision_function(X)
        log_likelihood = scores - scores.max(axis = 1)[(:, np.newaxis)]
        return log_likelihood - np.log(np.exp(log_likelihood).sum(axis = 1)[(:, np.newaxis)])



class LinearDiscriminantAnalysis(BaseEstimator, TransformerMixin, LinearClassifierMixin, ClassNamePrefixFeaturesOutMixin):
    pass
# WARNING: Decompyle incomplete


class QuadraticDiscriminantAnalysis(BaseEstimator, ClassifierMixin, DiscriminantAnalysisPredictionMixin):
    pass
# WARNING: Decompyle incomplete
