# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _gpc.pyc (Python 3.11)

'''Gaussian processes classification.'''
from numbers import Integral
from operator import itemgetter
import numpy as np
import scipy.optimize as scipy
from scipy.linalg import cho_solve, cholesky, solve
from scipy.special import erf, expit
from sklearn.base import BaseEstimator, ClassifierMixin, _fit_context, clone
from sklearn.gaussian_process.kernels import RBF, CompoundKernel, Kernel
from sklearn.gaussian_process.kernels import ConstantKernel as C
from sklearn.multiclass import OneVsOneClassifier, OneVsRestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import check_random_state
from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.utils.optimize import _check_optimize_result
from sklearn.utils.validation import check_is_fitted, validate_data
LAMBDAS = np.array([
    0.41,
    0.4,
    0.37,
    0.44,
    0.39])[(:, np.newaxis)]
COEFS = np.array([
    -1854.82,
    3516.9,
    221.293,
    128.123,
    -2010.49])[(:, np.newaxis)]

class _BinaryGaussianProcessClassifierLaplace(BaseEstimator):
    '''Binary Gaussian process classification based on Laplace approximation.

    The implementation is based on Algorithm 3.1, 3.2, and 5.1 from [RW2006]_.

    Internally, the Laplace approximation is used for approximating the
    non-Gaussian posterior by a Gaussian.

    Currently, the implementation is restricted to using the logistic link
    function.

    .. versionadded:: 0.18

    Parameters
    ----------
    kernel : kernel instance, default=None
        The kernel specifying the covariance function of the GP. If None is
        passed, the kernel "1.0 * RBF(1.0)" is used as default. Note that
        the kernel\'s hyperparameters are optimized during fitting.

    optimizer : \'fmin_l_bfgs_b\' or callable, default=\'fmin_l_bfgs_b\'
        Can either be one of the internally supported optimizers for optimizing
        the kernel\'s parameters, specified by a string, or an externally
        defined optimizer passed as a callable. If a callable is passed, it
        must have the  signature::

            def optimizer(obj_func, initial_theta, bounds):
                # * \'obj_func\' is the objective function to be maximized, which
                #   takes the hyperparameters theta as parameter and an
                #   optional flag eval_gradient, which determines if the
                #   gradient is returned additionally to the function value
                # * \'initial_theta\': the initial value for theta, which can be
                #   used by local optimizers
                # * \'bounds\': the bounds on the values of theta
                ....
                # Returned are the best found hyperparameters theta and
                # the corresponding value of the target function.
                return theta_opt, func_min

        Per default, the \'L-BFGS-B\' algorithm from scipy.optimize.minimize
        is used. If None is passed, the kernel\'s parameters are kept fixed.
        Available internal optimizers are::

            \'fmin_l_bfgs_b\'

    n_restarts_optimizer : int, default=0
        The number of restarts of the optimizer for finding the kernel\'s
        parameters which maximize the log-marginal likelihood. The first run
        of the optimizer is performed from the kernel\'s initial parameters,
        the remaining ones (if any) from thetas sampled log-uniform randomly
        from the space of allowed theta-values. If greater than 0, all bounds
        must be finite. Note that n_restarts_optimizer=0 implies that one
        run is performed.

    max_iter_predict : int, default=100
        The maximum number of iterations in Newton\'s method for approximating
        the posterior during predict. Smaller values will reduce computation
        time at the cost of worse results.

    warm_start : bool, default=False
        If warm-starts are enabled, the solution of the last Newton iteration
        on the Laplace approximation of the posterior mode is used as
        initialization for the next call of _posterior_mode(). This can speed
        up convergence when _posterior_mode is called several times on similar
        problems as in hyperparameter optimization. See :term:`the Glossary
        <warm_start>`.

    copy_X_train : bool, default=True
        If True, a persistent copy of the training data is stored in the
        object. Otherwise, just a reference to the training data is stored,
        which might cause predictions to change if the data is modified
        externally.

    random_state : int, RandomState instance or None, default=None
        Determines random number generation used to initialize the centers.
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    Attributes
    ----------
    X_train_ : array-like of shape (n_samples, n_features) or list of object
        Feature vectors or other representations of training data (also
        required for prediction).

    y_train_ : array-like of shape (n_samples,)
        Target values in training data (also required for prediction)

    classes_ : array-like of shape (n_classes,)
        Unique class labels.

    kernel_ : kernl instance
        The kernel used for prediction. The structure of the kernel is the
        same as the one passed as parameter but with optimized hyperparameters

    L_ : array-like of shape (n_samples, n_samples)
        Lower-triangular Cholesky decomposition of the kernel in X_train_

    pi_ : array-like of shape (n_samples,)
        The probabilities of the positive class for the training points
        X_train_

    W_sr_ : array-like of shape (n_samples,)
        Square root of W, the Hessian of log-likelihood of the latent function
        values for the observed labels. Since W is diagonal, only the diagonal
        of sqrt(W) is stored.

    log_marginal_likelihood_value_ : float
        The log-marginal-likelihood of ``self.kernel_.theta``

    References
    ----------
    .. [RW2006] `Carl E. Rasmussen and Christopher K.I. Williams,
       "Gaussian Processes for Machine Learning",
       MIT Press 2006 <https://www.gaussianprocess.org/gpml/chapters/RW.pdf>`_
    '''
    
    def __init__(self = None, kernel = (None,), *, optimizer, n_restarts_optimizer, max_iter_predict, warm_start, copy_X_train, random_state):
        self.kernel = kernel
        self.optimizer = optimizer
        self.n_restarts_optimizer = n_restarts_optimizer
        self.max_iter_predict = max_iter_predict
        self.warm_start = warm_start
        self.copy_X_train = copy_X_train
        self.random_state = random_state

    
    def fit(self, X, y):
        '''Fit Gaussian process classification model.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features) or list of object
            Feature vectors or other representations of training data.

        y : array-like of shape (n_samples,)
            Target values, must be binary.

        Returns
        -------
        self : returns an instance of self.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def predict(self, X):
        '''Perform classification on an array of test vectors X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features) or list of object
            Query points where the GP is evaluated for classification.

        Returns
        -------
        C : ndarray of shape (n_samples,)
            Predicted target values for X, values are from ``classes_``
        '''
        check_is_fitted(self)
        K_star = self.kernel_(self.X_train_, X)
        f_star = K_star.T.dot(self.y_train_ - self.pi_)
        return np.where(f_star > 0, self.classes_[1], self.classes_[0])

    
    def predict_proba(self, X):
        '''Return probability estimates for the test vector X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features) or list of object
            Query points where the GP is evaluated for classification.

        Returns
        -------
        C : array-like of shape (n_samples, n_classes)
            Returns the probability of the samples for each class in
            the model. The columns correspond to the classes in sorted
            order, as they appear in the attribute ``classes_``.
        '''
        check_is_fitted(self)
        (latent_mean, latent_var) = self.latent_mean_and_variance(X)
        alpha = 1 / (2 * latent_var)
        gamma = LAMBDAS * latent_mean
        integrals = np.sqrt(np.pi / alpha) * erf(gamma * np.sqrt(alpha / (alpha + LAMBDAS ** 2))) / (2 * np.sqrt(latent_var * 2 * np.pi))
        pi_star = (COEFS * integrals).sum(axis = 0) + 0.5 * COEFS.sum()
        return np.vstack((1 - pi_star, pi_star)).T

    
    def log_marginal_likelihood(self, theta, eval_gradient, clone_kernel = (None, False, True)):
        '''Returns log-marginal likelihood of theta for training data.

        Parameters
        ----------
        theta : array-like of shape (n_kernel_params,), default=None
            Kernel hyperparameters for which the log-marginal likelihood is
            evaluated. If None, the precomputed log_marginal_likelihood
            of ``self.kernel_.theta`` is returned.

        eval_gradient : bool, default=False
            If True, the gradient of the log-marginal likelihood with respect
            to the kernel hyperparameters at position theta is returned
            additionally. If True, theta must not be None.

        clone_kernel : bool, default=True
            If True, the kernel attribute is copied. If False, the kernel
            attribute is modified, but may result in a performance improvement.

        Returns
        -------
        log_likelihood : float
            Log-marginal likelihood of theta for training data.

        log_likelihood_gradient : ndarray of shape (n_kernel_params,),                 optional
            Gradient of the log-marginal likelihood with respect to the kernel
            hyperparameters at position theta.
            Only returned when `eval_gradient` is True.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def latent_mean_and_variance(self, X):
        '''Compute the mean and variance of the latent function values.

        Based on algorithm 3.2 of [RW2006]_, this function returns the latent
        mean (Line 4) and variance (Line 6) of the Gaussian process
        classification model.

        Note that this function is only supported for binary classification.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features) or list of object
            Query points where the GP is evaluated for classification.

        Returns
        -------
        latent_mean : array-like of shape (n_samples,)
            Mean of the latent function values at the query points.

        latent_var : array-like of shape (n_samples,)
            Variance of the latent function values at the query points.
        '''
        check_is_fitted(self)
        K_star = self.kernel_(self.X_train_, X)
        latent_mean = K_star.T.dot(self.y_train_ - self.pi_)
        v = solve(self.L_, self.W_sr_[(:, np.newaxis)] * K_star)
        latent_var = self.kernel_.diag(X) - np.einsum('ij,ij->j', v, v)
        return (latent_mean, latent_var)

    
    def _posterior_mode(self, K, return_temporaries = (False,)):
        """Mode-finding for binary Laplace GPC and fixed kernel.

        This approximates the posterior of the latent function values for given
        inputs and target observations with a Gaussian approximation and uses
        Newton's iteration to find the mode of this approximation.
        """
        if self.warm_start and hasattr(self, 'f_cached') and self.f_cached.shape == self.y_train_.shape:
            f = self.f_cached
        else:
            f = np.zeros_like(self.y_train_, dtype = np.float64)
        log_marginal_likelihood = -(np.inf)
        for _ in range(self.max_iter_predict):
            pi = expit(f)
            W = pi * (1 - pi)
            W_sr = np.sqrt(W)
            W_sr_K = W_sr[(:, np.newaxis)] * K
            B = np.eye(W.shape[0]) + W_sr_K * W_sr
            L = cholesky(B, lower = True)
            b = W * f + (self.y_train_ - pi)
            a = b - W_sr * cho_solve((L, True), W_sr_K.dot(b))
            f = K.dot(a)
            lml = -0.5 * a.T.dot(f) - np.log1p(np.exp(-(self.y_train_ * 2 - 1) * f)).sum() - np.log(np.diag(L)).sum()
            if lml - log_marginal_likelihood < 1e-10:
                pass
            else:
                log_marginal_likelihood = lml
            self.f_cached = f
            if return_temporaries:
                return (log_marginal_likelihood, (pi, W_sr, L, b, a))
            return None

    
    def _constrained_optimization(self, obj_func, initial_theta, bounds):
        if self.optimizer == 'fmin_l_bfgs_b':
            opt_res = scipy.optimize.minimize(obj_func, initial_theta, method = 'L-BFGS-B', jac = True, bounds = bounds)
            _check_optimize_result('lbfgs', opt_res)
            func_min = opt_res.fun
            theta_opt = opt_res.x
        elif callable(self.optimizer):
            (theta_opt, func_min) = self.optimizer(obj_func, initial_theta, bounds = bounds)
        else:
            raise ValueError('Unknown optimizer %s.' % self.optimizer)
        return (theta_opt, func_min)



class GaussianProcessClassifier(BaseEstimator, ClassifierMixin):
    '''Gaussian process classification (GPC) based on Laplace approximation.

    The implementation is based on Algorithm 3.1, 3.2, and 5.1 from [RW2006]_.

    Internally, the Laplace approximation is used for approximating the
    non-Gaussian posterior by a Gaussian.

    Currently, the implementation is restricted to using the logistic link
    function. For multi-class classification, several binary one-versus rest
    classifiers are fitted. Note that this class thus does not implement
    a true multi-class Laplace approximation.

    Read more in the :ref:`User Guide <gaussian_process>`.

    .. versionadded:: 0.18

    Parameters
    ----------
    kernel : kernel instance, default=None
        The kernel specifying the covariance function of the GP. If None is
        passed, the kernel "1.0 * RBF(1.0)" is used as default. Note that
        the kernel\'s hyperparameters are optimized during fitting. Also kernel
        cannot be a `CompoundKernel`.

    optimizer : \'fmin_l_bfgs_b\', callable or None, default=\'fmin_l_bfgs_b\'
        Can either be one of the internally supported optimizers for optimizing
        the kernel\'s parameters, specified by a string, or an externally
        defined optimizer passed as a callable. If a callable is passed, it
        must have the  signature::

            def optimizer(obj_func, initial_theta, bounds):
                # * \'obj_func\' is the objective function to be maximized, which
                #   takes the hyperparameters theta as parameter and an
                #   optional flag eval_gradient, which determines if the
                #   gradient is returned additionally to the function value
                # * \'initial_theta\': the initial value for theta, which can be
                #   used by local optimizers
                # * \'bounds\': the bounds on the values of theta
                ....
                # Returned are the best found hyperparameters theta and
                # the corresponding value of the target function.
                return theta_opt, func_min

        Per default, the \'L-BFGS-B\' algorithm from scipy.optimize.minimize
        is used. If None is passed, the kernel\'s parameters are kept fixed.
        Available internal optimizers are::

            \'fmin_l_bfgs_b\'

    n_restarts_optimizer : int, default=0
        The number of restarts of the optimizer for finding the kernel\'s
        parameters which maximize the log-marginal likelihood. The first run
        of the optimizer is performed from the kernel\'s initial parameters,
        the remaining ones (if any) from thetas sampled log-uniform randomly
        from the space of allowed theta-values. If greater than 0, all bounds
        must be finite. Note that n_restarts_optimizer=0 implies that one
        run is performed.

    max_iter_predict : int, default=100
        The maximum number of iterations in Newton\'s method for approximating
        the posterior during predict. Smaller values will reduce computation
        time at the cost of worse results.

    warm_start : bool, default=False
        If warm-starts are enabled, the solution of the last Newton iteration
        on the Laplace approximation of the posterior mode is used as
        initialization for the next call of _posterior_mode(). This can speed
        up convergence when _posterior_mode is called several times on similar
        problems as in hyperparameter optimization. See :term:`the Glossary
        <warm_start>`.

    copy_X_train : bool, default=True
        If True, a persistent copy of the training data is stored in the
        object. Otherwise, just a reference to the training data is stored,
        which might cause predictions to change if the data is modified
        externally.

    random_state : int, RandomState instance or None, default=None
        Determines random number generation used to initialize the centers.
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    multi_class : {\'one_vs_rest\', \'one_vs_one\'}, default=\'one_vs_rest\'
        Specifies how multi-class classification problems are handled.
        Supported are \'one_vs_rest\' and \'one_vs_one\'. In \'one_vs_rest\',
        one binary Gaussian process classifier is fitted for each class, which
        is trained to separate this class from the rest. In \'one_vs_one\', one
        binary Gaussian process classifier is fitted for each pair of classes,
        which is trained to separate these two classes. The predictions of
        these binary predictors are combined into multi-class predictions.
        Note that \'one_vs_one\' does not support predicting probability
        estimates.

    n_jobs : int, default=None
        The number of jobs to use for the computation: the specified
        multiclass problems are computed in parallel.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    Attributes
    ----------
    base_estimator_ : ``Estimator`` instance
        The estimator instance that defines the likelihood function
        using the observed data.

    kernel_ : kernel instance
        The kernel used for prediction. In case of binary classification,
        the structure of the kernel is the same as the one passed as parameter
        but with optimized hyperparameters. In case of multi-class
        classification, a CompoundKernel is returned which consists of the
        different kernels used in the one-versus-rest classifiers.

    log_marginal_likelihood_value_ : float
        The log-marginal-likelihood of ``self.kernel_.theta``

    classes_ : array-like of shape (n_classes,)
        Unique class labels.

    n_classes_ : int
        The number of classes in the training data

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    GaussianProcessRegressor : Gaussian process regression (GPR).

    References
    ----------
    .. [RW2006] `Carl E. Rasmussen and Christopher K.I. Williams,
       "Gaussian Processes for Machine Learning",
       MIT Press 2006 <https://www.gaussianprocess.org/gpml/chapters/RW.pdf>`_

    Examples
    --------
    >>> from sklearn.datasets import load_iris
    >>> from sklearn.gaussian_process import GaussianProcessClassifier
    >>> from sklearn.gaussian_process.kernels import RBF
    >>> X, y = load_iris(return_X_y=True)
    >>> kernel = 1.0 * RBF(1.0)
    >>> gpc = GaussianProcessClassifier(kernel=kernel,
    ...         random_state=0).fit(X, y)
    >>> gpc.score(X, y)
    0.9866...
    >>> gpc.predict_proba(X[:2,:])
    array([[0.83548752, 0.03228706, 0.13222543],
           [0.79064206, 0.06525643, 0.14410151]])

    For a comparison of the GaussianProcessClassifier with other classifiers see:
    :ref:`sphx_glr_auto_examples_classification_plot_classification_probability.py`.
    '''
    _parameter_constraints: dict = {
        'kernel': [
            Kernel,
            None],
        'optimizer': [
            StrOptions({
                'fmin_l_bfgs_b'}),
            callable,
            None],
        'n_restarts_optimizer': [
            Interval(Integral, 0, None, closed = 'left')],
        'max_iter_predict': [
            Interval(Integral, 1, None, closed = 'left')],
        'warm_start': [
            'boolean'],
        'copy_X_train': [
            'boolean'],
        'random_state': [
            'random_state'],
        'multi_class': [
            StrOptions({
                'one_vs_rest',
                'one_vs_one'})],
        'n_jobs': [
            Integral,
            None] }
    
    def __init__(self = None, kernel = (None,), *, optimizer, n_restarts_optimizer, max_iter_predict, warm_start, copy_X_train, random_state, multi_class, n_jobs):
        self.kernel = kernel
        self.optimizer = optimizer
        self.n_restarts_optimizer = n_restarts_optimizer
        self.max_iter_predict = max_iter_predict
        self.warm_start = warm_start
        self.copy_X_train = copy_X_train
        self.random_state = random_state
        self.multi_class = multi_class
        self.n_jobs = n_jobs

    fit = (lambda self, X, y: if isinstance(self.kernel, CompoundKernel):
raise ValueError('kernel cannot be a CompoundKernel')# WARNING: Decompyle incomplete
)()
    
    def predict(self, X):
        '''Perform classification on an array of test vectors X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features) or list of object
            Query points where the GP is evaluated for classification.

        Returns
        -------
        C : ndarray of shape (n_samples,)
            Predicted target values for X, values are from ``classes_``.
        '''
        check_is_fitted(self)
    # WARNING: Decompyle incomplete

    
    def predict_proba(self, X):
        '''Return probability estimates for the test vector X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features) or list of object
            Query points where the GP is evaluated for classification.

        Returns
        -------
        C : array-like of shape (n_samples, n_classes)
            Returns the probability of the samples for each class in
            the model. The columns correspond to the classes in sorted
            order, as they appear in the attribute :term:`classes_`.
        '''
        check_is_fitted(self)
        if self.n_classes_ > 2 and self.multi_class == 'one_vs_one':
            raise ValueError('one_vs_one multi-class mode does not support predicting probability estimates. Use one_vs_rest mode instead.')
    # WARNING: Decompyle incomplete

    kernel_ = (lambda self: if self.n_classes_ == 2:
self.base_estimator_.kernel_(lambda .0: [ estimator.kernel_ for estimator in .0 ])(self.base_estimator_.estimators_())
)()
    
    def log_marginal_likelihood(self, theta, eval_gradient, clone_kernel = (None, False, True)):
        '''Return log-marginal likelihood of theta for training data.

        In the case of multi-class classification, the mean log-marginal
        likelihood of the one-versus-rest classifiers are returned.

        Parameters
        ----------
        theta : array-like of shape (n_kernel_params,), default=None
            Kernel hyperparameters for which the log-marginal likelihood is
            evaluated. In the case of multi-class classification, theta may
            be the  hyperparameters of the compound kernel or of an individual
            kernel. In the latter case, all individual kernel get assigned the
            same theta values. If None, the precomputed log_marginal_likelihood
            of ``self.kernel_.theta`` is returned.

        eval_gradient : bool, default=False
            If True, the gradient of the log-marginal likelihood with respect
            to the kernel hyperparameters at position theta is returned
            additionally. Note that gradient computation is not supported
            for non-binary classification. If True, theta must not be None.

        clone_kernel : bool, default=True
            If True, the kernel attribute is copied. If False, the kernel
            attribute is modified, but may result in a performance improvement.

        Returns
        -------
        log_likelihood : float
            Log-marginal likelihood of theta for training data.

        log_likelihood_gradient : ndarray of shape (n_kernel_params,), optional
            Gradient of the log-marginal likelihood with respect to the kernel
            hyperparameters at position theta.
            Only returned when `eval_gradient` is True.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def latent_mean_and_variance(self, X):
        '''Compute the mean and variance of the latent function.

        Based on algorithm 3.2 of [RW2006]_, this function returns the latent
        mean (Line 4) and variance (Line 6) of the Gaussian process
        classification model.

        Note that this function is only supported for binary classification.

        .. versionadded:: 1.7

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features) or list of object
            Query points where the GP is evaluated for classification.

        Returns
        -------
        latent_mean : array-like of shape (n_samples,)
            Mean of the latent function values at the query points.

        latent_var : array-like of shape (n_samples,)
            Variance of the latent function values at the query points.
        '''
        if self.n_classes_ > 2:
            raise ValueError(f'''Returning the mean and variance of the latent function f is only supported for binary classification, received {self.n_classes_} classes.''')
        check_is_fitted(self)
    # WARNING: Decompyle incomplete
