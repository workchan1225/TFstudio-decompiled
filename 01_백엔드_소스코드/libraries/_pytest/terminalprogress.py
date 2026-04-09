# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: terminalprogress.pyc (Python 3.11)

from __future__ import annotations
import os
from _pytest.config import Config
from _pytest.config import hookimpl
from _pytest.terminal import TerminalProgressPlugin
from _pytest.terminal import TerminalReporter
pytest_configure = (lambda config = None: reporter = config.pluginmanager.get_plugin('terminalreporter')# WARNING: Decompyle incomplete
)()
