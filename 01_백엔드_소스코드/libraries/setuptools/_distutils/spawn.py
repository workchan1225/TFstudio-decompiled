# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: spawn.pyc (Python 3.11)

"""distutils.spawn

Provides the 'spawn()' function, a front-end to various platform-
specific functions for launching another program in a sub-process.
Also provides the 'find_executable()' to search the path for a given
executable name.
"""
import sys
import os
import subprocess
from distutils.errors import DistutilsExecError
from distutils.debug import DEBUG
from distutils import log

def spawn(cmd, search_path, verbose, dry_run, env = (1, 0, 0, None)):
    """Run another program, specified as a command list 'cmd', in a new process.

    'cmd' is just the argument list for the new process, ie.
    cmd[0] is the program to run and cmd[1:] are the rest of its arguments.
    There is no way to run a program with a name different from that of its
    executable.

    If 'search_path' is true (the default), the system's executable
    search path will be used to find the program; otherwise, cmd[0]
    must be the exact path to the executable.  If 'dry_run' is true,
    the command will not actually be run.

    Raise DistutilsExecError if running the program fails in any way; just
    return on success.
    """
    cmd = list(cmd)
    log.info(subprocess.list2cmdline(cmd))
    if dry_run:
        return None
# WARNING: Decompyle incomplete


def find_executable(executable, path = (None,)):
    """Tries to find 'executable' in the directories listed in 'path'.

    A string listing directories separated by 'os.pathsep'; defaults to
    os.environ['PATH'].  Returns the complete filename or None if not found.
    """
    (_, ext) = os.path.splitext(executable)
    if sys.platform == 'win32' and ext != '.exe':
        executable = executable + '.exe'
    if os.path.isfile(executable):
        return executable
# WARNING: Decompyle incomplete
