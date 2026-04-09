# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: setupplan.pyc (Python 3.11)

from __future__ import annotations
from _pytest.config import Config
from _pytest.config import ExitCode
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureDef
from _pytest.fixtures import SubRequest
import pytest

def pytest_addoption(parser = None):
    group = parser.getgroup('debugconfig')
    group.addoption('--setupplan', '--setup-plan', action = 'store_true', help = "Show what fixtures and tests would be executed but don't execute anything")

pytest_fixture_setup = (lambda fixturedef = None, request = None: if request.config.option.setupplan:
my_cache_key = fixturedef.cache_key(request)fixturedef.cached_result = (None, my_cache_key, None)fixturedef.cached_result)()
pytest_cmdline_main = (lambda config = None: if config.option.setupplan:
config.option.setuponly = Trueconfig.option.setupshow = True)()
