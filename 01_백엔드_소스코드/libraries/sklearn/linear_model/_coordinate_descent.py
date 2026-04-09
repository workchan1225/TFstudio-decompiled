# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _coordinate_descent.pyc (Python 3.11)

import numbers
import sys
import warnings
from abc import ABC, abstractmethod
from functools import partial
from numbers import Integral, Real
import numpy as np
from joblib import effective_n_jobs
from scipy import sparse
from sklearn.base import MultiOutputMixin, RegressorMixin, _fit_context
from sklearn.linear_model import _cd_fast as cd_fast
from sklearn.linear_model._base import LinearModel, _pre_fit, _preprocess_data
from sklearn.model_selection import check_cv
from sklearn.utils import Bunch, check_array, check_scalar, metadata_routing
from sklearn.utils._metadata_requests import MetadataRouter, MethodMapping, _raise_for_params, get_routing_for_object
from sklearn.utils._param_validation import Hidden, Interval, StrOptions, validate_params
from sklearn.utils.extmath import safe_sparse_dot
from sklearn.utils.metadata_routing import _routing_enabled, process_routing
from sklearn.utils.parallel import Parallel, delayed
from sklearn.utils.sparsefuncs import mean_variance_axis
from sklearn.utils.validation import _check_sample_weight, check_consistent_length, check_is_fitted, check_random_state, column_or_1d, has_fit_parameter, validate_data

def _set_order(X, y, order = ('C',)):
    """Change the order of X and y if necessary.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        Training data.

    y : ndarray of shape (n_samples,)
        Target values.

    order : {None, 'C', 'F'}
        If 'C', dense arrays are returned as C-ordered, sparse matrices in csr
        format. If 'F', dense arrays are return as F-ordered, sparse matrices
        in csc format.

    Returns
    -------
    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        Training data with guaranteed order.

    y : ndarray of shape (n_samples,)
        Target values with guaranteed order.
    """
    if order not in (None, 'C', 'F'):
        raise ValueError("Unknown value for order. Got {} instead of None, 'C' or 'F'.".format(order))
    sparse_X = sparse.issparse(X)
    sparse_y = sparse.issparse(y)
# WARNING: Decompyle incomplete


def _alpha_grid(X, y, Xy, l1_ratio, fit_intercept, eps, n_alphas, sample_weight = (None, 1, True, 0.001, 100, None)):
    '''Compute the grid of alpha values for elastic net parameter search

    Computes alpha_max which results in coef=0 and then uses a multiplicative grid of
    length `eps`.
    `X` is never copied.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        Training data. Pass directly as Fortran-contiguous data to avoid
        unnecessary memory duplication

    y : ndarray of shape (n_samples,) or (n_samples, n_outputs)
        Target values

    Xy : array-like of shape (n_features,) or (n_features, n_outputs),         default=None
        Xy = np.dot(X.T, y) that can be precomputed.

    l1_ratio : float, default=1.0
        The elastic net mixing parameter, with ``0 < l1_ratio <= 1``.
        For ``l1_ratio = 0`` the penalty is an L2 penalty. (currently not
        supported) ``For l1_ratio = 1`` it is an L1 penalty. For
        ``0 < l1_ratio <1``, the penalty is a combination of L1 and L2.

    eps : float, default=1e-3
        Length of the path. ``eps=1e-3`` means that
        ``alpha_min / alpha_max = 1e-3``

    n_alphas : int, default=100
        Number of alphas along the regularization path

    fit_intercept : bool, default=True
        Whether to fit an intercept or not

    sample_weight : ndarray of shape (n_samples,), default=None

    Returns
    -------
    np.ndarray
        Grid of alpha values.
    '''
    if l1_ratio == 0:
        raise ValueError('Automatic alpha grid generation is not supported for l1_ratio=0. Please supply a grid by providing your estimator with the appropriate `alphas=` argument.')
# WARNING: Decompyle incomplete

lasso_path = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'y': [
        'array-like',
        'sparse matrix'],
    'eps': [
        Interval(Real, 0, None, closed = 'neither')],
    'n_alphas': [
        Interval(Integral, 1, None, closed = 'left')],
    'alphas': [
        'array-like',
        None],
    'precompute': [
        StrOptions({
            'auto'}),
        'boolean',
        'array-like'],
    'Xy': [
        'array-like',
        None],
    'copy_X': [
        'boolean'],
    'coef_init': [
        'array-like',
        None],
    'verbose': [
        'verbose'],
    'return_n_iter': [
        'boolean'],
    'positive': [
        'boolean'] }, prefer_skip_nested_validation = True), y = {
    'eps': 0.001,
    'n_alphas': 100,
    'alphas': None,
    'precompute': 'auto',
    'Xy': None,
    'copy_X': True,
    'coef_init': None,
    'verbose': False,
    'return_n_iter': False,
    'positive': False }, *, eps, n_alphas: pass# WARNING: Decompyle incomplete
)()
enet_path = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'y': [
        'array-like',
        'sparse matrix'],
    'l1_ratio': [
        Interval(Real, 0, 1, closed = 'both')],
    'eps': [
        Interval(Real, 0, None, closed = 'neither')],
    'n_alphas': [
        Interval(Integral, 1, None, closed = 'left')],
    'alphas': [
        'array-like',
        None],
    'precompute': [
        StrOptions({
            'auto'}),
        'boolean',
        'array-like'],
    'Xy': [
        'array-like',
        None],
    'copy_X': [
        'boolean'],
    'coef_init': [
        'array-like',
        None],
    'verbose': [
        'verbose'],
    'return_n_iter': [
        'boolean'],
    'positive': [
        'boolean'],
    'check_input': [
        'boolean'] }, prefer_skip_nested_validation = True), y = {
    'l1_ratio': 0.5,
    'eps': 0.001,
    'n_alphas': 100,
    'alphas': None,
    'precompute': 'auto',
    'Xy': None,
    'copy_X': True,
    'coef_init': None,
    'verbose': False,
    'return_n_iter': False,
    'positive': False,
    'check_input': True }, *, l1_ratio, eps: X_offset_param = params.pop('X_offset', None)X_scale_param = params.pop('X_scale', None)sample_weight = params.pop('sample_weight', None)tol = params.pop('tol', 0.0001)max_iter = params.pop('max_iter', 1000)random_state = params.pop('random_state', None)selection = params.pop('selection', 'cyclic')do_screening = params.pop('do_screening', True)if len(params) > 0:
raise ValueError('Unexpected parameters in params', params.keys())# WARNING: Decompyle incomplete
)()

class ElasticNet(LinearModel, RegressorMixin, MultiOutputMixin):
    pass
# WARNING: Decompyle incomplete


class Lasso(ElasticNet):
    pass
# WARNING: Decompyle incomplete


def _path_residuals(X, y, sample_weight, train, test, fit_intercept, path, path_params, alphas, l1_ratio, X_order, dtype = (None, 1, None, None)):
    """Returns the MSE for the models computed by 'path'.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        Training data.

    y : array-like of shape (n_samples,) or (n_samples, n_targets)
        Target values.

    sample_weight : None or array-like of shape (n_samples,)
        Sample weights.

    train : list of indices
        The indices of the train set.

    test : list of indices
        The indices of the test set.

    path : callable
        Function returning a list of models on the path. See
        enet_path for an example of signature.

    path_params : dictionary
        Parameters passed to the path function.

    alphas : array-like, default=None
        Array of float that is used for cross-validation. If not
        provided, computed using 'path'.

    l1_ratio : float, default=1
        float between 0 and 1 passed to ElasticNet (scaling between
        l1 and l2 penalties). For ``l1_ratio = 0`` the penalty is an
        L2 penalty. For ``l1_ratio = 1`` it is an L1 penalty. For ``0
        < l1_ratio < 1``, the penalty is a combination of L1 and L2.

    X_order : {'F', 'C'}, default=None
        The order of the arrays expected by the path function to
        avoid memory copies.

    dtype : a numpy dtype, default=None
        The dtype of the arrays expected by the path function to
        avoid memory copies.
    """
    X_train = X[train]
    y_train = y[train]
    X_test = X[test]
    y_test = y[test]
# WARNING: Decompyle incomplete


class LinearModelCV(ABC, LinearModel, MultiOutputMixin):
    pass
# WARNING: Decompyle incomplete


class LassoCV(LinearModelCV, RegressorMixin):
    pass
# WARNING: Decompyle incomplete


class ElasticNetCV(LinearModelCV, RegressorMixin):
    pass
# WARNING: Decompyle incomplete


class MultiTaskElasticNet(Lasso):
    pass
# WARNING: Decompyle incomplete


class MultiTaskLasso(MultiTaskElasticNet):
    __module__ = __name__
    __qualname__ = 'MultiTaskLasso'
    __doc__ = "Multi-task Lasso model trained with L1/L2 mixed-norm as regularizer.\n\n    The optimization objective for Lasso is::\n\n        (1 / (2 * n_samples)) * ||Y - XW||^2_Fro + alpha * ||W||_21\n\n    Where::\n\n        ||W||_21 = \\sum_i \\sqrt{\\sum_j w_{ij}^2}\n\n    i.e. the sum of norm of each row.\n\n    Read more in the :ref:`User Guide <multi_task_lasso>`.\n\n    Parameters\n    ----------\n    alpha : float, default=1.0\n        Constant that multiplies the L1/L2 term. Defaults to 1.0.\n\n    fit_intercept : bool, default=True\n        Whether to calculate the intercept for this model. If set\n        to false, no intercept will be used in calculations\n        (i.e. data is expected to be centered).\n\n    copy_X : bool, default=True\n        If ``True``, X will be copied; else, it may be overwritten.\n\n    max_iter : int, default=1000\n        The maximum number of iterations.\n\n    tol : float, default=1e-4\n        The tolerance for the optimization: if the updates are smaller or equal to\n        ``tol``, the optimization code checks the dual gap for optimality and continues\n        until it is smaller or equal to ``tol``.\n\n    warm_start : bool, default=False\n        When set to ``True``, reuse the solution of the previous call to fit as\n        initialization, otherwise, just erase the previous solution.\n        See :term:`the Glossary <warm_start>`.\n\n    random_state : int, RandomState instance, default=None\n        The seed of the pseudo random number generator that selects a random\n        feature to update. Used when ``selection`` == 'random'.\n        Pass an int for reproducible output across multiple function calls.\n        See :term:`Glossary <random_state>`.\n\n    selection : {'cyclic', 'random'}, default='cyclic'\n        If set to 'random', a random coefficient is updated every iteration\n        rather than looping over features sequentially by default. This\n        (setting to 'random') often leads to significantly faster convergence\n        especially when tol is higher than 1e-4.\n\n    Attributes\n    ----------\n    coef_ : ndarray of shape (n_targets, n_features)\n        Parameter vector (W in the cost function formula).\n        Note that ``coef_`` stores the transpose of ``W``, ``W.T``.\n\n    intercept_ : ndarray of shape (n_targets,)\n        Independent term in decision function.\n\n    n_iter_ : int\n        Number of iterations run by the coordinate descent solver to reach\n        the specified tolerance.\n\n    dual_gap_ : ndarray of shape (n_alphas,)\n        The dual gaps at the end of the optimization for each alpha.\n\n    eps_ : float\n        The tolerance scaled scaled by the variance of the target `y`.\n\n    sparse_coef_ : sparse matrix of shape (n_features,) or             (n_targets, n_features)\n        Sparse representation of the `coef_`.\n\n    n_features_in_ : int\n        Number of features seen during :term:`fit`.\n\n        .. versionadded:: 0.24\n\n    feature_names_in_ : ndarray of shape (`n_features_in_`,)\n        Names of features seen during :term:`fit`. Defined only when `X`\n        has feature names that are all strings.\n\n        .. versionadded:: 1.0\n\n    See Also\n    --------\n    Lasso: Linear Model trained with L1 prior as regularizer (aka the Lasso).\n    MultiTaskLassoCV: Multi-task L1 regularized linear model with built-in\n        cross-validation.\n    MultiTaskElasticNetCV: Multi-task L1/L2 ElasticNet with built-in cross-validation.\n\n    Notes\n    -----\n    The algorithm used to fit the model is coordinate descent.\n\n    To avoid unnecessary memory duplication the X and y arguments of the fit\n    method should be directly passed as Fortran-contiguous numpy arrays.\n\n    Examples\n    --------\n    >>> from sklearn import linear_model\n    >>> clf = linear_model.MultiTaskLasso(alpha=0.1)\n    >>> clf.fit([[0, 1], [1, 2], [2, 4]], [[0, 0], [1, 1], [2, 3]])\n    MultiTaskLasso(alpha=0.1)\n    >>> print(clf.coef_)\n    [[0.         0.60809415]\n    [0.         0.94592424]]\n    >>> print(clf.intercept_)\n    [-0.41888636 -0.87382323]\n    "
# WARNING: Decompyle incomplete


class MultiTaskElasticNetCV(LinearModelCV, RegressorMixin):
    pass
# WARNING: Decompyle incomplete


class MultiTaskLassoCV(LinearModelCV, RegressorMixin):
    pass
# WARNING: Decompyle incomplete
