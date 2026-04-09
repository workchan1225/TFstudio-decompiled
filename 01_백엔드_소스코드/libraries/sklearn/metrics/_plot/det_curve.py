# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: det_curve.pyc (Python 3.11)

import numpy as np
import scipy as sp
from sklearn.metrics._ranking import det_curve
from sklearn.utils._plotting import _BinaryClassifierCurveDisplayMixin, _deprecate_y_pred_parameter

class DetCurveDisplay(_BinaryClassifierCurveDisplayMixin):
    '''Detection Error Tradeoff (DET) curve visualization.

    It is recommended to use :func:`~sklearn.metrics.DetCurveDisplay.from_estimator`
    or :func:`~sklearn.metrics.DetCurveDisplay.from_predictions` to create a
    visualizer. All parameters are stored as attributes.

    For general information regarding `scikit-learn` visualization tools, see
    the :ref:`Visualization Guide <visualizations>`.
    For guidance on interpreting these plots, refer to the
    :ref:`Model Evaluation Guide <det_curve>`.

    .. versionadded:: 0.24

    Parameters
    ----------
    fpr : ndarray
        False positive rate.

    fnr : ndarray
        False negative rate.

    estimator_name : str, default=None
        Name of estimator. If None, the estimator name is not shown.

    pos_label : int, float, bool or str, default=None
        The label of the positive class. If not `None`, this value is displayed in
        the x- and y-axes labels.

    Attributes
    ----------
    line_ : matplotlib Artist
        DET Curve.

    ax_ : matplotlib Axes
        Axes with DET Curve.

    figure_ : matplotlib Figure
        Figure containing the curve.

    See Also
    --------
    det_curve : Compute error rates for different probability thresholds.
    DetCurveDisplay.from_estimator : Plot DET curve given an estimator and
        some data.
    DetCurveDisplay.from_predictions : Plot DET curve given the true and
        predicted labels.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> from sklearn.datasets import make_classification
    >>> from sklearn.metrics import det_curve, DetCurveDisplay
    >>> from sklearn.model_selection import train_test_split
    >>> from sklearn.svm import SVC
    >>> X, y = make_classification(n_samples=1000, random_state=0)
    >>> X_train, X_test, y_train, y_test = train_test_split(
    ...     X, y, test_size=0.4, random_state=0)
    >>> clf = SVC(random_state=0).fit(X_train, y_train)
    >>> y_score = clf.decision_function(X_test)
    >>> fpr, fnr, _ = det_curve(y_test, y_score)
    >>> display = DetCurveDisplay(
    ...     fpr=fpr, fnr=fnr, estimator_name="SVC"
    ... )
    >>> display.plot()
    <...>
    >>> plt.show()
    '''
    
    def __init__(self = None, *, fpr, fnr, estimator_name, pos_label):
        self.fpr = fpr
        self.fnr = fnr
        self.estimator_name = estimator_name
        self.pos_label = pos_label

    from_estimator = (lambda cls, estimator, X = classmethod, y = {
        'sample_weight': None,
        'drop_intermediate': True,
        'response_method': 'auto',
        'pos_label': None,
        'name': None,
        'ax': None }, *, sample_weight, drop_intermediate, response_method, pos_label: (y_score, pos_label, name) = cls._validate_and_get_response_values(estimator, X, y, response_method = response_method, pos_label = pos_label, name = name)# WARNING: Decompyle incomplete
)()
    from_predictions = (lambda cls = classmethod, y_true = (None,), y_score = {
        'sample_weight': None,
        'drop_intermediate': True,
        'pos_label': None,
        'name': None,
        'ax': None,
        'y_pred': 'deprecated' }, *, sample_weight, drop_intermediate, pos_label: y_score = _deprecate_y_pred_parameter(y_score, y_pred, '1.8')(pos_label_validated, name) = cls._validate_from_predictions_params(y_true, y_score, sample_weight = sample_weight, pos_label = pos_label, name = name)(fpr, fnr, _) = det_curve(y_true, y_score, pos_label = pos_label, sample_weight = sample_weight, drop_intermediate = drop_intermediate)viz = cls(fpr = fpr, fnr = fnr, estimator_name = name, pos_label = pos_label_validated)# WARNING: Decompyle incomplete
)()
    
    def plot(self = None, ax = (None,), *, name, **kwargs):
        '''Plot visualization.

        Parameters
        ----------
        ax : matplotlib axes, default=None
            Axes object to plot on. If `None`, a new figure and axes is
            created.

        name : str, default=None
            Name of DET curve for labeling. If `None`, use `estimator_name` if
            it is not `None`, otherwise no labeling is shown.

        **kwargs : dict
            Additional keywords arguments passed to matplotlib `plot` function.

        Returns
        -------
        display : :class:`~sklearn.metrics.DetCurveDisplay`
            Object that stores computed values.
        '''
        (self.ax_, self.figure_, name) = self._validate_plot_params(ax = ax, name = name)
    # WARNING: Decompyle incomplete
