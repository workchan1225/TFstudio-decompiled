# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tmpdir.pyc (Python 3.11)

'''Support for providing temporary directories to test functions.'''
from __future__ import annotations
from collections.abc import Generator
import dataclasses
import os
from pathlib import Path
import re
from shutil import rmtree
import tempfile
from typing import Any
from typing import final
from typing import Literal
from pathlib import cleanup_dead_symlinks
from pathlib import LOCK_TIMEOUT
from pathlib import make_numbered_dir
from pathlib import make_numbered_dir_with_cleanup
from pathlib import rm_rf
from _pytest.compat import get_user_id
from _pytest.config import Config
from _pytest.config import ExitCode
from _pytest.config import hookimpl
from _pytest.config.argparsing import Parser
from _pytest.deprecated import check_ispytest
from _pytest.fixtures import fixture
from _pytest.fixtures import FixtureRequest
from _pytest.monkeypatch import MonkeyPatch
from _pytest.nodes import Item
from _pytest.reports import TestReport
from _pytest.stash import StashKey
tmppath_result_key = StashKey[dict[(str, bool)]]()
RetentionType = Literal[('all', 'failed', 'none')]
TempPathFactory = <NODE:12>()()

def get_user():
    '''Return the current user name, or None if getuser() does not work
    in the current environment (see #1010).'''
    
    try:
        import getpass
        return getpass.getuser()
    except (ImportError, OSError, KeyError):
        return None



def pytest_configure(config = None):
    '''Create a TempPathFactory and attach it to the config object.

    This is to comply with existing plugins which expect the handler to be
    available at pytest_configure time, but ideally should be moved entirely
    to the tmp_path_factory session fixture.
    '''
    mp = MonkeyPatch()
    config.add_cleanup(mp.undo)
    _tmp_path_factory = TempPathFactory.from_config(config, _ispytest = True)
    mp.setattr(config, '_tmp_path_factory', _tmp_path_factory, raising = False)


def pytest_addoption(parser = None):
    parser.addini('tmp_path_retention_count', help = 'How many sessions should we keep the `tmp_path` directories, according to `tmp_path_retention_policy`.', default = '3', type = 'string')
    parser.addini('tmp_path_retention_policy', help = 'Controls which directories created by the `tmp_path` fixture are kept around, based on test outcome. (all/failed/none)', type = 'string', default = 'all')

tmp_path_factory = (lambda request = None: request.config._tmp_path_factory)()

def _mk_tmp(request = None, factory = None):
    name = request.node.name
    name = re.sub('[\\W]', '_', name)
    MAXVAL = 30
    name = name[:MAXVAL]
    return factory.mktemp(name, numbered = True)

tmp_path = (lambda request = None, tmp_path_factory = None: pass# WARNING: Decompyle incomplete
)()

def pytest_sessionfinish(session = None, exitstatus = None):
    '''After each session, remove base directory if all the tests passed,
    the policy is "failed", and the basetemp is not specified by a user.
    '''
    tmp_path_factory = session.config._tmp_path_factory
    basetemp = tmp_path_factory._basetemp
# WARNING: Decompyle incomplete

pytest_runtest_makereport = (lambda item = None, call = None: pass# WARNING: Decompyle incomplete
)()
