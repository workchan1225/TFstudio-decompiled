# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _truncated_svd.pyc (Python 3.11)

'''Truncated SVD for sparse matrices, aka latent semantic analysis (LSA).'''
from numbers import Integral, Real
import numpy as np
from scipy.sparse import sparse as sp
from scipy.sparse.linalg import svds
from sklearn.base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin, _fit_context
from sklearn.utils import check_array, check_random_state
from sklearn.utils._arpack import _init_arpack_v0
from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.utils.extmath import _randomized_svd, safe_sparse_dot, svd_flip
from sklearn.utils.sparsefuncs import mean_variance_axis
from sklearn.utils.validation import check_is_fitted, validate_data
__all__ = [
    'TruncatedSVD']

class TruncatedSVD(BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin):
    pass
# WARNING: Decompyle incomplete
