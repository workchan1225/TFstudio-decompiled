# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _nca.pyc (Python 3.11)

'''
Neighborhood Component Analysis
'''
import sys
import time
from numbers import Integral, Real
from warnings import warn
import numpy as np
from scipy.optimize import minimize
from sklearn.base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin, _fit_context
from sklearn.decomposition import PCA
from sklearn.exceptions import ConvergenceWarning
from sklearn.metrics import pairwise_distances
from sklearn.preprocessing import LabelEncoder
from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.utils.extmath import softmax
from sklearn.utils.fixes import _get_additional_lbfgs_options_dict
from sklearn.utils.multiclass import check_classification_targets
from sklearn.utils.random import check_random_state
from sklearn.utils.validation import check_array, check_is_fitted, validate_data

class NeighborhoodComponentsAnalysis(BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin):
    pass
# WARNING: Decompyle incomplete
