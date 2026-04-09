# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Configure global settings and get information about the working environment.'''
import importlib as _importlib
import logging
import os
import random
from sklearn._config import config_context, get_config, set_config
logger = logging.getLogger(__name__)
__version__ = '1.8.0'
os.environ.setdefault('KMP_DUPLICATE_LIB_OK', 'True')
os.environ.setdefault('KMP_INIT_AT_FORK', 'FALSE')
from sklearn import __check_build, _distributor_init
from sklearn.base import clone
from sklearn.utils._show_versions import show_versions
_submodules = [
    'calibration',
    'cluster',
    'covariance',
    'cross_decomposition',
    'datasets',
    'decomposition',
    'dummy',
    'ensemble',
    'exceptions',
    'experimental',
    'externals',
    'feature_extraction',
    'feature_selection',
    'frozen',
    'gaussian_process',
    'inspection',
    'isotonic',
    'kernel_approximation',
    'kernel_ridge',
    'linear_model',
    'manifold',
    'metrics',
    'mixture',
    'model_selection',
    'multiclass',
    'multioutput',
    'naive_bayes',
    'neighbors',
    'neural_network',
    'pipeline',
    'preprocessing',
    'random_projection',
    'semi_supervised',
    'svm',
    'tree',
    'discriminant_analysis',
    'impute',
    'compose']
__all__ = _submodules + [
    'clone',
    'get_config',
    'set_config',
    'config_context',
    'show_versions']

def __dir__():
    return __all__


def __getattr__(name):
    if name in _submodules:
        return _importlib.import_module(f'''sklearn.{name}''')
    
    try:
        return globals()[name]
    except KeyError:
        raise AttributeError(f'''Module \'sklearn\' has no attribute \'{name}\'''')



def setup_module(module):
    '''Fixture for the tests to assure globally controllable seeding of RNGs'''
    import numpy as np
    _random_seed = os.environ.get('SKLEARN_SEED', None)
# WARNING: Decompyle incomplete
