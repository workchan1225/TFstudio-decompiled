# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _bisect_k_means.pyc (Python 3.11)

'''Bisecting K-means clustering.'''
import warnings
import numpy as np
from scipy.sparse import sparse as sp
from sklearn.base import _fit_context
from sklearn.cluster._k_means_common import _inertia_dense, _inertia_sparse
from sklearn.cluster._kmeans import _BaseKMeans, _kmeans_single_elkan, _kmeans_single_lloyd, _labels_inertia_threadpool_limit
from sklearn.utils._openmp_helpers import _openmp_effective_n_threads
from sklearn.utils._param_validation import Integral, Interval, StrOptions
from sklearn.utils.extmath import row_norms
from sklearn.utils.validation import _check_sample_weight, check_is_fitted, check_random_state, validate_data

class _BisectingTree:
    '''Tree structure representing the hierarchical clusters of BisectingKMeans.'''
    
    def __init__(self, center, indices, score):
        '''Create a new cluster node in the tree.

        The node holds the center of this cluster and the indices of the data points
        that belong to it.
        '''
        self.center = center
        self.indices = indices
        self.score = score
        self.left = None
        self.right = None

    
    def split(self, labels, centers, scores):
        '''Split the cluster node into two subclusters.'''
        self.left = _BisectingTree(indices = self.indices[labels == 0], center = centers[0], score = scores[0])
        self.right = _BisectingTree(indices = self.indices[labels == 1], center = centers[1], score = scores[1])
        self.indices = None

    
    def get_cluster_to_bisect(self):
        """Return the cluster node to bisect next.

        It's based on the score of the cluster, which can be either the number of
        data points assigned to that cluster or the inertia of that cluster
        (see `bisecting_strategy` for details).
        """
        max_score = None
    # WARNING: Decompyle incomplete

    
    def iter_leaves(self):
        '''Iterate over all the cluster leaves in the tree.'''
        pass
    # WARNING: Decompyle incomplete



class BisectingKMeans(_BaseKMeans):
    pass
# WARNING: Decompyle incomplete
