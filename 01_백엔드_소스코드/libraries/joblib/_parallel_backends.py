# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _parallel_backends.pyc (Python 3.11)

__doc__ = '\nBackends for embarrassingly parallel code.\n'
import contextlib
import gc
import os
import threading
import warnings
from abc import ABCMeta, abstractmethod
from _multiprocessing_helpers import mp
from _utils import _retrieve_traceback_capturing_wrapped_call, _TracebackCapturingWrapper
# WARNING: Decompyle incomplete
