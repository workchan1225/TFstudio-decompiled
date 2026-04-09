# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _sparse_pca.pyc (Python 3.11)

'''Matrix factorization with Sparse PCA.'''
from numbers import Integral, Real
import numpy as np
from sklearn.base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin, _fit_context
from sklearn.decomposition._dict_learning import MiniBatchDictionaryLearning, dict_learning
from sklearn.linear_model import ridge_regression
from sklearn.utils import check_random_state
from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.utils.extmath import svd_flip
from sklearn.utils.validation import check_array, check_is_fitted, validate_data

class _BaseSparsePCA(BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin):
    pass
# WARNING: Decompyle incomplete


class SparsePCA(_BaseSparsePCA):
    pass
# WARNING: Decompyle incomplete


class MiniBatchSparsePCA(_BaseSparsePCA):
    pass
# WARNING: Decompyle incomplete
