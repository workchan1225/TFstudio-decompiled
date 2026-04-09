# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: subtests.pyc (Python 3.11)

'''Builtin plugin that adds subtests support.'''
from __future__ import annotations
from collections import defaultdict
from collections.abc import Callable
from collections.abc import Iterator
from collections.abc import Mapping
from contextlib import AbstractContextManager
from contextlib import contextmanager
from contextlib import ExitStack
from contextlib import nullcontext
import dataclasses
import time
from types import TracebackType
from typing import Any
from typing import TYPE_CHECKING
import pluggy
from _pytest._code import ExceptionInfo
from _pytest._io.saferepr import saferepr
from _pytest.capture import CaptureFixture
from _pytest.capture import FDCapture
from _pytest.capture import SysCapture
from _pytest.config import Config
from _pytest.config import hookimpl
from _pytest.config.argparsing import Parser
from _pytest.deprecated import check_ispytest
from _pytest.fixtures import fixture
from _pytest.fixtures import SubRequest
from _pytest.logging import catching_logs
from _pytest.logging import LogCaptureHandler
from _pytest.logging import LoggingPlugin
from _pytest.reports import TestReport
from _pytest.runner import CallInfo
from _pytest.runner import check_interactive_exception
from _pytest.runner import get_reraise_exceptions
from _pytest.stash import StashKey
if TYPE_CHECKING:
    from typing_extensions import Self

def pytest_addoption(parser = None):
    Config._add_verbosity_ini(parser, Config.VERBOSITY_SUBTESTS, help = 'Specify verbosity level for subtests. Higher levels will generate output for passed subtests. Failed subtests are always reported.')

SubtestContext = <NODE:12>()
SubtestReport = <NODE:12>()
subtests = (lambda request = dataclasses.dataclass(frozen = True, slots = True, kw_only = True): capmam = request.node.config.pluginmanager.get_plugin('capturemanager')# WARNING: Decompyle incomplete
)()

class Subtests:
    '''Subtests fixture, enables declaring subtests inside test functions via the :meth:`test` method.'''
    
    def __init__(self = None, ihook = None, suspend_capture_ctx = None, request = None, *, _ispytest):
        check_ispytest(_ispytest)
        self._ihook = ihook
        self._suspend_capture_ctx = suspend_capture_ctx
        self._request = request

    
    def test(self = None, msg = None, **kwargs):
        '''
        Context manager for subtests, capturing exceptions raised inside the subtest scope and
        reporting assertion failures and errors individually.

        Usage
        -----

        .. code-block:: python

            def test(subtests):
                for i in range(5):
                    with subtests.test("custom message", i=i):
                        assert i % 2 == 0

        :param msg:
            If given, the message will be shown in the test report in case of subtest failure.

        :param kwargs:
            Arbitrary values that are also added to the subtest report.
        '''
        return _SubTestContextManager(self._ihook, msg, kwargs, request = self._request, suspend_capture_ctx = self._suspend_capture_ctx, config = self._request.config)


_SubTestContextManager = <NODE:12>()
capturing_output = (lambda request = None: pass# WARNING: Decompyle incomplete
)()
capturing_logs = (lambda request = None: pass# WARNING: Decompyle incomplete
)()
Captured = <NODE:12>()
CapturedLogs = <NODE:12>()

def pytest_report_to_serializable(report = None):
    if isinstance(report, SubtestReport):
        return report._to_json()


def pytest_report_from_serializable(data = None):
    if data.get('_report_type') == 'SubTestReport':
        return SubtestReport._from_json(data)

failed_subtests_key = StashKey[defaultdict[(str, int)]]()

def pytest_configure(config = None):
    config.stash[failed_subtests_key] = defaultdict((lambda : 0))

pytest_report_teststatus = (lambda report = None, config = None: if report.when != 'call':
Nonequiet = None.get_verbosity(Config.VERBOSITY_SUBTESTS) == 0if isinstance(report, SubtestReport):
outcome = report.outcomedescription = report._sub_test_description()if hasattr(report, 'wasxfail'):
if quiet:
('', '', '')if None == 'skipped':
category = 'xfailed'short = 'y'status = 'SUBXFAIL'else:
None(None, short, f'''{status}{description}''')if None.failed:
(outcome, 'u', f'''SUBFAILED{description}''')if None.passed:
if quiet:
('', '', '')(f'''{outcome}''', 'u', f'''SUBPASSED{description}''')if None.skipped:
if quiet:
('', '', '')(None, '-', f'''SUBSKIPPED{description}''')failed_subtests_count = config.stash[failed_subtests_key][report.nodeid]if report.passed and failed_subtests_count > 0:
report.outcome = 'failed'suffix = 's' if failed_subtests_count > 1 else ''report.longrepr = f'''contains {failed_subtests_count} failed subtest{suffix}''')()
