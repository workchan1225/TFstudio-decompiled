# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _logistic.pyc (Python 3.11)

'''
Logistic Regression
'''
import numbers
import warnings
from numbers import Integral, Real
import numpy as np
from scipy import optimize
from sklearn._loss.loss import HalfBinomialLoss, HalfMultinomialLoss
from sklearn.base import _fit_context
from sklearn.linear_model._base import BaseEstimator, LinearClassifierMixin, SparseCoefMixin
from sklearn.linear_model._glm.glm import NewtonCholeskySolver
from sklearn.linear_model._linear_loss import LinearModelLoss
from sklearn.linear_model._sag import sag_solver
from sklearn.metrics import get_scorer, get_scorer_names
from sklearn.model_selection import check_cv
from sklearn.preprocessing import LabelEncoder
from sklearn.svm._base import _fit_liblinear
from sklearn.utils import Bunch, check_array, check_consistent_length, check_random_state, compute_class_weight
from sklearn.utils._param_validation import Hidden, Interval, StrOptions
from sklearn.utils.extmath import row_norms, softmax
from sklearn.utils.fixes import _get_additional_lbfgs_options_dict
from sklearn.utils.metadata_routing import MetadataRouter, MethodMapping, _raise_for_params, _routing_enabled, process_routing
from sklearn.utils.multiclass import check_classification_targets
from sklearn.utils.optimize import _check_optimize_result, _newton_cg
from sklearn.utils.parallel import Parallel, delayed
from sklearn.utils.validation import _check_method_params, _check_sample_weight, check_is_fitted, validate_data
_LOGISTIC_SOLVER_CONVERGENCE_MSG = 'Please also refer to the documentation for alternative solver options:\n    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression'

def _check_solver(solver, penalty, dual):
    if solver not in ('liblinear', 'saga') and penalty not in ('l2', None):
        raise ValueError(f'''Solver {solver} supports only \'l2\' or None penalties, got {penalty} penalty.''')
    if solver != 'liblinear' and dual:
        raise ValueError(f'''Solver {solver} supports only dual=False, got dual={dual}''')
    if penalty == 'elasticnet' and solver != 'saga':
        raise ValueError(f'''Only \'saga\' solver supports elasticnet penalty, got solver={solver}.''')
# WARNING: Decompyle incomplete


def _logistic_regression_path(X = None, y = {
    'Cs': 10,
    'fit_intercept': True,
    'max_iter': 100,
    'tol': 0.0001,
    'verbose': 0,
    'solver': 'lbfgs',
    'coef': None,
    'class_weight': None,
    'dual': False,
    'penalty': 'l2',
    'intercept_scaling': 1,
    'random_state': None,
    'check_input': True,
    'max_squared_sum': None,
    'sample_weight': None,
    'l1_ratio': None,
    'n_threads': 1 }, *, classes, Cs, fit_intercept, max_iter, tol, verbose, solver, coef, class_weight, dual, penalty, intercept_scaling, random_state, check_input, max_squared_sum, sample_weight, l1_ratio, n_threads):
    '''Compute a Logistic Regression model for a list of regularization
    parameters.

    This is an implementation that uses the result of the previous model
    to speed up computations along the set of solutions, making it faster
    than sequentially calling LogisticRegression for the different parameters.
    Note that there will be no speedup with liblinear solver, since it does
    not handle warm-starting.

    Read more in the :ref:`User Guide <logistic_regression>`.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        Input data.

    y : array-like of shape (n_samples,) or (n_samples, n_targets)
        Input data, target values.

    classes : ndarray
        A list of class labels known to the classifier.

    Cs : int or array-like of shape (n_cs,), default=10
        List of values for the regularization parameter or integer specifying
        the number of regularization parameters that should be used. In this
        case, the parameters will be chosen in a logarithmic scale between
        1e-4 and 1e4.

    fit_intercept : bool, default=True
        Whether to fit an intercept for the model. In this case the shape of
        the returned array is (n_cs, n_features + 1).

    max_iter : int, default=100
        Maximum number of iterations for the solver.

    tol : float, default=1e-4
        Stopping criterion. For the newton-cg and lbfgs solvers, the iteration
        will stop when ``max{|g_i | i = 1, ..., n} <= tol``
        where ``g_i`` is the i-th component of the gradient.

    verbose : int, default=0
        For the liblinear and lbfgs solvers set verbose to any positive
        number for verbosity.

    solver : {\'lbfgs\', \'liblinear\', \'newton-cg\', \'newton-cholesky\', \'sag\', \'saga\'},             default=\'lbfgs\'
        Numerical solver to use.

    coef : array-like of shape (n_classes, features + int(fit_intercept)) or             (1, n_features + int(fit_intercept)) or             (n_features + int(fit_intercept)), default=None
        Initialization value for coefficients of logistic regression.
        Useless for liblinear solver.

    class_weight : dict or \'balanced\', default=None
        Weights associated with classes in the form ``{class_label: weight}``.
        If not given, all classes are supposed to have weight one.

        The "balanced" mode uses the values of y to automatically adjust
        weights inversely proportional to class frequencies in the input data
        as ``n_samples / (n_classes * np.bincount(y))``.

        Note that these weights will be multiplied with sample_weight (passed
        through the fit method) if sample_weight is specified.

    dual : bool, default=False
        Dual or primal formulation. Dual formulation is only implemented for
        l2 penalty with liblinear solver. Prefer dual=False when
        n_samples > n_features.

    penalty : {\'l1\', \'l2\', \'elasticnet\'}, default=\'l2\'
        Used to specify the norm used in the penalization. The \'newton-cg\',
        \'sag\' and \'lbfgs\' solvers support only l2 penalties. \'elasticnet\' is
        only supported by the \'saga\' solver.

    intercept_scaling : float, default=1.
        Useful only when the solver `liblinear` is used
        and `self.fit_intercept` is set to `True`. In this case, `x` becomes
        `[x, self.intercept_scaling]`,
        i.e. a "synthetic" feature with constant value equal to
        `intercept_scaling` is appended to the instance vector.
        The intercept becomes
        ``intercept_scaling * synthetic_feature_weight``.

        .. note::
            The synthetic feature weight is subject to L1 or L2
            regularization as all other features.
            To lessen the effect of regularization on synthetic feature weight
            (and therefore on the intercept) `intercept_scaling` has to be increased.

    random_state : int, RandomState instance, default=None
        Used when ``solver`` == \'sag\', \'saga\' or \'liblinear\' to shuffle the
        data. See :term:`Glossary <random_state>` for details.

    check_input : bool, default=True
        If False, the input arrays X and y will not be checked.

    max_squared_sum : float, default=None
        Maximum squared sum of X over samples. Used only in SAG solver.
        If None, it will be computed, going through all the samples.
        The value should be precomputed to speed up cross validation.

    sample_weight : array-like of shape (n_samples,), default=None
        Array of weights that are assigned to individual samples.
        If not provided, then each sample is given unit weight.

    l1_ratio : float, default=None
        The Elastic-Net mixing parameter, with ``0 <= l1_ratio <= 1``. Only
        used if ``penalty=\'elasticnet\'``. Setting ``l1_ratio=0`` is equivalent
        to using ``penalty=\'l2\'``, while setting ``l1_ratio=1`` is equivalent
        to using ``penalty=\'l1\'``. For ``0 < l1_ratio <1``, the penalty is a
        combination of L1 and L2.

    n_threads : int, default=1
       Number of OpenMP threads to use.

    Returns
    -------
    coefs : ndarray of shape (n_cs, n_classes, n_features + int(fit_intercept)) or             (n_cs, n_features + int(fit_intercept))
        List of coefficients for the Logistic Regression model. If fit_intercept is set
        to True, then the last dimension will be n_features + 1, where the last item
        represents the intercept.
        For binary problems the second dimension in n_classes is dropped, i.e. the shape
        will be `(n_cs, n_features + int(fit_intercept))`.

    Cs : ndarray
        Grid of Cs used for cross-validation.

    n_iter : array of shape (n_cs,)
        Actual number of iteration for each C in Cs.

    Notes
    -----
    You might get slightly different results with the solver liblinear than
    with the others since this uses LIBLINEAR which penalizes the intercept.

    .. versionchanged:: 0.19
        The "copy" parameter was removed.
    '''
    if isinstance(Cs, numbers.Integral):
        Cs = np.logspace(-4, 4, Cs)
    solver = _check_solver(solver, penalty, dual)
    if check_input:
        X = check_array(X, accept_sparse = 'csr', dtype = np.float64, accept_large_sparse = solver not in ('liblinear', 'sag', 'saga'))
        y = check_array(y, ensure_2d = False, dtype = None)
        check_consistent_length(X, y)
# WARNING: Decompyle incomplete


def _log_reg_scoring_path(X, y, train, test, *, classes, Cs, scoring, fit_intercept, max_iter, tol, class_weight, verbose, solver, penalty, dual, intercept_scaling, random_state, max_squared_sum, sample_weight, l1_ratio, score_params):
    '''Computes scores across logistic_regression_path

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        Training data.

    y : array-like of shape (n_samples,) or (n_samples, n_targets)
        Target labels.

    train : list of indices
        The indices of the train set.

    test : list of indices
        The indices of the test set.

    classes : ndarray
        A list of class labels known to the classifier.

    Cs : int or list of floats
        Each of the values in Cs describes the inverse of
        regularization strength. If Cs is as an int, then a grid of Cs
        values are chosen in a logarithmic scale between 1e-4 and 1e4.

    scoring : str, callable or None
        The scoring method to use for cross-validation. Options:

        - str: see :ref:`scoring_string_names` for options.
        - callable: a scorer callable object (e.g., function) with signature
          ``scorer(estimator, X, y)``. See :ref:`scoring_callable` for details.
        - `None`: :ref:`accuracy <accuracy_score>` is used.

    fit_intercept : bool
        If False, then the bias term is set to zero. Else the last
        term of each coef_ gives us the intercept.

    max_iter : int
        Maximum number of iterations for the solver.

    tol : float
        Tolerance for stopping criteria.

    class_weight : dict or \'balanced\'
        Weights associated with classes in the form ``{class_label: weight}``.
        If not given, all classes are supposed to have weight one.

        The "balanced" mode uses the values of y to automatically adjust
        weights inversely proportional to class frequencies in the input data
        as ``n_samples / (n_classes * np.bincount(y))``

        Note that these weights will be multiplied with sample_weight (passed
        through the fit method) if sample_weight is specified.

    verbose : int
        For the liblinear and lbfgs solvers set verbose to any positive
        number for verbosity.

    solver : {\'lbfgs\', \'liblinear\', \'newton-cg\', \'newton-cholesky\', \'sag\', \'saga\'}
        Decides which solver to use.

    penalty : {\'l1\', \'l2\', \'elasticnet\'}
        Used to specify the norm used in the penalization. The \'newton-cg\',
        \'sag\' and \'lbfgs\' solvers support only l2 penalties. \'elasticnet\' is
        only supported by the \'saga\' solver.

    dual : bool
        Dual or primal formulation. Dual formulation is only implemented for
        l2 penalty with liblinear solver. Prefer dual=False when
        n_samples > n_features.

    intercept_scaling : float
        Useful only when the solver `liblinear` is used
        and `self.fit_intercept` is set to `True`. In this case, `x` becomes
        `[x, self.intercept_scaling]`,
        i.e. a "synthetic" feature with constant value equal to
        `intercept_scaling` is appended to the instance vector.
        The intercept becomes
        ``intercept_scaling * synthetic_feature_weight``.

        .. note::
            The synthetic feature weight is subject to L1 or L2
            regularization as all other features.
            To lessen the effect of regularization on synthetic feature weight
            (and therefore on the intercept) `intercept_scaling` has to be increased.

    random_state : int, RandomState instance
        Used when ``solver`` == \'sag\', \'saga\' or \'liblinear\' to shuffle the
        data. See :term:`Glossary <random_state>` for details.

    max_squared_sum : float
        Maximum squared sum of X over samples. Used only in SAG solver.
        If None, it will be computed, going through all the samples.
        The value should be precomputed to speed up cross validation.

    sample_weight : array-like of shape (n_samples,)
        Array of weights that are assigned to individual samples.
        If not provided, then each sample is given unit weight.

    l1_ratio : float
        The Elastic-Net mixing parameter, with ``0 <= l1_ratio <= 1``. Only
        used if ``penalty=\'elasticnet\'``. Setting ``l1_ratio=0`` is equivalent
        to using ``penalty=\'l2\'``, while setting ``l1_ratio=1`` is equivalent
        to using ``penalty=\'l1\'``. For ``0 < l1_ratio <1``, the penalty is a
        combination of L1 and L2.

    score_params : dict
        Parameters to pass to the `score` method of the underlying scorer.

    Returns
    -------
    coefs : ndarray of shape (n_cs, n_classes, n_features + int(fit_intercept)) or             (n_cs, n_features + int(fit_intercept))
        List of coefficients for the Logistic Regression model. If fit_intercept is set
        to True, then the last dimension will be n_features + 1, where the last item
        represents the intercept.
        For binary problems the second dimension in n_classes is dropped, i.e. the shape
        will be `(n_cs, n_features + int(fit_intercept))`.

    Cs : ndarray of shape (n_cs,)
        Grid of Cs used for cross-validation.

    scores : ndarray of shape (n_cs,)
        Scores obtained for each Cs.

    n_iter : ndarray of shape (n_cs,)
        Actual number of iteration for each C in Cs.
    '''
    X_train = X[train]
    X_test = X[test]
    y_train = y[train]
    y_test = y[test]
    (sw_train, sw_test) = (None, None)
# WARNING: Decompyle incomplete


class LogisticRegression(BaseEstimator, SparseCoefMixin, LinearClassifierMixin):
    pass
# WARNING: Decompyle incomplete


class LogisticRegressionCV(BaseEstimator, LinearClassifierMixin, LogisticRegression):
    pass
# WARNING: Decompyle incomplete
