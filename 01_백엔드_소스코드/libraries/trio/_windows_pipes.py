# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _windows_pipes.pyc (Python 3.11)

from __future__ import annotations
import sys
from typing import TYPE_CHECKING
from  import _core
from _abc import ReceiveStream, SendStream
from _core._windows_cffi import _handle, kernel32, raise_winerror
from _util import ConflictDetector, final
# WARNING: Decompyle incomplete
