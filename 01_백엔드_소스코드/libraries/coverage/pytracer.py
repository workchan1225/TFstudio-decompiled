# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pytracer.pyc (Python 3.11)

__doc__ = 'Raw data collector for coverage.py.'
from __future__ import annotations
import atexit
import dis
import itertools
import sys
import threading
from types import FrameType, ModuleType
from typing import Any, Callable, cast
from coverage import env
from coverage.types import TArc, TFileDisposition, TLineNo, Tracer, TShouldStartContextFn, TShouldTraceFn, TTraceData, TTraceFileData, TTraceFn, TWarnFn
set_TLineNo = set[TLineNo]
set_TArc = set[TArc]
RESUME = dis.opmap.get('RESUME')
RETURN_VALUE = dis.opmap['RETURN_VALUE']
# WARNING: Decompyle incomplete
