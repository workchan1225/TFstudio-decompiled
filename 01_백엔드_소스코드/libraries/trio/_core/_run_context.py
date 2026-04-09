# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _run_context.pyc (Python 3.11)

from __future__ import annotations
import threading
from typing import TYPE_CHECKING, Final
if TYPE_CHECKING:
    from _run import Runner, Task

class RunContext(threading.local):
    task: 'Task' = 'RunContext'

GLOBAL_RUN_CONTEXT: 'Final' = RunContext()
