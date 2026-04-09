# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
pandas._config is considered explicitly upstream of everything else in pandas,
should have no intra-pandas dependencies.

importing `dates` and `display` ensures that keys needed by _libs
are initialized.
'''
__all__ = [
    'config',
    'describe_option',
    'detect_console_encoding',
    'get_option',
    'option_context',
    'options',
    'reset_option',
    'set_option']
from pandas._config import config
from pandas._config import dates
from pandas._config.config import _global_config, describe_option, get_option, option_context, options, reset_option, set_option
from pandas._config.display import detect_console_encoding

def using_string_dtype():
    _mode_options = _global_config['future']
    return _mode_options['infer_string']


def using_python_scalars():
    _mode_options = _global_config['future']
    return _mode_options['python_scalars']


def is_nan_na():
    _mode_options = _global_config['future']
    return not _mode_options['distinguish_nan_and_na']
