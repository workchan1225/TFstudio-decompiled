# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: spawn.pyc (Python 3.11)

import os
import sys
import runpy
import types
from  import get_start_method, set_start_method
from  import process
from context import reduction
from  import util
__all__ = [
    '_main',
    'freeze_support',
    'set_executable',
    'get_executable',
    'get_preparation_data',
    'get_command_line',
    'import_main_path']
if sys.platform != 'win32':
    WINEXE = False
    WINSERVICE = False
else:
    WINEXE = getattr(sys, 'frozen', False)
    if sys.executable:
        WINSERVICE = sys.executable.lower().endswith('pythonservice.exe')
        
        def set_executable(exe):
            pass
        # WARNING: Decompyle incomplete

        
        def get_executable():
            return _python_exe

        if WINSERVICE:
            set_executable(os.path.join(sys.exec_prefix, 'python.exe'))
        else:
            set_executable(sys.executable)

def is_forking(argv):
    '''
    Return whether commandline indicates we are forking
    '''
    if len(argv) >= 2 and argv[1] == '--multiprocessing-fork':
        return True


def freeze_support():
    '''
    Run code for process object if this in not the main process
    '''
    pass
# WARNING: Decompyle incomplete


def get_command_line(**kwds):
    '''
    Returns prefix of command line used for spawning a child process
    '''
    if getattr(sys, 'frozen', False):
        return (lambda .0: [ '%s=%r' % item for item in .0 ]) + kwds.items()()
    prog = None
    ', '.join %= (lambda .0: pass# WARNING: Decompyle incomplete
)(kwds.items()())
    opts = util._args_from_interpreter_flags()
    exe = get_executable()
    return [
        exe] + opts + [
        '-c',
        prog,
        '--multiprocessing-fork']


def spawn_main(pipe_handle, parent_pid, tracker_fd = (None, None)):
    '''
    Run code specified by data received over pipe
    '''
    pass
# WARNING: Decompyle incomplete


def _main(fd, parent_sentinel):
