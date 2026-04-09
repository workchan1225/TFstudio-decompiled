# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _quantile.pyc (Python 3.11)

import warnings
from numbers import Real
import numpy as np
from scipy import sparse
from scipy.optimize import linprog
from sklearn.base import BaseEstimator, RegressorMixin, _fit_context
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model._base import LinearModel
from sklearn.utils import _safe_indexing
from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.utils.fixes import parse_version, sp_version
from sklearn.utils.validation import _check_sample_weight, validate_data

class QuantileRegressor(BaseEstimator, RegressorMixin, LinearModel):
    pass
# WARNING: Decompyle incomplete
