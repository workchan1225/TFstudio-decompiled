# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Tools for model selection, such as cross validation and hyper-parameter tuning.'''
import typing
from sklearn.model_selection._classification_threshold import FixedThresholdClassifier, TunedThresholdClassifierCV
from sklearn.model_selection._plot import LearningCurveDisplay, ValidationCurveDisplay
from sklearn.model_selection._search import GridSearchCV, ParameterGrid, ParameterSampler, RandomizedSearchCV
from sklearn.model_selection._split import BaseCrossValidator, BaseShuffleSplit, GroupKFold, GroupShuffleSplit, KFold, LeaveOneGroupOut, LeaveOneOut, LeavePGroupsOut, LeavePOut, PredefinedSplit, RepeatedKFold, RepeatedStratifiedKFold, ShuffleSplit, StratifiedGroupKFold, StratifiedKFold, StratifiedShuffleSplit, TimeSeriesSplit, check_cv, train_test_split
from sklearn.model_selection._validation import cross_val_predict, cross_val_score, cross_validate, learning_curve, permutation_test_score, validation_curve
if typing.TYPE_CHECKING:
    from sklearn.model_selection._search_successive_halving import HalvingGridSearchCV, HalvingRandomSearchCV
__all__ = [
    'BaseCrossValidator',
    'BaseShuffleSplit',
    'FixedThresholdClassifier',
    'GridSearchCV',
    'GroupKFold',
    'GroupShuffleSplit',
    'HalvingGridSearchCV',
    'HalvingRandomSearchCV',
    'KFold',
    'LearningCurveDisplay',
    'LeaveOneGroupOut',
    'LeaveOneOut',
    'LeavePGroupsOut',
    'LeavePOut',
    'ParameterGrid',
    'ParameterSampler',
    'PredefinedSplit',
    'RandomizedSearchCV',
    'RepeatedKFold',
    'RepeatedStratifiedKFold',
    'ShuffleSplit',
    'StratifiedGroupKFold',
    'StratifiedKFold',
    'StratifiedShuffleSplit',
    'TimeSeriesSplit',
    'TunedThresholdClassifierCV',
    'ValidationCurveDisplay',
    'check_cv',
    'cross_val_predict',
    'cross_val_score',
    'cross_validate',
    'learning_curve',
    'permutation_test_score',
    'train_test_split',
    'validation_curve']

def __getattr__(name):
    if name in frozenset({'HalvingGridSearchCV', 'HalvingRandomSearchCV'}):
        raise ImportError(f'''{name} is experimental and the API might change without any deprecation cycle. To use it, you need to explicitly import enable_halving_search_cv:\nfrom sklearn.experimental import enable_halving_search_cv''')
    raise AttributeError(f'''module {__name__} has no attribute {name}''')
