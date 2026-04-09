# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: helpconfig.pyc (Python 3.11)

'''Version info, help messages, tracing configuration.'''
from __future__ import annotations
import argparse
from collections.abc import Generator
from collections.abc import Sequence
import os
import sys
from typing import Any
from _pytest.config import Config
from _pytest.config import ExitCode
from _pytest.config import PrintHelp
from _pytest.config.argparsing import Parser
from _pytest.terminal import TerminalReporter
import pytest

class HelpAction(argparse.Action):
    pass
# WARNING: Decompyle incomplete


def pytest_addoption(parser = None):
    group = parser.getgroup('debugconfig')
    group.addoption('--version', '-V', action = 'count', default = 0, dest = 'version', help = 'Display pytest version and information about plugins. When given twice, also display information about plugins.')
    group._addoption('-h', '--help', action = HelpAction, dest = 'help', help = 'Show help message and configuration info')
    group._addoption('-p', action = 'append', dest = 'plugins', default = [], metavar = 'name', help = 'Early-load given plugin module name or entry point (multi-allowed). To avoid loading of plugins, use the `no:` prefix, e.g. `no:doctest`. See also --disable-plugin-autoload.')
    group.addoption('--disable-plugin-autoload', action = 'store_true', default = False, help = 'Disable plugin auto-loading through entry point packaging metadata. Only plugins explicitly specified in -p or env var PYTEST_PLUGINS will be loaded.')
    group.addoption('--traceconfig', '--trace-config', action = 'store_true', default = False, help = 'Trace considerations of conftest.py files')
    group.addoption('--debug', action = 'store', nargs = '?', const = 'pytestdebug.log', dest = 'debug', metavar = 'DEBUG_FILE_NAME', help = "Store internal tracing debug information in this log file. This file is opened with 'w' and truncated as a result, care advised. Default: pytestdebug.log.")
    group._addoption('-o', '--override-ini', dest = 'override_ini', action = 'append', help = 'Override configuration option with "option=value" style, e.g. `-o strict_xfail=True -o cache_dir=cache`.')

pytest_cmdline_parse = (lambda : pass# WARNING: Decompyle incomplete
)()

def show_version_verbose(config = None):
    '''Show verbose pytest version installation, including plugins.'''
    sys.stdout.write(f'''This is pytest version {pytest.__version__}, imported from {pytest.__file__}\n''')
    plugininfo = getpluginversioninfo(config)
    if plugininfo:
        for line in plugininfo:
            sys.stdout.write(line + '\n')
            return None
            return None


def pytest_cmdline_main(config = None):
    if config.option.version > 1:
        show_version_verbose(config)
        return ExitCode.OK
    if None.option.help:
        config._do_configure()
        showhelp(config)
        config._ensure_unconfigure()
        return ExitCode.OK


def showhelp(config = None):
    import textwrap
    reporter = config.pluginmanager.get_plugin('terminalreporter')
# WARNING: Decompyle incomplete


def getpluginversioninfo(config = None):
    lines = []
    plugininfo = config.pluginmanager.list_plugin_distinfo()
    if plugininfo:
        lines.append('registered third-party plugins:')
        for plugin, dist in plugininfo:
            loc = getattr(plugin, '__file__', repr(plugin))
            content = f'''{dist.project_name}-{dist.version} at {loc}'''
            lines.append('  ' + content)
            return lines


def pytest_report_header(config = None):
    lines = []
    if config.option.debug or config.option.traceconfig:
        lines.append(f'''using: pytest-{pytest.__version__}''')
        verinfo = getpluginversioninfo(config)
        if verinfo:
            lines.extend(verinfo)
    if config.option.traceconfig:
        lines.append('active plugins:')
        items = config.pluginmanager.list_name_plugin()
        for name, plugin in items:
            if hasattr(plugin, '__file__'):
                r = plugin.__file__
            else:
                r = repr(plugin)
            lines.append(f'''    {name:<20}: {r}''')
            return lines
