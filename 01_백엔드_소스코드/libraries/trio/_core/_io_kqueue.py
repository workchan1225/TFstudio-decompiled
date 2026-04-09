# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _io_kqueue.pyc (Python 3.11)

from __future__ import annotations
import errno
import select
import sys
from contextlib import contextmanager
from typing import TYPE_CHECKING, Literal, TypeAlias
import attrs
import outcome
from  import _core
from _run import _public
from _wakeup_socketpair import WakeupSocketpair
if TYPE_CHECKING:
    from collections.abc import Callable, Iterator
    from _core import Abort, RaiseCancelT, Task, UnboundedQueue
    from _file_io import _HasFileNo
# WARNING: Decompyle incomplete
