# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _ridge.pyc (Python 3.11)

'''
Ridge regression
'''
import numbers
import warnings
from abc import ABCMeta, abstractmethod
from functools import partial
from numbers import Integral, Real
import numpy as np
from scipy import linalg, optimize, sparse
from scipy.sparse import linalg as sp_linalg
from sklearn.base import BaseEstimator, MultiOutputMixin, RegressorMixin, _fit_context, is_classifier
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model._base import LinearClassifierMixin, LinearModel, _preprocess_data, _rescale_data
from sklearn.linear_model._sag import sag_solver
from sklearn.metrics import check_scoring, get_scorer, get_scorer_names
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import LabelBinarizer
from sklearn.utils import Bunch, check_array, check_consistent_length, check_scalar, column_or_1d, compute_sample_weight
from sklearn.utils._array_api import _is_numpy_namespace, _max_precision_float_dtype, _ravel, device, get_namespace, get_namespace_and_device, move_to
from sklearn.utils._param_validation import Interval, StrOptions, validate_params
from sklearn.utils.extmath import row_norms, safe_sparse_dot
from sklearn.utils.fixes import _sparse_linalg_cg
from sklearn.utils.metadata_routing import MetadataRouter, MethodMapping, _raise_for_params, _routing_enabled, process_routing
from sklearn.utils.sparsefuncs import mean_variance_axis
from sklearn.utils.validation import _check_sample_weight, check_is_fitted, validate_data

def _get_rescaled_operator(X, X_offset, sample_weight_sqrt):
    '''Create LinearOperator for matrix products with implicit centering.

    Matrix product `LinearOperator @ coef` returns `(X - X_offset) @ coef`.
    '''
    pass
# WARNING: Decompyle incomplete


def _solve_sparse_cg(X, y, alpha, max_iter, tol, verbose, X_offset, X_scale, sample_weight_sqrt = (None, 0.0001, 0, None, None, None)):
    pass
# WARNING: Decompyle incomplete


def _solve_lsqr(X = None, y = {
    'fit_intercept': True,
    'max_iter': None,
    'tol': 0.0001,
    'X_offset': None,
    'X_scale': None,
    'sample_weight_sqrt': None }, *, alpha, fit_intercept, max_iter, tol, X_offset, X_scale, sample_weight_sqrt):
    '''Solve Ridge regression via LSQR.

    We expect that y is always mean centered.
    If X is dense, we expect it to be mean centered such that we can solve
        ||y - Xw||_2^2 + alpha * ||w||_2^2

    If X is sparse, we expect X_offset to be given such that we can solve
        ||y - (X - X_offset)w||_2^2 + alpha * ||w||_2^2

    With sample weights S=diag(sample_weight), this becomes
        ||sqrt(S) (y - (X - X_offset) w)||_2^2 + alpha * ||w||_2^2
    and we expect y and X to already be rescaled, i.e. sqrt(S) @ y, sqrt(S) @ X. In
    this case, X_offset is the sample_weight weighted mean of X before scaling by
    sqrt(S). The objective then reads
       ||y - (X - sqrt(S) X_offset) w)||_2^2 + alpha * ||w||_2^2
    '''
    pass
# WARNING: Decompyle incomplete


def _solve_cholesky(X, y, alpha):
    n_features = X.shape[1]
    n_targets = y.shape[1]
    A = safe_sparse_dot(X.T, X, dense_output = True)
    Xy = safe_sparse_dot(X.T, y, dense_output = True)
    one_alpha = np.array_equal(alpha, len(alpha) * [
        alpha[0]])
    if one_alpha:
        return linalg.solve(A, Xy, assume_a = 'pos', overwrite_a = True).T
    None.empty([
        n_targets,
        n_features], dtype = X.dtype) = None
    for coef, target, current_alpha in zip(coefs, Xy.T, alpha):
        linalg.solve(A, target, assume_a = 'pos', overwrite_a = False).ravel() = None
        return coefs


def _solve_cholesky_kernel(K, y, alpha, sample_weight, copy = (None, False)):
    n_samples = K.shape[0]
    n_targets = y.shape[1]
    if copy:
        K = K.copy()
    alpha = np.atleast_1d(alpha)
    one_alpha = (alpha == alpha[0]).all()
    if not isinstance(sample_weight, np.ndarray):
        has_sw = sample_weight not in (1, None)
        if has_sw:
            sw = np.sqrt(np.atleast_1d(sample_weight))
            y = y * sw[(:, np.newaxis)]
            K *= np.outer(sw, sw)
    if one_alpha:
        
        try:
            linalg.solve(K, y, assume_a = 'pos', overwrite_a = False) = None
        except np.linalg.LinAlgError:
            warnings.warn('Singular matrix in solving dual problem. Using least-squares solution instead.')
            dual_coef = linalg.lstsq(K, y)[0]

        if has_sw:
            dual_coef *= sw[(:, np.newaxis)] = None
        return dual_coef
    dual_coefs = np.empty([
        n_targets,
        n_samples], K.dtype)
    for dual_coef, target, current_alpha in zip(dual_coefs, y.T, alpha):
        linalg.solve(K, target, assume_a = 'pos', overwrite_a = False).ravel() = None
        if has_sw:
            dual_coefs *= sw[(np.newaxis, :)] = None
    return dual_coefs.T


def _solve_svd(X, y, alpha, xp = (None,)):
    (xp, _) = get_namespace(X, xp = xp)
    (U, s, Vt) = xp.linalg.svd(X, full_matrices = False)
    idx = s > 1e-15
    s_nnz = s[idx][(:, None)]
    UTy = U.T @ y
    d = xp.zeros((s.shape[0], alpha.shape[0]), dtype = X.dtype, device = device(X))
    d[idx] = s_nnz / (s_nnz ** 2 + alpha)
    d_UT_y = d * UTy
    return (Vt.T @ d_UT_y).T


def _solve_lbfgs(X, y, alpha, positive, max_iter, tol, X_offset, X_scale, sample_weight_sqrt = (True, None, 0.0001, None, None, None)):
    '''Solve ridge regression with LBFGS.

    The main purpose is fitting with forcing coefficients to be positive.
    For unconstrained ridge regression, there are faster dedicated solver methods.
    Note that with positive bounds on the coefficients, LBFGS seems faster
    than scipy.optimize.lsq_linear.
    '''
    pass
# WARNING: Decompyle incomplete


def _get_valid_accept_sparse(is_X_sparse, solver):
