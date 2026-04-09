# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _classes.pyc (Python 3.11)

'''
This module gathers tree-based methods, including decision, regression and
randomized trees. Single and multi-output problems are both handled.
'''
import copy
import numbers
from abc import ABCMeta, abstractmethod
from math import ceil
from numbers import Integral, Real
import numpy as np
from scipy.sparse import issparse
from sklearn.base import BaseEstimator, ClassifierMixin, MultiOutputMixin, RegressorMixin, _fit_context, clone, is_classifier
from sklearn.tree import _criterion, _splitter, _tree
from sklearn.tree._criterion import Criterion
from sklearn.tree._splitter import Splitter
from sklearn.tree._tree import BestFirstTreeBuilder, DepthFirstTreeBuilder, Tree, _build_pruned_tree_ccp, ccp_pruning_path
from sklearn.tree._utils import _any_isnan_axis0
from sklearn.utils import Bunch, check_random_state, compute_sample_weight, metadata_routing
from sklearn.utils._param_validation import Hidden, Interval, RealNotInt, StrOptions
from sklearn.utils.multiclass import check_classification_targets
from sklearn.utils.validation import _assert_all_finite_element_wise, _check_n_features, _check_sample_weight, assert_all_finite, check_is_fitted, validate_data
__all__ = [
    'DecisionTreeClassifier',
    'DecisionTreeRegressor',
    'ExtraTreeClassifier',
    'ExtraTreeRegressor']
DTYPE = _tree.DTYPE
DOUBLE = _tree.DOUBLE
CRITERIA_CLF = {
    'gini': _criterion.Gini,
    'log_loss': _criterion.Entropy,
    'entropy': _criterion.Entropy }
CRITERIA_REG = {
    'squared_error': _criterion.MSE,
    'friedman_mse': _criterion.FriedmanMSE,
    'absolute_error': _criterion.MAE,
    'poisson': _criterion.Poisson }
DENSE_SPLITTERS = {
    'best': _splitter.BestSplitter,
    'random': _splitter.RandomSplitter }
SPARSE_SPLITTERS = {
    'best': _splitter.BestSparseSplitter,
    'random': _splitter.RandomSparseSplitter }

def BaseDecisionTree():
    '''BaseDecisionTree'''
    pass
# WARNING: Decompyle incomplete

BaseDecisionTree = <NODE:27>(BaseDecisionTree, 'BaseDecisionTree', MultiOutputMixin, BaseEstimator, metaclass = ABCMeta)

class DecisionTreeClassifier(BaseDecisionTree, ClassifierMixin):
    pass
# WARNING: Decompyle incomplete


class DecisionTreeRegressor(BaseDecisionTree, RegressorMixin):
    pass
# WARNING: Decompyle incomplete


class ExtraTreeClassifier(DecisionTreeClassifier):
    pass
# WARNING: Decompyle incomplete


class ExtraTreeRegressor(DecisionTreeRegressor):
    pass
# WARNING: Decompyle incomplete
