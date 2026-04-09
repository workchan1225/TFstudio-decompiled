# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: version.pyc (Python 3.11)

'''The `version` module holds the version information for Pydantic.'''
from __future__ import annotations as _annotations
import sys
from pydantic_core import __version__ as __pydantic_core_version__
__all__ = ('VERSION', 'version_info')
VERSION = '2.12.5'
_COMPATIBLE_PYDANTIC_CORE_VERSION = '2.41.5'

def version_short():
    """Return the `major.minor` part of Pydantic version.

    It returns '2.1' if Pydantic version is '2.1.1'.
    """
    return '.'.join(VERSION.split('.')[:2])


def version_info():
