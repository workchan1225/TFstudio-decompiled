# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _kernel_pca.pyc (Python 3.11)

'''Kernel Principal Components Analysis.'''
from numbers import Integral, Real
import numpy as np
from scipy import linalg
from scipy.linalg import eigh
from scipy.sparse.linalg import eigsh
from sklearn.base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin, _fit_context
from sklearn.exceptions import NotFittedError
from sklearn.metrics.pairwise import pairwise_kernels
from sklearn.preprocessing import KernelCenterer
from sklearn.utils._arpack import _init_arpack_v0
from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.utils.extmath import _randomized_eigsh, svd_flip
from sklearn.utils.validation import _check_psd_eigenvalues, check_is_fitted, validate_data

class KernelPCA(BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin):
    pass
# WARNING: Decompyle incomplete
