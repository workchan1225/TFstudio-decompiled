# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: unraisableexception.pyc (Python 3.11)

from __future__ import annotations
import collections
from collections.abc import Callable
import functools
import gc
import sys
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
gc_collect_iterations_key = StashKey[int]()

def gc_collect_harder(iterations = None):
    for _ in range(iterations):
        gc.collect()
        return None


class UnraisableMeta(NamedTuple):
    exc_value: 'BaseException | None' = 'UnraisableMeta'

unraisable_exceptions: 'StashKey[collections.deque[UnraisableMeta | BaseException]]' = StashKey()

def collect_unraisable(config = None):
    pop_unraisable = config.stash[unraisable_exceptions].pop
    errors = []
    meta = None
    hook_error = None
# WARNING: Decompyle incomplete


def cleanup(*, config, prev_hook):
    gc_collect_iterations = config.stash.get(gc_collect_iterations_key, 5)
    
    try:
        gc_collect_harder(gc_collect_iterations)
        collect_unraisable(config)
        
        try:
            sys.unraisablehook = prev_hook
        sys.unraisablehook = prev_hook
        try:
            del config.stash[unraisable_exceptions]
            return None
        except:
            del config.stash[unraisable_exceptions]




def unraisable_hook(unraisable = None, *, append):
    pass
# WARNING: Decompyle incomplete


def pytest_configure(config = None):
    prev_hook = sys.unraisablehook
    deque = collections.deque()
    config.stash[unraisable_exceptions] = deque
    config.add_cleanup(functools.partial(cleanup, config = config, prev_hook = prev_hook))
    sys.unraisablehook = functools.partial(unraisable_hook, append = deque.append)

pytest_runtest_setup = (lambda item = None: collect_unraisable(item.config))()
pytest_runtest_call = (lambda item = None: collect_unraisable(item.config))()
pytest_runtest_teardown = (lambda item = None: collect_unraisable(item.config))()
