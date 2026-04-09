# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _elliptic_envelope.pyc (Python 3.11)

from numbers import Real
import numpy as np
from sklearn.base import OutlierMixin, _fit_context
from sklearn.covariance._robust_covariance import MinCovDet
from sklearn.metrics import accuracy_score
from sklearn.utils._param_validation import Interval
from sklearn.utils.validation import check_is_fitted

class EllipticEnvelope(MinCovDet, OutlierMixin):
    pass
# WARNING: Decompyle incomplete
