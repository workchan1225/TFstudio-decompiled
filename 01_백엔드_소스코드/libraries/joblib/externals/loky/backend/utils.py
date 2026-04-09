# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import os
import sys
import time
import errno
import signal
import warnings
import subprocess
import traceback

try:
    import psutil
except ImportError:
    psutil = None


def kill_process_tree(process, use_psutil = (True,)):
    '''Terminate process and its descendants with SIGKILL'''
    pass
# WARNING: Decompyle incomplete


def recursive_terminate(process, use_psutil = (True,)):
    warnings.warn('recursive_terminate is deprecated in loky 3.2, use kill_process_treeinstead', DeprecationWarning)
    kill_process_tree(process, use_psutil = use_psutil)


def _kill_process_tree_with_psutil(process):
    
    try:
        descendants = psutil.Process(process.pid).children(recursive = True)
    except psutil.NoSuchProcess:
        return None

    for descendant in descendants[::-1]:
        descendant.kill()
        except psutil.NoSuchProcess:
            continue
        
        try:
            psutil.Process(process.pid).kill()
        except psutil.NoSuchProcess:
            pass

        process.join()
        return None


def _kill_process_tree_without_psutil(process):
    '''Terminate a process and its descendants.'''
    
    try:
        if sys.platform == 'win32':
            _windows_taskkill_process_tree(process.pid)
        else:
            _posix_recursive_kill(process.pid)
    except Exception:
        details = traceback.format_exc()
        warnings.warn(f'''Failed to kill subprocesses on this platform. Please installpsutil: https://github.com/giampaolo/psutil\nDetails:\n{details}''')
        process.kill()

    process.join()


def _windows_taskkill_process_tree(pid):
    
    try:
        subprocess.check_output([
            'taskkill',
            '/F',
            '/T',
            '/PID',
            str(pid)], stderr = None)
        return None
    except subprocess.CalledProcessError:
        e = None
        if e.returncode not in (128, 255):
            raise 
        e = None
        del e
        return None
        e = None
        del e



def _kill(pid):
    kill_signal = getattr(signal, 'SIGKILL', signal.SIGTERM)
    
    try:
        os.kill(pid, kill_signal)
        return None
    except OSError:
        e = None
        if e.errno != errno.ESRCH:
            raise 
        e = None
        del e
        return None
        e = None
        del e



def _posix_recursive_kill(pid):
    '''Recursively kill the descendants of a process before killing it.'''
    
    try:
        children_pids = subprocess.check_output([
            'pgrep',
            '-P',
            str(pid)], stderr = None, text = True)
    except subprocess.CalledProcessError:
        e = None
        if e.returncode == 1:
            children_pids = ''
        else:
            raise 
        e = None
        del e
    except:
        e = None
        del e

    for cpid in children_pids.splitlines():
        cpid = int(cpid)
        _posix_recursive_kill(cpid)
        _kill(pid)
        return None


def get_exitcodes_terminated_worker(processes):
    '''Return a formatted string with the exitcodes of terminated workers.

    If necessary, wait (up to .25s) for the system to correctly set the
    exitcode of one terminated worker.
    '''
    patience = 5
    exitcodes = list(processes.values())()
# WARNING: Decompyle incomplete


def _format_exitcodes(exitcodes):
    '''Format a list of exit code with names of the signals if possible'''
    str_exitcodes = exitcodes()
    return '{' + ', '.join(str_exitcodes) + '}'


def _get_exitcode_name(exitcode):
    if sys.platform == 'win32':
        return 'UNKNOWN'
    if None < 0:
        
        try:
            import signal
            return signal.Signals(-exitcode).name
        except ValueError:
            return 'UNKNOWN'
            if exitcode != 255:
                return 'EXIT'
            return None
