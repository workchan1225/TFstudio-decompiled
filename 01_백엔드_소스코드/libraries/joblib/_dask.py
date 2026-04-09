# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _dask.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import asyncio
import concurrent.futures as concurrent
import contextlib
import time
import weakref
from uuid import uuid4
from _utils import _retrieve_traceback_capturing_wrapped_call, _TracebackCapturingWrapper
from parallel import AutoBatchingMixin, ParallelBackendBase, parallel_config

try:
    import dask
    import distributed
except ImportError:
    dask = None
    distributed = None

# WARNING: Decompyle incomplete
