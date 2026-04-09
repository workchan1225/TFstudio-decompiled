# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _plotting.pyc (Python 3.11)

import warnings
from collections.abc import Mapping
import numpy as np
from sklearn.utils import check_consistent_length
from sklearn.utils._optional_dependencies import check_matplotlib_support
from sklearn.utils._response import _get_response_values_binary
from sklearn.utils.fixes import parse_version
from sklearn.utils.multiclass import type_of_target
from sklearn.utils.validation import _check_pos_label_consistency, _num_samples

class _BinaryClassifierCurveDisplayMixin:
    '''Mixin class to be used in Displays requiring a binary classifier.

    The aim of this class is to centralize some validations regarding the estimator and
    the target and gather the response of the estimator.
    '''
    
    def _validate_plot_params(self = None, *, ax, name):
        check_matplotlib_support(f'''{self.__class__.__name__}.plot''')
        plt = pyplot
        import matplotlib.pyplot
    # WARNING: Decompyle incomplete

    _validate_and_get_response_values = (lambda cls, estimator, X = classmethod, y = {
        'response_method': 'auto',
        'pos_label': None,
        'name': None }, *, response_method, pos_label, name, y_pred = None: check_matplotlib_support(f'''{cls.__name__}.from_estimator''')# WARNING: Decompyle incomplete
)()
    _validate_from_predictions_params = (lambda cls, y_true = classmethod, y_pred = {
        'sample_weight': None,
        'pos_label': None,
        'name': None }, *, sample_weight, pos_label, name: check_matplotlib_support(f'''{cls.__name__}.from_predictions''')if type_of_target(y_true) != 'binary':
raise ValueError(f'''The target y is not binary. Got {type_of_target(y_true)} type of target.''')check_consistent_length(y_true, y_pred, sample_weight)pos_label = _check_pos_label_consistency(pos_label, y_true)# WARNING: Decompyle incomplete
)()
    _validate_from_cv_results_params = (lambda cls, cv_results, X, y, *, sample_weight, required_keys = None, train_size = None, test_size = None: pass# WARNING: Decompyle incomplete
)()
    _get_legend_label = (lambda curve_legend_metric, curve_name, legend_metric_name: pass# WARNING: Decompyle incomplete
)()
    _validate_curve_kwargs = (lambda n_curves, name, legend_metric, legend_metric_name, curve_kwargs, default_curve_kwargs, default_multi_curve_kwargs = (None, None): pass# WARNING: Decompyle incomplete
)()


def _validate_score_name(score_name, scoring, negate_score):
    '''Validate the `score_name` parameter.

    If `score_name` is provided, we just return it as-is.
    If `score_name` is `None`, we use `Score` if `negate_score` is `False` and
    `Negative score` otherwise.
    If `score_name` is a string or a callable, we infer the name. We replace `_` by
    spaces and capitalize the first letter. We remove `neg_` and replace it by
    `"Negative"` if `negate_score` is `False` or just remove it otherwise.
    '''
    pass
# WARNING: Decompyle incomplete


def _interval_max_min_ratio(data):
    '''Compute the ratio between the largest and smallest inter-point distances.

    A value larger than 5 typically indicates that the parameter range would
    better be displayed with a log scale while a linear scale would be more
    suitable otherwise.
    '''
    diff = np.diff(np.sort(data))
    return diff.max() / diff.min()


def _validate_style_kwargs(default_style_kwargs, user_style_kwargs):
    """Create valid style kwargs by avoiding Matplotlib alias errors.

    Matplotlib raises an error when, for example, 'color' and 'c', or 'linestyle' and
    'ls', are specified together. To avoid this, we automatically keep only the one
    specified by the user and raise an error if the user specifies both.

    Parameters
    ----------
    default_style_kwargs : dict
        The Matplotlib style kwargs used by default in the scikit-learn display.
    user_style_kwargs : dict
        The user-defined Matplotlib style kwargs.

    Returns
    -------
    valid_style_kwargs : dict
        The validated style kwargs taking into account both default and user-defined
        Matplotlib style kwargs.
    """
    pass
# WARNING: Decompyle incomplete


def _despine(ax):
    '''Remove the top and right spines of the plot.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes of the plot to despine.
    '''
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
        for s in ('bottom', 'left'):
            ax.spines[s].set_bounds(0, 1)
            return None


def _deprecate_estimator_name(estimator_name, name, version):
    '''Deprecate `estimator_name` in favour of `name`.'''
    version = parse_version(version)
    version_remove = f'''{version.major}.{version.minor + 2}'''
    if estimator_name != 'deprecated':
        if name:
            raise ValueError(f'''Cannot provide both `estimator_name` and `name`. `estimator_name` is deprecated in {version} and will be removed in {version_remove}. Use `name` only.''')
        warnings.warn(f'''`estimator_name` is deprecated in {version} and will be removed in {version_remove}. Use `name` instead.''', FutureWarning)
        return estimator_name


def _convert_to_list_leaving_none(param):
    '''Convert parameters to a list, leaving `None` as is.'''
    pass
# WARNING: Decompyle incomplete


def _check_param_lengths(required, optional, class_name):
    '''Check required and optional parameters are of the same length.'''
    optional_provided = { }
# WARNING: Decompyle incomplete


def _deprecate_y_pred_parameter(y_score, y_pred, version):
    '''Deprecate `y_pred` in favour of of `y_score`.'''
    version = parse_version(version)
    version_remove = f'''{version.major}.{version.minor + 2}'''
# WARNING: Decompyle incomplete
