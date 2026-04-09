# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _omp.pyc (Python 3.11)

'''Orthogonal matching pursuit algorithms'''
import warnings
from math import sqrt
from numbers import Integral, Real
import numpy as np
from scipy import linalg
from scipy.linalg.lapack import get_lapack_funcs
from sklearn.base import MultiOutputMixin, RegressorMixin, _fit_context
from sklearn.linear_model._base import LinearModel, _pre_fit
from sklearn.model_selection import check_cv
from sklearn.utils import Bunch, as_float_array, check_array
from sklearn.utils._param_validation import Interval, StrOptions, validate_params
from sklearn.utils.metadata_routing import MetadataRouter, MethodMapping, _raise_for_params, _routing_enabled, process_routing
from sklearn.utils.parallel import Parallel, delayed
from sklearn.utils.validation import FLOAT_DTYPES, validate_data
premature = 'Orthogonal matching pursuit ended prematurely due to linear dependence in the dictionary. The requested precision might not have been met.'

def _cholesky_omp(X, y, n_nonzero_coefs, tol, copy_X, return_path = (None, True, False)):
    '''Orthogonal Matching Pursuit step using the Cholesky decomposition.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        Input dictionary. Columns are assumed to have unit norm.

    y : ndarray of shape (n_samples,)
        Input targets.

    n_nonzero_coefs : int
        Targeted number of non-zero elements.

    tol : float, default=None
        Targeted squared error, if not None overrides n_nonzero_coefs.

    copy_X : bool, default=True
        Whether the design matrix X must be copied by the algorithm. A false
        value is only helpful if X is already Fortran-ordered, otherwise a
        copy is made anyway.

    return_path : bool, default=False
        Whether to return every value of the nonzero coefficients along the
        forward path. Useful for cross-validation.

    Returns
    -------
    gamma : ndarray of shape (n_nonzero_coefs,)
        Non-zero elements of the solution.

    idx : ndarray of shape (n_nonzero_coefs,)
        Indices of the positions of the elements in gamma within the solution
        vector.

    coef : ndarray of shape (n_features, n_nonzero_coefs)
        The first k values of column k correspond to the coefficient value
        for the active features at that step. The lower left triangle contains
        garbage. Only returned if ``return_path=True``.

    n_active : int
        Number of active features at convergence.
    '''
    if copy_X:
        X = X.copy('F')
    else:
        X = np.asfortranarray(X)
    min_float = np.finfo(X.dtype).eps
    (nrm2, swap) = linalg.get_blas_funcs(('nrm2', 'swap'), (X,))
    (potrs,) = get_lapack_funcs(('potrs',), (X,))
    alpha = np.dot(X.T, y)
    residual = y
    gamma = np.empty(0)
    n_active = 0
    indices = np.arange(X.shape[1])
# WARNING: Decompyle incomplete


def _gram_omp(Gram, Xy, n_nonzero_coefs, tol_0, tol, copy_Gram, copy_Xy, return_path = (None, None, True, True, False)):
    '''Orthogonal Matching Pursuit step on a precomputed Gram matrix.

    This function uses the Cholesky decomposition method.

    Parameters
    ----------
    Gram : ndarray of shape (n_features, n_features)
        Gram matrix of the input data matrix.

    Xy : ndarray of shape (n_features,)
        Input targets.

    n_nonzero_coefs : int
        Targeted number of non-zero elements.

    tol_0 : float, default=None
        Squared norm of y, required if tol is not None.

    tol : float, default=None
        Targeted squared error, if not None overrides n_nonzero_coefs.

    copy_Gram : bool, default=True
        Whether the gram matrix must be copied by the algorithm. A false
        value is only helpful if it is already Fortran-ordered, otherwise a
        copy is made anyway.

    copy_Xy : bool, default=True
        Whether the covariance vector Xy must be copied by the algorithm.
        If False, it may be overwritten.

    return_path : bool, default=False
        Whether to return every value of the nonzero coefficients along the
        forward path. Useful for cross-validation.

    Returns
    -------
    gamma : ndarray of shape (n_nonzero_coefs,)
        Non-zero elements of the solution.

    idx : ndarray of shape (n_nonzero_coefs,)
        Indices of the positions of the elements in gamma within the solution
        vector.

    coefs : ndarray of shape (n_features, n_nonzero_coefs)
        The first k values of column k correspond to the coefficient value
        for the active features at that step. The lower left triangle contains
        garbage. Only returned if ``return_path=True``.

    n_active : int
        Number of active features at convergence.
    '''
    Gram = Gram.copy('F') if copy_Gram else np.asfortranarray(Gram)
    if not copy_Xy or Xy.flags.writeable:
        Xy = Xy.copy()
    min_float = np.finfo(Gram.dtype).eps
    (nrm2, swap) = linalg.get_blas_funcs(('nrm2', 'swap'), (Gram,))
    (potrs,) = get_lapack_funcs(('potrs',), (Gram,))
    indices = np.arange(len(Gram))
    alpha = Xy
    tol_curr = tol_0
    delta = 0
    gamma = np.empty(0)
    n_active = 0
# WARNING: Decompyle incomplete

orthogonal_mp = (lambda X = validate_params({
    'X': [
        'array-like'],
    'y': [
        np.ndarray],
    'n_nonzero_coefs': [
        Interval(Integral, 1, None, closed = 'left'),
        None],
    'tol': [
        Interval(Real, 0, None, closed = 'left'),
        None],
    'precompute': [
        'boolean',
        StrOptions({
            'auto'})],
    'copy_X': [
        'boolean'],
    'return_path': [
        'boolean'],
    'return_n_iter': [
        'boolean'] }, prefer_skip_nested_validation = True), y = {
    'n_nonzero_coefs': None,
    'tol': None,
    'precompute': False,
    'copy_X': True,
    'return_path': False,
    'return_n_iter': False }, *, n_nonzero_coefs, tol: X = check_array(X, order = 'F', copy = copy_X)copy_X = Falseif y.ndim == 1:
y = y.reshape(-1, 1)y = check_array(y)if y.shape[1] > 1:
copy_X = True# WARNING: Decompyle incomplete
)()
orthogonal_mp_gram = (lambda Gram = validate_params({
    'Gram': [
        'array-like'],
    'Xy': [
        'array-like'],
    'n_nonzero_coefs': [
        Interval(Integral, 0, None, closed = 'neither'),
        None],
    'tol': [
        Interval(Real, 0, None, closed = 'left'),
        None],
    'norms_squared': [
        'array-like',
        None],
    'copy_Gram': [
        'boolean'],
    'copy_Xy': [
        'boolean'],
    'return_path': [
        'boolean'],
    'return_n_iter': [
        'boolean'] }, prefer_skip_nested_validation = True), Xy = {
    'n_nonzero_coefs': None,
    'tol': None,
    'norms_squared': None,
    'copy_Gram': True,
    'copy_Xy': True,
    'return_path': False,
    'return_n_iter': False }, *, n_nonzero_coefs, tol: Gram = check_array(Gram, order = 'F', copy = copy_Gram)Xy = np.asarray(Xy)if Xy.ndim > 1 and Xy.shape[1] > 1:
copy_Gram = True# WARNING: Decompyle incomplete
)()

class OrthogonalMatchingPursuit(LinearModel, RegressorMixin, MultiOutputMixin):
    """Orthogonal Matching Pursuit model (OMP).

    Read more in the :ref:`User Guide <omp>`.

    Parameters
    ----------
    n_nonzero_coefs : int, default=None
        Desired number of non-zero entries in the solution. Ignored if `tol` is set.
        When `None` and `tol` is also `None`, this value is either set to 10% of
        `n_features` or 1, whichever is greater.

    tol : float, default=None
        Maximum squared norm of the residual. If not None, overrides n_nonzero_coefs.

    fit_intercept : bool, default=True
        Whether to calculate the intercept for this model. If set
        to false, no intercept will be used in calculations
        (i.e. data is expected to be centered).

    precompute : 'auto' or bool, default='auto'
        Whether to use a precomputed Gram and Xy matrix to speed up
        calculations. Improves performance when :term:`n_targets` or
        :term:`n_samples` is very large.

    Attributes
    ----------
    coef_ : ndarray of shape (n_features,) or (n_targets, n_features)
        Parameter vector (w in the formula).

    intercept_ : float or ndarray of shape (n_targets,)
        Independent term in decision function.

    n_iter_ : int or array-like
        Number of active features across every target.

    n_nonzero_coefs_ : int or None
        The number of non-zero coefficients in the solution or `None` when `tol` is
        set. If `n_nonzero_coefs` is None and `tol` is None this value is either set
        to 10% of `n_features` or 1, whichever is greater.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    orthogonal_mp : Solves n_targets Orthogonal Matching Pursuit problems.
    orthogonal_mp_gram :  Solves n_targets Orthogonal Matching Pursuit
        problems using only the Gram matrix X.T * X and the product X.T * y.
    lars_path : Compute Least Angle Regression or Lasso path using LARS algorithm.
    Lars : Least Angle Regression model a.k.a. LAR.
    LassoLars : Lasso model fit with Least Angle Regression a.k.a. Lars.
    sklearn.decomposition.sparse_encode : Generic sparse coding.
        Each column of the result is the solution to a Lasso problem.
    OrthogonalMatchingPursuitCV : Cross-validated
        Orthogonal Matching Pursuit model (OMP).

    Notes
    -----
    Orthogonal matching pursuit was introduced in G. Mallat, Z. Zhang,
    Matching pursuits with time-frequency dictionaries, IEEE Transactions on
    Signal Processing, Vol. 41, No. 12. (December 1993), pp. 3397-3415.
    (https://www.di.ens.fr/~mallat/papiers/MallatPursuit93.pdf)

    This implementation is based on Rubinstein, R., Zibulevsky, M. and Elad,
    M., Efficient Implementation of the K-SVD Algorithm using Batch Orthogonal
    Matching Pursuit Technical Report - CS Technion, April 2008.
    https://www.cs.technion.ac.il/~ronrubin/Publications/KSVD-OMP-v2.pdf

    Examples
    --------
    >>> from sklearn.linear_model import OrthogonalMatchingPursuit
    >>> from sklearn.datasets import make_regression
    >>> X, y = make_regression(noise=4, random_state=0)
    >>> reg = OrthogonalMatchingPursuit().fit(X, y)
    >>> reg.score(X, y)
    0.9991
    >>> reg.predict(X[:1,])
    array([-78.3854])
    """
    _parameter_constraints: dict = {
        'n_nonzero_coefs': [
            Interval(Integral, 1, None, closed = 'left'),
            None],
        'tol': [
            Interval(Real, 0, None, closed = 'left'),
            None],
        'fit_intercept': [
            'boolean'],
        'precompute': [
            StrOptions({
                'auto'}),
            'boolean'] }
    
    def __init__(self = None, *, n_nonzero_coefs, tol, fit_intercept, precompute):
        self.n_nonzero_coefs = n_nonzero_coefs
        self.tol = tol
        self.fit_intercept = fit_intercept
        self.precompute = precompute

    fit = (lambda self, X, y: (X, y) = validate_data(self, X, y, multi_output = True, y_numeric = True, dtype = FLOAT_DTYPES)n_features = X.shape[1](X, y, X_offset, y_offset, X_scale, Gram, Xy) = _pre_fit(X, y, None, self.precompute, self.fit_intercept, copy = True, check_gram = False)if y.ndim == 1:
y = y[(:, np.newaxis)]# WARNING: Decompyle incomplete
)()


def _omp_path_residues(X_train, y_train, X_test, y_test, copy, fit_intercept, max_iter = (True, True, 100)):
    '''Compute the residues on left-out data for a full LARS path.

    Parameters
    ----------
    X_train : ndarray of shape (n_samples, n_features)
        The data to fit the LARS on.

    y_train : ndarray of shape (n_samples)
        The target variable to fit LARS on.

    X_test : ndarray of shape (n_samples, n_features)
        The data to compute the residues on.

    y_test : ndarray of shape (n_samples)
        The target variable to compute the residues on.

    copy : bool, default=True
        Whether X_train, X_test, y_train and y_test should be copied.  If
        False, they may be overwritten.

    fit_intercept : bool, default=True
        Whether to calculate the intercept for this model. If set
        to false, no intercept will be used in calculations
        (i.e. data is expected to be centered).

    max_iter : int, default=100
        Maximum numbers of iterations to perform, therefore maximum features
        to include. 100 by default.

    Returns
    -------
    residues : ndarray of shape (n_samples, max_features)
        Residues of the prediction on the test data.
    '''
    if copy:
        X_train = X_train.copy()
        y_train = y_train.copy()
        X_test = X_test.copy()
        y_test = y_test.copy()
    if fit_intercept:
        X_mean = X_train.mean(axis = 0)
        X_train -= X_mean
        X_test -= X_mean
        y_mean = y_train.mean(axis = 0)
        y_train = as_float_array(y_train, copy = False)
        y_train -= y_mean
        y_test = as_float_array(y_test, copy = False)
        y_test -= y_mean
    coefs = orthogonal_mp(X_train, y_train, n_nonzero_coefs = max_iter, tol = None, precompute = False, copy_X = False, return_path = True)
    if coefs.ndim == 1:
        coefs = coefs[(:, np.newaxis)]
    return np.dot(coefs.T, X_test.T) - y_test


class OrthogonalMatchingPursuitCV(LinearModel, RegressorMixin):
    '''Cross-validated Orthogonal Matching Pursuit model (OMP).

    See glossary entry for :term:`cross-validation estimator`.

    Read more in the :ref:`User Guide <omp>`.

    Parameters
    ----------
    copy : bool, default=True
        Whether the design matrix X must be copied by the algorithm. A false
        value is only helpful if X is already Fortran-ordered, otherwise a
        copy is made anyway.

    fit_intercept : bool, default=True
        Whether to calculate the intercept for this model. If set
        to false, no intercept will be used in calculations
        (i.e. data is expected to be centered).

    max_iter : int, default=None
        Maximum numbers of iterations to perform, therefore maximum features
        to include. 10% of ``n_features`` but at least 5 if available.

    cv : int, cross-validation generator or iterable, default=None
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:

        - None, to use the default 5-fold cross-validation,
        - integer, to specify the number of folds.
        - :term:`CV splitter`,
        - An iterable yielding (train, test) splits as arrays of indices.

        For integer/None inputs, :class:`~sklearn.model_selection.KFold` is used.

        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validation strategies that can be used here.

        .. versionchanged:: 0.22
            ``cv`` default value if None changed from 3-fold to 5-fold.

    n_jobs : int, default=None
        Number of CPUs to use during the cross validation.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    verbose : bool or int, default=False
        Sets the verbosity amount.

    Attributes
    ----------
    intercept_ : float or ndarray of shape (n_targets,)
        Independent term in decision function.

    coef_ : ndarray of shape (n_features,) or (n_targets, n_features)
        Parameter vector (w in the problem formulation).

    n_nonzero_coefs_ : int
        Estimated number of non-zero coefficients giving the best mean squared
        error over the cross-validation folds.

    n_iter_ : int or array-like
        Number of active features across every target for the model refit with
        the best hyperparameters got by cross-validating across all folds.

    n_features_in_ : int
        Number of features seen during :term:`fit`.

        .. versionadded:: 0.24

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of features seen during :term:`fit`. Defined only when `X`
        has feature names that are all strings.

        .. versionadded:: 1.0

    See Also
    --------
    orthogonal_mp : Solves n_targets Orthogonal Matching Pursuit problems.
    orthogonal_mp_gram : Solves n_targets Orthogonal Matching Pursuit
        problems using only the Gram matrix X.T * X and the product X.T * y.
    lars_path : Compute Least Angle Regression or Lasso path using LARS algorithm.
    Lars : Least Angle Regression model a.k.a. LAR.
    LassoLars : Lasso model fit with Least Angle Regression a.k.a. Lars.
    OrthogonalMatchingPursuit : Orthogonal Matching Pursuit model (OMP).
    LarsCV : Cross-validated Least Angle Regression model.
    LassoLarsCV : Cross-validated Lasso model fit with Least Angle Regression.
    sklearn.decomposition.sparse_encode : Generic sparse coding.
        Each column of the result is the solution to a Lasso problem.

    Notes
    -----
    In `fit`, once the optimal number of non-zero coefficients is found through
    cross-validation, the model is fit again using the entire training set.

    Examples
    --------
    >>> from sklearn.linear_model import OrthogonalMatchingPursuitCV
    >>> from sklearn.datasets import make_regression
    >>> X, y = make_regression(n_features=100, n_informative=10,
    ...                        noise=4, random_state=0)
    >>> reg = OrthogonalMatchingPursuitCV(cv=5).fit(X, y)
    >>> reg.score(X, y)
    0.9991
    >>> reg.n_nonzero_coefs_
    np.int64(10)
    >>> reg.predict(X[:1,])
    array([-78.3854])
    '''
    _parameter_constraints: dict = {
        'copy': [
            'boolean'],
        'fit_intercept': [
            'boolean'],
        'max_iter': [
            Interval(Integral, 0, None, closed = 'left'),
            None],
        'cv': [
            'cv_object'],
        'n_jobs': [
            Integral,
            None],
        'verbose': [
            'verbose'] }
    
    def __init__(self = None, *, copy, fit_intercept, max_iter, cv, n_jobs, verbose):
        self.copy = copy
        self.fit_intercept = fit_intercept
        self.max_iter = max_iter
        self.cv = cv
        self.n_jobs = n_jobs
        self.verbose = verbose

    fit = (lambda self, X, y: pass# WARNING: Decompyle incomplete
)()
    
    def get_metadata_routing(self):
        '''Get metadata routing of this object.

        Please check :ref:`User Guide <metadata_routing>` on how the routing
        mechanism works.

        .. versionadded:: 1.4

        Returns
        -------
        routing : MetadataRouter
            A :class:`~sklearn.utils.metadata_routing.MetadataRouter` encapsulating
            routing information.
        '''
        router = MetadataRouter(owner = self).add(splitter = self.cv, method_mapping = MethodMapping().add(caller = 'fit', callee = 'split'))
        return router
