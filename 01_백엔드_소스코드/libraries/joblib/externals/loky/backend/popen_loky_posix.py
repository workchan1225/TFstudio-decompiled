# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: popen_loky_posix.pyc (Python 3.11)

import os
import sys
import signal
import pickle
from io import BytesIO
from multiprocessing import util, process
from multiprocessing.connection import wait
from multiprocessing.context import set_spawning_popen
from  import reduction, resource_tracker, spawn
__all__ = [
    'Popen']

class _DupFd:
    
    def __init__(self, fd):
        self.fd = reduction._mk_inheritable(fd)

    
    def detach(self):
        return self.fd



class Popen:
    method = 'loky'
    DupFd = _DupFd
    
    def __init__(self, process_obj):
        sys.stdout.flush()
        sys.stderr.flush()
        self.returncode = None
        self._fds = []
        self._launch(process_obj)

    
    def duplicate_for_child(self, fd):
        self._fds.append(fd)
        return reduction._mk_inheritable(fd)

    
    def poll(self, flag = (os.WNOHANG,)):
        pass
    # WARNING: Decompyle incomplete

    
    def wait(self, timeout = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def terminate(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _launch(self, process_obj):
        tracker_fd = resource_tracker._resource_tracker.getfd()
        fp = BytesIO()
        set_spawning_popen(self)
        
        try:
            prep_data = spawn.get_preparation_data(process_obj._name, getattr(process_obj, 'init_main_module', True))
            reduction.dump(prep_data, fp)
            reduction.dump(process_obj, fp)
            set_spawning_popen(None)
        except:
            set_spawning_popen(None)

    # WARNING: Decompyle incomplete

    thread_is_spawning = (lambda : True)()

# WARNING: Decompyle incomplete
