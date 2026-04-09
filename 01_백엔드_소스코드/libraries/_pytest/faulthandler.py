# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: faulthandler.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Generator
import os
import sys
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.nodes import Item
from _pytest.stash import StashKey
import pytest
fault_handler_original_stderr_fd_key = StashKey[int]()
fault_handler_stderr_fd_key = StashKey[int]()

def pytest_addoption(parser = None):
    help_timeout = 'Dump the traceback of all threads if a test takes more than TIMEOUT seconds to finish'
    help_exit_on_timeout = 'Exit the test process if a test takes more than faulthandler_timeout seconds to finish'
    parser.addini('faulthandler_timeout', help_timeout, default = 0)
    parser.addini('faulthandler_exit_on_timeout', help_exit_on_timeout, type = 'bool', default = False)


def pytest_configure(config = None):
    import faulthandler
    stderr_fileno = get_stderr_fileno()
    if faulthandler.is_enabled():
        config.stash[fault_handler_original_stderr_fd_key] = stderr_fileno
    config.stash[fault_handler_stderr_fd_key] = os.dup(stderr_fileno)
    faulthandler.enable(file = config.stash[fault_handler_stderr_fd_key])


def pytest_unconfigure(config = None):
    import faulthandler
    faulthandler.disable()
    if fault_handler_stderr_fd_key in config.stash:
        os.close(config.stash[fault_handler_stderr_fd_key])
        del config.stash[fault_handler_stderr_fd_key]
    if fault_handler_original_stderr_fd_key in config.stash:
        faulthandler.enable(config.stash[fault_handler_original_stderr_fd_key])
        del config.stash[fault_handler_original_stderr_fd_key]
        return None


def get_stderr_fileno():
    pass
# WARNING: Decompyle incomplete


def get_timeout_config_value(config = None):
