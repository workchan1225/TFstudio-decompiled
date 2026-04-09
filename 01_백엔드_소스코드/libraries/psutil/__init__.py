# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''psutil is a cross-platform library for retrieving information on
running processes and system utilization (CPU, memory, disks, network,
sensors) in Python. Supported platforms:

 - Linux
 - Windows
 - macOS
 - FreeBSD
 - OpenBSD
 - NetBSD
 - Sun Solaris
 - AIX

Supported Python versions are cPython 3.6+ and PyPy.
'''
import collections
import contextlib
import datetime
import functools
import os
import signal
import socket
import subprocess
import sys
import threading
import time

try:
    import pwd
except ImportError:
    pwd = None

from  import _common
from _common import AIX
from _common import BSD
from _common import CONN_CLOSE
from _common import CONN_CLOSE_WAIT
from _common import CONN_CLOSING
from _common import CONN_ESTABLISHED
from _common import CONN_FIN_WAIT1
from _common import CONN_FIN_WAIT2
from _common import CONN_LAST_ACK
from _common import CONN_LISTEN
from _common import CONN_NONE
from _common import CONN_SYN_RECV
from _common import CONN_SYN_SENT
from _common import CONN_TIME_WAIT
from _common import FREEBSD
from _common import LINUX
from _common import MACOS
from _common import NETBSD
from _common import NIC_DUPLEX_FULL
from _common import NIC_DUPLEX_HALF
from _common import NIC_DUPLEX_UNKNOWN
from _common import OPENBSD
from _common import OSX
from _common import POSIX
from _common import POWER_TIME_UNKNOWN
from _common import POWER_TIME_UNLIMITED
from _common import STATUS_DEAD
from _common import STATUS_DISK_SLEEP
from _common import STATUS_IDLE
from _common import STATUS_LOCKED
from _common import STATUS_PARKED
from _common import STATUS_RUNNING
from _common import STATUS_SLEEPING
from _common import STATUS_STOPPED
from _common import STATUS_TRACING_STOP
from _common import STATUS_WAITING
from _common import STATUS_WAKING
from _common import STATUS_ZOMBIE
from _common import SUNOS
from _common import WINDOWS
from _common import AccessDenied
from _common import Error
from _common import NoSuchProcess
from _common import TimeoutExpired
from _common import ZombieProcess
from _common import debug
from _common import memoize_when_activated
from _common import wrap_numbers as _wrap_numbers
if LINUX:
    PROCFS_PATH = '/proc'
    from  import _pslinux as _psplatform
    from _pslinux import IOPRIO_CLASS_BE
    from _pslinux import IOPRIO_CLASS_IDLE
    from _pslinux import IOPRIO_CLASS_NONE
    from _pslinux import IOPRIO_CLASS_RT
elif WINDOWS:
    from  import _pswindows as _psplatform
    from _psutil_windows import ABOVE_NORMAL_PRIORITY_CLASS
    from _psutil_windows import BELOW_NORMAL_PRIORITY_CLASS
    from _psutil_windows import HIGH_PRIORITY_CLASS
    from _psutil_windows import IDLE_PRIORITY_CLASS
    from _psutil_windows import NORMAL_PRIORITY_CLASS
    from _psutil_windows import REALTIME_PRIORITY_CLASS
    from _pswindows import CONN_DELETE_TCB
    from _pswindows import IOPRIO_HIGH
    from _pswindows import IOPRIO_LOW
    from _pswindows import IOPRIO_NORMAL
    from _pswindows import IOPRIO_VERYLOW
elif MACOS:
    from  import _psosx as _psplatform
elif BSD:
    from  import _psbsd as _psplatform
elif SUNOS:
    from  import _pssunos as _psplatform
    from _pssunos import CONN_BOUND
    from _pssunos import CONN_IDLE
    PROCFS_PATH = '/proc'
elif AIX:
    from  import _psaix as _psplatform
    PROCFS_PATH = '/proc'
else:
    msg = f'''platform {sys.platform} is not supported'''
    raise NotImplementedError(msg)
__all__ = [
    'Error',
    'NoSuchProcess',
    'ZombieProcess',
    'AccessDenied',
    'TimeoutExpired',
    'version_info',
    '__version__',
    'STATUS_RUNNING',
    'STATUS_IDLE',
    'STATUS_SLEEPING',
    'STATUS_DISK_SLEEP',
    'STATUS_STOPPED',
    'STATUS_TRACING_STOP',
    'STATUS_ZOMBIE',
    'STATUS_DEAD',
    'STATUS_WAKING',
    'STATUS_LOCKED',
    'STATUS_WAITING',
    'STATUS_LOCKED',
    'STATUS_PARKED',
    'CONN_ESTABLISHED',
    'CONN_SYN_SENT',
    'CONN_SYN_RECV',
    'CONN_FIN_WAIT1',
    'CONN_FIN_WAIT2',
    'CONN_TIME_WAIT',
    'CONN_CLOSE',
    'CONN_CLOSE_WAIT',
    'CONN_LAST_ACK',
    'CONN_LISTEN',
    'CONN_CLOSING',
    'CONN_NONE',
    'AF_LINK',
    'NIC_DUPLEX_FULL',
    'NIC_DUPLEX_HALF',
    'NIC_DUPLEX_UNKNOWN',
    'POWER_TIME_UNKNOWN',
    'POWER_TIME_UNLIMITED',
    'BSD',
    'FREEBSD',
    'LINUX',
    'NETBSD',
    'OPENBSD',
    'MACOS',
    'OSX',
    'POSIX',
    'SUNOS',
    'WINDOWS',
    'AIX',
    'Process',
    'Popen',
    'pid_exists',
    'pids',
    'process_iter',
    'wait_procs',
    'virtual_memory',
    'swap_memory',
    'cpu_times',
    'cpu_percent',
    'cpu_times_percent',
    'cpu_count',
    'cpu_stats',
    'net_io_counters',
    'net_connections',
    'net_if_addrs',
    'net_if_stats',
    'disk_io_counters',
    'disk_partitions',
    'disk_usage',
    'users',
    'boot_time']
__all__.extend(_psplatform.__extra__all__)
if hasattr(_psplatform.Process, 'rlimit'):
    _globals = globals()
    _name = None
    for _name in dir(_psplatform.cext):
        if _name.startswith('RLIM') and _name.isupper():
            _globals[_name] = getattr(_psplatform.cext, _name)
            __all__.append(_name)
        del _globals
        del _name
        AF_LINK = _psplatform.AF_LINK
        __author__ = "Giampaolo Rodola'"
        __version__ = '7.1.3'
        version_info = (lambda .0: pass# WARNING: Decompyle incomplete
)(__version__.split('.')())
        _timer = getattr(time, 'monotonic', time.time)
        _TOTAL_PHYMEM = None
        _LOWEST_PID = None
        _SENTINEL = object()
        if int(__version__.replace('.', '')) != getattr(_psplatform.cext, 'version', None):
            msg = f'''version conflict: {_psplatform.cext.__file__!r} C extension '''
            msg += 'module was built for another version of psutil'
            what = getattr(_psplatform.cext, '__file__', 'the existing psutil install directory')
            msg += f'''; you may try to \'pip uninstall psutil\', manually remove {what}'''
            msg += ' or clean the virtual env somehow, then reinstall'
            raise ImportError(msg)

def _pprint_secs(secs):
    '''Format seconds in a human readable form.'''
    now = time.time()
    secs_ago = int(now - secs)
    fmt = '%H:%M:%S' if secs_ago < 86400 else '%Y-%m-%d %H:%M:%S'
    return datetime.datetime.fromtimestamp(secs).strftime(fmt)


def _check_conn_kind(kind):
    """Check net_connections()'s `kind` parameter."""
    kinds = tuple(_common.conn_tmap)
    if kind not in kinds:
        msg = f'''invalid kind argument {kind!r}; valid ones are: {kinds}'''
        raise ValueError(msg)


class Process:
    '''Represents an OS process with the given PID.
    If PID is omitted current process PID (os.getpid()) is used.
    Raise NoSuchProcess if PID does not exist.

    Note that most of the methods of this class do not make sure that
    the PID of the process being queried has been reused. That means
    that you may end up retrieving information for another process.

    The only exceptions for which process identity is pre-emptively
    checked and guaranteed are:

     - parent()
     - children()
     - nice() (set)
     - ionice() (set)
     - rlimit() (set)
     - cpu_affinity (set)
     - suspend()
     - resume()
     - send_signal()
     - terminate()
     - kill()

    To prevent this problem for all other methods you can use
    is_running() before querying the process.
    '''
    
    def __init__(self, pid = (None,)):
        self._init(pid)

    
    def _init(self, pid, _ignore_nsp = (False,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_ident(self):
        """Return a (pid, uid) tuple which is supposed to identify a
        Process instance univocally over time. The PID alone is not
        enough, as it can be assigned to a new process after this one
        terminates, so we add process creation time to the mix. We need
        this in order to prevent killing the wrong process later on.
        This is also known as PID reuse or PID recycling problem.

        The reliability of this strategy mostly depends on
        create_time() precision, which is 0.01 secs on Linux. The
        assumption is that, after a process terminates, the kernel
        won't reuse the same PID after such a short period of time
        (0.01 secs). Technically this is inherently racy, but
        practically it should be good enough.

        NOTE: unreliable on FreeBSD and OpenBSD as ctime is subject to
        system clock updates.
        """
        if WINDOWS:
            self._create_time = self._proc.create_time(fast_only = True)
            return (self.pid, self._create_time)
        if None and NETBSD or OSX:
            return (self.pid, self._proc.create_time(monotonic = True))
        return (None.pid, self.create_time())

    
    def __str__(self):
        info = collections.OrderedDict()
        info['pid'] = self.pid
        if self._name:
            info['name'] = self._name
        self.oneshot()
        if self._pid_reused:
            info['status'] = 'terminated + PID reused'
        else:
            info['name'] = self.name()
            info['status'] = self.status()
        except ZombieProcess:
            info['status'] = 'zombie'
        except NoSuchProcess:
            info['status'] = 'terminated'
        except AccessDenied:
            pass
        if self._exitcode not in {
            _SENTINEL,
            None}:
            info['exitcode'] = self._exitcode
    # WARNING: Decompyle incomplete

    __repr__ = __str__
    
    def __eq__(self, other):
