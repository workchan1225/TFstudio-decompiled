# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _pprint.pyc (Python 3.11)

'''This module contains the _EstimatorPrettyPrinter class used in
BaseEstimator.__repr__ for pretty-printing estimators'''
import inspect
import pprint
from sklearn._config import get_config
from sklearn.base import BaseEstimator
from sklearn.utils._missing import is_scalar_nan

class KeyValTuple(tuple):
    pass
# WARNING: Decompyle incomplete


class KeyValTupleParam(KeyValTuple):
    '''Dummy class for correctly rendering key-value tuples from parameters.'''
    pass


def _changed_params(estimator):
    '''Return dict (param_name: value) of parameters that were given to
    estimator with non-default values.'''
    pass
# WARNING: Decompyle incomplete


class _EstimatorPrettyPrinter(pprint.PrettyPrinter):
    pass
# WARNING: Decompyle incomplete


def _safe_repr(object, context, maxlevels, level, changed_only = (False,)):
