# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dprocess.pyc (Python 3.11)

import atexit
import logging
import multiprocessing
import os
import platform
import signal
from subprocess import PIPE
from subprocess import Popen
import sys
CREATE_NEW_PROCESS_GROUP = 512
DETACHED_PROCESS = 8
REGISTERED = []

def start_detached(executable, *args):
    """
    Starts a fully independent subprocess (with no parent)
    :param executable: executable
    :param args: arguments to the executable, eg: ['--param1_key=param1_val', '-vvv' ...]
    :return: pid of the grandchild process
    """
    (reader, writer) = multiprocessing.Pipe(False)
# WARNING: Decompyle incomplete


def _start_detached(executable = None, *, writer, *args):
    kwargs = { }
    if platform.system() == 'Windows':
        kwargs.update(creationflags = DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
    elif sys.version_info < (3, 2):
        kwargs.update(preexec_fn = os.setsid)
    else:
        kwargs.update(start_new_session = True)
# WARNING: Decompyle incomplete


def _cleanup():
    for pid in REGISTERED:
        logging.getLogger(__name__).debug('cleaning up pid %d ' % pid)
        os.kill(pid, signal.SIGTERM)
        return None

atexit.register(_cleanup)
