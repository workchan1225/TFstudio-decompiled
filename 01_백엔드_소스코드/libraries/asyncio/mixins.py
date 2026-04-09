# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mixins.pyc (Python 3.11)

'''Event loop mixins.'''
import threading
from  import events
_global_lock = threading.Lock()

class _LoopBoundMixin:
    _loop = None
    
    def _get_loop(self):
        loop = events._get_running_loop()
    # WARNING: Decompyle incomplete
