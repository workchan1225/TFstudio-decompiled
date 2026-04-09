# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: resource_tracker.pyc (Python 3.11)

import os
import signal
import sys
import threading
import warnings
from  import spawn
from  import util
__all__ = [
    'ensure_running',
    'register',
    'unregister']
_HAVE_SIGMASK = hasattr(signal, 'pthread_sigmask')
_IGNORED_SIGNALS = (signal.SIGINT, signal.SIGTERM)
_CLEANUP_FUNCS = {
    'noop': (lambda : pass) }
if os.name == 'posix':
    import _multiprocessing
    import _posixshmem
    if hasattr(_multiprocessing, 'sem_unlink'):
        _CLEANUP_FUNCS.update({
            'semaphore': _multiprocessing.sem_unlink })
    _CLEANUP_FUNCS.update({
        'shared_memory': _posixshmem.shm_unlink })

class ReentrantCallError(RuntimeError):
    pass


class ResourceTracker(object):
    
    def __init__(self):
        self._lock = threading.RLock()
        self._fd = None
        self._pid = None

    
    def _reentrant_call_error(self):
        raise ReentrantCallError('Reentrant call into the multiprocessing resource tracker')

    
    def _stop(self):
        self._lock
        if self._lock._recursion_count() > 1:
            None(None, None)
            return 
    # WARNING: Decompyle incomplete

    
    def getfd(self):
        self.ensure_running()
        return self._fd

    
    def ensure_running(self):
        '''Make sure that resource tracker process is running.

        This can be run from any process.  Usually a child process will use
        the resource created by its parent.'''
        self._lock
        if self._lock._recursion_count() > 1:
            None(None, None)
            return 
    # WARNING: Decompyle incomplete

    
    def _check_alive(self):
        '''Check that the pipe has not been closed by sending a probe.'''
        
        try:
            os.write(self._fd, b'PROBE:0:noop\n')
            return True
        except OSError:
            return False


    
    def register(self, name, rtype):
        '''Register name of resource with resource tracker.'''
        self._send('REGISTER', name, rtype)

    
    def unregister(self, name, rtype):
        '''Unregister name of resource with resource tracker.'''
        self._send('UNREGISTER', name, rtype)

    
    def _send(self, cmd, name, rtype):
        
        try:
            self.ensure_running()
        except ReentrantCallError:
            warnings.warn(f'''ResourceTracker called reentrantly for resource cleanup, which is unsupported. The {rtype} object {name!r} might leak.''')

        msg = '{0}:{1}:{2}\n'.format(cmd, name, rtype).encode('ascii')
        if len(msg) > 512:
            raise ValueError('msg too long')
        nbytes = os.write(self._fd, msg)
    # WARNING: Decompyle incomplete


_resource_tracker = ResourceTracker()
ensure_running = _resource_tracker.ensure_running
register = _resource_tracker.register
unregister = _resource_tracker.unregister
getfd = _resource_tracker.getfd

def main(fd):
    '''Run resource tracker.'''
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    if _HAVE_SIGMASK:
        signal.pthread_sigmask(signal.SIG_UNBLOCK, _IGNORED_SIGNALS)
# WARNING: Decompyle incomplete
