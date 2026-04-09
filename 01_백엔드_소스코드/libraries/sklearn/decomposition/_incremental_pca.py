# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _incremental_pca.pyc (Python 3.11)

'''Incremental Principal Components Analysis.'''
from numbers import Integral
import numpy as np
from scipy import linalg, sparse
from sklearn.base import _fit_context
from sklearn.decomposition._base import _BasePCA
from sklearn.utils import gen_batches, metadata_routing
from sklearn.utils._param_validation import Interval
from sklearn.utils.extmath import _incremental_mean_and_var, svd_flip
from sklearn.utils.validation import validate_data

class IncrementalPCA(_BasePCA):
    pass
# WARNING: Decompyle incomplete
