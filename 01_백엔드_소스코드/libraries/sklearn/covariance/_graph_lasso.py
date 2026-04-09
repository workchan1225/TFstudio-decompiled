# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _graph_lasso.pyc (Python 3.11)

'''GraphicalLasso: sparse inverse covariance estimation with an l1-penalized
estimator.
'''
import operator
import sys
import time
import warnings
from numbers import Integral, Real
import numpy as np
from scipy import linalg
from sklearn.base import _fit_context
from sklearn.covariance import EmpiricalCovariance, empirical_covariance, log_likelihood
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import _cd_fast as cd_fast
from sklearn.linear_model import lars_path_gram
from sklearn.model_selection import check_cv, cross_val_score
from sklearn.utils import Bunch
from sklearn.utils._param_validation import Interval, StrOptions, validate_params
from sklearn.utils.metadata_routing import MetadataRouter, MethodMapping, _raise_for_params, _routing_enabled, process_routing
from sklearn.utils.parallel import Parallel, delayed
from sklearn.utils.validation import _is_arraylike_not_scalar, check_random_state, check_scalar, validate_data

def _objective(mle, precision_, alpha):
    '''Evaluation of the graphical-lasso objective function

    the objective function is made of a shifted scaled version of the
    normalized log-likelihood (i.e. its empirical mean over the samples) and a
    penalisation term to promote sparsity
    '''
    p = precision_.shape[0]
    cost = -2 * log_likelihood(mle, precision_) + p * np.log(2 * np.pi)
    cost += alpha * (np.abs(precision_).sum() - np.abs(np.diag(precision_)).sum())
    return cost


def _dual_gap(emp_cov, precision_, alpha):
    '''Expression of the dual gap convergence criterion

    The specific definition is given in Duchi "Projected Subgradient Methods
    for Learning Sparse Gaussians".
    '''
    gap = np.sum(emp_cov * precision_)
    gap -= precision_.shape[0]
    gap += alpha * (np.abs(precision_).sum() - np.abs(np.diag(precision_)).sum())
    return gap


def _graphical_lasso(emp_cov = None, alpha = {
    'cov_init': None,
    'mode': 'cd',
    'tol': 0.0001,
    'enet_tol': 0.0001,
    'max_iter': 100,
    'verbose': False,
    'eps': np.finfo(np.float64).eps }, *, cov_init, mode, tol, enet_tol, max_iter, verbose, eps):
    (_, n_features) = emp_cov.shape
    if alpha == 0:
        precision_ = linalg.inv(emp_cov)
        cost = -2 * log_likelihood(emp_cov, precision_)
        cost += n_features * np.log(2 * np.pi)
        d_gap = np.sum(emp_cov * precision_) - n_features
        return (emp_cov, precision_, (cost, d_gap), 0)
# WARNING: Decompyle incomplete


def alpha_max(emp_cov):
    '''Find the maximum alpha for which there are some non-zeros off-diagonal.

    Parameters
    ----------
    emp_cov : ndarray of shape (n_features, n_features)
        The sample covariance matrix.

    Notes
    -----
    This results from the bound for the all the Lasso that are solved
    in GraphicalLasso: each time, the row of cov corresponds to Xy. As the
    bound for alpha is given by `max(abs(Xy))`, the result follows.
    '''
    A = np.copy(emp_cov)
    A.flat[::A.shape[0] + 1] = 0
    return np.max(np.abs(A))

graphical_lasso = (lambda emp_cov = validate_params({
    'emp_cov': [
        'array-like'],
    'return_costs': [
        'boolean'],
    'return_n_iter': [
        'boolean'] }, prefer_skip_nested_validation = False), alpha = {
    'mode': 'cd',
    'tol': 0.0001,
    'enet_tol': 0.0001,
    'max_iter': 100,
    'verbose': False,
    'return_costs': False,
    'eps': np.finfo(np.float64).eps,
    'return_n_iter': False }, *, mode, tol: model = GraphicalLasso(alpha = alpha, mode = mode, covariance = 'precomputed', tol = tol, enet_tol = enet_tol, max_iter = max_iter, verbose = verbose, eps = eps, assume_centered = True).fit(emp_cov)output = [
model.covariance_,
model.precision_]if return_costs:
output.append(model.costs_)if return_n_iter:
output.append(model.n_iter_)tuple(output))()

class BaseGraphicalLasso(EmpiricalCovariance):
    pass
# WARNING: Decompyle incomplete


class GraphicalLasso(BaseGraphicalLasso):
    pass
# WARNING: Decompyle incomplete


def graphical_lasso_path(X, alphas, cov_init, X_test, mode, tol, enet_tol, max_iter, verbose, eps = (None, None, 'cd', 0.0001, 0.0001, 100, False, np.finfo(np.float64).eps)):
    """l1-penalized covariance estimator along a path of decreasing alphas

    Read more in the :ref:`User Guide <sparse_inverse_covariance>`.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        Data from which to compute the covariance estimate.

    alphas : array-like of shape (n_alphas,)
        The list of regularization parameters, decreasing order.

    cov_init : array of shape (n_features, n_features), default=None
        The initial guess for the covariance.

    X_test : array of shape (n_test_samples, n_features), default=None
        Optional test matrix to measure generalisation error.

    mode : {'cd', 'lars'}, default='cd'
        The Lasso solver to use: coordinate descent or LARS. Use LARS for
        very sparse underlying graphs, where p > n. Elsewhere prefer cd
        which is more numerically stable.

    tol : float, default=1e-4
        The tolerance to declare convergence: if the dual gap goes below
        this value, iterations are stopped. The tolerance must be a positive
        number.

    enet_tol : float, default=1e-4
        The tolerance for the elastic net solver used to calculate the descent
        direction. This parameter controls the accuracy of the search direction
        for a given column update, not of the overall parameter estimate. Only
        used for mode='cd'. The tolerance must be a positive number.

    max_iter : int, default=100
        The maximum number of iterations. This parameter should be a strictly
        positive integer.

    verbose : int or bool, default=False
        The higher the verbosity flag, the more information is printed
        during the fitting.

    eps : float, default=eps
        The machine-precision regularization in the computation of the
        Cholesky diagonal factors. Increase this for very ill-conditioned
        systems. Default is `np.finfo(np.float64).eps`.

        .. versionadded:: 1.3

    Returns
    -------
    covariances_ : list of shape (n_alphas,) of ndarray of shape             (n_features, n_features)
        The estimated covariance matrices.

    precisions_ : list of shape (n_alphas,) of ndarray of shape             (n_features, n_features)
        The estimated (sparse) precision matrices.

    scores_ : list of shape (n_alphas,), dtype=float
        The generalisation error (log-likelihood) on the test data.
        Returned only if test data is passed.
    """
    inner_verbose = max(0, verbose - 1)
    emp_cov = empirical_covariance(X)
# WARNING: Decompyle incomplete


class GraphicalLassoCV(BaseGraphicalLasso):
    pass
# WARNING: Decompyle incomplete
