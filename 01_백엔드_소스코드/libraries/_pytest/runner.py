# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: runner.pyc (Python 3.11)

'''Basic collect and runtest protocol implementations.'''
from __future__ import annotations
import bdb
from collections.abc import Callable
import dataclasses
import os
import sys
import types
from typing import cast
from typing import final
from typing import Generic
from typing import Literal
from typing import TYPE_CHECKING
from typing import TypeVar
from config import Config
from reports import BaseReport
from reports import CollectErrorRepr
from reports import CollectReport
from reports import TestReport
from _pytest import timing
from _pytest._code.code import ExceptionChainRepr
from _pytest._code.code import ExceptionInfo
from _pytest._code.code import TerminalRepr
from _pytest.config.argparsing import Parser
from _pytest.deprecated import check_ispytest
from _pytest.nodes import Collector
from _pytest.nodes import Directory
from _pytest.nodes import Item
from _pytest.nodes import Node
from _pytest.outcomes import Exit
from _pytest.outcomes import OutcomeException
from _pytest.outcomes import Skipped
from _pytest.outcomes import TEST_OUTCOME
if sys.version_info < (3, 11):
    from exceptiongroup import BaseExceptionGroup
if TYPE_CHECKING:
    from _pytest.main import Session
    from _pytest.terminal import TerminalReporter

def pytest_addoption(parser = None):
    group = parser.getgroup('terminal reporting', 'Reporting', after = 'general')
    group.addoption('--durations', action = 'store', type = int, default = None, metavar = 'N', help = 'Show N slowest setup/test durations (N=0 for all)')
    group.addoption('--durations-min', action = 'store', type = float, default = None, metavar = 'N', help = 'Minimal duration in seconds for inclusion in slowest list. Default: 0.005 (or 0.0 if -vv is given).')


def pytest_terminal_summary(terminalreporter = None):
    durations = terminalreporter.config.option.durations
    durations_min = terminalreporter.config.option.durations_min
    verbose = terminalreporter.config.get_verbosity()
# WARNING: Decompyle incomplete


def pytest_sessionstart(session = None):
    session._setupstate = SetupState()


def pytest_sessionfinish(session = None):
    session._setupstate.teardown_exact(None)


def pytest_runtest_protocol(item = None, nextitem = None):
    ihook = item.ihook
    ihook.pytest_runtest_logstart(nodeid = item.nodeid, location = item.location)
    runtestprotocol(item, nextitem = nextitem)
    ihook.pytest_runtest_logfinish(nodeid = item.nodeid, location = item.location)
    return True


def runtestprotocol(item = None, log = None, nextitem = None):
    hasrequest = hasattr(item, '_request')
    if not hasrequest and item._request:
        item._initrequest()
    rep = call_and_report(item, 'setup', log)
    reports = [
        rep]
    if rep.passed:
        if item.config.getoption('setupshow', False):
            show_test_item(item)
        if not item.config.getoption('setuponly', False):
            reports.append(call_and_report(item, 'call', log))
    if item.session.shouldfail or item.session.shouldstop:
        nextitem = None
    reports.append(call_and_report(item, 'teardown', log, nextitem = nextitem))
    if hasrequest:
        item._request = False
        item.funcargs = None
    return reports


def show_test_item(item = None):
    '''Show test function, parameters and the fixtures of the test item.'''
    tw = item.config.get_terminal_writer()
    tw.line()
    tw.write('        ')
    tw.write(item.nodeid)
    used_fixtures = sorted(getattr(item, 'fixturenames', []))
    if used_fixtures:
        tw.write(' (fixtures used: {})'.format(', '.join(used_fixtures)))
    tw.flush()


def pytest_runtest_setup(item = None):
    _update_current_test_var(item, 'setup')
    item.session._setupstate.setup(item)


def pytest_runtest_call(item = None):
    _update_current_test_var(item, 'call')
# WARNING: Decompyle incomplete


def pytest_runtest_teardown(item = None, nextitem = None):
    _update_current_test_var(item, 'teardown')
    item.session._setupstate.teardown_exact(nextitem)
    _update_current_test_var(item, None)


def _update_current_test_var(item = None, when = None):
    '''Update :envvar:`PYTEST_CURRENT_TEST` to reflect the current item and stage.

    If ``when`` is None, delete ``PYTEST_CURRENT_TEST`` from the environment.
    '''
    var_name = 'PYTEST_CURRENT_TEST'
    if when:
        value = f'''{item.nodeid} ({when})'''
        value = value.replace('\x00', '(null)')
        os.environ[var_name] = value
        return None
    None.environ.pop(var_name)


def pytest_report_teststatus(report = None):
    if report.when in ('setup', 'teardown'):
        if report.failed:
            return ('error', 'E', 'ERROR')
        if None.skipped:
            return ('skipped', 's', 'SKIPPED')
        return None


def call_and_report(item = None, when = None, log = None, **kwds):
    pass
# WARNING: Decompyle incomplete


def get_reraise_exceptions(config = None):
    '''Return exception types that should not be suppressed in general.'''
    reraise = (Exit,)
    if not config.getoption('usepdb', False):
        reraise += (KeyboardInterrupt,)
    return reraise


def check_interactive_exception(call = None, report = None):
    '''Check whether the call raised an exception that should be reported as
    interactive.'''
    pass
# WARNING: Decompyle incomplete

TResult = TypeVar('TResult', covariant = True)

def CallInfo():
    '''CallInfo'''
    when: "Literal['collect', 'setup', 'call', 'teardown']" = 'Result/Exception info of a function invocation.'
    
    def __init__(self, result = None, excinfo = None, start = None, stop = None, duration = {
        '_ispytest': False }, when = ('result', 'TResult | None', 'excinfo', 'ExceptionInfo[BaseException] | None', 'start', 'float', 'stop', 'float', 'duration', 'float', 'when', "Literal['collect', 'setup', 'call', 'teardown']", '_ispytest', 'bool', 'return', 'None'), *, _ispytest):
        check_ispytest(_ispytest)
        self._result = result
        self.excinfo = excinfo
        self.start = start
        self.stop = stop
        self.duration = duration
        self.when = when

    result = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    from_call = (lambda cls = None, func = None, when = classmethod, reraise = (None,): excinfo = Noneinstant = timing.Instant()# WARNING: Decompyle incomplete
)()
    
    def __repr__(self = None):
        pass
    # WARNING: Decompyle incomplete


CallInfo = <NODE:27>(CallInfo, 'CallInfo', Generic[TResult])()()

def pytest_runtest_makereport(item = None, call = final):
    return TestReport.from_item_and_call(item, call)


def pytest_make_collect_report(collector = None):
    pass
# WARNING: Decompyle incomplete


class SetupState:
    '''Shared state for setting up/tearing down test items or collectors
    in a session.

    Suppose we have a collection tree as follows:

    <Session session>
        <Module mod1>
            <Function item1>
        <Module mod2>
            <Function item2>

    The SetupState maintains a stack. The stack starts out empty:

        []

    During the setup phase of item1, setup(item1) is called. What it does
    is:

        push session to stack, run session.setup()
        push mod1 to stack, run mod1.setup()
        push item1 to stack, run item1.setup()

    The stack is:

        [session, mod1, item1]

    While the stack is in this shape, it is allowed to add finalizers to
    each of session, mod1, item1 using addfinalizer().

    During the teardown phase of item1, teardown_exact(item2) is called,
    where item2 is the next item to item1. What it does is:

        pop item1 from stack, run its teardowns
        pop mod1 from stack, run its teardowns

    mod1 was popped because it ended its purpose with item1. The stack is:

        [session]

    During the setup phase of item2, setup(item2) is called. What it does
    is:

        push mod2 to stack, run mod2.setup()
        push item2 to stack, run item2.setup()

    Stack:

        [session, mod2, item2]

    During the teardown phase of item2, teardown_exact(None) is called,
    because item2 is the last item. What it does is:

        pop item2 from stack, run its teardowns
        pop mod2 from stack, run its teardowns
        pop session from stack, run its teardowns

    Stack:

        []

    The end!
    '''
    
    def __init__(self = None):
        self.stack = { }

    
    def setup(self = None, item = None):
        '''Setup objects along the collector chain to the item.'''
        needed_collectors = item.listchain()
    # WARNING: Decompyle incomplete

    
    def addfinalizer(self = None, finalizer = None, node = None):
        '''Attach a finalizer to the given node.

        The node must be currently active in the stack.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def teardown_exact(self = None, nextitem = None):
        """Teardown the current stack up until reaching nodes that nextitem
        also descends from.

        When nextitem is None (meaning we're at the last item), the entire
        stack is torn down.
        """
        pass
    # WARNING: Decompyle incomplete



def collect_one_node(collector = None):
    ihook = collector.ihook
    ihook.pytest_collectstart(collector = collector)
    rep = ihook.pytest_make_collect_report(collector = collector)
    call = rep.__dict__.pop('call', None)
    if call and check_interactive_exception(call, rep):
        ihook.pytest_exception_interact(node = collector, call = call, report = rep)
    return rep
