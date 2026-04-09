# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _fastica.pyc (Python 3.11)

'''
Python implementation of the fast ICA algorithms.

Reference: Tables 8.3 and 8.4 page 196 in the book:
Independent Component Analysis, by  Hyvarinen et al.
'''
import warnings
from numbers import Integral, Real
import numpy as np
from scipy import linalg
from sklearn.base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin, _fit_context
from sklearn.exceptions import ConvergenceWarning
from sklearn.utils import as_float_array, check_array, check_random_state
from sklearn.utils._param_validation import Interval, Options, StrOptions, validate_params
from sklearn.utils.validation import check_is_fitted, validate_data
__all__ = [
    'FastICA',
    'fastica']

def _gs_decorrelation(w, W, j):
    '''
    Orthonormalize w wrt the first j rows of W.

    Parameters
    ----------
    w : ndarray of shape (n,)
        Array to be orthogonalized

    W : ndarray of shape (p, n)
        Null space definition

    j : int < p
        The no of (from the first) rows of Null space W wrt which w is
        orthogonalized.

    Notes
    -----
    Assumes that W is orthogonal
    w changed in place
    '''
    w -= np.linalg.multi_dot([
        w,
        W[:j].T,
        W[:j]])
    return w


def _sym_decorrelation(W):
    '''Symmetric decorrelation
    i.e. W <- (W * W.T) ^{-1/2} * W
    '''
    (s, u) = linalg.eigh(np.dot(W, W.T))
    s = np.clip(s, a_min = np.finfo(W.dtype).tiny, a_max = None)
    return np.linalg.multi_dot([
        u * (1 / np.sqrt(s)),
        u.T,
        W])


def _ica_def(X, tol, g, fun_args, max_iter, w_init):
    '''Deflationary FastICA using fun approx to neg-entropy function

    Used internally by FastICA.
    '''
    n_components = w_init.shape[0]
    W = np.zeros((n_components, n_components), dtype = X.dtype)
    n_iter = []
    for j in range(n_components):
        w = w_init[(j, :)].copy()
        w /= np.sqrt((w ** 2).sum())
        for i in range(max_iter):
            (gwtx, g_wtx) = g(np.dot(w.T, X), fun_args)
            w1 = (X * gwtx).mean(axis = 1) - g_wtx.mean() * w
            _gs_decorrelation(w1, W, j)
            w1 /= np.sqrt((w1 ** 2).sum())
            lim = np.abs(np.abs((w1 * w).sum()) - 1)
            w = w1
            if lim < tol:
                pass
            
            n_iter.append(i + 1)
            W[(j, :)] = w
            return (W, max(n_iter))


def _ica_par(X, tol, g, fun_args, max_iter, w_init):
    '''Parallel FastICA.

    Used internally by FastICA --main loop

    '''
    W = _sym_decorrelation(w_init)
    del w_init
    p_ = float(X.shape[1])
    for ii in range(max_iter):
        (gwtx, g_wtx) = g(np.dot(W, X), fun_args)
        W1 = _sym_decorrelation(np.dot(gwtx, X.T) / p_ - g_wtx[(:, np.newaxis)] * W)
        del gwtx
        del g_wtx
        lim = max(abs(abs(np.einsum('ij,ij->i', W1, W)) - 1))
        W = W1
        if lim < tol:
            pass
        
        warnings.warn('FastICA did not converge. Consider increasing tolerance or the maximum number of iterations.', ConvergenceWarning)
        return (W, ii + 1)


def _logcosh(x, fun_args = (None,)):
    alpha = fun_args.get('alpha', 1)
    x *= alpha
    gx = np.tanh(x, x)
    g_x = np.empty(x.shape[0], dtype = x.dtype)
    for i, gx_i in enumerate(gx):
        g_x[i] = (alpha * (1 - gx_i ** 2)).mean()
        return (gx, g_x)


def _exp(x, fun_args):
    exp = np.exp(-x ** 2 / 2)
    gx = x * exp
    g_x = (1 - x ** 2) * exp
    return (gx, g_x.mean(axis = -1))


def _cube(x, fun_args):
    return (x ** 3, (3 * x ** 2).mean(axis = -1))

fastica = (lambda X = validate_params({
    'X': [
        'array-like'],
    'return_X_mean': [
        'boolean'],
    'compute_sources': [
        'boolean'],
    'return_n_iter': [
        'boolean'] }, prefer_skip_nested_validation = False), n_components = (None,), *, algorithm, whiten: est = FastICA(n_components = n_components, algorithm = algorithm, whiten = whiten, fun = fun, fun_args = fun_args, max_iter = max_iter, tol = tol, w_init = w_init, whiten_solver = whiten_solver, random_state = random_state)est._validate_params()S = est._fit_transform(X, compute_sources = compute_sources)if est.whiten in ('unit-variance', 'arbitrary-variance'):
K = est.whitening_X_mean = est.mean_else:
K = NoneX_mean = Nonereturned_values = [
K,
est._unmixing,
S]if return_X_mean:
returned_values.append(X_mean)if return_n_iter:
returned_values.append(est.n_iter_)returned_values)()

class FastICA(BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin):
    pass
# WARNING: Decompyle incomplete
