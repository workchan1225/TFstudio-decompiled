# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: setuponly.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Generator
from _pytest._io.saferepr import saferepr
from _pytest.config import Config
from _pytest.config import ExitCode
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureDef
from _pytest.fixtures import SubRequest
from _pytest.scope import Scope
import pytest

def pytest_addoption(parser = None):
    group = parser.getgroup('debugconfig')
    group.addoption('--setuponly', '--setup-only', action = 'store_true', help = 'Only setup fixtures, do not execute tests')
    group.addoption('--setupshow', '--setup-show', action = 'store_true', help = 'Show setup of fixtures while executing tests')

pytest_fixture_setup = (lambda fixturedef = None, request = None: pass# WARNING: Decompyle incomplete
)()

def pytest_fixture_post_finalizer(fixturedef = None, request = None):
    pass
# WARNING: Decompyle incomplete


def _show_fixture_action(fixturedef = None, config = None, msg = None):
    capman = config.pluginmanager.getplugin('capturemanager')
    if capman:
        capman.suspend_global_capture()
    tw = config.get_terminal_writer()
    tw.line()
    scope_indent = list(reversed(Scope)).index(fixturedef._scope)
    tw.write('  ' * scope_indent)
    scopename = fixturedef.scope[0].upper()
    tw.write(f'''{msg:<8} {scopename} {fixturedef.argname}''')
    if msg == 'SETUP':
        deps = (lambda .0: pass# WARNING: Decompyle incomplete
)(fixturedef.argnames())
        if deps:
            tw.write(' (fixtures used: {})'.format(', '.join(deps)))
    if hasattr(fixturedef, 'cached_param'):
        tw.write(f'''[{saferepr(fixturedef.cached_param, maxsize = 42)}]''')
    tw.flush()
    if capman:
        capman.resume_global_capture()
        return None
    return sorted

pytest_cmdline_main = (lambda config = None: if config.option.setuponly:
config.option.setupshow = True)()
