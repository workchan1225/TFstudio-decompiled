# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _compat.pyc (Python 3.11)

import sys
import platform
__all__ = [
    'install',
    'NullFinder',
    'Protocol']

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol


def install(cls):
    '''
    Class decorator for installation on sys.meta_path.

    Adds the backport DistributionFinder to sys.meta_path and
    attempts to disable the finder functionality of the stdlib
    DistributionFinder.
    '''
    sys.meta_path.append(cls())
    disable_stdlib_finder()
    return cls


def disable_stdlib_finder():
    '''
    Give the backport primacy for discovering path-based distributions
    by monkey-patching the stdlib O_O.

    See #91 for more background for rationale on this sketchy
    behavior.
    '''
    
    def matches(finder):
