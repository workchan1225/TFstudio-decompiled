# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _lof.pyc (Python 3.11)

import warnings
from numbers import Real
import numpy as np
from sklearn.base import OutlierMixin, _fit_context
from sklearn.neighbors._base import KNeighborsMixin, NeighborsBase
from sklearn.utils import check_array
from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.utils.metaestimators import available_if
from sklearn.utils.validation import check_is_fitted
__all__ = [
    'LocalOutlierFactor']

class LocalOutlierFactor(NeighborsBase, OutlierMixin, KNeighborsMixin):
    pass
# WARNING: Decompyle incomplete
