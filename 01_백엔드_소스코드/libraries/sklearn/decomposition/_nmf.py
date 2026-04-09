# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _nmf.pyc (Python 3.11)

'''Non-negative matrix factorization.'''
import itertools
import time
import warnings
from abc import ABC
from math import sqrt
from numbers import Integral, Real
import numpy as np
from scipy.sparse import sparse as sp
from scipy import linalg
from sklearn._config import config_context
from sklearn.base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin, _fit_context
from sklearn.decomposition._cdnmf_fast import _update_cdnmf_fast
from sklearn.exceptions import ConvergenceWarning
from sklearn.utils import check_array, check_random_state, gen_batches
from sklearn.utils._param_validation import Interval, StrOptions, validate_params
from sklearn.utils.extmath import _randomized_svd, safe_sparse_dot, squared_norm
from sklearn.utils.validation import check_is_fitted, check_non_negative, validate_data
EPSILON = np.finfo(np.float32).eps

def norm(x):
    '''Dot product-based Euclidean norm implementation.

    See: http://fa.bianp.net/blog/2011/computing-the-vector-norm/

    Parameters
    ----------
    x : array-like
        Vector for which to compute the norm.
    '''
    return sqrt(squared_norm(x))


def trace_dot(X, Y):
    '''Trace of np.dot(X, Y.T).

    Parameters
    ----------
    X : array-like
        First matrix.
    Y : array-like
        Second matrix.
    '''
    return np.dot(X.ravel(), Y.ravel())


def _check_init(A, shape, whom):
    A = check_array(A)
    if shape[0] != 'auto' and A.shape[0] != shape[0]:
        raise ValueError(f'''Array with wrong first dimension passed to {whom}. Expected {shape[0]}, but got {A.shape[0]}.''')
    if shape[1] != 'auto' and A.shape[1] != shape[1]:
        raise ValueError(f'''Array with wrong second dimension passed to {whom}. Expected {shape[1]}, but got {A.shape[1]}.''')
    check_non_negative(A, whom)
    if np.max(A) == 0:
        raise ValueError(f'''Array passed to {whom} is full of zeros.''')


def _beta_divergence(X, W, H, beta, square_root = (False,)):
    """Compute the beta-divergence of X and dot(W, H).

    Parameters
    ----------
    X : float or array-like of shape (n_samples, n_features)

    W : float or array-like of shape (n_samples, n_components)

    H : float or array-like of shape (n_components, n_features)

    beta : float or {'frobenius', 'kullback-leibler', 'itakura-saito'}
        Parameter of the beta-divergence.
        If beta == 2, this is half the Frobenius *squared* norm.
        If beta == 1, this is the generalized Kullback-Leibler divergence.
        If beta == 0, this is the Itakura-Saito divergence.
        Else, this is the general beta-divergence.

    square_root : bool, default=False
        If True, return np.sqrt(2 * res)
        For beta == 2, it corresponds to the Frobenius norm.

    Returns
    -------
        res : float
            Beta divergence of X and np.dot(X, H).
    """
    beta = _beta_loss_to_float(beta)
    if not sp.issparse(X):
        X = np.atleast_2d(X)
    W = np.atleast_2d(W)
    H = np.atleast_2d(H)
    if beta == 2:
        if sp.issparse(X):
            norm_X = np.dot(X.data, X.data)
            norm_WH = trace_dot(np.linalg.multi_dot([
                W.T,
                W,
                H]), H)
            cross_prod = trace_dot(X @ H.T, W)
            res = (norm_X + norm_WH - 2 * cross_prod) / 2
        else:
            res = squared_norm(X - np.dot(W, H)) / 2
        if square_root:
            return np.sqrt(res * 2)
        return None
    if None.issparse(X):
        WH_data = _special_sparse_dot(W, H, X).data
        X_data = X.data
    else:
        WH = np.dot(W, H)
        WH_data = WH.ravel()
        X_data = X.ravel()
    indices = X_data > EPSILON
    WH_data = WH_data[indices]
    X_data = X_data[indices]
    WH_data[WH_data < EPSILON] = EPSILON
    if beta == 1:
        sum_WH = np.dot(np.sum(W, axis = 0), np.sum(H, axis = 1))
        div = X_data / WH_data
        res = np.dot(X_data, np.log(div))
        res += sum_WH - X_data.sum()
    elif beta == 0:
        div = X_data / WH_data
        res = np.sum(div) - np.prod(X.shape) - np.sum(np.log(div))
    elif sp.issparse(X):
        sum_WH_beta = 0
        for i in range(X.shape[1]):
            sum_WH_beta += np.sum(np.dot(W, H[(:, i)]) ** beta)
    sum_WH_beta = np.sum(WH ** beta)
    sum_X_WH = np.dot(X_data, WH_data ** (beta - 1))
    res = (X_data ** beta).sum() - beta * sum_X_WH
    res += sum_WH_beta * (beta - 1)
    res /= beta * (beta - 1)
    if square_root:
        res = max(res, 0)
        return np.sqrt(2 * res)


def _special_sparse_dot(W, H, X):
    '''Computes np.dot(W, H), only where X is non zero.'''
    if sp.issparse(X):
        (ii, jj) = X.nonzero()
        n_vals = ii.shape[0]
        dot_vals = np.empty(n_vals)
        n_components = W.shape[1]
        batch_size = max(n_components, n_vals // n_components)
        for start in range(0, n_vals, batch_size):
            batch = slice(start, start + batch_size)
            dot_vals[batch] = np.multiply(W[(ii[batch], :)], H.T[(jj[batch], :)]).sum(axis = 1)
            WH = sp.coo_matrix((dot_vals, (ii, jj)), shape = X.shape)
            return WH.tocsr()
            return np.dot(W, H)


def _beta_loss_to_float(beta_loss):
    '''Convert string beta_loss to float.'''
    beta_loss_map = {
        'frobenius': 2,
        'kullback-leibler': 1,
        'itakura-saito': 0 }
    if isinstance(beta_loss, str):
        beta_loss = beta_loss_map[beta_loss]
    return beta_loss


def _initialize_nmf(X, n_components, init, eps, random_state = (None, 1e-06, None)):
    """Algorithms for NMF initialization.

    Computes an initial guess for the non-negative
    rank k matrix approximation for X: X = WH.

    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        The data matrix to be decomposed.

    n_components : int
        The number of components desired in the approximation.

    init :  {'random', 'nndsvd', 'nndsvda', 'nndsvdar'}, default=None
        Method used to initialize the procedure.
        Valid options:

        - None: 'nndsvda' if n_components <= min(n_samples, n_features),
            otherwise 'random'.

        - 'random': non-negative random matrices, scaled with:
            sqrt(X.mean() / n_components)

        - 'nndsvd': Nonnegative Double Singular Value Decomposition (NNDSVD)
            initialization (better for sparseness)

        - 'nndsvda': NNDSVD with zeros filled with the average of X
            (better when sparsity is not desired)

        - 'nndsvdar': NNDSVD with zeros filled with small random values
            (generally faster, less accurate alternative to NNDSVDa
            for when sparsity is not desired)

        - 'custom': use custom matrices W and H

        .. versionchanged:: 1.1
            When `init=None` and n_components is less than n_samples and n_features
            defaults to `nndsvda` instead of `nndsvd`.

    eps : float, default=1e-6
        Truncate all values less then this in output to zero.

    random_state : int, RandomState instance or None, default=None
        Used when ``init`` == 'nndsvdar' or 'random'. Pass an int for
        reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    Returns
    -------
    W : array-like of shape (n_samples, n_components)
        Initial guesses for solving X ~= WH.

    H : array-like of shape (n_components, n_features)
        Initial guesses for solving X ~= WH.

    References
    ----------
    C. Boutsidis, E. Gallopoulos: SVD based initialization: A head start for
    nonnegative matrix factorization - Pattern Recognition, 2008
    http://tinyurl.com/nndsvd
    """
    check_non_negative(X, 'NMF initialization')
    (n_samples, n_features) = X.shape
# WARNING: Decompyle incomplete


def _update_coordinate_descent(X, W, Ht, l1_reg, l2_reg, shuffle, random_state):
    '''Helper function for _fit_coordinate_descent.

    Update W to minimize the objective function, iterating once over all
    coordinates. By symmetry, to update H, one can call
    _update_coordinate_descent(X.T, Ht, W, ...).

    '''
    n_components = Ht.shape[1]
    HHt = np.dot(Ht.T, Ht)
    XHt = safe_sparse_dot(X, Ht)
    if l2_reg != 0:
        pass
    if l1_reg != 0:
        XHt -= l1_reg = None
    if shuffle:
        permutation = random_state.permutation(n_components)
    else:
        permutation = np.arange(n_components)
    permutation = np.asarray(permutation, dtype = np.intp)
    return _update_cdnmf_fast(W, HHt, XHt, permutation)


def _fit_coordinate_descent(X, W, H, tol, max_iter, l1_reg_W, l1_reg_H, l2_reg_W, l2_reg_H, update_H, verbose, shuffle, random_state = (0.0001, 200, 0, 0, 0, 0, True, 0, False, None)):
    '''Compute Non-negative Matrix Factorization (NMF) with Coordinate Descent

    The objective function is minimized with an alternating minimization of W
    and H. Each minimization is done with a cyclic (up to a permutation of the
    features) Coordinate Descent.

    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        Constant matrix.

    W : array-like of shape (n_samples, n_components)
        Initial guess for the solution.

    H : array-like of shape (n_components, n_features)
        Initial guess for the solution.

    tol : float, default=1e-4
        Tolerance of the stopping condition.

    max_iter : int, default=200
        Maximum number of iterations before timing out.

    l1_reg_W : float, default=0.
        L1 regularization parameter for W.

    l1_reg_H : float, default=0.
        L1 regularization parameter for H.

    l2_reg_W : float, default=0.
        L2 regularization parameter for W.

    l2_reg_H : float, default=0.
        L2 regularization parameter for H.

    update_H : bool, default=True
        Set to True, both W and H will be estimated from initial guesses.
        Set to False, only W will be estimated.

    verbose : int, default=0
        The verbosity level.

    shuffle : bool, default=False
        If true, randomize the order of coordinates in the CD solver.

    random_state : int, RandomState instance or None, default=None
        Used to randomize the coordinates in the CD solver, when
        ``shuffle`` is set to ``True``. Pass an int for reproducible
        results across multiple function calls.
        See :term:`Glossary <random_state>`.

    Returns
    -------
    W : ndarray of shape (n_samples, n_components)
        Solution to the non-negative least squares problem.

    H : ndarray of shape (n_components, n_features)
        Solution to the non-negative least squares problem.

    n_iter : int
        The number of iterations done by the algorithm.

    References
    ----------
    .. [1] :doi:`"Fast local algorithms for large scale nonnegative matrix and tensor
       factorizations" <10.1587/transfun.E92.A.708>`
       Cichocki, Andrzej, and P. H. A. N. Anh-Huy. IEICE transactions on fundamentals
       of electronics, communications and computer sciences 92.3: 708-721, 2009.
    '''
    Ht = check_array(H.T, order = 'C')
    X = check_array(X, accept_sparse = 'csr')
    rng = check_random_state(random_state)
    for n_iter in range(1, max_iter + 1):
        violation = 0
        violation += _update_coordinate_descent(X, W, Ht, l1_reg_W, l2_reg_W, shuffle, rng)
        if update_H:
            violation += _update_coordinate_descent(X.T, Ht, W, l1_reg_H, l2_reg_H, shuffle, rng)
        if n_iter == 1:
            violation_init = violation
        if violation_init == 0:
            pass
        elif verbose:
            print('violation:', violation / violation_init)
        if violation / violation_init <= tol:
            if verbose:
                print('Converged at iteration', n_iter + 1)
        
        return (W, Ht.T, n_iter)


def _multiplicative_update_w(X, W, H, beta_loss, l1_reg_W, l2_reg_W, gamma, H_sum, HHt, XHt, update_H = (None, None, None, True)):
    '''Update W in Multiplicative Update NMF.'''
    pass
# WARNING: Decompyle incomplete


def _multiplicative_update_h(X, W, H, beta_loss, l1_reg_H, l2_reg_H, gamma, A, B, rho = (None, None, None)):
    '''update H in Multiplicative Update NMF.'''
    if beta_loss == 2:
        numerator = safe_sparse_dot(W.T, X)
        denominator = np.linalg.multi_dot([
            W.T,
            W,
            H])
    else:
        WH_safe_X = _special_sparse_dot(W, H, X)
        if sp.issparse(X):
            WH_safe_X_data = WH_safe_X.data
            X_data = X.data
        else:
            WH_safe_X_data = WH_safe_X
            X_data = X
            WH = WH_safe_X.copy()
            if beta_loss - 1 < 0:
                WH[WH < EPSILON] = EPSILON
        if beta_loss - 2 < 0:
            WH_safe_X_data[WH_safe_X_data < EPSILON] = EPSILON
        if beta_loss == 1:
            np.divide(X_data, WH_safe_X_data, out = WH_safe_X_data)
        elif beta_loss == 0:
            WH_safe_X_data **= -1
            WH_safe_X_data **= 2
            WH_safe_X_data *= X_data
        else:
            WH_safe_X_data **= beta_loss - 2
            WH_safe_X_data *= X_data
        numerator = safe_sparse_dot(W.T, WH_safe_X)
        if beta_loss == 1:
            W_sum = np.sum(W, axis = 0)
            W_sum[W_sum == 0] = 1
            denominator = W_sum[(:, np.newaxis)]
        elif sp.issparse(X):
            WtWH = np.empty(H.shape)
            for i in range(X.shape[1]):
                WHi = np.dot(W, H[(:, i)])
                if beta_loss - 1 < 0:
                    WHi[WHi < EPSILON] = EPSILON
                WHi **= beta_loss - 1
                WtWH[(:, i)] = np.dot(W.T, WHi)
        WH **= beta_loss - 1
        WtWH = np.dot(W.T, WH)
        denominator = WtWH
    if l1_reg_H > 0:
        denominator += l1_reg_H
    if l2_reg_H > 0:
        denominator = denominator + l2_reg_H * H
    denominator[denominator == 0] = EPSILON
# WARNING: Decompyle incomplete


def _fit_multiplicative_update(X, W, H, beta_loss, max_iter, tol, l1_reg_W, l1_reg_H, l2_reg_W, l2_reg_H, update_H, verbose = ('frobenius', 200, 0.0001, 0, 0, 0, 0, True, 0)):
    """Compute Non-negative Matrix Factorization with Multiplicative Update.

    The objective function is _beta_divergence(X, WH) and is minimized with an
    alternating minimization of W and H. Each minimization is done with a
    Multiplicative Update.

    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        Constant input matrix.

    W : array-like of shape (n_samples, n_components)
        Initial guess for the solution.

    H : array-like of shape (n_components, n_features)
        Initial guess for the solution.

    beta_loss : float or {'frobenius', 'kullback-leibler',             'itakura-saito'}, default='frobenius'
        String must be in {'frobenius', 'kullback-leibler', 'itakura-saito'}.
        Beta divergence to be minimized, measuring the distance between X
        and the dot product WH. Note that values different from 'frobenius'
        (or 2) and 'kullback-leibler' (or 1) lead to significantly slower
        fits. Note that for beta_loss <= 0 (or 'itakura-saito'), the input
        matrix X cannot contain zeros.

    max_iter : int, default=200
        Number of iterations.

    tol : float, default=1e-4
        Tolerance of the stopping condition.

    l1_reg_W : float, default=0.
        L1 regularization parameter for W.

    l1_reg_H : float, default=0.
        L1 regularization parameter for H.

    l2_reg_W : float, default=0.
        L2 regularization parameter for W.

    l2_reg_H : float, default=0.
        L2 regularization parameter for H.

    update_H : bool, default=True
        Set to True, both W and H will be estimated from initial guesses.
        Set to False, only W will be estimated.

    verbose : int, default=0
        The verbosity level.

    Returns
    -------
    W : ndarray of shape (n_samples, n_components)
        Solution to the non-negative least squares problem.

    H : ndarray of shape (n_components, n_features)
        Solution to the non-negative least squares problem.

    n_iter : int
        The number of iterations done by the algorithm.

    References
    ----------
    Lee, D. D., & Seung, H., S. (2001). Algorithms for Non-negative Matrix
    Factorization. Adv. Neural Inform. Process. Syst.. 13.
    Fevotte, C., & Idier, J. (2011). Algorithms for nonnegative matrix
    factorization with the beta-divergence. Neural Computation, 23(9).
    """
    start_time = time.time()
    beta_loss = _beta_loss_to_float(beta_loss)
    if beta_loss < 1:
        gamma = 1 / (2 - beta_loss)
    elif beta_loss > 2:
        gamma = 1 / (beta_loss - 1)
    else:
        gamma = 1
    error_at_init = _beta_divergence(X, W, H, beta_loss, square_root = True)
    previous_error = error_at_init
    (H_sum, HHt, XHt) = (None, None, None)
    for n_iter in range(1, max_iter + 1):
        (W, H_sum, HHt, XHt) = _multiplicative_update_w(X, W, H, beta_loss = beta_loss, l1_reg_W = l1_reg_W, l2_reg_W = l2_reg_W, gamma = gamma, H_sum = H_sum, HHt = HHt, XHt = XHt, update_H = update_H)
        if beta_loss < 1:
            W[W < np.finfo(np.float64).eps] = 0
        if update_H:
            H = _multiplicative_update_h(X, W, H, beta_loss = beta_loss, l1_reg_H = l1_reg_H, l2_reg_H = l2_reg_H, gamma = gamma)
            (H_sum, HHt, XHt) = (None, None, None)
            if beta_loss <= 1:
                H[H < np.finfo(np.float64).eps] = 0
        if tol > 0 and n_iter % 10 == 0:
            error = _beta_divergence(X, W, H, beta_loss, square_root = True)
            if verbose:
                iter_time = time.time()
                print('Epoch %02d reached after %.3f seconds, error: %f' % (n_iter, iter_time - start_time, error))
            if (previous_error - error) / error_at_init < tol:
                pass
            else:
                previous_error = error
            if verbose:
                if tol == 0 or n_iter % 10 != 0:
                    end_time = time.time()
                    print('Epoch %02d reached after %.3f seconds.' % (n_iter, end_time - start_time))
    return (W, H, n_iter)

non_negative_factorization = (lambda X, W = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'W': [
        'array-like',
        None],
    'H': [
        'array-like',
        None],
    'update_H': [
        'boolean'] }, prefer_skip_nested_validation = False), H = (None, None, 'auto'), n_components = {
    'init': None,
    'update_H': True,
    'solver': 'cd',
    'beta_loss': 'frobenius',
    'tol': 0.0001,
    'max_iter': 200,
    'alpha_W': 0,
    'alpha_H': 'same',
    'l1_ratio': 0,
    'random_state': None,
    'verbose': 0,
    'shuffle': False }, *, init, update_H, solver, beta_loss: est = NMF(n_components = n_components, init = init, solver = solver, beta_loss = beta_loss, tol = tol, max_iter = max_iter, random_state = random_state, alpha_W = alpha_W, alpha_H = alpha_H, l1_ratio = l1_ratio, verbose = verbose, shuffle = shuffle)est._validate_params()X = check_array(X, accept_sparse = ('csr', 'csc'), dtype = [
np.float64,
np.float32])config_context(assume_finite = True)(W, H, n_iter) = est._fit_transform(X, W = W, H = H, update_H = update_H)None(None, None))()

class _BaseNMF(ABC, BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin):
    pass
# WARNING: Decompyle incomplete


class NMF(_BaseNMF):
    pass
# WARNING: Decompyle incomplete


class MiniBatchNMF(_BaseNMF):
    pass
# WARNING: Decompyle incomplete
