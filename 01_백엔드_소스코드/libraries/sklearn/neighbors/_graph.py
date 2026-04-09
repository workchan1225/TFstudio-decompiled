# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _graph.pyc (Python 3.11)

__doc__ = 'Nearest Neighbors graph functions'
import itertools
from sklearn.base import ClassNamePrefixFeaturesOutMixin, TransformerMixin, _fit_context
from sklearn.neighbors._base import VALID_METRICS, KNeighborsMixin, NeighborsBase, RadiusNeighborsMixin
from sklearn.neighbors._unsupervised import NearestNeighbors
from sklearn.utils._param_validation import Integral, Interval, Real, StrOptions, validate_params
from sklearn.utils.validation import check_is_fitted

def _check_params(X, metric, p, metric_params):
    '''Check the validity of the input parameters'''
    params = zip([
        'metric',
        'p',
        'metric_params'], [
        metric,
        p,
        metric_params])
    est_params = X.get_params()
    for param_name, func_param in params:
        if func_param != est_params[param_name]:
            raise ValueError(f'''Got {func_param!s} for {param_name!s}, while the estimator has {est_params[param_name]!s} for the same parameter.''')
        return None


def _query_include_self(X, include_self, mode):
    '''Return the query based on include_self param'''
    if include_self == 'auto':
        include_self = mode == 'connectivity'
    if not include_self:
        X = None
    return X

# WARNING: Decompyle incomplete
