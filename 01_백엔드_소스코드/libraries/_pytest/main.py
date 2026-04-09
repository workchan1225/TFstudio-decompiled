# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: main.pyc (Python 3.11)

'''Core implementation of the testing process: init, session, runtest loop.'''
from __future__ import annotations
import argparse
from collections.abc import Callable
from collections.abc import Iterable
from collections.abc import Iterator
from collections.abc import Sequence
from collections.abc import Set as AbstractSet
import dataclasses
import fnmatch
import functools
import importlib
import importlib.util as importlib
import os
from pathlib import Path
import sys
from typing import final
from typing import Literal
from typing import overload
from typing import TYPE_CHECKING
import warnings
import pluggy
from _pytest import nodes
import _pytest._code as _pytest
from _pytest.config import Config
from _pytest.config import directory_arg
from _pytest.config import ExitCode
from _pytest.config import hookimpl
from _pytest.config import PytestPluginManager
from _pytest.config import UsageError
from _pytest.config.argparsing import OverrideIniAction
from _pytest.config.argparsing import Parser
from _pytest.config.compat import PathAwareHookProxy
from _pytest.outcomes import exit
from _pytest.pathlib import absolutepath
from _pytest.pathlib import bestrelpath
from _pytest.pathlib import fnmatch_ex
from _pytest.pathlib import safe_exists
from _pytest.pathlib import samefile_nofollow
from _pytest.pathlib import scandir
from _pytest.reports import CollectReport
from _pytest.reports import TestReport
from _pytest.runner import collect_one_node
from _pytest.runner import SetupState
from _pytest.warning_types import PytestWarning
if TYPE_CHECKING:
    from typing_extensions import Self
    from _pytest.fixtures import FixtureManager

def pytest_addoption(parser = None):
    group = parser.getgroup('general')
    group._addoption('-x', '--exitfirst', action = 'store_const', dest = 'maxfail', const = 1, help = 'Exit instantly on first error or failed test')
    group.addoption('--maxfail', metavar = 'num', action = 'store', type = int, dest = 'maxfail', default = 0, help = 'Exit after first num failures or errors')
    group.addoption('--strict-config', action = OverrideIniAction, ini_option = 'strict_config', ini_value = 'true', help = 'Enables the strict_config option')
    group.addoption('--strict-markers', action = OverrideIniAction, ini_option = 'strict_markers', ini_value = 'true', help = 'Enables the strict_markers option')
    group.addoption('--strict', action = OverrideIniAction, ini_option = 'strict', ini_value = 'true', help = 'Enables the strict option')
    parser.addini('strict_config', 'Any warnings encountered while parsing the `pytest` section of the configuration file raise errors', type = 'bool', default = None)
    parser.addini('strict_markers', 'Markers not registered in the `markers` section of the configuration file raise errors', type = 'bool', default = None)
    parser.addini('strict', 'Enables all strictness options, currently: strict_config, strict_markers, strict_xfail, strict_parametrization_ids', type = 'bool', default = False)
    group = parser.getgroup('pytest-warnings')
    group.addoption('-W', '--pythonwarnings', action = 'append', help = 'Set which warnings to report, see -W option of Python itself')
    parser.addini('filterwarnings', type = 'linelist', help = 'Each line specifies a pattern for warnings.filterwarnings. Processed after -W/--pythonwarnings.')
    group = parser.getgroup('collect', 'collection')
    group.addoption('--collectonly', '--collect-only', '--co', action = 'store_true', help = "Only collect tests, don't execute them")
    group.addoption('--pyargs', action = 'store_true', help = 'Try to interpret all arguments as Python packages')
    group.addoption('--ignore', action = 'append', metavar = 'path', help = 'Ignore path during collection (multi-allowed)')
    group.addoption('--ignore-glob', action = 'append', metavar = 'path', help = 'Ignore path pattern during collection (multi-allowed)')
    group.addoption('--deselect', action = 'append', metavar = 'nodeid_prefix', help = 'Deselect item (via node id prefix) during collection (multi-allowed)')
    group.addoption('--confcutdir', dest = 'confcutdir', default = None, metavar = 'dir', type = functools.partial(directory_arg, optname = '--confcutdir'), help = "Only load conftest.py's relative to specified dir")
    group.addoption('--noconftest', action = 'store_true', dest = 'noconftest', default = False, help = "Don't load any conftest.py files")
    group.addoption('--keepduplicates', '--keep-duplicates', action = 'store_true', dest = 'keepduplicates', default = False, help = 'Keep duplicate tests')
    group.addoption('--collect-in-virtualenv', action = 'store_true', dest = 'collect_in_virtualenv', default = False, help = "Don't ignore tests in a local virtualenv directory")
    group.addoption('--continue-on-collection-errors', action = 'store_true', default = False, dest = 'continue_on_collection_errors', help = 'Force test execution even if collection errors occur')
    group.addoption('--import-mode', default = 'prepend', choices = [
        'prepend',
        'append',
        'importlib'], dest = 'importmode', help = 'Prepend/append to sys.path when importing test modules and conftest files. Default: prepend.')
    parser.addini('norecursedirs', 'Directory patterns to avoid for recursion', type = 'args', default = [
        '*.egg',
        '.*',
        '_darcs',
        'build',
        'CVS',
        'dist',
        'node_modules',
        'venv',
        '{arch}'])
    parser.addini('testpaths', 'Directories to search for tests when no files or directories are given on the command line', type = 'args', default = [])
    parser.addini('collect_imported_tests', 'Whether to collect tests in imported modules outside `testpaths`', type = 'bool', default = True)
    parser.addini('consider_namespace_packages', type = 'bool', default = False, help = 'Consider namespace packages when resolving module names during import')
    group = parser.getgroup('debugconfig', 'test session debugging and configuration')
    group._addoption('-c', '--config-file', metavar = 'FILE', type = str, dest = 'inifilename', help = 'Load configuration from `FILE` instead of trying to locate one of the implicit configuration files.')
    group.addoption('--rootdir', action = 'store', dest = 'rootdir', help = "Define root directory for tests. Can be relative path: 'root_dir', './root_dir', 'root_dir/another_dir/'; absolute path: '/home/user/root_dir'; path with variables: '$HOME/root_dir'.")
    group.addoption('--basetemp', dest = 'basetemp', default = None, type = validate_basetemp, metavar = 'dir', help = 'Base temporary directory for this test run. (Warning: this directory is removed if it exists.)')


def validate_basetemp(path = None):
    msg = 'basetemp must not be empty, the current working directory or any parent directory of it'
    if not path:
        raise argparse.ArgumentTypeError(msg)
    
    def is_ancestor(base = None, query = None):
        '''Return whether query is an ancestor of base.'''
        if base == query:
            return True
        return None in base.parents

    if is_ancestor(Path.cwd(), Path(path).absolute()):
        raise argparse.ArgumentTypeError(msg)
    if is_ancestor(Path.cwd().resolve(), Path(path).resolve()):
        raise argparse.ArgumentTypeError(msg)
    return path


def wrap_session(config = None, doit = None):
    '''Skeleton command line program.'''
    session = Session.from_config(config)
    session.exitstatus = ExitCode.OK
    initstate = 0
# WARNING: Decompyle incomplete


def pytest_cmdline_main(config = None):
    return wrap_session(config, _main)


def _main(config = None, session = None):
    '''Default command line protocol for initialization, session,
    running tests and reporting.'''
    config.hook.pytest_collection(session = session)
    config.hook.pytest_runtestloop(session = session)
    if session.testsfailed:
        return ExitCode.TESTS_FAILED
    if None.testscollected == 0:
        return ExitCode.NO_TESTS_COLLECTED


def pytest_collection(session = None):
    session.perform_collect()


def pytest_runtestloop(session = None):
    if not session.testsfailed and session.config.option.continue_on_collection_errors:
        raise session.Interrupted(f'''{session.testsfailed} error{'s' if session.testsfailed != 1 else ''} during collection''')
    if session.config.option.collectonly:
        return True
    for i, item in None(session.items):
        nextitem = session.items[i + 1] if i + 1 < len(session.items) else None
        item.config.hook.pytest_runtest_protocol(item = item, nextitem = nextitem)
        if session.shouldfail:
            raise session.Failed(session.shouldfail)
        if session.shouldstop:
            raise session.Interrupted(session.shouldstop)
        return True


def _in_venv(path = None):
    '''Attempt to detect if ``path`` is the root of a Virtual Environment by
    checking for the existence of the pyvenv.cfg file.

    [https://peps.python.org/pep-0405/]

    For regression protection we also check for conda environments that do not include pyenv.cfg yet --
    https://github.com/conda/conda/issues/13337 is the conda issue tracking adding pyenv.cfg.

    Checking for the `conda-meta/history` file per https://github.com/pytest-dev/pytest/issues/12652#issuecomment-2246336902.

    '''
    
    try:
        if not path.joinpath('pyvenv.cfg').is_file():
            return path.joinpath('conda-meta', 'history').is_file()
        except OSError:
            return False



def pytest_ignore_collect(collection_path = None, config = None):
    pass
# WARNING: Decompyle incomplete


def pytest_collect_directory(path = None, parent = None):
    return Dir.from_parent(parent, path = path)


def pytest_collection_modifyitems(items = None, config = None):
    if not config.getoption('deselect'):
        deselect_prefixes = tuple([])
        if not deselect_prefixes:
            return None
        remaining = None
        deselected = []
        for colitem in items:
            if colitem.nodeid.startswith(deselect_prefixes):
                deselected.append(colitem)
                continue
            remaining.append(colitem)
            if deselected:
                config.hook.pytest_deselected(items = deselected)
                items[:] = remaining
                return None
            return None


class FSHookProxy:
    
    def __init__(self = None, pm = None, remove_mods = None):
        self.pm = pm
        self.remove_mods = remove_mods

    
    def __getattr__(self = None, name = None):
        x = self.pm.subset_hook_caller(name, remove_plugins = self.remove_mods)
        self.__dict__[name] = x
        return x



class Interrupted(KeyboardInterrupt):
    '''Signals that the test run was interrupted.'''
    __module__ = 'builtins'


class Failed(Exception):
    '''Signals a stop as failed test run.'''
    pass


def _bestrelpath_cache():
    '''_bestrelpath_cache'''
    path: 'Path' = ('path',)
    
    def __missing__(self = None, path = None):
        r = bestrelpath(self.path, path)
        self[path] = r
        return r


_bestrelpath_cache = <NODE:27>(_bestrelpath_cache, '_bestrelpath_cache', dict[(Path, str)])()
Dir = <NODE:12>()
Session = <NODE:12>()

def search_pypath(module_name = None, *, consider_namespace_packages):
    '''Search sys.path for the given a dotted module name, and return its file
    system path if found.'''
    
    try:
        spec = importlib.util.find_spec(module_name)
    except (AttributeError, ImportError, ValueError):
        return None

# WARNING: Decompyle incomplete

CollectionArgument = <NODE:12>()

def resolve_collection_argument(invocation_path = None, arg = None, arg_index = None, *, as_pypath, consider_namespace_packages):
    '''Parse path arguments optionally containing selection parts and return (fspath, names).

    Command-line arguments can point to files and/or directories, and optionally contain
    parts for specific tests selection, for example:

        "pkg/tests/test_foo.py::TestClass::test_foo"

    This function ensures the path exists, and returns a resolved `CollectionArgument`:

        CollectionArgument(
            path=Path("/full/path/to/pkg/tests/test_foo.py"),
            parts=["TestClass", "test_foo"],
            module_name=None,
        )

    When as_pypath is True, expects that the command-line argument actually contains
    module paths instead of file-system paths:

        "pkg.tests.test_foo::TestClass::test_foo[a,b]"

    In which case we search sys.path for a matching module, and then return the *path* to the
    found module, which may look like this:

        CollectionArgument(
            path=Path("/home/u/myvenv/lib/site-packages/pkg/tests/test_foo.py"),
            parts=["TestClass", "test_foo"],
            parametrization="[a,b]",
            module_name="pkg.tests.test_foo",
        )

    If the path doesn\'t exist, raise UsageError.
    If the path is a directory and selection parts are present, raise UsageError.
    '''
    (base, squacket, rest) = arg.partition('[')
# WARNING: Decompyle incomplete


def is_collection_argument_subsumed_by(arg = None, by = None):
    '''Check if `arg` is subsumed (contained) by `by`.'''
    if by.path != arg.path:
        if not by.parts:
            return arg.path.is_relative_to(by.path)
        return None
    if None(by.parts) > len(arg.parts) or arg.parts[:len(by.parts)] != by.parts:
        return False
# WARNING: Decompyle incomplete


def normalize_collection_arguments(collection_args = None):
    '''Normalize collection arguments to eliminate overlapping paths and parts.

    Detects when collection arguments overlap in either paths or parts and only
    keeps the shorter prefix, or the earliest argument if duplicate, preserving
    order. The result is prefix-free.
    '''
    collection_args_sorted = sorted(collection_args, key = (lambda arg:
