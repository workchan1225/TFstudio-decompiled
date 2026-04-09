# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''distutils

The main package for the Python Module Distribution Utilities.  Normally
used from a setup script as

   from distutils.core import setup

   setup (...)
'''
import sys
import warnings
__version__ = None[sys.version:sys.version.index(' ')]
_DEPRECATION_MESSAGE = 'The distutils package is deprecated and slated for removal in Python 3.12. Use setuptools or check PEP 632 for potential alternatives'
warnings.warn(_DEPRECATION_MESSAGE, DeprecationWarning, 2)
