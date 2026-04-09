# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _set_output.pyc (Python 3.11)

import importlib
from functools import wraps
from typing import Protocol, runtime_checkable
import numpy as np
from scipy.sparse import issparse
from sklearn._config import get_config
from sklearn.utils._available_if import available_if

def check_library_installed(library):
    '''Check library is installed.'''
    
    try:
        return importlib.import_module(library)
    except ImportError:
        exc = None
        raise ImportError(f'''Setting output container to \'{library}\' requires {library} to be installed'''), exc
        exc = None
        del exc



def get_columns(columns):
    if callable(columns):
        
        try:
            return columns()
        except Exception:
            return None
            return columns


ContainerAdapterProtocol = <NODE:12>()

class PandasAdapter:
    container_lib = 'pandas'
    
    def create_container(self, X_output, X_original, columns, inplace = (True,)):
        pd = check_library_installed('pandas')
        columns = get_columns(columns)
        if not inplace or isinstance(X_output, pd.DataFrame):
            if isinstance(X_output, pd.DataFrame):
                index = X_output.index
            elif isinstance(X_original, (pd.DataFrame, pd.Series)):
                index = X_original.index
            else:
                index = None
            X_output = pd.DataFrame(X_output, index = index, copy = not inplace)
    # WARNING: Decompyle incomplete

    
    def is_supported_container(self, X):
        pd = check_library_installed('pandas')
        return isinstance(X, pd.DataFrame)

    
    def rename_columns(self, X, columns):
        X.columns = columns
        return X

    
    def hstack(self, Xs):
        pd = check_library_installed('pandas')
        return pd.concat(Xs, axis = 1)



class PolarsAdapter:
    container_lib = 'polars'
    
    def create_container(self, X_output, X_original, columns, inplace = (True,)):
        pl = check_library_installed('polars')
        columns = get_columns(columns)
        columns = columns.tolist() if isinstance(columns, np.ndarray) else columns
        if not inplace or isinstance(X_output, pl.DataFrame):
            return pl.DataFrame(X_output, schema = columns, orient = 'row')
    # WARNING: Decompyle incomplete

    
    def is_supported_container(self, X):
        pl = check_library_installed('polars')
        return isinstance(X, pl.DataFrame)

    
    def rename_columns(self, X, columns):
        X.columns = columns
        return X

    
    def hstack(self, Xs):
        pl = check_library_installed('polars')
        return pl.concat(Xs, how = 'horizontal')



class ContainerAdaptersManager:
    
    def __init__(self):
        self.adapters = { }

    supported_outputs = (lambda self: {
'default'} | set(self.adapters))()
    
    def register(self, adapter):
        self.adapters[adapter.container_lib] = adapter


ADAPTERS_MANAGER = ContainerAdaptersManager()
ADAPTERS_MANAGER.register(PandasAdapter())
ADAPTERS_MANAGER.register(PolarsAdapter())

def _get_adapter_from_container(container):
    '''Get the adapter that knows how to handle such container.

    See :class:`sklearn.utils._set_output.ContainerAdapterProtocol` for more
    details.
    '''
    module_name = container.__class__.__module__.split('.')[0]
    
    try:
        return ADAPTERS_MANAGER.adapters[module_name]
    except KeyError:
        exc = None
        available_adapters = list(ADAPTERS_MANAGER.adapters.keys())
        raise ValueError(f'''The container does not have a registered adapter in scikit-learn. Available adapters are: {available_adapters} while the container provided is: {container!r}.'''), exc
        exc = None
        del exc



def _get_container_adapter(method, estimator = (None,)):
    '''Get container adapter.'''
    dense_config = _get_output_config(method, estimator)['dense']
    
    try:
        return ADAPTERS_MANAGER.adapters[dense_config]
    except KeyError:
        return None



def _get_output_config(method, estimator = (None,)):
    '''Get output config based on estimator and global configuration.

    Parameters
    ----------
    method : {"transform"}
        Estimator\'s method for which the output container is looked up.

    estimator : estimator instance or None
        Estimator to get the output configuration from. If `None`, check global
        configuration is used.

    Returns
    -------
    config : dict
        Dictionary with keys:

        - "dense": specifies the dense container for `method`. This can be
          `"default"` or `"pandas"`.
    '''
    est_sklearn_output_config = getattr(estimator, '_sklearn_output_config', { })
    if method in est_sklearn_output_config:
        dense_config = est_sklearn_output_config[method]
    else:
        dense_config = get_config()[f'''{method}_output''']
    supported_outputs = ADAPTERS_MANAGER.supported_outputs
    if dense_config not in supported_outputs:
        raise ValueError(f'''output config must be in {sorted(supported_outputs)}, got {dense_config}''')
    return {
        'dense': dense_config }


def _wrap_data_with_container(method, data_to_wrap, original_input, estimator):
    '''Wrap output with container based on an estimator\'s or global config.

    Parameters
    ----------
    method : {"transform"}
        Estimator\'s method to get container output for.

    data_to_wrap : {ndarray, dataframe}
        Data to wrap with container.

    original_input : {ndarray, dataframe}
        Original input of function.

    estimator : estimator instance
        Estimator with to get the output configuration from.

    Returns
    -------
    output : {ndarray, dataframe}
        If the output config is "default" or the estimator is not configured
        for wrapping return `data_to_wrap` unchanged.
        If the output config is "pandas", return `data_to_wrap` as a pandas
        DataFrame.
    '''
    output_config = _get_output_config(method, estimator)
    if not output_config['dense'] == 'default' or _auto_wrap_is_configured(estimator):
        return data_to_wrap
    dense_config = None['dense']
    if issparse(data_to_wrap):
        raise ValueError(f'''The transformer outputs a scipy sparse matrix. Try to set the transformer output to a dense array or disable {dense_config.capitalize()} output with set_output(transform=\'default\').''')
    adapter = ADAPTERS_MANAGER.adapters[dense_config]
    return adapter.create_container(data_to_wrap, original_input, columns = estimator.get_feature_names_out)


def _wrap_method_output(f, method):
    '''Wrapper used by `_SetOutputMixin` to automatically wrap methods.'''
    pass
# WARNING: Decompyle incomplete


def _auto_wrap_is_configured(estimator):
