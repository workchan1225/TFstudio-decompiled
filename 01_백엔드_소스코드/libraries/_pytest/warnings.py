# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: warnings.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Generator
from contextlib import contextmanager
from contextlib import ExitStack
import sys
from typing import Literal
import warnings
from _pytest.config import apply_warning_filters
from _pytest.config import Config
from _pytest.config import parse_warning_filter
from _pytest.main import Session
from _pytest.nodes import Item
from _pytest.terminal import TerminalReporter
from _pytest.tracemalloc import tracemalloc_message
import pytest
catch_warnings_for_item = (lambda config = None, ihook = None, when = None, item = contextmanager, *, record, config_filters = None, cmdline_filters = None, log = None: pass# WARNING: Decompyle incomplete
)()

def warning_record_to_str(warning_message = None):
    '''Convert a warnings.WarningMessage to a string.'''
    return warnings.formatwarning(str(warning_message.message), warning_message.category, warning_message.filename, warning_message.lineno, warning_message.line) + tracemalloc_message(warning_message.source)

pytest_runtest_protocol = (lambda item = None: pass# WARNING: Decompyle incomplete
)()
pytest_collection = (lambda session = None: pass# WARNING: Decompyle incomplete
)()
pytest_terminal_summary = (lambda terminalreporter = None: pass# WARNING: Decompyle incomplete
)()
pytest_sessionfinish = (lambda session = None: pass# WARNING: Decompyle incomplete
)()
pytest_load_initial_conftests = (lambda early_config = None: pass# WARNING: Decompyle incomplete
)()

def pytest_configure(config = None):
    stack = ExitStack()
    stack.enter_context(catch_warnings_for_item(config = config, ihook = config.hook, when = 'config', item = None, record = False))
    config.addinivalue_line('markers', 'filterwarnings(warning): add a warning filter to the given test. see https://docs.pytest.org/en/stable/how-to/capture-warnings.html#pytest-mark-filterwarnings ')
    config.add_cleanup(stack.pop_all().close)
    None(None, None)
    return None
    with None:
        if not None:
            pass
