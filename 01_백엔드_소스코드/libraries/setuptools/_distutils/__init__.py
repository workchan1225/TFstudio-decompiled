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
import importlib
__version__ = None[sys.version:sys.version.index(' ')]

try:
    importlib.import_module('_distutils_system_mod')
    return None
except ImportError:
    return None
