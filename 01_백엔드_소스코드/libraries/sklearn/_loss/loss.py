# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: loss.pyc (Python 3.11)

'''
This module contains loss classes suitable for fitting.

It is not part of the public API.
Specific losses are used for regression, binary classification or multiclass
classification.
'''
import numbers
import numpy as np
from scipy.special import xlogy
from sklearn._loss._loss import CyAbsoluteError, CyExponentialLoss, CyHalfBinomialLoss, CyHalfGammaLoss, CyHalfMultinomialLoss, CyHalfPoissonLoss, CyHalfSquaredError, CyHalfTweedieLoss, CyHalfTweedieLossIdentity, CyHuberLoss, CyPinballLoss
from sklearn._loss.link import HalfLogitLink, IdentityLink, Interval, LogitLink, LogLink, MultinomialLogit
from sklearn.utils import check_scalar
from sklearn.utils.stats import _weighted_percentile

class BaseLoss:
    """Base class for a loss function of 1-dimensional targets.

    Conventions:

        - y_true.shape = sample_weight.shape = (n_samples,)
        - y_pred.shape = raw_prediction.shape = (n_samples,)
        - If is_multiclass is true (multiclass classification), then
          y_pred.shape = raw_prediction.shape = (n_samples, n_classes)
          Note that this corresponds to the return value of decision_function.

    y_true, y_pred, sample_weight and raw_prediction must either be all float64
    or all float32.
    gradient and hessian must be either both float64 or both float32.

    Note that y_pred = link.inverse(raw_prediction).

    Specific loss classes can inherit specific link classes to satisfy
    BaseLink's abstractmethods.

    Parameters
    ----------
    sample_weight : {None, ndarray}
        If sample_weight is None, the hessian might be constant.
    n_classes : {None, int}
        The number of classes for classification, else None.

    Attributes
    ----------
    closs: CyLossFunction
    link : BaseLink
    interval_y_true : Interval
        Valid interval for y_true
    interval_y_pred : Interval
        Valid Interval for y_pred
    differentiable : bool
        Indicates whether or not loss function is differentiable in
        raw_prediction everywhere.
    need_update_leaves_values : bool
        Indicates whether decision trees in gradient boosting need to uptade
        leave values after having been fit to the (negative) gradients.
    approx_hessian : bool
        Indicates whether the hessian is approximated or exact. If,
        approximated, it should be larger or equal to the exact one.
    constant_hessian : bool
        Indicates whether the hessian is one for this loss.
    is_multiclass : bool
        Indicates whether n_classes > 2 is allowed.
    """
    differentiable = True
    need_update_leaves_values = False
    is_multiclass = False
    
    def __init__(self, closs, link, n_classes = (None,)):
        self.closs = closs
        self.link = link
        self.approx_hessian = False
        self.constant_hessian = False
        self.n_classes = n_classes
        self.interval_y_true = Interval(-(np.inf), np.inf, False, False)
        self.interval_y_pred = self.link.interval_y_pred

    
    def in_y_true_range(self, y):
        '''Return True if y is in the valid range of y_true.

        Parameters
        ----------
        y : ndarray
        '''
        return self.interval_y_true.includes(y)

    
    def in_y_pred_range(self, y):
        '''Return True if y is in the valid range of y_pred.

        Parameters
        ----------
        y : ndarray
        '''
        return self.interval_y_pred.includes(y)

    
    def loss(self, y_true, raw_prediction, sample_weight, loss_out, n_threads = (None, None, 1)):
        '''Compute the pointwise loss value for each input.

        Parameters
        ----------
        y_true : C-contiguous array of shape (n_samples,)
            Observed, true target values.
        raw_prediction : C-contiguous array of shape (n_samples,) or array of             shape (n_samples, n_classes)
            Raw prediction values (in link space).
        sample_weight : None or C-contiguous array of shape (n_samples,)
            Sample weights.
        loss_out : None or C-contiguous array of shape (n_samples,)
            A location into which the result is stored. If None, a new array
            might be created.
        n_threads : int, default=1
            Might use openmp thread parallelism.

        Returns
        -------
        loss : array of shape (n_samples,)
            Element-wise loss function.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def loss_gradient(self, y_true, raw_prediction, sample_weight, loss_out, gradient_out, n_threads = (None, None, None, 1)):
        '''Compute loss and gradient w.r.t. raw_prediction for each input.

        Parameters
        ----------
        y_true : C-contiguous array of shape (n_samples,)
            Observed, true target values.
        raw_prediction : C-contiguous array of shape (n_samples,) or array of             shape (n_samples, n_classes)
            Raw prediction values (in link space).
        sample_weight : None or C-contiguous array of shape (n_samples,)
            Sample weights.
        loss_out : None or C-contiguous array of shape (n_samples,)
            A location into which the loss is stored. If None, a new array
            might be created.
        gradient_out : None or C-contiguous array of shape (n_samples,) or array             of shape (n_samples, n_classes)
            A location into which the gradient is stored. If None, a new array
            might be created.
        n_threads : int, default=1
            Might use openmp thread parallelism.

        Returns
        -------
        loss : array of shape (n_samples,)
            Element-wise loss function.

        gradient : array of shape (n_samples,) or (n_samples, n_classes)
            Element-wise gradients.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def gradient(self, y_true, raw_prediction, sample_weight, gradient_out, n_threads = (None, None, 1)):
        '''Compute gradient of loss w.r.t raw_prediction for each input.

        Parameters
        ----------
        y_true : C-contiguous array of shape (n_samples,)
            Observed, true target values.
        raw_prediction : C-contiguous array of shape (n_samples,) or array of             shape (n_samples, n_classes)
            Raw prediction values (in link space).
        sample_weight : None or C-contiguous array of shape (n_samples,)
            Sample weights.
        gradient_out : None or C-contiguous array of shape (n_samples,) or array             of shape (n_samples, n_classes)
            A location into which the result is stored. If None, a new array
            might be created.
        n_threads : int, default=1
            Might use openmp thread parallelism.

        Returns
        -------
        gradient : array of shape (n_samples,) or (n_samples, n_classes)
            Element-wise gradients.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def gradient_hessian(self, y_true, raw_prediction, sample_weight, gradient_out, hessian_out, n_threads = (None, None, None, 1)):
        '''Compute gradient and hessian of loss w.r.t raw_prediction.

        Parameters
        ----------
        y_true : C-contiguous array of shape (n_samples,)
            Observed, true target values.
        raw_prediction : C-contiguous array of shape (n_samples,) or array of             shape (n_samples, n_classes)
            Raw prediction values (in link space).
        sample_weight : None or C-contiguous array of shape (n_samples,)
            Sample weights.
        gradient_out : None or C-contiguous array of shape (n_samples,) or array             of shape (n_samples, n_classes)
            A location into which the gradient is stored. If None, a new array
            might be created.
        hessian_out : None or C-contiguous array of shape (n_samples,) or array             of shape (n_samples, n_classes)
            A location into which the hessian is stored. If None, a new array
            might be created.
        n_threads : int, default=1
            Might use openmp thread parallelism.

        Returns
        -------
        gradient : arrays of shape (n_samples,) or (n_samples, n_classes)
            Element-wise gradients.

        hessian : arrays of shape (n_samples,) or (n_samples, n_classes)
            Element-wise hessians.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self, y_true, raw_prediction, sample_weight, n_threads = (None, 1)):
        '''Compute the weighted average loss.

        Parameters
        ----------
        y_true : C-contiguous array of shape (n_samples,)
            Observed, true target values.
        raw_prediction : C-contiguous array of shape (n_samples,) or array of             shape (n_samples, n_classes)
            Raw prediction values (in link space).
        sample_weight : None or C-contiguous array of shape (n_samples,)
            Sample weights.
        n_threads : int, default=1
            Might use openmp thread parallelism.

        Returns
        -------
        loss : float
            Mean or averaged loss function.
        '''
        return np.average(self.loss(y_true = y_true, raw_prediction = raw_prediction, sample_weight = None, loss_out = None, n_threads = n_threads), weights = sample_weight)

    
    def fit_intercept_only(self, y_true, sample_weight = (None,)):
        '''Compute raw_prediction of an intercept-only model.

        This can be used as initial estimates of predictions, i.e. before the
        first iteration in fit.

        Parameters
        ----------
        y_true : array-like of shape (n_samples,)
            Observed, true target values.
        sample_weight : None or array of shape (n_samples,)
            Sample weights.

        Returns
        -------
        raw_prediction : numpy scalar or array of shape (n_classes,)
            Raw predictions of an intercept-only model.
        '''
        y_pred = np.average(y_true, weights = sample_weight, axis = 0)
        eps = 10 * np.finfo(y_pred.dtype).eps
        if self.interval_y_pred.low == -(np.inf):
            a_min = None
        elif self.interval_y_pred.low_inclusive:
            a_min = self.interval_y_pred.low
        else:
            a_min = self.interval_y_pred.low + eps
        if self.interval_y_pred.high == np.inf:
            a_max = None
        elif self.interval_y_pred.high_inclusive:
            a_max = self.interval_y_pred.high
        else:
            a_max = self.interval_y_pred.high - eps
    # WARNING: Decompyle incomplete

    
    def constant_to_optimal_zero(self, y_true, sample_weight = (None,)):
        '''Calculate term dropped in loss.

        With this term added, the loss of perfect predictions is zero.

        Parameters
        ----------
        y_true : array-like of shape (n_samples,)
            Observed, true target values.

        sample_weight : None or array of shape (n_samples,), default=None
            Sample weights.

        Returns
        -------
        constant : ndarray of shape (n_samples,)
            Constant value to be added to raw predictions so that the loss
            of perfect predictions becomes zero.
        '''
        return np.zeros_like(y_true)

    
    def init_gradient_and_hessian(self, n_samples, dtype, order = (np.float64, 'F')):
        """Initialize arrays for gradients and hessians.

        Unless hessians are constant, arrays are initialized with undefined values.

        Parameters
        ----------
        n_samples : int
            The number of samples, usually passed to `fit()`.
        dtype : {np.float64, np.float32}, default=np.float64
            The dtype of the arrays gradient and hessian.
        order : {'C', 'F'}, default='F'
            Order of the arrays gradient and hessian. The default 'F' makes the arrays
            contiguous along samples.

        Returns
        -------
        gradient : C-contiguous array of shape (n_samples,) or array of shape             (n_samples, n_classes)
            Empty array (allocated but not initialized) to be used as argument
            gradient_out.
        hessian : C-contiguous array of shape (n_samples,), array of shape
            (n_samples, n_classes) or shape (1,)
            Empty (allocated but not initialized) array to be used as argument
            hessian_out.
            If constant_hessian is True (e.g. `HalfSquaredError`), the array is
            initialized to ``1``.
        """
        if dtype not in (np.float32, np.float64):
            raise ValueError(f'''Valid options for \'dtype\' are np.float32 and np.float64. Got dtype={dtype} instead.''')
        if self.is_multiclass:
            shape = (n_samples, self.n_classes)
        else:
            shape = (n_samples,)
        gradient = np.empty(shape = shape, dtype = dtype, order = order)
        if self.constant_hessian:
            hessian = np.ones(shape = (1,), dtype = dtype)
        else:
            hessian = np.empty(shape = shape, dtype = dtype, order = order)
        return (gradient, hessian)



class HalfSquaredError(BaseLoss):
    pass
# WARNING: Decompyle incomplete


class AbsoluteError(BaseLoss):
    pass
# WARNING: Decompyle incomplete


class PinballLoss(BaseLoss):
    pass
# WARNING: Decompyle incomplete


class HuberLoss(BaseLoss):
    pass
# WARNING: Decompyle incomplete


class HalfPoissonLoss(BaseLoss):
    pass
# WARNING: Decompyle incomplete


class HalfGammaLoss(BaseLoss):
    pass
# WARNING: Decompyle incomplete


class HalfTweedieLoss(BaseLoss):
    pass
# WARNING: Decompyle incomplete


class HalfTweedieLossIdentity(BaseLoss):
    pass
# WARNING: Decompyle incomplete


class HalfBinomialLoss(BaseLoss):
    pass
# WARNING: Decompyle incomplete


class HalfMultinomialLoss(BaseLoss):
    pass
# WARNING: Decompyle incomplete


class ExponentialLoss(BaseLoss):
    pass
# WARNING: Decompyle incomplete

_LOSSES = {
    'squared_error': HalfSquaredError,
    'absolute_error': AbsoluteError,
    'pinball_loss': PinballLoss,
    'huber_loss': HuberLoss,
    'poisson_loss': HalfPoissonLoss,
    'gamma_loss': HalfGammaLoss,
    'tweedie_loss': HalfTweedieLoss,
    'binomial_loss': HalfBinomialLoss,
    'multinomial_loss': HalfMultinomialLoss,
    'exponential_loss': ExponentialLoss }
