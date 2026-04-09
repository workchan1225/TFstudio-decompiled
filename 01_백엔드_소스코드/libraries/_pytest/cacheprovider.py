# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cacheprovider.pyc (Python 3.11)

'''Implementation of the cache provider.'''
from __future__ import annotations
from collections.abc import Generator
from collections.abc import Iterable
import dataclasses
import errno
import json
import os
from pathlib import Path
import tempfile
from typing import final
from pathlib import resolve_from_str
from pathlib import rm_rf
from reports import CollectReport
from _pytest import nodes
from _pytest._io import TerminalWriter
from _pytest.config import Config
from _pytest.config import ExitCode
from _pytest.config import hookimpl
from _pytest.config.argparsing import Parser
from _pytest.deprecated import check_ispytest
from _pytest.fixtures import fixture
from _pytest.fixtures import FixtureRequest
from _pytest.main import Session
from _pytest.nodes import Directory
from _pytest.nodes import File
from _pytest.reports import TestReport
README_CONTENT = "# pytest cache directory #\n\nThis directory contains data from the pytest's cache plugin,\nwhich provides the `--lf` and `--ff` options, as well as the `cache` fixture.\n\n**Do not** commit this to version control.\n\nSee [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.\n"
CACHEDIR_TAG_CONTENT = b'Signature: 8a477f597d28d172789f06886806bc55\n# This file is a cache directory tag created by pytest.\n# For information about cache directory tags, see:\n#\thttps://bford.info/cachedir/spec.html\n'
Cache = <NODE:12>()()

class LFPluginCollWrapper:
    
    def __init__(self = None, lfplugin = None):
        self.lfplugin = lfplugin
        self._collected_at_least_one_failure = False

    pytest_make_collect_report = (lambda self = None, collector = None: pass# WARNING: Decompyle incomplete
)()


class LFPluginCollSkipfiles:
    
    def __init__(self = None, lfplugin = None):
        self.lfplugin = lfplugin

    pytest_make_collect_report = (lambda self = None, collector = None: if isinstance(collector, File) and collector.path not in self.lfplugin._last_failed_paths:
CollectReport(collector.nodeid, 'passed', longrepr = None, result = []))()


class LFPlugin:
    '''Plugin which implements the --lf (run last-failing) option.'''
    
    def __init__(self = None, config = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_last_failed_paths(self = None):
        '''Return a set with all Paths of the previously failed nodeids and
        their parents.'''
        rootpath = self.config.rootpath
        result = set()
        for nodeid in self.lastfailed:
            path = rootpath / nodeid.split('::')[0]
            result.add(path)
            result.update(path.parents)
            return result()

    
    def pytest_report_collectionfinish(self = None):
        if self.active and self.config.get_verbosity() >= 0:
            return f'''run-last-failure: {self._report_status}'''

    
    def pytest_runtest_logreport(self = None, report = None):
        if report.when == 'call' or report.passed or report.skipped:
            self.lastfailed.pop(report.nodeid, None)
            return None
        if None.failed:
            self.lastfailed[report.nodeid] = True
            return None

    
    def pytest_collectreport(self = None, report = None):
        passed = report.outcome in ('passed', 'skipped')
        if passed:
            if report.nodeid in self.lastfailed:
                self.lastfailed.pop(report.nodeid)
                (lambda .0: pass# WARNING: Decompyle incomplete
)(report.result())
                return None
            return None
        self.lastfailed[report.nodeid] = None

    pytest_collection_modifyitems = (lambda self = None, config = None, items = hookimpl(wrapper = True, tryfirst = True): pass# WARNING: Decompyle incomplete
)()
    
    def pytest_sessionfinish(self = None, session = None):
        config = self.config
        if config.getoption('cacheshow') or hasattr(config, 'workerinput'):
            return None
    # WARNING: Decompyle incomplete



class NFPlugin:
    '''Plugin which implements the --nf (run new-first) option.'''
    
    def __init__(self = None, config = None):
        self.config = config
        self.active = config.option.newfirst
    # WARNING: Decompyle incomplete

    pytest_collection_modifyitems = (lambda self = None, items = None: pass# WARNING: Decompyle incomplete
)()
    
    def _get_increasing_order(self = None, items = None):
        return sorted(items, key = (lambda item: item.path.stat().st_mtime), reverse = True)

    
    def pytest_sessionfinish(self = None):
        config = self.config
        if config.getoption('cacheshow') or hasattr(config, 'workerinput'):
            return None
        if None.getoption('collectonly'):
            return None
    # WARNING: Decompyle incomplete



def pytest_addoption(parser = None):
    '''Add command-line options for cache functionality.

    :param parser: Parser object to add command-line options to.
    '''
    group = parser.getgroup('general')
    group.addoption('--lf', '--last-failed', action = 'store_true', dest = 'lf', help = 'Rerun only the tests that failed at the last run (or all if none failed)')
    group.addoption('--ff', '--failed-first', action = 'store_true', dest = 'failedfirst', help = 'Run all tests, but run the last failures first. This may re-order tests and thus lead to repeated fixture setup/teardown.')
    group.addoption('--nf', '--new-first', action = 'store_true', dest = 'newfirst', help = 'Run tests from new files first, then the rest of the tests sorted by file mtime')
    group.addoption('--cache-show', action = 'append', nargs = '?', dest = 'cacheshow', help = "Show cache contents, don't perform collection or tests. Optional argument: glob (default: '*').")
    group.addoption('--cache-clear', action = 'store_true', dest = 'cacheclear', help = 'Remove all cache contents at start of test run')
    cache_dir_default = '.pytest_cache'
    if 'TOX_ENV_DIR' in os.environ:
        cache_dir_default = os.path.join(os.environ['TOX_ENV_DIR'], cache_dir_default)
    parser.addini('cache_dir', default = cache_dir_default, help = 'Cache directory path')
    group.addoption('--lfnf', '--last-failed-no-failures', action = 'store', dest = 'last_failed_no_failures', choices = ('all', 'none'), default = 'all', help = 'With ``--lf``, determines whether to execute tests when there are no previously (known) failures or when no cached ``lastfailed`` data was found. ``all`` (the default) runs the full test suite again. ``none`` just emits a message about no known failures and exits successfully.')


def pytest_cmdline_main(config = final):
    if not config.option.cacheshow and config.option.help:
        wrap_session = wrap_session
        import _pytest.main
        return wrap_session(config, cacheshow)

pytest_configure = (lambda config = None: config.cache = Cache.for_config(config, _ispytest = True)config.pluginmanager.register(LFPlugin(config), 'lfplugin')config.pluginmanager.register(NFPlugin(config), 'nfplugin'))()
cache = (lambda request = None: pass# WARNING: Decompyle incomplete
)()

def pytest_report_header(config = None):
    '''Display cachedir with --cache-show and if non-default.'''
    pass
# WARNING: Decompyle incomplete


def cacheshow(config = None, session = None):
    """Display cache contents when --cache-show is used.

    Shows cached values and directories matching the specified glob pattern
    (default: '*'). Displays cache location, cached test results, and
    any cached directories created by plugins.

    :param config: pytest configuration object.
    :param session: pytest session object.
    :returns: Exit code (0 for success).
    """
    pformat = pformat
    import pprint
# WARNING: Decompyle incomplete
