# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: memoryutils.pyc (Python 3.11)

'''
Memory monitoring utilities for measuring memory usage.

Example usage:
    tracker = MemoryTracker("my_function")
    with tracker.monitor():
        my_function()
    # Access data: tracker.rss_delta, tracker.duration, etc.
    # Get formatted string: tracker.get_summary()
'''
from __future__ import annotations
import os
import contextlib
import time
from typing import Dict, Optional

try:
    import psutil
    _HAS_PSUTIL = True
except ImportError:
    _HAS_PSUTIL = False

IS_SUPPORTED = _HAS_PSUTIL

def get_available_memory():
