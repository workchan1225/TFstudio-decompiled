# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _target_encoder.pyc (Python 3.11)

from numbers import Integral, Real
import numpy as np
from sklearn.base import OneToOneFeatureMixin, _fit_context
from sklearn.preprocessing._encoders import _BaseEncoder
from sklearn.preprocessing._target_encoder_fast import _fit_encoding_fast, _fit_encoding_fast_auto_smooth
from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.utils.multiclass import type_of_target
from sklearn.utils.validation import _check_feature_names_in, _check_y, check_consistent_length, check_is_fitted

class TargetEncoder(_BaseEncoder, OneToOneFeatureMixin):
    pass
# WARNING: Decompyle incomplete
