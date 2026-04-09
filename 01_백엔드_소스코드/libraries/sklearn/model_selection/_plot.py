# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _plot.pyc (Python 3.11)

import numpy as np
from sklearn.model_selection._validation import learning_curve, validation_curve
from sklearn.utils._optional_dependencies import check_matplotlib_support
from sklearn.utils._plotting import _interval_max_min_ratio, _validate_score_name

class _BaseCurveDisplay:
    
    def _plot_curve(self = None, x_data = {
        'ax': None,
        'negate_score': False,
        'score_name': None,
        'score_type': 'test',
        'std_display_style': 'fill_between',
        'line_kw': None,
        'fill_between_kw': None,
        'errorbar_kw': None }, *, ax, negate_score, score_name, score_type, std_display_style, line_kw, fill_between_kw, errorbar_kw):
        check_matplotlib_support(f'''{self.__class__.__name__}.plot''')
        plt = pyplot
        import matplotlib.pyplot
    # WARNING: Decompyle incomplete



class LearningCurveDisplay(_BaseCurveDisplay):
    '''Learning Curve visualization.

    It is recommended to use
    :meth:`~sklearn.model_selection.LearningCurveDisplay.from_estimator` to
    create a :class:`~sklearn.model_selection.LearningCurveDisplay` instance.
    All parameters are stored as attributes.

    Read more in the :ref:`User Guide <visualizations>` for general information
    about the visualization API and
    :ref:`detailed documentation <learning_curve>` regarding the learning
    curve visualization.

    .. versionadded:: 1.2

    Parameters
    ----------
    train_sizes : ndarray of shape (n_unique_ticks,)
        Numbers of training examples that has been used to generate the
        learning curve.

    train_scores : ndarray of shape (n_ticks, n_cv_folds)
        Scores on training sets.

    test_scores : ndarray of shape (n_ticks, n_cv_folds)
        Scores on test set.

    score_name : str, default=None
        The name of the score used in `learning_curve`. It will override the name
        inferred from the `scoring` parameter. If `score` is `None`, we use `"Score"` if
        `negate_score` is `False` and `"Negative score"` otherwise. If `scoring` is a
        string or a callable, we infer the name. We replace `_` by spaces and capitalize
        the first letter. We remove `neg_` and replace it by `"Negative"` if
        `negate_score` is `False` or just remove it otherwise.

    Attributes
    ----------
    ax_ : matplotlib Axes
        Axes with the learning curve.

    figure_ : matplotlib Figure
        Figure containing the learning curve.

    errorbar_ : list of matplotlib Artist or None
        When the `std_display_style` is `"errorbar"`, this is a list of
        `matplotlib.container.ErrorbarContainer` objects. If another style is
        used, `errorbar_` is `None`.

    lines_ : list of matplotlib Artist or None
        When the `std_display_style` is `"fill_between"`, this is a list of
        `matplotlib.lines.Line2D` objects corresponding to the mean train and
        test scores. If another style is used, `line_` is `None`.

    fill_between_ : list of matplotlib Artist or None
        When the `std_display_style` is `"fill_between"`, this is a list of
        `matplotlib.collections.PolyCollection` objects. If another style is
        used, `fill_between_` is `None`.

    See Also
    --------
    sklearn.model_selection.learning_curve : Compute the learning curve.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> from sklearn.datasets import load_iris
    >>> from sklearn.model_selection import LearningCurveDisplay, learning_curve
    >>> from sklearn.tree import DecisionTreeClassifier
    >>> X, y = load_iris(return_X_y=True)
    >>> tree = DecisionTreeClassifier(random_state=0)
    >>> train_sizes, train_scores, test_scores = learning_curve(
    ...     tree, X, y)
    >>> display = LearningCurveDisplay(train_sizes=train_sizes,
    ...     train_scores=train_scores, test_scores=test_scores, score_name="Score")
    >>> display.plot()
    <...>
    >>> plt.show()
    '''
    
    def __init__(self = None, *, train_sizes, train_scores, test_scores, score_name):
        self.train_sizes = train_sizes
        self.train_scores = train_scores
        self.test_scores = test_scores
        self.score_name = score_name

    
    def plot(self = None, ax = (None,), *, negate_score, score_name, score_type, std_display_style, line_kw, fill_between_kw, errorbar_kw):
        '''Plot visualization.

        Parameters
        ----------
        ax : matplotlib Axes, default=None
            Axes object to plot on. If `None`, a new figure and axes is
            created.

        negate_score : bool, default=False
            Whether or not to negate the scores obtained through
            :func:`~sklearn.model_selection.learning_curve`. This is
            particularly useful when using the error denoted by `neg_*` in
            `scikit-learn`.

        score_name : str, default=None
            The name of the score used to decorate the y-axis of the plot. It will
            override the name inferred from the `scoring` parameter. If `score` is
            `None`, we use `"Score"` if `negate_score` is `False` and `"Negative score"`
            otherwise. If `scoring` is a string or a callable, we infer the name. We
            replace `_` by spaces and capitalize the first letter. We remove `neg_` and
            replace it by `"Negative"` if `negate_score` is
            `False` or just remove it otherwise.

        score_type : {"test", "train", "both"}, default="both"
            The type of score to plot. Can be one of `"test"`, `"train"`, or
            `"both"`.

        std_display_style : {"errorbar", "fill_between"} or None, default="fill_between"
            The style used to display the score standard deviation around the
            mean score. If None, no standard deviation representation is
            displayed.

        line_kw : dict, default=None
            Additional keyword arguments passed to the `plt.plot` used to draw
            the mean score.

        fill_between_kw : dict, default=None
            Additional keyword arguments passed to the `plt.fill_between` used
            to draw the score standard deviation.

        errorbar_kw : dict, default=None
            Additional keyword arguments passed to the `plt.errorbar` used to
            draw mean score and standard deviation score.

        Returns
        -------
        display : :class:`~sklearn.model_selection.LearningCurveDisplay`
            Object that stores computed values.
        '''
        self._plot_curve(self.train_sizes, ax = ax, negate_score = negate_score, score_name = score_name, score_type = score_type, std_display_style = std_display_style, line_kw = line_kw, fill_between_kw = fill_between_kw, errorbar_kw = errorbar_kw)
        self.ax_.set_xlabel('Number of samples in the training set')
        return self

    from_estimator = (lambda cls, estimator, X = classmethod, y = {
        'groups': None,
        'train_sizes': np.linspace(0.1, 1, 5),
        'cv': None,
        'scoring': None,
        'exploit_incremental_learning': False,
        'n_jobs': None,
        'pre_dispatch': 'all',
        'verbose': 0,
        'shuffle': False,
        'random_state': None,
        'error_score': np.nan,
        'fit_params': None,
        'ax': None,
        'negate_score': False,
        'score_name': None,
        'score_type': 'both',
        'std_display_style': 'fill_between',
        'line_kw': None,
        'fill_between_kw': None,
        'errorbar_kw': None }, *, groups, train_sizes, cv, scoring: check_matplotlib_support(f'''{cls.__name__}.from_estimator''')score_name = _validate_score_name(score_name, scoring, negate_score)(train_sizes, train_scores, test_scores) = learning_curve(estimator, X, y, groups = groups, train_sizes = train_sizes, cv = cv, scoring = scoring, exploit_incremental_learning = exploit_incremental_learning, n_jobs = n_jobs, pre_dispatch = pre_dispatch, verbose = verbose, shuffle = shuffle, random_state = random_state, error_score = error_score, return_times = False, params = fit_params)viz = cls(train_sizes = train_sizes, train_scores = train_scores, test_scores = test_scores, score_name = score_name)viz.plot(ax = ax, negate_score = negate_score, score_type = score_type, std_display_style = std_display_style, line_kw = line_kw, fill_between_kw = fill_between_kw, errorbar_kw = errorbar_kw))()


class ValidationCurveDisplay(_BaseCurveDisplay):
    '''Validation Curve visualization.

    It is recommended to use
    :meth:`~sklearn.model_selection.ValidationCurveDisplay.from_estimator` to
    create a :class:`~sklearn.model_selection.ValidationCurveDisplay` instance.
    All parameters are stored as attributes.

    Read more in the :ref:`User Guide <visualizations>` for general information
    about the visualization API and :ref:`detailed documentation
    <validation_curve>` regarding the validation curve visualization.

    .. versionadded:: 1.3

    Parameters
    ----------
    param_name : str
        Name of the parameter that has been varied.

    param_range : array-like of shape (n_ticks,)
        The values of the parameter that have been evaluated.

    train_scores : ndarray of shape (n_ticks, n_cv_folds)
        Scores on training sets.

    test_scores : ndarray of shape (n_ticks, n_cv_folds)
        Scores on test set.

    score_name : str, default=None
        The name of the score used in `validation_curve`. It will override the name
        inferred from the `scoring` parameter. If `score` is `None`, we use `"Score"` if
        `negate_score` is `False` and `"Negative score"` otherwise. If `scoring` is a
        string or a callable, we infer the name. We replace `_` by spaces and capitalize
        the first letter. We remove `neg_` and replace it by `"Negative"` if
        `negate_score` is `False` or just remove it otherwise.

    Attributes
    ----------
    ax_ : matplotlib Axes
        Axes with the validation curve.

    figure_ : matplotlib Figure
        Figure containing the validation curve.

    errorbar_ : list of matplotlib Artist or None
        When the `std_display_style` is `"errorbar"`, this is a list of
        `matplotlib.container.ErrorbarContainer` objects. If another style is
        used, `errorbar_` is `None`.

    lines_ : list of matplotlib Artist or None
        When the `std_display_style` is `"fill_between"`, this is a list of
        `matplotlib.lines.Line2D` objects corresponding to the mean train and
        test scores. If another style is used, `line_` is `None`.

    fill_between_ : list of matplotlib Artist or None
        When the `std_display_style` is `"fill_between"`, this is a list of
        `matplotlib.collections.PolyCollection` objects. If another style is
        used, `fill_between_` is `None`.

    See Also
    --------
    sklearn.model_selection.validation_curve : Compute the validation curve.

    Examples
    --------
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> from sklearn.datasets import make_classification
    >>> from sklearn.model_selection import ValidationCurveDisplay, validation_curve
    >>> from sklearn.linear_model import LogisticRegression
    >>> X, y = make_classification(n_samples=1_000, random_state=0)
    >>> logistic_regression = LogisticRegression()
    >>> param_name, param_range = "C", np.logspace(-8, 3, 10)
    >>> train_scores, test_scores = validation_curve(
    ...     logistic_regression, X, y, param_name=param_name, param_range=param_range
    ... )
    >>> display = ValidationCurveDisplay(
    ...     param_name=param_name, param_range=param_range,
    ...     train_scores=train_scores, test_scores=test_scores, score_name="Score"
    ... )
    >>> display.plot()
    <...>
    >>> plt.show()
    '''
    
    def __init__(self = None, *, param_name, param_range, train_scores, test_scores, score_name):
        self.param_name = param_name
        self.param_range = param_range
        self.train_scores = train_scores
        self.test_scores = test_scores
        self.score_name = score_name

    
    def plot(self = None, ax = (None,), *, negate_score, score_name, score_type, std_display_style, line_kw, fill_between_kw, errorbar_kw):
        '''Plot visualization.

        Parameters
        ----------
        ax : matplotlib Axes, default=None
            Axes object to plot on. If `None`, a new figure and axes is
            created.

        negate_score : bool, default=False
            Whether or not to negate the scores obtained through
            :func:`~sklearn.model_selection.validation_curve`. This is
            particularly useful when using the error denoted by `neg_*` in
            `scikit-learn`.

        score_name : str, default=None
            The name of the score used to decorate the y-axis of the plot. It will
            override the name inferred from the `scoring` parameter. If `score` is
            `None`, we use `"Score"` if `negate_score` is `False` and `"Negative score"`
            otherwise. If `scoring` is a string or a callable, we infer the name. We
            replace `_` by spaces and capitalize the first letter. We remove `neg_` and
            replace it by `"Negative"` if `negate_score` is
            `False` or just remove it otherwise.

        score_type : {"test", "train", "both"}, default="both"
            The type of score to plot. Can be one of `"test"`, `"train"`, or
            `"both"`.

        std_display_style : {"errorbar", "fill_between"} or None, default="fill_between"
            The style used to display the score standard deviation around the
            mean score. If None, no standard deviation representation is
            displayed.

        line_kw : dict, default=None
            Additional keyword arguments passed to the `plt.plot` used to draw
            the mean score.

        fill_between_kw : dict, default=None
            Additional keyword arguments passed to the `plt.fill_between` used
            to draw the score standard deviation.

        errorbar_kw : dict, default=None
            Additional keyword arguments passed to the `plt.errorbar` used to
            draw mean score and standard deviation score.

        Returns
        -------
        display : :class:`~sklearn.model_selection.ValidationCurveDisplay`
            Object that stores computed values.
        '''
        self._plot_curve(self.param_range, ax = ax, negate_score = negate_score, score_name = score_name, score_type = score_type, std_display_style = std_display_style, line_kw = line_kw, fill_between_kw = fill_between_kw, errorbar_kw = errorbar_kw)
        self.ax_.set_xlabel(f'''{self.param_name}''')
        return self

    from_estimator = (lambda cls, estimator, X = classmethod, y = {
        'groups': None,
        'cv': None,
        'scoring': None,
        'n_jobs': None,
        'pre_dispatch': 'all',
        'verbose': 0,
        'error_score': np.nan,
        'fit_params': None,
        'ax': None,
        'negate_score': False,
        'score_name': None,
        'score_type': 'both',
        'std_display_style': 'fill_between',
        'line_kw': None,
        'fill_between_kw': None,
        'errorbar_kw': None }, *, param_name, param_range, groups, cv: check_matplotlib_support(f'''{cls.__name__}.from_estimator''')score_name = _validate_score_name(score_name, scoring, negate_score)(train_scores, test_scores) = validation_curve(estimator, X, y, param_name = param_name, param_range = param_range, groups = groups, cv = cv, scoring = scoring, n_jobs = n_jobs, pre_dispatch = pre_dispatch, verbose = verbose, error_score = error_score, params = fit_params)viz = cls(param_name = param_name, param_range = np.asarray(param_range), train_scores = train_scores, test_scores = test_scores, score_name = score_name)viz.plot(ax = ax, negate_score = negate_score, score_type = score_type, std_display_style = std_display_style, line_kw = line_kw, fill_between_kw = fill_between_kw, errorbar_kw = errorbar_kw))()
