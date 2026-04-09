# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: unittest.pyc (Python 3.11)

'''Discover and run std-library "unittest" style tests.'''
from __future__ import annotations
from collections.abc import Callable
from collections.abc import Generator
from collections.abc import Iterable
from collections.abc import Iterator
from enum import auto
from enum import Enum
import inspect
import sys
import traceback
import types
from typing import Any
from typing import TYPE_CHECKING
from unittest import TestCase
import _pytest._code as _pytest
from _pytest._code import ExceptionInfo
from _pytest.compat import assert_never
from _pytest.compat import is_async_function
from _pytest.config import hookimpl
from _pytest.fixtures import FixtureRequest
from _pytest.monkeypatch import MonkeyPatch
from _pytest.nodes import Collector
from _pytest.nodes import Item
from _pytest.outcomes import exit
from _pytest.outcomes import fail
from _pytest.outcomes import skip
from _pytest.outcomes import xfail
from _pytest.python import Class
from _pytest.python import Function
from _pytest.python import Module
from _pytest.runner import CallInfo
from _pytest.runner import check_interactive_exception
from _pytest.subtests import SubtestContext
from _pytest.subtests import SubtestReport
if sys.version_info[:2] < (3, 11):
    from exceptiongroup import ExceptionGroup
if TYPE_CHECKING:
    from types import TracebackType
    import unittest
    import twisted.trial.unittest as twisted
_SysExcInfoType = tuple[(type[BaseException], BaseException, types.TracebackType)] | tuple[(None, None, None)]

def pytest_pycollect_makeitem(collector = None, name = None, obj = None):
    
    try:
        ut = sys.modules['unittest']
        if not issubclass(obj, ut.TestCase):
            return None
    except Exception:
        return None
        if inspect.isabstract(obj):
            return None
        return None.from_parent(collector, name = name, obj = obj)



class UnitTestCase(Class):
    nofuncargs = True
    
    def newinstance(self):
        return self.obj('runTest')

    
    def collect(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _register_unittest_setup_class_fixture(self = None, cls = None):
        '''Register an auto-use fixture to invoke setUpClass and
        tearDownClass (#517).'''
        pass
    # WARNING: Decompyle incomplete

    
    def _register_unittest_setup_method_fixture(self = None, cls = None):
        '''Register an auto-use fixture to invoke setup_method and
        teardown_method (#517).'''
        pass
    # WARNING: Decompyle incomplete



class TestCaseFunction(Function):
    pass
# WARNING: Decompyle incomplete

pytest_runtest_makereport = (lambda item = None, call = None: pass# WARNING: Decompyle incomplete
)()

def _is_skipped(obj = None):
    '''Return True if the given object has been marked with @unittest.skip.'''
    return bool(getattr(obj, '__unittest_skip__', False))


def pytest_configure():
    '''Register the TestCaseFunction class as an IReporter if twisted.trial is available.'''
    if _get_twisted_version() is not TwistedVersion.NotInstalled:
        IReporter = IReporter
        import twisted.trial.itrial
        classImplements = classImplements
        import zope.interface
        classImplements(TestCaseFunction, IReporter)
        return None


class TwistedVersion(Enum):
    '''
    The Twisted version installed in the environment.

    We have different workarounds in place for different versions of Twisted.
    '''
    Version24 = auto()
    Version25 = auto()
    NotInstalled = auto()


def _get_twisted_version():
    if 'twisted.trial.unittest' not in sys.modules:
        return TwistedVersion.NotInstalled
    import importlib.metadata as importlib
    import packaging.version as packaging
    version_str = importlib.metadata.version('twisted')
    version = packaging.version.parse(version_str)
    if version.major <= 24:
        return TwistedVersion.Version24
    return None.Version25

TWISTED_RAW_EXCINFO_ATTR = '_twisted_raw_excinfo'
pytest_runtest_protocol = (lambda item = None: pass# WARNING: Decompyle incomplete
)()

def _handle_twisted_exc_info(rawexcinfo = None):
    '''
    Twisted passes a custom Failure instance to `addError()` instead of using `sys.exc_info()`.
    Therefore, if `rawexcinfo` is a `Failure` instance, convert it into the equivalent `sys.exc_info()` tuple
    as expected by pytest.
    '''
    twisted_version = _get_twisted_version()
    if twisted_version is TwistedVersion.NotInstalled:
        return rawexcinfo
    if None is TwistedVersion.Version24:
        if hasattr(rawexcinfo, TWISTED_RAW_EXCINFO_ATTR):
            saved_exc_info = getattr(rawexcinfo, TWISTED_RAW_EXCINFO_ATTR)
            delattr(rawexcinfo, TWISTED_RAW_EXCINFO_ATTR)
            return saved_exc_info
        return None
# WARNING: Decompyle incomplete
