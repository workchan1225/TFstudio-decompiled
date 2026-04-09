# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parallel.pyc (Python 3.11)

'''Customizations of :mod:`joblib` and :mod:`threadpoolctl` tools for scikit-learn
usage.
'''
import functools
import warnings
from functools import update_wrapper
import joblib
from threadpoolctl import ThreadpoolController
from sklearn._config import config_context, get_config
_threadpool_controller = None

def _with_config_and_warning_filters(delayed_func, config, warning_filters):
    '''Helper function that intends to attach a config to a delayed function.'''
    if hasattr(delayed_func, 'with_config_and_warning_filters'):
        return delayed_func.with_config_and_warning_filters(config, warning_filters)
    None.warn('`sklearn.utils.parallel.Parallel` needs to be used in conjunction with `sklearn.utils.parallel.delayed` instead of `joblib.delayed` to correctly propagate the scikit-learn configuration to the joblib workers.', UserWarning)
    return delayed_func


class Parallel(joblib.Parallel):
    pass
# WARNING: Decompyle incomplete


def delayed(function):
    '''Decorator used to capture the arguments of a function.

    This alternative to `joblib.delayed` is meant to be used in conjunction
    with `sklearn.utils.parallel.Parallel`. The latter captures the scikit-
    learn configuration by calling `sklearn.get_config()` in the current
    thread, prior to dispatching the first task. The captured configuration is
    then propagated and enabled for the duration of the execution of the
    delayed function in the joblib workers.

    .. versionchanged:: 1.3
       `delayed` was moved from `sklearn.utils.fixes` to `sklearn.utils.parallel`
       in scikit-learn 1.3.

    Parameters
    ----------
    function : callable
        The function to be delayed.

    Returns
    -------
    output: tuple
        Tuple containing the delayed function, the positional arguments, and the
        keyword arguments.
    '''
    pass
# WARNING: Decompyle incomplete


class _FuncWrapper:
    '''Load the global configuration before calling the function.'''
    
    def __init__(self, function):
        self.function = function
        update_wrapper(self, self.function)

    
    def with_config_and_warning_filters(self, config, warning_filters):
        self.config = config
        self.warning_filters = warning_filters
        return self

    
    def __call__(self, *args, **kwargs):
        config = getattr(self, 'config', { })
        warning_filters = getattr(self, 'warning_filters', [])
        if not config or warning_filters:
            warnings.warn('`sklearn.utils.parallel.delayed` should be used with `sklearn.utils.parallel.Parallel` to make it possible to propagate the scikit-learn configuration of the current thread to the joblib workers.', UserWarning)
    # WARNING: Decompyle incomplete



def _get_threadpool_controller():
    '''Return the global threadpool controller instance.'''
    pass
# WARNING: Decompyle incomplete


def _threadpool_controller_decorator(limits, user_api = (1, 'blas')):
    '''Decorator to limit the number of threads used at the function level.

    It should be preferred over `threadpoolctl.ThreadpoolController.wrap` because this
    one only loads the shared libraries when the function is called while the latter
    loads them at import time.
    '''
    pass
# WARNING: Decompyle incomplete
