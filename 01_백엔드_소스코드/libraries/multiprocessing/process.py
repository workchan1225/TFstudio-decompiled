# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: process.pyc (Python 3.11)

__all__ = [
    'BaseProcess',
    'current_process',
    'active_children',
    'parent_process']
import os
import sys
import signal
import itertools
import threading
from _weakrefset import WeakSet

try:
    ORIGINAL_DIR = os.path.abspath(os.getcwd())
except OSError:
    ORIGINAL_DIR = None


def current_process():
    '''
    Return process object representing the current process
    '''
    return _current_process


def active_children():
    '''
    Return list of process objects corresponding to live child processes
    '''
    _cleanup()
    return list(_children)


def parent_process():
    '''
    Return process object representing the parent process
    '''
    return _parent_process


def _cleanup():
    pass
# WARNING: Decompyle incomplete


class BaseProcess(object):
    '''
    Process objects represent activity that is run in a separate process

    The class is analogous to `threading.Thread`
    '''
    
    def _Popen(self):
        raise NotImplementedError

    
    def __init__(self, group, target, name = None, args = (None, None, None, (), { }), kwargs = {
        'daemon': None }, *, daemon):
        pass
    # WARNING: Decompyle incomplete

    
    def _check_closed(self):
        if self._closed:
            raise ValueError('process object is closed')

    
    def run(self):
        '''
        Method to be run in sub-process; can be overridden in sub-class
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def start(self):
        '''
        Start child process
        '''
        self._check_closed()
    # WARNING: Decompyle incomplete

    
    def terminate(self):
        '''
        Terminate process; sends SIGTERM signal or uses TerminateProcess()
        '''
        self._check_closed()
        self._popen.terminate()

    
    def kill(self):
        '''
        Terminate process; sends SIGKILL signal or uses TerminateProcess()
        '''
        self._check_closed()
        self._popen.kill()

    
    def join(self, timeout = (None,)):
        '''
        Wait until child process terminates
        '''
        self._check_closed()
    # WARNING: Decompyle incomplete

    
    def is_alive(self):
        '''
        Return whether process is alive
        '''
        self._check_closed()
        if self is _current_process:
            return True
    # WARNING: Decompyle incomplete

    
    def close(self):
        '''
        Close the Process object.

        This method releases resources held by the Process object.  It is
        an error to call this method if the child process is still running.
        '''
        pass
    # WARNING: Decompyle incomplete

    name = (lambda self: self._name)()
    name = (lambda self, name: pass# WARNING: Decompyle incomplete
)()
    daemon = (lambda self: self._config.get('daemon', False))()
    daemon = (lambda self, daemonic: pass# WARNING: Decompyle incomplete
)()
    authkey = (lambda self: self._config['authkey'])()
    authkey = (lambda self, authkey: self._config['authkey'] = AuthenticationString(authkey))()
    exitcode = (lambda self: self._check_closed()# WARNING: Decompyle incomplete
)()
    ident = (lambda self:
