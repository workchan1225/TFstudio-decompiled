# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

__doc__ = 'Command line options, config-file and conftest.py processing.'
from __future__ import annotations
import argparse
import builtins
import collections.abc as collections
from collections.abc import Callable
from collections.abc import Generator
from collections.abc import Iterable
from collections.abc import Iterator
from collections.abc import Mapping
from collections.abc import MutableMapping
from collections.abc import Sequence
import contextlib
import copy
import dataclasses
import enum
from functools import lru_cache
import glob
import importlib.metadata as importlib
import inspect
import os
import pathlib
import re
import shlex
import sys
from textwrap import dedent
import types
from types import FunctionType
from typing import Any
from typing import cast
from typing import Final
from typing import final
from typing import IO
from typing import TextIO
from typing import TYPE_CHECKING
import warnings
import pluggy
from pluggy import HookimplMarker
from pluggy import HookimplOpts
from pluggy import HookspecMarker
from pluggy import HookspecOpts
from pluggy import PluginManager
from compat import PathAwareHookProxy
from exceptions import PrintHelp
from exceptions import UsageError
from findpaths import ConfigValue
from findpaths import determine_setup
from _pytest import __version__
import _pytest._code as _pytest
from _pytest._code import ExceptionInfo
from _pytest._code import filter_traceback
from _pytest._code.code import TracebackStyle
from _pytest._io import TerminalWriter
from _pytest.compat import assert_never
from _pytest.config.argparsing import Argument
from _pytest.config.argparsing import FILE_OR_DIR
from _pytest.config.argparsing import Parser
import _pytest.deprecated as _pytest
import _pytest.hookspec as _pytest
from _pytest.outcomes import fail
from _pytest.outcomes import Skipped
from _pytest.pathlib import absolutepath
from _pytest.pathlib import bestrelpath
from _pytest.pathlib import import_path
from _pytest.pathlib import ImportMode
from _pytest.pathlib import resolve_package_path
from _pytest.pathlib import safe_exists
from _pytest.stash import Stash
from _pytest.warning_types import PytestConfigWarning
from _pytest.warning_types import warn_explicit_for
if TYPE_CHECKING:
    from _pytest.assertion.rewrite import AssertionRewritingHook
    from _pytest.cacheprovider import Cache
    from _pytest.terminal import TerminalReporter
_PluggyPlugin = object
hookimpl = HookimplMarker('pytest')
hookspec = HookspecMarker('pytest')
ExitCode = <NODE:12>()

class ConftestImportFailure(Exception):
    
    def __init__(self = None, path = None, *, cause):
        self.path = path
        self.cause = cause

    
    def __str__(self = None):
        return f'''{type(self.cause).__name__}: {self.cause} (from {self.path})'''



def filter_traceback_for_conftest_import_failure(entry = None):
    '''Filter tracebacks entries which point to pytest internals or importlib.

    Make a special case for importlib because we use it to import test modules and conftest files
    in _pytest.pathlib.import_path.
    '''
    if filter_traceback(entry):
        pass
    return 'importlib' not in str(entry.path).split(os.sep)


def print_conftest_import_error(e = None, file = None):
    exc_info = ExceptionInfo.from_exception(e.cause)
    tw = TerminalWriter(file)
    tw.line(f'''ImportError while loading conftest \'{e.path}\'.''', red = True)
    exc_info.traceback = exc_info.traceback.filter(filter_traceback_for_conftest_import_failure)
    exc_repr = exc_info.getrepr(style = 'short', chain = False) if exc_info.traceback else exc_info.exconly()
    formatted_tb = str(exc_repr)
    for line in formatted_tb.splitlines():
        tw.line(line.rstrip(), red = True)
        return None


def print_usage_error(e = None, file = None):
    tw = TerminalWriter(file)
    for msg in e.args:
        tw.line(f'''ERROR: {msg}\n''', red = True)
        return None


def main(args = None, plugins = None):
    '''Perform an in-process test run.

    :param args:
        List of command line arguments. If `None` or not given, defaults to reading
        arguments directly from the process command line (:data:`sys.argv`).
    :param plugins: List of plugin objects to be auto-registered during initialization.

    :returns: An exit code.
    '''
    pass
# WARNING: Decompyle incomplete


def console_main():
    '''The CLI entry point of pytest.

    This function is not meant for programmable use; use `main()` instead.
    '''
    
    try:
        code = main()
        sys.stdout.flush()
        return code
    except BrokenPipeError:
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        return 1



class cmdline:
    main = staticmethod(main)


def filename_arg(path = None, optname = None):
    '''Argparse type validator for filename arguments.

    :path: Path of filename.
    :optname: Name of the option.
    '''
    if os.path.isdir(path):
        raise UsageError(f'''{optname} must be a filename, given: {path}''')
    return path


def directory_arg(path = None, optname = None):
    '''Argparse type validator for directory arguments.

    :path: Path of directory.
    :optname: Name of the option.
    '''
    if not os.path.isdir(path):
        raise UsageError(f'''{optname} must be a directory, given: {path}''')
    return path

essential_plugins = ('mark', 'main', 'runner', 'fixtures', 'helpconfig')
# WARNING: Decompyle incomplete
