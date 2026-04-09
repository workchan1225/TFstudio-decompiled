# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _isomap.pyc (Python 3.11)

'''Isomap for manifold learning'''
import warnings
from numbers import Integral, Real
import numpy as np
from scipy.sparse import issparse
from scipy.sparse.csgraph import connected_components, shortest_path
from sklearn.base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin, _fit_context
from sklearn.decomposition import KernelPCA
from sklearn.metrics.pairwise import _VALID_METRICS
from sklearn.neighbors import NearestNeighbors, kneighbors_graph, radius_neighbors_graph
from sklearn.preprocessing import KernelCenterer
from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.utils.graph import _fix_connected_components
from sklearn.utils.validation import check_is_fitted

class Isomap(BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin):
    pass
# WARNING: Decompyle incomplete
