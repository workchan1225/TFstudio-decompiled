# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _testing.pyc (Python 3.11)

from __future__ import annotations
import types
from abc import ABCMeta, abstractmethod
from collections.abc import AsyncGenerator, Callable, Coroutine, Iterable
from typing import Any, TypeVar
_T = TypeVar('_T')

def TestRunner():
    '''TestRunner'''
    __doc__ = '\n    Encapsulates a running event loop. Every call made through this object will use the\n    same event loop.\n    '
    
    def __enter__(self = None):
        return self

    __exit__ = (lambda self = None, exc_type = None, exc_val = abstractmethod, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'types.TracebackType | None', 'return', 'bool | None'): pass)()
    run_asyncgen_fixture = (lambda self = None, fixture_func = None, kwargs = abstractmethod: pass)()
    run_fixture = (lambda self = None, fixture_func = None, kwargs = abstractmethod: pass)()
    run_test = (lambda self = None, test_func = None, kwargs = abstractmethod: pass)()

TestRunner = <NODE:27>(TestRunner, 'TestRunner', metaclass = ABCMeta)
