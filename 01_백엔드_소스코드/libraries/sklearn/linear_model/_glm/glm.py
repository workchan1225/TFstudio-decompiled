# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: glm.pyc (Python 3.11)

'''
Generalized Linear Models with Exponential Dispersion Family
'''
from numbers import Integral, Real
import numpy as np
import scipy.optimize as scipy
from sklearn._loss.loss import HalfGammaLoss, HalfPoissonLoss, HalfSquaredError, HalfTweedieLoss, HalfTweedieLossIdentity
from sklearn.base import BaseEstimator, RegressorMixin, _fit_context
from sklearn.linear_model._glm._newton_solver import NewtonCholeskySolver, NewtonSolver
from sklearn.linear_model._linear_loss import LinearModelLoss
from sklearn.utils import check_array
from sklearn.utils._openmp_helpers import _openmp_effective_n_threads
from sklearn.utils._param_validation import Hidden, Interval, StrOptions
from sklearn.utils.fixes import _get_additional_lbfgs_options_dict
from sklearn.utils.optimize import _check_optimize_result
from sklearn.utils.validation import _check_sample_weight, check_is_fitted, validate_data

class _GeneralizedLinearRegressor(BaseEstimator, RegressorMixin):
    pass
# WARNING: Decompyle incomplete


class PoissonRegressor(_GeneralizedLinearRegressor):
    pass
# WARNING: Decompyle incomplete


class GammaRegressor(_GeneralizedLinearRegressor):
    pass
# WARNING: Decompyle incomplete


class TweedieRegressor(_GeneralizedLinearRegressor):
    pass
# WARNING: Decompyle incomplete
