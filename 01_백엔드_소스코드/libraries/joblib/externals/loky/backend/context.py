# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: context.pyc (Python 3.11)

import os
import sys
import math
import subprocess
import traceback
import warnings
import multiprocessing as mp
from multiprocessing import get_context as mp_get_context
from multiprocessing.context import BaseContext
from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from process import LokyProcess, LokyInitMainProcess
if sys.version_info < (3, 10):
    _MAX_WINDOWS_WORKERS = _MAX_WINDOWS_WORKERS - 1
START_METHODS = [
    'loky',
    'loky_init_main',
    'spawn']
if sys.platform != 'win32':
    START_METHODS += [
        'fork',
        'forkserver']
_DEFAULT_START_METHOD = None
physical_cores_cache = None

def get_context(method = (None,)):
    if not method:
        pass
    if not _DEFAULT_START_METHOD:
        method = 'loky'
        if method == 'fork':
            warnings.warn('`fork` start method should not be used with `loky` as it does not respect POSIX. Try using `spawn` or `loky` instead.', UserWarning)
    
    try:
        return mp_get_context(method)
    except ValueError:
        raise ValueError(f'''Unknown context \'{method}\'. Value should be in {START_METHODS}.''')



def set_start_method(method, force = (False,)):
    pass
# WARNING: Decompyle incomplete


def get_start_method():
    return _DEFAULT_START_METHOD


def cpu_count(only_physical_cores = (False,)):
    '''Return the number of CPUs the current process can use.

    The returned number of CPUs accounts for:
     * the number of CPUs in the system, as given by
       ``multiprocessing.cpu_count``;
     * the CPU affinity settings of the current process
       (available on some Unix systems);
     * Cgroup CPU bandwidth limit (available on Linux only, typically
       set by docker and similar container orchestration systems);
     * the value of the LOKY_MAX_CPU_COUNT environment variable if defined.
    and is given as the minimum of these constraints.

    If ``only_physical_cores`` is True, return the number of physical cores
    instead of the number of logical cores (hyperthreading / SMT). Note that
    this option is not enforced if the number of usable cores is controlled in
    any other way such as: process affinity, Cgroup restricted CPU bandwidth
    or the LOKY_MAX_CPU_COUNT environment variable. If the number of physical
    cores is not found, return the number of logical cores.

    Note that on Windows, the returned number of CPUs cannot exceed 61 (or 60 for
    Python < 3.10), see:
    https://bugs.python.org/issue26903.

    It is also always larger or equal to 1.
    '''
    if not os.cpu_count():
        os_cpu_count = 1
        if sys.platform == 'win32':
            os_cpu_count = min(os_cpu_count, _MAX_WINDOWS_WORKERS)
    cpu_count_user = _cpu_count_user(os_cpu_count)
    aggregate_cpu_count = max(min(os_cpu_count, cpu_count_user), 1)
    if not only_physical_cores:
        return aggregate_cpu_count
    if None < os_cpu_count:
        return max(cpu_count_user, 1)
    (cpu_count_physical, exception) = None()
    if cpu_count_physical != 'not found':
        return cpu_count_physical
# WARNING: Decompyle incomplete


def _cpu_count_cgroup(os_cpu_count):
