# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: logging.pyc (Python 3.11)

import logging
from ctranslate2 import _ext
_PYTHON_TO_CT2_LEVEL = {
    logging.NOTSET: _ext.LogLevel.Trace,
    logging.DEBUG: _ext.LogLevel.Debug,
    logging.INFO: _ext.LogLevel.Info,
    logging.WARNING: _ext.LogLevel.Warning,
    logging.ERROR: _ext.LogLevel.Error,
    logging.CRITICAL: _ext.LogLevel.Critical }
_CT2_TO_PYTHON_LEVEL = _PYTHON_TO_CT2_LEVEL.items()()

def set_log_level(level = None):
    '''Sets the CTranslate2 logging level from a Python logging level.

    Arguments:
      level: A Python logging level.

    Example:

        >>> import logging
        >>> ctranslate2.set_log_level(logging.INFO)

    Note:
       The argument is a Python logging level for convenience, but this function
       controls the C++ logs of the library.
    '''
    ct2_level = _PYTHON_TO_CT2_LEVEL.get(level)
# WARNING: Decompyle incomplete


def get_log_level():
    '''Returns the current logging level.

    Returns:
      A Python logging level.
    '''
    ct2_level = _ext.get_log_level()
    return _CT2_TO_PYTHON_LEVEL[ct2_level]
