# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _common.pyc (Python 3.11)

__doc__ = 'Common objects shared by __init__.py and _ps*.py modules.\n\nNote: this module is imported by setup.py, so it should not import\npsutil or third-party modules.\n'
import collections
import enum
import functools
import os
import socket
import stat
import sys
import threading
import warnings
from collections import namedtuple
from socket import AF_INET
from socket import SOCK_DGRAM
from socket import SOCK_STREAM

try:
    from socket import AF_INET6
except ImportError:
    AF_INET6 = None


try:
    from socket import AF_UNIX
except ImportError:
    AF_UNIX = None

PSUTIL_DEBUG = bool(os.getenv('PSUTIL_DEBUG'))
_DEFAULT = object()
__all__ = [
    'FREEBSD',
    'BSD',
    'LINUX',
    'NETBSD',
    'OPENBSD',
    'MACOS',
    'OSX',
    'POSIX',
    'SUNOS',
    'WINDOWS',
    'CONN_CLOSE',
    'CONN_CLOSE_WAIT',
    'CONN_CLOSING',
    'CONN_ESTABLISHED',
    'CONN_FIN_WAIT1',
    'CONN_FIN_WAIT2',
    'CONN_LAST_ACK',
    'CONN_LISTEN',
    'CONN_NONE',
    'CONN_SYN_RECV',
    'CONN_SYN_SENT',
    'CONN_TIME_WAIT',
    'NIC_DUPLEX_FULL',
    'NIC_DUPLEX_HALF',
    'NIC_DUPLEX_UNKNOWN',
    'STATUS_DEAD',
    'STATUS_DISK_SLEEP',
    'STATUS_IDLE',
    'STATUS_LOCKED',
    'STATUS_RUNNING',
    'STATUS_SLEEPING',
    'STATUS_STOPPED',
    'STATUS_SUSPENDED',
    'STATUS_TRACING_STOP',
    'STATUS_WAITING',
    'STATUS_WAKE_KILL',
    'STATUS_WAKING',
    'STATUS_ZOMBIE',
    'STATUS_PARKED',
    'ENCODING',
    'ENCODING_ERRS',
    'AF_INET6',
    'pconn',
    'pcputimes',
    'pctxsw',
    'pgids',
    'pio',
    'pionice',
    'popenfile',
    'pthread',
    'puids',
    'sconn',
    'scpustats',
    'sdiskio',
    'sdiskpart',
    'sdiskusage',
    'snetio',
    'snicaddr',
    'snicstats',
    'sswap',
    'suser',
    'conn_tmap',
    'deprecated_method',
    'isfile_strict',
    'memoize',
    'parse_environ_block',
    'path_exists_strict',
    'usage_percent',
    'supports_ipv6',
    'sockfam_to_enum',
    'socktype_to_enum',
    'wrap_numbers',
    'open_text',
    'open_binary',
    'cat',
    'bcat',
    'bytes2human',
    'conn_to_ntuple',
    'debug',
    'hilite',
    'term_supports_colors',
    'print_color']
POSIX = os.name == 'posix'
WINDOWS = os.name == 'nt'
LINUX = sys.platform.startswith('linux')
MACOS = sys.platform.startswith('darwin')
OSX = MACOS
FREEBSD = sys.platform.startswith(('freebsd', 'midnightbsd'))
OPENBSD = sys.platform.startswith('openbsd')
NETBSD = sys.platform.startswith('netbsd')
# WARNING: Decompyle incomplete
