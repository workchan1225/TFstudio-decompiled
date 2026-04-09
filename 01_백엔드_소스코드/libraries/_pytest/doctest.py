# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: doctest.pyc (Python 3.11)

'''Discover and run doctests in modules and test files.'''
from __future__ import annotations
import bdb
from collections.abc import Callable
from collections.abc import Generator
from collections.abc import Iterable
from collections.abc import Sequence
from contextlib import contextmanager
import functools
import inspect
import os
from pathlib import Path
import platform
import re
import sys
import traceback
import types
from typing import Any
from typing import TYPE_CHECKING
import warnings
from _pytest import outcomes
from _pytest._code.code import ExceptionInfo
from _pytest._code.code import ReprFileLocation
from _pytest._code.code import TerminalRepr
from _pytest._io import TerminalWriter
from _pytest.compat import safe_getattr
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.fixtures import fixture
from _pytest.fixtures import TopRequest
from _pytest.nodes import Collector
from _pytest.nodes import Item
from _pytest.outcomes import OutcomeException
from _pytest.outcomes import skip
from _pytest.pathlib import fnmatch_ex
from _pytest.python import Module
from _pytest.python_api import approx
from _pytest.warning_types import PytestWarning
if TYPE_CHECKING:
    import doctest
    from typing_extensions import Self
DOCTEST_REPORT_CHOICE_NONE = 'none'
DOCTEST_REPORT_CHOICE_CDIFF = 'cdiff'
DOCTEST_REPORT_CHOICE_NDIFF = 'ndiff'
DOCTEST_REPORT_CHOICE_UDIFF = 'udiff'
DOCTEST_REPORT_CHOICE_ONLY_FIRST_FAILURE = 'only_first_failure'
DOCTEST_REPORT_CHOICES = (DOCTEST_REPORT_CHOICE_NONE, DOCTEST_REPORT_CHOICE_CDIFF, DOCTEST_REPORT_CHOICE_NDIFF, DOCTEST_REPORT_CHOICE_UDIFF, DOCTEST_REPORT_CHOICE_ONLY_FIRST_FAILURE)
RUNNER_CLASS = None
CHECKER_CLASS: 'type[doctest.OutputChecker] | None' = None

def pytest_addoption(parser = None):
    parser.addini('doctest_optionflags', 'Option flags for doctests', type = 'args', default = [
        'ELLIPSIS'])
    parser.addini('doctest_encoding', 'Encoding used for doctest files', default = 'utf-8')
    group = parser.getgroup('collect')
    group.addoption('--doctest-modules', action = 'store_true', default = False, help = 'Run doctests in all .py modules', dest = 'doctestmodules')
    group.addoption('--doctest-report', type = str.lower, default = 'udiff', help = 'Choose another output format for diffs on doctest failure', choices = DOCTEST_REPORT_CHOICES, dest = 'doctestreport')
    group.addoption('--doctest-glob', action = 'append', default = [], metavar = 'pat', help = 'Doctests file matching pattern, default: test*.txt', dest = 'doctestglob')
    group.addoption('--doctest-ignore-import-errors', action = 'store_true', default = False, help = 'Ignore doctest collection errors', dest = 'doctest_ignore_import_errors')
    group.addoption('--doctest-continue-on-failure', action = 'store_true', default = False, help = 'For a given doctest, continue to run after the first failure', dest = 'doctest_continue_on_failure')


def pytest_unconfigure():
    global RUNNER_CLASS
    RUNNER_CLASS = None


def pytest_collect_file(file_path = None, parent = None):
    config = parent.config
    if file_path.suffix == '.py':
        if not config.option.doctestmodules and any((_is_setup_py(file_path), _is_main_py(file_path))):
            return DoctestModule.from_parent(parent, path = file_path)
    if _is_doctest(config, file_path, parent):
        return DoctestTextfile.from_parent(parent, path = file_path)


def _is_setup_py(path = None):
