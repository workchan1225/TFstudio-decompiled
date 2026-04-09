# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: Windows.pyc (Python 3.11)

from __future__ import annotations
import logging
from jaraco.context import ExceptionTrap
from backend import KeyringBackend
from compat import properties
from credentials import SimpleCredential
from errors import PasswordDeleteError
missing_deps = ExceptionTrap()
from win32ctypes.pywin32 import pywintypes, win32cred
win32cred.__name__
