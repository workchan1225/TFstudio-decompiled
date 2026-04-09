# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hookspec.pyc (Python 3.11)

'''Hook specifications for pytest plugins which are invoked by pytest itself
and by builtin plugins.'''
from __future__ import annotations
from collections.abc import Mapping
from collections.abc import Sequence
from pathlib import Path
from typing import Any
from typing import TYPE_CHECKING
from pluggy import HookspecMarker
from deprecated import HOOK_LEGACY_PATH_ARG
if TYPE_CHECKING:
    import pdb
    from typing import Literal
    import warnings
    from _pytest._code.code import ExceptionInfo
    from _pytest._code.code import ExceptionRepr
    from _pytest.compat import LEGACY_PATH
    from _pytest.config import _PluggyPlugin
    from _pytest.config import Config
    from _pytest.config import ExitCode
    from _pytest.config import PytestPluginManager
    from _pytest.config.argparsing import Parser
    from _pytest.fixtures import FixtureDef
    from _pytest.fixtures import SubRequest
    from _pytest.main import Session
    from _pytest.nodes import Collector
    from _pytest.nodes import Item
    from _pytest.outcomes import Exit
    from _pytest.python import Class
    from _pytest.python import Function
    from _pytest.python import Metafunc
    from _pytest.python import Module
    from _pytest.reports import CollectReport
    from _pytest.reports import TestReport
    from _pytest.runner import CallInfo
    from _pytest.terminal import TerminalReporter
    from _pytest.terminal import TestShortLogReport
hookspec = HookspecMarker('pytest')
pytest_addhooks = (lambda pluginmanager = None: pass)()
pytest_plugin_registered = (lambda plugin = None, plugin_name = None, manager = hookspec(historic = True): pass)()
pytest_addoption = (lambda parser = None, pluginmanager = None: pass)()
pytest_configure = (lambda config = None: pass)()
pytest_cmdline_parse = (lambda pluginmanager = None, args = None: pass)()

def pytest_load_initial_conftests(early_config = None, parser = None, args = None):
    '''Called to implement the loading of :ref:`initial conftest files
    <pluginorder>` ahead of command line option parsing.

    :param early_config: The pytest config object.
    :param args: Arguments passed on the command line.
    :param parser: To add command line options.

    Use in conftest plugins
    =======================

    This hook is not called for conftest files.
    '''
    pass

pytest_cmdline_main = (lambda config = None: pass)()
pytest_collection = (lambda session = None: pass)()

def pytest_collection_modifyitems(session = None, config = None, items = None):
    '''Called after collection has been performed. May filter or re-order
    the items in-place.

    When items are deselected (filtered out from ``items``),
    the hook :hook:`pytest_deselected` must be called explicitly
    with the deselected items to properly notify other plugins,
    e.g. with ``config.hook.pytest_deselected(items=deselected_items)``.

    :param session: The pytest session object.
    :param config: The pytest config object.
    :param items: List of item objects.

    Use in conftest plugins
    =======================

    Any conftest plugin can implement this hook.
    '''
    pass


def pytest_collection_finish(session = None):
    '''Called after collection has been performed and modified.

    :param session: The pytest session object.

    Use in conftest plugins
    =======================

    Any conftest plugin can implement this hook.
    '''
    pass

pytest_ignore_collect = (lambda collection_path = None, path = None, config = hookspec(firstresult = True, warn_on_impl_args = {
    'path': HOOK_LEGACY_PATH_ARG.format(pylib_path_arg = 'path', pathlib_path_arg = 'collection_path') }): pass)()
pytest_collect_directory = (lambda path = None, parent = None: pass)()
pytest_collect_file = (lambda file_path = None, path = None, parent = hookspec(warn_on_impl_args = {
    'path': HOOK_LEGACY_PATH_ARG.format(pylib_path_arg = 'path', pathlib_path_arg = 'file_path') }): pass)()

def pytest_collectstart(collector = None):
    """Collector starts collecting.

    :param collector:
        The collector.

    Use in conftest plugins
    =======================

    Any conftest file can implement this hook. For a given collector, only
    conftest files in the collector's directory and its parent directories are
    consulted.
    """
    pass


def pytest_itemcollected(item = None):
    """We just collected a test item.

    :param item:
        The item.

    Use in conftest plugins
    =======================

    Any conftest file can implement this hook. For a given item, only conftest
    files in the item's directory and its parent directories are consulted.
    """
    pass


def pytest_collectreport(report = None):
    """Collector finished collecting.

    :param report:
        The collect report.

    Use in conftest plugins
    =======================

    Any conftest file can implement this hook. For a given collector, only
    conftest files in the collector's directory and its parent directories are
    consulted.
    """
    pass


def pytest_deselected(items = None):
    '''Called for deselected test items, e.g. by keyword.

    Note that this hook has two integration aspects for plugins:

    - it can be *implemented* to be notified of deselected items
    - it must be *called* from :hook:`pytest_collection_modifyitems`
      implementations when items are deselected (to properly notify other plugins).

    May be called multiple times.

    :param items:
        The items.

    Use in conftest plugins
    =======================

    Any conftest file can implement this hook.
    '''
    pass

pytest_make_collect_report = (lambda collector = None: pass)()
pytest_pycollect_makemodule = (lambda module_path = None, path = None, parent = hookspec(firstresult = True, warn_on_impl_args = {
    'path': HOOK_LEGACY_PATH_ARG.format(pylib_path_arg = 'path', pathlib_path_arg = 'module_path') }): pass)()
pytest_pycollect_makeitem = (lambda collector = None, name = None, obj = hookspec(firstresult = True): pass)()
pytest_pyfunc_call = (lambda pyfuncitem = None: pass)()

def pytest_generate_tests(metafunc = None):
    """Generate (multiple) parametrized calls to a test function.

    :param metafunc:
        The :class:`~pytest.Metafunc` helper for the test function.

    Use in conftest plugins
    =======================

    Any conftest file can implement this hook. For a given function definition,
    only conftest files in the functions's directory and its parent directories
    are consulted.
    """
    pass

pytest_make_parametrize_id = (lambda config = None, val = None, argname = hookspec(firstresult = True): pass)()
pytest_runtestloop = (lambda session = None: pass)()
pytest_runtest_protocol = (lambda item = None, nextitem = None: pass)()

def pytest_runtest_logstart(nodeid = None, location = None):
    """Called at the start of running the runtest protocol for a single item.

    See :hook:`pytest_runtest_protocol` for a description of the runtest protocol.

    :param nodeid: Full node ID of the item.
    :param location: A tuple of ``(filename, lineno, testname)``
        where ``filename`` is a file path relative to ``config.rootpath``
        and ``lineno`` is 0-based.

    Use in conftest plugins
    =======================

    Any conftest file can implement this hook. For a given item, only conftest
    files in the item's directory and its parent directories are consulted.
    """
    pass


def pytest_runtest_logfinish(nodeid = None, location = None):
    """Called at the end of running the runtest protocol for a single item.

    See :hook:`pytest_runtest_protocol` for a description of the runtest protocol.

    :param nodeid: Full node ID of the item.
    :param location: A tuple of ``(filename, lineno, testname)``
        where ``filename`` is a file path relative to ``config.rootpath``
        and ``lineno`` is 0-based.

    Use in conftest plugins
    =======================

    Any conftest file can implement this hook. For a given item, only conftest
    files in the item's directory and its parent directories are consulted.
    """
    pass


def pytest_runtest_setup(item = None):
    """Called to perform the setup phase for a test item.

    The default implementation runs ``setup()`` on ``item`` and all of its
    parents (which haven't been setup yet). This includes obtaining the
    values of fixtures required by the item (which haven't been obtained
    yet).

    :param item:
        The item.

    Use in conftest plugins
    =======================

    Any conftest file can implement this hook. For a given item, only conftest
    files in the item's directory and its parent directories are consulted.
    """
    pass


def pytest_runtest_call(item = None):
    """Called to run the test for test item (the call phase).

    The default implementation calls ``item.runtest()``.

    :param item:
        The item.

    Use in conftest plugins
    =======================

    Any conftest file can implement this hook. For a given item, only conftest
    files in the item's directory and its parent directories are consulted.
    """
    pass


def pytest_runtest_teardown(item = None, nextitem = None):
    """Called to perform the teardown phase for a test item.

    The default implementation runs the finalizers and calls ``teardown()``
    on ``item`` and all of its parents (which need to be torn down). This
    includes running the teardown phase of fixtures required by the item (if
    they go out of scope).

    :param item:
        The item.
    :param nextitem:
        The scheduled-to-be-next test item (None if no further test item is
        scheduled). This argument is used to perform exact teardowns, i.e.
        calling just enough finalizers so that nextitem only needs to call
        setup functions.

    Use in conftest plugins
    =======================

    Any conftest file can implement this hook. For a given item, only conftest
    files in the item's directory and its parent directories are consulted.
    """
    pass

pytest_runtest_makereport = (lambda item = None, call = None: pass)()

def pytest_runtest_logreport(report = None):
    """Process the :class:`~pytest.TestReport` produced for each
    of the setup, call and teardown runtest phases of an item.

    See :hook:`pytest_runtest_protocol` for a description of the runtest protocol.

    Use in conftest plugins
    =======================

    Any conftest file can implement this hook. For a given item, only conftest
    files in the item's directory and its parent directories are consulted.
    """
    pass

pytest_report_to_serializable = (lambda config = None, report = None: pass)()
pytest_report_from_serializable = (lambda config = None, data = None: pass)()
pytest_fixture_setup = (lambda fixturedef = None, request = None: pass)()

def pytest_fixture_post_finalizer(fixturedef = None, request = None):
    """Called after fixture teardown, but before the cache is cleared, so
    the fixture result ``fixturedef.cached_result`` is still available (not
    ``None``).

    :param fixturedef:
        The fixture definition object.
    :param request:
        The fixture request object.

    Use in conftest plugins
    =======================

    Any conftest file can implement this hook. For a given fixture, only
    conftest files in the fixture scope's directory and its parent directories
    are consulted.
    """
    pass


def pytest_sessionstart(session = None):
    '''Called after the ``Session`` object has been created and before performing collection
    and entering the run test loop.

    :param session: The pytest session object.

    Use in conftest plugins
    =======================

    This hook is only called for :ref:`initial conftests <pluginorder>`.
    '''
    pass


def pytest_sessionfinish(session = None, exitstatus = None):
    '''Called after whole test run finished, right before returning the exit status to the system.

    :param session: The pytest session object.
    :param exitstatus: The status which pytest will return to the system.

    Use in conftest plugins
    =======================

    Any conftest file can implement this hook.
    '''
    pass


def pytest_unconfigure(config = None):
    '''Called before test process is exited.

    :param config: The pytest config object.

    Use in conftest plugins
    =======================

    Any conftest file can implement this hook.
    '''
    pass


def pytest_assertrepr_compare(config = None, op = None, left = None, right = ('config', 'Config', 'op', 'str', 'left', 'object', 'right', 'object', 'return', 'list[str] | None')):
    '''Return explanation for comparisons in failing assert expressions.

    Return None for no custom explanation, otherwise return a list
    of strings. The strings will be joined by newlines but any newlines
    *in* a string will be escaped. Note that all but the first line will
    be indented slightly, the intention is for the first line to be a summary.

    :param config: The pytest config object.
    :param op: The operator, e.g. `"=="`, `"!="`, `"not in"`.
    :param left: The left operand.
    :param right: The right operand.

    Use in conftest plugins
    =======================

    Any conftest file can implement this hook. For a given item, only conftest
    files in the item\'s directory and its parent directories are consulted.
    '''
    pass


def pytest_assertion_pass(item = None, lineno = None, orig = None, expl = ('item', 'Item', 'lineno', 'int', 'orig', 'str', 'expl', 'str', 'return', 'None')):
    """Called whenever an assertion passes.

    .. versionadded:: 5.0

    Use this hook to do some processing after a passing assertion.
    The original assertion information is available in the `orig` string
    and the pytest introspected assertion information is available in the
    `expl` string.

    This hook must be explicitly enabled by the :confval:`enable_assertion_pass_hook`
    configuration option:

    .. tab:: toml

        .. code-block:: toml

            [pytest]
            enable_assertion_pass_hook = true

    .. tab:: ini

        .. code-block:: ini

            [pytest]
            enable_assertion_pass_hook = true

    You need to **clean the .pyc** files in your project directory and interpreter libraries
    when enabling this option, as assertions will require to be re-written.

    :param item: pytest item object of current test.
    :param lineno: Line number of the assert statement.
    :param orig: String with the original assertion.
    :param expl: String with the assert explanation.

    Use in conftest plugins
    =======================

    Any conftest file can implement this hook. For a given item, only conftest
    files in the item's directory and its parent directories are consulted.
    """
    pass

pytest_report_header = (lambda config = None, start_path = None, startdir = hookspec(warn_on_impl_args = {
    'startdir': HOOK_LEGACY_PATH_ARG.format(pylib_path_arg = 'startdir', pathlib_path_arg = 'start_path') }): pass)()
pytest_report_collectionfinish = (lambda config = None, start_path = None, startdir = hookspec(warn_on_impl_args = {
    'startdir': HOOK_LEGACY_PATH_ARG.format(pylib_path_arg = 'startdir', pathlib_path_arg = 'start_path') }), items = ('config', 'Config', 'start_path', 'Path', 'startdir', 'LEGACY_PATH', 'items', 'Sequence[Item]', 'return', 'str | list[str]'): pass)()
pytest_report_teststatus = (lambda report = None, config = None: pass)()

def pytest_terminal_summary(terminalreporter = None, exitstatus = None, config = None):
    '''Add a section to terminal summary reporting.

    :param terminalreporter: The internal terminal reporter object.
    :param exitstatus: The exit status that will be reported back to the OS.
    :param config: The pytest config object.

    .. versionadded:: 4.2
        The ``config`` parameter.

    Use in conftest plugins
    =======================

    Any conftest plugin can implement this hook.
    '''
    pass

pytest_warning_recorded = (lambda warning_message = None, when = None, nodeid = hookspec(historic = True), location = ('warning_message', 'warnings.WarningMessage', 'when', "Literal['config', 'collect', 'runtest']", 'nodeid', 'str', 'location', 'tuple[str, int, str] | None', 'return', 'None'): pass)()

def pytest_markeval_namespace(config = None):
    '''Called when constructing the globals dictionary used for
    evaluating string conditions in xfail/skipif markers.

    This is useful when the condition for a marker requires
    objects that are expensive or impossible to obtain during
    collection time, which is required by normal boolean
    conditions.

    .. versionadded:: 6.2

    :param config: The pytest config object.
    :returns: A dictionary of additional globals to add.

    Use in conftest plugins
    =======================

    Any conftest file can implement this hook. For a given item, only conftest
    files in parent directories of the item are consulted.
    '''
    pass


def pytest_internalerror(excrepr = None, excinfo = None):
    '''Called for internal errors.

    Return True to suppress the fallback handling of printing an
    INTERNALERROR message directly to sys.stderr.

    :param excrepr: The exception repr object.
    :param excinfo: The exception info.

    Use in conftest plugins
    =======================

    Any conftest plugin can implement this hook.
    '''
    pass


def pytest_keyboard_interrupt(excinfo = None):
    '''Called for keyboard interrupt.

    :param excinfo: The exception info.

    Use in conftest plugins
    =======================

    Any conftest plugin can implement this hook.
    '''
    pass


def pytest_exception_interact(node = None, call = None, report = None):
    '''Called when an exception was raised which can potentially be
    interactively handled.

    May be called during collection (see :hook:`pytest_make_collect_report`),
    in which case ``report`` is a :class:`~pytest.CollectReport`.

    May be called during runtest of an item (see :hook:`pytest_runtest_protocol`),
    in which case ``report`` is a :class:`~pytest.TestReport`.

    This hook is not called if the exception that was raised is an internal
    exception like ``skip.Exception``.

    :param node:
        The item or collector.
    :param call:
        The call information. Contains the exception.
    :param report:
        The collection or test report.

    Use in conftest plugins
    =======================

    Any conftest file can implement this hook. For a given node, only conftest
    files in parent directories of the node are consulted.
    '''
    pass


def pytest_enter_pdb(config = None, pdb = None):
    '''Called upon pdb.set_trace().

    Can be used by plugins to take special action just before the python
    debugger enters interactive mode.

    :param config: The pytest config object.
    :param pdb: The Pdb instance.

    Use in conftest plugins
    =======================

    Any conftest plugin can implement this hook.
    '''
    pass


def pytest_leave_pdb(config = None, pdb = None):
    '''Called when leaving pdb (e.g. with continue after pdb.set_trace()).

    Can be used by plugins to take special action just after the python
    debugger leaves interactive mode.

    :param config: The pytest config object.
    :param pdb: The Pdb instance.

    Use in conftest plugins
    =======================

    Any conftest plugin can implement this hook.
    '''
    pass
