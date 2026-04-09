# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: version.pyc (Python 3.11)

import pkg_resources

try:
    __version__ = pkg_resources.get_distribution('setuptools').version
    return None
except Exception:
    __version__ = 'unknown'
    return None
