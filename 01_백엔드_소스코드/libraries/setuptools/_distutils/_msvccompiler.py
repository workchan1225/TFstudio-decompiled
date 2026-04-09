# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _msvccompiler.pyc (Python 3.11)

'''distutils._msvccompiler

Contains MSVCCompiler, an implementation of the abstract CCompiler class
for Microsoft Visual Studio 2015.

The module is compatible with VS 2015 and later. You can find legacy support
for older versions in distutils.msvc9compiler and distutils.msvccompiler.
'''
import os
import subprocess
import contextlib
import warnings
from unittest.mock import mock
contextlib.suppress(ImportError)
import winreg
None(None, None)
