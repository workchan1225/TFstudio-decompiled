# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sysmon.pyc (Python 3.11)

__doc__ = 'Callback functions and support for sys.monitoring data collection.'
from __future__ import annotations
import collections
import functools
import inspect
import os
import os.path as os
import sys
import threading
import traceback
from dataclasses import dataclass
from types import CodeType
from typing import Any, Callable, NewType, Optional, cast
from coverage import env
from coverage.bytecode import TBranchTrails, always_jumps, branch_trails
from coverage.debug import short_filename, short_stack
from coverage.exceptions import NoSource, NotPython
from coverage.misc import isolate_module
from coverage.parser import PythonParser
from coverage.types import AnyCallable, TFileDisposition, TLineNo, TOffset, Tracer, TShouldStartContextFn, TShouldTraceFn, TTraceData, TTraceFileData, TWarnFn
os = isolate_module(os)
LOG = bool(int(os.getenv('COVERAGE_SYSMON_LOG', 0)))
COLLECT_STATS = bool(int(os.getenv('COVERAGE_SYSMON_STATS', 0)))
sys_monitoring = getattr(sys, 'monitoring', None)
DISABLE_TYPE = NewType('DISABLE_TYPE', object)
MonitorReturn = Optional[DISABLE_TYPE]
DISABLE = cast(MonitorReturn, getattr(sys_monitoring, 'DISABLE', None))
# WARNING: Decompyle incomplete
