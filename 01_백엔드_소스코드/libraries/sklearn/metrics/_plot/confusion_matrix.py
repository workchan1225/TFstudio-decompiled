# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: confusion_matrix.pyc (Python 3.11)

from itertools import product
import numpy as np
from sklearn.base import is_classifier
from sklearn.metrics import confusion_matrix
from sklearn.utils._optional_dependencies import check_matplotlib_support
from sklearn.utils._plotting import _validate_style_kwargs
from sklearn.utils.multiclass import unique_labels

class ConfusionMatrixDisplay:
    '''Confusion Matrix visualization.

    It is recommended to use
    :func:`~sklearn.metrics.ConfusionMatrixDisplay.from_estimator` or
    :func:`~sklearn.metrics.ConfusionMatrixDisplay.from_predictions` to
    create a :class:`ConfusionMatrixDisplay`. All parameters are stored as
    attributes.

    For general information regarding `scikit-learn` visualization tools, see
    the :ref:`Visualization Guide <visualizations>`.
    For guidance on interpreting these plots, refer to the
    :ref:`Model Evaluation Guide <confusion_matrix>`.

    Parameters
    ----------
    confusion_matrix : ndarray of shape (n_classes, n_classes)
        Confusion matrix.

    display_labels : ndarray of shape (n_classes,), default=None
        Display labels for plot. If None, display labels are set from 0 to
        `n_classes - 1`.

    Attributes
    ----------
    im_ : matplotlib AxesImage
        Image representing the confusion matrix.

    text_ : ndarray of shape (n_classes, n_classes), dtype=matplotlib Text,             or None
        Array of matplotlib axes. `None` if `include_values` is false.

    ax_ : matplotlib Axes
        Axes with confusion matrix.

    figure_ : matplotlib Figure
        Figure containing the confusion matrix.

    See Also
    --------
    confusion_matrix : Compute Confusion Matrix to evaluate the accuracy of a
        classification.
    ConfusionMatrixDisplay.from_estimator : Plot the confusion matrix
        given an estimator, the data, and the label.
    ConfusionMatrixDisplay.from_predictions : Plot the confusion matrix
        given the true and predicted labels.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> from sklearn.datasets import make_classification
    >>> from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
    >>> from sklearn.model_selection import train_test_split
    >>> from sklearn.svm import SVC
    >>> X, y = make_classification(random_state=0)
    >>> X_train, X_test, y_train, y_test = train_test_split(X, y,
    ...                                                     random_state=0)
    >>> clf = SVC(random_state=0)
    >>> clf.fit(X_train, y_train)
    SVC(random_state=0)
    >>> predictions = clf.predict(X_test)
    >>> cm = confusion_matrix(y_test, predictions, labels=clf.classes_)
    >>> disp = ConfusionMatrixDisplay(confusion_matrix=cm,
    ...                               display_labels=clf.classes_)
    >>> disp.plot()
    <...>
    >>> plt.show()
    '''
    
    def __init__(self = None, confusion_matrix = {
        'display_labels': None }, *, display_labels):
        self.confusion_matrix = confusion_matrix
        self.display_labels = display_labels

    
    def plot(self = None, *, include_values, cmap, xticks_rotation, values_format, ax, colorbar, im_kw, text_kw):
        """Plot visualization.

        Parameters
        ----------
        include_values : bool, default=True
            Includes values in confusion matrix.

        cmap : str or matplotlib Colormap, default='viridis'
            Colormap recognized by matplotlib.

        xticks_rotation : {'vertical', 'horizontal'} or float,                          default='horizontal'
            Rotation of xtick labels.

        values_format : str, default=None
            Format specification for values in confusion matrix. If `None`,
            the format specification is 'd' or '.2g' whichever is shorter.

        ax : matplotlib axes, default=None
            Axes object to plot on. If `None`, a new figure and axes is
            created.

        colorbar : bool, default=True
            Whether or not to add a colorbar to the plot.

        im_kw : dict, default=None
            Dict with keywords passed to `matplotlib.pyplot.imshow` call.

        text_kw : dict, default=None
            Dict with keywords passed to `matplotlib.pyplot.text` call.

            .. versionadded:: 1.2

        Returns
        -------
        display : :class:`~sklearn.metrics.ConfusionMatrixDisplay`
            Returns a :class:`~sklearn.metrics.ConfusionMatrixDisplay` instance
            that contains all the information to plot the confusion matrix.
        """
        check_matplotlib_support('ConfusionMatrixDisplay.plot')
        plt = pyplot
        import matplotlib.pyplot
    # WARNING: Decompyle incomplete

    from_estimator = (lambda cls, estimator, X = classmethod, y = {
        'labels': None,
        'sample_weight': None,
        'normalize': None,
        'display_labels': None,
        'include_values': True,
        'xticks_rotation': 'horizontal',
        'values_format': None,
        'cmap': 'viridis',
        'ax': None,
        'colorbar': True,
        'im_kw': None,
        'text_kw': None }, *, labels, sample_weight, normalize, display_labels: method_name = f'''{cls.__name__}.from_estimator'''check_matplotlib_support(method_name)if not is_classifier(estimator):
raise ValueError(f'''{method_name} only supports classifiers''')y_pred = estimator.predict(X)cls.from_predictions(y, y_pred, sample_weight = sample_weight, labels = labels, normalize = normalize, display_labels = display_labels, include_values = include_values, cmap = cmap, ax = ax, xticks_rotation = xticks_rotation, values_format = values_format, colorbar = colorbar, im_kw = im_kw, text_kw = text_kw))()
    from_predictions = (lambda cls, y_true = classmethod, y_pred = {
        'labels': None,
        'sample_weight': None,
        'normalize': None,
        'display_labels': None,
        'include_values': True,
        'xticks_rotation': 'horizontal',
        'values_format': None,
        'cmap': 'viridis',
        'ax': None,
        'colorbar': True,
        'im_kw': None,
        'text_kw': None }, *, labels, sample_weight, normalize: check_matplotlib_support(f'''{cls.__name__}.from_predictions''')# WARNING: Decompyle incomplete
)()
