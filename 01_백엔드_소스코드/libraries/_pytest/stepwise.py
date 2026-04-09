# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: stepwise.pyc (Python 3.11)

from __future__ import annotations
import dataclasses
from datetime import datetime
from datetime import timedelta
from typing import Any
from typing import TYPE_CHECKING
from _pytest import nodes
from _pytest.cacheprovider import Cache
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.main import Session
from _pytest.reports import TestReport
if TYPE_CHECKING:
    from typing_extensions import Self
STEPWISE_CACHE_DIR = 'cache/stepwise'

def pytest_addoption(parser = None):
    group = parser.getgroup('general')
    group.addoption('--sw', '--stepwise', action = 'store_true', default = False, dest = 'stepwise', help = 'Exit on test failure and continue from last failing test next time')
    group.addoption('--sw-skip', '--stepwise-skip', action = 'store_true', default = False, dest = 'stepwise_skip', help = 'Ignore the first failing test but stop on the next failing test. Implicitly enables --stepwise.')
    group.addoption('--sw-reset', '--stepwise-reset', action = 'store_true', default = False, dest = 'stepwise_reset', help = 'Resets stepwise state, restarting the stepwise workflow. Implicitly enables --stepwise.')


def pytest_configure(config = None):
    if config.option.stepwise_skip or config.option.stepwise_reset:
        config.option.stepwise = True
    if config.getoption('stepwise'):
        config.pluginmanager.register(StepwisePlugin(config), 'stepwiseplugin')
        return None


def pytest_sessionfinish(session = None):
    pass
# WARNING: Decompyle incomplete

StepwiseCacheInfo = <NODE:12>()

class StepwisePlugin:
    
    def __init__(self = None, config = None):
        self.config = config
        self.session = None
        self.report_status = []
    # WARNING: Decompyle incomplete

    
    def _load_cached_info(self = None):
