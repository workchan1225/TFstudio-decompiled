# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _polynomial.pyc (Python 3.11)

'''
This file contains preprocessing tools based on polynomials.
'''
import collections
from itertools import chain, combinations
from itertools import combinations_with_replacement as combinations_w_r
from numbers import Integral
import numpy as np
from scipy import sparse
from scipy.interpolate import BSpline
from scipy.special import comb
from sklearn.base import BaseEstimator, TransformerMixin, _fit_context
from sklearn.preprocessing._csr_polynomial_expansion import _calc_expanded_nnz, _calc_total_nnz, _csr_polynomial_expansion
from sklearn.utils import check_array
from sklearn.utils._array_api import _is_numpy_namespace, get_namespace_and_device, supported_float_dtypes
from sklearn.utils._mask import _get_mask
from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.utils.stats import _weighted_percentile
from sklearn.utils.validation import FLOAT_DTYPES, _check_feature_names_in, _check_sample_weight, check_is_fitted, validate_data
__all__ = [
    'PolynomialFeatures',
    'SplineTransformer']

def _create_expansion(X, interaction_only, deg, n_features, cumulative_size = (0,)):
    '''Helper function for creating and appending sparse expansion matrices'''
    total_nnz = _calc_total_nnz(X.indptr, interaction_only, deg)
    expanded_col = _calc_expanded_nnz(n_features, interaction_only, deg)
    if expanded_col == 0:
        return None
    max_indices = None - 1
    max_indptr = total_nnz
    max_int32 = np.iinfo(np.int32).max
    needs_int64 = max(max_indices, max_indptr) > max_int32
    index_dtype = np.int64 if needs_int64 else np.int32
    expanded_data = np.empty(shape = total_nnz, dtype = X.data.dtype)
    expanded_indices = np.empty(shape = total_nnz, dtype = index_dtype)
    expanded_indptr = np.empty(shape = X.indptr.shape[0], dtype = index_dtype)
    _csr_polynomial_expansion(X.data, X.indices, X.indptr, X.shape[1], expanded_data, expanded_indices, expanded_indptr, interaction_only, deg)
    return sparse.csr_matrix((expanded_data, expanded_indices, expanded_indptr), shape = (X.indptr.shape[0] - 1, expanded_col), dtype = X.dtype)


class PolynomialFeatures(BaseEstimator, TransformerMixin):
    pass
# WARNING: Decompyle incomplete


class SplineTransformer(BaseEstimator, TransformerMixin):
    pass
# WARNING: Decompyle incomplete
