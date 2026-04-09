# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: optimize.pyc (Python 3.11)

'''
Our own implementation of the Newton algorithm

Unlike the scipy.optimize version, this version of the Newton conjugate
gradient solver uses only one function call to retrieve the
func value, the gradient value and a callable for the Hessian matvec
product. If the function call is very expensive (e.g. for logistic
regression with large design matrix), this approach gives very
significant speedups.
'''
import warnings
import numpy as np
import scipy
from scipy.optimize._linesearch import line_search_wolfe1, line_search_wolfe2
from sklearn.exceptions import ConvergenceWarning

class _LineSearchError(RuntimeError):
    pass


def _line_search_wolfe12(f, fprime, xk, pk, gfk, old_fval, old_old_fval, verbose = (0,), **kwargs):
    '''
    Same as line_search_wolfe1, but fall back to line_search_wolfe2 if
    suitable step length is not found, and raise an exception if a
    suitable step length is not found.

    Raises
    ------
    _LineSearchError
        If no suitable step size is found.

    '''
    is_verbose = verbose >= 2
    eps = 16 * np.finfo(np.asarray(old_fval).dtype).eps
    if is_verbose:
        print('  Line Search')
        print(f'''    eps=16 * finfo.eps={eps}''')
        print('    try line search wolfe1')
# WARNING: Decompyle incomplete


def _cg(fhess_p, fgrad, maxiter, tol, verbose = (0,)):
    """
    Solve iteratively the linear system 'fhess_p . xsupi = fgrad'
    with a conjugate gradient descent.

    Parameters
    ----------
    fhess_p : callable
        Function that takes the gradient as a parameter and returns the
        matrix product of the Hessian and gradient.

    fgrad : ndarray of shape (n_features,) or (n_features + 1,)
        Gradient vector.

    maxiter : int
        Number of CG iterations.

    tol : float
        Stopping criterion.

    Returns
    -------
    xsupi : ndarray of shape (n_features,) or (n_features + 1,)
        Estimated solution.
    """
    eps = 16 * np.finfo(np.float64).eps
    xsupi = np.zeros(len(fgrad), dtype = fgrad.dtype)
    ri = np.copy(fgrad)
    psupi = -ri
    i = 0
    dri0 = np.dot(ri, ri)
    psupi_norm2 = dri0
    is_verbose = verbose >= 2
# WARNING: Decompyle incomplete


def _newton_cg(grad_hess, func, grad, x0, args, tol, maxiter, maxinner, line_search, warn, verbose = ((), 0.0001, 100, 200, True, True, 0)):
    """
    Minimization of scalar function of one or more variables using the
    Newton-CG algorithm.

    Parameters
    ----------
    grad_hess : callable
        Should return the gradient and a callable returning the matvec product
        of the Hessian.

    func : callable
        Should return the value of the function.

    grad : callable
        Should return the function value and the gradient. This is used
        by the linesearch functions.

    x0 : array of float
        Initial guess.

    args : tuple, default=()
        Arguments passed to func_grad_hess, func and grad.

    tol : float, default=1e-4
        Stopping criterion. The iteration will stop when
        ``max{|g_i | i = 1, ..., n} <= tol``
        where ``g_i`` is the i-th component of the gradient.

    maxiter : int, default=100
        Number of Newton iterations.

    maxinner : int, default=200
        Number of CG iterations.

    line_search : bool, default=True
        Whether to use a line search or not.

    warn : bool, default=True
        Whether to warn when didn't converge.

    Returns
    -------
    xk : ndarray of float
        Estimated minimum.
    """
    x0 = np.asarray(x0).flatten()
    xk = np.copy(x0)
    k = 0
# WARNING: Decompyle incomplete


def _check_optimize_result(solver, result, max_iter, extra_warning_msg = (None, None)):
    '''Check the OptimizeResult for successful convergence

    Parameters
    ----------
    solver : str
       Solver name. Currently only `lbfgs` is supported.

    result : OptimizeResult
       Result of the scipy.optimize.minimize function.

    max_iter : int, default=None
       Expected maximum number of iterations.

    extra_warning_msg : str, default=None
        Extra warning message.

    Returns
    -------
    n_iter : int
       Number of iterations.
    '''
    pass
# WARNING: Decompyle incomplete
