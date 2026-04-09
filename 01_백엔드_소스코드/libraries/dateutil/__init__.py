# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import sys

try:
    from _version import version as __version__
except ImportError:
    __version__ = 'unknown'

__all__ = [
    'easter',
    'parser',
    'relativedelta',
    'rrule',
    'tz',
    'utils',
    'zoneinfo']

def __getattr__(name):
    import importlib
    if name in __all__:
        return importlib.import_module('.' + name, __name__)
    raise None('module {!r} has not attribute {!r}'.format(__name__, name))


def __dir__():
    return globals()() + __all__
