# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _io_common.pyc (Python 3.11)

from __future__ import annotations
import copy
from typing import TYPE_CHECKING
import outcome
from  import _core
if TYPE_CHECKING:
    from _io_epoll import EpollWaiters
    from _io_windows import AFDWaiters

def wake_all(waiters = None, exc = None):
    
    try:
        current_task = _core.current_task()
    except RuntimeError:
        current_task = None

    raise_at_end = False
# WARNING: Decompyle incomplete
