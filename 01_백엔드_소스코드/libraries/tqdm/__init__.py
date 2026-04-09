# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from _monitor import TMonitor, TqdmSynchronisationWarning
from _tqdm_pandas import tqdm_pandas
from cli import main
from gui import tqdm as tqdm_gui
from gui import trange as tgrange
from std import TqdmDeprecationWarning, TqdmExperimentalWarning, TqdmKeyError, TqdmMonitorWarning, TqdmTypeError, TqdmWarning, tqdm, trange
from version import __version__
__all__ = [
    'tqdm',
    'tqdm_gui',
    'trange',
    'tgrange',
    'tqdm_pandas',
    'tqdm_notebook',
    'tnrange',
    'main',
    'TMonitor',
    'TqdmTypeError',
    'TqdmKeyError',
    'TqdmWarning',
    'TqdmDeprecationWarning',
    'TqdmExperimentalWarning',
    'TqdmMonitorWarning',
    'TqdmSynchronisationWarning',
    '__version__']

def tqdm_notebook(*args, **kwargs):
    '''See tqdm.notebook.tqdm for full documentation'''
    warn = warn
    import warnings
    _tqdm_notebook = tqdm
    import notebook
    warn('This function will be removed in tqdm==5.0.0\nPlease use `tqdm.notebook.tqdm` instead of `tqdm.tqdm_notebook`', TqdmDeprecationWarning, stacklevel = 2)
# WARNING: Decompyle incomplete


def tnrange(*args, **kwargs):
    '''Shortcut for `tqdm.notebook.tqdm(range(*args), **kwargs)`.'''
    warn = warn
    import warnings
    _tnrange = trange
    import notebook
    warn('Please use `tqdm.notebook.trange` instead of `tqdm.tnrange`', TqdmDeprecationWarning, stacklevel = 2)
# WARNING: Decompyle incomplete
