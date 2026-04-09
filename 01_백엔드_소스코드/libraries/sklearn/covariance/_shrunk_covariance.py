# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _shrunk_covariance.pyc (Python 3.11)

'''
Covariance estimators using shrinkage.

Shrinkage corresponds to regularising `cov` using a convex combination:
shrunk_cov = (1-shrinkage)*cov + shrinkage*structured_estimate.

'''
import warnings
from numbers import Integral, Real
import numpy as np
from sklearn.base import _fit_context
from sklearn.covariance import EmpiricalCovariance, empirical_covariance
from sklearn.utils import check_array
from sklearn.utils._param_validation import Interval, validate_params
from sklearn.utils.validation import validate_data

def _ledoit_wolf(X, *, assume_centered, block_size):
    '''Estimate the shrunk Ledoit-Wolf covariance matrix.'''
    if len(X.shape) == 2 and X.shape[1] == 1:
        if not assume_centered:
            X = X - X.mean()
        return (np.atleast_2d((X ** 2).mean()), 0)
    n_features = None.shape[1]
    shrinkage = ledoit_wolf_shrinkage(X, assume_centered = assume_centered, block_size = block_size)
    emp_cov = empirical_covariance(X, assume_centered = assume_centered)
    mu = np.sum(np.trace(emp_cov)) / n_features
    shrunk_cov = (1 - shrinkage) * emp_cov
    return (shrunk_cov, shrinkage)


def _oas(X = None, *, assume_centered):
    '''Estimate covariance with the Oracle Approximating Shrinkage algorithm.

    The formulation is based on [1]_.
    [1] "Shrinkage algorithms for MMSE covariance estimation.",
        Chen, Y., Wiesel, A., Eldar, Y. C., & Hero, A. O.
        IEEE Transactions on Signal Processing, 58(10), 5016-5029, 2010.
        https://arxiv.org/pdf/0907.4698.pdf
    '''
    if len(X.shape) == 2 and X.shape[1] == 1:
        if not assume_centered:
            X = X - X.mean()
        return (np.atleast_2d((X ** 2).mean()), 0)
    (n_samples, n_features) = None.shape
    emp_cov = empirical_covariance(X, assume_centered = assume_centered)
    alpha = np.mean(emp_cov ** 2)
    mu = np.trace(emp_cov) / n_features
    mu_squared = mu ** 2
    num = alpha + mu_squared
    den = (n_samples + 1) * (alpha - mu_squared / n_features)
    shrinkage = 1 if den == 0 else min(num / den, 1)
    shrunk_cov = (1 - shrinkage) * emp_cov
    return (shrunk_cov, shrinkage)

shrunk_covariance = (lambda emp_cov, shrinkage = (0.1,): emp_cov = check_array(emp_cov, allow_nd = True)n_features = emp_cov.shape[-1]shrunk_cov = (1 - shrinkage) * emp_covmu = np.trace(emp_cov, axis1 = -2, axis2 = -1) / n_featuresmu = np.expand_dims(mu, axis = tuple(range(mu.ndim, emp_cov.ndim)))shrunk_cov += shrinkage * mu * np.eye(n_features)shrunk_cov)()

class ShrunkCovariance(EmpiricalCovariance):
    pass
# WARNING: Decompyle incomplete

ledoit_wolf_shrinkage = (lambda X, assume_centered, block_size = (False, 1000): X = check_array(X)if len(X.shape) == 2 and X.shape[1] == 1:
0if None.ndim == 1:
X = np.reshape(X, (1, -1))if X.shape[0] == 1:
warnings.warn('Only one sample available. You may want to reshape your data array')(n_samples, n_features) = X.shapeif not assume_centered:
X = X - X.mean(0)n_splits = int(n_features / block_size)X2 = X ** 2emp_cov_trace = np.sum(X2, axis = 0) / n_samplesmu = np.sum(emp_cov_trace) / n_featuresbeta_ = 0delta_ = 0for i in range(n_splits):
for j in range(n_splits):
rows = slice(block_size * i, block_size * (i + 1))cols = slice(block_size * j, block_size * (j + 1))beta_ += np.sum(np.dot(X2.T[rows], X2[(:, cols)]))delta_ += np.sum(np.dot(X.T[rows], X[(:, cols)]) ** 2)rows = slice(block_size * i, block_size * (i + 1))beta_ += np.sum(np.dot(X2.T[rows], X2[(:, block_size * n_splits:)]))delta_ += np.sum(np.dot(X.T[rows], X[(:, block_size * n_splits:)]) ** 2)for j in range(n_splits):
cols = slice(block_size * j, block_size * (j + 1))beta_ += np.sum(np.dot(X2.T[block_size * n_splits:], X2[(:, cols)]))delta_ += np.sum(np.dot(X.T[block_size * n_splits:], X[(:, cols)]) ** 2)delta_ += np.sum(np.dot(X.T[block_size * n_splits:], X[(:, block_size * n_splits:)]) ** 2)delta_ /= n_samples ** 2beta_ += np.sum(np.dot(X2.T[block_size * n_splits:], X2[(:, block_size * n_splits:)]))beta = (1 / (n_features * n_samples)) * (beta_ / n_samples - delta_)delta = (delta_ - 2 * mu * emp_cov_trace.sum()) + n_features * mu ** 2delta /= n_featuresbeta = min(beta, delta)shrinkage = 0 if beta == 0 else beta / deltashrinkage)()
ledoit_wolf = (lambda X = validate_params({
    'X': [
        'array-like'] }, prefer_skip_nested_validation = False), *, assume_centered: estimator = LedoitWolf(assume_centered = assume_centered, block_size = block_size, store_precision = False).fit(X)(estimator.covariance_, estimator.shrinkage_))()

class LedoitWolf(EmpiricalCovariance):
    pass
# WARNING: Decompyle incomplete

oas = (lambda X = validate_params({
    'X': [
        'array-like'] }, prefer_skip_nested_validation = False), *, assume_centered: estimator = OAS(assume_centered = assume_centered).fit(X)(estimator.covariance_, estimator.shrinkage_))()

class OAS(EmpiricalCovariance):
    '''Oracle Approximating Shrinkage Estimator.

    Read more in the :ref:`User Guide <shrunk_covariance>`.

    Parameters
    ----------
    store_precision : bool, default=True
        Specify if the estimated precision is stored.

    assume_centered : bool, default=False
        If True, data will not be centered before computation.
        Useful when working with data whose mean is almost, but not exactly
        zero.
        If False (default), data will be centered before computation.

    Attributes
    ----------
    covariance_ : ndarray of shape (n_features, n_features)
        Estimated covariance matrix.

    location_ : ndarray of shape (n_features,)
        Estimated location, i.e. the estimated mean.

    precision_ : ndarray of shape (n_features, n_features)
        Estimated pseudo inverse matrix.
        (stored only if store_precision is True)

    shrinkage_ : float
      coefficient in the convex combination used for the computation
      of the shrunk estimate. Range is [0, 1].

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    EllipticEnvelope : An object for detecting outliers in
        a Gaussian distributed dataset.
    EmpiricalCovariance : Maximum likelihood covariance estimator.
    GraphicalLasso : Sparse inverse covariance estimation
        with an l1-penalized estimator.
    GraphicalLassoCV : Sparse inverse covariance with cross-validated
        choice of the l1 penalty.
    LedoitWolf : LedoitWolf Estimator.
    MinCovDet : Minimum Covariance Determinant
        (robust estimator of covariance).
    ShrunkCovariance : Covariance estimator with shrinkage.

    Notes
    -----
    The regularised covariance is:

    (1 - shrinkage) * cov + shrinkage * mu * np.identity(n_features),

    where mu = trace(cov) / n_features and shrinkage is given by the OAS formula
    (see [1]_).

    The shrinkage formulation implemented here differs from Eq. 23 in [1]_. In
    the original article, formula (23) states that 2/p (p being the number of
    features) is multiplied by Trace(cov*cov) in both the numerator and
    denominator, but this operation is omitted because for a large p, the value
    of 2/p is so small that it doesn\'t affect the value of the estimator.

    References
    ----------
    .. [1] :arxiv:`"Shrinkage algorithms for MMSE covariance estimation.",
           Chen, Y., Wiesel, A., Eldar, Y. C., & Hero, A. O.
           IEEE Transactions on Signal Processing, 58(10), 5016-5029, 2010.
           <0907.4698>`

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.covariance import OAS
    >>> from sklearn.datasets import make_gaussian_quantiles
    >>> real_cov = np.array([[.8, .3],
    ...                      [.3, .4]])
    >>> rng = np.random.RandomState(0)
    >>> X = rng.multivariate_normal(mean=[0, 0],
    ...                             cov=real_cov,
    ...                             size=500)
    >>> oas = OAS().fit(X)
    >>> oas.covariance_
    array([[0.7533, 0.2763],
           [0.2763, 0.3964]])
    >>> oas.precision_
    array([[ 1.7833, -1.2431 ],
           [-1.2431,  3.3889]])
    >>> oas.shrinkage_
    np.float64(0.0195)

    See also :ref:`sphx_glr_auto_examples_covariance_plot_covariance_estimation.py`
    and :ref:`sphx_glr_auto_examples_covariance_plot_lw_vs_oas.py`
    for more detailed examples.
    '''
    fit = (lambda self, X, y = (None,): X = validate_data(self, X)if self.assume_centered:
self.location_ = np.zeros(X.shape[1])else:
self.location_ = X.mean(0)(covariance, shrinkage) = _oas(X - self.location_, assume_centered = True)self.shrinkage_ = shrinkageself._set_covariance(covariance)self)()
