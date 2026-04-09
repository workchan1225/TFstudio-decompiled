# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _export.pyc (Python 3.11)

__doc__ = '\nThis module defines export functions for decision trees.\n'
from collections.abc import Iterable
from io import StringIO
from numbers import Integral
import numpy as np
from sklearn.base import is_classifier
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, _criterion, _tree
from sklearn.tree._reingold_tilford import Tree, buchheim
from sklearn.utils._param_validation import HasMethods, Interval, StrOptions, validate_params
from sklearn.utils.validation import check_array, check_is_fitted

def _color_brew(n):
    '''Generate n colors with equally spaced hues.

    Parameters
    ----------
    n : int
        The number of colors required.

    Returns
    -------
    color_list : list, length n
        List of n tuples of form (R, G, B) being the components of each color.
    '''
    color_list = []
    (s, v) = (0.75, 0.9)
    c = s * v
    m = v - c
    for h in np.arange(25, 385, 360 / n).astype(int):
        h_bar = h / 60
        x = c * (1 - abs(h_bar % 2 - 1))
        rgb = [
            (c, x, 0),
            (x, c, 0),
            (0, c, x),
            (0, x, c),
            (x, 0, c),
            (c, 0, x),
            (c, x, 0)]
        (r, g, b) = rgb[int(h_bar)]
        rgb = [
            int(255 * (r + m)),
            int(255 * (g + m)),
            int(255 * (b + m))]
        color_list.append(rgb)
        return color_list


class Sentinel:
    
    def __repr__(self):
        return '"tree.dot"'


SENTINEL = Sentinel()
plot_tree = (lambda decision_tree = validate_params({
    'decision_tree': [
        DecisionTreeClassifier,
        DecisionTreeRegressor],
    'max_depth': [
        Interval(Integral, 0, None, closed = 'left'),
        None],
    'feature_names': [
        'array-like',
        None],
    'class_names': [
        'array-like',
        'boolean',
        None],
    'label': [
        StrOptions({
            'all',
            'none',
            'root'})],
    'filled': [
        'boolean'],
    'impurity': [
        'boolean'],
    'node_ids': [
        'boolean'],
    'proportion': [
        'boolean'],
    'rounded': [
        'boolean'],
    'precision': [
        Interval(Integral, 0, None, closed = 'left'),
        None],
    'ax': 'no_validation',
    'fontsize': [
        Interval(Integral, 0, None, closed = 'left'),
        None] }, prefer_skip_nested_validation = True), *, max_depth: check_is_fitted(decision_tree)exporter = _MPLTreeExporter(max_depth = max_depth, feature_names = feature_names, class_names = class_names, label = label, filled = filled, impurity = impurity, node_ids = node_ids, proportion = proportion, rounded = rounded, precision = precision, fontsize = fontsize)exporter.export(decision_tree, ax = ax))()

class _BaseTreeExporter:
    
    def __init__(self, max_depth, feature_names, class_names, label, filled, impurity, node_ids, proportion, rounded, precision, fontsize = (None, None, None, 'all', False, True, False, False, False, 3, None)):
        self.max_depth = max_depth
        self.feature_names = feature_names
        self.class_names = class_names
        self.label = label
        self.filled = filled
        self.impurity = impurity
        self.node_ids = node_ids
        self.proportion = proportion
        self.rounded = rounded
        self.precision = precision
        self.fontsize = fontsize

    
    def get_color(self, value):
        pass
    # WARNING: Decompyle incomplete

    
    def get_fill_color(self, tree, node_id):
        if 'rgb' not in self.colors:
            self.colors['rgb'] = _color_brew(tree.n_classes[0])
            if tree.n_outputs != 1:
                self.colors['bounds'] = (-np.max(tree.impurity), -np.min(tree.impurity))
            elif tree.n_classes[0] == 1 and len(np.unique(tree.value)) != 1:
                self.colors['bounds'] = (np.min(tree.value), np.max(tree.value))
    # WARNING: Decompyle incomplete

    
    def node_to_str(self, tree, node_id, criterion):
        if tree.n_outputs == 1:
            value = tree.value[node_id][(0, :)]
        else:
            value = tree.value[node_id]
        if self.label == 'root':
            if not node_id == 0:
                labels = self.label == 'all'
                characters = self.characters
                node_string = characters[-1]
                if self.node_ids:
                    if labels:
                        node_string += 'node '
                    node_string += characters[0] + str(node_id) + characters[4]
    # WARNING: Decompyle incomplete

    
    def str_escape(self, string):
        return string



class _DOTTreeExporter(_BaseTreeExporter):
    pass
# WARNING: Decompyle incomplete


class _MPLTreeExporter(_BaseTreeExporter):
    pass
# WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete
