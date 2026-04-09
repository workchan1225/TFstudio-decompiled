# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _function_transformer.pyc (Python 3.11)

import warnings
from functools import partial
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin, _fit_context
from sklearn.utils._dataframe import is_pandas_df, is_polars_df
from sklearn.utils._param_validation import StrOptions
from sklearn.utils._repr_html.estimator import _VisualBlock
from sklearn.utils._set_output import _get_adapter_from_container, _get_output_config
from sklearn.utils.metaestimators import available_if
from sklearn.utils.validation import _allclose_dense_sparse, _check_feature_names_in, _get_feature_names, check_array, validate_data

def _identity(X):
    '''The identity function.'''
    return X


class FunctionTransformer(BaseEstimator, TransformerMixin):
    pass
# WARNING: Decompyle incomplete
