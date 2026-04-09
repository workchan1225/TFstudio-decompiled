# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: regression.pyc (Python 3.11)

import numbers
import numpy as np
from sklearn.utils import _safe_indexing, check_random_state
from sklearn.utils._optional_dependencies import check_matplotlib_support
from sklearn.utils._plotting import _validate_style_kwargs

class PredictionErrorDisplay:
    '''Visualization of the prediction error of a regression model.

    This tool can display "residuals vs predicted" or "actual vs predicted"
    using scatter plots to qualitatively assess the behavior of a regressor,
    preferably on held-out data points.

    See the details in the docstrings of
    :func:`~sklearn.metrics.PredictionErrorDisplay.from_estimator` or
    :func:`~sklearn.metrics.PredictionErrorDisplay.from_predictions` to
    create a visualizer. All parameters are stored as attributes.

    For general information regarding `scikit-learn` visualization tools, read
    more in the :ref:`Visualization Guide <visualizations>`.
    For details regarding interpreting these plots, refer to the
    :ref:`Model Evaluation Guide <visualization_regression_evaluation>`.

    .. versionadded:: 1.2

    Parameters
    ----------
    y_true : ndarray of shape (n_samples,)
        True values.

    y_pred : ndarray of shape (n_samples,)
        Prediction values.

    Attributes
    ----------
    line_ : matplotlib Artist
        Optimal line representing `y_true == y_pred`. Therefore, it is a
        diagonal line for `kind="predictions"` and a horizontal line for
        `kind="residuals"`.

    errors_lines_ : matplotlib Artist or None
        Residual lines. If `with_errors=False`, then it is set to `None`.

    scatter_ : matplotlib Artist
        Scatter data points.

    ax_ : matplotlib Axes
        Axes with the different matplotlib axis.

    figure_ : matplotlib Figure
        Figure containing the scatter and lines.

    See Also
    --------
    PredictionErrorDisplay.from_estimator : Prediction error visualization
        given an estimator and some data.
    PredictionErrorDisplay.from_predictions : Prediction error visualization
        given the true and predicted targets.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> from sklearn.datasets import load_diabetes
    >>> from sklearn.linear_model import Ridge
    >>> from sklearn.metrics import PredictionErrorDisplay
    >>> X, y = load_diabetes(return_X_y=True)
    >>> ridge = Ridge().fit(X, y)
    >>> y_pred = ridge.predict(X)
    >>> display = PredictionErrorDisplay(y_true=y, y_pred=y_pred)
    >>> display.plot()
    <...>
    >>> plt.show()
    '''
    
    def __init__(self, *, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred

    
    def plot(self = None, ax = (None,), *, kind, scatter_kwargs, line_kwargs):
        '''Plot visualization.

        Extra keyword arguments will be passed to matplotlib\'s ``plot``.

        Parameters
        ----------
        ax : matplotlib axes, default=None
            Axes object to plot on. If `None`, a new figure and axes is
            created.

        kind : {"actual_vs_predicted", "residual_vs_predicted"},                 default="residual_vs_predicted"
            The type of plot to draw:

            - "actual_vs_predicted" draws the observed values (y-axis) vs.
              the predicted values (x-axis).
            - "residual_vs_predicted" draws the residuals, i.e. difference
              between observed and predicted values, (y-axis) vs. the predicted
              values (x-axis).

        scatter_kwargs : dict, default=None
            Dictionary with keywords passed to the `matplotlib.pyplot.scatter`
            call.

        line_kwargs : dict, default=None
            Dictionary with keyword passed to the `matplotlib.pyplot.plot`
            call to draw the optimal line.

        Returns
        -------
        display : :class:`~sklearn.metrics.PredictionErrorDisplay`

            Object that stores computed values.
        '''
        check_matplotlib_support(f'''{self.__class__.__name__}.plot''')
        expected_kind = ('actual_vs_predicted', 'residual_vs_predicted')
        if kind not in expected_kind:
            raise ValueError(f'''`kind` must be one of {', '.join(expected_kind)}. Got {kind!r} instead.''')
        plt = pyplot
        import matplotlib.pyplot
    # WARNING: Decompyle incomplete

    from_estimator = (lambda cls, estimator, X = classmethod, y = {
        'kind': 'residual_vs_predicted',
        'subsample': 1000,
        'random_state': None,
        'ax': None,
        'scatter_kwargs': None,
        'line_kwargs': None }, *, kind, subsample, random_state, ax: check_matplotlib_support(f'''{cls.__name__}.from_estimator''')y_pred = estimator.predict(X)cls.from_predictions(y_true = y, y_pred = y_pred, kind = kind, subsample = subsample, random_state = random_state, ax = ax, scatter_kwargs = scatter_kwargs, line_kwargs = line_kwargs))()
    from_predictions = (lambda cls, y_true = classmethod, y_pred = {
        'kind': 'residual_vs_predicted',
        'subsample': 1000,
        'random_state': None,
        'ax': None,
        'scatter_kwargs': None,
        'line_kwargs': None }, *, kind, subsample, random_state: check_matplotlib_support(f'''{cls.__name__}.from_predictions''')random_state = check_random_state(random_state)n_samples = len(y_true)if isinstance(subsample, numbers.Integral):
if subsample <= 0:
raise ValueError(f'''When an integer, subsample={subsample} should be positive.''')elif isinstance(subsample, numbers.Real):
if subsample <= 0 or subsample >= 1:
raise ValueError(f'''When a floating-point, subsample={subsample} should be in the (0, 1) range.''')subsample = int(n_samples * subsample)# WARNING: Decompyle incomplete
)()
