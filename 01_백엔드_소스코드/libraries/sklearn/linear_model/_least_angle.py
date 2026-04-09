# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _least_angle.pyc (Python 3.11)

'''
Least Angle Regression algorithm. See the documentation on the
Generalized Linear Model for a complete discussion.
'''
import sys
import warnings
from math import log
from numbers import Integral, Real
import numpy as np
from scipy import interpolate, linalg
from scipy.linalg.lapack import get_lapack_funcs
from sklearn.base import MultiOutputMixin, RegressorMixin, _fit_context
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model._base import LinearModel, LinearRegression, _preprocess_data
from sklearn.model_selection import check_cv
from sklearn.utils import Bunch, arrayfuncs, as_float_array, check_random_state
from sklearn.utils._metadata_requests import MetadataRouter, MethodMapping, _raise_for_params, _routing_enabled, process_routing
from sklearn.utils._param_validation import Hidden, Interval, StrOptions, validate_params
from sklearn.utils.parallel import Parallel, delayed
from sklearn.utils.validation import validate_data
SOLVE_TRIANGULAR_ARGS = {
    'check_finite': False }
lars_path = (lambda X = validate_params({
    'X': [
        np.ndarray,
        None],
    'y': [
        np.ndarray,
        None],
    'Xy': [
        np.ndarray,
        None],
    'Gram': [
        StrOptions({
            'auto'}),
        'boolean',
        np.ndarray,
        None],
    'max_iter': [
        Interval(Integral, 0, None, closed = 'left')],
    'alpha_min': [
        Interval(Real, 0, None, closed = 'left')],
    'method': [
        StrOptions({
            'lar',
            'lasso'})],
    'copy_X': [
        'boolean'],
    'eps': [
        Interval(Real, 0, None, closed = 'neither'),
        None],
    'copy_Gram': [
        'boolean'],
    'verbose': [
        'verbose'],
    'return_path': [
        'boolean'],
    'return_n_iter': [
        'boolean'],
    'positive': [
        'boolean'] }, prefer_skip_nested_validation = True), y = (None,), Xy = {
    'Gram': None,
    'max_iter': 500,
    'alpha_min': 0,
    'method': 'lar',
    'copy_X': True,
    'eps': np.finfo(float).eps,
    'copy_Gram': True,
    'verbose': 0,
    'return_path': True,
    'return_n_iter': False,
    'positive': False }, *, Gram, max_iter, alpha_min: pass# WARNING: Decompyle incomplete
)()
lars_path_gram = (lambda Xy = validate_params({
    'Xy': [
        np.ndarray],
    'Gram': [
        np.ndarray],
    'n_samples': [
        Interval(Integral, 0, None, closed = 'left')],
    'max_iter': [
        Interval(Integral, 0, None, closed = 'left')],
    'alpha_min': [
        Interval(Real, 0, None, closed = 'left')],
    'method': [
        StrOptions({
            'lar',
            'lasso'})],
    'copy_X': [
        'boolean'],
    'eps': [
        Interval(Real, 0, None, closed = 'neither'),
        None],
    'copy_Gram': [
        'boolean'],
    'verbose': [
        'verbose'],
    'return_path': [
        'boolean'],
    'return_n_iter': [
        'boolean'],
    'positive': [
        'boolean'] }, prefer_skip_nested_validation = True), Gram = {
    'max_iter': 500,
    'alpha_min': 0,
    'method': 'lar',
    'copy_X': True,
    'eps': np.finfo(float).eps,
    'copy_Gram': True,
    'verbose': 0,
    'return_path': True,
    'return_n_iter': False,
    'positive': False }, *, n_samples, max_iter: _lars_path_solver(X = None, y = None, Xy = Xy, Gram = Gram, n_samples = n_samples, max_iter = max_iter, alpha_min = alpha_min, method = method, copy_X = copy_X, eps = eps, copy_Gram = copy_Gram, verbose = verbose, return_path = return_path, return_n_iter = return_n_iter, positive = positive))()

def _lars_path_solver(X, y, Xy, Gram, n_samples, max_iter, alpha_min, method, copy_X, eps, copy_Gram, verbose, return_path, return_n_iter, positive = (None, None, None, 500, 0, 'lar', True, np.finfo(float).eps, True, 0, True, False, False)):
    '''Compute Least Angle Regression or Lasso path using LARS algorithm [1]

    The optimization objective for the case method=\'lasso\' is::

    (1 / (2 * n_samples)) * ||y - Xw||^2_2 + alpha * ||w||_1

    in the case of method=\'lar\', the objective function is only known in
    the form of an implicit equation (see discussion in [1])

    Read more in the :ref:`User Guide <least_angle_regression>`.

    Parameters
    ----------
    X : None or ndarray of shape (n_samples, n_features)
        Input data. Note that if X is None then Gram must be specified,
        i.e., cannot be None or False.

    y : None or ndarray of shape (n_samples,)
        Input targets.

    Xy : array-like of shape (n_features,), default=None
        `Xy = np.dot(X.T, y)` that can be precomputed. It is useful
        only when the Gram matrix is precomputed.

    Gram : None, \'auto\' or array-like of shape (n_features, n_features),             default=None
        Precomputed Gram matrix `(X\' * X)`, if ``\'auto\'``, the Gram
        matrix is precomputed from the given X, if there are more samples
        than features.

    n_samples : int or float, default=None
        Equivalent size of sample. If `None`, it will be `n_samples`.

    max_iter : int, default=500
        Maximum number of iterations to perform, set to infinity for no limit.

    alpha_min : float, default=0
        Minimum correlation along the path. It corresponds to the
        regularization parameter alpha parameter in the Lasso.

    method : {\'lar\', \'lasso\'}, default=\'lar\'
        Specifies the returned model. Select ``\'lar\'`` for Least Angle
        Regression, ``\'lasso\'`` for the Lasso.

    copy_X : bool, default=True
        If ``False``, ``X`` is overwritten.

    eps : float, default=np.finfo(float).eps
        The machine-precision regularization in the computation of the
        Cholesky diagonal factors. Increase this for very ill-conditioned
        systems. Unlike the ``tol`` parameter in some iterative
        optimization-based algorithms, this parameter does not control
        the tolerance of the optimization.

    copy_Gram : bool, default=True
        If ``False``, ``Gram`` is overwritten.

    verbose : int, default=0
        Controls output verbosity.

    return_path : bool, default=True
        If ``return_path==True`` returns the entire path, else returns only the
        last point of the path.

    return_n_iter : bool, default=False
        Whether to return the number of iterations.

    positive : bool, default=False
        Restrict coefficients to be >= 0.
        This option is only allowed with method \'lasso\'. Note that the model
        coefficients will not converge to the ordinary-least-squares solution
        for small values of alpha. Only coefficients up to the smallest alpha
        value (``alphas_[alphas_ > 0.].min()`` when fit_path=True) reached by
        the stepwise Lars-Lasso algorithm are typically in congruence with the
        solution of the coordinate descent lasso_path function.

    Returns
    -------
    alphas : array-like of shape (n_alphas + 1,)
        Maximum of covariances (in absolute value) at each iteration.
        ``n_alphas`` is either ``max_iter``, ``n_features`` or the
        number of nodes in the path with ``alpha >= alpha_min``, whichever
        is smaller.

    active : array-like of shape (n_alphas,)
        Indices of active variables at the end of the path.

    coefs : array-like of shape (n_features, n_alphas + 1)
        Coefficients along the path

    n_iter : int
        Number of iterations run. Returned only if return_n_iter is set
        to True.

    See Also
    --------
    lasso_path
    LassoLars
    Lars
    LassoLarsCV
    LarsCV
    sklearn.decomposition.sparse_encode

    References
    ----------
    .. [1] "Least Angle Regression", Efron et al.
           http://statweb.stanford.edu/~tibs/ftp/lars.pdf

    .. [2] `Wikipedia entry on the Least-angle regression
           <https://en.wikipedia.org/wiki/Least-angle_regression>`_

    .. [3] `Wikipedia entry on the Lasso
           <https://en.wikipedia.org/wiki/Lasso_(statistics)>`_

    '''
    pass
# WARNING: Decompyle incomplete


class Lars(LinearModel, RegressorMixin, MultiOutputMixin):
    """Least Angle Regression model a.k.a. LAR.

    Read more in the :ref:`User Guide <least_angle_regression>`.

    Parameters
    ----------
    fit_intercept : bool, default=True
        Whether to calculate the intercept for this model. If set
        to false, no intercept will be used in calculations
        (i.e. data is expected to be centered).

    verbose : bool or int, default=False
        Sets the verbosity amount.

    precompute : bool, 'auto' or array-like , default='auto'
        Whether to use a precomputed Gram matrix to speed up
        calculations. If set to ``'auto'`` let us decide. The Gram
        matrix can also be passed as argument.

    n_nonzero_coefs : int, default=500
        Target number of non-zero coefficients. Use ``np.inf`` for no limit.

    eps : float, default=np.finfo(float).eps
        The machine-precision regularization in the computation of the
        Cholesky diagonal factors. Increase this for very ill-conditioned
        systems. Unlike the ``tol`` parameter in some iterative
        optimization-based algorithms, this parameter does not control
        the tolerance of the optimization.

    copy_X : bool, default=True
        If ``True``, X will be copied; else, it may be overwritten.

    fit_path : bool, default=True
        If True the full path is stored in the ``coef_path_`` attribute.
        If you compute the solution for a large problem or many targets,
        setting ``fit_path`` to ``False`` will lead to a speedup, especially
        with a small alpha.

    jitter : float, default=None
        Upper bound on a uniform noise parameter to be added to the
        `y` values, to satisfy the model's assumption of
        one-at-a-time computations. Might help with stability.

        .. versionadded:: 0.23

    random_state : int, RandomState instance or None, default=None
        Determines random number generation for jittering. Pass an int
        for reproducible output across multiple function calls.
        See :term:`Glossary <random_state>`. Ignored if `jitter` is None.

        .. versionadded:: 0.23

    Attributes
    ----------
    alphas_ : array-like of shape (n_alphas + 1,) or list of such arrays
        Maximum of covariances (in absolute value) at each iteration.
        ``n_alphas`` is either ``max_iter``, ``n_features`` or the
        number of nodes in the path with ``alpha >= alpha_min``, whichever
        is smaller. If this is a list of array-like, the length of the outer
        list is `n_targets`.

    active_ : list of shape (n_alphas,) or list of such lists
        Indices of active variables at the end of the path.
        If this is a list of list, the length of the outer list is `n_targets`.

    coef_path_ : array-like of shape (n_features, n_alphas + 1) or list             of such arrays
        The varying values of the coefficients along the path. It is not
        present if the ``fit_path`` parameter is ``False``. If this is a list
        of array-like, the length of the outer list is `n_targets`.

    coef_ : array-like of shape (n_features,) or (n_targets, n_features)
        Parameter vector (w in the formulation formula).

    intercept_ : float or array-like of shape (n_targets,)
        Independent term in decision function.

    n_iter_ : array-like or int
        The number of iterations taken by lars_path to find the
        grid of alphas for each target.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    lars_path: Compute Least Angle Regression or Lasso
        path using LARS algorithm.
    LarsCV : Cross-validated Least Angle Regression model.
    sklearn.decomposition.sparse_encode : Sparse coding.

    Examples
    --------
    >>> from sklearn import linear_model
    >>> reg = linear_model.Lars(n_nonzero_coefs=1)
    >>> reg.fit([[-1, 1], [0, 0], [1, 1]], [-1.1111, 0, -1.1111])
    Lars(n_nonzero_coefs=1)
    >>> print(reg.coef_)
    [ 0. -1.11]
    """
    _parameter_constraints: dict = {
        'fit_intercept': [
            'boolean'],
        'verbose': [
            'verbose'],
        'precompute': [
            'boolean',
            StrOptions({
                'auto'}),
            np.ndarray,
            Hidden(None)],
        'n_nonzero_coefs': [
            Interval(Integral, 1, None, closed = 'left')],
        'eps': [
            Interval(Real, 0, None, closed = 'left')],
        'copy_X': [
            'boolean'],
        'fit_path': [
            'boolean'],
        'jitter': [
            Interval(Real, 0, None, closed = 'left'),
            None],
        'random_state': [
            'random_state'] }
    method = 'lar'
    positive = False
    
    def __init__(self = None, *, fit_intercept, verbose, precompute, n_nonzero_coefs, eps, copy_X, fit_path, jitter, random_state):
        self.fit_intercept = fit_intercept
        self.verbose = verbose
        self.precompute = precompute
        self.n_nonzero_coefs = n_nonzero_coefs
        self.eps = eps
        self.copy_X = copy_X
        self.fit_path = fit_path
        self.jitter = jitter
        self.random_state = random_state

    _get_gram = (lambda precompute, X, y: if not hasattr(precompute, '__array__'):
if not precompute is True:
if (precompute == 'auto' or X.shape[0] > X.shape[1] or precompute == 'auto') and y.shape[1] > 1:
precompute = np.dot(X.T, X)precompute)()
    
    def _fit(self, X, y, max_iter, alpha, fit_path, Xy = (None,)):
        '''Auxiliary method to fit the model using X, y as training data'''
        n_features = X.shape[1]
        (X, y, X_offset, y_offset, X_scale, _) = _preprocess_data(X, y, fit_intercept = self.fit_intercept, copy = self.copy_X)
        if y.ndim == 1:
            y = y[(:, np.newaxis)]
        n_targets = y.shape[1]
        Gram = self._get_gram(self.precompute, X, y)
        self.alphas_ = []
        self.n_iter_ = []
        self.coef_ = np.empty((n_targets, n_features), dtype = X.dtype)
    # WARNING: Decompyle incomplete

    fit = (lambda self, X, y, Xy = (None,): (X, y) = validate_data(self, X, y, force_writeable = True, y_numeric = True, multi_output = True)alpha = getattr(self, 'alpha', 0)if hasattr(self, 'n_nonzero_coefs'):
alpha = 0max_iter = self.n_nonzero_coefselse:
max_iter = self.max_iter# WARNING: Decompyle incomplete
)()


class LassoLars(Lars):
    __module__ = __name__
    __qualname__ = 'LassoLars'
    __doc__ = "Lasso model fit with Least Angle Regression a.k.a. Lars.\n\n    It is a Linear Model trained with an L1 prior as regularizer.\n\n    The optimization objective for Lasso is::\n\n    (1 / (2 * n_samples)) * ||y - Xw||^2_2 + alpha * ||w||_1\n\n    Read more in the :ref:`User Guide <least_angle_regression>`.\n\n    Parameters\n    ----------\n    alpha : float, default=1.0\n        Constant that multiplies the penalty term. Defaults to 1.0.\n        ``alpha = 0`` is equivalent to an ordinary least square, solved\n        by :class:`LinearRegression`. For numerical reasons, using\n        ``alpha = 0`` with the LassoLars object is not advised and you\n        should prefer the LinearRegression object.\n\n    fit_intercept : bool, default=True\n        Whether to calculate the intercept for this model. If set\n        to false, no intercept will be used in calculations\n        (i.e. data is expected to be centered).\n\n    verbose : bool or int, default=False\n        Sets the verbosity amount.\n\n    precompute : bool, 'auto' or array-like, default='auto'\n        Whether to use a precomputed Gram matrix to speed up\n        calculations. If set to ``'auto'`` let us decide. The Gram\n        matrix can also be passed as argument.\n\n    max_iter : int, default=500\n        Maximum number of iterations to perform.\n\n    eps : float, default=np.finfo(float).eps\n        The machine-precision regularization in the computation of the\n        Cholesky diagonal factors. Increase this for very ill-conditioned\n        systems. Unlike the ``tol`` parameter in some iterative\n        optimization-based algorithms, this parameter does not control\n        the tolerance of the optimization.\n\n    copy_X : bool, default=True\n        If True, X will be copied; else, it may be overwritten.\n\n    fit_path : bool, default=True\n        If ``True`` the full path is stored in the ``coef_path_`` attribute.\n        If you compute the solution for a large problem or many targets,\n        setting ``fit_path`` to ``False`` will lead to a speedup, especially\n        with a small alpha.\n\n    positive : bool, default=False\n        Restrict coefficients to be >= 0. Be aware that you might want to\n        remove fit_intercept which is set True by default.\n        Under the positive restriction the model coefficients will not converge\n        to the ordinary-least-squares solution for small values of alpha.\n        Only coefficients up to the smallest alpha value (``alphas_[alphas_ >\n        0.].min()`` when fit_path=True) reached by the stepwise Lars-Lasso\n        algorithm are typically in congruence with the solution of the\n        coordinate descent Lasso estimator.\n\n    jitter : float, default=None\n        Upper bound on a uniform noise parameter to be added to the\n        `y` values, to satisfy the model's assumption of\n        one-at-a-time computations. Might help with stability.\n\n        .. versionadded:: 0.23\n\n    random_state : int, RandomState instance or None, default=None\n        Determines random number generation for jittering. Pass an int\n        for reproducible output across multiple function calls.\n        See :term:`Glossary <random_state>`. Ignored if `jitter` is None.\n\n        .. versionadded:: 0.23\n\n    Attributes\n    ----------\n    alphas_ : array-like of shape (n_alphas + 1,) or list of such arrays\n        Maximum of covariances (in absolute value) at each iteration.\n        ``n_alphas`` is either ``max_iter``, ``n_features`` or the\n        number of nodes in the path with ``alpha >= alpha_min``, whichever\n        is smaller. If this is a list of array-like, the length of the outer\n        list is `n_targets`.\n\n    active_ : list of length n_alphas or list of such lists\n        Indices of active variables at the end of the path.\n        If this is a list of list, the length of the outer list is `n_targets`.\n\n    coef_path_ : array-like of shape (n_features, n_alphas + 1) or list             of such arrays\n        If a list is passed it's expected to be one of n_targets such arrays.\n        The varying values of the coefficients along the path. It is not\n        present if the ``fit_path`` parameter is ``False``. If this is a list\n        of array-like, the length of the outer list is `n_targets`.\n\n    coef_ : array-like of shape (n_features,) or (n_targets, n_features)\n        Parameter vector (w in the formulation formula).\n\n    intercept_ : float or array-like of shape (n_targets,)\n        Independent term in decision function.\n\n    n_iter_ : array-like or int\n        The number of iterations taken by lars_path to find the\n        grid of alphas for each target.\n\n    n_features_in_ : int\n        Number of features seen during :term:`fit`.\n\n        .. versionadded:: 0.24\n\n    feature_names_in_ : ndarray of shape (`n_features_in_`,)\n        Names of features seen during :term:`fit`. Defined only when `X`\n        has feature names that are all strings.\n\n        .. versionadded:: 1.0\n\n    See Also\n    --------\n    lars_path : Compute Least Angle Regression or Lasso\n        path using LARS algorithm.\n    lasso_path : Compute Lasso path with coordinate descent.\n    Lasso : Linear Model trained with L1 prior as\n        regularizer (aka the Lasso).\n    LassoCV : Lasso linear model with iterative fitting\n        along a regularization path.\n    LassoLarsCV: Cross-validated Lasso, using the LARS algorithm.\n    LassoLarsIC : Lasso model fit with Lars using BIC\n        or AIC for model selection.\n    sklearn.decomposition.sparse_encode : Sparse coding.\n\n    Examples\n    --------\n    >>> from sklearn import linear_model\n    >>> reg = linear_model.LassoLars(alpha=0.01)\n    >>> reg.fit([[-1, 1], [0, 0], [1, 1]], [-1, 0, -1])\n    LassoLars(alpha=0.01)\n    >>> print(reg.coef_)\n    [ 0.         -0.955]\n    "
# WARNING: Decompyle incomplete


def _check_copy_and_writeable(array, copy = (False,)):
    if not copy or array.flags.writeable:
        return array.copy()


def _lars_path_residues(X_train, y_train, X_test, y_test, Gram, copy, method, verbose, fit_intercept, max_iter, eps, positive = (None, True, 'lar', False, True, 500, np.finfo(float).eps, False)):
    """Compute the residues on left-out data for a full LARS path

    Parameters
    -----------
    X_train : array-like of shape (n_samples, n_features)
        The data to fit the LARS on

    y_train : array-like of shape (n_samples,)
        The target variable to fit LARS on

    X_test : array-like of shape (n_samples, n_features)
        The data to compute the residues on

    y_test : array-like of shape (n_samples,)
        The target variable to compute the residues on

    Gram : None, 'auto' or array-like of shape (n_features, n_features),             default=None
        Precomputed Gram matrix (X' * X), if ``'auto'``, the Gram
        matrix is precomputed from the given X, if there are more samples
        than features

    copy : bool, default=True
        Whether X_train, X_test, y_train and y_test should be copied;
        if False, they may be overwritten.

    method : {'lar' , 'lasso'}, default='lar'
        Specifies the returned model. Select ``'lar'`` for Least Angle
        Regression, ``'lasso'`` for the Lasso.

    verbose : bool or int, default=False
        Sets the amount of verbosity

    fit_intercept : bool, default=True
        whether to calculate the intercept for this model. If set
        to false, no intercept will be used in calculations
        (i.e. data is expected to be centered).

    positive : bool, default=False
        Restrict coefficients to be >= 0. Be aware that you might want to
        remove fit_intercept which is set True by default.
        See reservations for using this option in combination with method
        'lasso' for expected small values of alpha in the doc of LassoLarsCV
        and LassoLarsIC.

    max_iter : int, default=500
        Maximum number of iterations to perform.

    eps : float, default=np.finfo(float).eps
        The machine-precision regularization in the computation of the
        Cholesky diagonal factors. Increase this for very ill-conditioned
        systems. Unlike the ``tol`` parameter in some iterative
        optimization-based algorithms, this parameter does not control
        the tolerance of the optimization.

    Returns
    --------
    alphas : array-like of shape (n_alphas,)
        Maximum of covariances (in absolute value) at each iteration.
        ``n_alphas`` is either ``max_iter`` or ``n_features``, whichever
        is smaller.

    active : list
        Indices of active variables at the end of the path.

    coefs : array-like of shape (n_features, n_alphas)
        Coefficients along the path

    residues : array-like of shape (n_alphas, n_samples)
        Residues of the prediction on the test data
    """
    X_train = _check_copy_and_writeable(X_train, copy)
    y_train = _check_copy_and_writeable(y_train, copy)
    X_test = _check_copy_and_writeable(X_test, copy)
    y_test = _check_copy_and_writeable(y_test, copy)
    if fit_intercept:
        X_mean = X_train.mean(axis = 0)
        X_train -= X_mean
        X_test -= X_mean
        y_mean = y_train.mean(axis = 0)
        y_train = as_float_array(y_train, copy = False)
        y_train -= y_mean
        y_test = as_float_array(y_test, copy = False)
        y_test -= y_mean
    (alphas, active, coefs) = lars_path(X_train, y_train, Gram = Gram, copy_X = False, copy_Gram = False, method = method, verbose = max(0, verbose - 1), max_iter = max_iter, eps = eps, positive = positive)
    residues = np.dot(X_test, coefs) - y_test[(:, np.newaxis)]
    return (alphas, active, coefs, residues.T)


class LarsCV(Lars):
    pass
# WARNING: Decompyle incomplete


class LassoLarsCV(LarsCV):
    __module__ = __name__
    __qualname__ = 'LassoLarsCV'
    __doc__ = "Cross-validated Lasso, using the LARS algorithm.\n\n    See glossary entry for :term:`cross-validation estimator`.\n\n    The optimization objective for Lasso is::\n\n    (1 / (2 * n_samples)) * ||y - Xw||^2_2 + alpha * ||w||_1\n\n    Read more in the :ref:`User Guide <least_angle_regression>`.\n\n    Parameters\n    ----------\n    fit_intercept : bool, default=True\n        Whether to calculate the intercept for this model. If set\n        to false, no intercept will be used in calculations\n        (i.e. data is expected to be centered).\n\n    verbose : bool or int, default=False\n        Sets the verbosity amount.\n\n    max_iter : int, default=500\n        Maximum number of iterations to perform.\n\n    precompute : bool or 'auto' , default='auto'\n        Whether to use a precomputed Gram matrix to speed up\n        calculations. If set to ``'auto'`` let us decide. The Gram matrix\n        cannot be passed as argument since we will use only subsets of X.\n\n    cv : int, cross-validation generator or an iterable, default=None\n        Determines the cross-validation splitting strategy.\n        Possible inputs for cv are:\n\n        - None, to use the default 5-fold cross-validation,\n        - integer, to specify the number of folds.\n        - :term:`CV splitter`,\n        - An iterable yielding (train, test) splits as arrays of indices.\n\n        For integer/None inputs, :class:`~sklearn.model_selection.KFold` is used.\n\n        Refer :ref:`User Guide <cross_validation>` for the various\n        cross-validation strategies that can be used here.\n\n        .. versionchanged:: 0.22\n            ``cv`` default value if None changed from 3-fold to 5-fold.\n\n    max_n_alphas : int, default=1000\n        The maximum number of points on the path used to compute the\n        residuals in the cross-validation.\n\n    n_jobs : int or None, default=None\n        Number of CPUs to use during the cross validation.\n        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.\n        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`\n        for more details.\n\n    eps : float, default=np.finfo(float).eps\n        The machine-precision regularization in the computation of the\n        Cholesky diagonal factors. Increase this for very ill-conditioned\n        systems. Unlike the ``tol`` parameter in some iterative\n        optimization-based algorithms, this parameter does not control\n        the tolerance of the optimization.\n\n    copy_X : bool, default=True\n        If True, X will be copied; else, it may be overwritten.\n\n    positive : bool, default=False\n        Restrict coefficients to be >= 0. Be aware that you might want to\n        remove fit_intercept which is set True by default.\n        Under the positive restriction the model coefficients do not converge\n        to the ordinary-least-squares solution for small values of alpha.\n        Only coefficients up to the smallest alpha value (``alphas_[alphas_ >\n        0.].min()`` when fit_path=True) reached by the stepwise Lars-Lasso\n        algorithm are typically in congruence with the solution of the\n        coordinate descent Lasso estimator.\n        As a consequence using LassoLarsCV only makes sense for problems where\n        a sparse solution is expected and/or reached.\n\n    Attributes\n    ----------\n    coef_ : array-like of shape (n_features,)\n        parameter vector (w in the formulation formula)\n\n    intercept_ : float\n        independent term in decision function.\n\n    coef_path_ : array-like of shape (n_features, n_alphas)\n        the varying values of the coefficients along the path\n\n    alpha_ : float\n        the estimated regularization parameter alpha\n\n    alphas_ : array-like of shape (n_alphas,)\n        the different values of alpha along the path\n\n    cv_alphas_ : array-like of shape (n_cv_alphas,)\n        all the values of alpha along the path for the different folds\n\n    mse_path_ : array-like of shape (n_folds, n_cv_alphas)\n        the mean square error on left-out for each fold along the path\n        (alpha values given by ``cv_alphas``)\n\n    n_iter_ : array-like or int\n        the number of iterations run by Lars with the optimal alpha.\n\n    active_ : list of int\n        Indices of active variables at the end of the path.\n\n    n_features_in_ : int\n        Number of features seen during :term:`fit`.\n\n        .. versionadded:: 0.24\n\n    feature_names_in_ : ndarray of shape (`n_features_in_`,)\n        Names of features seen during :term:`fit`. Defined only when `X`\n        has feature names that are all strings.\n\n        .. versionadded:: 1.0\n\n    See Also\n    --------\n    lars_path : Compute Least Angle Regression or Lasso\n        path using LARS algorithm.\n    lasso_path : Compute Lasso path with coordinate descent.\n    Lasso : Linear Model trained with L1 prior as\n        regularizer (aka the Lasso).\n    LassoCV : Lasso linear model with iterative fitting\n        along a regularization path.\n    LassoLars : Lasso model fit with Least Angle Regression a.k.a. Lars.\n    LassoLarsIC : Lasso model fit with Lars using BIC\n        or AIC for model selection.\n    sklearn.decomposition.sparse_encode : Sparse coding.\n\n    Notes\n    -----\n    The object solves the same problem as the\n    :class:`~sklearn.linear_model.LassoCV` object. However, unlike the\n    :class:`~sklearn.linear_model.LassoCV`, it find the relevant alphas values\n    by itself. In general, because of this property, it will be more stable.\n    However, it is more fragile to heavily multicollinear datasets.\n\n    It is more efficient than the :class:`~sklearn.linear_model.LassoCV` if\n    only a small number of features are selected compared to the total number,\n    for instance if there are very few samples compared to the number of\n    features.\n\n    In `fit`, once the best parameter `alpha` is found through\n    cross-validation, the model is fit again using the entire training set.\n\n    Examples\n    --------\n    >>> from sklearn.linear_model import LassoLarsCV\n    >>> from sklearn.datasets import make_regression\n    >>> X, y = make_regression(noise=4.0, random_state=0)\n    >>> reg = LassoLarsCV(cv=5).fit(X, y)\n    >>> reg.score(X, y)\n    0.9993\n    >>> reg.alpha_\n    np.float64(0.3972)\n    >>> reg.predict(X[:1,])\n    array([-78.4831])\n    "
# WARNING: Decompyle incomplete


class LassoLarsIC(LassoLars):
    pass
# WARNING: Decompyle incomplete
