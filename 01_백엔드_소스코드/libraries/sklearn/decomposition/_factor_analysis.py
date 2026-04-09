# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _factor_analysis.pyc (Python 3.11)

"""Factor Analysis.

A latent linear variable model.

FactorAnalysis is similar to probabilistic PCA implemented by PCA.score
While PCA assumes Gaussian noise with the same variance for each
feature, the FactorAnalysis model assumes different variances for
each of them.

This implementation is based on David Barber's Book,
Bayesian Reasoning and Machine Learning,
http://www.cs.ucl.ac.uk/staff/d.barber/brml,
Algorithm 21.1
"""
import warnings
from math import log, sqrt
from numbers import Integral, Real
import numpy as np
from scipy import linalg
from sklearn.base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin, _fit_context
from sklearn.exceptions import ConvergenceWarning
from sklearn.utils import check_random_state
from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.utils.extmath import _randomized_svd, fast_logdet, squared_norm
from sklearn.utils.validation import check_is_fitted, validate_data

class FactorAnalysis(BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin):
    '''Factor Analysis (FA).

    A simple linear generative model with Gaussian latent variables.

    The observations are assumed to be caused by a linear transformation of
    lower dimensional latent factors and added Gaussian noise.
    Without loss of generality the factors are distributed according to a
    Gaussian with zero mean and unit covariance. The noise is also zero mean
    and has an arbitrary diagonal covariance matrix.

    If we would restrict the model further, by assuming that the Gaussian
    noise is even isotropic (all diagonal entries are the same) we would obtain
    :class:`PCA`.

    FactorAnalysis performs a maximum likelihood estimate of the so-called
    `loading` matrix, the transformation of the latent variables to the
    observed ones, using SVD based approach.

    Read more in the :ref:`User Guide <FA>`.

    .. versionadded:: 0.13

    Parameters
    ----------
    n_components : int, default=None
        Dimensionality of latent space, the number of components
        of ``X`` that are obtained after ``transform``.
        If None, n_components is set to the number of features.

    tol : float, default=1e-2
        Stopping tolerance for log-likelihood increase.

    copy : bool, default=True
        Whether to make a copy of X. If ``False``, the input X gets overwritten
        during fitting.

    max_iter : int, default=1000
        Maximum number of iterations.

    noise_variance_init : array-like of shape (n_features,), default=None
        The initial guess of the noise variance for each feature.
        If None, it defaults to np.ones(n_features).

    svd_method : {\'lapack\', \'randomized\'}, default=\'randomized\'
        Which SVD method to use. If \'lapack\' use standard SVD from
        scipy.linalg, if \'randomized\' use fast ``randomized_svd`` function.
        Defaults to \'randomized\'. For most applications \'randomized\' will
        be sufficiently precise while providing significant speed gains.
        Accuracy can also be improved by setting higher values for
        `iterated_power`. If this is not sufficient, for maximum precision
        you should choose \'lapack\'.

    iterated_power : int, default=3
        Number of iterations for the power method. 3 by default. Only used
        if ``svd_method`` equals \'randomized\'.

    rotation : {\'varimax\', \'quartimax\'}, default=None
        If not None, apply the indicated rotation. Currently, varimax and
        quartimax are implemented. See
        `"The varimax criterion for analytic rotation in factor analysis"
        <https://link.springer.com/article/10.1007%2FBF02289233>`_
        H. F. Kaiser, 1958.

        .. versionadded:: 0.24

    random_state : int or RandomState instance, default=0
        Only used when ``svd_method`` equals \'randomized\'. Pass an int for
        reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    Attributes
    ----------
    components_ : ndarray of shape (n_components, n_features)
        Components with maximum variance.

    loglike_ : list of shape (n_iterations,)
        The log likelihood at each iteration.

    noise_variance_ : ndarray of shape (n_features,)
        The estimated noise variance for each feature.

    n_iter_ : int
        Number of iterations run.

    mean_ : ndarray of shape (n_features,)
        Per-feature empirical mean, estimated from the training set.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    PCA: Principal component analysis is also a latent linear variable model
        which however assumes equal noise variance for each feature.
        This extra assumption makes probabilistic PCA faster as it can be
        computed in closed form.
    FastICA: Independent component analysis, a latent variable model with
        non-Gaussian latent variables.

    References
    ----------
    - David Barber, Bayesian Reasoning and Machine Learning,
      Algorithm 21.1.

    - Christopher M. Bishop: Pattern Recognition and Machine Learning,
      Chapter 12.2.4.

    Examples
    --------
    >>> from sklearn.datasets import load_digits
    >>> from sklearn.decomposition import FactorAnalysis
    >>> X, _ = load_digits(return_X_y=True)
    >>> transformer = FactorAnalysis(n_components=7, random_state=0)
    >>> X_transformed = transformer.fit_transform(X)
    >>> X_transformed.shape
    (1797, 7)
    '''
    _parameter_constraints: dict = {
        'n_components': [
            Interval(Integral, 0, None, closed = 'left'),
            None],
        'tol': [
            Interval(Real, 0, None, closed = 'left')],
        'copy': [
            'boolean'],
        'max_iter': [
            Interval(Integral, 1, None, closed = 'left')],
        'noise_variance_init': [
            'array-like',
            None],
        'svd_method': [
            StrOptions({
                'randomized',
                'lapack'})],
        'iterated_power': [
            Interval(Integral, 0, None, closed = 'left')],
        'rotation': [
            StrOptions({
                'varimax',
                'quartimax'}),
            None],
        'random_state': [
            'random_state'] }
    
    def __init__(self = None, n_components = (None,), *, tol, copy, max_iter, noise_variance_init, svd_method, iterated_power, rotation, random_state):
        self.n_components = n_components
        self.copy = copy
        self.tol = tol
        self.max_iter = max_iter
        self.svd_method = svd_method
        self.noise_variance_init = noise_variance_init
        self.iterated_power = iterated_power
        self.random_state = random_state
        self.rotation = rotation

    fit = (lambda self, X, y = (None,): pass# WARNING: Decompyle incomplete
)()
    
    def transform(self, X):
        '''Apply dimensionality reduction to X using the model.

        Compute the expected mean of the latent variables.
        See Barber, 21.2.33 (or Bishop, 12.66).

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training data.

        Returns
        -------
        X_new : ndarray of shape (n_samples, n_components)
            The latent variables of X.
        '''
        check_is_fitted(self)
        X = validate_data(self, X, reset = False)
        Ih = np.eye(len(self.components_))
        X_transformed = X - self.mean_
        Wpsi = self.components_ / self.noise_variance_
        cov_z = linalg.inv(Ih + np.dot(Wpsi, self.components_.T))
        tmp = np.dot(X_transformed, Wpsi.T)
        X_transformed = np.dot(tmp, cov_z)
        return X_transformed

    
    def get_covariance(self):
        '''Compute data covariance with the FactorAnalysis model.

        ``cov = components_.T * components_ + diag(noise_variance)``

        Returns
        -------
        cov : ndarray of shape (n_features, n_features)
            Estimated covariance of data.
        '''
        check_is_fitted(self)
        cov = np.dot(self.components_.T, self.components_)
        return cov

    
    def get_precision(self):
        '''Compute data precision matrix with the FactorAnalysis model.

        Returns
        -------
        precision : ndarray of shape (n_features, n_features)
            Estimated precision of data.
        '''
        check_is_fitted(self)
        n_features = self.components_.shape[1]
        if self.n_components == 0:
            return np.diag(1 / self.noise_variance_)
        if None.n_components == n_features:
            return linalg.inv(self.get_covariance())
        components_ = None.components_
        precision = np.dot(components_ / self.noise_variance_, components_.T)
        np.dot(components_.T, np.dot(linalg.inv(precision), components_)) = None
        precision /= self.noise_variance_[(:, np.newaxis)]
        precision /= -self.noise_variance_[(np.newaxis, :)]
        return precision

    
    def score_samples(self, X):
        '''Compute the log-likelihood of each sample.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            The data.

        Returns
        -------
        ll : ndarray of shape (n_samples,)
            Log-likelihood of each sample under the current model.
        '''
        check_is_fitted(self)
        X = validate_data(self, X, reset = False)
        Xr = X - self.mean_
        precision = self.get_precision()
        n_features = X.shape[1]
        log_like = -0.5 * (Xr * np.dot(Xr, precision)).sum(axis = 1)
        log_like -= 0.5 * (n_features * log(2 * np.pi) - fast_logdet(precision))
        return log_like

    
    def score(self, X, y = (None,)):
        '''Compute the average log-likelihood of the samples.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            The data.

        y : Ignored
            Ignored parameter.

        Returns
        -------
        ll : float
            Average log-likelihood of the samples under the current model.
        '''
        return np.mean(self.score_samples(X))

    
    def _rotate(self, components, n_components, tol = (None, 1e-06)):
        '''Rotate the factor analysis solution.'''
        return _ortho_rotation(components.T, method = self.rotation, tol = tol)[:self.n_components]

    _n_features_out = (lambda self: self.components_.shape[0])()


def _ortho_rotation(components, method, tol, max_iter = ('varimax', 1e-06, 100)):
    '''Return rotated components.'''
    (nrow, ncol) = components.shape
    rotation_matrix = np.eye(ncol)
    var = 0
    for _ in range(max_iter):
        comp_rot = np.dot(components, rotation_matrix)
        if method == 'varimax':
            tmp = comp_rot * np.transpose((comp_rot ** 2).sum(axis = 0) / nrow)
        elif method == 'quartimax':
            tmp = 0
        (u, s, v) = np.linalg.svd(np.dot(components.T, comp_rot ** 3 - tmp))
        rotation_matrix = np.dot(u, v)
        var_new = np.sum(s)
        if var != 0 and var_new < var * (1 + tol):
            pass
        else:
            var = var_new
        return np.dot(components, rotation_matrix).T
