# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _birch.pyc (Python 3.11)

import warnings
from math import sqrt
from numbers import Integral, Real
import numpy as np
from scipy import sparse
from sklearn._config import config_context
from sklearn.base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, ClusterMixin, TransformerMixin, _fit_context
from sklearn.cluster import AgglomerativeClustering
from sklearn.exceptions import ConvergenceWarning
from sklearn.metrics import pairwise_distances_argmin
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.utils._param_validation import Interval
from sklearn.utils.extmath import row_norms
from sklearn.utils.validation import check_is_fitted, validate_data

def _iterate_sparse_X(X):
    '''This little hack returns a densified row when iterating over a sparse
    matrix, instead of constructing a sparse matrix for every row that is
    expensive.
    '''
    pass
# WARNING: Decompyle incomplete


def _split_node(node, threshold, branching_factor):
    '''The node has to be split if there is no place for a new subcluster
    in the node.
    1. Two empty nodes and two empty subclusters are initialized.
    2. The pair of distant subclusters are found.
    3. The properties of the empty subclusters and nodes are updated
       according to the nearest distance between the subclusters to the
       pair of distant subclusters.
    4. The two nodes are set as children to the two subclusters.
    '''
    new_subcluster1 = _CFSubcluster()
    new_subcluster2 = _CFSubcluster()
    new_node1 = _CFNode(threshold = threshold, branching_factor = branching_factor, is_leaf = node.is_leaf, n_features = node.n_features, dtype = node.init_centroids_.dtype)
    new_node2 = _CFNode(threshold = threshold, branching_factor = branching_factor, is_leaf = node.is_leaf, n_features = node.n_features, dtype = node.init_centroids_.dtype)
    new_subcluster1.child_ = new_node1
    new_subcluster2.child_ = new_node2
# WARNING: Decompyle incomplete


class _CFNode:
    '''Each node in a CFTree is called a CFNode.

    The CFNode can have a maximum of branching_factor
    number of CFSubclusters.

    Parameters
    ----------
    threshold : float
        Threshold needed for a new subcluster to enter a CFSubcluster.

    branching_factor : int
        Maximum number of CF subclusters in each node.

    is_leaf : bool
        We need to know if the CFNode is a leaf or not, in order to
        retrieve the final subclusters.

    n_features : int
        The number of features.

    Attributes
    ----------
    subclusters_ : list
        List of subclusters for a particular CFNode.

    prev_leaf_ : _CFNode
        Useful only if is_leaf is True.

    next_leaf_ : _CFNode
        next_leaf. Useful only if is_leaf is True.
        the final subclusters.

    init_centroids_ : ndarray of shape (branching_factor + 1, n_features)
        Manipulate ``init_centroids_`` throughout rather than centroids_ since
        the centroids are just a view of the ``init_centroids_`` .

    init_sq_norm_ : ndarray of shape (branching_factor + 1,)
        manipulate init_sq_norm_ throughout. similar to ``init_centroids_``.

    centroids_ : ndarray of shape (branching_factor + 1, n_features)
        View of ``init_centroids_``.

    squared_norm_ : ndarray of shape (branching_factor + 1,)
        View of ``init_sq_norm_``.

    '''
    
    def __init__(self, *, threshold, branching_factor, is_leaf, n_features, dtype):
        self.threshold = threshold
        self.branching_factor = branching_factor
        self.is_leaf = is_leaf
        self.n_features = n_features
        self.subclusters_ = []
        self.init_centroids_ = np.zeros((branching_factor + 1, n_features), dtype = dtype)
        self.init_sq_norm_ = np.zeros(branching_factor + 1, dtype)
        self.squared_norm_ = []
        self.prev_leaf_ = None
        self.next_leaf_ = None

    
    def append_subcluster(self, subcluster):
        n_samples = len(self.subclusters_)
        self.subclusters_.append(subcluster)
        self.init_centroids_[n_samples] = subcluster.centroid_
        self.init_sq_norm_[n_samples] = subcluster.sq_norm_
        self.centroids_ = self.init_centroids_[(:n_samples + 1, :)]
        self.squared_norm_ = self.init_sq_norm_[:n_samples + 1]

    
    def update_split_subclusters(self, subcluster, new_subcluster1, new_subcluster2):
        '''Remove a subcluster from a node and update it with the
        split subclusters.
        '''
        ind = self.subclusters_.index(subcluster)
        self.subclusters_[ind] = new_subcluster1
        self.init_centroids_[ind] = new_subcluster1.centroid_
        self.init_sq_norm_[ind] = new_subcluster1.sq_norm_
        self.append_subcluster(new_subcluster2)

    
    def insert_cf_subcluster(self, subcluster):
        '''Insert a new subcluster into the node.'''
        if not self.subclusters_:
            self.append_subcluster(subcluster)
            return False
        threshold = None.threshold
        branching_factor = self.branching_factor
        dist_matrix = np.dot(self.centroids_, subcluster.centroid_)
        dist_matrix *= -2
        dist_matrix += self.squared_norm_
        closest_index = np.argmin(dist_matrix)
        closest_subcluster = self.subclusters_[closest_index]
    # WARNING: Decompyle incomplete



class _CFSubcluster:
    '''Each subcluster in a CFNode is called a CFSubcluster.

    A CFSubcluster can have a CFNode has its child.

    Parameters
    ----------
    linear_sum : ndarray of shape (n_features,), default=None
        Sample. This is kept optional to allow initialization of empty
        subclusters.

    Attributes
    ----------
    n_samples_ : int
        Number of samples that belong to each subcluster.

    linear_sum_ : ndarray
        Linear sum of all the samples in a subcluster. Prevents holding
        all sample data in memory.

    squared_sum_ : float
        Sum of the squared l2 norms of all samples belonging to a subcluster.

    centroid_ : ndarray of shape (branching_factor + 1, n_features)
        Centroid of the subcluster. Prevent recomputing of centroids when
        ``CFNode.centroids_`` is called.

    child_ : _CFNode
        Child Node of the subcluster. Once a given _CFNode is set as the child
        of the _CFNode, it is set to ``self.child_``.

    sq_norm_ : ndarray of shape (branching_factor + 1,)
        Squared norm of the subcluster. Used to prevent recomputing when
        pairwise minimum distances are computed.
    '''
    
    def __init__(self = None, *, linear_sum):
        pass
    # WARNING: Decompyle incomplete

    
    def update(self, subcluster):
        self.linear_sum_ / self.n_samples_ = self, self.squared_sum_ += subcluster.squared_sum_, .squared_sum_
        self.sq_norm_ = np.dot(self.centroid_, self.centroid_)

    
    def merge_subcluster(self, nominee_cluster, threshold):
        '''Check if a cluster is worthy enough to be merged. If
        yes then merge.
        '''
        new_ss = self.squared_sum_ + nominee_cluster.squared_sum_
        new_ls = self.linear_sum_ + nominee_cluster.linear_sum_
        new_n = self.n_samples_ + nominee_cluster.n_samples_
        new_centroid = (1 / new_n) * new_ls
        new_sq_norm = np.dot(new_centroid, new_centroid)
        sq_radius = new_ss / new_n - new_sq_norm
        if sq_radius <= threshold ** 2:
            (self.n_samples_, self.linear_sum_, self.squared_sum_, self.centroid_, self.sq_norm_) = (new_n, new_ls, new_ss, new_centroid, new_sq_norm)
            return True

    radius = (lambda self: sq_radius = self.squared_sum_ / self.n_samples_ - self.sq_norm_sqrt(max(0, sq_radius)))()


class Birch(BaseEstimator, TransformerMixin, ClusterMixin, ClassNamePrefixFeaturesOutMixin):
    pass
# WARNING: Decompyle incomplete
