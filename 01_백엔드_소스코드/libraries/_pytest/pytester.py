# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pytester.pyc (Python 3.11)

'''(Disabled by default) support for testing pytest and pytest plugins.

PYTEST_DONT_REWRITE
'''
from __future__ import annotations
import collections.abc as collections
from collections.abc import Callable
from collections.abc import Generator
from collections.abc import Iterable
from collections.abc import Sequence
import contextlib
from fnmatch import fnmatch
import gc
import importlib
from io import StringIO
import locale
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import traceback
from typing import Any
from typing import Final
from typing import final
from typing import IO
from typing import Literal
from typing import overload
from typing import TextIO
from typing import TYPE_CHECKING
from weakref import WeakKeyDictionary
from iniconfig import IniConfig
from iniconfig import SectionWrapper
from _pytest import timing
from _pytest._code import Source
from _pytest.capture import _get_multicapture
from _pytest.compat import NOTSET
from _pytest.compat import NotSetType
from _pytest.config import _PluggyPlugin
from _pytest.config import Config
from _pytest.config import ExitCode
from _pytest.config import hookimpl
from _pytest.config import main
from _pytest.config import PytestPluginManager
from _pytest.config.argparsing import Parser
from _pytest.deprecated import check_ispytest
from _pytest.fixtures import fixture
from _pytest.fixtures import FixtureRequest
from _pytest.main import Session
from _pytest.monkeypatch import MonkeyPatch
from _pytest.nodes import Collector
from _pytest.nodes import Item
from _pytest.outcomes import fail
from _pytest.outcomes import importorskip
from _pytest.outcomes import skip
from _pytest.pathlib import bestrelpath
from _pytest.pathlib import make_numbered_dir
from _pytest.reports import CollectReport
from _pytest.reports import TestReport
from _pytest.tmpdir import TempPathFactory
from _pytest.warning_types import PytestFDWarning
if TYPE_CHECKING:
    import pexpect
pytest_plugins = [
    'pytester_assertions']
IGNORE_PAM = [
    '/var/lib/sss/mc/passwd']

def pytest_addoption(parser = None):
    parser.addoption('--lsof', action = 'store_true', dest = 'lsof', default = False, help = 'Run FD checks if lsof is available')
    parser.addoption('--runpytest', default = 'inprocess', dest = 'runpytest', choices = ('inprocess', 'subprocess'), help = "Run pytest sub runs in tests using an 'inprocess' or 'subprocess' (python -m main) method")
    parser.addini('pytester_example_dir', help = 'Directory to take the pytester example files from')


def pytest_configure(config = None):
    if config.getvalue('lsof'):
        checker = LsofFdLeakChecker()
        if checker.matching_platform():
            config.pluginmanager.register(checker)
    config.addinivalue_line('markers', 'pytester_example_path(*path_segments): join the given path segments to `pytester_example_dir` for this test.')


class LsofFdLeakChecker:
    
    def get_open_files(self = None):
        if sys.version_info >= (3, 11):
            encoding = locale.getencoding()
        else:
            encoding = locale.getpreferredencoding(False)
        out = subprocess.run(('lsof', '-Ffn0', '-p', str(os.getpid())), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL, check = True, text = True, encoding = encoding).stdout
        
        def isopen(line = None):
