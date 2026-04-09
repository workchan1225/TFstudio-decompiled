# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _gpr.pyc (Python 3.11)

'''Gaussian processes regression.'''
import warnings
from numbers import Integral, Real
from operator import itemgetter
import numpy as np
import scipy.optimize as scipy
from scipy.linalg import cho_solve, cholesky, solve_triangular
from sklearn.base import BaseEstimator, MultiOutputMixin, RegressorMixin, _fit_context, clone
from sklearn.gaussian_process.kernels import RBF, Kernel
from sklearn.gaussian_process.kernels import ConstantKernel as C
from sklearn.preprocessing._data import _handle_zeros_in_scale
from sklearn.utils import check_random_state
from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.utils.optimize import _check_optimize_result
from sklearn.utils.validation import validate_data
GPR_CHOLESKY_LOWER = True

class GaussianProcessRegressor(BaseEstimator, RegressorMixin, MultiOutputMixin):
    pass
# WARNING: Decompyle incomplete
