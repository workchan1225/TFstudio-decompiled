# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _pswindows.pyc (Python 3.11)

__doc__ = 'Windows platform implementation.'
import contextlib
import enum
import functools
import os
import signal
import sys
import threading
import time
from collections import namedtuple
from  import _common
from _common import ENCODING
from _common import AccessDenied
from _common import NoSuchProcess
from _common import TimeoutExpired
from _common import conn_tmap
from _common import conn_to_ntuple
from _common import debug
from _common import isfile_strict
from _common import memoize
from _common import memoize_when_activated
from _common import parse_environ_block
from _common import usage_percent
from _psutil_windows import ABOVE_NORMAL_PRIORITY_CLASS
from _psutil_windows import BELOW_NORMAL_PRIORITY_CLASS
from _psutil_windows import HIGH_PRIORITY_CLASS
from _psutil_windows import IDLE_PRIORITY_CLASS
from _psutil_windows import NORMAL_PRIORITY_CLASS
from _psutil_windows import REALTIME_PRIORITY_CLASS

try:
    from  import _psutil_windows as cext
except ImportError:
    err = None
    if str(err).lower().startswith('dll load failed') and sys.getwindowsversion()[0] < 6:
        msg = 'this Windows version is too old (< Windows Vista); '
        msg += 'psutil 3.4.2 is the latest version which supports Windows '
        msg += '2000, XP and 2003 server'
        raise RuntimeError(msg), err
    raise 
    err = None
    del err

__extra__all__ = [
    'win_service_iter',
    'win_service_get',
    'ABOVE_NORMAL_PRIORITY_CLASS',
    'BELOW_NORMAL_PRIORITY_CLASS',
    'HIGH_PRIORITY_CLASS',
    'IDLE_PRIORITY_CLASS',
    'NORMAL_PRIORITY_CLASS',
    'REALTIME_PRIORITY_CLASS',
    'IOPRIO_VERYLOW',
    'IOPRIO_LOW',
    'IOPRIO_NORMAL',
    'IOPRIO_HIGH',
    'CONN_DELETE_TCB',
    'AF_LINK']
CONN_DELETE_TCB = 'DELETE_TCB'
ERROR_PARTIAL_COPY = 299
PYPY = '__pypy__' in sys.builtin_module_names
AddressFamily = enum.IntEnum('AddressFamily', {
    'AF_LINK': -1 })
AF_LINK = AddressFamily.AF_LINK
TCP_STATUSES = {
    cext.PSUTIL_CONN_NONE: _common.CONN_NONE,
    cext.MIB_TCP_STATE_DELETE_TCB: CONN_DELETE_TCB,
    cext.MIB_TCP_STATE_CLOSING: _common.CONN_CLOSING,
    cext.MIB_TCP_STATE_LISTEN: _common.CONN_LISTEN,
    cext.MIB_TCP_STATE_LAST_ACK: _common.CONN_LAST_ACK,
    cext.MIB_TCP_STATE_CLOSE_WAIT: _common.CONN_CLOSE_WAIT,
    cext.MIB_TCP_STATE_CLOSED: _common.CONN_CLOSE,
    cext.MIB_TCP_STATE_TIME_WAIT: _common.CONN_TIME_WAIT,
    cext.MIB_TCP_STATE_FIN_WAIT2: _common.CONN_FIN_WAIT2,
    cext.MIB_TCP_STATE_FIN_WAIT1: _common.CONN_FIN_WAIT1,
    cext.MIB_TCP_STATE_SYN_RCVD: _common.CONN_SYN_RECV,
    cext.MIB_TCP_STATE_SYN_SENT: _common.CONN_SYN_SENT,
    cext.MIB_TCP_STATE_ESTAB: _common.CONN_ESTABLISHED }

class Priority(enum.IntEnum):
    ABOVE_NORMAL_PRIORITY_CLASS = ABOVE_NORMAL_PRIORITY_CLASS
    BELOW_NORMAL_PRIORITY_CLASS = BELOW_NORMAL_PRIORITY_CLASS
    HIGH_PRIORITY_CLASS = HIGH_PRIORITY_CLASS
    IDLE_PRIORITY_CLASS = IDLE_PRIORITY_CLASS
    NORMAL_PRIORITY_CLASS = NORMAL_PRIORITY_CLASS
    REALTIME_PRIORITY_CLASS = REALTIME_PRIORITY_CLASS

globals().update(Priority.__members__)

class IOPriority(enum.IntEnum):
    IOPRIO_VERYLOW = 0
    IOPRIO_LOW = 1
    IOPRIO_NORMAL = 2
    IOPRIO_HIGH = 3

globals().update(IOPriority.__members__)
# WARNING: Decompyle incomplete
