# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: terminal.pyc (Python 3.11)

'''Terminal reporting of the full testing process.

This is a good source for looking at the various reporting hooks.
'''
from __future__ import annotations
import argparse
from collections import Counter
from collections.abc import Callable
from collections.abc import Generator
from collections.abc import Mapping
from collections.abc import Sequence
import dataclasses
import datetime
from functools import partial
import inspect
from pathlib import Path
import platform
import sys
import textwrap
from typing import Any
from typing import ClassVar
from typing import final
from typing import Literal
from typing import NamedTuple
from typing import TextIO
from typing import TYPE_CHECKING
import warnings
import pluggy
from _pytest import compat
from _pytest import nodes
from _pytest import timing
from _pytest._code import ExceptionInfo
from _pytest._code.code import ExceptionRepr
from _pytest._io import TerminalWriter
from _pytest._io.wcwidth import wcswidth
import _pytest._version as _pytest
from _pytest.compat import running_on_ci
from _pytest.config import _PluggyPlugin
from _pytest.config import Config
from _pytest.config import ExitCode
from _pytest.config import hookimpl
from _pytest.config.argparsing import Parser
from _pytest.nodes import Item
from _pytest.nodes import Node
from _pytest.pathlib import absolutepath
from _pytest.pathlib import bestrelpath
from _pytest.reports import BaseReport
from _pytest.reports import CollectReport
from _pytest.reports import TestReport
if TYPE_CHECKING:
    from _pytest.main import Session
REPORT_COLLECTING_RESOLUTION = 0.5
KNOWN_TYPES = ('failed', 'passed', 'skipped', 'deselected', 'xfailed', 'xpassed', 'warnings', 'error', 'subtests passed', 'subtests failed', 'subtests skipped')
_REPORTCHARS_DEFAULT = 'fE'

class MoreQuietAction(argparse.Action):
    pass
# WARNING: Decompyle incomplete


class TestShortLogReport(NamedTuple):
    word: 'str | tuple[str, Mapping[str, bool]]' = 'Used to store the test status result category, shortletter and verbose word.\n    For example ``"rerun", "R", ("RERUN", {"yellow": True})``.\n\n    :ivar category:\n        The class of result, for example ``“passed”``, ``“skipped”``, ``“error”``, or the empty string.\n\n    :ivar letter:\n        The short letter shown as testing progresses, for example ``"."``, ``"s"``, ``"E"``, or the empty string.\n\n    :ivar word:\n        Verbose word is shown as testing progresses in verbose mode, for example ``"PASSED"``, ``"SKIPPED"``,\n        ``"ERROR"``, or the empty string.\n    '


def pytest_addoption(parser = None):
    group = parser.getgroup('terminal reporting', 'Reporting', after = 'general')
    group._addoption('-v', '--verbose', action = 'count', default = 0, dest = 'verbose', help = 'Increase verbosity')
    group.addoption('--no-header', action = 'store_true', default = False, dest = 'no_header', help = 'Disable header')
    group.addoption('--no-summary', action = 'store_true', default = False, dest = 'no_summary', help = 'Disable summary')
    group.addoption('--no-fold-skipped', action = 'store_false', dest = 'fold_skipped', default = True, help = 'Do not fold skipped tests in short summary.')
    group.addoption('--force-short-summary', action = 'store_true', dest = 'force_short_summary', default = False, help = 'Force condensed summary output regardless of verbosity level.')
    group._addoption('-q', '--quiet', action = MoreQuietAction, default = 0, dest = 'verbose', help = 'Decrease verbosity')
    group.addoption('--verbosity', dest = 'verbose', type = int, default = 0, help = 'Set verbosity. Default: 0.')
    group._addoption('-r', action = 'store', dest = 'reportchars', default = _REPORTCHARS_DEFAULT, metavar = 'chars', help = "Show extra test summary info as specified by chars: (f)ailed, (E)rror, (s)kipped, (x)failed, (X)passed, (p)assed, (P)assed with output, (a)ll except passed (p/P), or (A)ll. (w)arnings are enabled by default (see --disable-warnings), 'N' can be used to reset the list. (default: 'fE').")
    group.addoption('--disable-warnings', '--disable-pytest-warnings', default = False, dest = 'disable_warnings', action = 'store_true', help = 'Disable warnings summary')
    group._addoption('-l', '--showlocals', action = 'store_true', dest = 'showlocals', default = False, help = 'Show locals in tracebacks (disabled by default)')
    group.addoption('--no-showlocals', action = 'store_false', dest = 'showlocals', help = 'Hide locals in tracebacks (negate --showlocals passed through addopts)')
    group.addoption('--tb', metavar = 'style', action = 'store', dest = 'tbstyle', default = 'auto', choices = [
        'auto',
        'long',
        'short',
        'no',
        'line',
        'native'], help = 'Traceback print mode (auto/long/short/line/native/no)')
    group.addoption('--xfail-tb', action = 'store_true', dest = 'xfail_tb', default = False, help = 'Show tracebacks for xfail (as long as --tb != no)')
    group.addoption('--show-capture', action = 'store', dest = 'showcapture', choices = [
        'no',
        'stdout',
        'stderr',
        'log',
        'all'], default = 'all', help = 'Controls how captured stdout/stderr/log is shown on failed tests. Default: all.')
    group.addoption('--fulltrace', '--full-trace', action = 'store_true', default = False, help = "Don't cut any tracebacks (default is to cut)")
    group.addoption('--color', metavar = 'color', action = 'store', dest = 'color', default = 'auto', choices = [
        'yes',
        'no',
        'auto'], help = 'Color terminal output (yes/no/auto)')
    group.addoption('--code-highlight', default = 'yes', choices = [
        'yes',
        'no'], help = 'Whether code should be highlighted (only if --color is also enabled). Default: yes.')
    parser.addini('console_output_style', help = 'Console output: "classic", or with additional progress information ("progress" (percentage) | "count" | "progress-even-when-capture-no" (forces progress even when capture=no)', default = 'progress')
    Config._add_verbosity_ini(parser, Config.VERBOSITY_TEST_CASES, help = 'Specify a verbosity level for test case execution, overriding the main level. Higher levels will provide more detailed information about each test case executed.')


def pytest_configure(config = None):
    pass
# WARNING: Decompyle incomplete


def getreportopt(config = None):
    reportchars = config.option.reportchars
    old_aliases = {
        'F',
        'S'}
    reportopts = ''
    for char in reportchars:
        if char in old_aliases:
            char = char.lower()
        if char == 'a':
            reportopts = 'sxXEf'
            continue
        if char == 'A':
            reportopts = 'PpsxXEf'
            continue
        if char == 'N':
            reportopts = ''
            continue
        if char not in reportopts:
            reportopts += char
        if config.option.disable_warnings and 'w' not in reportopts:
            reportopts = 'w' + reportopts
        elif config.option.disable_warnings and 'w' in reportopts:
            reportopts = reportopts.replace('w', '')
    return reportopts

pytest_report_teststatus = (lambda report = None: letter = 'F'if report.passed:
letter = '.'elif report.skipped:
letter = 's'outcome = report.outcomeif report.when in ('collect', 'setup', 'teardown') and outcome == 'failed':
outcome = 'error'letter = 'E'(outcome, letter, outcome.upper()))()
WarningReport = <NODE:12>()
TerminalReporter = <NODE:12>()

def _get_node_id_with_markup(tw = None, config = dataclasses.dataclass, rep = final):
    nodeid = config.cwd_relative_nodeid(rep.nodeid)
# WARNING: Decompyle incomplete


def _format_trimmed(format = None, msg = None, available_width = None):
    """Format msg into format, ellipsizing it if doesn't fit in available_width.

    Returns None if even the ellipsis can't fit.
    """
    i = msg.find('\n')
    if i != -1:
        msg = msg[:i]
    ellipsis = '...'
    format_width = wcswidth(format.format(''))
    if format_width + len(ellipsis) > available_width:
        return None
# WARNING: Decompyle incomplete


def _get_line_with_reprcrash_message(config = None, rep = None, tw = None, word_markup = ('config', 'Config', 'rep', 'BaseReport', 'tw', 'TerminalWriter', 'word_markup', 'dict[str, bool]', 'return', 'str')):
    '''Get summary line for a report, trying to add reprcrash message.'''
    (verbose_word, verbose_markup) = rep._get_verbose_word_with_markup(config, word_markup)
# WARNING: Decompyle incomplete


def _folded_skips(startpath = None, skipped = None):
    d = { }
# WARNING: Decompyle incomplete

_color_for_type = {
    'failed': 'red',
    'error': 'red',
    'warnings': 'yellow',
    'passed': 'green',
    'subtests passed': 'green',
    'subtests failed': 'red' }
_color_for_type_default = 'yellow'

def pluralize(count = None, noun = None):
    if noun not in ('error', 'warnings', 'test'):
        return (count, noun)
    noun = None.replace('warnings', 'warning')
    return (count, noun + 's' if count != 1 else noun)


def _plugin_nameversions(plugininfo = None):
    values = []
    for plugin, dist in plugininfo:
        name = f'''{dist.project_name}-{dist.version}'''
        if name.startswith('pytest-'):
            name = name[7:]
        if name not in values:
            values.append(name)
        return values


def format_session_duration(seconds = None):
    '''Format the given seconds in a human readable manner to show in the final summary.'''
    if seconds < 60:
        return f'''{seconds:.2f}s'''
    dt = None.timedelta(seconds = int(seconds))
    return f'''{seconds:.2f}s ({dt})'''


def format_node_duration(seconds = None):
    '''Format the given seconds in a human readable manner to show in the test progress.'''
    if seconds < 1e-05:
        return f''' {seconds * 1000000:.3f}us'''
    if None < 0.0001:
        return f''' {seconds * 1000000:.2f}us'''
    if None < 0.001:
        return f''' {seconds * 1000000:.1f}us'''
    if None < 0.01:
        return f''' {seconds * 1000:.3f}ms'''
    if None < 0.1:
        return f''' {seconds * 1000:.2f}ms'''
    if None < 1:
        return f''' {seconds * 1000:.1f}ms'''
    if None < 60:
        return f''' {seconds:.3f}s'''
    if None < 3600:
        return f''' {seconds // 60:.0f}m {seconds % 60:.0f}s'''
    return f'''{seconds // 3600:.0f}h {(seconds % 3600) // 60:.0f}m'''


def _get_raw_skip_reason(report = None):
    '''Get the reason string of a skip/xfail/xpass test report.

    The string is just the part given by the user.
    '''
    if hasattr(report, 'wasxfail'):
        reason = report.wasxfail
        if reason.startswith('reason: '):
            reason = reason[len('reason: '):]
        return reason
# WARNING: Decompyle incomplete


class TerminalProgressPlugin:
    '''Terminal progress reporting plugin using OSC 9;4 ANSI sequences.

    Emits OSC 9;4 sequences to indicate test progress to terminal
    tabs/windows/etc.

    Not all terminal emulators support this feature.

    Ref: https://conemu.github.io/en/AnsiEscapeCodes.html#ConEmu_specific_OSC
    '''
    
    def __init__(self = None, tr = None):
        self._tr = tr
        self._session = None
        self._has_failures = False

    
    def _emit_progress(self = None, state = None, progress = None):
        '''Emit OSC 9;4 sequence for indicating progress to the terminal.

        :param state:
            Progress state to set.
        :param progress:
            Progress value 0-100. Required for "normal", optional for "error"
            and "paused", otherwise ignored.
        '''
        pass
    # WARNING: Decompyle incomplete

    pytest_sessionstart = (lambda self = None, session = None: self._session = sessionself._emit_progress('indeterminate'))()
    pytest_collection_finish = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    pytest_runtest_logreport = (lambda self = None, report = None: if report.failed:
self._has_failures = Trueif report.when != 'call':
None# WARNING: Decompyle incomplete
)()
    pytest_sessionfinish = (lambda self = None: self._emit_progress('remove'))()
