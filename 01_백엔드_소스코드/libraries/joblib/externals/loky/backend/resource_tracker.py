# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: resource_tracker.pyc (Python 3.11)

import os
import shutil
import sys
import signal
import warnings
from multiprocessing import util
from multiprocessing.resource_tracker import ResourceTracker as _ResourceTracker
from  import spawn
if sys.platform == 'win32':
    import _winapi
    import msvcrt
    from multiprocessing.reduction import duplicate
__all__ = [
    'ensure_running',
    'register',
    'unregister']
_HAVE_SIGMASK = hasattr(signal, 'pthread_sigmask')
_IGNORED_SIGNALS = (signal.SIGINT, signal.SIGTERM)

def cleanup_noop(name):
    raise RuntimeError('noop should never be registered or cleaned up')

_CLEANUP_FUNCS = {
    'noop': cleanup_noop,
    'folder': shutil.rmtree,
    'file': os.unlink }
if os.name == 'posix':
    import _multiprocessing
    if hasattr(_multiprocessing, 'sem_unlink'):
        _CLEANUP_FUNCS.update({
            'semlock': _multiprocessing.sem_unlink })
VERBOSE = False

class ResourceTracker(_ResourceTracker):
    pass
# WARNING: Decompyle incomplete

_resource_tracker = ResourceTracker()
ensure_running = _resource_tracker.ensure_running
register = _resource_tracker.register
maybe_unlink = _resource_tracker.maybe_unlink
unregister = _resource_tracker.unregister
getfd = _resource_tracker.getfd

def main(fd, verbose = (0,)):
    '''Run resource tracker.'''
    pass
# WARNING: Decompyle incomplete


def spawnv_passfds(path, args, passfds):
    if sys.platform != 'win32':
        args = args()
        path = path.encode('utf-8')
        return util.spawnv_passfds(path, args, passfds)
    passfds = None(passfds)
    cmd = (lambda .0: pass# WARNING: Decompyle incomplete
)(args())
    
    try:
        (_, ht, pid, _) = _winapi.CreateProcess(path, cmd, None, None, True, 0, None, None, None)
        _winapi.CloseHandle(ht)
    except BaseException:
        pass

    return pid
