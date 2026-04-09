# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _robust_covariance.pyc (Python 3.11)

'''
Robust location and covariance estimators.

Here are implemented estimators that are resistant to outliers.

'''
import warnings
from numbers import Integral, Real
import numpy as np
from scipy import linalg
from scipy.stats import chi2
from sklearn.base import _fit_context
from sklearn.covariance._empirical_covariance import EmpiricalCovariance, empirical_covariance
from sklearn.utils import check_array, check_random_state
from sklearn.utils._param_validation import Interval
from sklearn.utils.extmath import fast_logdet
from sklearn.utils.validation import validate_data

def c_step(X, n_support, remaining_iterations, initial_estimates, verbose, cov_computation_method, random_state = (30, None, False, empirical_covariance, None)):
    '''C_step procedure described in [Rouseeuw1984]_ aiming at computing MCD.

    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        Data set in which we look for the n_support observations whose
        scatter matrix has minimum determinant.

    n_support : int
        Number of observations to compute the robust estimates of location
        and covariance from. This parameter must be greater than
        `n_samples / 2`.

    remaining_iterations : int, default=30
        Number of iterations to perform.
        According to [Rouseeuw1999]_, two iterations are sufficient to get
        close to the minimum, and we never need more than 30 to reach
        convergence.

    initial_estimates : tuple of shape (2,), default=None
        Initial estimates of location and shape from which to run the c_step
        procedure:
        - initial_estimates[0]: an initial location estimate
        - initial_estimates[1]: an initial covariance estimate

    verbose : bool, default=False
        Verbose mode.

    cov_computation_method : callable,             default=:func:`sklearn.covariance.empirical_covariance`
        The function which will be used to compute the covariance.
        Must return array of shape (n_features, n_features).

    random_state : int, RandomState instance or None, default=None
        Determines the pseudo random number generator for shuffling the data.
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    Returns
    -------
    location : ndarray of shape (n_features,)
        Robust location estimates.

    covariance : ndarray of shape (n_features, n_features)
        Robust covariance estimates.

    support : ndarray of shape (n_samples,)
        A mask for the `n_support` observations whose scatter matrix has
        minimum determinant.

    References
    ----------
    .. [Rouseeuw1999] A Fast Algorithm for the Minimum Covariance Determinant
        Estimator, 1999, American Statistical Association and the American
        Society for Quality, TECHNOMETRICS
    '''
    X = np.asarray(X)
    random_state = check_random_state(random_state)
    return _c_step(X, n_support, remaining_iterations = remaining_iterations, initial_estimates = initial_estimates, verbose = verbose, cov_computation_method = cov_computation_method, random_state = random_state)


def _c_step(X, n_support, random_state, remaining_iterations, initial_estimates, verbose, cov_computation_method = (30, None, False, empirical_covariance)):
    (n_samples, n_features) = X.shape
    dist = np.inf
# WARNING: Decompyle incomplete


def _consistency_factor(n_features, alpha):
    '''Multiplicative factor to make covariance estimate consistent
    at the normal distribution, as described in [Pison2002]_.

    Parameters
    ----------
    n_features : int
        Number of features.

    alpha : float
        Parameter related to the proportion of discarded points.
        This parameter must be in the range (0, 1).

    Returns
    -------
    c_alpha : float
        Scaling factor to make covariance matrix consistent.

    References
    ----------
    .. [Butler1993] R. W. Butler. P. L. Davies. M. Jhun. "Asymptotics for the
        Minimum Covariance Determinant Estimator." Ann. Statist. 21 (3)
        1385 - 1400, September, 1993. https://doi.org/10.1214/aos/1176349264]

    .. [Croux1999] Croux, C., Haesbroeck, G. "Influence Function and
        Efficiency of the Minimum Covariance Determinant Scatter Matrix
        Estimator" Journal of Multivariate Analysis 71(2) (1999) 161-190

    .. [Pison2002] Pison, G., Van Aelst, S., Willems, G., "Small sample
        corrections for LTS and MCD" Metrika 55(1) (2002) 111-123
    '''
    q_alpha = chi2.ppf(alpha, df = n_features)
    c_alpha = alpha / chi2.cdf(q_alpha, n_features + 2)
    return c_alpha


def select_candidates(X, n_support, n_trials, select, n_iter, verbose, cov_computation_method, random_state = (1, 30, False, empirical_covariance, None)):
    '''Finds the best pure subset of observations to compute MCD from it.

    The purpose of this function is to find the best sets of n_support
    observations with respect to a minimization of their covariance
    matrix determinant. Equivalently, it removes n_samples-n_support
    observations to construct what we call a pure data set (i.e. not
    containing outliers). The list of the observations of the pure
    data set is referred to as the `support`.

    Starting from a random support, the pure data set is found by the
    c_step procedure introduced by Rousseeuw and Van Driessen in
    [RV]_.

    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        Data (sub)set in which we look for the n_support purest observations.

    n_support : int
        The number of samples the pure data set must contain.
        This parameter must be in the range `[(n + p + 1)/2] < n_support < n`.

    n_trials : int or tuple of shape (2,)
        Number of different initial sets of observations from which to
        run the algorithm. This parameter should be a strictly positive
        integer.
        Instead of giving a number of trials to perform, one can provide a
        list of initial estimates that will be used to iteratively run
        c_step procedures. In this case:
        - n_trials[0]: array-like, shape (n_trials, n_features)
          is the list of `n_trials` initial location estimates
        - n_trials[1]: array-like, shape (n_trials, n_features, n_features)
          is the list of `n_trials` initial covariances estimates

    select : int, default=1
        Number of best candidates results to return. This parameter must be
        a strictly positive integer.

    n_iter : int, default=30
        Maximum number of iterations for the c_step procedure.
        (2 is enough to be close to the final solution. "Never" exceeds 20).
        This parameter must be a strictly positive integer.

    verbose : bool, default=False
        Control the output verbosity.

    cov_computation_method : callable,             default=:func:`sklearn.covariance.empirical_covariance`
        The function which will be used to compute the covariance.
        Must return an array of shape (n_features, n_features).

    random_state : int, RandomState instance or None, default=None
        Determines the pseudo random number generator for shuffling the data.
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    See Also
    ---------
    c_step

    Returns
    -------
    best_locations : ndarray of shape (select, n_features)
        The `select` location estimates computed from the `select` best
        supports found in the data set (`X`).

    best_covariances : ndarray of shape (select, n_features, n_features)
        The `select` covariance estimates computed from the `select`
        best supports found in the data set (`X`).

    best_supports : ndarray of shape (select, n_samples)
        The `select` best supports found in the data set (`X`).

    References
    ----------
    .. [RV] A Fast Algorithm for the Minimum Covariance Determinant
        Estimator, 1999, American Statistical Association and the American
        Society for Quality, TECHNOMETRICS
    '''
    random_state = check_random_state(random_state)
    if isinstance(n_trials, Integral):
        run_from_estimates = False
    elif isinstance(n_trials, tuple):
        run_from_estimates = True
        estimates_list = n_trials
        n_trials = estimates_list[0].shape[0]
    else:
        raise TypeError(f'''Invalid \'n_trials\' parameter, expected tuple or  integer, got {n_trials!s} ({type(n_trials)!s})''')
    all_estimates = []
    if not run_from_estimates:
        for j in range(n_trials):
            all_estimates.append(_c_step(X, n_support, remaining_iterations = n_iter, verbose = verbose, cov_computation_method = cov_computation_method, random_state = random_state))
# WARNING: Decompyle incomplete


def fast_mcd(X, support_fraction, cov_computation_method, random_state = (None, empirical_covariance, None)):
    '''Estimate the Minimum Covariance Determinant matrix.

    Read more in the :ref:`User Guide <robust_covariance>`.

    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        The data matrix, with p features and n samples.

    support_fraction : float, default=None
        The proportion of points to be included in the support of the raw
        MCD estimate. Default is `None`, which implies that the minimum
        value of `support_fraction` will be used within the algorithm:
        `(n_samples + n_features + 1) / 2 * n_samples`. This parameter must be
        in the range (0, 1).

    cov_computation_method : callable,             default=:func:`sklearn.covariance.empirical_covariance`
        The function which will be used to compute the covariance.
        Must return an array of shape (n_features, n_features).

    random_state : int, RandomState instance or None, default=None
        Determines the pseudo random number generator for shuffling the data.
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    Returns
    -------
    location : ndarray of shape (n_features,)
        Robust location of the data.

    covariance : ndarray of shape (n_features, n_features)
        Robust covariance of the features.

    support : ndarray of shape (n_samples,), dtype=bool
        A mask of the observations that have been used to compute
        the robust location and covariance estimates of the data set.

    Notes
    -----
    The FastMCD algorithm has been introduced by Rousseuw and Van Driessen
    in "A Fast Algorithm for the Minimum Covariance Determinant Estimator,
    1999, American Statistical Association and the American Society
    for Quality, TECHNOMETRICS".
    The principle is to compute robust estimates and random subsets before
    pooling them into a larger subsets, and finally into the full data set.
    Depending on the size of the initial sample, we have one, two or three
    such computation levels.

    Note that only raw estimates are returned. If one is interested in
    the correction and reweighting steps described in [RouseeuwVan]_,
    see the MinCovDet object.

    References
    ----------

    .. [RouseeuwVan] A Fast Algorithm for the Minimum Covariance
        Determinant Estimator, 1999, American Statistical Association
        and the American Society for Quality, TECHNOMETRICS

    .. [Butler1993] R. W. Butler, P. L. Davies and M. Jhun,
        Asymptotics For The Minimum Covariance Determinant Estimator,
        The Annals of Statistics, 1993, Vol. 21, No. 3, 1385-1400
    '''
    random_state = check_random_state(random_state)
    X = check_array(X, ensure_min_samples = 2, estimator = 'fast_mcd')
    (n_samples, n_features) = X.shape
# WARNING: Decompyle incomplete


class MinCovDet(EmpiricalCovariance):
    __module__ = __name__
    __qualname__ = 'MinCovDet'
    __doc__ = 'Minimum Covariance Determinant (MCD): robust estimator of covariance.\n\n    The Minimum Covariance Determinant covariance estimator is to be applied\n    on Gaussian-distributed data, but could still be relevant on data\n    drawn from a unimodal, symmetric distribution. It is not meant to be used\n    with multi-modal data (the algorithm used to fit a MinCovDet object is\n    likely to fail in such a case).\n    One should consider projection pursuit methods to deal with multi-modal\n    datasets.\n\n    Read more in the :ref:`User Guide <robust_covariance>`.\n\n    Parameters\n    ----------\n    store_precision : bool, default=True\n        Specify if the estimated precision is stored.\n\n    assume_centered : bool, default=False\n        If True, the support of the robust location and the covariance\n        estimates is computed, and a covariance estimate is recomputed from\n        it, without centering the data.\n        Useful to work with data whose mean is significantly equal to\n        zero but is not exactly zero.\n        If False, the robust location and covariance are directly computed\n        with the FastMCD algorithm without additional treatment.\n\n    support_fraction : float, default=None\n        The proportion of points to be included in the support of the raw\n        MCD estimate. Default is None, which implies that the minimum\n        value of support_fraction will be used within the algorithm:\n        `(n_samples + n_features + 1) / 2 * n_samples`. The parameter must be\n        in the range (0, 1].\n\n    random_state : int, RandomState instance or None, default=None\n        Determines the pseudo random number generator for shuffling the data.\n        Pass an int for reproducible results across multiple function calls.\n        See :term:`Glossary <random_state>`.\n\n    Attributes\n    ----------\n    raw_location_ : ndarray of shape (n_features,)\n        The raw robust estimated location before correction and re-weighting.\n\n    raw_covariance_ : ndarray of shape (n_features, n_features)\n        The raw robust estimated covariance before correction and re-weighting.\n\n    raw_support_ : ndarray of shape (n_samples,)\n        A mask of the observations that have been used to compute\n        the raw robust estimates of location and shape, before correction\n        and re-weighting.\n\n    location_ : ndarray of shape (n_features,)\n        Estimated robust location.\n\n        For an example of comparing raw robust estimates with\n        the true location and covariance, refer to\n        :ref:`sphx_glr_auto_examples_covariance_plot_robust_vs_empirical_covariance.py`.\n\n    covariance_ : ndarray of shape (n_features, n_features)\n        Estimated robust covariance matrix.\n\n    precision_ : ndarray of shape (n_features, n_features)\n        Estimated pseudo inverse matrix.\n        (stored only if store_precision is True)\n\n    support_ : ndarray of shape (n_samples,)\n        A mask of the observations that have been used to compute\n        the robust estimates of location and shape.\n\n    dist_ : ndarray of shape (n_samples,)\n        Mahalanobis distances of the training set (on which :meth:`fit` is\n        called) observations.\n\n    n_features_in_ : int\n        Number of features seen during :term:`fit`.\n\n        .. versionadded:: 0.24\n\n    feature_names_in_ : ndarray of shape (`n_features_in_`,)\n        Names of features seen during :term:`fit`. Defined only when `X`\n        has feature names that are all strings.\n\n        .. versionadded:: 1.0\n\n    See Also\n    --------\n    EllipticEnvelope : An object for detecting outliers in\n        a Gaussian distributed dataset.\n    EmpiricalCovariance : Maximum likelihood covariance estimator.\n    GraphicalLasso : Sparse inverse covariance estimation\n        with an l1-penalized estimator.\n    GraphicalLassoCV : Sparse inverse covariance with cross-validated\n        choice of the l1 penalty.\n    LedoitWolf : LedoitWolf Estimator.\n    OAS : Oracle Approximating Shrinkage Estimator.\n    ShrunkCovariance : Covariance estimator with shrinkage.\n\n    References\n    ----------\n\n    .. [Rouseeuw1984] P. J. Rousseeuw. Least median of squares regression.\n        J. Am Stat Ass, 79:871, 1984.\n    .. [Rousseeuw] A Fast Algorithm for the Minimum Covariance Determinant\n        Estimator, 1999, American Statistical Association and the American\n        Society for Quality, TECHNOMETRICS\n    .. [ButlerDavies] R. W. Butler, P. L. Davies and M. Jhun,\n        Asymptotics For The Minimum Covariance Determinant Estimator,\n        The Annals of Statistics, 1993, Vol. 21, No. 3, 1385-1400\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> from sklearn.covariance import MinCovDet\n    >>> from sklearn.datasets import make_gaussian_quantiles\n    >>> real_cov = np.array([[.8, .3],\n    ...                      [.3, .4]])\n    >>> rng = np.random.RandomState(0)\n    >>> X = rng.multivariate_normal(mean=[0, 0],\n    ...                                   cov=real_cov,\n    ...                                   size=500)\n    >>> cov = MinCovDet(random_state=0).fit(X)\n    >>> cov.covariance_\n    array([[0.8102, 0.2736],\n           [0.2736, 0.3330]])\n    >>> cov.location_\n    array([0.0769 , 0.0397])\n    '
# WARNING: Decompyle incomplete
