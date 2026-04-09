# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: threadexception.pyc (Python 3.11)

from __future__ import annotations
import collections
from collections.abc import Callable
import functools
import sys
import threading
import traceback
from typing import NamedTuple
from typing import TYPE_CHECKING
import warnings
from _pytest.config import Config
from _pytest.nodes import Item
from _pytest.stash import StashKey
from _pytest.tracemalloc import tracemalloc_message
import pytest
if TYPE_CHECKING:
    pass
if sys.version_info < (3, 11):
    from exceptiongroup import ExceptionGroup

class ThreadExceptionMeta(NamedTuple):
    exc_value: 'BaseException | None' = 'ThreadExceptionMeta'

thread_exceptions: 'StashKey[collections.deque[ThreadExceptionMeta | BaseException]]' = StashKey()

def collect_thread_exception(config = None):
    pop_thread_exception = config.stash[thread_exceptions].pop
    errors = []
    meta = None
    hook_error = None
# WARNING: Decompyle incomplete


def cleanup(*, config, prev_hook):
    
    try:
        collect_thread_exception(config)
        
        try:
            threading.excepthook = prev_hook
        threading.excepthook = prev_hook
        try:
            del config.stash[thread_exceptions]
            return None
        except:
            del config.stash[thread_exceptions]




def thread_exception_hook(args = None, *, append):
    pass
# WARNING: Decompyle incomplete


def pytest_configure(config = None):
    prev_hook = threading.excepthook
    deque = collections.deque()
    config.stash[thread_exceptions] = deque
    config.add_cleanup(functools.partial(cleanup, config = config, prev_hook = prev_hook))
    threading.excepthook = functools.partial(thread_exception_hook, append = deque.append)

pytest_runtest_setup = (lambda item = None: collect_thread_exception(item.config))()
pytest_runtest_call = (lambda item = None: collect_thread_exception(item.config))()
pytest_runtest_teardown = (lambda item = None: collect_thread_exception(item.config))()
