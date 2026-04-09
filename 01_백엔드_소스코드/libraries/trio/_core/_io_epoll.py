# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _io_epoll.pyc (Python 3.11)

from __future__ import annotations
import contextlib
import select
import sys
from collections import defaultdict
from typing import TYPE_CHECKING, Literal, TypeAlias
import attrs
from  import _core
from _io_common import wake_all
from _run import Task, _public
from _wakeup_socketpair import WakeupSocketpair
if TYPE_CHECKING:
    from _core import Abort, RaiseCancelT
    from _file_io import _HasFileNo
EpollWaiters = <NODE:12>()
# WARNING: Decompyle incomplete
