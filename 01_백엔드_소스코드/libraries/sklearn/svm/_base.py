# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _base.pyc (Python 3.11)

import warnings
from abc import ABCMeta, abstractmethod
from numbers import Integral, Real
import numpy as np
from scipy.sparse import sparse as sp
from sklearn.base import BaseEstimator, ClassifierMixin, _fit_context
from sklearn.exceptions import ConvergenceWarning, NotFittedError
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import _liblinear as liblinear
from sklearn.svm import _libsvm as libsvm
from sklearn.svm import _libsvm_sparse as libsvm_sparse
from sklearn.utils import check_array, check_random_state, column_or_1d, compute_class_weight
from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.utils.extmath import safe_sparse_dot
from sklearn.utils.metaestimators import available_if
from sklearn.utils.multiclass import _ovr_decision_function, check_classification_targets
from sklearn.utils.validation import _check_large_sparse, _check_sample_weight, _num_samples, check_consistent_length, check_is_fitted, validate_data
LIBSVM_IMPL = [
    'c_svc',
    'nu_svc',
    'one_class',
    'epsilon_svr',
    'nu_svr']

def _one_vs_one_coef(dual_coef, n_support, support_vectors):
    '''Generate primal coefficients from dual coefficients
    for the one-vs-one multi class LibSVM in the case
    of a linear kernel.'''
    n_class = dual_coef.shape[0] + 1
    coef = []
    sv_locs = np.cumsum(np.hstack([
        [
            0],
        n_support]))
    for class1 in range(n_class):
        sv1 = support_vectors[(sv_locs[class1]:sv_locs[class1 + 1], :)]
        for class2 in range(class1 + 1, n_class):
            sv2 = support_vectors[(sv_locs[class2]:sv_locs[class2 + 1], :)]
            alpha1 = dual_coef[(class2 - 1, sv_locs[class1]:sv_locs[class1 + 1])]
            alpha2 = dual_coef[(class1, sv_locs[class2]:sv_locs[class2 + 1])]
            coef.append(safe_sparse_dot(alpha1, sv1) + safe_sparse_dot(alpha2, sv2))
            return coef


def BaseLibSVM():
    '''BaseLibSVM'''
    pass
# WARNING: Decompyle incomplete

BaseLibSVM = <NODE:27>(BaseLibSVM, 'BaseLibSVM', BaseEstimator, metaclass = ABCMeta)

def BaseSVC():
    '''BaseSVC'''
    pass
# WARNING: Decompyle incomplete

BaseSVC = <NODE:27>(BaseSVC, 'BaseSVC', ClassifierMixin, BaseLibSVM, metaclass = ABCMeta)

def _get_liblinear_solver_type(multi_class, penalty, loss, dual):
    '''Find the liblinear magic number for the solver.

    This number depends on the values of the following attributes:
      - multi_class
      - penalty
      - loss
      - dual

    The same number is also internally used by LibLinear to determine
    which solver to use.
    '''
    _solver_type_dict = {
        'logistic_regression': {
            'l1': {
                False: 6 },
            'l2': {
                False: 0,
                True: 7 } },
        'hinge': {
            'l2': {
                True: 3 } },
        'squared_hinge': {
            'l1': {
                False: 5 },
            'l2': {
                False: 2,
                True: 1 } },
        'epsilon_insensitive': {
            'l2': {
                True: 13 } },
        'squared_epsilon_insensitive': {
            'l2': {
                False: 11,
                True: 12 } },
        'crammer_singer': 4 }
    if multi_class == 'crammer_singer':
        return _solver_type_dict[multi_class]
    if None != 'ovr':
        raise ValueError('`multi_class` must be one of `ovr`, `crammer_singer`, got %r' % multi_class)
    _solver_pen = _solver_type_dict.get(loss, None)
# WARNING: Decompyle incomplete


def _fit_liblinear(X, y, C, fit_intercept, intercept_scaling, class_weight, penalty, dual, verbose, max_iter, tol, random_state, multi_class, loss, epsilon, sample_weight = (None, 'ovr', 'logistic_regression', 0.1, None)):
    '''Used by Logistic Regression (and CV) and LinearSVC/LinearSVR.

    Preprocessing is done in this function before supplying it to liblinear.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        Training vector, where `n_samples` is the number of samples and
        `n_features` is the number of features.

    y : array-like of shape (n_samples,)
        Target vector relative to X

    C : float
        Inverse of cross-validation parameter. The lower the C, the higher
        the penalization.

    fit_intercept : bool
        Whether or not to fit an intercept. If set to True, the feature vector
        is extended to include an intercept term: ``[x_1, ..., x_n, 1]``, where
        1 corresponds to the intercept. If set to False, no intercept will be
        used in calculations (i.e. data is expected to be already centered).

    intercept_scaling : float
        Liblinear internally penalizes the intercept, treating it like any
        other term in the feature vector. To reduce the impact of the
        regularization on the intercept, the `intercept_scaling` parameter can
        be set to a value greater than 1; the higher the value of
        `intercept_scaling`, the lower the impact of regularization on it.
        Then, the weights become `[w_x_1, ..., w_x_n,
        w_intercept*intercept_scaling]`, where `w_x_1, ..., w_x_n` represent
        the feature weights and the intercept weight is scaled by
        `intercept_scaling`. This scaling allows the intercept term to have a
        different regularization behavior compared to the other features.

    class_weight : dict or \'balanced\', default=None
        Weights associated with classes in the form ``{class_label: weight}``.
        If not given, all classes are supposed to have weight one. For
        multi-output problems, a list of dicts can be provided in the same
        order as the columns of y.

        The "balanced" mode uses the values of y to automatically adjust
        weights inversely proportional to class frequencies in the input data
        as ``n_samples / (n_classes * np.bincount(y))``

    penalty : {\'l1\', \'l2\'}
        The norm of the penalty used in regularization.

    dual : bool
        Dual or primal formulation,

    verbose : int
        Set verbose to any positive number for verbosity.

    max_iter : int
        Number of iterations.

    tol : float
        Stopping condition.

    random_state : int, RandomState instance or None, default=None
        Controls the pseudo random number generation for shuffling the data.
        Pass an int for reproducible output across multiple function calls.
        See :term:`Glossary <random_state>`.

    multi_class : {\'ovr\', \'crammer_singer\'}, default=\'ovr\'
        `ovr` trains n_classes one-vs-rest classifiers, while `crammer_singer`
        optimizes a joint objective over all classes.
        While `crammer_singer` is interesting from a theoretical perspective
        as it is consistent it is seldom used in practice and rarely leads to
        better accuracy and is more expensive to compute.
        If `crammer_singer` is chosen, the options loss, penalty and dual will
        be ignored.

    loss : {\'logistic_regression\', \'hinge\', \'squared_hinge\',             \'epsilon_insensitive\', \'squared_epsilon_insensitive},             default=\'logistic_regression\'
        The loss function used to fit the model.

    epsilon : float, default=0.1
        Epsilon parameter in the epsilon-insensitive loss function. Note
        that the value of this parameter depends on the scale of the target
        variable y. If unsure, set epsilon=0.

    sample_weight : array-like of shape (n_samples,), default=None
        Weights assigned to each sample.

    Returns
    -------
    coef_ : ndarray of shape (n_features, n_features + 1)
        The coefficient vector got by minimizing the objective function.

    intercept_ : float
        The intercept term added to the vector.

    n_iter_ : array of int
        Number of iterations run across for each class.
    '''
    if loss not in ('epsilon_insensitive', 'squared_epsilon_insensitive'):
        enc = LabelEncoder()
        y_ind = enc.fit_transform(y)
        classes_ = enc.classes_
        if len(classes_) < 2:
            raise ValueError('This solver needs samples of at least 2 classes in the data, but the data contains only one class: %r' % classes_[0])
        class_weight_ = compute_class_weight(class_weight, classes = classes_, y = y, sample_weight = sample_weight)
    else:
        class_weight_ = np.empty(0, dtype = np.float64)
        y_ind = y
    liblinear.set_verbosity_wrap(verbose)
    rnd = check_random_state(random_state)
    if verbose:
        print('[LibLinear]', end = '')
    bias = -1
    if fit_intercept:
        if intercept_scaling <= 0:
            raise ValueError('Intercept scaling is %r but needs to be greater than 0. To disable fitting an intercept, set fit_intercept=False.' % intercept_scaling)
        bias = intercept_scaling
    libsvm.set_verbosity_wrap(verbose)
    libsvm_sparse.set_verbosity_wrap(verbose)
    liblinear.set_verbosity_wrap(verbose)
    if sp.issparse(X):
        _check_large_sparse(X)
    y_ind = np.asarray(y_ind, dtype = np.float64).ravel()
    y_ind = np.require(y_ind, requirements = 'W')
    sample_weight = _check_sample_weight(sample_weight, X, dtype = np.float64)
    solver_type = _get_liblinear_solver_type(multi_class, penalty, loss, dual)
    (raw_coef_, n_iter_) = liblinear.train_wrap(X, y_ind, sp.issparse(X), solver_type, tol, bias, C, class_weight_, max_iter, rnd.randint(np.iinfo('i').max), epsilon, sample_weight)
    n_iter_max = max(n_iter_)
    if n_iter_max >= max_iter:
        warnings.warn('Liblinear failed to converge, increase the number of iterations.', ConvergenceWarning)
    if fit_intercept:
        coef_ = raw_coef_[(:, :-1)]
        intercept_ = intercept_scaling * raw_coef_[(:, -1)]
    else:
        coef_ = raw_coef_
        intercept_ = 0
    return (coef_, intercept_, n_iter_)
