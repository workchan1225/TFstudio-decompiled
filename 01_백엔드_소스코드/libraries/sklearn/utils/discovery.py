# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: discovery.pyc (Python 3.11)

'''Utilities to discover scikit-learn objects.'''
import inspect
import pkgutil
from importlib import import_module
from operator import itemgetter
from pathlib import Path
_MODULE_TO_IGNORE = {
    'setup',
    'tests',
    'conftest',
    'externals',
    'experimental',
    'estimator_checks'}

def all_estimators(type_filter = (None,)):
    '''Get a list of all estimators from `sklearn`.

    This function crawls the module and gets all classes that inherit
    from BaseEstimator. Classes that are defined in test-modules are not
    included.

    Parameters
    ----------
    type_filter : {"classifier", "regressor", "cluster", "transformer"}             or list of such str, default=None
        Which kind of estimators should be returned. If None, no filter is
        applied and all estimators are returned.  Possible values are
        \'classifier\', \'regressor\', \'cluster\' and \'transformer\' to get
        estimators only of these specific types, or a list of these to
        get the estimators that fit at least one of the types.

    Returns
    -------
    estimators : list of tuples
        List of (name, class), where ``name`` is the class name as string
        and ``class`` is the actual type of the class.

    Examples
    --------
    >>> from sklearn.utils.discovery import all_estimators
    >>> estimators = all_estimators()
    >>> type(estimators)
    <class \'list\'>
    >>> type(estimators[0])
    <class \'tuple\'>
    >>> estimators[:2]
    [(\'ARDRegression\', <class \'sklearn.linear_model._bayes.ARDRegression\'>),
     (\'AdaBoostClassifier\',
      <class \'sklearn.ensemble._weight_boosting.AdaBoostClassifier\'>)]
    >>> classifiers = all_estimators(type_filter="classifier")
    >>> classifiers[:2]
    [(\'AdaBoostClassifier\',
      <class \'sklearn.ensemble._weight_boosting.AdaBoostClassifier\'>),
     (\'BaggingClassifier\', <class \'sklearn.ensemble._bagging.BaggingClassifier\'>)]
    >>> regressors = all_estimators(type_filter="regressor")
    >>> regressors[:2]
    [(\'ARDRegression\', <class \'sklearn.linear_model._bayes.ARDRegression\'>),
     (\'AdaBoostRegressor\',
      <class \'sklearn.ensemble._weight_boosting.AdaBoostRegressor\'>)]
    >>> both = all_estimators(type_filter=["classifier", "regressor"])
    >>> both[:2]
    [(\'ARDRegression\', <class \'sklearn.linear_model._bayes.ARDRegression\'>),
     (\'AdaBoostClassifier\',
      <class \'sklearn.ensemble._weight_boosting.AdaBoostClassifier\'>)]
    '''
    pass
# WARNING: Decompyle incomplete


def all_displays():
    """Get a list of all displays from `sklearn`.

    Returns
    -------
    displays : list of tuples
        List of (name, class), where ``name`` is the display class name as
        string and ``class`` is the actual type of the class.

    Examples
    --------
    >>> from sklearn.utils.discovery import all_displays
    >>> displays = all_displays()
    >>> displays[0]
    ('CalibrationDisplay', <class 'sklearn.calibration.CalibrationDisplay'>)
    """
    ignore_warnings = ignore_warnings
    import sklearn.utils._testing
    all_classes = []
    root = str(Path(__file__).parent.parent)
    ignore_warnings(category = FutureWarning)
    for _, module_name, _ in pkgutil.walk_packages(path = [
        root], prefix = 'sklearn.'):
        module_parts = module_name.split('.')
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(module_parts()) or '._' in module_name:
            continue
        module = import_module(module_name)
        classes = inspect.getmembers(module, inspect.isclass)
        classes = classes()
        all_classes.extend(classes)
        None(None, None)
    with None:
        if not (lambda .0: pass# WARNING: Decompyle incomplete
):
            pass
    any
    return sorted(set(all_classes), key = itemgetter(0))


def _is_checked_function(item):
    if not inspect.isfunction(item):
        return False
    if None.__name__.startswith('_'):
        return False
    mod = None.__module__
    if mod.startswith('sklearn.') or mod.endswith('estimator_checks'):
        return False


def all_functions():
    """Get a list of all functions from `sklearn`.

    Returns
    -------
    functions : list of tuples
        List of (name, function), where ``name`` is the function name as
        string and ``function`` is the actual function.

    Examples
    --------
    >>> from sklearn.utils.discovery import all_functions
    >>> functions = all_functions()
    >>> name, function = functions[0]
    >>> name
    'accuracy_score'
    """
    ignore_warnings = ignore_warnings
    import sklearn.utils._testing
    all_functions = []
    root = str(Path(__file__).parent.parent)
    ignore_warnings(category = FutureWarning)
    for _, module_name, _ in pkgutil.walk_packages(path = [
        root], prefix = 'sklearn.'):
        module_parts = module_name.split('.')
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(module_parts()) or '._' in module_name:
            continue
        module = import_module(module_name)
        functions = inspect.getmembers(module, _is_checked_function)
        functions = functions()
        all_functions.extend(functions)
        None(None, None)
    with None:
        if not (lambda .0: pass# WARNING: Decompyle incomplete
):
            pass
    any
    return sorted(set(all_functions), key = itemgetter(0))
