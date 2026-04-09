# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: skipping.pyc (Python 3.11)

'''Support for skip/xfail functions and markers.'''
from __future__ import annotations
from collections.abc import Generator
from collections.abc import Mapping
import dataclasses
import os
import platform
import sys
import traceback
from _pytest.config import Config
from _pytest.config import hookimpl
from _pytest.config.argparsing import Parser
from _pytest.mark.structures import Mark
from _pytest.nodes import Item
from _pytest.outcomes import fail
from _pytest.outcomes import skip
from _pytest.outcomes import xfail
from _pytest.raises import AbstractRaises
from _pytest.reports import BaseReport
from _pytest.reports import TestReport
from _pytest.runner import CallInfo
from _pytest.stash import StashKey

def pytest_addoption(parser = None):
    group = parser.getgroup('general')
    group.addoption('--runxfail', action = 'store_true', dest = 'runxfail', default = False, help = 'Report the results of xfail tests as if they were not marked')
    parser.addini('strict_xfail', 'Default for the strict parameter of xfail markers when not given explicitly (default: False) (alias: xfail_strict)', type = 'bool', default = None, aliases = [
        'xfail_strict'])


def pytest_configure(config = None):
    pass
# WARNING: Decompyle incomplete


def evaluate_condition(item = None, mark = None, condition = None):
    """Evaluate a single skipif/xfail condition.

    If an old-style string condition is given, it is eval()'d, otherwise the
    condition is bool()'d. If this fails, an appropriately formatted pytest.fail
    is raised.

    Returns (result, reason). The reason is only relevant if the result is True.
    """
    pass
# WARNING: Decompyle incomplete

Skip = <NODE:12>()

def evaluate_skip_marks(item = None):
    '''Evaluate skip and skipif marks on item, returning Skip if triggered.'''
    pass
# WARNING: Decompyle incomplete

Xfail = <NODE:12>()

def evaluate_xfail_marks(item = None):
    '''Evaluate xfail marks on item, returning Xfail if triggered.'''
    pass
# WARNING: Decompyle incomplete

xfailed_key = StashKey[Xfail | None]()
pytest_runtest_setup = (lambda item = None: skipped = evaluate_skip_marks(item)if skipped:
raise skip.Exception(skipped.reason, _use_item_location = True)item.stash[xfailed_key] = evaluate_xfail_marks(item)xfailed = evaluate_xfail_marks(item)if not xfailed or item.config.option.runxfail or xfailed.run:
xfail('[NOTRUN] ' + xfailed.reason)NoneNoneNone)()
pytest_runtest_call = (lambda item = None: pass# WARNING: Decompyle incomplete
)()
pytest_runtest_makereport = (lambda item = None, call = None: pass# WARNING: Decompyle incomplete
)()

def pytest_report_teststatus(report = None):
