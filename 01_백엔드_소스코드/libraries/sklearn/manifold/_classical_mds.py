# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _classical_mds.pyc (Python 3.11)

'''
Classical multi-dimensional scaling (classical MDS).
'''
from numbers import Integral
import numpy as np
from scipy import linalg
from sklearn.base import BaseEstimator, _fit_context
from sklearn.metrics import pairwise_distances
from sklearn.utils import check_symmetric
from sklearn.utils._param_validation import Interval
from sklearn.utils.extmath import svd_flip
from sklearn.utils.validation import validate_data

class ClassicalMDS(BaseEstimator):
    pass
# WARNING: Decompyle incomplete
