# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: timing.pyc (Python 3.11)

'''Indirection for time functions.

We intentionally grab some "time" functions internally to avoid tests mocking "time" to affect
pytest runtime information (issue #185).

Fixture "mock_timing" also interacts with this module for pytest\'s own tests.
'''
from __future__ import annotations
import dataclasses
from datetime import datetime
from datetime import timezone
from time import perf_counter
from time import sleep
from time import time
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pytest import MonkeyPatch
Instant = <NODE:12>()
Duration = <NODE:12>()
MockTiming = <NODE:12>()
__all__ = [
    'perf_counter',
    'sleep',
    'time']
