# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _nearest_centroid.pyc (Python 3.11)

'''
Nearest Centroid Classification
'''
import warnings
from numbers import Real
import numpy as np
from scipy import sparse as sp
from sklearn.base import BaseEstimator, ClassifierMixin, _fit_context
from sklearn.discriminant_analysis import DiscriminantAnalysisPredictionMixin
from sklearn.metrics.pairwise import pairwise_distances, pairwise_distances_argmin
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import get_tags
from sklearn.utils._available_if import available_if
from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.utils.multiclass import check_classification_targets
from sklearn.utils.sparsefuncs import csc_median_axis_0
from sklearn.utils.validation import check_is_fitted, validate_data

class NearestCentroid(BaseEstimator, ClassifierMixin, DiscriminantAnalysisPredictionMixin):
    pass
# WARNING: Decompyle incomplete
