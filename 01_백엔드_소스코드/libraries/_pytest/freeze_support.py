# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: freeze_support.pyc (Python 3.11)

'''Provides a function to report all internal modules for using freezing
tools.'''
from __future__ import annotations
from collections.abc import Iterator
import types

def freeze_includes():
    '''Return a list of module names used by pytest that should be
    included by cx_freeze.'''
    import _pytest
    result = list(_iter_all_modules(_pytest))
    return result


def _iter_all_modules(package = None, prefix = None):
    """Iterate over the names of all modules that can be found in the given
    package, recursively.

        >>> import _pytest
        >>> list(_iter_all_modules(_pytest))
        ['_pytest._argcomplete', '_pytest._code.code', ...]
    """
    pass
# WARNING: Decompyle incomplete
