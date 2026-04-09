# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: precision_recall_curve.pyc (Python 3.11)

from collections import Counter
from sklearn.metrics._ranking import average_precision_score, precision_recall_curve
from sklearn.utils._plotting import _BinaryClassifierCurveDisplayMixin, _deprecate_estimator_name, _deprecate_y_pred_parameter, _despine, _validate_style_kwargs

class PrecisionRecallDisplay(_BinaryClassifierCurveDisplayMixin):
    '''Precision Recall visualization.

    It is recommended to use
    :func:`~sklearn.metrics.PrecisionRecallDisplay.from_estimator` or
    :func:`~sklearn.metrics.PrecisionRecallDisplay.from_predictions` to create
    a :class:`~sklearn.metrics.PrecisionRecallDisplay`. All parameters are
    stored as attributes.

    For general information regarding `scikit-learn` visualization tools, see
    the :ref:`Visualization Guide <visualizations>`.
    For guidance on interpreting these plots, refer to the :ref:`Model
    Evaluation Guide <precision_recall_f_measure_metrics>`.

    Parameters
    ----------
    precision : ndarray
        Precision values.

    recall : ndarray
        Recall values.

    average_precision : float, default=None
        Average precision. If None, the average precision is not shown.

    name : str, default=None
        Name of estimator. If None, then the estimator name is not shown.

        .. versionchanged:: 1.8
            `estimator_name` was deprecated in favor of `name`.

    pos_label : int, float, bool or str, default=None
        The class considered the positive class when precision and recall metrics
        computed. If not `None`, this value is displayed in the x- and y-axes labels.

        .. versionadded:: 0.24

    prevalence_pos_label : float, default=None
        The prevalence of the positive label. It is used for plotting the
        chance level line. If None, the chance level line will not be plotted
        even if `plot_chance_level` is set to True when plotting.

        .. versionadded:: 1.3

    estimator_name : str, default=None
        Name of estimator. If None, the estimator name is not shown.

        .. deprecated:: 1.8
            `estimator_name` is deprecated and will be removed in 1.10. Use `name`
            instead.

    Attributes
    ----------
    line_ : matplotlib Artist
        Precision recall curve.

    chance_level_ : matplotlib Artist or None
        The chance level line. It is `None` if the chance level is not plotted.

        .. versionadded:: 1.3

    ax_ : matplotlib Axes
        Axes with precision recall curve.

    figure_ : matplotlib Figure
        Figure containing the curve.

    See Also
    --------
    precision_recall_curve : Compute precision-recall pairs for different
        probability thresholds.
    PrecisionRecallDisplay.from_estimator : Plot Precision Recall Curve given
        a binary classifier.
    PrecisionRecallDisplay.from_predictions : Plot Precision Recall Curve
        using predictions from a binary classifier.

    Notes
    -----
    The average precision (cf. :func:`~sklearn.metrics.average_precision_score`) in
    scikit-learn is computed without any interpolation. To be consistent with
    this metric, the precision-recall curve is plotted without any
    interpolation as well (step-wise style).

    You can change this style by passing the keyword argument
    `drawstyle="default"` in :meth:`plot`, :meth:`from_estimator`, or
    :meth:`from_predictions`. However, the curve will not be strictly
    consistent with the reported average precision.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> from sklearn.datasets import make_classification
    >>> from sklearn.metrics import (precision_recall_curve,
    ...                              PrecisionRecallDisplay)
    >>> from sklearn.model_selection import train_test_split
    >>> from sklearn.svm import SVC
    >>> X, y = make_classification(random_state=0)
    >>> X_train, X_test, y_train, y_test = train_test_split(X, y,
    ...                                                     random_state=0)
    >>> clf = SVC(random_state=0)
    >>> clf.fit(X_train, y_train)
    SVC(random_state=0)
    >>> predictions = clf.predict(X_test)
    >>> precision, recall, _ = precision_recall_curve(y_test, predictions)
    >>> disp = PrecisionRecallDisplay(precision=precision, recall=recall)
    >>> disp.plot()
    <...>
    >>> plt.show()
    '''
    
    def __init__(self, precision = None, recall = {
        'average_precision': None,
        'name': None,
        'pos_label': None,
        'prevalence_pos_label': None,
        'estimator_name': 'deprecated' }, *, average_precision, name, pos_label, prevalence_pos_label, estimator_name):
        self.name = _deprecate_estimator_name(estimator_name, name, '1.8')
        self.precision = precision
        self.recall = recall
        self.average_precision = average_precision
        self.pos_label = pos_label
        self.prevalence_pos_label = prevalence_pos_label

    
    def plot(self = None, ax = (None,), *, name, plot_chance_level, chance_level_kw, despine, **kwargs):
        '''Plot visualization.

        Extra keyword arguments will be passed to matplotlib\'s `plot`.

        Parameters
        ----------
        ax : Matplotlib Axes, default=None
            Axes object to plot on. If `None`, a new figure and axes is
            created.

        name : str, default=None
            Name of precision recall curve for labeling. If `None`, use
            `name` if not `None`, otherwise no labeling is shown.

        plot_chance_level : bool, default=False
            Whether to plot the chance level. The chance level is the prevalence
            of the positive label computed from the data passed during
            :meth:`from_estimator` or :meth:`from_predictions` call.

            .. versionadded:: 1.3

        chance_level_kw : dict, default=None
            Keyword arguments to be passed to matplotlib\'s `plot` for rendering
            the chance level line.

            .. versionadded:: 1.3

        despine : bool, default=False
            Whether to remove the top and right spines from the plot.

            .. versionadded:: 1.6

        **kwargs : dict
            Keyword arguments to be passed to matplotlib\'s `plot`.

        Returns
        -------
        display : :class:`~sklearn.metrics.PrecisionRecallDisplay`
            Object that stores computed values.

        Notes
        -----
        The average precision (cf. :func:`~sklearn.metrics.average_precision_score`)
        in scikit-learn is computed without any interpolation. To be consistent
        with this metric, the precision-recall curve is plotted without any
        interpolation as well (step-wise style).

        You can change this style by passing the keyword argument
        `drawstyle="default"`. However, the curve will not be strictly
        consistent with the reported average precision.
        '''
        (self.ax_, self.figure_, name) = self._validate_plot_params(ax = ax, name = name)
        default_line_kwargs = {
            'drawstyle': 'steps-post' }
    # WARNING: Decompyle incomplete

    from_estimator = (lambda cls, estimator, X = classmethod, y = {
        'sample_weight': None,
        'drop_intermediate': False,
        'response_method': 'auto',
        'pos_label': None,
        'name': None,
        'ax': None,
        'plot_chance_level': False,
        'chance_level_kw': None,
        'despine': False }, *, sample_weight, drop_intermediate, response_method, pos_label: (y_score, pos_label, name) = cls._validate_and_get_response_values(estimator, X, y, response_method = response_method, pos_label = pos_label, name = name)# WARNING: Decompyle incomplete
)()
    from_predictions = (lambda cls = classmethod, y_true = (None,), y_score = {
        'sample_weight': None,
        'drop_intermediate': False,
        'pos_label': None,
        'name': None,
        'ax': None,
        'plot_chance_level': False,
        'chance_level_kw': None,
        'despine': False,
        'y_pred': 'deprecated' }, *, sample_weight, drop_intermediate, pos_label: y_score = _deprecate_y_pred_parameter(y_score, y_pred, '1.8')(pos_label, name) = cls._validate_from_predictions_params(y_true, y_score, sample_weight = sample_weight, pos_label = pos_label, name = name)(precision, recall, _) = precision_recall_curve(y_true, y_score, pos_label = pos_label, sample_weight = sample_weight, drop_intermediate = drop_intermediate)average_precision = average_precision_score(y_true, y_score, pos_label = pos_label, sample_weight = sample_weight)class_count = Counter(y_true)prevalence_pos_label = class_count[pos_label] / sum(class_count.values())viz = cls(precision = precision, recall = recall, average_precision = average_precision, name = name, pos_label = pos_label, prevalence_pos_label = prevalence_pos_label)# WARNING: Decompyle incomplete
)()
