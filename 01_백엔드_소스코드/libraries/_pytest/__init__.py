# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import annotations
__all__ = [
    '__version__',
    'version_tuple']

try:
    from _version import version as __version__
    from _version import version_tuple
    return None
except ImportError:
    __version__ = 'unknown'
    version_tuple = (0, 0, 'unknown')
    return None
