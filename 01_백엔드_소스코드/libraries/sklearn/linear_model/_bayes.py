# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _bayes.pyc (Python 3.11)

'''
Various bayesian regression
'''
from math import log
from numbers import Integral, Real
import numpy as np
from scipy import linalg
from scipy.linalg import pinvh
from sklearn.base import RegressorMixin, _fit_context
from sklearn.linear_model._base import LinearModel, _preprocess_data
from sklearn.utils import _safe_indexing
from sklearn.utils._param_validation import Interval
from sklearn.utils.extmath import fast_logdet
from sklearn.utils.validation import _check_sample_weight, validate_data

class BayesianRidge(LinearModel, RegressorMixin):
    '''Bayesian ridge regression.

    Fit a Bayesian ridge model. See the Notes section for details on this
    implementation and the optimization of the regularization parameters
    lambda (precision of the weights) and alpha (precision of the noise).

    Read more in the :ref:`User Guide <bayesian_regression>`.
    For an intuitive visualization of how the sinusoid is approximated by
    a polynomial using different pairs of initial values, see
    :ref:`sphx_glr_auto_examples_linear_model_plot_bayesian_ridge_curvefit.py`.

    Parameters
    ----------
    max_iter : int, default=300
        Maximum number of iterations over the complete dataset before
        stopping independently of any early stopping criterion.

        .. versionchanged:: 1.3

    tol : float, default=1e-3
        Stop the algorithm if w has converged.

    alpha_1 : float, default=1e-6
        Hyper-parameter : shape parameter for the Gamma distribution prior
        over the alpha parameter.

    alpha_2 : float, default=1e-6
        Hyper-parameter : inverse scale parameter (rate parameter) for the
        Gamma distribution prior over the alpha parameter.

    lambda_1 : float, default=1e-6
        Hyper-parameter : shape parameter for the Gamma distribution prior
        over the lambda parameter.

    lambda_2 : float, default=1e-6
        Hyper-parameter : inverse scale parameter (rate parameter) for the
        Gamma distribution prior over the lambda parameter.

    alpha_init : float, default=None
        Initial value for alpha (precision of the noise).
        If not set, alpha_init is 1/Var(y).

        .. versionadded:: 0.22

    lambda_init : float, default=None
        Initial value for lambda (precision of the weights).
        If not set, lambda_init is 1.

        .. versionadded:: 0.22

    compute_score : bool, default=False
        If True, compute the log marginal likelihood at each iteration of the
        optimization.

    fit_intercept : bool, default=True
        Whether to calculate the intercept for this model.
        The intercept is not treated as a probabilistic parameter
        and thus has no associated variance. If set
        to False, no intercept will be used in calculations
        (i.e. data is expected to be centered).

    copy_X : bool, default=True
        If True, X will be copied; else, it may be overwritten.

    verbose : bool, default=False
        Verbose mode when fitting the model.

    Attributes
    ----------
    coef_ : array-like of shape (n_features,)
        Coefficients of the regression model (mean of distribution)

    intercept_ : float
        Independent term in decision function. Set to 0.0 if
        `fit_intercept = False`.

    alpha_ : float
       Estimated precision of the noise.

    lambda_ : float
       Estimated precision of the weights.

    sigma_ : array-like of shape (n_features, n_features)
        Estimated variance-covariance matrix of the weights

    scores_ : array-like of shape (n_iter_+1,)
        If computed_score is True, value of the log marginal likelihood (to be
        maximized) at each iteration of the optimization. The array starts
        with the value of the log marginal likelihood obtained for the initial
        values of alpha and lambda and ends with the value obtained for the
        estimated alpha and lambda.

    n_iter_ : int
        The actual number of iterations to reach the stopping criterion.

    X_offset_ : ndarray of shape (n_features,)
        If `fit_intercept=True`, offset subtracted for centering data to a
        zero mean. Set to np.zeros(n_features) otherwise.

    X_scale_ : ndarray of shape (n_features,)
        Set to np.ones(n_features).

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    ARDRegression : Bayesian ARD regression.

    Notes
    -----
    There exist several strategies to perform Bayesian ridge regression. This
    implementation is based on the algorithm described in Appendix A of
    (Tipping, 2001) where updates of the regularization parameters are done as
    suggested in (MacKay, 1992). Note that according to A New
    View of Automatic Relevance Determination (Wipf and Nagarajan, 2008) these
    update rules do not guarantee that the marginal likelihood is increasing
    between two consecutive iterations of the optimization.

    References
    ----------
    D. J. C. MacKay, Bayesian Interpolation, Computation and Neural Systems,
    Vol. 4, No. 3, 1992.

    M. E. Tipping, Sparse Bayesian Learning and the Relevance Vector Machine,
    Journal of Machine Learning Research, Vol. 1, 2001.

    Examples
    --------
    >>> from sklearn import linear_model
    >>> clf = linear_model.BayesianRidge()
    >>> clf.fit([[0,0], [1, 1], [2, 2]], [0, 1, 2])
    BayesianRidge()
    >>> clf.predict([[1, 1]])
    array([1.])
    '''
    _parameter_constraints: dict = {
        'max_iter': [
            Interval(Integral, 1, None, closed = 'left')],
        'tol': [
            Interval(Real, 0, None, closed = 'neither')],
        'alpha_1': [
            Interval(Real, 0, None, closed = 'left')],
        'alpha_2': [
            Interval(Real, 0, None, closed = 'left')],
        'lambda_1': [
            Interval(Real, 0, None, closed = 'left')],
        'lambda_2': [
            Interval(Real, 0, None, closed = 'left')],
        'alpha_init': [
            None,
            Interval(Real, 0, None, closed = 'left')],
        'lambda_init': [
            None,
            Interval(Real, 0, None, closed = 'left')],
        'compute_score': [
            'boolean'],
        'fit_intercept': [
            'boolean'],
        'copy_X': [
            'boolean'],
        'verbose': [
            'verbose'] }
    
    def __init__(self = None, *, max_iter, tol, alpha_1, alpha_2, lambda_1, lambda_2, alpha_init, lambda_init, compute_score, fit_intercept, copy_X, verbose):
        self.max_iter = max_iter
        self.tol = tol
        self.alpha_1 = alpha_1
        self.alpha_2 = alpha_2
        self.lambda_1 = lambda_1
        self.lambda_2 = lambda_2
        self.alpha_init = alpha_init
        self.lambda_init = lambda_init
        self.compute_score = compute_score
        self.fit_intercept = fit_intercept
        self.copy_X = copy_X
        self.verbose = verbose

    fit = (lambda self, X, y, sample_weight = (None,): (X, y) = validate_data(self, X, y, dtype = [
np.float64,
np.float32], force_writeable = True, y_numeric = True)dtype = X.dtype(n_samples, n_features) = X.shapesw_sum = n_samplesy_var = y.var()# WARNING: Decompyle incomplete
)()
    
    def predict(self, X, return_std = (False,)):
        '''Predict using the linear model.

        In addition to the mean of the predictive distribution, also its
        standard deviation can be returned.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Samples.

        return_std : bool, default=False
            Whether to return the standard deviation of posterior prediction.

        Returns
        -------
        y_mean : array-like of shape (n_samples,)
            Mean of predictive distribution of query points.

        y_std : array-like of shape (n_samples,)
            Standard deviation of predictive distribution of query points.
        '''
        y_mean = self._decision_function(X)
        if not return_std:
            return y_mean
        sigmas_squared_data = (None.dot(X, self.sigma_) * X).sum(axis = 1)
        y_std = np.sqrt(sigmas_squared_data + 1 / self.alpha_)
        return (y_mean, y_std)

    
    def _update_coef_(self, X, y, n_samples, n_features, XT_y, U, Vh, eigen_vals_, alpha_, lambda_):
        '''Update posterior mean and compute corresponding sse (sum of squared errors).

        Posterior mean is given by coef_ = scaled_sigma_ * X.T * y where
        scaled_sigma_ = (lambda_/alpha_ * np.eye(n_features)
                         + np.dot(X.T, X))^-1
        '''
        if n_samples > n_features:
            coef_ = np.linalg.multi_dot([
                Vh.T,
                Vh / eigen_vals_ + lambda_ / alpha_[(:, np.newaxis)],
                XT_y])
        else:
            coef_ = np.linalg.multi_dot([
                X.T,
                U / eigen_vals_ + lambda_ / alpha_[(None, :)],
                U.T,
                y])
        sse_ = np.sum((y - np.dot(X, coef_)) ** 2)
        return (coef_, sse_)

    
    def _log_marginal_likelihood(self, n_samples, n_features, sw_sum, eigen_vals, alpha_, lambda_, coef, sse):
        '''Log marginal likelihood.'''
        alpha_1 = self.alpha_1
        alpha_2 = self.alpha_2
        lambda_1 = self.lambda_1
        lambda_2 = self.lambda_2
        if n_samples > n_features:
            logdet_sigma = -np.sum(np.log(lambda_ + alpha_ * eigen_vals))
        else:
            logdet_sigma = np.full(n_features, lambda_, dtype = np.array(lambda_).dtype)
            -np.sum(np.log(logdet_sigma)) = None
        score = lambda_1 * log(lambda_) - lambda_2 * lambda_
        score += alpha_1 * log(alpha_) - alpha_2 * alpha_
        score += 0.5 * ((n_features * log(lambda_) + sw_sum * log(alpha_) - alpha_ * sse - lambda_ * np.sum(coef ** 2)) + logdet_sigma - sw_sum * log(2 * np.pi))
        return score



class ARDRegression(LinearModel, RegressorMixin):
    '''Bayesian ARD regression.

    Fit the weights of a regression model, using an ARD prior. The weights of
    the regression model are assumed to be in Gaussian distributions.
    Also estimate the parameters lambda (precisions of the distributions of the
    weights) and alpha (precision of the distribution of the noise).
    The estimation is done by an iterative procedures (Evidence Maximization)

    Read more in the :ref:`User Guide <bayesian_regression>`.

    Parameters
    ----------
    max_iter : int, default=300
        Maximum number of iterations.

        .. versionchanged:: 1.3

    tol : float, default=1e-3
        Stop the algorithm if w has converged.

    alpha_1 : float, default=1e-6
        Hyper-parameter : shape parameter for the Gamma distribution prior
        over the alpha parameter.

    alpha_2 : float, default=1e-6
        Hyper-parameter : inverse scale parameter (rate parameter) for the
        Gamma distribution prior over the alpha parameter.

    lambda_1 : float, default=1e-6
        Hyper-parameter : shape parameter for the Gamma distribution prior
        over the lambda parameter.

    lambda_2 : float, default=1e-6
        Hyper-parameter : inverse scale parameter (rate parameter) for the
        Gamma distribution prior over the lambda parameter.

    compute_score : bool, default=False
        If True, compute the objective function at each step of the model.

    threshold_lambda : float, default=10 000
        Threshold for removing (pruning) weights with high precision from
        the computation.

    fit_intercept : bool, default=True
        Whether to calculate the intercept for this model. If set
        to false, no intercept will be used in calculations
        (i.e. data is expected to be centered).

    copy_X : bool, default=True
        If True, X will be copied; else, it may be overwritten.

    verbose : bool, default=False
        Verbose mode when fitting the model.

    Attributes
    ----------
    coef_ : array-like of shape (n_features,)
        Coefficients of the regression model (mean of distribution)

    alpha_ : float
       estimated precision of the noise.

    lambda_ : array-like of shape (n_features,)
       estimated precisions of the weights.

    sigma_ : array-like of shape (n_features, n_features)
        estimated variance-covariance matrix of the weights

    scores_ : float
        if computed, value of the objective function (to be maximized)

    n_iter_ : int
        The actual number of iterations to reach the stopping criterion.

        .. versionadded:: 1.3

    intercept_ : float
        Independent term in decision function. Set to 0.0 if
        ``fit_intercept = False``.

    X_offset_ : float
        If `fit_intercept=True`, offset subtracted for centering data to a
        zero mean. Set to np.zeros(n_features) otherwise.

    X_scale_ : float
        Set to np.ones(n_features).

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    BayesianRidge : Bayesian ridge regression.

    References
    ----------
    D. J. C. MacKay, Bayesian nonlinear modeling for the prediction
    competition, ASHRAE Transactions, 1994.

    R. Salakhutdinov, Lecture notes on Statistical Machine Learning,
    http://www.utstat.toronto.edu/~rsalakhu/sta4273/notes/Lecture2.pdf#page=15
    Their beta is our ``self.alpha_``
    Their alpha is our ``self.lambda_``
    ARD is a little different than the slide: only dimensions/features for
    which ``self.lambda_ < self.threshold_lambda`` are kept and the rest are
    discarded.

    Examples
    --------
    >>> from sklearn import linear_model
    >>> clf = linear_model.ARDRegression()
    >>> clf.fit([[0,0], [1, 1], [2, 2]], [0, 1, 2])
    ARDRegression()
    >>> clf.predict([[1, 1]])
    array([1.])

    -   :ref:`sphx_glr_auto_examples_linear_model_plot_ard.py` demonstrates ARD
        Regression.
    -   :ref:`sphx_glr_auto_examples_linear_model_plot_lasso_and_elasticnet.py`
        showcases ARD Regression alongside Lasso and Elastic-Net for sparse,
        correlated signals, in the presence of noise.
    '''
    _parameter_constraints: dict = {
        'max_iter': [
            Interval(Integral, 1, None, closed = 'left')],
        'tol': [
            Interval(Real, 0, None, closed = 'left')],
        'alpha_1': [
            Interval(Real, 0, None, closed = 'left')],
        'alpha_2': [
            Interval(Real, 0, None, closed = 'left')],
        'lambda_1': [
            Interval(Real, 0, None, closed = 'left')],
        'lambda_2': [
            Interval(Real, 0, None, closed = 'left')],
        'compute_score': [
            'boolean'],
        'threshold_lambda': [
            Interval(Real, 0, None, closed = 'left')],
        'fit_intercept': [
            'boolean'],
        'copy_X': [
            'boolean'],
        'verbose': [
            'verbose'] }
    
    def __init__(self = None, *, max_iter, tol, alpha_1, alpha_2, lambda_1, lambda_2, compute_score, threshold_lambda, fit_intercept, copy_X, verbose):
        self.max_iter = max_iter
        self.tol = tol
        self.fit_intercept = fit_intercept
        self.alpha_1 = alpha_1
        self.alpha_2 = alpha_2
        self.lambda_1 = lambda_1
        self.lambda_2 = lambda_2
        self.compute_score = compute_score
        self.threshold_lambda = threshold_lambda
        self.copy_X = copy_X
        self.verbose = verbose

    fit = (lambda self, X, y: (X, y) = validate_data(self, X, y, dtype = [
np.float64,
np.float32], force_writeable = True, y_numeric = True, ensure_min_samples = 2)dtype = X.dtype(n_samples, n_features) = X.shapecoef_ = np.zeros(n_features, dtype = dtype)(X, y, X_offset_, y_offset_, X_scale_, _) = _preprocess_data(X, y, fit_intercept = self.fit_intercept, copy = self.copy_X)self.X_offset_ = X_offset_self.X_scale_ = X_scale_keep_lambda = np.ones(n_features, dtype = bool)lambda_1 = self.lambda_1lambda_2 = self.lambda_2alpha_1 = self.alpha_1alpha_2 = self.alpha_2verbose = self.verboseeps = np.finfo(np.float64).epsalpha_ = np.asarray(1 / (np.var(y) + eps), dtype = dtype)lambda_ = np.ones(n_features, dtype = dtype)self.scores_ = list()coef_old_ = None
def update_coeff(X, y, coef_, alpha_, keep_lambda, sigma_):
coef_[keep_lambda] = alpha_ * np.linalg.multi_dot([
sigma_,
X[(:, keep_lambda)].T,
y])coef_update_sigma = self._update_sigma if n_samples >= n_features else self._update_sigma_woodburyfor iter_ in range(self.max_iter):
sigma_ = update_sigma(X, alpha_, lambda_, keep_lambda)coef_ = update_coeff(X, y, coef_, alpha_, keep_lambda, sigma_)sse_ = np.sum((y - np.dot(X, coef_)) ** 2)gamma_ = 1 - lambda_[keep_lambda] * np.diag(sigma_)lambda_[keep_lambda] = (gamma_ + 2 * lambda_1) / (coef_[keep_lambda] ** 2 + 2 * lambda_2)alpha_ = ((n_samples - gamma_.sum()) + 2 * alpha_1) / (sse_ + 2 * alpha_2)keep_lambda = lambda_ < self.threshold_lambdacoef_[~keep_lambda] = 0if self.compute_score:
s = (lambda_1 * np.log(lambda_) - lambda_2 * lambda_).sum()s += alpha_1 * log(alpha_) - alpha_2 * alpha_s += 0.5 * (fast_logdet(sigma_) + n_samples * log(alpha_) + np.sum(np.log(lambda_)))s -= 0.5 * (alpha_ * sse_ + (lambda_ * coef_ ** 2).sum())self.scores_.append(s)if iter_ > 0 and np.sum(np.abs(coef_old_ - coef_)) < self.tol:
if verbose:
print('Converged after %s iterations' % iter_)else:
coef_old_ = np.copy(coef_)if not keep_lambda.any():
passself.n_iter_ = iter_ + 1if keep_lambda.any():
sigma_ = update_sigma(X, alpha_, lambda_, keep_lambda)coef_ = update_coeff(X, y, coef_, alpha_, keep_lambda, sigma_)else:
sigma_ = np.array([]).reshape(0, 0)self.coef_ = coef_self.alpha_ = alpha_self.sigma_ = sigma_self.lambda_ = lambda_self._set_intercept(X_offset_, y_offset_, X_scale_)self)()
    
    def _update_sigma_woodbury(self, X, alpha_, lambda_, keep_lambda):
        n_samples = X.shape[0]
        X_keep = X[(:, keep_lambda)]
        inv_lambda = 1 / lambda_[keep_lambda].reshape(1, -1)
        sigma_ = pinvh(np.eye(n_samples, dtype = X.dtype) / alpha_ + np.dot(X_keep * inv_lambda, X_keep.T))
        sigma_ = np.dot(sigma_, X_keep * inv_lambda)
        sigma_ = -np.dot(inv_lambda.reshape(-1, 1) * X_keep.T, sigma_)
        return sigma_

    
    def _update_sigma(self, X, alpha_, lambda_, keep_lambda):
        X_keep = X[(:, keep_lambda)]
        gram = np.dot(X_keep.T, X_keep)
        eye = np.eye(gram.shape[0], dtype = X.dtype)
        sigma_inv = lambda_[keep_lambda] * eye + alpha_ * gram
        sigma_ = pinvh(sigma_inv)
        return sigma_

    
    def predict(self, X, return_std = (False,)):
        '''Predict using the linear model.

        In addition to the mean of the predictive distribution, also its
        standard deviation can be returned.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            Samples.

        return_std : bool, default=False
            Whether to return the standard deviation of posterior prediction.

        Returns
        -------
        y_mean : array-like of shape (n_samples,)
            Mean of predictive distribution of query points.

        y_std : array-like of shape (n_samples,)
            Standard deviation of predictive distribution of query points.
        '''
        y_mean = self._decision_function(X)
        if return_std is False:
            return y_mean
        col_index = None.lambda_ < self.threshold_lambda
        X = _safe_indexing(X, indices = col_index, axis = 1)
        sigmas_squared_data = (np.dot(X, self.sigma_) * X).sum(axis = 1)
        y_std = np.sqrt(sigmas_squared_data + 1 / self.alpha_)
        return (y_mean, y_std)
