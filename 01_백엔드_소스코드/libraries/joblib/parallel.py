# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parallel.pyc (Python 3.11)

__doc__ = '\nHelpers for embarrassingly parallel code.\n'
from __future__ import division
import collections
import functools
import itertools
import os
import queue
import sys
import threading
import time
import warnings
import weakref
from contextlib import nullcontext
from math import floor, log10, sqrt
from multiprocessing import TimeoutError
from numbers import Integral
from uuid import uuid4
from _multiprocessing_helpers import mp
from _parallel_backends import AutoBatchingMixin, FallbackToBackend, LokyBackend, MultiprocessingBackend, ParallelBackendBase, SequentialBackend, ThreadingBackend
from _utils import _Sentinel, eval_expr
from disk import memstr_to_bytes
from logger import Logger, short_format_time
BACKENDS = {
    'threading': ThreadingBackend,
    'sequential': SequentialBackend }
DEFAULT_BACKEND = 'threading'
DEFAULT_THREAD_BACKEND = 'threading'
DEFAULT_PROCESS_BACKEND = 'threading'
MAYBE_AVAILABLE_BACKENDS = {
    'multiprocessing',
    'loky'}
# WARNING: Decompyle incomplete
