# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: roc_curve.pyc (Python 3.11)

import numpy as np
from sklearn.metrics._ranking import auc, roc_curve
from sklearn.utils import _safe_indexing
from sklearn.utils._plotting import _BinaryClassifierCurveDisplayMixin, _check_param_lengths, _convert_to_list_leaving_none, _deprecate_estimator_name, _deprecate_y_pred_parameter, _despine, _validate_style_kwargs
from sklearn.utils._response import _get_response_values_binary

class RocCurveDisplay(_BinaryClassifierCurveDisplayMixin):
    pass
# WARNING: Decompyle incomplete
