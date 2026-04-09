# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: validation.pyc (Python 3.11)

'''Functions to validate input and parameters within scikit-learn estimators.'''
import numbers
import operator
import warnings
from collections.abc import Sequence
from contextlib import suppress
from functools import reduce, wraps
from inspect import Parameter, isclass, signature
import joblib
import numpy as np
from scipy.sparse import sparse as sp
from sklearn import get_config as _get_config
from sklearn.exceptions import DataConversionWarning, NotFittedError, PositiveSpectrumWarning
from sklearn.utils._array_api import _asarray_with_order, _convert_to_numpy, _is_numpy_namespace, _max_precision_float_dtype, get_namespace, get_namespace_and_device
from sklearn.utils._dataframe import is_pandas_df, is_pandas_df_or_series
from sklearn.utils._isfinite import FiniteStatus, cy_isfinite
from sklearn.utils._tags import get_tags
from sklearn.utils.fixes import ComplexWarning, _object_dtype_isnan, _preserve_dia_indices_dtype
FLOAT_DTYPES = (np.float64, np.float32, np.float16)

def _deprecate_positional_args(func = None, *, version):
    '''Decorator for methods that issues warnings for positional arguments.

    Using the keyword-only argument syntax in pep 3102, arguments after the
    * will issue a warning when passed as a positional argument.

    Parameters
    ----------
    func : callable, default=None
        Function to check arguments on.
    version : callable, default="1.3"
        The version when positional arguments will result in error.
    '''
    pass
# WARNING: Decompyle incomplete


def _assert_all_finite(X, allow_nan, msg_dtype, estimator_name, input_name = (False, None, None, '')):
