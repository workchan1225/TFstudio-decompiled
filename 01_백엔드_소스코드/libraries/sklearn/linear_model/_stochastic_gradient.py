# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _stochastic_gradient.pyc (Python 3.11)

'''Classification, regression and One-Class SVM using Stochastic Gradient
Descent (SGD).
'''
import warnings
from abc import ABCMeta, abstractmethod
from numbers import Integral, Real
import numpy as np
from sklearn._loss._loss import CyHalfBinomialLoss, CyHalfSquaredError, CyHuberLoss
from sklearn.base import BaseEstimator, OutlierMixin, RegressorMixin, _fit_context, clone, is_classifier
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model._base import LinearClassifierMixin, SparseCoefMixin, make_dataset
from sklearn.linear_model._sgd_fast import EpsilonInsensitive, Hinge, ModifiedHuber, SquaredEpsilonInsensitive, SquaredHinge, _plain_sgd32, _plain_sgd64
from sklearn.model_selection import ShuffleSplit, StratifiedShuffleSplit
from sklearn.utils import check_random_state, compute_class_weight
from sklearn.utils._param_validation import Hidden, Interval, StrOptions
from sklearn.utils.extmath import safe_sparse_dot
from sklearn.utils.metaestimators import available_if
from sklearn.utils.multiclass import _check_partial_fit_first_call
from sklearn.utils.parallel import Parallel, delayed
from sklearn.utils.validation import _check_sample_weight, check_is_fitted, validate_data
LEARNING_RATE_TYPES = {
    'constant': 1,
    'optimal': 2,
    'invscaling': 3,
    'adaptive': 4,
    'pa1': 5,
    'pa2': 6 }
PENALTY_TYPES = {
    'none': 0,
    'l2': 2,
    'l1': 1,
    'elasticnet': 3 }
DEFAULT_EPSILON = 0.1
MAX_INT = np.iinfo(np.int32).max

class _ValidationScoreCallback:
    '''Callback for early stopping based on validation score'''
    
    def __init__(self, estimator, X_val, y_val, sample_weight_val, classes = (None,)):
        self.estimator = clone(estimator)
        self.estimator.t_ = 1
    # WARNING: Decompyle incomplete

    
    def __call__(self, coef, intercept):
        est = self.estimator
        est.coef_ = coef.reshape(1, -1)
        est.intercept_ = np.atleast_1d(intercept)
        return est.score(self.X_val, self.y_val, self.sample_weight_val)



def BaseSGD():
    '''BaseSGD'''
    __doc__ = 'Base class for SGD classification and regression.'
    _parameter_constraints: dict = {
        'fit_intercept': [
            'boolean'],
        'max_iter': [
            Interval(Integral, 1, None, closed = 'left')],
        'tol': [
            Interval(Real, 0, None, closed = 'left'),
            None],
        'shuffle': [
            'boolean'],
        'verbose': [
            'verbose'],
        'random_state': [
            'random_state'],
        'warm_start': [
            'boolean'],
        'average': [
            Interval(Integral, 0, None, closed = 'neither'),
            'boolean'],
        'eta0': [
            Interval(Real, 0, None, closed = 'neither')] }
    
    def __init__(self = None, loss = {
        'penalty': 'l2',
        'alpha': 0.0001,
        'l1_ratio': 0.15,
        'fit_intercept': True,
        'max_iter': 1000,
        'tol': 0.001,
        'shuffle': True,
        'verbose': 0,
        'epsilon': 0.1,
        'random_state': None,
        'learning_rate': 'optimal',
        'eta0': 0.01,
        'power_t': 0.5,
        'early_stopping': False,
        'validation_fraction': 0.1,
        'n_iter_no_change': 5,
        'warm_start': False,
        'average': False }, *, penalty, alpha, l1_ratio, fit_intercept, max_iter, tol, shuffle, verbose, epsilon, random_state, learning_rate, eta0, power_t, early_stopping, validation_fraction, n_iter_no_change, warm_start, average):
        self.loss = loss
        self.penalty = penalty
        self.learning_rate = learning_rate
        self.epsilon = epsilon
        self.alpha = alpha
        self.l1_ratio = l1_ratio
        self.fit_intercept = fit_intercept
        self.shuffle = shuffle
        self.random_state = random_state
        self.verbose = verbose
        self.eta0 = eta0
        self.power_t = power_t
        self.early_stopping = early_stopping
        self.validation_fraction = validation_fraction
        self.n_iter_no_change = n_iter_no_change
        self.warm_start = warm_start
        self.average = average
        self.max_iter = max_iter
        self.tol = tol

    fit = (lambda self, X, y: pass)()
    
    def _more_validate_params(self, for_partial_fit = (False,)):
        '''Validate input params.'''
        if self.early_stopping and for_partial_fit:
            raise ValueError('early_stopping should be False with partial_fit')
        if self.learning_rate == 'optimal' and self.alpha == 0:
            raise ValueError("alpha must be > 0 since learning_rate is 'optimal'. alpha is used to compute the optimal learning rate.")
        if self.learning_rate in ('pa1', 'pa2'):
            if is_classifier(self):
                if self.loss != 'hinge':
                    msg = f'''Learning rate \'{self.learning_rate}\' only works with loss \'hinge\'.'''
                    raise ValueError(msg)
            elif self.loss != 'epsilon_insensitive':
                msg = f'''Learning rate \'{self.learning_rate}\' only works with loss \'epsilon_insensitive\'.'''
                raise ValueError(msg)
    # WARNING: Decompyle incomplete

    
    def _get_l1_ratio(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_loss_function(self, loss):
        '''Get concrete ``LossFunction`` object for str ``loss``.'''
        loss_ = self.loss_functions[loss]
        args = loss_[1:]
        loss_class = loss_[0]
        if loss in ('huber', 'epsilon_insensitive', 'squared_epsilon_insensitive'):
            args = (self.epsilon,)
    # WARNING: Decompyle incomplete

    
    def _get_learning_rate_type(self, learning_rate):
        return LEARNING_RATE_TYPES[learning_rate]

    
    def _get_penalty_type(self, penalty):
        penalty = str(penalty).lower()
        return PENALTY_TYPES[penalty]

    
    def _allocate_parameter_mem(self, n_classes, n_features, input_dtype, coef_init, intercept_init, one_class = (None, None, 0)):
        '''Allocate mem for parameters; initialize if provided.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _make_validation_split(self, y, sample_mask):
        '''Split the dataset between training set and validation set.

        Parameters
        ----------
        y : ndarray of shape (n_samples, )
            Target values.

        sample_mask : ndarray of shape (n_samples, )
            A boolean array indicating whether each sample should be included
            for validation set.

        Returns
        -------
        validation_mask : ndarray of shape (n_samples, )
            Equal to True on the validation set, False on the training set.
        '''
        n_samples = y.shape[0]
        validation_mask = np.zeros(n_samples, dtype = np.bool_)
        if not self.early_stopping:
            return validation_mask
        if None(self):
            splitter_type = StratifiedShuffleSplit
        else:
            splitter_type = ShuffleSplit
        cv = splitter_type(test_size = self.validation_fraction, random_state = self.random_state)
        (idx_train, idx_val) = next(cv.split(np.zeros(shape = (y.shape[0], 1)), y))
        if not np.any(sample_mask[idx_val]):
            raise ValueError('The sample weights for validation set are all zero, consider using a different random state.')
        if idx_train.shape[0] == 0 or idx_val.shape[0] == 0:
            raise ValueError('Splitting %d samples into a train set and a validation set with validation_fraction=%r led to an empty set (%d and %d samples). Please either change validation_fraction, increase number of samples, or disable early_stopping.' % (n_samples, self.validation_fraction, idx_train.shape[0], idx_val.shape[0]))
        validation_mask[idx_val] = True
        return validation_mask

    
    def _make_validation_score_cb(self, validation_mask, X, y, sample_weight, classes = (None,)):
        if not self.early_stopping:
            return None
        return None(self, X[validation_mask], y[validation_mask], sample_weight[validation_mask], classes = classes)


BaseSGD = <NODE:27>(BaseSGD, 'BaseSGD', SparseCoefMixin, BaseEstimator, metaclass = ABCMeta)

def _prepare_fit_binary(est, y, i, input_dtype, label_encode = (True,)):
    '''Initialization for fit_binary.

    Returns y, coef, intercept, average_coef, average_intercept.
    '''
    y_i = np.ones(y.shape, dtype = input_dtype, order = 'C')
    if label_encode:
        y_i[y != est.classes_[i]] = 0
    else:
        y_i[y != est.classes_[i]] = -1
    average_intercept = 0
    average_coef = None
    if len(est.classes_) == 2:
        if not est.average:
            coef = est.coef_.ravel()
            intercept = est.intercept_[0]
        else:
            coef = est._standard_coef.ravel()
            intercept = est._standard_intercept[0]
            average_coef = est._average_coef.ravel()
            average_intercept = est._average_intercept[0]
    elif not est.average:
        coef = est.coef_[i]
        intercept = est.intercept_[i]
    else:
        coef = est._standard_coef[i]
        intercept = est._standard_intercept[i]
        average_coef = est._average_coef[i]
        average_intercept = est._average_intercept[i]
    return (y_i, coef, intercept, average_coef, average_intercept)


def fit_binary(est, i, X, y, alpha, learning_rate, max_iter, pos_weight, neg_weight, sample_weight, validation_mask, random_state = (None, None)):
    '''Fit a single binary classifier.

    The i\'th class is considered the "positive" class.

    Parameters
    ----------
    est : Estimator object
        The estimator to fit

    i : int
        Index of the positive class

    X : numpy array or sparse matrix of shape [n_samples,n_features]
        Training data

    y : numpy array of shape [n_samples, ]
        Target values

    alpha : float
        The regularization parameter

    learning_rate : str
        The learning rate. Accepted values are \'constant\', \'optimal\',
        \'invscaling\', \'pa1\' and \'pa2\'.

    max_iter : int
        The maximum number of iterations (epochs)

    pos_weight : float
        The weight of the positive class

    neg_weight : float
        The weight of the negative class

    sample_weight : numpy array of shape [n_samples, ]
        The weight of each sample

    validation_mask : numpy array of shape [n_samples, ], default=None
        Precomputed validation mask in case _fit_binary is called in the
        context of a one-vs-rest reduction.

    random_state : int, RandomState instance, default=None
        If int, random_state is the seed used by the random number generator;
        If RandomState instance, random_state is the random number generator;
        If None, the random number generator is the RandomState instance used
        by `np.random`.
    '''
    label_encode = isinstance(est._loss_function_, CyHalfBinomialLoss)
    (y_i, coef, intercept, average_coef, average_intercept) = _prepare_fit_binary(est, y, i, input_dtype = X.dtype, label_encode = label_encode)
    if not  == y_i.shape[0], y.shape[0] or y_i.shape[0], y.shape[0] == sample_weight.shape[0]:
        pass
    
# WARNING: Decompyle incomplete


def _get_plain_sgd_function(input_dtype):
    return _plain_sgd32 if input_dtype == np.float32 else _plain_sgd64


def BaseSGDClassifier():
    '''BaseSGDClassifier'''
    pass
# WARNING: Decompyle incomplete

BaseSGDClassifier = <NODE:27>(BaseSGDClassifier, 'BaseSGDClassifier', LinearClassifierMixin, BaseSGD, metaclass = ABCMeta)

class SGDClassifier(BaseSGDClassifier):
    pass
# WARNING: Decompyle incomplete


class BaseSGDRegressor(BaseSGD, RegressorMixin):
    pass
# WARNING: Decompyle incomplete


class SGDRegressor(BaseSGDRegressor):
    pass
# WARNING: Decompyle incomplete


class SGDOneClassSVM(BaseSGD, OutlierMixin):
    pass
# WARNING: Decompyle incomplete
