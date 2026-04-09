# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _windows.pyc (Python 3.11)

import sys
from dataclasses import dataclass
WindowsConsoleFeatures = <NODE:12>()

try:
    import ctypes
    from ctypes import LibraryLoader
    if sys.platform == 'win32':
        windll = LibraryLoader(ctypes.WinDLL)
    else:
        windll = None
        raise ImportError('Not windows')
    from rich._win32_console import ENABLE_VIRTUAL_TERMINAL_PROCESSING, GetConsoleMode, GetStdHandle, LegacyWindowsError
    
    def get_windows_console_features():
